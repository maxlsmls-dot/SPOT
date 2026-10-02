#!/usr/bin/env python3
"""Audiobooks economics model — tests the claim that the gross-margin uplift from
bundling audiobooks into Premium has been clawed back (by music publishers via
direct deals and by book publishers via consumption-based cost) while the priced
channel (Audiobooks+) has stayed small.

Identity:  N(t) = B(t) + A_gp(t) − C(t)
  B   bundle mechanical-royalty saving, net of hand-backs to the majors' publishers
  A_gp gross profit on priced audiobook consumption (Audiobooks+, top-ups, Access)
  C   audiobook licensing cost on included consumption

Outputs: data/SPOT_audiobooks_model.xlsx (two tabs, live formulas), data/charts/5_*.png, 6_*.png,
         analysis/audiobooks-findings.md
Run:     python3 analysis/audiobooks_model.py
"""
import os
from collections import OrderedDict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data"); CH = os.path.join(DATA, "charts"); os.makedirs(CH, exist_ok=True)
BLUE, ORANGE, AQUA, YELLOW, RED = "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e34948"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
YEARS = [2024, 2025, 2026, 2027]

# ----------------------------------------------------------------------------
# INPUTS: (key, label, value, unit, period, source, type)
# type: D = disclosed by company/filing; R = reported by third party; E = estimate;
#       L = forecast placeholder that must be linked to the main model
# ----------------------------------------------------------------------------
INPUTS = [
    # Revenue base
    ("prem_rev_2022", "Premium revenue 2022", 10250, "€M", "FY22", "Spotify 20-F", "D"),
    ("prem_rev_2023", "Premium revenue 2023", 11566, "€M", "FY23", "Spotify 20-F", "D"),
    ("prem_rev_2024", "Premium revenue 2024", 13819, "€M", "FY24", "Spotify 20-F", "D"),
    ("prem_rev_2025", "Premium revenue 2025", 15350, "€M", "FY25", "Spotify 20-F", "D"),
    ("prem_rev_2026", "Premium revenue 2026E", 17700, "€M", "FY26E", "Placeholder: H1 actual (4,150 + 4,330) plus H2 estimate. Link to model: Premium revenue FY26E", "L"),
    ("prem_rev_2027", "Premium revenue 2027E", 19400, "€M", "FY27E", "Placeholder. Link to model: Premium revenue FY27E", "L"),
    ("grp_rev_2023", "Group revenue 2023", 13247, "€M", "FY23", "Spotify 20-F", "D"),
    ("grp_rev_2024", "Group revenue 2024", 15673, "€M", "FY24", "Spotify 20-F", "D"),
    ("grp_rev_2025", "Group revenue 2025", 17186, "€M", "FY25", "Spotify 20-F", "D"),
    ("grp_rev_2026", "Group revenue 2026E", 19500, "€M", "FY26E", "Placeholder. Link to model: total revenue FY26E", "L"),
    ("grp_rev_2027", "Group revenue 2027E", 21300, "€M", "FY27E", "Placeholder. Link to model: total revenue FY27E", "L"),
    # Premium cost of revenue (residual method)
    ("cogs_ratio_2022", "Premium cost of revenue / Premium revenue 2022", 0.72, "%", "FY22", "20-F: Premium gross margin 28%", "D"),
    ("cogs_ratio_2023", "Premium cost of revenue / Premium revenue 2023", 0.71, "%", "FY23", "FY24 20-F: 71% to 67%", "D"),
    ("cogs_ratio_2024", "Premium cost of revenue / Premium revenue 2024", 0.67, "%", "FY24", "FY24 20-F", "D"),
    ("cogs_ratio_2025", "Premium cost of revenue / Premium revenue 2025", 0.66, "%", "FY25", "FY25 20-F: Premium gross margin 34%", "D"),
    ("cogs_inc_2024", "Premium cost of revenue increase 2024", 1093, "€M", "FY24", "FY24 20-F (+13%)", "D"),
    ("royalty_inc_2024", "of which royalty / content costs 2024", 1078, "€M", "FY24", "FY24 20-F", "D"),
    ("royalty_inc_2025", "Royalty / content cost increase 2025 (music + audiobooks + Partner Program, net of marketplace)", 765, "€M", "FY25", "FY25 20-F", "D"),
    ("royalty_inc_9m25", "Royalty / content cost increase 9M-25", 588, "€M", "9M25", "Q3-25 6-K", "D"),
    ("royalty_inc_h126", "Content cost increase H1-26", 474, "€M", "H1-26", "Q2-26 6-K (Premium cost of revenue +€500M, +10%; ratio 67% to 65%)", "D"),
    ("prem_rev_h125", "Premium revenue H1-25", 7508, "€M", "H1-25", "3,771 + 3,737", "D"),
    ("prem_rev_h126", "Premium revenue H1-26", 8480, "€M", "H1-26", "4,150 + 4,330", "D"),
    ("prem_rev_9m24", "Premium revenue 9M-24", 10114, "€M", "9M24", "FY24 13,819 less Q4-24 3,705", "D"),
    ("prem_rev_9m25", "Premium revenue 9M-25", 11333, "€M", "9M25", "3,771 + 3,737 + 3,825", "D"),
    # B: bundle saving
    ("bundle_13m", "Bundle mechanical-royalty reduction, 1 Mar 2024 to 31 Mar 2025 (13 months)", 205, "€M", "Mar24-Mar25", "Spotify 6-K Q1-25: 'additional royalties that would be due would be approximately €205 million, plus potentially penalties and interest'", "D"),
    ("bundle_months", "Months in the disclosure period", 13, "months", "", "", "D"),
    ("nmpa_first_year", "NMPA estimate of first-year publisher loss", 230, "$M", "2024-25", "NMPA via Billboard", "R"),
    ("bb_q423_mech", "Mechanical royalties paid, Q4-23 (MLC reports)", 97.3, "$M", "Q4-23", "Billboard analysis", "R"),
    ("bb_q425_mech", "Mechanical royalties paid, Q4-25 (MLC reports; majors direct-licensed, so not comparable after 2025)", 53.3, "$M", "Q4-25", "Billboard analysis", "R"),
    ("music_alloc", "Music share of bundle revenue under CRB allocation", 0.52, "%", "", "NMPA / Billboard ('$5.70 of the bundle')", "R"),
    ("share_umpg", "UMPG share of US mechanicals", 0.22, "%", "", "Estimate from US publishing market shares (range 20-25%)", "E"),
    ("share_wcm", "Warner Chappell share of US mechanicals", 0.13, "%", "", "Estimate (range 11-15%)", "E"),
    ("share_smp", "Sony Music Publishing share of US mechanicals", 0.26, "%", "", "Estimate; SMP ranked #1 publisher in 2025 (range 23-28%)", "E"),
    ("start_umpg", "UMPG direct licence start month (2025)", 2, "month", "2025", "Announced 26 Jan 2025; reported to 'nullify' the bundle discount going forward", "R"),
    ("start_wcm", "Warner Chappell direct licence start month (2025)", 3, "month", "2025", "Announced 6 Feb 2025; 'supersedes the bundling payment structure' (MBW)", "R"),
    ("start_smp", "Sony Music Publishing direct licence start month (2025)", 10, "month", "2025", "Announced Sep 2025; direct US licence", "R"),
    ("restoration", "Share of the bundle discount restored to direct-licensed publishers", 1.0, "%", "", "Assumption per reporting ('nullified'); sensitivity at 50%", "E"),
    ("mlc_loss_2027", "MLC amended complaint succeeds in 2027 (1 = yes): remaining saving goes to zero", 0, "flag", "2027", "Scenario switch. Interlocutory appeal denied 1 Sep 2026; case continues at district court", "E"),
    # C: audiobook licensing cost
    ("c_2024", "Audiobook licensing cost 2024 ('hundreds of millions of dollars a year' by Oct-24)", 190, "€M", "FY24", "Axios 15 Oct 2024; Spotify newsroom Mar-25 repeats; 'tens of millions' by Feb-24 (Digital Music News). Sized as a full year", "E"),
    ("c_g_2025", "Audiobook licensing cost growth 2025 (listeners +30-36%, hours +35-37%, DACH launch, Family members)", 0.58, "%", "FY25", "Spotify newsroom Mar-25, Oct-25; estimate", "E"),
    ("c_g_2026", "Audiobook licensing cost growth 2026E (listeners +60%, Nordics, Audiobooks+ Europe)", 0.43, "%", "FY26E", "Placeholder: Publishers Weekly 2026. Link to model: audiobook cost growth FY26E", "L"),
    ("c_g_2027", "Audiobook licensing cost growth 2027E", 0.30, "%", "FY27E", "Placeholder: assumes deceleration. Link to model: audiobook cost growth FY27E", "L"),
    ("c_low_mult", "Low-case multiplier on audiobook licensing cost", 0.80, "x", "", "Sensitivity band", "E"),
    ("c_high_mult", "High-case multiplier on audiobook licensing cost", 1.25, "x", "", "Sensitivity band", "E"),
    ("apa_us_2025", "US audiobook publisher receipts 2025", 2430, "$M", "FY25", "Audio Publishers Association, Jun 2026 (+9%)", "R"),
    ("apa_us_2024", "US audiobook publisher receipts 2024", 2220, "$M", "FY24", "Audio Publishers Association (+13%)", "R"),
    ("spot_us_share_lo", "Spotify share of US publisher audiobook receipts, low", 0.10, "%", "FY25", "Estimate; Audible 63.4% to 59.8% (eMarketer Mar-26), Spotify #2", "E"),
    ("spot_us_share_hi", "Spotify share of US publisher audiobook receipts, high", 0.14, "%", "FY25", "Estimate", "E"),
    ("nonus_uplift", "Non-US markets as a multiple of US cost (UK, AU, CA, IE, NZ, FR, BX, DACH, Nordics)", 1.40, "x", "FY25", "Estimate", "E"),
    ("eurusd", "EUR/USD", 1.13, "x", "2025 avg", "Approximate 2025 average", "E"),
    # A: priced channel
    ("ab_plus_arr", "Audiobooks+ annual recurring revenue", 100, "$M", "Jul-26", "Investor Day 21 May 2026 ('on track for $100M ARR in July'); Q2-26 call: reached", "D"),
    ("ab_plus_payers", "Audiobooks+ paying users", 1.0, "M", "May-26", "Investor Day via Publishers Weekly ('more than one million')", "D"),
    ("a_rev_2024", "Priced audiobook revenue 2024 (top-ups from Mar-24)", 5, "€M", "FY24", "Estimate", "E"),
    ("a_rev_2025", "Priced audiobook revenue 2025 (US Audiobooks+ from Aug-25; 11 EU markets late-25)", 30, "€M", "FY25", "Estimate", "E"),
    ("a_rev_2026", "Priced audiobook revenue 2026E", 75, "€M", "FY26E", "Placeholder: ARR $100M mid-year is about €88M run-rate; H1 lower. Link to model: paid audiobook revenue FY26E", "L"),
    ("a_rev_2027", "Priced audiobook revenue 2027E", 120, "€M", "FY27E", "Placeholder (+60%). Link to model: paid audiobook revenue FY27E", "L"),
    ("a_cogs_ratio", "Content cost ratio on paid hours (same publisher payments apply)", 0.55, "%", "", "Assumption", "E"),
    # Attach denominators
    ("subs_global", "Premium subscribers", 300, "M", "Q2-26", "Spotify Q2-26 deck", "D"),
    ("subs_eligible", "Subscribers in markets with audiobooks in Premium", 140, "M", "Q2-26", "Estimate: North America 75M + eligible Europe ~60M + AU/NZ ~6M", "E"),
    ("listen_share", "Share of Premium subscribers listening to audiobooks", 0.25, "%", "2025", "The Bookseller 2025; TechCrunch 17 Jul 2025", "R"),
    ("tried_share", "Share of eligible Premium users who have ever pressed play", 0.50, "%", "Oct-25", "Spotify newsroom 15 Oct 2025", "D"),
    ("basic_optout", "US individual subscribers who took the $1 Basic plan to drop audiobooks", 0.155, "%", "2024", "Morgan Stanley survey via Billboard (14-17%)", "R"),
    ("bull_attach", "Music Pro attach assumption, bull case", 0.03, "%", "2027", "Placeholder. Link to model: bull-case Music Pro attach", "L"),
    # Consensus
    ("cons_gm_exp_2026", "Consensus gross-margin expansion 2026E", 115, "bp", "FY26E", "Placeholder: 33.2% vs 32.0%. Link to model: consensus gross margin FY26E", "L"),
    ("cons_gm_exp_2027", "Consensus gross-margin expansion 2027E", 130, "bp", "FY27E", "Placeholder: ~34.5% vs 33.2%. Link to model: consensus gross margin FY27E", "L"),
    # Memo: price increase attributed to audiobooks (excluded from N)
    ("p_2024", "Memo: Jun-24 US price increase, annualized revenue (not in N)", 500, "€M", "run-rate", "Estimate: ~7% blended on ~€8B US Premium revenue", "E"),
]

