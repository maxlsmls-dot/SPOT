#!/usr/bin/env python3
"""SPOT short — data desk model.

Builds the quarterly KPI dataset from company disclosures, the price-hike
calendar from press coverage, and derives the four things the pitch rests on:

  1. ARPU lapping schedule: y/y price contribution by quarter from the hike
     calendar, calibrated to the company's own ARPU bridge, under three mix-drag
     scenarios, against the ARPU growth consensus needs.
  2. Opex ex social charges and the gross-margin expansion run-rate (the
     "zero operating leverage" evidence).
  3. Guidance track record (where beats come from, where misses started).
  4. Regional back-solve: MAU, subs and conversion by region.
  5. Consensus vs ours, quarterly, through Q4-27 (consensus quarterlies are a
     reconstruction from annual consensus + guidance; replace with Visible Alpha).

Outputs: data/*.csv, data/charts/*.png, data/SPOT_model.xlsx, analysis/data-findings.md
Run: python3 analysis/model.py
"""
import csv, os
from collections import OrderedDict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from openpyxl import Workbook

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CH = os.path.join(DATA, "charts")
os.makedirs(CH, exist_ok=True)

# Validated default palette (dataviz skill, light mode)
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"

# ----------------------------------------------------------------------------
# 1. Quarterly KPIs (company disclosures; € millions unless noted)
# ----------------------------------------------------------------------------
# rev, premium_rev, ad_rev (as originally reported; ad/premium reclass from 1 Jan 2026),
# arpu (€), gm (%), oi, social_charges (None = not disclosed), mau (M), subs (M)
KPI = OrderedDict([
    ("Q1-25", dict(rev=4190, prem=3771, ad=419, arpu=4.73, gm=31.6, oi=509, sc=76,  mau=678, subs=268, arpu_cc=4.0)),
    ("Q2-25", dict(rev=4190, prem=3737, ad=453, arpu=4.57, gm=31.5, oi=406, sc=116, mau=696, subs=276, arpu_cc=2.0)),
    ("Q3-25", dict(rev=4272, prem=3825, ad=447, arpu=4.53, gm=31.6, oi=582, sc=-16, mau=713, subs=281, arpu_cc=0.0)),
    ("Q4-25", dict(rev=4500, prem=3982, ad=518, arpu=4.70, gm=33.1, oi=701, sc=None, mau=751, subs=290, arpu_cc=2.0)),
    ("Q1-26", dict(rev=4530, prem=4150, ad=385, arpu=4.76, gm=33.0, oi=715, sc=-39, mau=761, subs=293, arpu_cc=5.7)),
    ("Q2-26", dict(rev=4780, prem=4330, ad=446, arpu=4.89, gm=33.4, oi=655, sc=1,   mau=777, subs=300, arpu_cc=7.4)),
    ("Q3-26G", dict(rev=5000, prem=None, ad=None, arpu=None, gm=32.9, oi=670, sc=9, mau=788, subs=305, arpu_cc=7.0)),
])
# Prior-year comps needed for y/y (Q1-24..Q4-24): gm, oi, mau, subs, rev
PRIOR = OrderedDict([
    ("Q1-24", dict(rev=3636, gm=27.6, oi=168, mau=615, subs=239)),
    ("Q2-24", dict(rev=3807, gm=29.2, oi=266, mau=626, subs=246)),
    ("Q3-24", dict(rev=3988, gm=31.1, oi=454, mau=640, subs=252)),
    ("Q4-24", dict(rev=4242, gm=32.2, oi=477, mau=675, subs=263)),
])

