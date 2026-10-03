#!/usr/bin/env python3
"""Validate a rendered primer PDF and its markdown source.
Checks: near-blank pages (< 120 chars), exhibit titles without a table, page count, word count,
and writes a PNG of one page for a visual spot check.
Usage: python validate.py part.pdf part.md [--png-page N] [--png out.png]
"""
import argparse, re, sys, subprocess, os
import pypdf

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf"); ap.add_argument("md", nargs="?")
    ap.add_argument("--png-page", type=int, default=0); ap.add_argument("--png", default=None)
    ap.add_argument("--min-chars", type=int, default=120)
    a = ap.parse_args()
    r = pypdf.PdfReader(a.pdf); n = len(r.pages); problems = []
    blank = []
    for i, p in enumerate(r.pages, 1):
        t = (p.extract_text() or "").strip()
        is_divider = re.search(r"PART [IVX]+|THE SPINE|SPINE", t, flags=re.I) is not None and len(t) < 600
        if len(t) < a.min_chars and i not in (1,) and not is_divider:  # cover, title and divider pages may be short
            blank.append((i, len(t)))
    if blank: problems.append(f"near-blank pages (page, chars): {blank}")
    words = 0
    if a.md:
        src = open(a.md, encoding="utf-8").read()
        words = len(re.sub(r"<[^>]+>", " ", src).split())
        # every exhibit block must contain a table (block runs to its closing </cite></div> or the next exhibit)
        chunks = re.split(r'<div class="exh">', src)[1:]
        for blk in chunks:
            end = blk.find("</cite></div>")
            seg = blk[: end if end != -1 else 2000]
            if "<table" not in seg and not re.search(r"^\|", seg, flags=re.M):
                problems.append("exhibit without table: " + re.sub(r"\s+", " ", seg[:80]))
        titles = len(re.findall(r'class="exh-title"', src))
        tables = len(re.findall(r'class="exh"', src))
        if titles != tables: problems.append(f"exhibit title count {titles} != exhibit block count {tables}")
        # unbalanced divs
        if src.count("<div") != src.count("</div>"):
            problems.append(f"unbalanced <div>: {src.count('<div')} open vs {src.count('</div>')} close")
    print(f"pages={n} words_in_source={words}")
    for p in problems: print("PROBLEM:", p)
    if a.png:
        pg = a.png_page or min(3, n)
        subprocess.run(["pdftoppm", "-png", "-r", "60", "-f", str(pg), "-l", str(pg), "-singlefile", a.pdf, a.png.replace(".png", "")], check=True)
        print("png:", a.png)
    sys.exit(1 if problems else 0)

if __name__ == "__main__":
    main()
