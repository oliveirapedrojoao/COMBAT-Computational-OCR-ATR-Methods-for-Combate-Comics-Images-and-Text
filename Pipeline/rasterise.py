"""rasterise.py — COMBAT project, stage 2

Turn every page of every issue into a bitmap the rest of the pipeline
can work on. A PDF page is a set of drawing instructions; a bitmap is a
grid of grey values, which is what OpenCV and Tesseract read.

Usage:
    python3 rasterise.py /path/to/repository out/pages
"""
import sys, pathlib, json
import numpy as np
import pypdfium2 as pdfium
import cv2

DPI = 150                   # 150 dots per inch: enough for OCR and
SCALE = DPI / 72            # region detection, small enough to keep
                            # 487 pages in memory. PDF space is 72 dpi.

def render_page(doc, index):
    """Render one page to an 8-bit greyscale array (rows x cols)."""
    page = doc[index]
    bitmap = page.render(scale=SCALE, grayscale=True)  # anti-aliased
    grey = bitmap.to_numpy()                            # uint8 array
    if grey.ndim == 3:                                  # drop channels
        grey = grey[:, :, 0]
    return grey

def norm_box(x, y, w, h, W, H):
    """Pixel box -> fractions of the page (0–1), origin top-left.
    Every coordinate the project stores uses this convention, so a box
    found at 150 dpi can be cut again from a 300 dpi render, or drawn
    by the website on whatever size the browser renders the page."""
    return [round(x / W, 4), round(y / H, 4), round(w / W, 4), round(h / H, 4)]

def main(repo, out):
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    index = []
    for pdf in sorted(pathlib.Path(repo, "Combate_Newsfiles").rglob("*.pdf"),
                      key=lambda p: int(p.stem)):
        doc = pdfium.PdfDocument(str(pdf))
        for i in range(len(doc)):
            grey = render_page(doc, i)
            name = f"n{int(pdf.stem):02d}-p{i + 1}.png"
            cv2.imwrite(str(out / name), grey)
            H, W = grey.shape
            index.append({"issue": int(pdf.stem), "page": i + 1,
                          "file": name, "width": W, "height": H})
        doc.close()
        print(pdf.name, len(doc), "pages")
    (out / "pages.json").write_text(json.dumps(index, indent=1))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "pages")