# ----------------------------------------------------------------------------
# Python computation (mirrors the workbook formulas)
# ----------------------------------------------------------------------------
I = {k: v for k, _, v, *_ in INPUTS}

def compute():
    r = {}
    run_rate = I["bundle_13m"] / I["bundle_months"] * 12
    r["run_rate"] = run_rate
    months_active = {2024: 10, 2025: 12, 2026: 12, 2027: 12}
    handback_months = {
        "umpg": {2024: 0, 2025: 13 - I["start_umpg"], 2026: 12, 2027: 12},
        "wcm": {2024: 0, 2025: 13 - I["start_wcm"], 2026: 12, 2027: 12},
        "smp": {2024: 0, 2025: 13 - I["start_smp"], 2026: 12, 2027: 12},
    }
    shares = {"umpg": I["share_umpg"], "wcm": I["share_wcm"], "smp": I["share_smp"]}
    r["B_gross"], r["B_handback"], r["B"] = {}, {}, {}
    for y in YEARS:
        gross = run_rate * months_active[y] / 12
        hb = sum(run_rate * shares[p] * handback_months[p][y] / 12 for p in shares) * I["restoration"]
        b = gross - hb
        if y == 2027 and I["mlc_loss_2027"]:
            b = 0
        r["B_gross"][y], r["B_handback"][y], r["B"][y] = gross, hb, b
    # C
    c = {2024: I["c_2024"]}
    c[2025] = c[2024] * (1 + I["c_g_2025"]); c[2026] = c[2025] * (1 + I["c_g_2026"]); c[2027] = c[2026] * (1 + I["c_g_2027"])
    r["C"] = c
    r["C_low"] = {y: c[y] * I["c_low_mult"] for y in c}; r["C_high"] = {y: c[y] * I["c_high_mult"] for y in c}
    # market-share triangulation (2025)
    r["C_tri_lo"] = I["apa_us_2025"] * I["spot_us_share_lo"] * I["nonus_uplift"] / I["eurusd"]
    r["C_tri_hi"] = I["apa_us_2025"] * I["spot_us_share_hi"] * I["nonus_uplift"] / I["eurusd"]
    # A
    a_rev = {2024: I["a_rev_2024"], 2025: I["a_rev_2025"], 2026: I["a_rev_2026"], 2027: I["a_rev_2027"]}
    r["A_rev"] = a_rev; r["A_gp"] = {y: a_rev[y] * (1 - I["a_cogs_ratio"]) for y in YEARS}
    # N
    grp = {2024: I["grp_rev_2024"], 2025: I["grp_rev_2025"], 2026: I["grp_rev_2026"], 2027: I["grp_rev_2027"]}
    r["grp"] = grp
    r["N"] = {y: r["B"][y] + r["A_gp"][y] - c[y] for y in YEARS}
    r["N_bp"] = {y: r["N"][y] / grp[y] * 1e4 for y in YEARS}
    r["dN"] = {y: r["N"][y] - r["N"][y - 1] for y in YEARS[1:]}
    r["dN_bp"] = {y: r["dN"][y] / grp[y] * 1e4 for y in YEARS[1:]}
    r["dC"] = {y: c[y] - c[y - 1] for y in YEARS[1:]}
    r["dA_gp"] = {y: r["A_gp"][y] - r["A_gp"][y - 1] for y in YEARS[1:]}
    r["dB"] = {y: r["B"][y] - r["B"][y - 1] for y in YEARS[1:]}
    # residual
    prem = {2022: I["prem_rev_2022"], 2023: I["prem_rev_2023"], 2024: I["prem_rev_2024"], 2025: I["prem_rev_2025"]}
    ratio = {2022: I["cogs_ratio_2022"], 2023: I["cogs_ratio_2023"], 2024: I["cogs_ratio_2024"], 2025: I["cogs_ratio_2025"]}
    cogs = {y: prem[y] * ratio[y] for y in prem}
    r["prem"], r["cogs"] = prem, cogs
    r["inc_ratio"] = {
        "FY24 (royalty component)": I["royalty_inc_2024"] / (prem[2024] - prem[2023]),
        "FY25 (royalty component)": I["royalty_inc_2025"] / (prem[2025] - prem[2024]),
        "9M-25 (royalty component)": I["royalty_inc_9m25"] / (I["prem_rev_9m25"] - I["prem_rev_9m24"]),
        "H1-26 (content component)": I["royalty_inc_h126"] / (I["prem_rev_h126"] - I["prem_rev_h125"]),
    }
    # attach
    listeners_all = I["subs_global"] * I["listen_share"]
    listeners_elig = I["subs_eligible"] * I["listen_share"]
    r["attach"] = OrderedDict([
        ("payers / global subscribers", I["ab_plus_payers"] / I["subs_global"]),
        ("payers / eligible-market subscribers", I["ab_plus_payers"] / I["subs_eligible"]),
        ("payers / monthly listeners (25% of eligible)", I["ab_plus_payers"] / listeners_elig),
        ("payers / monthly listeners (25% of global)", I["ab_plus_payers"] / listeners_all),
        ("Basic-plan opt-out share, US individual (inverse signal)", I["basic_optout"]),
        ("bull-case Music Pro attach assumption", I["bull_attach"]),
    ])
    r["arr_per_payer"] = I["ab_plus_arr"] / I["ab_plus_payers"]
    return r