# Guidance vs actual (company decks)
GUIDE = [
    # quarter, metric, guide, actual
    ("Q1-25", "MAU", 678, 678), ("Q1-25", "Subs", 265, 268), ("Q1-25", "Revenue", 4200, 4190), ("Q1-25", "GM %", 31.5, 31.6), ("Q1-25", "OI", 548, 509),
    ("Q2-25", "MAU", 689, 696), ("Q2-25", "Subs", 273, 276), ("Q2-25", "Revenue", 4300, 4190), ("Q2-25", "GM %", 31.5, 31.5), ("Q2-25", "OI", 539, 406),
    ("Q3-25", "MAU", 710, 713), ("Q3-25", "Subs", 281, 281), ("Q3-25", "Revenue", 4200, 4272), ("Q3-25", "GM %", 31.1, 31.6), ("Q3-25", "OI", 485, 582),
    ("Q4-25", "MAU", 745, 751), ("Q4-25", "Subs", 289, 290), ("Q4-25", "Revenue", 4500, 4500), ("Q4-25", "GM %", 32.9, 33.1), ("Q4-25", "OI", 620, 701),
    ("Q1-26", "MAU", 759, 761), ("Q1-26", "Subs", 293, 293), ("Q1-26", "Revenue", 4500, 4530), ("Q1-26", "GM %", 32.8, 33.0), ("Q1-26", "OI", 660, 715),
    ("Q2-26", "MAU", 778, 777), ("Q2-26", "Subs", 299, 300), ("Q2-26", "Revenue", 4800, 4780), ("Q2-26", "GM %", 33.1, 33.4), ("Q2-26", "OI", 630, 655),
]
GUIDE_NOTES = {
    "Q1-25": "OI below guide: social charges €76M",
    "Q2-25": "OI below guide: social charges €116M (€98M above forecast); revenue miss = FX",
    "Q3-25": "OI beat = lower social charges (−€16M)",
    "Q4-25": "OI beat: €67M of the €81M beat was social charges",
    "Q1-26": "OI beat: social charges −€39M; GM timing",
    "Q2-26": "First MAU miss vs guide; OI beat = GM timing + social charges €9M below forecast",
}

# Regional mix (% of MAU / % of subs) as disclosed; None = not found
REGION = OrderedDict([
    ("Q1-25", dict(mau=None,                       subs=dict(EU=36, NA=25, LA=24, RW=15))),
    ("Q2-25", dict(mau=dict(EU=27, NA=17, LA=22, RW=34), subs=None)),
    ("Q3-25", dict(mau=dict(EU=26, NA=17, LA=21, RW=36), subs=dict(EU=37, NA=25, LA=23, RW=14))),
    ("Q4-25", dict(mau=dict(EU=26, NA=16, LA=21, RW=37), subs=dict(EU=36, NA=25, LA=23, RW=15))),
    ("Q1-26", dict(mau=None,                       subs=dict(EU=36, NA=25, LA=24, RW=15))),
    ("Q2-26", dict(mau=dict(EU=25, NA=17, LA=21, RW=37), subs=dict(EU=36, NA=25, LA=24, RW=15))),
])

# ----------------------------------------------------------------------------
# 2. Price-hike calendar (press coverage) and lapping model
# ----------------------------------------------------------------------------
# Each hike: label, announced, effective (for existing subs), markets, individual list change,
# est. share of Premium revenue affected, est. blended uplift incl. family/duo, and the
# fraction of each quarter at the new price (f), from which y/y contribution = c * (f_q - f_q-4).
QTRS = ["Q1-24","Q2-24","Q3-24","Q4-24","Q1-25","Q2-25","Q3-25","Q4-25","Q1-26","Q2-26","Q3-26","Q4-26","Q1-27","Q2-27","Q3-27","Q4-27"]

def ramp(start_q, first_frac=1.0):
    """fraction of quarter at new price: 0 before start, first_frac in start quarter, 1 after."""
    f = {}
    seen = False
    for q in QTRS:
        if q == start_q:
            seen = True; f[q] = first_frac
        elif seen:
            f[q] = 1.0
        else:
            f[q] = 0.0
    return f

