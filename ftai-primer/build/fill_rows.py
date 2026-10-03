#!/usr/bin/env python3
"""Replace "(Part III §24, row: <driver name>)" placeholders with translation-table row ids.
Row ids are fixed by Part III §24 (Exhibit 3.14). Keyword mapping; ambiguous names get every matching id.
Usage: python3 fill_rows.py ../parts/partNN-*.md  (edits in place; prints each replacement)"""
import re, sys

ROWS = [
    ("T-1",  r"retire"),
    ("T-2",  r"gtf|powder|grounding(?!s? eas)"),
    ("T-3",  r"leap"),
    ("T-4",  r"\bmax\b|boeing|rate cap"),
    ("T-5",  r"airbus"),
    ("T-6",  r"lease extension|extension|availability|return condition"),
    ("T-7",  r"escalation|parts[- ]price|list price|oem parts"),
    ("T-8",  r"mro capacity|capacity short|turnaround|slot|shop-visit capacity"),
    ("T-9",  r"used[- ]material|usm|feedstock|material supply|teardown"),
    ("T-10", r"data[- ]cent|power demand|turbine shortage|gas-turbine|mod-1|core sink"),
    ("T-11", r"freighter|conversion"),
    ("T-12", r"utili[sz]ation"),
    ("T-13", r"groundings? easing|aog -|easing"),
    ("T-14", r"plateau|shop-visit demand|demand plateau|forecast|parity|decline"),
]
LABEL = {"T-1":"low CFM56 retirements","T-2":"GTF powder-metal groundings","T-3":"LEAP durability shortfall and the 2026 kit",
         "T-4":"737 MAX production rate cap","T-5":"Airbus delivery shortfall","T-6":"lessor extension behaviour",
         "T-7":"OEM parts-price escalation","T-8":"MRO capacity shortfall and turnaround","T-9":"used-material and feedstock scarcity",
         "T-10":"data-center power demand and the gas-turbine shortage","T-11":"freighter conversion",
         "T-12":"higher utilisation of mature narrowbodies","T-13":"GTF groundings easing","T-14":"CFM56 plateau-then-decline and LEAP aftermarket parity"}

def ids_for(name):
    n = name.lower()
    hits = [rid for rid, pat in ROWS if re.search(pat, n)]
    # "GTF groundings easing" should not also hit T-2
    if "T-13" in hits and "T-2" in hits and re.search(r"easing", n): hits.remove("T-2")
    return hits

for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    def rep(m):
        name = m.group(1).strip()
        hits = ids_for(name)
        if not hits:
            print(f"  UNMAPPED in {path}: {name}"); return m.group(0)
        tag = ", ".join(hits)
        print(f"  {path}: '{name}' -> {tag}")
        return f"(Part III §24, row{'s' if len(hits)>1 else ''} {tag}: {name})"
    new = re.sub(r"\(Part III §24, rows?: ([^)]+)\)", rep, s)
    # also catch bare "row: X" variants inside the opening paragraph
    if new != s:
        open(path, "w", encoding="utf-8").write(new)