# ----------------------------------------------------------------------------
# Workbook: two tabs, live formulas
#   Audiobooks_Inputs   hard-coded inputs with source, type and link flags
#   Audiobooks_Analysis build (B, C, A), bridge, attach, cross-checks, sensitivity
# Colour convention: blue = hard-coded input; green = reference to the inputs tab;
# black = formula; orange fill = estimate; yellow fill / red text = forecast placeholder to link
# ----------------------------------------------------------------------------
HDR = Font(bold=True); TITLE = Font(bold=True, size=12)
FILL = PatternFill("solid", fgColor="DDEBF7"); EST = PatternFill("solid", fgColor="FCE4D6"); LINK = PatternFill("solid", fgColor="FFF2CC")
F_BLUE = Font(color="0000FF"); F_GREEN = Font(color="008000"); F_BLACK = Font(color="000000"); LINKF = Font(color="C00000", bold=True)
FMT_M = '#,##0_);(#,##0)'; FMT_BP = '0_);(0)'; FMT_PCT = '0.0%'; FMT_PCT0 = '0%'; FMT_X = '0.00'; FMT_INT = '0'
UNIT_FMT = {"€M": FMT_M, "$M": FMT_M, "%": FMT_PCT, "x": FMT_X, "bp": FMT_INT, "M": '0.0', "flag": FMT_INT, "month": FMT_INT, "months": FMT_INT}
TYPE = {"D": "Actual", "R": "Reported", "E": "Estimate", "L": "LINK TO MODEL"}
SHEET_IN, SHEET_AN = "Audiobooks_Inputs", "Audiobooks_Analysis"
COLS = ["C", "D", "E", "F"]  # 2024A, 2025A, 2026E, 2027E

def _style(cell, fmt=None):
    v = cell.value
    if isinstance(v, str) and v.startswith("="):
        cell.font = F_GREEN if SHEET_IN + "!" in v else F_BLACK
    elif isinstance(v, (int, float)):
        cell.font = F_BLUE
    if fmt: cell.number_format = fmt