HIKES = [
    # label, announced, effective, markets, list change, rev share, blended uplift (contribution pts = share*uplift), ramp
    dict(label="Jul-23 global (53 mkts incl US $9.99→10.99)", announced="2023-07-24", effective="2023-08/09", share=0.70, uplift=0.11, contrib=None, f=ramp("Q3-23") if False else {q: 1.0 for q in QTRS}),
    dict(label="Apr-24 UK/AU/PK (+2)", announced="2024-04", effective="2024-04/05", share=0.08, uplift=0.11, contrib=1.0, f=ramp("Q2-24", 0.5)),
    dict(label="Jun-24 US $10.99→11.99 (family +18%)", announced="2024-06-03", effective="2024-07", share=0.32, uplift=0.11, contrib=3.5, f=ramp("Q3-24", 1.0)),
    dict(label="Apr-25 Benelux (+9–22%)", announced="2025-04", effective="2025-04", share=0.03, uplift=0.12, contrib=0.3, f=ramp("Q2-25", 0.67)),
    dict(label="Sep-25 Europe/LatAm/APAC/MEA/S.Asia (€10.99→11.99; US & CA excluded)", announced="2025-08-04", effective="2025-09→11 on billing dates", share=0.55, uplift=0.127, contrib=7.0, f={**ramp("Q3-25", 0.10), "Q4-25": 0.75}),
    dict(label="Nov-25 EM three-tier (ID, SA, UAE, ZA, IN)", announced="2025-11", effective="2025-11", share=0.02, uplift=0.10, contrib=0.2, f=ramp("Q4-25", 0.5)),
    dict(label="Feb-26 US $11.99→12.99 (+EE, LV)", announced="2026-01-15", effective="2026-02 billing dates", share=0.33, uplift=0.10, contrib=3.4, f=ramp("Q1-26", 0.5)),
    dict(label="May-26 Canada CAD 12.69→13.99", announced="2026-05-12", effective="2026-07 for existing", share=0.03, uplift=0.10, contrib=0.3, f=ramp("Q2-26", 0.1)),
    dict(label="May-26 India Standard ₹199→139 (−30%), Lite scrapped", announced="2026-05-15", effective="2026-05", share=0.005, uplift=-0.30, contrib=-0.1, f=ramp("Q2-26", 0.5)),
]
# Fix the Jul-23 ramp: fully in base throughout our window (laps by Q4-24); contribution 0 from Q1-25.
HIKES[0]["contrib"] = 0.0

def yoy_price(q):
    i = QTRS.index(q)
    if i < 4:
        return None
    tot = 0.0
    for h in HIKES:
        c = h["contrib"] or 0.0
        tot += c * (h["f"][q] - h["f"][QTRS[i-4]])
    return tot

MIX_SCEN = OrderedDict([("mix drag 0 (pre Q4-25 run-rate)", 0.0), ("mix drag −1.5", -1.5), ("mix drag −3 (Q4-25→Q2-26 run-rate)", -3.0)])
CONS_ARPU = {"Q3-26": 7.0, "Q4-26": 5.5, "Q1-27": 4.5, "Q2-27": 4.5, "Q3-27": 4.5, "Q4-27": 4.5}   # reconstructed
ACTUAL_ARPU_CC = {"Q1-25": 4.0, "Q2-25": 2.0, "Q3-25": 0.0, "Q4-25": 2.0, "Q1-26": 5.7, "Q2-26": 7.4}
ACTUAL_PRICE_PTS = {"Q2-26": 10.7}  # company bridge: +€0.49 on €4.57

# ----------------------------------------------------------------------------
# 3. Consensus vs ours, quarterly (consensus = reconstruction; replace with Visible Alpha)
# ----------------------------------------------------------------------------
MODEL = OrderedDict([
    # q: (cons_rev, cons_gm, cons_oi, our_rev, our_gm, our_opex_exsc, our_oi) € millions
    ("Q3-26", dict(c_rev=5000, c_gm=32.9, c_oi=678, o_rev=5000, o_gm=33.0, o_opex=975, o_oi=675)),
    ("Q4-26", dict(c_rev=5240, c_gm=33.5, c_oi=870, o_rev=5200, o_gm=33.3, o_opex=950, o_oi=782)),
    ("Q1-27", dict(c_rev=5150, c_gm=34.0, c_oi=830, o_rev=5000, o_gm=33.5, o_opex=935, o_oi=740)),
    ("Q2-27", dict(c_rev=5500, c_gm=34.3, c_oi=900, o_rev=5200, o_gm=33.7, o_opex=1045, o_oi=707)),
    ("Q3-27", dict(c_rev=5750, c_gm=34.6, c_oi=1000, o_rev=5400, o_gm=33.9, o_opex=1065, o_oi=766)),
    ("Q4-27", dict(c_rev=6100, c_gm=34.9, c_oi=1180, o_rev=5700, o_gm=34.0, o_opex=1045, o_oi=893)),
])

