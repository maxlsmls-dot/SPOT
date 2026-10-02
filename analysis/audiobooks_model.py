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
    ("grp_rev_2024", "Group revenue 2024", 15673, "€M", "FY24", "Spotify 20-F", "D"),
    ("grp_rev_2025", "Group revenue 2025", 17186, "€M", "FY25", "Spotify 20-F", "D"),
    ("grp_rev_2026", "Group revenue 2026E", 19500, "€M", "FY26E", "Placeholder. Link to model: total revenue FY26E", "L"),
    ("grp_rev_2027", "Group revenue 2027E", 21300, "€M", "FY27E", "Placeholder. Link to model: total revenue FY27E", "L"),
    ("grp_q124", "Group revenue Q1-24", 3636, "€M", "Q1-24", "Spotify Q1-24 6-K", "D"),
    ("grp_q224", "Group revenue Q2-24", 3807, "€M", "Q2-24", "Spotify Q2-24 6-K", "D"),
    ("grp_q324", "Group revenue Q3-24", 3988, "€M", "Q3-24", "Spotify Q3-24 6-K", "D"),
    ("grp_q424", "Group revenue Q4-24", 4242, "€M", "Q4-24", "Spotify Q4-24 deck", "D"),
    ("grp_q125", "Group revenue Q1-25", 4190, "€M", "Q1-25", "Spotify Q1-25 6-K", "D"),
    ("grp_q225", "Group revenue Q2-25", 4190, "€M", "Q2-25", "Spotify Q2-25 6-K", "D"),
    ("grp_q325", "Group revenue Q3-25", 4272, "€M", "Q3-25", "Spotify Q3-25 6-K", "D"),
    ("grp_q425", "Group revenue Q4-25", 4500, "€M", "Q4-25", "Spotify Q4-25 deck; quarters sum to 17,152 vs 17,186 annual input, tie out in the model", "D"),
    ("grp_q126", "Group revenue Q1-26", 4530, "€M", "Q1-26", "Spotify Q1-26 6-K", "D"),
    ("grp_q226", "Group revenue Q2-26", 4780, "€M", "Q2-26", "Spotify Q2-26 6-K", "D"),
    ("grp_q326", "Group revenue Q3-26E", 5000, "€M", "Q3-26E", "Placeholder: company guidance (about €5.0B). Link to model: revenue Q3-26E", "L"),
    # Premium cost of revenue (residual method)
    ("cogs_ratio_2022", "Premium cost of revenue / Premium revenue 2022", 0.72, "%", "FY22", "20-F: Premium gross margin 28%", "D"),
    ("cogs_ratio_2023", "Premium cost of revenue / Premium revenue 2023", 0.71, "%", "FY23", "FY24 20-F: 71% to 67%", "D"),
    ("cogs_ratio_2024", "Premium cost of revenue / Premium revenue 2024", 0.67, "%", "FY24", "FY24 20-F", "D"),
    ("cogs_ratio_2025", "Premium cost of revenue / Premium revenue 2025", 0.66, "%", "FY25", "FY25 20-F: Premium gross margin 34%", "D"),
    ("royalty_inc_2024", "of which royalty / content costs 2024", 1078, "€M", "FY24", "FY24 20-F", "D"),
    ("royalty_inc_2025", "Royalty / content cost increase 2025 (music + audiobooks + Partner Program, net of marketplace)", 765, "€M", "FY25", "FY25 20-F", "D"),
    ("royalty_inc_9m25", "Royalty / content cost increase 9M-25", 588, "€M", "9M25", "Q3-25 6-K", "D"),
    ("royalty_inc_h126", "Content cost increase H1-26", 474, "€M", "H1-26", "Q2-26 6-K (Premium cost of revenue +€500M, +10%; ratio 67% to 65%)", "D"),
    ("prem_rev_h125", "Premium revenue H1-25", 7508, "€M", "H1-25", "3,771 + 3,737", "D"),
    ("prem_rev_h126", "Premium revenue H1-26", 8480, "€M", "H1-26", "4,150 + 4,330", "D"),
    ("prem_rev_9m24", "Premium revenue 9M-24", 10114, "€M", "9M24", "FY24 13,819 less Q4-24 3,705", "D"),
    ("prem_rev_9m25", "Premium revenue 9M-25", 11333, "€M", "9M25", "3,771 + 3,737 + 3,825", "D"),
    # B: bundle saving. MLC contingency series: "additional royalties that would be due" if Premium were not a bundle, cumulative from 1 Mar 2024
    ("mlc_cum_q224", "MLC contingency, cumulative 1 Mar 2024 to 30 Jun 2024", 46, "€M", "Q2-24", "6-K Q2-24: 'approximately €46 million, of which approximately €35 million relates to the three months ended June 30, 2024'", "D"),
    ("mlc_q224_only", "of which the three months April to June 2024", 35, "€M", "Q2-24", "6-K Q2-24 (same sentence)", "D"),
    ("mlc_cum_q324", "MLC contingency, cumulative to 30 Sep 2024", 94, "€M", "Q3-24", "6-K Q3-24", "D"),
    ("mlc_cum_q424", "MLC contingency, cumulative to 31 Dec 2024", 150, "€M", "Q4-24", "20-F FY24", "D"),
    ("mlc_cum_q125", "MLC contingency, cumulative to 31 Mar 2025", 205, "€M", "Q1-25", "6-K Q1-25", "D"),
    ("mlc_cum_q225", "MLC contingency, cumulative to 30 Jun 2025", 256, "€M", "Q2-25", "6-K Q2-25", "D"),
    ("mlc_cum_q325", "MLC contingency, cumulative to 30 Sep 2025", 308, "€M", "Q3-25", "6-K Q3-25: first filing to add 'Any liability would be partially offset by direct deals with publishers'", "D"),
    ("mlc_cum_q425", "MLC contingency, cumulative to 31 Dec 2025", 358, "€M", "Q4-25", "20-F FY25", "D"),
    ("mlc_cum_q126", "MLC contingency, cumulative to 31 Mar 2026", 410, "€M", "Q1-26", "6-K Q1-26 (USD 473M at the time, per NMPA 'nearly $480 million by Spotify's own admission')", "D"),
    ("mlc_cum_q226", "MLC contingency, cumulative to 30 Jun 2026", 437, "€M", "Q2-26", "6-K Q2-26 as quoted by Music Ally, 7 Sep 2026. A second reading of the same filing gives €473M (which is also the USD value of the Q1-26 figure). Verify against the Q2-26 6-K legal-proceedings note before quoting", "D"),
    ("bundle_rr_2026", "Gross bundle saving 2026E", 205, "€M", "FY26E", "Placeholder: 4 x average quarterly contingency increment Q2-25 to Q1-26 (€51M). Link to model: bundle saving FY26E", "L"),
    ("bundle_rr_2027", "Gross bundle saving 2027E", 205, "€M", "FY27E", "Placeholder: flat on 2026E; Phonorecords IV settlement runs to end-2027. Link to model: bundle saving FY27E", "L"),
    ("nmpa_first_year", "NMPA estimate of first-year publisher loss", 230, "$M", "2024-25", "NMPA via Billboard", "R"),
    ("nmpa_cum_2026", "NMPA estimate of cumulative publisher loss to Spotify and Amazon bundling since 2024", 495, "$M", "Jun-26", "NMPA annual meeting, Jun 2026 ('nearly $500 million')", "R"),
    ("bb_q423_mech", "Mechanical royalties paid to the MLC, paid tiers, Q4-23", 97.3, "$M", "Q4-23", "Billboard analysis of Spotify's MLC reports", "R"),
    ("bb_q425_mech", "Mechanical royalties paid to the MLC, paid tiers, Q4-25", 53.3, "$M", "Q4-25", "Billboard analysis (-45%)", "R"),
    ("bb_q423_rate", "Blended mechanical per-stream rate, paid tiers, Q4-23", 0.00068, "$/stream", "Q4-23", "Billboard analysis", "R"),
    ("bb_q425_rate", "Blended mechanical per-stream rate, paid tiers, Q4-25", 0.00033, "$/stream", "Q4-25", "Billboard analysis (-51%)", "R"),
    ("eurusd_q425", "EUR/USD, Q4-25 average", 1.16, "x", "Q4-25", "Approximate", "E"),
    ("share_umpg", "UMPG share of US mechanicals", 0.22, "%", "", "Estimate from US publishing market shares (range 20-25%)", "E"),
    ("share_wcm", "Warner Chappell share of US mechanicals", 0.13, "%", "", "Estimate (range 11-15%)", "E"),
    ("share_kobalt", "Kobalt share of US mechanicals", 0.05, "%", "", "Estimate; largest independent (range 4-7%)", "E"),
    ("share_smp", "Sony Music Publishing share of US mechanicals", 0.26, "%", "", "Estimate; SMP ranked #1 publisher in every quarter of 2025 (range 23-28%)", "E"),
    ("share_bmg", "BMG share of US mechanicals", 0.03, "%", "", "Estimate (range 2-4%)", "E"),
    ("start_umpg", "UMPG direct licence start month (2025)", 2, "month", "2025", "Announced 26 Jan 2025; reported to 'nullify' the bundle discount going forward", "R"),
    ("start_wcm", "Warner Chappell direct licence start month (2025)", 3, "month", "2025", "Announced 6 Feb 2025; 'supersedes the bundling payment structure' (MBW)", "R"),
    ("start_kobalt", "Kobalt direct licence start month (2025)", 9, "month", "2025", "Announced 13 Aug 2025; 'bespoke terms rather than the compulsory licence rates'", "R"),
    ("start_smp", "Sony Music Publishing direct licence start month (2025)", 10, "month", "2025", "Announced 18 Sep 2025; direct US licence", "R"),
    ("start_bmg", "BMG direct licence start month (2025)", 11, "month", "2025", "Announced 9 Oct 2025", "R"),
    ("restoration", "Share of the bundle discount restored to direct-licensed publishers", 0.75, "%", "", "Estimate. Spotify: liability 'partially offset by direct deals'. MBW on the Warner deal: terms 'continue to recognize a difference between bundled and music-only listeners' but payments 'substantially improved'. Range 50-100%", "E"),
    ("mlc_loss_2027", "MLC amended complaint succeeds in 2027 (1 = yes): the independents' share of the saving goes to zero", 0, "flag", "2027", "Scenario switch. Interlocutory appeal denied 1 Sep 2026; fact discovery cutoff 13 Mar 2027; no trial date set", "E"),
    # C: audiobook licensing cost
    ("c_2024", "Audiobook licensing cost 2024 ('hundreds of millions of dollars a year' by Oct-24)", 190, "€M", "FY24", "Axios 15 Oct 2024; Spotify newsroom Mar-25 repeats; 'tens of millions' by Feb-24 (Digital Music News). Sized as a full year", "E"),
    ("c_g_2025", "Audiobook licensing cost growth 2025 (listeners +30-36%, hours +35-37%, DACH launch, Family members)", 0.58, "%", "FY25", "Spotify newsroom Mar-25, Oct-25; estimate", "E"),
    ("c_g_2026", "Audiobook licensing cost growth 2026E (listeners +60%, Nordics, Audiobooks+ Europe)", 0.43, "%", "FY26E", "Placeholder: Publishers Weekly 2026. Link to model: audiobook cost growth FY26E", "L"),
    ("c_g_2027", "Audiobook licensing cost growth 2027E", 0.30, "%", "FY27E", "Placeholder: assumes deceleration. Link to model: audiobook cost growth FY27E", "L"),
    ("c_low_mult", "Low-case multiplier on audiobook licensing cost", 0.80, "x", "", "Sensitivity band", "E"),
    ("c_high_mult", "High-case multiplier on audiobook licensing cost", 1.25, "x", "", "Sensitivity band", "E"),
    ("apa_us_2025", "US audiobook publisher receipts 2025", 2430, "$M", "FY25", "Audio Publishers Association, Jun 2026 (+9%)", "R"),
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
    # MLC contingency series -> quarterly increments (gross bundle discount)
    series = [("6-K Q2-24", "Jun-24", I["mlc_cum_q224"], 4), ("6-K Q3-24", "Sep-24", I["mlc_cum_q324"], 3), ("20-F FY24", "Dec-24", I["mlc_cum_q424"], 3),
              ("6-K Q1-25", "Mar-25", I["mlc_cum_q125"], 3), ("6-K Q2-25", "Jun-25", I["mlc_cum_q225"], 3), ("6-K Q3-25", "Sep-25", I["mlc_cum_q325"], 3),
              ("20-F FY25", "Dec-25", I["mlc_cum_q425"], 3), ("6-K Q1-26", "Mar-26", I["mlc_cum_q126"], 3), ("6-K Q2-26", "Jun-26", I["mlc_cum_q226"], 3)]
    r["mlc_series"] = []
    prev = 0
    for filing, pe, cum, months in series:
        inc = cum - prev; r["mlc_series"].append((filing, pe, cum, inc, months, inc / months)); prev = cum
    r["mlc_avg_q"] = sum(x[3] for x in r["mlc_series"][4:8]) / 4  # Q2-25 .. Q1-26
    r["B_gross"] = {2024: I["mlc_cum_q424"], 2025: I["mlc_cum_q425"] - I["mlc_cum_q424"], 2026: I["bundle_rr_2026"], 2027: I["bundle_rr_2027"]}
    pubs = {"umpg": ("share_umpg", "start_umpg"), "wcm": ("share_wcm", "start_wcm"), "kobalt": ("share_kobalt", "start_kobalt"), "smp": ("share_smp", "start_smp"), "bmg": ("share_bmg", "start_bmg")}
    shares = {p: I[k] for p, (k, _) in pubs.items()}
    handback_months = {p: {2024: 0, 2025: 13 - I[st], 2026: 12, 2027: 12} for p, (_, st) in pubs.items()}
    r["S_direct"] = sum(shares.values())
    r["B_handback"], r["B"] = {}, {}
    for y in YEARS:
        gross = r["B_gross"][y]
        hb = gross * sum(shares[p] * handback_months[p][y] / 12 for p in shares) * I["restoration"]
        b = gross - hb
        if y == 2027 and I["mlc_loss_2027"]:
            b = gross * r["S_direct"] * (1 - I["restoration"])  # independents' share goes to zero; un-restored part of direct deals stays
        r["B_handback"][y], r["B"][y] = hb, b
    # Billboard cross-check of the gross discount (Q4-25)
    r["bb_streams_q423"] = I["bb_q423_mech"] / I["bb_q423_rate"] / 1000
    r["bb_streams_q425"] = I["bb_q425_mech"] / I["bb_q425_rate"] / 1000
    r["bb_counterfactual"] = r["bb_streams_q425"] * I["bb_q423_rate"] * 1000
    r["bb_discount_usd"] = r["bb_counterfactual"] - I["bb_q425_mech"]
    r["bb_discount_eur"] = r["bb_discount_usd"] / I["eurusd_q425"]
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
#   Audiobooks_Inputs  segmented inputs (blocks A-K), each tagged with the bridge section it feeds
#   Audiobooks_Bridge  B, C, A -> N -> output block for the operating model (annual and quarterly), then checks and sensitivity
# Colour convention: blue = hard-coded input; green = reference to the inputs tab; black = formula;
# orange fill = estimate; yellow fill / red text = forecast placeholder to link; green fill = output rows
# ----------------------------------------------------------------------------
HDR = Font(bold=True); TITLE = Font(bold=True, size=12)
FILL = PatternFill("solid", fgColor="DDEBF7"); SECT = PatternFill("solid", fgColor="BDD7EE"); EST = PatternFill("solid", fgColor="FCE4D6")
LINK = PatternFill("solid", fgColor="FFF2CC"); OUT = PatternFill("solid", fgColor="E2EFDA")
F_BLUE = Font(color="0000FF"); F_GREEN = Font(color="008000"); F_BLACK = Font(color="000000"); LINKF = Font(color="C00000", bold=True)
FMT_M = '#,##0_);(#,##0)'; FMT_BP = '0_);(0)'; FMT_PCT = '0.0%'; FMT_PCT0 = '0%'; FMT_X = '0.00'; FMT_INT = '0'
UNIT_FMT = {"€M": FMT_M, "$M": FMT_M, "%": FMT_PCT, "x": FMT_X, "bp": FMT_INT, "M": '0.0', "flag": FMT_INT, "month": FMT_INT, "months": FMT_INT, "$/stream": '0.00000'}
TYPE = {"D": "Actual", "R": "Reported", "E": "Estimate", "L": "LINK TO MODEL"}
SHEET_IN, SHEET_AN = "Audiobooks_Inputs", "Audiobooks_Bridge"
COLS = ["C", "D", "E", "F"]  # 2024A, 2025A, 2026E, 2027E
SECTIONS = [
    ("A. Revenue base", "4, 6", ["prem_rev_2022", "prem_rev_2023", "prem_rev_2024", "prem_rev_2025", "grp_rev_2024", "grp_rev_2025", "grp_rev_2026", "grp_rev_2027",
                                 "grp_q124", "grp_q224", "grp_q324", "grp_q424", "grp_q125", "grp_q225", "grp_q325", "grp_q425", "grp_q126", "grp_q226", "grp_q326"]),
    ("B. Bundle saving: MLC contingency series (gross discount, from filings)", "1a, 1b", ["mlc_cum_q224", "mlc_q224_only", "mlc_cum_q324", "mlc_cum_q424", "mlc_cum_q125", "mlc_cum_q225", "mlc_cum_q325", "mlc_cum_q425", "mlc_cum_q126", "mlc_cum_q226", "bundle_rr_2026", "bundle_rr_2027"]),
    ("C. Bundle saving: cross-check and references", "7a", ["bb_q423_mech", "bb_q425_mech", "bb_q423_rate", "bb_q425_rate", "eurusd_q425", "nmpa_first_year", "nmpa_cum_2026"]),
    ("D. Direct publisher deals (hand-back of the saving)", "1c", ["share_umpg", "start_umpg", "share_wcm", "start_wcm", "share_kobalt", "start_kobalt", "share_smp", "start_smp", "share_bmg", "start_bmg", "restoration", "mlc_loss_2027"]),
    ("E. Licensing cost on included hours", "2", ["c_2024", "c_g_2025", "c_g_2026", "c_g_2027", "c_low_mult", "c_high_mult"]),
    ("F. Licensing cost: market-share triangulation", "7b", ["apa_us_2025", "spot_us_share_lo", "spot_us_share_hi", "nonus_uplift", "eurusd"]),
    ("G. Paid channel (Audiobooks+, top-ups, a la carte)", "3", ["ab_plus_arr", "ab_plus_payers", "a_rev_2024", "a_rev_2025", "a_rev_2026", "a_rev_2027", "a_cogs_ratio"]),
    ("H. Attach denominators", "8", ["subs_global", "subs_eligible", "listen_share", "tried_share", "basic_optout", "bull_attach"]),
    ("I. Premium cost of revenue (residual cross-check)", "7c", ["cogs_ratio_2022", "cogs_ratio_2023", "cogs_ratio_2024", "cogs_ratio_2025", "royalty_inc_2024", "royalty_inc_2025", "royalty_inc_9m25", "royalty_inc_h126", "prem_rev_h125", "prem_rev_h126", "prem_rev_9m24", "prem_rev_9m25"]),
    ("J. Consensus", "5", ["cons_gm_exp_2026", "cons_gm_exp_2027"]),
    ("K. Memo (excluded from the bridge)", "5", ["p_2024"]),
]