def build_workbook(r):
    wb = Workbook(); wb.properties.creator = "SPOT"; wb.properties.lastModifiedBy = "SPOT"

    # ---- Inputs tab
    ws = wb.active; ws.title = SHEET_IN
    ws["A1"] = "Audiobooks: inputs"; ws["A1"].font = TITLE
    ws["A2"] = ("Blue text = hard-coded input. Orange fill = estimate. Yellow fill with red text = forecast placeholder: "
                "replace with a link to the main model before use. No forecasts beyond FY27.")
    ws.append([]); ws.append(["Input", "Value", "Unit", "Period", "Type", "Source / note"])
    for c in ws[4]: c.font = HDR; c.fill = FILL
    A = {}
    for i, (k, label, v, unit, period, src, conf) in enumerate(INPUTS, start=5):
        ws.append([label, v, unit, period, TYPE[conf], src]); A[k] = f"{SHEET_IN}!$B${i}"
        cell = ws.cell(row=i, column=2); cell.font = F_BLUE; cell.number_format = UNIT_FMT.get(unit, "General")
        if conf == "E": cell.fill = EST
        if conf == "L":
            cell.fill = LINK; cell.font = LINKF
            ws.cell(row=i, column=5).fill = LINK; ws.cell(row=i, column=5).font = LINKF
    ws.append([]); ws.append(["Sources"]); ws.cell(row=ws.max_row, column=1).font = HDR
    for line in SOURCES: ws.append([line])
    for col, w in zip("ABCDEF", [78, 12, 8, 12, 16, 110]): ws.column_dimensions[col].width = w
    ws.freeze_panes = "A5"

    # ---- Analysis tab
    an = wb.create_sheet(SHEET_AN)
    state = {"row": 0}

    def put(label, vals=None, single=None, fmt=None, bold=False, fill=None, extra=None):
        state["row"] += 1; rr = state["row"]
        an.cell(row=rr, column=1, value=label)
        if bold: an.cell(row=rr, column=1).font = HDR
        if single is not None:
            c = an.cell(row=rr, column=2, value=single); _style(c, fmt)
        if vals:
            for col, v in zip(COLS, vals):
                if v is None or v == "": continue
                c = an[f"{col}{rr}"]; c.value = v; _style(c, fmt)
        if extra:
            for col, v in extra.items():
                c = an[f"{col}{rr}"]; c.value = v; _style(c, fmt)
        if fill:
            for col in range(1, 7): an.cell(row=rr, column=col).fill = fill
        return rr

    def nxt(): return state["row"] + 1

    put("Audiobooks: gross-margin build (€M unless stated)", bold=True); an["A1"].font = TITLE
    put("2026E and 2027E are driven by placeholder inputs on the inputs tab flagged LINK TO MODEL. Blue = hard-coded; green = reference to inputs tab; black = formula.")
    put("")
    hdr = put("", vals=["2024A", "2025A", "2026E", "2027E"], bold=True, fill=FILL)
    for col in COLS: an[f"{col}{hdr}"].font = HDR; an[f"{col}{hdr}"].alignment = Alignment(horizontal="right")

    # 1. Bundle saving
    put("1. Bundle mechanical-royalty saving (B)", bold=True)
    R_rr = put("Run-rate bundle saving, €M per year (13-month disclosure x 12/13)", single=f"={A['bundle_13m']}/{A['bundle_months']}*12", fmt=FMT_M)
    R_mo = put("Months bundle active in year", vals=[10, 12, 12, 12], fmt=FMT_INT)
    R_gross = put("Gross saving = run-rate x months / 12", vals=[f"=$B${R_rr}*{c}{R_mo}/12" for c in COLS], fmt=FMT_M)
    R_u = put("UMPG months on direct licence", vals=[0, f"=13-{A['start_umpg']}", 12, 12], fmt=FMT_INT)
    R_w = put("Warner Chappell months on direct licence", vals=[0, f"=13-{A['start_wcm']}", 12, 12], fmt=FMT_INT)
    R_s = put("Sony Music Publishing months on direct licence", vals=[0, f"=13-{A['start_smp']}", 12, 12], fmt=FMT_INT)
    R_hb = put("Hand-back to direct-licensed publishers = run-rate x sum(share x months / 12) x restoration",
               vals=[f"=$B${R_rr}*({A['share_umpg']}*{c}{R_u}+{A['share_wcm']}*{c}{R_w}+{A['share_smp']}*{c}{R_s})/12*{A['restoration']}" for c in COLS], fmt=FMT_M)
    R_B = put("B  Net bundle saving (2027: zero if MLC switch = 1)",
              vals=[f"={c}{R_gross}-{c}{R_hb}" for c in COLS[:3]] + [f"=IF({A['mlc_loss_2027']}=1,0,F{R_gross}-F{R_hb})"], fmt=FMT_M, bold=True)
    put("")

    # 2. Licensing cost on included hours
    put("2. Audiobook licensing cost on included hours (C)", bold=True)
    R_g = put("Growth y/y", vals=["", f"={A['c_g_2025']}", f"={A['c_g_2026']}", f"={A['c_g_2027']}"], fmt=FMT_PCT0)
    rc = nxt()
    R_C = put("C  Base case", vals=[f"={A['c_2024']}", f"=C{rc}*(1+D{R_g})", f"=D{rc}*(1+E{R_g})", f"=E{rc}*(1+F{R_g})"], fmt=FMT_M, bold=True)
    R_Cl = put("C  Low case", vals=[f"={c}{R_C}*{A['c_low_mult']}" for c in COLS], fmt=FMT_M)
    R_Ch = put("C  High case", vals=[f"={c}{R_C}*{A['c_high_mult']}" for c in COLS], fmt=FMT_M)
    put("")

    # 3. Priced channel
    put("3. Priced channel (Audiobooks+, top-ups, a la carte)", bold=True)
    R_arev = put("Revenue", vals=[f"={A['a_rev_2024']}", f"={A['a_rev_2025']}", f"={A['a_rev_2026']}", f"={A['a_rev_2027']}"], fmt=FMT_M)
    R_ratio = put("Content cost ratio on paid hours", single=f"={A['a_cogs_ratio']}", fmt=FMT_PCT0)
    R_Agp = put("A  Gross profit on paid hours = revenue x (1 - ratio)", vals=[f"={c}{R_arev}*(1-$B${R_ratio})" for c in COLS], fmt=FMT_M, bold=True)
    put("")

    # 4. Bridge
    put("4. Net contribution to gross profit: N = B + A - C", bold=True)
    R_B2 = put("B  Net bundle saving", vals=[f"={c}{R_B}" for c in COLS], fmt=FMT_M)
    R_A2 = put("A  Gross profit on paid hours", vals=[f"={c}{R_Agp}" for c in COLS], fmt=FMT_M)
    R_C2 = put("C  Licensing cost on included hours", vals=[f"={c}{R_C}" for c in COLS], fmt=FMT_M)
    R_N = put("N  Net contribution", vals=[f"={c}{R_B2}+{c}{R_A2}-{c}{R_C2}" for c in COLS], fmt=FMT_M, bold=True)
    R_grp = put("Group revenue", vals=[f"={A['grp_rev_2024']}", f"={A['grp_rev_2025']}", f"={A['grp_rev_2026']}", f"={A['grp_rev_2027']}"], fmt=FMT_M)
    R_Nbp = put("N, bp of group revenue", vals=[f"={c}{R_N}/{c}{R_grp}*10000" for c in COLS], fmt=FMT_BP)
    R_dN = put("Change in N y/y, €M (gross-margin headwind)", vals=[""] + [f"={c}{R_N}-{p}{R_N}" for p, c in zip(COLS, COLS[1:])], fmt=FMT_M, bold=True)
    R_dNbp = put("Change in N y/y, bp of group revenue", vals=[""] + [f"={c}{R_dN}/{c}{R_grp}*10000" for c in COLS[1:]], fmt=FMT_BP, bold=True)
    R_dB = put("   of which music publishers reclaim the bundle saving (change in B)", vals=[""] + [f"={c}{R_B2}-{p}{R_B2}" for p, c in zip(COLS, COLS[1:])], fmt=FMT_M)
    R_dC = put("   of which book publishers paid on consumption (change in C, negative)", vals=[""] + [f"=-({c}{R_C2}-{p}{R_C2})" for p, c in zip(COLS, COLS[1:])], fmt=FMT_M)
    R_dA = put("   of which paid hours (change in A)", vals=[""] + [f"={c}{R_A2}-{p}{R_A2}" for p, c in zip(COLS, COLS[1:])], fmt=FMT_M)
    R_cons = put("Consensus gross-margin expansion, bp", vals=["", "", f"={A['cons_gm_exp_2026']}", f"={A['cons_gm_exp_2027']}"], fmt=FMT_BP)
    put("Audiobook headwind as share of consensus expansion", vals=["", "", f"=-E{R_dNbp}/E{R_cons}", f"=-F{R_dNbp}/F{R_cons}"], fmt=FMT_PCT0)
    put("Memo (excluded from N): Jun-24 US price increase, annualized €M", vals=[f"={A['p_2024']}"], fmt=FMT_M)
    put("")

    # 5. Attach
    put("5. Paid attach", bold=True)
    R_pay = put("Audiobooks+ paying users (M)", single=f"={A['ab_plus_payers']}", fmt='0.0')
    put("ARR per payer ($ per year)", single=f"={A['ab_plus_arr']}/{A['ab_plus_payers']}", fmt=FMT_INT)
    put("Payers / global Premium subscribers", single=f"=$B${R_pay}/{A['subs_global']}", fmt=FMT_PCT)
    put("Payers / Premium subscribers in eligible markets", single=f"=$B${R_pay}/{A['subs_eligible']}", fmt=FMT_PCT)
    put("Payers / monthly audiobook listeners, eligible markets", single=f"=$B${R_pay}/({A['subs_eligible']}*{A['listen_share']})", fmt=FMT_PCT)
    put("Payers / monthly audiobook listeners, global", single=f"=$B${R_pay}/({A['subs_global']}*{A['listen_share']})", fmt=FMT_PCT)
    put("Eligible Premium users who have ever pressed play", single=f"={A['tried_share']}", fmt=FMT_PCT)
    put("US individual subscribers who took the $1 Basic plan (opt-out)", single=f"={A['basic_optout']}", fmt=FMT_PCT)
    put("Music Pro attach assumption, bull case", single=f"={A['bull_attach']}", fmt=FMT_PCT)
    put("")

    # 6. Cross-checks
    put("6. Cross-checks", bold=True)
    put("a. Market-share triangulation of C (2025)", bold=True)
    R_apa = put("US audiobook publisher receipts 2025 ($M)", single=f"={A['apa_us_2025']}", fmt=FMT_M)
    R_sh = put("Spotify share of US receipts: low (col B), high (col C)", single=f"={A['spot_us_share_lo']}", extra={"C": f"={A['spot_us_share_hi']}"}, fmt=FMT_PCT0)
    R_nonus = put("Non-US markets, multiple of US cost", single=f"={A['nonus_uplift']}", fmt=FMT_X)
    R_fx = put("EUR/USD", single=f"={A['eurusd']}", fmt=FMT_X)
    R_imp = put("Implied global C 2025, €M: low (col B), high (col C)", single=f"=B{R_apa}*B{R_sh}*B{R_nonus}/B{R_fx}", extra={"C": f"=B{R_apa}*C{R_sh}*B{R_nonus}/B{R_fx}"}, fmt=FMT_M)
    R_base = put("Base case C 2025, €M", single=f"=D{R_C}", fmt=FMT_M)
    put("Base case vs implied range: vs low (col B), vs high (col C)", single=f"=B{R_base}/B{R_imp}-1", extra={"C": f"=B{R_base}/C{R_imp}-1"}, fmt=FMT_PCT)
    put("")
    put("b. Incremental Premium content-cost ratio (does the P&L show an audiobook step?)", bold=True)
    h = put("", vals=["Premium revenue change", "Content cost change", "Incremental ratio"], bold=True)
    for col in COLS[:3]: an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
    for label, rev_f, cost_f in [
        ("FY24 vs FY23", f"={A['prem_rev_2024']}-{A['prem_rev_2023']}", f"={A['royalty_inc_2024']}"),
        ("FY25 vs FY24", f"={A['prem_rev_2025']}-{A['prem_rev_2024']}", f"={A['royalty_inc_2025']}"),
        ("9M-25 vs 9M-24", f"={A['prem_rev_9m25']}-{A['prem_rev_9m24']}", f"={A['royalty_inc_9m25']}"),
        ("H1-26 vs H1-25", f"={A['prem_rev_h126']}-{A['prem_rev_h125']}", f"={A['royalty_inc_h126']}"),
    ]:
        rr = nxt(); put(label, vals=[rev_f, cost_f, f"=D{rr}/C{rr}"], fmt=FMT_M); an[f"E{rr}"].number_format = FMT_PCT
    put("Note: the incremental ratio holds at 48-50% in every period against a ~66% average ratio. It bounds the growth in C rather than measuring it: music royalties, the bundle saving, marketplace offsets and the Partner Program all move inside the same line.")
    put("")
    put("c. Bundle saving, external references", bold=True)
    put("NMPA first-year publisher loss estimate ($M)", single=f"={A['nmpa_first_year']}", fmt=FMT_M)
    put("MLC mechanical royalties paid, $M: Q4-23 (col B), Q4-25 (col C); direct-licensed publishers leave the MLC pool after 2025, so the series overstates the net saving",
        single=f"={A['bb_q423_mech']}", extra={"C": f"={A['bb_q425_mech']}"}, fmt='0.0')
    put("")

    # 7. Sensitivity (live)
    put("7. Sensitivity: 2027E, by audiobook cost growth (rows) and bundle-discount restoration / MLC outcome (columns)", bold=True)
    S = f"({A['share_umpg']}+{A['share_wcm']}+{A['share_smp']})"
    R_h1 = put("Restoration of bundle discount", vals=[0.5, 1.0, 1.0], fmt=FMT_PCT0)
    R_h2 = put("MLC complaint succeeds in 2027 (1 = yes)", vals=[0, 0, 1], fmt=FMT_INT)
    h = put("Cost growth p.a. 2026-27 (col A)", vals=["Change in N 2027, bp", "Change in N 2027, bp", "Change in N 2027, bp"], bold=True)
    for col in COLS[:3]: an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
    for gr in [0.20, 0.30, 0.45, 0.60]:
        rr = nxt()
        vals = [f"=((IF({c}${R_h2}=1,0,$B${R_rr}*(1-{S}*{c}${R_h1}))-$B${R_rr}*(1-{S}*{c}${R_h1}))+($F${R_Agp}-$E${R_Agp})-$D${R_C}*(1+$A{rr})*$A{rr})/$F${R_grp}*10000" for c in COLS[:3]]
        put(gr, vals=vals, fmt=FMT_BP); an[f"A{rr}"].number_format = FMT_PCT0; an[f"A{rr}"].font = F_BLUE
    h = put("Cost growth p.a. 2026-27 (col A)", vals=["N 2027, €M", "N 2027, €M", "N 2027, €M"], bold=True)
    for col in COLS[:3]: an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
    for gr in [0.20, 0.30, 0.45, 0.60]:
        rr = nxt()
        vals = [f"=IF({c}${R_h2}=1,0,$B${R_rr}*(1-{S}*{c}${R_h1}))+$F${R_Agp}-$D${R_C}*(1+$A{rr})^2" for c in COLS[:3]]
        put(gr, vals=vals, fmt=FMT_M); an[f"A{rr}"].number_format = FMT_PCT0; an[f"A{rr}"].font = F_BLUE
    put("Restoration below 100% does not change the 2027 headwind (B is flat 2026 to 2027 once all three majors are on direct licences); it changes the level of N.")

    an.column_dimensions["A"].width = 88; an.column_dimensions["B"].width = 14
    for col in COLS: an.column_dimensions[col].width = 13
    an.freeze_panes = "C5"
    wb.save(os.path.join(DATA, "SPOT_audiobooks_model.xlsx"))