# ----------------------------------------------------------------------------
# Derived series
# ----------------------------------------------------------------------------
def derived():
    rows = []
    allq = OrderedDict(list(PRIOR.items()) + list(KPI.items()))
    keys = list(allq.keys())
    for i, (q, d) in enumerate(allq.items()):
        gp = d["rev"] * d["gm"] / 100
        opex = gp - d["oi"]
        sc = d.get("sc")
        opex_ex = opex - sc if sc is not None else None
        r = dict(q=q, rev=d["rev"], gm=d["gm"], gp=round(gp), oi=d["oi"], oi_margin=round(100 * d["oi"] / d["rev"], 1),
                 opex=round(opex), sc=sc, opex_ex_sc=round(opex_ex) if opex_ex is not None else None,
                 mau=d["mau"], subs=d["subs"], arpu=d.get("arpu"), ad=d.get("ad"), prem=d.get("prem"))
        if i >= 4:
            p = rows[i-4]
            r["gm_yoy_bp"] = round((d["gm"] - p["gm"]) * 100)
            r["oi_margin_yoy_bp"] = round((r["oi_margin"] - p["oi_margin"]) * 100)
            r["mau_yoy"] = round(100 * (d["mau"] / p["mau"] - 1), 1)
            r["subs_yoy"] = round(100 * (d["subs"] / p["subs"] - 1), 1)
            r["rev_yoy_rep"] = round(100 * (d["rev"] / p["rev"] - 1), 1)
            if r["opex_ex_sc"] is not None and p.get("opex_ex_sc") is not None:
                r["opex_ex_sc_yoy"] = round(100 * (r["opex_ex_sc"] / p["opex_ex_sc"] - 1), 1)
            else:
                r["opex_ex_sc_yoy"] = None
            r["opex_yoy"] = round(100 * (r["opex"] / p["opex"] - 1), 1)
        rows.append(r)
    return rows

def write_csv(path, rows, fields=None):
    if not rows:
        return
    fields = fields or list(rows[0].keys())
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

def regional():
    out = []
    for q, m in REGION.items():
        base = KPI[q]
        row = dict(q=q, mau=base["mau"], subs=base["subs"])
        for reg in ["EU", "NA", "LA", "RW"]:
            mm = m["mau"][reg] / 100 * base["mau"] if m["mau"] else None
            ss = m["subs"][reg] / 100 * base["subs"] if m["subs"] else None
            row[f"{reg}_mau"] = round(mm, 1) if mm else None
            row[f"{reg}_subs"] = round(ss, 1) if ss else None
            row[f"{reg}_conv"] = round(100 * ss / mm, 1) if (mm and ss) else None
        out.append(row)
    return out

# ----------------------------------------------------------------------------
# Charts
# ----------------------------------------------------------------------------
def style(ax, title, sub=None):
    ax.set_facecolor(SURF)
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    for s in ["left", "bottom"]:
        ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9)
    ax.yaxis.grid(True, color=GRID, linewidth=0.8); ax.set_axisbelow(True)
    ax.set_title(title, loc="left", fontsize=12, color=INK, fontweight="bold", pad=14)
    if sub:
        ax.text(0, 1.01, sub, transform=ax.transAxes, fontsize=9, color=INK2)

def chart_lapping(lap):
    qs = [q for q in QTRS if QTRS.index(q) >= QTRS.index("Q4-25")]
    fig, ax = plt.subplots(figsize=(9, 4.6), dpi=160); fig.patch.set_facecolor(SURF)
    x = range(len(qs))
    price = [lap[q]["price_pts"] for q in qs]
    ax.bar(x, price, width=0.55, color="#b7d3f6", label="Price contribution to ARPU (y/y pts, hike calendar)", zorder=2)
    for i, v in enumerate(price):
        ax.text(i, v + 0.25, f"{v:+.1f}", ha="center", fontsize=8.5, color=INK2)
    for (name, col) in [("mix drag −1.5", BLUE), ("mix drag −3 (Q4-25→Q2-26 run-rate)", ORANGE)]:
        ys = [lap[q][name] for q in qs]
        ax.plot(x, ys, color=col, linewidth=2, marker="o", markersize=5, label=f"Implied ARPU growth, {name}", zorder=3)
    cons = [CONS_ARPU.get(q) for q in qs]
    cx = [i for i, c in enumerate(cons) if c is not None]
    ax.plot(cx, [cons[i] for i in cx], color=INK2, linewidth=2, linestyle="--", label="ARPU growth consensus needs (reconstructed)", zorder=3)
    act = [ACTUAL_ARPU_CC.get(q) for q in qs]
    axx = [i for i, a in enumerate(act) if a is not None]
    ax.scatter(axx, [act[i] for i in axx], color=INK, s=36, zorder=4, label="Reported ARPU growth, constant currency")
    ax.axhline(0, color=INK2, linewidth=0.8)
    ax.set_xticks(list(x)); ax.set_xticklabels(qs)
    ax.set_ylabel("y/y %", color=INK2)
    style(ax, "ARPU: the price tailwind laps out by Q2-27 with no new hike",
          "Sep-25 international round rolls out of the comparison in Q4-26, the Feb-26 US round in Q1-27")
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    fig.tight_layout(); fig.savefig(os.path.join(CH, "1_arpu_lapping.png")); plt.close(fig)

