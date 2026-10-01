#!/usr/bin/env python3
"""Narrative shift in management's own words.

Paste earnings-call transcripts (prepared remarks + Q&A) into
transcripts/earnings/ as YYYY-QN.md (e.g. 2026-Q2.md). The script counts key
phrases per call and prints a markdown table: what management started saying,
and what it stopped saying.

Usage:
  python3 tools/transcript_phrase_tracker.py --out data/phrases.csv
"""
import argparse, csv, glob, os, re

PHRASES = {
    "price increase": r"price (?:increase|hike|adjustment)s?",
    "churn": r"\bchurn",
    "superfan / Music Pro": r"super ?fan|music pro|supremium",
    "add-on": r"add-?on",
    "double-digit (ads)": r"double[- ]digit",
    "temporary": r"\btemporar",
    "normalize": r"normali[sz]",
    "monetization lever": r"moneti[sz]ation lever",
    "friction": r"\bfriction",
    "Discovery Mode": r"discovery mode",
    "marketplace": r"\bmarketplace",
    "gross margin": r"gross margin",
    "AI": r"\bAI\b",
    "compute / cloud": r"\bcompute\b|\bcloud\b",
    "emerging markets": r"emerging market",
    "India / Indonesia": r"\bindia\b|\bindonesia",
    "1 billion": r"1 billion|one billion",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="transcripts/earnings")
    ap.add_argument("--out", default="data/phrases.csv")
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(a.dir, "*.md")))
    if not files:
        print("no transcripts found in", a.dir)
        return
    table = []
    for fp in files:
        txt = open(fp, encoding="utf-8", errors="ignore").read()
        row = {"call": os.path.basename(fp).replace(".md", "")}
        for k, pat in PHRASES.items():
            row[k] = len(re.findall(pat, txt, flags=re.I))
        table.append(row)
    keys = ["call"] + list(PHRASES)
    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        w.writerows(table)
    print("| " + " | ".join(keys) + " |")
    print("|" + "---|" * len(keys))
    for r in table:
        print("| " + " | ".join(str(r[k]) for k in keys) + " |")
    print(f"\nwrote {a.out}")


if __name__ == "__main__":
    main()