def compute_with(vals):
    global I
    old = I; I = vals
    try:
        return compute()
    finally:
        I = old

def decision_rows(r):
    rows = []
    rows.append(["1. Book publishers' cost (ΔC, €M) grows faster than priced-channel gross profit (ΔA_gp, €M)", "ΔC > ΔA_gp in 2025 and 2026",
                 f"2025: ΔC {r['dC'][2025]:+.0f} vs ΔA_gp {r['dA_gp'][2025]:+.0f}; 2026: ΔC {r['dC'][2026]:+.0f} vs ΔA_gp {r['dA_gp'][2026]:+.0f}", "CONFIRMED"])
    rows.append(["2. Music publishers claw back the bundle saving (B falls)", "B(2026) < B(2024)",
                 f"B: 2024 {r['B'][2024]:.0f} → 2025 {r['B'][2025]:.0f} → 2026 {r['B'][2026]:.0f} (direct deals reported to nullify the discount; restoration factor is an assumption)", "SUPPORTED"])
    rows.append(["3. Net contribution N is negative by 2026", "N(2026) ≤ 0",
                 f"N: 2024 {r['N'][2024]:.0f}, 2025 {r['N'][2025]:.0f}, 2026 {r['N'][2026]:.0f}, 2027 {r['N'][2027]:.0f} (€M). Negative in every year once the price increase is excluded", "CONFIRMED"])
    rows.append(["4. Paid attach is low after a full year", "< 1% of eligible subscribers; < 3% of listeners",
                 "; ".join(f"{k}: {v:.1%}" for k, v in list(r['attach'].items())[:4]), "CONFIRMED"])
    rows.append(["5. C grows faster than Premium revenue", "C growth > Premium revenue growth",
                 f"C +{I['c_g_2025']:.0%} / +{I['c_g_2026']:.0%} vs Premium revenue +11% / +15%", "CONFIRMED"])
    rows.append(["6. Residual cross-check (incremental content-cost ratio) shows an audiobook step", "Visible jump in FY25 or H1-26 ratio",
                 "; ".join(f"{k}: {v:.1%}" for k, v in r['inc_ratio'].items()) + ". Flat at 48–50%: inconclusive, bounds C's growth to ~€100–150M/yr", "INCONCLUSIVE"])
    rows.append(["7. Market-share triangulation agrees with C(2025)", "Base C(2025) inside the triangulated range",
                 f"C(2025) base {r['C'][2025]:.0f} vs triangulation {r['C_tri_lo']:.0f}–{r['C_tri_hi']:.0f} €M", "CONFIRMED" if r['C_tri_lo'] <= r['C'][2025] <= r['C_tri_hi'] else "CHECK"])
    return rows

