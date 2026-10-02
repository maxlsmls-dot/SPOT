"""Build analysis/spot_gm_driver_model.xlsx: a driver-based gross margin bridge for Spotify
keyed on Discovery Mode (DM) and autoplay / programmed-listening growth.
Blue = hardcoded input, black = formula, green = cross-sheet link, yellow fill = key lever."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter

OUT = "/home/user/SPOT/analysis/spot_gm_driver_model.xlsx"
F = "Arial"
BLUE = Font(name=F, color="0000FF", size=10)
BLACK = Font(name=F, color="000000", size=10)
GREEN = Font(name=F, color="008000", size=10)
BOLD = Font(name=F, bold=True, size=10)
TITLE = Font(name=F, bold=True, size=13)
H2 = Font(name=F, bold=True, size=11)
ITAL = Font(name=F, italic=True, size=9, color="555555")
YELLOW = PatternFill("solid", fgColor="FFFF00")
GREY = PatternFill("solid", fgColor="EDEDED")
thin = Side(style="thin", color="BBBBBB")
BOX = Border(top=thin, bottom=thin, left=thin, right=thin)

EUR = '#,##0;(#,##0);-'
PCT = '0.0%;(0.0%);-'
PCT2 = '0.00%;(0.00%);-'
BPS = '#,##0" bps";(#,##0" bps");-'
MULT = '0.00"x"'

wb = openpyxl.Workbook()

def setw(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def put(ws, ref, val, font=BLACK, fmt=None, fill=None, bold=False, comment=None, wrap=False):
    c = ws[ref]
    c.value = val
    c.font = Font(name=F, bold=bold, color=font.color, size=font.size, italic=font.italic)
    if fmt: c.number_format = fmt
    if fill: c.fill = fill
    if comment: c.comment = Comment(comment, "model")
    if wrap: c.alignment = Alignment(wrap_text=True, vertical="top")
    return c

# =====================================================================================
# Sheet 1: Inputs
# =====================================================================================
ws = wb.active; ws.title = "Inputs"
setw(ws, [58, 16, 16, 16, 16, 70])
put(ws, "A1", "Spotify gross margin driver model: Discovery Mode and autoplay growth", TITLE)
put(ws, "A2", "Blue = hardcoded input; black = formula; green = link to another sheet; yellow = key lever to set from the expert calls. Currency in EUR millions. Percentages stored as fractions.", ITAL)

put(ws, "A4", "A. Reported anchors (Spotify filings and shareholder letters)", H2)
put(ws, "B5", "Value", BOLD); put(ws, "F5", "Source / note", BOLD)
rows = [
    ("FY2025 total revenue (EUR m)", 17186, EUR, "Spotify FY2025 20-F: revenue EUR 17,186m (Premium 15,350m; Ad-Supported 1,836m)."),
    ("FY2025 Premium revenue (EUR m)", 15350, EUR, "Spotify FY2025 20-F."),
    ("FY2025 Ad-Supported revenue (EUR m)", 1836, EUR, "Spotify FY2025 20-F."),
    ("FY2025 consolidated gross margin", 0.320, PCT, "Spotify FY2025 20-F (rounded 32%); quarterly path 31.6% / 31.5% / 31.6% / 33.1%."),
    ("FY2025 Premium gross margin", 0.34, PCT, "Spotify FY2025 20-F (rounded 34%; 33% in FY2024, 29% in FY2023)."),
    ("Q2 2026 consolidated gross margin (reported)", 0.334, PCT, "Q2 2026 shareholder letter: 33.4%, +193 bps YoY; Premium 35% vs 33%."),
    ("Q3 2026 gross margin guidance", 0.329, PCT, "Q2 2026 shareholder letter: Q3 guide 32.9% on EUR 5.0bn revenue (+14% YoY)."),
    ("2030 gross margin target: low end", 0.35, PCT, "Investor Day, May 21 2026: 35-40% gross margin by 2030, mid-teens revenue CAGR."),
    ("2030 gross margin target: high end", 0.40, PCT, "Investor Day, May 21 2026."),
    ("Marketplace gross profit contribution, 2021 (EUR m)", 160, EUR, "Investor Day June 2022: 'more than EUR 160 million' in 2021 (under EUR 20m in 2018). Treated as the floor."),
    ("Marketplace gross profit multiple, 2025 vs 2021", 4.0, MULT, "Investor Day May 2026: 2025 marketplace gross profit was four times 2021. Marketplace = Discovery Mode + Marquee + Showcase."),
    ("Music royalty pool, FY2025, after all discounts (EUR m)", 10100, EUR, "Loud & Clear 2026: USD 11bn paid to music rights holders in 2025, converted at ~1.09 USD/EUR. Approximates the pool the DM discount is taken from; pre-discount pool is ~3% higher."),
]
r = 6
for label, val, fmt, note in rows:
    put(ws, f"A{r}", label); put(ws, f"B{r}", val, BLUE, fmt); put(ws, f"F{r}", note, ITAL, wrap=True)
    r += 1
# r is now 18
put(ws, "A18", "Derived: FY2025 marketplace gross profit (EUR m)"); put(ws, "B18", "=B15*B16", BLACK, EUR)
put(ws, "F18", "2021 contribution x the 2025/2021 multiple. A floor, because the 2021 figure was stated as more than 160.", ITAL, wrap=True)
put(ws, "A19", "Derived: FY2025 marketplace contribution to consolidated GM"); put(ws, "B19", "=B18/B6", BLACK, PCT2)
put(ws, "F19", "Share of revenue. Multiply by 10,000 for basis points.", ITAL)
put(ws, "A20", "Derived: FY2025 music royalty pool as % of revenue"); put(ws, "B20", "=B17/B6", BLACK, PCT)

put(ws, "A22", "B. Discovery Mode structural parameters (the levers the expert calls should pin down)", H2)
put(ws, "B23", "Value", BOLD); put(ws, "F23", "Source / note", BOLD)
params = [
    ("DM royalty discount on DM-context streams", 0.30, PCT, True, "Program term: rights holder accepts a 30% lower royalty on streams delivered in Radio, Autoplay and (since Jan 2024) Mixes. Could change at label renewals or under regulatory pressure."),
    ("Eligible-surface share of streams, 2025 (Radio + Autoplay + Mixes)", 0.18, PCT, True, "KEY LEVER 'e'. Not disclosed. Spotify: 33% of discoveries happen in algorithmic contexts; third parties put algorithmic listening near 40% of streams, of which Radio/Autoplay/Mixes is a subset; enrolled established artists in the DM workbook report DM-context at 3.5-5% of their streams. Plausible range 12-25%. This is what 'autoplay growth' moves."),
    ("Discovery Mode share of marketplace gross profit, 2025", 0.45, PCT, True, "KEY LEVER. Not disclosed. Marquee/Showcase are booked as Ad-Supported revenue (+EUR 58m in 2024 from marketplace growth); DM is a reduction of cost of revenue. Range 35-65%. Used only to calibrate the 2025 enrolled share below."),
    ("Base revenue growth 2026E", 0.14, PCT, False, "Q3 2026 guide +14% YoY; 2030 target mid-teens CAGR."),
    ("Base revenue growth 2027E", 0.13, PCT, False, "Assumption."),
    ("Base revenue growth 2028E", 0.12, PCT, False, "Assumption."),
    ("Music royalty pool as % of revenue, forecast (held flat)", "=B20", PCT, False, "Linked to FY2025 derived value; royalties are the greater of a % of revenue and per-subscriber minimums, so the pool scales with revenue."),
]
r = 24
for label, val, fmt, key, note in params:
    put(ws, f"A{r}", label)
    put(ws, f"B{r}", val, BLACK if isinstance(val, str) and val.startswith("=") else BLUE, fmt, fill=YELLOW if key else None)
    put(ws, f"F{r}", note, ITAL, wrap=True)
    r += 1
# rows 24..30

put(ws, "A32", "C. Calibration of the 2025 enrolled share (solve for 's' from the top-down marketplace figure)", H2)
put(ws, "A33", "Top-down FY2025 DM gross profit (EUR m)"); put(ws, "B33", "=B18*B26", BLACK, EUR)
put(ws, "A34", "Royalty pool on eligible surfaces (EUR m) = pool x e"); put(ws, "B34", "=B17*B25", BLACK, EUR)
put(ws, "A35", "Implied enrolled share of eligible-surface streams, 2025 ('s')"); put(ws, "B35", "=IF(B34*B24=0,0,B33/(B34*B24))", BLACK, PCT, fill=YELLOW)
put(ws, "F35", "s = DM gross profit / (pool x e x discount). This is Topic 2 in the triangulation matrix: replace with the expert-call figure when available and the sheet re-solves nothing else; set DM share (B26) so that B35 matches the calls.", ITAL, wrap=True)
put(ws, "A36", "Ceiling: DM gross profit if 100% of eligible-surface streams enrolled, 2025 (EUR m)"); put(ws, "B36", "=B34*B24", BLACK, EUR)
put(ws, "A37", "Ceiling as share of FY2025 revenue"); put(ws, "B37", "=B36/B6", BLACK, PCT2)
put(ws, "A38", "Remaining runway at current surfaces and discount (EUR m)"); put(ws, "B38", "=B36-B33", BLACK, EUR)
put(ws, "A39", "Remaining runway as share of FY2025 revenue"); put(ws, "B39", "=B38/B6", BLACK, PCT2)
put(ws, "F39", "The whole remaining DM lever at today's surfaces is this many points of margin, and it shrinks in bps terms as revenue grows. Only 'e' (autoplay share, new surfaces) or the discount rate can expand it.", ITAL, wrap=True)

put(ws, "A41", "D. Sensitivity: implied 2025 enrolled share 's' for combinations of e (rows) and DM share of marketplace GP (columns)", H2)
e_vals = [0.12, 0.15, 0.18, 0.21, 0.25]
d_vals = [0.35, 0.45, 0.55, 0.65]
put(ws, "A42", "e  \\  DM share of marketplace GP", BOLD)
for j, dv in enumerate(d_vals):
    put(ws, f"{get_column_letter(2+j)}42", dv, BLUE, PCT, bold=True)
for i, ev in enumerate(e_vals):
    rr = 43 + i
    put(ws, f"A{rr}", ev, BLUE, PCT)
    for j in range(len(d_vals)):
        col = get_column_letter(2 + j)
        put(ws, f"{col}{rr}", f"=IF($A{rr}*$B$24=0,0,($B$18*{col}$42)/($B$17*$A{rr}*$B$24))", BLACK, PCT)
put(ws, "A48", "Reading: a cell above 100% means that combination is impossible (DM would need more streams than the surfaces carry). The expert calls on Topic 2 and Topic 3 should land in a cell of this grid.", ITAL, wrap=True)
ws.merge_cells("A48:F48"); ws.row_dimensions[48].height = 28
for rr in range(6, 18): ws.row_dimensions[rr].height = 30
for rr in range(24, 31): ws.row_dimensions[rr].height = 42
ws.row_dimensions[25].height = 70; ws.row_dimensions[26].height = 55; ws.row_dimensions[35].height = 55; ws.row_dimensions[39].height = 42
ws.freeze_panes = "B6"

# =====================================================================================
# Sheet 2: Scenarios
# =====================================================================================
sc = wb.create_sheet("Scenarios")
setw(sc, [62, 14, 14, 14, 14, 60])
put(sc, "A1", "Gross margin bridge under three Discovery Mode / autoplay paths", TITLE)
put(sc, "A2", "Each block: set the yearly path of e (eligible-surface share) and s (enrolled share) and the Marquee/Showcase growth rate. DM gross profit = royalty pool x e x s x discount. Blue inputs; everything else is formula.", ITAL)
sc.merge_cells("A2:F2"); sc.row_dimensions[2].height = 30
years = ["2025A", "2026E", "2027E", "2028E"]
cols = ["B", "C", "D", "E"]

put(sc, "A4", "Common lines", H2)
put(sc, "A5", "Year", BOLD)
for c, y in zip(cols, years): put(sc, f"{c}5", y, BOLD)
put(sc, "A6", "Revenue growth"); put(sc, "B6", None)
put(sc, "C6", "=Inputs!B27", GREEN, PCT); put(sc, "D6", "=Inputs!B28", GREEN, PCT); put(sc, "E6", "=Inputs!B29", GREEN, PCT)
put(sc, "A7", "Revenue (EUR m)"); put(sc, "B7", "=Inputs!B6", GREEN, EUR)
for p, c in zip(cols[:-1], cols[1:]): put(sc, f"{c}7", f"={p}7*(1+{c}6)", BLACK, EUR)
put(sc, "A8", "Music royalty pool (EUR m) = revenue x pool %"); put(sc, "B8", "=Inputs!B17", GREEN, EUR)
for c in cols[1:]: put(sc, f"{c}8", f"={c}7*Inputs!$B$30", BLACK, EUR)
put(sc, "A9", "DM discount rate");
for c in cols: put(sc, f"{c}9", "=Inputs!$B$24", GREEN, PCT)
put(sc, "A10", "Other gross margin drivers, cumulative vs 2025 (pricing, audiobooks, podcasts, ad mix): INPUT, replace from your P&L model")
put(sc, "B10", 0, BLUE, BPS); put(sc, "C10", 100, BLUE, BPS, fill=YELLOW); put(sc, "D10", 180, BLUE, BPS, fill=YELLOW); put(sc, "E10", 240, BLUE, BPS, fill=YELLOW)
put(sc, "F10", "Basis points. Default set so the 'Slowing' case lands near H1 2026 actuals (33.0-33.4%) and the Q3 guide (32.9%): i.e. ~+100 bps in 2026 from everything except Discovery Mode and Marquee. Replace with your own non-marketplace bridge.", ITAL, wrap=True)
sc.row_dimensions[10].height = 55
put(sc, "A11", "FY2025 gross margin (base)"); put(sc, "B11", "=Inputs!B9", GREEN, PCT)
put(sc, "A12", "Reference: Q3 2026 guide / 2030 target midpoint"); put(sc, "C12", "=Inputs!B12", GREEN, PCT); put(sc, "E12", "=(Inputs!B13+Inputs!B14)/2", GREEN, PCT)
put(sc, "F12", "2030 midpoint shown in the 2028E column only as a direction marker, not a 2028 forecast.", ITAL)

def block(top, name, desc, e_path, s_path, mq_growth):
    put(sc, f"A{top}", name, H2); put(sc, f"A{top+1}", desc, ITAL, wrap=True); sc.merge_cells(f"A{top+1}:F{top+1}"); sc.row_dimensions[top+1].height = 42
    r0 = top + 2
    put(sc, f"A{r0}", "Year", BOLD)
    for c, y in zip(cols, years): put(sc, f"{c}{r0}", y, BOLD)
    put(sc, f"A{r0+1}", "e: eligible-surface share of streams (Radio + Autoplay + Mixes)")
    put(sc, f"B{r0+1}", "=Inputs!$B$25", GREEN, PCT)
    for c, v in zip(cols[1:], e_path): put(sc, f"{c}{r0+1}", v, BLUE, PCT, fill=YELLOW)
    put(sc, f"A{r0+2}", "s: enrolled share of eligible-surface streams")
    put(sc, f"B{r0+2}", "=Inputs!$B$35", GREEN, PCT)
    for c, v in zip(cols[1:], s_path): put(sc, f"{c}{r0+2}", v, BLUE, PCT, fill=YELLOW)
    put(sc, f"A{r0+3}", "DM-context enrolled streams as share of all streams = e x s")
    for c in cols: put(sc, f"{c}{r0+3}", f"={c}{r0+1}*{c}{r0+2}", BLACK, PCT)
    put(sc, f"A{r0+4}", "Discovery Mode gross profit (EUR m) = pool x e x s x discount")
    for c in cols: put(sc, f"{c}{r0+4}", f"={c}$8*{c}{r0+3}*{c}$9", BLACK, EUR)
    put(sc, f"A{r0+5}", "DM contribution to consolidated gross margin (bps)")
    for c in cols: put(sc, f"{c}{r0+5}", f"={c}{r0+4}/{c}$7*10000", BLACK, BPS)
    put(sc, f"A{r0+6}", "DM contribution: change vs 2025 (bps)")
    put(sc, f"B{r0+6}", 0, BLACK, BPS)
    for c in cols[1:]: put(sc, f"{c}{r0+6}", f"={c}{r0+5}-$B{r0+5}", BLACK, BPS)
    put(sc, f"A{r0+7}", "Marquee + Showcase gross profit growth (input)")
    for c, v in zip(cols[1:], mq_growth): put(sc, f"{c}{r0+7}", v, BLUE, PCT)
    put(sc, f"A{r0+8}", "Marquee + Showcase gross profit (EUR m)")
    put(sc, f"B{r0+8}", "=Inputs!$B$18-Inputs!$B$33", GREEN, EUR)
    for p, c in zip(cols[:-1], cols[1:]): put(sc, f"{c}{r0+8}", f"={p}{r0+8}*(1+{c}{r0+7})", BLACK, EUR)
    put(sc, f"A{r0+9}", "Marquee + Showcase contribution to gross margin (bps)")
    for c in cols: put(sc, f"{c}{r0+9}", f"={c}{r0+8}/{c}$7*10000", BLACK, BPS)
    put(sc, f"A{r0+10}", "Marquee + Showcase: change vs 2025 (bps)")
    put(sc, f"B{r0+10}", 0, BLACK, BPS)
    for c in cols[1:]: put(sc, f"{c}{r0+10}", f"={c}{r0+9}-$B{r0+9}", BLACK, BPS)
    put(sc, f"A{r0+11}", "Total marketplace gross profit (EUR m)")
    for c in cols: put(sc, f"{c}{r0+11}", f"={c}{r0+4}+{c}{r0+8}", BLACK, EUR)
    put(sc, f"A{r0+12}", "Implied marketplace gross profit growth")
    for p, c in zip(cols[:-1], cols[1:]): put(sc, f"{c}{r0+12}", f"={c}{r0+11}/{p}{r0+11}-1", BLACK, PCT)
    put(sc, f"A{r0+13}", "Gross margin = 2025 base + other drivers + DM change + Marquee change", bold=True)
    for c in cols: put(sc, f"{c}{r0+13}", f"=$B$11+({c}$10+{c}{r0+6}+{c}{r0+10})/10000", BLACK, PCT, fill=GREY, bold=True)
    put(sc, f"A{r0+14}", "Gross margin expansion vs 2025 (bps)")
    for c in cols: put(sc, f"{c}{r0+14}", f"=({c}{r0+13}-$B$11)*10000", BLACK, BPS)
    put(sc, f"A{r0+15}", "Of which from marketplace (DM + Marquee), bps")
    for c in cols: put(sc, f"{c}{r0+15}", f"={c}{r0+6}+{c}{r0+10}", BLACK, BPS)
    return r0 + 15

end_a = block(14, "Scenario A: continued growth (the street-style path)",
    "Autoplay / programmed listening keeps gaining share (e +1.5 pt a year, including new surfaces such as Smart Shuffle or DJ sessions), enrollment keeps rising (s +8 pts a year), Marquee/Showcase grows 20% a year. Roughly extends the 2021-25 marketplace growth rate.",
    [0.195, 0.21, 0.225], [0.61, 0.69, 0.77], [0.20, 0.20, 0.20])
end_b = block(end_a + 2, "Scenario B: slowing (the thesis in the two workbooks)",
    "Autoplay share plateaus (e flat): Reddit mentions of autoplay/recs peaked in 2025, DJ/Smart Shuffle discussion has halved from 2024, Smart Shuffle became removable in April 2025. Enrollment still creeps up because staying in is defensive (s +3 pts a year) but new surfaces do not arrive. Marquee/Showcase +10% a year.",
    [0.18, 0.18, 0.18], [0.56, 0.59, 0.62], [0.10, 0.10, 0.10])
end_c = block(end_b + 2, "Scenario C: saturation with backlash",
    "Eligible surfaces lose share (e -1 pt a year: users disable autoplay / Smart Shuffle, AI-slop clean-up trims recommendation volume), enrollment caps out at the 2026 level (label pushback, Congressional scrutiny, or lifts too small to justify the 30%), Marquee/Showcase flat.",
    [0.17, 0.16, 0.15], [0.55, 0.55, 0.55], [0.0, 0.0, 0.0])

top = end_c + 2
put(sc, f"A{top}", "Summary: gross margin by scenario", H2)
put(sc, f"A{top+1}", "Year", BOLD)
for c, y in zip(cols, years): put(sc, f"{c}{top+1}", y, BOLD)
put(sc, f"A{top+2}", "Scenario A: continued growth"); put(sc, f"A{top+3}", "Scenario B: slowing"); put(sc, f"A{top+4}", "Scenario C: saturation with backlash")
put(sc, f"A{top+5}", "Spread A minus C (bps)")
for c in cols:
    put(sc, f"{c}{top+2}", f"={c}{end_a}", BLACK, PCT)       # wait: end_a is r0+15 (the 'of which' row). GM row is r0+13 = end-2
for c in cols:
    put(sc, f"{c}{top+2}", f"={c}{end_a-2}", BLACK, PCT, fill=GREY)
    put(sc, f"{c}{top+3}", f"={c}{end_b-2}", BLACK, PCT, fill=GREY)
    put(sc, f"{c}{top+4}", f"={c}{end_c-2}", BLACK, PCT, fill=GREY)
    put(sc, f"{c}{top+5}", f"=({c}{top+2}-{c}{top+4})*10000", BLACK, BPS)
put(sc, f"A{top+6}", "Marketplace gross profit growth needed just to hold its margin contribution flat = revenue growth");
for c in cols[1:]: put(sc, f"{c}{top+6}", f"={c}6", BLACK, PCT)
put(sc, f"F{top+6}", "If marketplace gross profit grows slower than revenue, it is a margin headwind in bps even while it grows in euros.", ITAL, wrap=True)
sc.row_dimensions[top+6].height = 30
sc.freeze_panes = "B6"

# =====================================================================================
# Sheet 3: 2028 sensitivity
# =====================================================================================
se = wb.create_sheet("Sensitivity 2028")
setw(se, [40, 12, 12, 12, 12, 12, 12, 12])
put(se, "A1", "DM contribution to 2028E consolidated gross margin (bps) for combinations of e (rows) and s (columns)", TITLE)
put(se, "A2", "Uses the common revenue path and discount from Scenarios. Compare any cell with the 2025 contribution (bottom) to read the incremental bps.", ITAL)
s_vals = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
e_vals2 = [0.12, 0.15, 0.18, 0.21, 0.24]
put(se, "A4", "e  \\  s", BOLD)
for j, sv in enumerate(s_vals): put(se, f"{get_column_letter(2+j)}4", sv, BLUE, PCT, bold=True)
for i, ev in enumerate(e_vals2):
    rr = 5 + i
    put(se, f"A{rr}", ev, BLUE, PCT)
    for j in range(len(s_vals)):
        col = get_column_letter(2 + j)
        put(se, f"{col}{rr}", f"=Scenarios!$E$8*$A{rr}*{col}$4*Scenarios!$E$9/Scenarios!$E$7*10000", BLACK, BPS)
put(se, "A11", "2025A DM contribution (bps), from Inputs"); put(se, "B11", "=Inputs!B33/Inputs!B6*10000", GREEN, BPS)
put(se, "A12", "2025A e and s"); put(se, "B12", "=Inputs!B25", GREEN, PCT); put(se, "C12", "=Inputs!B35", GREEN, PCT)
put(se, "A13", "Reading: at the calibrated e (18%) you need s to rise by roughly 10 pts per year just to add ~30 bps by 2028; with e flat and s flat the DM lever adds nothing further. Cells to the right of s = 100% are impossible.", ITAL, wrap=True)
se.merge_cells("A13:H13"); se.row_dimensions[13].height = 40

# =====================================================================================
# Sheet 4: Evidence
# =====================================================================================
ev = wb.create_sheet("Evidence")
setw(ev, [50, 12, 12, 12, 12, 16, 70])
put(ev, "A1", "What the two workbooks say, mapped to the model's levers", TITLE)
put(ev, "A2", "Counts are copied from data/spotify_autoplay_sentiment.xlsx and data/discovery_mode_efficacy.xlsx (blue); ratios are formulas. See the memo for method caveats.", ITAL)

put(ev, "A4", "1. Autoplay / recommendation discussion on r/spotify + r/truespotify (lever: e)", H2)
hdr = ["Metric", "2023", "2024", "2025", "2026 YTD", "Lever", "Reading"]
for j, h in enumerate(hdr): put(ev, f"{get_column_letter(1+j)}5", h, BOLD)
put(ev, "A6", "All posts");
for c, v in zip(["B","C","D","E"], [67394, 72114, 45831, 25026]): put(ev, f"{c}6", v, BLUE, EUR)
put(ev, "A7", "Posts about autoplay / recommendations")
for c, v in zip(["B","C","D","E"], [4793, 7156, 5425, 2574]): put(ev, f"{c}7", v, BLUE, EUR)
put(ev, "A8", "Share of all posts");
for c in ["B","C","D","E"]: put(ev, f"{c}8", f"={c}7/{c}6", BLACK, PCT)
put(ev, "F8", "e", BOLD); put(ev, "G8", "Share rose through 2025 and slipped in 2026 YTD. Weak evidence of a plateau: the 2026 archive is thin for Jul-Sep, and total subreddit volume is falling.", ITAL, wrap=True)
put(ev, "A9", "Posts mentioning DJ / daylist / Smart Shuffle")
for c, v in zip(["B","C","D","E"], [947, 1231, 778, 411]): put(ev, f"{c}9", v, BLUE, EUR)
put(ev, "A10", "  as share of autoplay posts")
for c in ["B","C","D","E"]: put(ev, f"{c}10", f"={c}9/{c}7", BLACK, PCT)
put(ev, "F10", "e", BOLD); put(ev, "G10", "The AI DJ / Smart Shuffle novelty is fading: mention share fell from 20% to 16%. Smart Shuffle became removable in April 2025 (959-upvote post).", ITAL, wrap=True)
put(ev, "A11", "Posts mentioning Discover Weekly / Release Radar")
for c, v in zip(["B","C","D","E"], [367, 572, 567, 257]): put(ev, f"{c}11", v, BLUE, EUR)
put(ev, "A12", "  as share of autoplay posts")
for c in ["B","C","D","E"]: put(ev, f"{c}12", f"={c}11/{c}7", BLACK, PCT)
put(ev, "A13", "Posts on AI-generated music")
for c, v in zip(["B","C","D","E"], [15, 43, 169, 119]): put(ev, f"{c}13", v, BLUE, EUR)
put(ev, "A14", "  as share of autoplay posts")
for c in ["B","C","D","E"]: put(ev, f"{c}14", f"={c}13/{c}7", BLACK, PCT)
put(ev, "F14", "e (quality)", BOLD); put(ev, "G14", "From 0.3% to 4.6% of topic posts. The clean-up Spotify announced in Sept 2025 (AI labels, spam filter) trims recommendation inventory and is the main channel by which e could fall.", ITAL, wrap=True)
put(ev, "A15", "Posts on paid / pushed content (Discovery Mode, payola, sponsored)")
for c, v in zip(["B","C","D","E"], [24, 89, 55, 47]): put(ev, f"{c}15", v, BLUE, EUR)
put(ev, "A16", "  as share of autoplay posts")
for c in ["B","C","D","E"]: put(ev, f"{c}16", f"={c}15/{c}7", BLACK, PCT)
put(ev, "F16", "backlash", BOLD); put(ev, "G16", "Listener-side awareness of paid placement is small but at its highest in 2026. Only one of the 4,000 scored posts says 'discovery mode' by name: listeners do not see the program, they see 'sponsored recs'.", ITAL, wrap=True)

put(ev, "A18", "2. Sentiment of the scored sample (1,000 posts per year)", H2)
for j, h in enumerate(hdr): put(ev, f"{get_column_letter(1+j)}19", h, BOLD)
put(ev, "A20", "Negative, all scored posts")
for c, v in zip(["B","C","D","E"], [340, 366, 391, 424]): put(ev, f"{c}20", v, BLUE, EUR)
put(ev, "A21", "Positive, all scored posts")
for c, v in zip(["B","C","D","E"], [232, 246, 279, 242]): put(ev, f"{c}21", v, BLUE, EUR)
put(ev, "A22", "Share negative, headline")
for c in ["B","C","D","E"]: put(ev, f"{c}22", f"={c}20/1000", BLACK, PCT)
put(ev, "A23", "Net sentiment (positive minus negative share)")
for c in ["B","C","D","E"]: put(ev, f"{c}23", f"=({c}21-{c}20)/1000", BLACK, PCT)
put(ev, "A24", "Deleted / removed posts in sample (title only)")
for c, v in zip(["B","C","D","E"], [262, 143, 39, 47]): put(ev, f"{c}24", v, BLUE, EUR)
put(ev, "A25", "Negative among deleted / removed")
for c, v in zip(["B","C","D","E"], [60, 30, 8, 9]): put(ev, f"{c}25", v, BLUE, EUR)
put(ev, "A26", "Share negative, intact posts only (the cleaner series)")
for c in ["B","C","D","E"]: put(ev, f"{c}26", f"=({c}20-{c}25)/(1000-{c}24)", BLACK, PCT)
put(ev, "F26", "e, churn", BOLD); put(ev, "G26", "Deleted posts score ~21% negative vs ~40% for intact ones and were 26% of the 2023 sample but 4-5% of 2025-26. On intact posts the deterioration is ~5-6 pts, not 8. Still rising, with 2026 H1 the worst half; 2026 Q3 improved to 39%.", ITAL, wrap=True)
put(ev, "A27", "Share of scored posts with cancel / switch language")
for c, v in zip(["B","C","D","E"], [0.006, 0.014, 0.012, 0.024]): put(ev, f"{c}27", v, BLUE, PCT)
put(ev, "G27", "Regex on cancel / unsubscribe / switched to Apple, Tidal, YouTube / goodbye Spotify. 56 posts in total; directional only.", ITAL, wrap=True)
put(ev, "A28", "Discovery love posts, share positive")
for c, v in zip(["B","C","D","E"], [0.71, 0.44, 0.71, 0.68]): put(ev, f"{c}28", v, BLUE, PCT)
put(ev, "G28", "The pro-recommendation pocket is stable at ~1-2% of topic posts: the user base is polarising, not uniformly souring.", ITAL, wrap=True)

put(ev, "A30", "3. Discovery Mode efficacy (lever: s and the discount)", H2)
for j, h in enumerate(["Metric", "Value", "n", "", "", "Lever", "Reading"]): put(ev, f"{get_column_letter(1+j)}31", h, BOLD)
dm_rows = [
    ("Median Spotify-reported lift, campaigns Aug 2023 - Nov 2024", 4.06, 4, MULT, "s", "Lift = DM-context streams in campaign / prior 28 days - 1. n = 4 vs 3: the gap is not statistically meaningful (Mann-Whitney p ~ 0.1) and the metric rewards songs with a tiny prior base."),
    ("Median Spotify-reported lift, campaigns Jan 2025 - Jul 2026", 0.78, 3, MULT, "s", "Direction is consistent with a crowded pool: a fixed set of Radio/Autoplay slots shared by more enrolled tracks."),
    ("Saves + playlist adds per DM listener (median, 8 campaigns)", 0.0124, 8, PCT2, "quality", "Spotify's own 'intent' metric. 0.7-4.8% per campaign; latest (Sep 2026) is the lowest at 0.68%."),
    ("Saves per listener, artists' overall audience (median, 4 dashboards)", 0.1985, 4, PCT, "quality", "Different definition (saves only, 12 months) so read as order of magnitude: DM streams are ~16x lower intent. They still carry a royalty, at 70%."),
    ("Share of first-hand reports that went up: artists under 10k listeners", 1.00, 8, PCT, "s", "All eight small artists went up; the long tail will keep enrolling."),
    ("Share of first-hand reports that went up: artists 10k+ listeners", 0.389, 18, PCT, "s", "Above 10k it is a coin flip; mid-size indies are the enrollment that can leave."),
    ("First-hand reports (all)", 0.557, 70, PCT, "s", "39 up / 21 down / 7 mixed / 3 flat."),
    ("DM-context streams as share of an enrolled artist's streams, established artists", 0.04, 4, PCT, "e", "3.5-5% for 500k+ monthly-stream artists; 33-50% for catalog-heavy or tiny artists. The workbook's 7.5% 'median' mixes both groups."),
    ("Switching DM off: change in radio / autoplay streams per day (two charted cases)", -0.6, 2, PCT, "s (defensive)", "-50% and -71%. Enrollment has become defensive, which supports enrollment creeping up even as the lift fades: good for s, bad for the program's reputation."),
]
r = 32
for label, val, n, fmt, lever, note in dm_rows:
    put(ev, f"A{r}", label); put(ev, f"B{r}", val, BLUE, fmt); put(ev, f"C{r}", n, BLUE, EUR); put(ev, f"F{r}", lever, BOLD); put(ev, f"G{r}", note, ITAL, wrap=True)
    ev.row_dimensions[r].height = 42
    r += 1
for rr in [8, 10, 14, 16, 26, 27, 28]: ev.row_dimensions[rr].height = 42
ev.freeze_panes = "B6"

# =====================================================================================
# Sheet 5: Notes
# =====================================================================================
nt = wb.create_sheet("Notes")
setw(nt, [28, 120])
put(nt, "A1", "Method, sources and caveats", TITLE)
notes = [
    ("Mechanics", "Discovery Mode is a royalty discount, not revenue: 'Cost of revenue also reflects discounts provided by certain rights holders in return for promotional activities in connection with marketplace programs' (Spotify 20-F). Marquee and Showcase are sold to labels and booked as Ad-Supported revenue. So DM lifts Premium and Ad-Supported gross margin in proportion to where DM streams occur; Marquee lifts Ad-Supported revenue at near-100% margin."),
    ("Why DM is a bounded lever", "DM reallocates a fixed pool of Radio / Autoplay / Mixes slots among enrolled tracks; it does not create streams (the Jan 2025 case: Spotify reported +55% in DM contexts while the song's total streams fell). Spotify's saving is therefore enrolled DM-context streams x 30% of their royalty, regardless of whether the artist gains. The ceiling is e x discount x royalty pool; only a larger e (autoplay share, new surfaces) or a bigger discount raises it."),
    ("Why 'slowing' is a margin headwind, not just slower help", "Gross margin is a ratio. With revenue compounding at 12-14%, marketplace gross profit must grow at least that fast to hold its bps contribution; 2021-25 it grew ~41% a year. Scenario B (+8-12% a year) is close to zero incremental bps; Scenario C is negative."),
    ("Calibration", "Marketplace gross profit 2025 ~ EUR 640m (4 x 'more than EUR 160m' in 2021) ~ 370 bps of consolidated GM. DM's share is undisclosed; at 45% it is ~EUR 290m ~ 170 bps. With e = 18% and a EUR 10.1bn royalty pool, that implies ~53% of eligible-surface streams are enrolled. Topic 2 and Topic 3 of the triangulation matrix exist to replace these two guesses."),
    ("What the Reddit data can and cannot say", "r/spotify + r/truespotify posts, Arctic Shift archive, 210k posts. The topic share (7% -> 12% -> 10%) is the best proxy for autoplay salience, not usage. The sentiment model (twitter-roberta) scores overall tone, not tone toward the algorithm; deleted posts bias early years toward neutral; 2026 coverage is thin after June. Treat sentiment as a direction-of-travel input to e, worth no more than +/- 1 pt a year."),
    ("What the DM data can and cannot say", "70 first-hand artist reports and 35 screenshots from r/musicmarketing, self-selected. 7 campaign lifts (n = 4 vs 3 by era), 18 before/after pairs that actually trend toward 'Up' over time (mix shift toward small artists). The 'Reference' sheet's undated lift list mixes multiples and percentages and should not be used. Use the workbook for mechanism and direction, not magnitudes."),
    ("Sources", "Spotify FY2025 20-F; Q1 and Q2 2026 shareholder letters (sec.gov 6-K exhibits); Investor Day June 8 2022 transcript (marketplace EUR 160m+ in 2021); Investor Day May 21 2026 recap (marketplace 4x since 2021; 35-40% GM by 2030); Loud & Clear 2026 (USD 11bn royalties 2025); artists.spotify.com Discovery Mode page (+50% saves, +44% playlist adds, +37% follows in month one; 33% of discoveries in algorithmic contexts); Billboard reporting on House Judiciary scrutiny and manager-reported fade of lifts from 200-300% to 20-30%."),
    ("Reproduce", "analysis/build_gm_model.py builds this workbook; data/ holds the two source workbooks."),
]
r = 3
for k, v in notes:
    put(nt, f"A{r}", k, BOLD); put(nt, f"B{r}", v, BLACK, wrap=True); nt.row_dimensions[r].height = 75
    r += 1

wb.save(OUT)
print("saved", OUT)
