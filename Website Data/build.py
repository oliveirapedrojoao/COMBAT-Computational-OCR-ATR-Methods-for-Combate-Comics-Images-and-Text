#!/usr/bin/env python3
"""build.py — assembles the single-file site combate.html

Inputs (all in this folder or beside it):
  template.html         the page, with English text; blocks marked data-t
  translations_pt.py    Portuguese text for every data-t block + UI strings
  figs.json             figures and numbers produced by make_figures.py
  ../pipeline/*.py      the three detector scripts, embedded verbatim
  data/thumbs.js, data/issues.js, data/catalogue.js   catalogue seed data

Output:
  ../combate.html       open it with a double click
"""
import json, pathlib, re, sys
from bs4 import BeautifulSoup
import translations_pt as PT

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

tpl = (HERE / "template.html").read_text()
soup = BeautifulSoup(tpl, "html.parser")

# translation blocks: English comes from the template itself
T = {}
for el in soup.select("[data-t]"):
    key = el["data-t"]
    en = el.decode_contents()
    if key not in PT.BLOCKS:
        sys.exit(f"missing Portuguese translation for block '{key}'")
    T[key] = {"en": en, "pt": PT.BLOCKS[key]}
missing = set(PT.BLOCKS) - set(T)
if missing:
    sys.exit(f"translations without a block in the template: {missing}")

figs = json.loads((HERE / "figs.json").read_text())
code = {n: (ROOT / "pipeline" / n).read_text() for n in ["rasterise.py", "segment.py", "ocr.py"]}
data = [
    (HERE / "data" / "thumbs.js").read_text().strip(),
    (HERE / "data" / "issues.js").read_text().strip(),
    (HERE / "data" / "catalogue.js").read_text().strip(),
    "const METHOD=" + json.dumps(figs) + ";",
    "const CODE=" + json.dumps(code) + ";",
    "const T=" + json.dumps(T, ensure_ascii=False) + ";",
    "const STRINGS=" + json.dumps(PT.STRINGS, ensure_ascii=False) + ";",
]
blob = "\n".join(data)
assert "</script" not in blob.lower(), "embedded data must not contain </script>"
out = tpl.replace("__DATA__", blob)
(ROOT / "combate.html").write_text(out)
print("combate.html:", round(len(out) / 1024), "KB")