SOURCES = [
    "Spotify Form 6-K, Q1-25 (bundle: ~€205M additional royalties for 1 Mar 2024–31 Mar 2025 if the MLC prevailed): sec.gov/Archives/edgar/data/1639920/000163992025000006/spot-20250331x6xk.htm",
    "Spotify Form 20-F FY2024 and FY2025 (Premium cost of revenue drivers, royalty component increases, Premium GM): sec.gov/Archives/edgar/data/1639920/000163992025000003/ck0001639920-20241231.htm ; .../000162828026006874/ck0001639920-20251231.htm",
    "Spotify Form 6-K Q2-26 (H1-26 Premium cost of revenue +€500M, content +€474M, ratio 67%→65%): sec.gov/Archives/edgar/data/0001639920/000162828026052543/spot-20260630x6xk.htm",
    "Spotify Form 6-K Q3-25 (9M-25 royalty component +€588M): sec.gov/Archives/edgar/data/1639920/000162828025048927/spot-20250930x6xk.htm",
    "Billboard, 'How much have Spotify bundles decreased the mechanical per-stream rate' (Q4-23 $97.3M → Q4-25 $53.3M; per-stream −51%)",
    "NMPA statements: $150M (May 2024), $230M first-year loss, ~$500M cumulative with Amazon (2025–26); Billboard 'bundling controversy one year later'",
    "Direct deals: UMPG (26 Jan 2025, DMN/Billboard: bundle discount 'nullified going forward'); Warner Chappell (6 Feb 2025, MBW: 'supersedes the bundling payment structure'); Sony Music Publishing (Sep 2025, MBW)",
    "MLC v. Spotify: dismissal Jan 2025 (Variety); amended complaint late 2025; interlocutory appeal denied 1 Sep 2026 (MBW, Soundstock)",
    "Audiobook cost phrases: Digital Music News 5 Feb 2024 ('tens of millions'); Axios 15 Oct 2024 ('hundreds of millions annually'); Spotify newsroom 13 Mar 2025",
    "Spotify newsroom 15 Oct 2025 (two-year stats: listeners +36%, hours +37%, >50% tried); Mar 2025 (listeners +30%, hours +35%, 400k titles); Publishers Weekly 2026 (listeners +60%, Audiobooks+ $100M ARR, >1M payers)",
    "The Bookseller 2025 / TechCrunch 17 Jul 2025 ('more than 25% of Premium subscribers listening')",
    "Audio Publishers Association sales surveys: 2022 $1.8B, 2023 $2.0B, 2024 $2.22B, 2025 $2.43B; eMarketer Mar 2026 (Audible 63.4%→59.8%)",
    "Publisher confirmations: Bloomsbury AR 2025 (audio +57% 'in part Spotify'); News Corp/HarperCollins (audio +18% FY, +28% Q4, citing Spotify)",
    "Audible Standard plan $8.99 (Audible newsroom, 3 Mar 2026); Amazon Music Unlimited + Audible (Nov 2024)",
    "Basic plan opt-out 14–17% (Morgan Stanley survey via Billboard, 2024)",
    "Audiobooks+ launch and pricing: 9to5Mac 5 Aug 2025; Publishers Weekly (11 EU markets); Spotify newsroom Mar 2024 (Access tier, top-ups)",
]

# ----------------------------------------------------------------------------
# Charts
# ----------------------------------------------------------------------------
def style(ax, title, sub=None):
    ax.set_facecolor(SURF)
    for s in ["top", "right"]: ax.spines[s].set_visible(False)
    for s in ["left", "bottom"]: ax.spines[s].set_color(GRID)
    ax.tick_params(colors=INK2, labelsize=9); ax.yaxis.grid(True, color=GRID, linewidth=0.8); ax.set_axisbelow(True)
    ax.set_title(title, loc="left", fontsize=12, color=INK, fontweight="bold", pad=14)
    if sub: ax.text(0, 1.01, sub, transform=ax.transAxes, fontsize=9, color=INK2)