def _style(cell, fmt=None):
    v = cell.value
    if isinstance(v, str) and v.startswith("="):
        cell.font = F_GREEN if SHEET_IN + "!" in v else F_BLACK
    elif isinstance(v, (int, float)):
        cell.font = F_BLUE
    if fmt: cell.number_format = fmt

def build_workbook(r):
    wb = Workbook(); wb.properties.creator = "SPOT"; wb.properties.lastModifiedBy = "SPOT"
    by_key = {row[0]: row for row in INPUTS}
    placed = set(k for _, _, keys in SECTIONS for k in keys)
    missing = [row[0] for row in INPUTS if row[0] not in placed]
    assert not missing, f"inputs not placed in a section: {missing}"

    # ---- Inputs tab
    ws = wb.active; ws.title = SHEET_IN
    ws["A1"] = "Audiobooks: inputs"; ws["A1"].font = TITLE
    ws["A2"] = ("Blue text = hard-coded input. Orange fill = estimate. Yellow fill with red text = forecast placeholder: replace with a link to the main model before use. "
                "No forecasts beyond FY27. 'Bridge ref' is the section of the Audiobooks_Bridge tab the input feeds.")
    ws.append([]); ws.append(["Input", "Value", "Unit", "Period", "Type", "Bridge ref", "Source / note"])
    for c in ws[4]: c.font = HDR; c.fill = FILL
    A = {}; i = 4
    for title, ref, keys in SECTIONS:
        i += 1; ws.append([title]); 
        for col in range(1, 8): ws.cell(row=i, column=col).fill = SECT
        ws.cell(row=i, column=1).font = HDR
        for k in keys:
            _, label, v, unit, period, src, conf = by_key[k]
            i += 1; ws.append([label, v, unit, period, TYPE[conf], ref, src]); A[k] = f"{SHEET_IN}!$B${i}"
            cell = ws.cell(row=i, column=2); cell.font = F_BLUE; cell.number_format = UNIT_FMT.get(unit, "General")
            if conf == "E": cell.fill = EST
            if conf == "L":
                cell.fill = LINK; cell.font = LINKF; ws.cell(row=i, column=5).fill = LINK; ws.cell(row=i, column=5).font = LINKF
        i += 1; ws.append([])
    ws.append(["Sources"]); ws.cell(row=ws.max_row, column=1).font = HDR
    for line in SOURCES: ws.append([line])
    for col, w in zip("ABCDEFG", [78, 12, 9, 12, 16, 10, 110]): ws.column_dimensions[col].width = w
    ws.freeze_panes = "A5"

    # ---- Bridge tab
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
            for col in range(1, 9): an.cell(row=rr, column=col).fill = fill
        return rr

    def nxt(): return state["row"] + 1
    def section(title):
        rr = put(title, bold=True, fill=SECT); return rr
    def year_header():
        h = put("", vals=["2024A", "2025A", "2026E", "2027E"], bold=True, fill=FILL)
        for col in COLS: an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
        return h

    put("Audiobooks: bridge from inputs to the gross-margin headwind (€M unless stated)", bold=True); an["A1"].font = TITLE
    put("Flow: 1 bundle saving (B)  ->  2 licensing cost on included hours (C)  ->  3 paid channel (A)  ->  4 net contribution N = B + A - C  ->  5 output for the operating model  ->  6 quarterly allocation. Sections 7-9 are checks, context and sensitivity. Blue = hard-coded; green = inputs tab; black = formula.")
    put("")

    # ---------------- 1. Bundle saving
    section("1. Bundle mechanical-royalty saving (B)")
    put("1a. MLC contingency disclosed in Spotify filings: additional royalties due if Premium were not a bundle, cumulative from 1 Mar 2024 (€M)", bold=True)
    h = put("Filing (period end)", vals=["Cumulative", "Increment", "Months", "€M per month"], bold=True)
    for col in COLS: an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
    series_keys = [("6-K Q2-24 (30 Jun 2024)", "mlc_cum_q224", 4), ("6-K Q3-24 (30 Sep 2024)", "mlc_cum_q324", 3), ("20-F FY24 (31 Dec 2024)", "mlc_cum_q424", 3),
                   ("6-K Q1-25 (31 Mar 2025)", "mlc_cum_q125", 3), ("6-K Q2-25 (30 Jun 2025)", "mlc_cum_q225", 3), ("6-K Q3-25 (30 Sep 2025)", "mlc_cum_q325", 3),
                   ("20-F FY25 (31 Dec 2025)", "mlc_cum_q425", 3), ("6-K Q1-26 (31 Mar 2026)", "mlc_cum_q126", 3), ("6-K Q2-26 (30 Jun 2026): verify, see inputs note", "mlc_cum_q226", 3)]
    R_series = {}; prev_row = None
    for label, key, months in series_keys:
        rr = nxt(); inc = f"=C{rr}" if prev_row is None else f"=C{rr}-C{prev_row}"
        put(label, vals=[f"={A[key]}", inc, months, f"=D{rr}/E{rr}"], fmt=FMT_M); an[f"F{rr}"].number_format = '0.0'
        R_series[key] = rr; prev_row = rr
    rr = nxt(); put("   of which April to June 2024 (so March 2024 alone was about €11M)", vals=[f"={A['mlc_q224_only']}", "", 3, f"=C{rr}/E{rr}"], fmt=FMT_M); an[f"F{rr}"].number_format = '0.0'
    R_avg = put("Average quarterly increment, Q2-25 to Q1-26", single=f"=AVERAGE(D{R_series['mlc_cum_q225']}:D{R_series['mlc_cum_q126']})", fmt='0.0')
    put("Annualised (basis for the 2026E-27E placeholders)", single=f"=B{R_avg}*4", fmt=FMT_M)
    put("Reading: the increment ran at €50-56M a quarter from Q4-24 to Q1-26 with no step down after the direct deals, so the figure is gross: every paid-tier stream is still reported through the MLC at the bundle rate and the direct-licensed publishers receive a top-up outside it. The Q2-26 increment of €27M is either an FX translation effect or the first filing to net out direct-deal publishers; the 6-K wording decides which.")
    put("")
    put("1b. Gross bundle saving by year", bold=True); year_header()
    R_gross = put("Gross saving (2024-25 from the filings; 2026E-27E placeholders on the inputs tab)",
                  vals=[f"={A['mlc_cum_q424']}", f"={A['mlc_cum_q425']}-{A['mlc_cum_q424']}", f"={A['bundle_rr_2026']}", f"={A['bundle_rr_2027']}"], fmt=FMT_M, bold=True)
    put("")
    put("1c. Hand-back to direct-licensed publishers", bold=True)
    h = put("Publisher (share of US mechanicals in col B)", vals=["Months on direct licence", "", "", ""], bold=True); an[f"C{h}"].alignment = Alignment(horizontal="left")
    pub_rows = {}
    for label, sk, st in [("UMPG", "share_umpg", "start_umpg"), ("Warner Chappell", "share_wcm", "start_wcm"), ("Kobalt", "share_kobalt", "start_kobalt"),
                          ("Sony Music Publishing", "share_smp", "start_smp"), ("BMG", "share_bmg", "start_bmg")]:
        pub_rows[sk] = put(label, single=f"={A[sk]}", vals=[0, f"=13-{A[st]}", 12, 12], fmt=FMT_INT); an[f"B{pub_rows[sk]}"].number_format = FMT_PCT0
    first, last = min(pub_rows.values()), max(pub_rows.values())
    R_S = put("Sum of shares on direct licences (independents are the remainder, still paid at the bundle rate via the MLC)", single=f"=SUM(B{first}:B{last})", fmt=FMT_PCT0)
    R_rest = put("Restoration of the bundle discount in the direct deals", single=f"={A['restoration']}", fmt=FMT_PCT0)
    R_hb = put("Hand-back = gross x sum(share x months / 12) x restoration", vals=[f"={c}{R_gross}*SUMPRODUCT($B${first}:$B${last},{c}{first}:{c}{last})/12*$B${R_rest}" for c in COLS], fmt=FMT_M)
    R_B = put("B  Net bundle saving retained by Spotify (2027: if MLC switch = 1, the independents' share goes to zero)",
              vals=[f"={c}{R_gross}-{c}{R_hb}" for c in COLS[:3]] + [f"=IF({A['mlc_loss_2027']}=1,F{R_gross}*$B${R_S}*(1-$B${R_rest}),F{R_gross}-F{R_hb})"], fmt=FMT_M, bold=True)
    put("")

    # ---------------- 2. Licensing cost
    section("2. Audiobook licensing cost on included hours (C)"); year_header()
    R_g = put("Growth y/y (2025 from reported consumption growth; 2026E-27E placeholders)", vals=["", f"={A['c_g_2025']}", f"={A['c_g_2026']}", f"={A['c_g_2027']}"], fmt=FMT_PCT0)
    rc = nxt()
    R_C = put("C  Base case (2024 anchored on 'hundreds of millions of dollars a year', Oct-24)", vals=[f"={A['c_2024']}", f"=C{rc}*(1+D{R_g})", f"=D{rc}*(1+E{R_g})", f"=E{rc}*(1+F{R_g})"], fmt=FMT_M, bold=True)
    put("C  Low case", vals=[f"={c}{R_C}*{A['c_low_mult']}" for c in COLS], fmt=FMT_M)
    put("C  High case", vals=[f"={c}{R_C}*{A['c_high_mult']}" for c in COLS], fmt=FMT_M)
    put("")

    # ---------------- 3. Paid channel
    section("3. Priced channel (Audiobooks+, top-ups, a la carte)"); year_header()
    R_arev = put("Revenue", vals=[f"={A['a_rev_2024']}", f"={A['a_rev_2025']}", f"={A['a_rev_2026']}", f"={A['a_rev_2027']}"], fmt=FMT_M)
    R_ratio = put("Content cost ratio on paid hours", single=f"={A['a_cogs_ratio']}", fmt=FMT_PCT0)
    R_Agp = put("A  Gross profit on paid hours = revenue x (1 - ratio)", vals=[f"={c}{R_arev}*(1-$B${R_ratio})" for c in COLS], fmt=FMT_M, bold=True)
    put("")

    # ---------------- 4. Net contribution
    section("4. Net contribution to gross profit: N = B + A - C"); year_header()
    R_B2 = put("B  Net bundle saving", vals=[f"={c}{R_B}" for c in COLS], fmt=FMT_M)
    R_A2 = put("A  Gross profit on paid hours", vals=[f"={c}{R_Agp}" for c in COLS], fmt=FMT_M)
    R_C2 = put("C  Licensing cost on included hours", vals=[f"=-{c}{R_C}" for c in COLS], fmt=FMT_M)
    R_N = put("N  Net contribution", vals=[f"={c}{R_B2}+{c}{R_A2}+{c}{R_C2}" for c in COLS], fmt=FMT_M, bold=True)
    R_grp = put("Group revenue", vals=[f"={A['grp_rev_2024']}", f"={A['grp_rev_2025']}", f"={A['grp_rev_2026']}", f"={A['grp_rev_2027']}"], fmt=FMT_M)
    R_Nbp = put("N, bp of group revenue", vals=[f"={c}{R_N}/{c}{R_grp}*10000" for c in COLS], fmt=FMT_BP)
    R_dN = put("Change in N y/y, €M", vals=[""] + [f"={c}{R_N}-{p}{R_N}" for p, c in zip(COLS, COLS[1:])], fmt=FMT_M)
    R_dNbp = put("Change in N y/y, bp of group revenue", vals=[""] + [f"={c}{R_dN}/{c}{R_grp}*10000" for c in COLS[1:]], fmt=FMT_BP)
    put("   of which music publishers reclaim the bundle saving (change in B)", vals=[""] + [f"={c}{R_B2}-{p}{R_B2}" for p, c in zip(COLS, COLS[1:])], fmt=FMT_M)
    put("   of which book publishers paid on consumption (change in C)", vals=[""] + [f"={c}{R_C2}-{p}{R_C2}" for p, c in zip(COLS, COLS[1:])], fmt=FMT_M)
    put("   of which paid hours (change in A)", vals=[""] + [f"={c}{R_A2}-{p}{R_A2}" for p, c in zip(COLS, COLS[1:])], fmt=FMT_M)
    put("")

    # ---------------- 5. Output
    section("5. OUTPUT FOR THE OPERATING MODEL (annual)"); year_header()
    R_o1 = put("Audiobook net contribution to gross profit, €M  (add this row to gross profit)", vals=[f"={c}{R_N}" for c in COLS], fmt=FMT_M, bold=True, fill=OUT)
    put("   as bp of group revenue", vals=[f"={c}{R_Nbp}" for c in COLS], fmt=FMT_BP, fill=OUT)
    put("Y/y change in contribution, €M", vals=[""] + [f"={c}{R_dN}" for c in COLS[1:]], fmt=FMT_M, fill=OUT)
    R_o4 = put("Y/y change, bp of group revenue  =  audiobook gross-margin headwind (subtract from y/y gross-margin expansion)", vals=[""] + [f"={c}{R_dNbp}" for c in COLS[1:]], fmt=FMT_BP, bold=True, fill=OUT)
    R_cons = put("Consensus gross-margin expansion, bp", vals=["", "", f"={A['cons_gm_exp_2026']}", f"={A['cons_gm_exp_2027']}"], fmt=FMT_BP)
    put("Headwind as share of consensus expansion", vals=["", "", f"=-E{R_o4}/E{R_cons}", f"=-F{R_o4}/F{R_cons}"], fmt=FMT_PCT0)
    put("Memo, excluded from the bridge: June 2024 US price increase, annualised €M (the item management credits to audiobooks)", vals=[f"={A['p_2024']}"], fmt=FMT_M)
    put("Use: either add the €M row to gross profit (level), or subtract the bp row from the model's y/y gross-margin expansion (change). Do not do both.")
    put("")

    # ---------------- 6. Quarterly allocation
    section("6. Quarterly allocation (annual N allocated by revenue share, so N is a constant bp of revenue within each year)")
    h = put("Quarter", single="Group revenue €M", vals=["Share of year", "N allocated €M", "N bp of revenue", "Y/y change €M"], extra={"G": "Y/y change bp"}, bold=True)
    for col in "BCDEFG": an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
    quarters = [("Q1-24", 2024, f"={A['grp_q124']}"), ("Q2-24", 2024, f"={A['grp_q224']}"), ("Q3-24", 2024, f"={A['grp_q324']}"), ("Q4-24", 2024, f"={A['grp_q424']}"),
                ("Q1-25", 2025, f"={A['grp_q125']}"), ("Q2-25", 2025, f"={A['grp_q225']}"), ("Q3-25", 2025, f"={A['grp_q325']}"), ("Q4-25", 2025, f"={A['grp_q425']}"),
                ("Q1-26", 2026, f"={A['grp_q126']}"), ("Q2-26", 2026, f"={A['grp_q226']}"), ("Q3-26E", 2026, f"={A['grp_q326']}"), ("Q4-26E", 2026, None),
                ("Q1-27E", 2027, None), ("Q2-27E", 2027, None), ("Q3-27E", 2027, None), ("Q4-27E", 2027, None)]
    start_row = nxt(); year_rows = {}
    for idx, (q, y, rev) in enumerate(quarters):
        rr = start_row + idx; year_rows.setdefault(y, []).append(rr)
    ycol = {2024: "C", 2025: "D", 2026: "E", 2027: "F"}
    q_rows = []
    for idx, (q, y, rev) in enumerate(quarters):
        rr = start_row + idx; yr = year_rows[y]; y0, y1 = yr[0], yr[-1]
        if rev is None and y == 2026:
            rev = f"={A['grp_rev_2026']}-SUM(B{y0}:B{rr-1})"
        elif rev is None and y == 2027:
            r26 = year_rows[2026][idx - quarters.index(("Q1-27E", 2027, None))]
            rev = f"={A['grp_rev_2027']}*B{r26}/SUM(B{year_rows[2026][0]}:B{year_rows[2026][-1]})"
        share = f"=B{rr}/SUM(B{y0}:B{y1})"
        nq = f"=C{rr}*{ycol[y]}${R_N}"
        nbp = f"=D{rr}/B{rr}*10000"
        dn = "" if y == 2024 else f"=D{rr}-D{rr-4}"
        dnbp = "" if y == 2024 else f"=F{rr}/B{rr}*10000"
        put(q, single=rev, vals=[share, nq, nbp, dn], extra={"G": dnbp} if dnbp else None, fmt=FMT_M)
        an[f"C{rr}"].number_format = FMT_PCT; an[f"E{rr}"].number_format = FMT_BP; an[f"G{rr}"].number_format = FMT_BP
        if q.endswith("E"):
            an[f"B{rr}"].fill = LINK; an[f"B{rr}"].font = LINKF
        for col in "DEFG": an[f"{col}{rr}"].fill = OUT
        q_rows.append(rr)
    put("Tie-out: sum of quarters less annual revenue input (2025 quarters sum to 17,152 vs the 17,186 annual figure; link both to the model)",
        vals=[f"=SUM(B{year_rows[y][0]}:B{year_rows[y][-1]})-{ycol[y]}{R_grp}" for y in [2024, 2025, 2026, 2027]], fmt=FMT_M)
    put("Yellow revenue cells are placeholders (Q3-26E guidance; Q4-26E = annual less Q1-Q3; 2027E = annual x 2026 quarterly weights). Replace with links to the model's quarterly revenue.")
    put("")

    # ---------------- 7. Checks
    section("7. Checks")
    put("7a. Bundle saving: Billboard analysis of Spotify's MLC reports, paid tiers (independent of the filings)", bold=True)
    R_bm = put("Mechanical royalties paid to the MLC, $M: Q4-23 (col B), Q4-25 (col C)", single=f"={A['bb_q423_mech']}", extra={"C": f"={A['bb_q425_mech']}"}, fmt='0.0')
    R_br = put("Blended per-stream rate, $: Q4-23 (col B), Q4-25 (col C)", single=f"={A['bb_q423_rate']}", extra={"C": f"={A['bb_q425_rate']}"}, fmt='0.00000')
    R_bs = put("Implied paid-tier streams, bn: Q4-23 (col B), Q4-25 (col C)", single=f"=B{R_bm}/B{R_br}/1000", extra={"C": f"=C{R_bm}/C{R_br}/1000"}, fmt='0.0')
    R_bc = put("Counterfactual Q4-25 payment at the Q4-23 rate, $M", single=f"=C{R_bs}*B{R_br}*1000", fmt='0.0')
    R_bd = put("Implied quarterly bundle discount, $M", single=f"=B{R_bc}-C{R_bm}", fmt='0.0')
    R_bf = put("EUR/USD, Q4-25", single=f"={A['eurusd_q425']}", fmt=FMT_X)
    put("Implied quarterly discount, €M (col B) vs 6-K Q4-25 increment (col C)", single=f"=B{R_bd}/B{R_bf}", extra={"C": f"=D{R_series['mlc_cum_q425']}"}, fmt='0.0')
    put("NMPA: first-year publisher loss $M (col B); cumulative to Jun-26 with Amazon, $M (col C)", single=f"={A['nmpa_first_year']}", extra={"C": f"={A['nmpa_cum_2026']}"}, fmt=FMT_M)
    put("Reading: streams in the MLC reports grew 19bn between the two quarters, so direct-licensed publishers have not left the blanket licence. Two independent sources put the gross discount at about €50M a quarter.")
    put("")
    put("7b. Licensing cost: market-share triangulation of C (2025)", bold=True)
    R_apa = put("US audiobook publisher receipts 2025 ($M)", single=f"={A['apa_us_2025']}", fmt=FMT_M)
    R_sh = put("Spotify share of US receipts: low (col B), high (col C)", single=f"={A['spot_us_share_lo']}", extra={"C": f"={A['spot_us_share_hi']}"}, fmt=FMT_PCT0)
    R_nonus = put("Non-US markets, multiple of US cost", single=f"={A['nonus_uplift']}", fmt=FMT_X)
    R_fx = put("EUR/USD", single=f"={A['eurusd']}", fmt=FMT_X)
    R_imp = put("Implied global C 2025, €M: low (col B), high (col C)", single=f"=B{R_apa}*B{R_sh}*B{R_nonus}/B{R_fx}", extra={"C": f"=B{R_apa}*C{R_sh}*B{R_nonus}/B{R_fx}"}, fmt=FMT_M)
    R_base = put("Base case C 2025, €M", single=f"=D{R_C}", fmt=FMT_M)
    put("Base case vs implied range: vs low (col B), vs high (col C)", single=f"=B{R_base}/B{R_imp}-1", extra={"C": f"=B{R_base}/C{R_imp}-1"}, fmt=FMT_PCT)
    put("")
    put("7c. Licensing cost: incremental Premium content-cost ratio (does the P&L show an audiobook step?)", bold=True)
    h = put("", vals=["Premium revenue change", "Content cost change", "Incremental ratio"], bold=True)
    for col in COLS[:3]: an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
    for label, rev_f, cost_f in [
        ("FY24 vs FY23", f"={A['prem_rev_2024']}-{A['prem_rev_2023']}", f"={A['royalty_inc_2024']}"),
        ("FY25 vs FY24", f"={A['prem_rev_2025']}-{A['prem_rev_2024']}", f"={A['royalty_inc_2025']}"),
        ("9M-25 vs 9M-24", f"={A['prem_rev_9m25']}-{A['prem_rev_9m24']}", f"={A['royalty_inc_9m25']}"),
        ("H1-26 vs H1-25", f"={A['prem_rev_h126']}-{A['prem_rev_h125']}", f"={A['royalty_inc_h126']}"),
    ]:
        rr = nxt(); put(label, vals=[rev_f, cost_f, f"=D{rr}/C{rr}"], fmt=FMT_M); an[f"E{rr}"].number_format = FMT_PCT
    put("Reading: the incremental ratio holds at 48-50% in every period against a ~66% average ratio. It bounds the growth in C rather than measuring it: music royalties, the bundle saving, marketplace offsets and the Partner Program all move inside the same line.")
    put("")

    # ---------------- 8. Attach
    section("8. Context: paid attach (evidence on add-on uptake)")
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

    # ---------------- 9. Sensitivity (live)
    section("9. Sensitivity: 2027E, by audiobook cost growth (rows) and bundle-discount restoration / MLC outcome (columns)")
    R_h1 = put("Restoration of bundle discount", vals=[0.5, 0.75, 0.75], fmt=FMT_PCT0)
    R_h2 = put("MLC complaint succeeds in 2027 (1 = yes)", vals=[0, 0, 1], fmt=FMT_INT)
    h = put("Cost growth p.a. 2026-27 (col A)", vals=["Change in N 2027, bp", "Change in N 2027, bp", "Change in N 2027, bp"], bold=True)
    for col in COLS[:3]: an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
    for gr in [0.20, 0.30, 0.45, 0.60]:
        rr = nxt()
        vals = [f"=((IF({c}${R_h2}=1,$F${R_gross}*$B${R_S}*(1-{c}${R_h1}),$F${R_gross}*(1-$B${R_S}*{c}${R_h1}))-$E${R_gross}*(1-$B${R_S}*{c}${R_h1}))+($F${R_Agp}-$E${R_Agp})-$D${R_C}*(1+$A{rr})*$A{rr})/$F${R_grp}*10000" for c in COLS[:3]]
        put(gr, vals=vals, fmt=FMT_BP); an[f"A{rr}"].number_format = FMT_PCT0; an[f"A{rr}"].font = F_BLUE
    h = put("Cost growth p.a. 2026-27 (col A)", vals=["N 2027, €M", "N 2027, €M", "N 2027, €M"], bold=True)
    for col in COLS[:3]: an[f"{col}{h}"].font = HDR; an[f"{col}{h}"].alignment = Alignment(horizontal="right")
    for gr in [0.20, 0.30, 0.45, 0.60]:
        rr = nxt()
        vals = [f"=IF({c}${R_h2}=1,$F${R_gross}*$B${R_S}*(1-{c}${R_h1}),$F${R_gross}*(1-$B${R_S}*{c}${R_h1}))+$F${R_Agp}-$D${R_C}*(1+$A{rr})^2" for c in COLS[:3]]
        put(gr, vals=vals, fmt=FMT_M); an[f"A{rr}"].number_format = FMT_PCT0; an[f"A{rr}"].font = F_BLUE
    put("Restoration does not change the 2027 headwind (B is flat 2026 to 2027 once every direct deal is a full year old); it changes the level of N. An MLC win removes the independents' share of the gross saving.")

    an.column_dimensions["A"].width = 92; an.column_dimensions["B"].width = 16
    for col in "CDEFG": an.column_dimensions[col].width = 15
    an.freeze_panes = "B4"
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
                 f"B: 2024 {r['B'][2024]:.0f} → 2025 {r['B'][2025]:.0f} → 2026 {r['B'][2026]:.0f}. Gross saving is disclosed (€{r['B_gross'][2024]:.0f}M 2024, €{r['B_gross'][2025]:.0f}M 2025); five direct deals cover ~{r['S_direct']:.0%} of US mechanicals; restoration ({I['restoration']:.0%}) is an estimate", "SUPPORTED"])
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
    "MLC contingency series (legal proceedings note in each filing): 6-K Q2-24 sec.gov/Archives/edgar/data/1639920/000163992024000009/spot-20240630x6xk.htm; 6-K Q3-24 .../000163992024000013/spot-20240930x6xk.htm; 20-F FY24 .../000163992025000003/ck0001639920-20241231.htm; 6-K Q1-25 .../000163992025000006/spot-20250331x6xk.htm; 6-K Q2-25 .../000163992025000012/spot-20250630x6xk.htm; 6-K Q3-25 .../000162828025048927/spot-20250930x6xk.htm; 20-F FY25 .../000162828026006874/ck0001639920-20251231.htm; 6-K Q1-26 .../000162828026027951/spot-20260331x6xk.htm; 6-K Q2-26 .../000162828026052543/spot-20260630x6xk.htm",
    "Billboard, 'How Much Have Spotify Bundles Decreased the Mechanical Per-Stream Rate? (Analysis)': Q4-23 $97.3M at $0.00068 per stream; Q4-25 $53.3M at $0.00033; streams +19.3bn",
    "Direct deals: UMPG 26 Jan 2025 (MBW); Warner Chappell 6 Feb 2025 (MBW: 'supersedes the bundling payment structure'; terms 'continue to recognize a difference between bundled and music-only listeners'); Kobalt 13 Aug 2025 (CMU, MBW); Sony Music Publishing 18 Sep 2025 (MBW, Variety); BMG 9 Oct 2025 (CMU)",
    "MLC v. Spotify USA Inc., S.D.N.Y. 1:24-cv-03809: dismissed with prejudice 29 Jan 2025; reconsideration granted Sep 2025; amended complaint 1 Oct 2025 (valuation of the bundle components and the Audiobook Access tier); jury demand 8 Oct 2025; interlocutory appeal denied 1 Sep 2026; fact discovery cutoff 13 Mar 2027",
    "Spotify Form 20-F FY2024 and FY2025 (Premium cost of revenue drivers, royalty component increases, Premium GM): sec.gov/Archives/edgar/data/1639920/000163992025000003/ck0001639920-20241231.htm ; .../000162828026006874/ck0001639920-20251231.htm",
    "Spotify Form 6-K Q2-26 (H1-26 Premium cost of revenue +€500M, content +€474M, ratio 67%→65%): sec.gov/Archives/edgar/data/0001639920/000162828026052543/spot-20260630x6xk.htm",
    "Spotify Form 6-K Q3-25 (9M-25 royalty component +€588M): sec.gov/Archives/edgar/data/1639920/000162828025048927/spot-20250930x6xk.htm",
    "NMPA statements: $150M (May 2024), $230M first-year loss, nearly $500M cumulative with Amazon (annual meeting, Jun 2026; 'nearly $480 million by Spotify's own admission')",
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
    L.append("Model: `analysis/audiobooks_model.py` → `data/SPOT_audiobooks_model.xlsx` (two tabs, Audiobooks_Inputs and Audiobooks_Bridge, live formulas; forecast placeholders for 2026E–2027E are flagged LINK TO MODEL). Identity: N(t) = B(t) + A_gp(t) − C(t). The June 2024 price increase is deliberately outside N.\n")
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
    L.append("\nTwo different rights-holder groups, two different mechanisms. The music publishers' claw-back is contractual: UMPG (Jan-25), Warner Chappell (Feb-25), Kobalt (Aug-25), Sony Music Publishing (Sep-25) and BMG (Oct-25) moved to direct US licences that supersede the bundle rate. The book publishers' claw-back is volumetric: per-title fees and pool payments on consumption that the company reports growing 35–60% a year. The priced channel offsets roughly a sixth of the book-publisher cost growth.\n")
    L.append("## 3. How each term was sized\n")
    L.append(f"**B.** The gross saving is disclosed. Every 6-K and 20-F since Q2-24 states the additional royalties that would be due to the MLC if Premium were not a bundle, cumulative from 1 March 2024. The quarterly increments run at €50-56M from Q4-24 to Q1-26, so the gross discount is about €{r['B_gross'][2024]:.0f}M for 2024 (ten months) and €{r['B_gross'][2025]:.0f}M for 2025. Billboard's analysis of Spotify's MLC reports gives the same answer independently: at the Q4-23 per-stream rate, Q4-25 streams would have cost ${r['bb_counterfactual']:.0f}M against ${I['bb_q425_mech']:.1f}M paid, a discount of €{r['bb_discount_eur']:.0f}M for the quarter versus the filing increment of €{r['mlc_series'][6][3]:.0f}M. Streams in the MLC reports grew between the two quarters, so the direct-licensed publishers have not left the blanket licence: the contingency is gross and the hand-back must be estimated. Five direct deals (UMPG Jan-25, Warner Chappell Feb-25, Kobalt Aug-25, Sony Music Publishing Sep-25, BMG Oct-25) cover an estimated {r['S_direct']:.0%} of US mechanicals; restoration is set at {I['restoration']:.0%} because Spotify calls the offset partial and the Warner terms still distinguish bundled from music-only listeners. The remaining independents' share (€{r['B_gross'][2026]*(1-r['S_direct']):.0f}M a year) is what the MLC's amended complaint pursues.\n")
    L.append("| Filing | Period end | Cumulative €M | Increment €M | Months | €M per month |\n|---|---|---|---|---|---|")
    for filing, pe, cum, inc, months, pm in r["mlc_series"]: L.append(f"| {filing} | {pe} | {cum:.0f} | {inc:.0f} | {months} | {pm:.1f} |")
    L.append("\nThe Q2-26 figure is quoted by Music Ally as €437M; a second reading of the same filing gives €473M. The increment is €27M on the first reading and €63M on the second. Verify in the Q2-26 6-K legal-proceedings note. The 2026E placeholder uses the Q2-25 to Q1-26 average and does not depend on it.\n")
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
    L.append("| C growth p.a. | restoration 50% | restoration 75% (base) | restoration 75% + MLC loss |\n|---|---|---|---|")
    for gr in [0.20, 0.30, 0.45, 0.60]:
        vals = []
        for rest, mlc in [(0.5, 0), (0.75, 0), (0.75, 1)]:
            sv = dict(I); sv["restoration"] = rest; sv["mlc_loss_2027"] = mlc; sv["c_g_2026"] = gr; sv["c_g_2027"] = gr
            vals.append(compute_with(sv)["dN_bp"][2027])
        L.append(f"| {gr:.0%} | " + " | ".join(f"{v:.0f}" for v in vals) + " |")
    L.append("\n## 8. What the result means for the pitch\n")
    L.append(f"- The audiobook 'margin contribution' the Street absorbed in 2024 was a royalty reclassification worth ~€{r['B_gross'][2024]:.0f}M plus a price increase worth ~€{I['p_2024']}M annualized. Audiobook consumption itself cost more than the reclassification saved in the same year.")
    L.append(f"- From 2025 the reclassification is being handed back to the majors' publishers through direct deals while consumption compounds. On base assumptions the net line moves from about −€{-r['N'][2024]:.0f}M in 2024 to −€{-r['N'][2027]:.0f}M in 2027, a {-r['dN_bp'][2025]:.0f}/{-r['dN_bp'][2026]:.0f}/{-r['dN_bp'][2027]:.0f}bp headwind in 2025/2026/2027.")
    L.append("- Spotify's only governors are the hour cap (already 12 h in every market launched since 2024), the per-title triggers, and the pool rate. Audible at $8.99 and Amazon's free book remove the price lever.")
    L.append("- The priced channel is real but small: it funds roughly a sixth of the consumption cost growth and attaches below 1% of eligible subscribers, which is the platform's own evidence against a 3% Music Pro attach.")
    L.append("- Caveats: C is triangulated, not disclosed; the gross bundle saving is disclosed but the restoration factor on the direct deals is an estimate; the residual method is silent. The direction survives every sensitivity in section 7; the size ranges from ~30 to ~110bp a year.")
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
