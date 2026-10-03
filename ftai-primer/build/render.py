#!/usr/bin/env python3
"""Render one or more primer markdown files to a paginated EB Garamond PDF.

Usage:
  python render.py part.md --out part.pdf                       # one Part
  python render.py spine.md partI.md partII.md ... --out master.pdf --master   # compile
Front matter (--- yaml ---) at the top of the FIRST file drives title/header/TOC.
Raw HTML blocks (cover, part dividers, defn/worked/box/exh components) pass through
(markdown extension md_in_html). Section numbering is written by the author.
"""
import argparse, os, re, sys
import markdown

HERE = os.path.dirname(os.path.abspath(__file__))

def parse_front_matter(text):
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end].strip(); body = text[end + 4:].lstrip("\n")
            for line in block.splitlines():
                m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line.strip())
                if m: meta[m.group(1).lower()] = m.group(2).strip().strip('"\'')
            return meta, body
    return meta, text

def strip_front_matter(text):
    return parse_front_matter(text)[1]

def css_escape(s): return s.replace("\\", "\\\\").replace('"', '\\"')

BACK_MATTER = {"Tensions carried in this Part", "Unknowns carried in this Part", "Tensions carried in the Spine", "Unknowns carried in the Spine", "Sources", "Build notes"}

def build_toc_html(toc_tokens, depth, skip_back_matter=False):
    rows = []
    def walk(tokens):
        for t in tokens:
            lvl = t["level"]; name = t["name"]
            if skip_back_matter and name.strip() in BACK_MATTER:
                continue
            if lvl == 1:
                rows.append(f'<li class="toc-part"><a href="#{t["id"]}">{name}</a></li>')
            elif lvl == 2:
                rows.append(f'<li><a href="#{t["id"]}">{name}</a></li>')
            elif lvl == 3 and depth >= 3:
                rows.append(f'<li class="toc-sub"><a href="#{t["id"]}">{name}</a></li>')
            if t.get("children"): walk(t["children"])
    walk(toc_tokens)
    return '<section class="toc"><h2>Contents</h2><ul>' + "".join(rows) + "</ul></section>" if rows else ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md", nargs="+"); ap.add_argument("--out", required=True)
    ap.add_argument("--master", action="store_true", help="compile mode: files joined with page breaks")
    ap.add_argument("--toc-depth", type=int, default=3)
    args = ap.parse_args()

    first = open(args.md[0], encoding="utf-8").read()
    meta, body = parse_front_matter(first)
    bodies = [body] + [strip_front_matter(open(p, encoding="utf-8").read()) for p in args.md[1:]]
    body_md = "\n\n".join(bodies) if args.master else bodies[0]   # each Part's divider carries its own page break

    md = markdown.Markdown(extensions=["tables", "footnotes", "attr_list", "toc", "def_list", "sane_lists", "md_in_html"],
                           extension_configs={"toc": {"toc_depth": "1-3"}})
    # Let markdown (tables, lists, emphasis) work inside the component blocks.
    body_md = re.sub(r'<div class="(exh|worked|defn|box|part-divider)">', r'<div class="\1" markdown="1">', body_md)
    # Part-divider titles: turn the raw <h1> into a markdown heading so the TOC indexes it.
    body_md = re.sub(r'(<div class="part-divider" markdown="1">\s*<div class="pn">[^<]*</div>)\s*<h1>(.*?)</h1>',
                     lambda m: m.group(1) + "\n\n# " + m.group(2) + "\n\n", body_md, flags=re.S)
    body_html = md.convert(body_md)
    toc_html = build_toc_html(getattr(md, "toc_tokens", []), args.toc_depth, skip_back_matter=args.master) if meta.get("toc", "").lower() in ("true", "yes", "1") else ""

    title = meta.get("title", "Deep Primer"); subtitle = meta.get("subtitle", "")
    if meta.get("cover", "").lower() in ("true", "yes", "1"):
        title_block = (f'<div class="cover"><div class="tag">{meta.get("tag", "Deep primer")}</div><h1>{title}</h1>'
                       f'<p class="sub">{subtitle}</p><p class="meta">{meta.get("as_of", "")}<br>{meta.get("meta", "")}</p></div>')
    else:
        title_block = f'<div class="title-block"><h1>{title}</h1>' + (f'<p class="subtitle">{subtitle}</p>' if subtitle else "") + "</div>"

    document = f"<!DOCTYPE html><html><head><meta charset='utf-8'></head><body>{title_block}{toc_html}{body_html}</body></html>"
    dyn_css = ('@page { @top-left { content: "%s"; } @top-right { content: "%s"; } }\n'
               '@page :first { @top-left { content: ""; } @top-right { content: ""; } }\n'
               % (css_escape(meta.get("header", title)), css_escape(meta.get("as_of", ""))))
    from weasyprint import HTML, CSS
    HTML(string=document, base_url=os.path.dirname(os.path.abspath(args.md[0]))).write_pdf(
        args.out, stylesheets=[CSS(filename=os.path.join(HERE, "assets", "primer.css")), CSS(string=dyn_css)])
    print(f"Rendered {args.out}", file=sys.stderr)

if __name__ == "__main__":
    main()