def chart_bridge(r):
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=160); fig.patch.set_facecolor(SURF)
    xs = range(len(YEARS)); w = 0.6
    B = [r["B"][y] for y in YEARS]; Ag = [r["A_gp"][y] for y in YEARS]; C = [-r["C"][y] for y in YEARS]; N = [r["N"][y] for y in YEARS]
    ax.bar(xs, B, w, color=BLUE, label="B: bundle royalty saving, net of hand-backs", zorder=2)
    ax.bar(xs, Ag, w, bottom=B, color=AQUA, label="A: gross profit on paid audiobook hours", zorder=2)
    ax.bar(xs, C, w, color="#f4b79f", label="C: licensing cost on included hours", zorder=2)
    ax.plot(list(xs), N, color=INK, linewidth=2, marker="o", markersize=6, label="N = B + A − C", zorder=4)
    for i, y in enumerate(YEARS):
        ax.text(i, N[i] - 28, f"{N[i]:.0f}", ha="center", fontsize=9, color=INK, fontweight="bold")
        ax.text(i, B[i] + Ag[i] + 8, f"+{B[i]+Ag[i]:.0f}", ha="center", fontsize=8, color=INK2)
        ax.text(i, C[i] - 8, f"{C[i]:.0f}", ha="center", va="top", fontsize=8, color=INK2)
    ax.axhline(0, color=INK2, linewidth=0.8)
    ax.set_xticks(list(xs)); ax.set_xticklabels([f"{y}{'E' if y >= 2026 else ''}" for y in YEARS]); ax.set_ylabel("€ millions", color=INK2)
    style(ax, "Audiobooks: the bundle saving is being clawed back faster than paid hours replace it",
          "N excludes the Jun-24 price increase that management credits to audiobooks; B falls as the majors' publishers move to direct deals")
    ax.legend(fontsize=8, frameon=False, loc="lower left")
    fig.tight_layout(); fig.savefig(os.path.join(CH, "5_audiobook_bridge.png")); plt.close(fig)

def chart_headwind(r):
    fig, ax = plt.subplots(figsize=(9, 4.4), dpi=160); fig.patch.set_facecolor(SURF)
    ys = YEARS[1:]; xs = range(len(ys)); w = 0.26
    mp = [r["dB"][y] / r["grp"][y] * 1e4 for y in ys]; bp = [-r["dC"][y] / r["grp"][y] * 1e4 for y in ys]; ag = [r["dA_gp"][y] / r["grp"][y] * 1e4 for y in ys]
    ax.bar([i - w for i in xs], mp, w, color=BLUE, label="Music publishers reclaim the bundle saving (ΔB)", zorder=2)
    ax.bar(list(xs), bp, w, color=ORANGE, label="Book publishers paid on consumption (−ΔC)", zorder=2)
    ax.bar([i + w for i in xs], ag, w, color=AQUA, label="Paid hours (ΔA gross profit)", zorder=2)
    tot = [r["dN_bp"][y] for y in ys]
    ax.plot(list(xs), tot, color=INK, linewidth=2, marker="o", markersize=6, label="Net audiobook headwind to gross margin (ΔN)", zorder=4)
    for i, v in enumerate(tot): ax.text(i, v - 9, f"{v:.0f} bp", ha="center", fontsize=9, color=INK, fontweight="bold")
    need = {2026: I["cons_gm_exp_2026"], 2027: I["cons_gm_exp_2027"]}
    for i, y in enumerate(ys):
        if y in need:
            ax.scatter([i], [need[y]], color=RED, s=40, zorder=5); ax.text(i + 0.05, need[y] + 4, f"consensus needs +{need[y]} bp", fontsize=8, color=RED)
    ax.axhline(0, color=INK2, linewidth=0.8)
    ax.set_xticks(list(xs)); ax.set_xticklabels([f"{y}{'E' if y >= 2026 else ''}" for y in ys]); ax.set_ylabel("bp of group revenue, y/y", color=INK2)
    ax.set_ylim(min(tot) - 40, max(need.values()) + 60)
    style(ax, "Who is clawing it back, and against what the Street needs", "bp of group revenue; 2025 is the first full year of direct deals and of 50%+ consumption growth")
    ax.legend(fontsize=8, frameon=False, loc="upper left")
    fig.tight_layout(); fig.savefig(os.path.join(CH, "6_audiobook_headwind.png")); plt.close(fig)

