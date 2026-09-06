"""segment.py — COMBAT project, stage 3

Split a rendered page into text zones and graphic zones. Combate has
no fixed grid, so nothing here assumes columns or templates. The page
is read as ink: small, row-aligned ink is text; anything else is a
candidate graphic. Classical OpenCV only, no trained model.

Usage:
    python3 segment.py out/pages regions.json
"""
import sys, pathlib, json
import numpy as np
import cv2
from rasterise import norm_box

def binarise(grey):
    """Ink = 1, paper = 0. The scans are uneven, so the threshold is
    adaptive: each pixel is compared with the mean of its 51-px
    neighbourhood, not with one global value for the whole page."""
    blur = cv2.GaussianBlur(grey, (3, 3), 0)
    ink = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY_INV, 51, 12)
    return ink

def remove_rules(ink):
    """Column filets and frames are long straight lines. Erode with a
    very wide (and a very tall) kernel: only lines survive, and those
    are subtracted from the ink so they cannot glue regions together."""
    H, W = ink.shape
    horiz = cv2.morphologyEx(ink, cv2.MORPH_OPEN,
                             cv2.getStructuringElement(cv2.MORPH_RECT, (W // 12, 1)))
    vert = cv2.morphologyEx(ink, cv2.MORPH_OPEN,
                            cv2.getStructuringElement(cv2.MORPH_RECT, (1, H // 12)))
    return cv2.subtract(ink, cv2.bitwise_or(horiz, vert))

def clear_border(ink):
    """The scans carry a dark, ragged band where the sheet met the
    scanner bed. Ink touching the page edge and running along most of
    it is that band, not content, and it would glue regions together."""
    H, W = ink.shape
    m = int(0.012 * max(H, W))
    ink[:m, :] = 0; ink[-m:, :] = 0; ink[:, :m] = 0; ink[:, -m:] = 0
    n, lab, stats, _ = cv2.connectedComponentsWithStats(ink, 8)
    for i in range(1, n):
        x, y, w, h, area = stats[i]
        touches = x <= m or y <= m or x + w >= W - m or y + h >= H - m
        if touches and (w > 0.5 * W or h > 0.5 * H) and area < 0.15 * w * h:
            ink[lab == i] = 0
    return ink

def text_mask(ink, grey):
    """Body text is made of small marks: each glyph, or a few glyphs
    stuck together, is no taller than a line of type. Keep every
    component of that size as text. Thresholds are fractions of the
    page height, so they follow the scan size rather than a fixed
    pixel value."""
    H, W = ink.shape
    line_h = H * 0.012                       # ~ one line of body type
    n, lab, stats, _ = cv2.connectedComponentsWithStats(ink, 8)
    small = np.zeros(n, bool)
    for i in range(1, n):
        x, y, w, h, area = stats[i]
        small[i] = h < 1.6 * line_h and w < 8 * line_h
    mask = (small[lab] * 255).astype(np.uint8)
    # a headline drawn by hand is big glyphs; body text is small ones.
    # thicken the small marks slightly so that broken glyphs count too.
    return cv2.dilate(mask, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))

def graphic_blocks(ink, text):
    """What is left after the text is masked out is graphic ink. Dilate
    it so that the strokes of one drawing touch each other, then take
    each connected block as a region proposal."""
    H, W = ink.shape
    rest = cv2.subtract(ink, text)
    k = int(H * 0.012)                       # join strokes of one figure;
    blocks = cv2.dilate(rest, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (k, max(3, k // 2))))
    n, lab, stats, _ = cv2.connectedComponentsWithStats(blocks, 8)
    out = []
    for i in range(1, n):
        x, y, w, h, area = stats[i]
        if w * h < 0.004 * W * H:            # page-relative: drop specks
            continue
        if w < 0.05 * W or h < 0.03 * H:     # slivers and stray rules
            continue
        density = ink[y:y+h, x:x+w].mean() / 255
        out.append({"px": [int(x), int(y), int(w), int(h)],
                    "density": round(float(density), 3)})
    return out

def merge_blocks(blocks, W, H, gap=0.01):
    """Two proposals that touch, or nearly touch, belong to one figure:
    the letters of a masthead, a drawing and its caption. Merge boxes
    whose outlines come within `gap` of the page size of each other,
    and keep merging until nothing more moves."""
    g = int(gap * max(W, H))
    boxes = [dict(b) for b in blocks]
    changed = True
    while changed:
        changed = False
        out = []
        while boxes:
            a = boxes.pop()
            ax, ay, aw, ah = a["px"]
            keep = []
            for b in boxes:
                bx, by, bw, bh = b["px"]
                if (ax - g < bx + bw and bx - g < ax + aw and
                        ay - g < by + bh and by - g < ay + ah):
                    x1, y1 = min(ax, bx), min(ay, by)
                    x2, y2 = max(ax + aw, bx + bw), max(ay + ah, by + bh)
                    ax, ay, aw, ah = x1, y1, x2 - x1, y2 - y1
                    a["density"] = max(a["density"], b["density"])
                    changed = True
                else:
                    keep.append(b)
            a["px"] = [ax, ay, aw, ah]
            out.append(a); boxes = keep
        boxes = out
    return boxes

def classify(block, grey, W, H):
    """A first guess at the type, refined by hand later.
    masthead   - wide band at the top of a page
    photograph - dark, evenly filled (halftone) area
    composed   - large block mixing lettering and ink
    lettering  - a short wide band: a hand-drawn headline
    drawing    - open strokes on paper"""
    x, y, w, h = block["px"]
    if y < 0.08 * H and w > 0.6 * W:
        return "masthead"
    if block["density"] > 0.35:
        return "photograph"
    if w * h > 0.25 * W * H:
        return "composed block"
    if h < 0.08 * H and w > 2.5 * h:
        return "lettering"
    return "drawing"

def segment_page(grey):
    H, W = grey.shape
    ink = clear_border(remove_rules(binarise(grey)))
    text = text_mask(ink, grey)
    regions = []
    for b in merge_blocks(graphic_blocks(ink, text), W, H):
        x, y, w, h = b["px"]
        regions.append({"box": norm_box(x, y, w, h, W, H),
                        "type": classify(b, grey, W, H),
                        "density": b["density"]})
    return regions, ink, text

def main(pages_dir, out):
    pages = json.loads(pathlib.Path(pages_dir, "pages.json").read_text())
    result = []
    for p in pages:
        grey = cv2.imread(str(pathlib.Path(pages_dir, p["file"])), 0)
        regions, _, _ = segment_page(grey)
        for r in regions:
            result.append({"issue": p["issue"], "page": p["page"], **r})
        print(f"issue {p['issue']:2d} page {p['page']}: {len(regions)} regions")
    pathlib.Path(out).write_text(json.dumps(result, indent=1))
    print(len(result), "candidate regions")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "regions.json")