def chart_leverage(rows):
    qs = [r["q"] for r in rows if r["q"] >= "Q1-25" and r["q"][-2:] in ("25", "26")]
    qs = [q for q in [r["q"] for r in rows] if q in ("Q1-25","Q2-25","Q3-25","Q4-25","Q1-26","Q2-26","Q3-26G")]
    byq = {r["q"]: r for r in rows}
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.4), dpi=160); fig.patch.set_facecolor(SURF)
    ax = axes[0]
    vals = [byq[q]["opex_ex_sc_yoy"] for q in qs]
    xs = list(range(len(qs)))
    ax.bar(xs, [v if v is not None else 0 for v in vals], width=0.55, color=[ORANGE if q == "Q3-26G" else BLUE for q in qs], zorder=2)
    for i, v in enumerate(vals):
        ax.text(i, (v if v else 0) + 0.6, "n/a" if v is None else f"{v:+.0f}%", ha="center", fontsize=8.5, color=INK2)
    ax.set_xticks(xs); ax.set_xticklabels(qs); ax.set_ylabel("y/y %", color=INK2)
    style(ax, "Opex ex social charges, y/y", "Q3-26 derived from guidance (€5.0B × 32.9% − €670M − €9M)")
    ax = axes[1]
    gm = [byq[q]["gm_yoy_bp"] for q in qs]
    om = [byq[q]["oi_margin_yoy_bp"] for q in qs]
    w = 0.38
    ax.bar([i - w/2 for i in xs], gm, width=w, color=BLUE, label="Gross margin, y/y bp", zorder=2)
    ax.bar([i + w/2 for i in xs], om, width=w, color=AQUA, label="Operating margin, y/y bp", zorder=2)
    for i, (g, o) in enumerate(zip(gm, om)):
        ax.text(i - w/2, g + (6 if g >= 0 else -14), f"{g:+d}", ha="center", fontsize=7.5, color=INK2)
        ax.text(i + w/2, o + (6 if o >= 0 else -14), f"{o:+d}", ha="center", fontsize=7.5, color=INK2)
    ax.axhline(0, color=INK2, linewidth=0.8)
    ax.set_xticks(xs); ax.set_xticklabels(qs)
    style(ax, "Margin expansion peaked in Q2-26", "Q3-26 guide: GM +130bp y/y, operating margin −20bp y/y")
    ax.set_ylim(-80, 900)
    ax.legend(fontsize=8, frameon=False, loc="upper right")
    fig.tight_layout(); fig.savefig(os.path.join(CH, "2_operating_leverage.png")); plt.close(fig)