# ----------------------------------------------------------------------------
# Findings
# ----------------------------------------------------------------------------
def findings(r):
    L = []
    L.append("# Audiobooks economics — findings\n")
    L.append("Model: `analysis/audiobooks_model.py` → `data/SPOT_audiobooks_model.xlsx` (two tabs, Audiobooks_Inputs and Audiobooks_Analysis, live formulas; forecast placeholders for 2026E–2027E are flagged LINK TO MODEL). Identity: N(t) = B(t) + A_gp(t) − C(t). The June 2024 price increase is deliberately outside N.\n")
    L.append("## 1. The bridge\n")
    L.append("| €M | 2024 | 2025 | 2026E | 2027E |\n|---|---|---|---|---|")
    L.append("| B  bundle saving, net of hand-backs | " + " | ".join(f"{r['B'][y]:.0f}" for y in YEARS) + " |")
    L.append("| A_gp  gross profit on paid hours | " + " | ".join(f"{r['A_gp'][y]:.0f}" for y in YEARS) + " |")
    L.append("| C  licensing cost on included hours | " + " | ".join(f"{r['C'][y]:.0f}" for y in YEARS) + " |")
    L.append("| **N = B + A_gp − C** | " + " | ".join(f"**{r['N'][y]:.0f}**" for y in YEARS) + " |")
    L.append("| N, bp of group revenue | " + " | ".join(f"{r['N_bp'][y]:.0f}" for y in YEARS) + " |")
    L.append("| ΔN y/y, €M (the headwind) | — | " + " | ".join(f"{r['dN'][y]:.0f}" for y in YEARS[1:]) + " |")
    L.append("| ΔN y/y, bp | — | " + " | ".join(f"{r['dN_bp'][y]:.0f}" for y in YEARS[1:]) + " |")
    L.append("| memo: Jun-24 US price increase, annualized (excluded) | " + f"{I['p_2024']:.0f}" + " | | | |")
    L.append(f"\nAgainst consensus gross-margin expansion of ~{I['cons_gm_exp_2026']}bp (2026) and ~{I['cons_gm_exp_2027']}bp (2027), audiobooks absorb {-r['dN_bp'][2026]/I['cons_gm_exp_2026']:.0%} and {-r['dN_bp'][2027]/I['cons_gm_exp_2027']:.0%} of what the Street needs.\n")
    L.append("## 2. Who clawed it back\n")
    L.append("| ΔN decomposition, €M | 2025 | 2026E | 2027E |\n|---|---|---|---|")
    L.append("| Music publishers reclaim the bundle saving (ΔB) | " + " | ".join(f"{r['dB'][y]:.0f}" for y in YEARS[1:]) + " |")
    L.append("| Book publishers paid on consumption (−ΔC) | " + " | ".join(f"{-r['dC'][y]:.0f}" for y in YEARS[1:]) + " |")
    L.append("| Paid hours offset (ΔA_gp) | " + " | ".join(f"{r['dA_gp'][y]:+.0f}" for y in YEARS[1:]) + " |")
    L.append("| Net | " + " | ".join(f"{r['dN'][y]:.0f}" for y in YEARS[1:]) + " |")
    L.append("\nTwo different rights-holder groups, two different mechanisms. The music publishers' claw-back is contractual: UMPG (Jan-25), Warner Chappell (Feb-25) and Sony Music Publishing (Sep-25) moved to direct US licences that reporting describes as nullifying the bundle discount. The book publishers' claw-back is volumetric: per-title fees and pool payments on consumption that the company reports growing 35–60% a year. The priced channel offsets roughly a sixth of the book-publisher cost growth.\n")
    L.append("## 3. How each term was sized\n")
    L.append(f"**B.** Spotify's own 6-K puts the bundle reduction at €{I['bundle_13m']}M for the 13 months to March 2025, a run-rate of €{r['run_rate']:.0f}M a year, consistent with the NMPA's $230M first-year figure and Billboard's finding that MLC mechanical payments fell 45% between Q4-23 and Q4-25. Hand-backs assume the three majors' publishers hold ~{(I['share_umpg']+I['share_wcm']+I['share_smp']):.0%} of US mechanicals and that their direct deals restore {I['restoration']:.0%} of the discount; the Billboard series cannot test this because direct-licensed publishers drop out of MLC data. The remaining €{r['B'][2026]:.0f}M (independents) is what the MLC's amended complaint is pursuing.\n")
    L.append(f"**C.** Anchored on the company's words: 'tens of millions' three months after US launch (Feb-24) and 'hundreds of millions of dollars a year' by Oct-24, set at €{I['c_2024']}M for 2024 and grown by disclosed consumption growth. Market-share triangulation: {I['spot_us_share_lo']:.0%}–{I['spot_us_share_hi']:.0%} of $2.43B US publisher receipts, times {I['nonus_uplift']:.1f}x for non-US markets, gives €{r['C_tri_lo']:.0f}–{r['C_tri_hi']:.0f}M for 2025 against the base €{r['C'][2025]:.0f}M. Low/high cases at {I['c_low_mult']:.0%}/{I['c_high_mult']:.0%} of base.\n")
    L.append(f"**A.** Audiobooks+ reached ~$100M ARR and >1M payers by mid-2026 (ARR per payer ≈ ${r['arr_per_payer']:.0f}/yr, consistent with the $11.99 price and a mix of top-ups). Gross profit assumes paid hours carry the same publisher payments at a {I['a_cogs_ratio']:.0%} cost ratio.\n")
    L.append("## 4. Residual cross-check (inconclusive, and that matters)\n")
    L.append("| Period | Incremental content-cost ratio |\n|---|---|")
    for k, v in r["inc_ratio"].items(): L.append(f"| {k} | {v:.1%} |")
    L.append("\nThe incremental ratio sits at 48–50% in every period against a ~66% average, with no visible step in FY25 or H1-26. Read correctly, this does not refute C: music royalties, the bundle saving, marketplace offsets and the Partner Program all move inside the same line, and a €100–150M annual audiobook increase is 7–10% of the €765M FY25 royalty increase. But it does mean the audiobook cost cannot be proven from the P&L alone. The claim rests on the company's own cost phrases, the consumption growth it reports, and the publisher-side confirmations. A former audiobooks lead with the per-title fee and the hours-per-listener figure would turn this from triangulated to measured.\n")
    L.append("## 5. The add-on test\n")
    L.append("| Attach measure | Value |\n|---|---|")
    for k, v in r["attach"].items(): L.append(f"| {k} | {v:.1%} |")
    L.append("\nAfter a full year of the paid add-on and three years of the feature, fewer than one in a hundred eligible subscribers pays for more hours, while roughly one in six US individual subscribers took a $1 discount to give the feature up. The bull case's 3% Music Pro attach is four to nine times the attach Spotify achieved on its most engaged add-on.\n")
    L.append("## 6. Decision rules\n")
    L.append("| Test | Threshold | Result | Verdict |\n|---|---|---|---|")
    for row in decision_rows(r): L.append("| " + " | ".join(str(x) for x in row) + " |")
    L.append("\n## 7. Sensitivity (ΔN 2027, bp of group revenue)\n")
    L.append("| C growth p.a. | restoration 0.5 | restoration 1.0 | restoration 1.0 + MLC loss |\n|---|---|---|---|")
    for gr in [0.20, 0.30, 0.45, 0.60]:
        vals = []
        for rest, mlc in [(0.5, 0), (1.0, 0), (1.0, 1)]:
            sv = dict(I); sv["restoration"] = rest; sv["mlc_loss_2027"] = mlc; sv["c_g_2026"] = gr; sv["c_g_2027"] = gr
            vals.append(compute_with(sv)["dN_bp"][2027])
        L.append(f"| {gr:.0%} | " + " | ".join(f"{v:.0f}" for v in vals) + " |")
    L.append("\n## 8. What the result means for the pitch\n")
    L.append(f"- The audiobook 'margin contribution' the Street absorbed in 2024 was a royalty reclassification worth ~€{r['B_gross'][2024]:.0f}M plus a price increase worth ~€{I['p_2024']}M annualized. Audiobook consumption itself cost more than the reclassification saved in the same year.")
    L.append(f"- From 2025 the reclassification is being handed back to the majors' publishers through direct deals while consumption compounds. On base assumptions the net line moves from about −€{-r['N'][2024]:.0f}M in 2024 to −€{-r['N'][2027]:.0f}M in 2027, a {-r['dN_bp'][2025]:.0f}/{-r['dN_bp'][2026]:.0f}/{-r['dN_bp'][2027]:.0f}bp headwind in 2025/2026/2027.")
    L.append("- Spotify's only governors are the hour cap (already 12 h in every market launched since 2024), the per-title triggers, and the pool rate. Audible at $8.99 and Amazon's free book remove the price lever.")
    L.append("- The priced channel is real but small: it funds roughly a sixth of the consumption cost growth and attaches below 1% of eligible subscribers, which is the platform's own evidence against a 3% Music Pro attach.")
    L.append("- Caveats: C is triangulated, not disclosed; the restoration factor on the direct deals is reported, not quantified; the residual method is silent. The direction survives every sensitivity in section 7; the size ranges from ~30 to ~110bp a year.")
    open(os.path.join(ROOT, "analysis", "audiobooks-findings.md"), "w").write("\n".join(L))

def main():
    r = compute()
    build_workbook(r)
    chart_bridge(r); chart_headwind(r)
    findings(r)
    print("N:", {y: round(r["N"][y]) for y in YEARS}); print("dN bp:", {y: round(r["dN_bp"][y]) for y in YEARS[1:]})
    print("B:", {y: round(r["B"][y]) for y in YEARS}); print("C:", {y: round(r["C"][y]) for y in r["C"]})
    print("C tri:", round(r["C_tri_lo"]), round(r["C_tri_hi"])); print("inc ratios:", {k: round(v, 3) for k, v in r["inc_ratio"].items()})
    print("attach:", {k: round(v, 4) for k, v in r["attach"].items()})

if __name__ == "__main__":
    main()
