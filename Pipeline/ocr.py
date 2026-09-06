"""ocr.py — COMBAT project, stage 4

Read the printed text of a page with Tesseract, after masking the
graphic regions found in stage 3 and cleaning the scan. Handwritten
facsimiles are skipped here: they go to a separate HTR model.

Usage:
    python3 ocr.py out/pages regions.json text/
"""
import sys, pathlib, json
import numpy as np
import cv2
import pytesseract
from segment import binarise, remove_rules

def deskew(grey):
    """Estimate the tilt of the text lines from the ink and rotate the
    page back to horizontal. Scans of a folded newspaper are rarely
    straight; even one degree costs Tesseract whole words."""
    ink = binarise(grey)
    coords = np.column_stack(np.where(ink > 0))
    angle = cv2.minAreaRect(coords[:, ::-1].astype(np.float32))[-1]
    if angle > 45: angle -= 90
    if abs(angle) > 5: return grey            # not text tilt, leave it
    H, W = grey.shape
    M = cv2.getRotationMatrix2D((W / 2, H / 2), angle, 1.0)
    return cv2.warpAffine(grey, M, (W, H), flags=cv2.INTER_CUBIC,
                          borderMode=cv2.BORDER_REPLICATE)

def clean(grey):
    """Denoise, even out the exposure, and stretch the contrast so that
    grey ink on grey paper becomes black on white."""
    den = cv2.fastNlMeansDenoising(grey, None, h=9, templateWindowSize=7,
                                   searchWindowSize=21)
    bg = cv2.medianBlur(den, 41)               # the paper tone, locally
    flat = cv2.divide(den, bg, scale=255)      # remove uneven lighting
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(flat)

def mask_graphics(grey, regions):
    """Paint every graphic region white so that captions inside a
    drawing are not read as body text."""
    H, W = grey.shape
    out = grey.copy()
    for r in regions:
        x, y, w, h = r["box"]
        cv2.rectangle(out, (int(x * W), int(y * H)),
                      (int((x + w) * W), int((y + h) * H)), 255, -1)
    return out

def read_page(grey, regions):
    """Returns the recognised text and Tesseract's word-level data.
    --psm 3 lets Tesseract find the columns itself; the page has no
    grid we could hand it. Language: Portuguese."""
    img = mask_graphics(clean(deskew(grey)), regions)
    config = "--oem 1 --psm 3 -l por"
    text = pytesseract.image_to_string(img, config=config)
    data = pytesseract.image_to_data(img, config=config,
                                     output_type=pytesseract.Output.DICT)
    conf = [int(c) for c in data["conf"] if str(c) not in ("-1", "")]
    return text, (sum(conf) / len(conf) if conf else 0), data

def main(pages_dir, regions_file, out):
    out = pathlib.Path(out); out.mkdir(exist_ok=True)
    pages = json.loads(pathlib.Path(pages_dir, "pages.json").read_text())
    regions = json.loads(pathlib.Path(regions_file).read_text())
    for p in pages:
        grey = cv2.imread(str(pathlib.Path(pages_dir, p["file"])), 0)
        regs = [r for r in regions if r["issue"] == p["issue"] and r["page"] == p["page"]]
        text, conf, _ = read_page(grey, regs)
        (out / (p["file"][:-4] + ".txt")).write_text(text)
        print(f"issue {p['issue']:2d} page {p['page']}: {len(text.split())} words, mean confidence {conf:.0f}")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "text")