def chart_model():
    qs = list(MODEL.keys())
    xs = list(range(len(qs)))
    fig, ax = plt.subplots(figsize=(9, 4.4), dpi=160); fig.patch.set_facecolor(SURF)
    w = 0.38
    c = [MODEL[q]["c_oi"] for q in qs]; o = [MODEL[q]["o_oi"] for q in qs]
    ax.bar([i - w/2 for i in xs], c, width=w, color="#9ec5f4", label="Consensus (reconstructed)", zorder=2)
    ax.bar([i + w/2 for i in xs], o, width=w, color=BLUE, label="Ours", zorder=2)
    for i in xs:
        ax.text(i - w/2, c[i] + 12, f"{c[i]}", ha="center", fontsize=8, color=INK2)
        ax.text(i + w/2, o[i] + 12, f"{o[i]}", ha="center", fontsize=8, color=INK2)
        gap = 100 * (o[i] / c[i] - 1)
        ax.text(i, max(c[i], o[i]) + 70, f"{gap:+.0f}%", ha="center", fontsize=9, color=ORANGE, fontweight="bold")
    ax.set_xticks(xs); ax.set_xticklabels(qs); ax.set_ylabel("Operating income, € millions", color=INK2)
    ax.set_ylim(0, max(c) * 1.25)
    style(ax, "Operating income: where the delta to consensus builds", "Gap labels = ours vs consensus; Q3-26 is guided so the two agree")
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    fig.tight_layout(); fig.savefig(os.path.join(CH, "3_oi_consensus_vs_ours.png")); plt.close(fig)

def chart_growth(rows):
    byq = {r["q"]: r for r in rows}
    qs = ["Q1-25","Q2-25","Q3-25","Q4-25","Q1-26","Q2-26","Q3-26G"]
    xs = list(range(len(qs)))
    fig, ax = plt.subplots(figsize=(9, 4.2), dpi=160); fig.patch.set_facecolor(SURF)
    for key, col, lab, off in [("subs_yoy", BLUE, "Premium subscribers, y/y", -0.45), ("mau_yoy", AQUA, "MAU, y/y", 0.25)]:
        ys = [byq[q][key] for q in qs]
        ax.plot(xs, ys, color=col, linewidth=2, marker="o", markersize=5, label=lab, zorder=3)
        for i, v in enumerate(ys):
            ax.text(i, v + off, f"{v:.1f}%", ha="center", fontsize=8, color=INK2)
    ax.set_xticks(xs); ax.set_xticklabels(qs); ax.set_ylabel("y/y %", color=INK2)
    ax.set_ylim(6, 14)
    style(ax, "Volume growth is decelerating into the Q4-25 comp (+38M MAU, +9M subs)", "Q3-26 from guidance: 788M MAU, 305M subs")
    ax.legend(fontsize=8, frameon=False, loc="lower left")
    fig.tight_layout(); fig.savefig(os.path.join(CH, "4_volume_growth.png")); plt.close(fig)

# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------
def main():
    rows = derived()
    write_csv(os.path.join(DATA, "spot_kpis.csv"), rows)

    # lapping
    lap = OrderedDict()
    for q in QTRS[4:]:
        p = yoy_price(q)
        lap[q] = {"price_pts": round(p, 2)}
        for name, drag in MIX_SCEN.items():
            lap[q][name] = round(p + drag, 2)
        lap[q]["reported_arpu_cc"] = ACTUAL_ARPU_CC.get(q)
        lap[q]["implied_mix_drag"] = round(ACTUAL_ARPU_CC[q] - p, 2) if q in ACTUAL_ARPU_CC else None
        lap[q]["consensus_arpu_growth"] = CONS_ARPU.get(q)
    write_csv(os.path.join(DATA, "arpu_lapping.csv"), [dict(q=q, **v) for q, v in lap.items()])
    write_csv(os.path.join(DATA, "price_hike_calendar.csv"),
              [dict(label=h["label"], announced=h["announced"], effective=h["effective"], est_share_of_premium_rev=h["share"],
                    est_blended_uplift=h["uplift"], yoy_contribution_pts_at_full_run=h["contrib"]) for h in HIKES])

    g = [dict(quarter=q, metric=m, guide=gd, actual=a, delta=round(a - gd, 1), note=GUIDE_NOTES.get(q, "")) for q, m, gd, a in GUIDE]
    write_csv(os.path.join(DATA, "guidance_track_record.csv"), g)
    reg = regional(); write_csv(os.path.join(DATA, "regional_backsolve.csv"), reg)
    write_csv(os.path.join(DATA, "model_consensus_vs_ours.csv"), [dict(q=q, **v, gap_oi_pct=round(100 * (v["o_oi"] / v["c_oi"] - 1), 1)) for q, v in MODEL.items()])

    chart_lapping(lap); chart_leverage(rows); chart_model(); chart_growth(rows)

    # xlsx
    wb = Workbook(); ws = wb.active; ws.title = "KPIs"
    def sheet(ws, rows_):
        if not rows_:
            return
        ws.append(list(rows_[0].keys()))
        for r in rows_:
            ws.append([r.get(k) for k in rows_[0].keys()])
    sheet(ws, rows)
    sheet(wb.create_sheet("ARPU lapping"), [dict(q=q, **v) for q, v in lap.items()])
    sheet(wb.create_sheet("Hike calendar"), [dict(label=h["label"], announced=h["announced"], effective=h["effective"], share=h["share"], uplift=h["uplift"], contrib_pts=h["contrib"]) for h in HIKES])
    sheet(wb.create_sheet("Guidance track record"), g)
    sheet(wb.create_sheet("Regional back-solve"), reg)
    sheet(wb.create_sheet("Consensus vs ours"), [dict(q=q, **v) for q, v in MODEL.items()])
    notes = wb.create_sheet("Notes")
    for line in [
        "Sources: Spotify quarterly shareholder decks and 6-Ks (Q1-25 to Q2-26, Q3-26 guidance); price-hike dates from company notices and press (MBW, 9to5Google, DMN, Billboard).",
        "Consensus quarterlies are a reconstruction from annual consensus (MarketScreener: 2026 sales €19.68B / EBIT €2.9B; 2027 sales €22.5B / EBIT €3.91B) and the guidance pattern. Replace with Visible Alpha before presenting.",
        "Lapping model: y/y price contribution = Σ hike contribution × (fraction of quarter at new price − same fraction a year earlier). Contributions calibrated to the company's Q2-26 ARPU bridge (+€0.49 price on €4.57 = +10.7 pts) and to Q4-25 / Q1-26 reported ARPU growth.",
        "Ad / Premium revenue reclassified from 1 Jan 2026; 2025 ad figures shown as originally reported.",
        "Q4-25 social charges not separately disclosed; the OI beat included €67M of social-charge favorability.",
        "Q1-25 and Q2-25 constant-currency ARPU growth are approximate (+4%, +2%); Q3-25 (0%), Q4-25 (+2%), Q1-26 (+5.7%), Q2-26 (+7.4%) are as reported.",
    ]:
        notes.append([line])
    wb.save(os.path.join(DATA, "SPOT_model.xlsx"))

    # findings
    byq = {r["q"]: r for r in rows}
    md = []
    md.append("# Data findings — SPOT short\n")
    md.append("Generated by `analysis/model.py` from company disclosures and the press record. Charts in `data/charts/`, workbook `data/SPOT_model.xlsx`.\n")
    md.append("## 1. ARPU: the price tailwind laps out (thesis point 1)\n")
    md.append("Calibrated to the company's own Q2-26 bridge (+10.7 pts from price, −3.1 pts from mix). Implied mix drag by quarter: " +
              ", ".join(f"{q} {lap[q]['implied_mix_drag']:+.1f}" for q in ACTUAL_ARPU_CC) + ". The drag was ~0 in Q3-25 and ~−3 to −3.5 from Q4-25, coinciding with record promo-driven adds and the EM tier changes.\n")
    md.append("| Quarter | Price contribution (pts) | ARPU growth @ mix −1.5 | @ mix −3 | Consensus needs |\n|---|---|---|---|---|")
    for q in ["Q3-26","Q4-26","Q1-27","Q2-27","Q3-27","Q4-27"]:
        md.append(f"| {q} | {lap[q]['price_pts']:+.1f} | {lap[q]['mix drag −1.5']:+.1f}% | {lap[q]['mix drag −3 (Q4-25→Q2-26 run-rate)']:+.1f}% | {CONS_ARPU[q]:+.1f}% |")
    md.append("\nConsensus 2027 ARPU growth of ~4.5% requires roughly 6 points of new price contribution in 2027, i.e. a broad US-plus-Europe round effective by early 2027. The May-26 Canada hike adds 0.3 pts; the India cut subtracts 0.1.\n")
    md.append("## 2. Zero operating leverage in the guide (thesis point 5)\n")
    md.append("| Quarter | Opex ex SC (€M) | y/y | GM y/y bp | OI margin y/y bp |\n|---|---|---|---|---|")
    for q in ["Q1-25","Q2-25","Q3-25","Q4-25","Q1-26","Q2-26","Q3-26G"]:
        r = byq[q]
        md.append(f"| {q} | {r['opex_ex_sc'] if r['opex_ex_sc'] is not None else 'n/a'} | {('%+.0f%%' % r['opex_ex_sc_yoy']) if r.get('opex_ex_sc_yoy') is not None else 'n/a'} | {r['gm_yoy_bp']:+d} | {r['oi_margin_yoy_bp']:+d} |")
    md.append("\nOpex ex social charges accelerates from +11% (Q1-26) to +18% (Q2-26) to ~+23% (Q3-26 guide). Gross-margin expansion peaked at +193bp in Q2-26 and the Q3 guide has operating margin down 20bp y/y on +14% cc revenue growth. Consensus FY-26 EBIT of €2.87–2.95B implies Q4-26 OI of ~€830–910M, which needs Q4 opex to fall sequentially into the Wrapped quarter; ours is €780M.\n")
    md.append("## 3. Guidance track record (rebuts 'management is conservative')\n")
    md.append("| Quarter | MAU Δ | Subs Δ | Revenue Δ | GM Δ bp | OI Δ | Why |\n|---|---|---|---|---|---|---|")
    for q in ["Q1-25","Q2-25","Q3-25","Q4-25","Q1-26","Q2-26"]:
        d = {m: (a - gd) for qq, m, gd, a in GUIDE if qq == q}
        md.append(f"| {q} | {d['MAU']:+.0f} | {d['Subs']:+.0f} | {d['Revenue']:+.0f} | {d['GM %']*100:+.0f} | {d['OI']:+.0f} | {GUIDE_NOTES[q]} |")
    md.append("\nOperating-income beats are social charges and gross-margin timing, not underlying cost control; the two OI misses (Q1-25, Q2-25) were social charges in the other direction. MAU beat guidance every quarter until Q2-26, the first miss, and the Q3-26 guide is the smallest Q3 add since 2018.\n")
    md.append("## 4. Regional back-solve (thesis point 3)\n")
    md.append("| Quarter | EU conv | NA conv | LatAm conv | RoW conv | RoW share of MAU | RoW share of subs |\n|---|---|---|---|---|---|---|")
    for r in reg:
        if r["EU_conv"]:
            md.append(f"| {r['q']} | {r['EU_conv']}% | {r['NA_conv']}% | {r['LA_conv']}% | {r['RW_conv']}% | {round(100*r['RW_mau']/r['mau'])}% | {round(100*r['RW_subs']/r['subs'])}% |")
    md.append("\nRest of World converts at ~16% against ~55–60% in Europe and North America, and it is 37% of users but 15% of subscribers. Rounded mix percentages carry ±1.5M of noise per region per quarter, so q/q regional subscriber moves (the Q1-26 North America decline) must be taken from the deck's own statement, not from this back-solve.\n")
    md.append("## 5. Consensus vs ours, quarterly\n")
    md.append("| Quarter | Cons rev | Ours rev | Cons GM | Ours GM | Cons OI | Ours OI | Gap |\n|---|---|---|---|---|---|---|---|")
    for q, v in MODEL.items():
        md.append(f"| {q} | {v['c_rev']} | {v['o_rev']} | {v['c_gm']}% | {v['o_gm']}% | {v['c_oi']} | {v['o_oi']} | {100*(v['o_oi']/v['c_oi']-1):+.0f}% |")
    md.append("\nFY-27: consensus €22.5B / €3.91B; ours €21.3B / €3.1B. Consensus quarterlies are reconstructed; swap in Visible Alpha.\n")
    md.append("## Caveats\n- Q1-25 and Q2-25 constant-currency ARPU growth are approximate; the calibration rests on Q3-25 to Q2-26, which are as reported.\n- All inputs are from search summaries of the decks and filings, cross-checked across outlets; verify the Q3-26 revenue guide (~€5.0B) and the Q4-25 social-charge figure against the decks.\n- The hike calendar's revenue-share and blended-uplift estimates are ours; the calibration to the company's bridge is what makes the lapping schedule defensible.\n")
    open(os.path.join(ROOT, "analysis", "data-findings.md"), "w").write("\n".join(md))
    print("done:", os.listdir(DATA), os.listdir(CH))


if __name__ == "__main__":
    main()
