#!/usr/bin/env python3
"""make_figures.py — produces figs.json for the Method page

Runs the three pipeline stages on real pages of Combate and stores the
resulting images (as base64 JPEG data URIs) and numbers, so that the
Method page shows what the code actually does rather than a description.

Usage:
    python3 make_figures.py /path/to/repository        # writes figs.json
Needs: pypdfium2, opencv-python-headless, numpy, pytesseract, and the
Tesseract binary with its Portuguese model (tesseract-ocr-por).
"""
import sys, json, base64, pathlib
import cv2, numpy as np, pypdfium2 as pdfium

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "pipeline"))
from rasterise import render_page
from segment import (segment_page, binarise, remove_rules, clear_border, text_mask)
from ocr import read_page, clean, deskew, mask_graphics

REPO = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "../repo")
PDF = REPO / "Combate_Newsfiles"
YELLOW = (0, 213, 255)          # BGR

def b64(img, q=62):
    ok, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, q])
    return "data:image/jpeg;base64," + base64.b64encode(buf).decode()

def fit(img, w):
    h = int(img.shape[0] * w / img.shape[1])
    return cv2.resize(img, (w, h), interpolation=cv2.INTER_AREA)

def page(year, issue, index):
    doc = pdfium.PdfDocument(str(PDF / f"Y{year}" / f"{issue}.pdf"))
    pts = doc[index].get_size()
    g = render_page(doc, index)
    doc.close()
    return g, pts

def overlay(g, regs, width, thick=(10, 6)):
    vis = cv2.cvtColor(g, cv2.COLOR_GRAY2BGR); H, W = g.shape
    for r in regs:
        x, y, w, h = r["box"]
        p1, p2 = (int(x * W), int(y * H)), (int((x + w) * W), int((y + h) * H))
        cv2.rectangle(vis, p1, p2, (0, 0, 0), thick[0])
        cv2.rectangle(vis, p1, p2, YELLOW, thick[1])
    return fit(vis, width)

FIG = {}
g, pts = page(1974, 1, 2)                     # issue 1, page 3
H, W = g.shape

# hero and stage 2
FIG["hero"] = b64(overlay(g, segment_page(g)[0], 720, (12, 7)), 60)
FIG["ras_page"] = b64(fit(g, 520), 58)
py, px = int(0.672 * H), int(0.29 * W)        # the C of COMUNISTA
patch = g[py:py + 14, px:px + 22]
FIG["ras_patch"] = b64(cv2.resize(patch, (22 * 14, 14 * 14), interpolation=cv2.INTER_NEAREST), 80)
FIG["ras_patch_ctx"] = b64(fit(g[py - 40:py + 54, px - 60:px + 82], 420), 70)
patch_values = patch[:8, :14].tolist()

# stage 3, the five moves
ink = clear_border(remove_rules(binarise(g)))
text = text_mask(ink, g)
regs, _, _ = segment_page(g)
FIG["seg_grey"] = b64(fit(g, 360), 55)
FIG["seg_ink"] = b64(fit(255 - ink, 360), 55)
FIG["seg_text"] = b64(fit(255 - text, 360), 55)
FIG["seg_rest"] = b64(fit(255 - cv2.subtract(ink, text), 360), 55)
FIG["seg_boxes"] = b64(overlay(g, regs, 360), 58)

extra = []
for year, issue, index in [(1976, 47, 0), (1975, 20, 4), (1974, 6, 6)]:
    gg, _ = page(year, issue, index)
    rr, _, _ = segment_page(gg)
    extra.append({"issue": issue, "page": index + 1, "label": f"Issue {issue}, page {index + 1}",
                  "img": b64(overlay(gg, rr, 360, (8, 5)), 55), "n": len(rr),
                  "types": sorted(set(r["type"] for r in rr))})

# stage 4
cl = mask_graphics(clean(deskew(g)), regs)
y0, y1, x0, x1 = int(0.135 * H), int(0.30 * H), int(0.055 * W), int(0.245 * W)
FIG["ocr_raw"] = b64(fit(g[y0:y1, x0:x1], 380), 70)
FIG["ocr_clean"] = b64(fit(cl[y0:y1, x0:x1], 380), 70)
txt, conf, _ = read_page(g, regs)
lines = [l for l in txt.split("\n") if l.strip()]
i = next(i for i, l in enumerate(lines) if l.startswith("As Forças"))
sample = "\n".join(lines[i:i + 12])

json.dump({"FIG": FIG, "patch": patch_values, "regions": regs, "extra": extra,
           "ocr": sample, "conf": round(conf), "words": len(txt.split()),
           "pts": pts, "px": [W, H]}, open(HERE / "figs.json", "w"))
print("figs.json written;", round(sum(len(v) for v in FIG.values()) / 1024), "KB of figures")
