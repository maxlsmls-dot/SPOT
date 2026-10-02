"""Build the Discovery Mode -> gross margin workbook (Spotify, SPOT)."""
import sys

from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.chart.text import RichText, Text
from openpyxl.chart.title import Title
from openpyxl.drawing.line import LineProperties
from openpyxl.drawing.text import CharacterProperties, Font as DFont, Paragraph, ParagraphProperties, RegularTextRun
from openpyxl.styles import Alignment, Font, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

OUT = sys.argv[1] if len(sys.argv) > 1 else "discovery_mode_gross_margin.xlsx"

F = "Arial"
TITLE = Font(name=F, size=14, bold=True)
H2 = Font(name=F, size=11, bold=True)
HDR = Font(name=F, size=10, bold=True, color="52514E")
TXT = Font(name=F, size=10)
BOLD = Font(name=F, size=10, bold=True)
INP = Font(name=F, size=10, color="0000FF")
FML = Font(name=F, size=10)
FMLB = Font(name=F, size=10, bold=True)
LNK = Font(name=F, size=10, color="008000")
NOTE = Font(name=F, size=9, italic=True, color="52514E")
HFILL = PatternFill("solid", fgColor="F0EFEC")
KEYFILL = PatternFill("solid", fgColor="FFFF00")
WRAP = Alignment(wrap_text=True, vertical="top")
RIGHT = Alignment(horizontal="right")
THIN = Side(style="thin", color="C3C2B7")
TOPLINE = Border(top=THIN)

BLUE, ORANGE, AQUA, GRID = "2A78D6", "EB6834", "1BAF7A", "E1E0D9"

YEARS = list(range(2021, 2031))
YC = [get_column_letter(3 + i) for i in range(len(YEARS))]   # C..L
COL = dict(zip(YEARS, YC))
HIST = YEARS[:5]      # FY2021A-FY2025A
FC = YEARS[5:]        # FY2026E-FY2030E


def put(ws, r, c, v, font=TXT, fmt=None, align=None, fill=None, border=None):
    if isinstance(c, str):
        cell = ws[f"{c}{r}"]
        cell.value = v
    else:
        cell = ws.cell(row=r, column=c, value=v)
    cell.font = font
    if fmt:
        cell.number_format = fmt
    if align:
        cell.alignment = align
    if fill:
        cell.fill = fill
    if border:
        cell.border = border
    return cell


def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def year_header(ws, r, label="EUR m unless stated", unit_hdr="Unit"):
    put(ws, r, 1, label, HDR, fill=HFILL)
    put(ws, r, 2, unit_hdr, HDR, fill=HFILL)
    for y in YEARS:
        put(ws, r, COL[y], f"FY{y}{'A' if y in HIST else 'E'}", HDR, align=RIGHT, fill=HFILL)


def section(ws, r, text):
    put(ws, r, 1, text, H2)


def note(ws, r, text, span=12):
    put(ws, r, 1, text, NOTE, align=WRAP)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=span)
    ws.row_dimensions[r].height = 28


def row_values(ws, r, label, unit, values, font, fmt, years=YEARS):
    """values: dict year->value (or formula string)."""
    put(ws, r, 1, label, TXT)
    put(ws, r, 2, unit, NOTE)
    for y in years:
        v = values.get(y)
        if v is None:
            continue
        put(ws, r, COL[y], v, font, fmt, RIGHT)


def rich_title(text, size, bold):
    cp = CharacterProperties(sz=size, b=bold, latin=DFont(typeface=F), solidFill="0B0B0B")
    para = Paragraph(pPr=ParagraphProperties(defRPr=cp), r=[RegularTextRun(rPr=cp, t=text)])
    return Title(tx=Text(rich=RichText(p=[para])), overlay=False)


def small_text(size=900):
    cp = CharacterProperties(sz=size, latin=DFont(typeface=F), solidFill="52514E")
    return RichText(p=[Paragraph(pPr=ParagraphProperties(defRPr=cp), endParaRPr=cp)])


def style_chart(ch, title, y_title=None, y_fmt=None, w=20, h=9):
    ch.title = rich_title(title, 1200, True)
    ch.x_axis.delete = False
    ch.y_axis.delete = False
    ch.x_axis.txPr = small_text()
    ch.y_axis.txPr = small_text()
    ch.y_axis.majorGridlines.spPr = GraphicalProperties(ln=LineProperties(solidFill=GRID))
    if y_title:
        ch.y_axis.title = rich_title(y_title, 900, False)
    if y_fmt:
        ch.y_axis.numFmt = y_fmt
    ch.legend.position = "b"
    ch.legend.txPr = small_text()
    ch.width, ch.height = w, h


wb = Workbook()

# =============================================================================
# INPUTS
# =============================================================================
wi = wb.active
wi.title = "Inputs"
widths(wi, [62, 16] + [11] * 10)
put(wi, 1, 1, "Inputs and scenarios (blue = hardcoded input; black = formula)", TITLE)
put(wi, 2, 1, "Change the scenario selector or any blue cell. History (FY2021-25) uses the same estimate in every scenario; scenarios diverge from FY2026.", NOTE)

put(wi, 4, 1, "Scenario selector (1 = Bear, 2 = Base, 3 = Bull)", BOLD)
put(wi, 4, 2, 2, INP, "0", RIGHT, KEYFILL)
put(wi, 4, 3, '=CHOOSE($B$4,"Bear","Base","Bull")', FMLB)
SEL = "Inputs!$B$4"

year_header(wi, 6, "Assumption")

section(wi, 7, "Constants")
put(wi, 8, 1, "Recording royalties as % of music revenue (r_rec)", TXT)
put(wi, 8, 2, "% of music rev", NOTE)
put(wi, 8, 3, 0.54, INP, "0.0%", RIGHT)
put(wi, 8, 4, "Spotify does not disclose. MIDiA per-stream split 30% DSP / 56% recording / 14% publishing; FY2025 Premium cost of revenue 66% of Premium revenue incl. publishing, delivery, audiobooks. Range 50-58%.", NOTE)
R_REC = "Inputs!$C$8"
put(wi, 9, 1, "Music share of total revenue (m)", TXT)
put(wi, 9, 2, "% of total rev", NOTE)
put(wi, 9, 3, 0.92, INP, "0.0%", RIGHT)
put(wi, 9, 4, "Podcast advertising, audiobook a-la-carte and other non-music revenue carry no Discovery Mode commission. Assumption.", NOTE)
M_SHARE = "Inputs!$C$9"

# --- s_ctx ---------------------------------------------------------------
section(wi, 11, "A. DM-eligible context share of music streams (Spotify Radio + Autoplay + Spotify Mixes) - s_ctx")
hist_ctx = {2021: 0.09, 2022: 0.09, 2023: 0.095, 2024: 0.13, 2025: 0.14}
ctx = {
    "Bear": {**hist_ctx, 2026: 0.14, 2027: 0.14, 2028: 0.14, 2029: 0.14, 2030: 0.14},
    "Base": {**hist_ctx, 2026: 0.145, 2027: 0.15, 2028: 0.155, 2029: 0.16, 2030: 0.165},
    "Bull": {**hist_ctx, 2026: 0.15, 2027: 0.19, 2028: 0.20, 2029: 0.21, 2030: 0.22},
}
CTX_ROW = {}
for i, (name, vals) in enumerate(ctx.items()):
    r = 12 + i
    CTX_ROW[name] = r
    row_values(wi, r, f"  {name}", "% of music streams", vals, INP, "0.0%")
put(wi, 15, 1, "  Selected scenario", BOLD)
put(wi, 15, 2, "% of music streams", NOTE)
for y in YEARS:
    put(wi, 15, COL[y], f"=CHOOSE($B$4,{COL[y]}12,{COL[y]}13,{COL[y]}14)", FMLB, "0.0%", RIGHT)
CTX_SEL = 15
note(wi, 16, "History: Radio + Autoplay only until Daily Mix joined Discovery Mode on 3 Jan 2024 and Artist/Genre/Decade/Mood Mixes through 2024 (+3.5pp step). "
     "FY2025 base 14% sits inside the 9-20% triangulated range (see Triangulation sheet). Bear: flat. Base: +0.5pp a year as lean-back listening grows. "
     "Bull: +1pp a year plus a +3pp step in FY2027 if Spotify extends Discovery Mode to Smart Shuffle or other personalised surfaces (not a DM context today).")

# --- s_dm ----------------------------------------------------------------
section(wi, 18, "B. Discovery Mode-enrolled share of DM-context streams - s_dm")
hist_dm = {2021: 0.05, 2022: 0.10, 2023: 0.20, 2024: 0.28, 2025: 0.33}
dm = {
    "Bear": {**hist_dm, 2026: 0.315, 2027: 0.30, 2028: 0.285, 2029: 0.27, 2030: 0.255},
    "Base": {**hist_dm, 2026: 0.34, 2027: 0.35, 2028: 0.36, 2029: 0.37, 2030: 0.38},
    "Bull": {**hist_dm, 2026: 0.35, 2027: 0.43, 2028: 0.455, 2029: 0.48, 2030: 0.50},
}
DM_ROW = {}
for i, (name, vals) in enumerate(dm.items()):
    r = 19 + i
    DM_ROW[name] = r
    row_values(wi, r, f"  {name}", "% of context streams", vals, INP, "0.0%")
put(wi, 22, 1, "  Selected scenario", BOLD)
put(wi, 22, 2, "% of context streams", NOTE)
for y in YEARS:
    put(wi, 22, COL[y], f"=CHOOSE($B$4,{COL[y]}19,{COL[y]}20,{COL[y]}21)", FMLB, "0.0%", RIGHT)
DM_SEL = 22
note(wi, 23, "FY2025 = your 33% assumption; the Triangulation sheet shows it is consistent with ~28% of streams outside the majors and Merlin, about half of that catalog enrolled, "
     "and a ~3x in-context boost. History ramps from the Nov 2020 US beta (Radio/Autoplay, few licensors) through self-serve access for all distributors (Mar 2023). "
     "Bear: -1.5pp a year as the per-track boost fades and enrollment churns (the r/musicmarketing evidence). Base: +1pp a year toward a ~40% no-majors ceiling. "
     "Bull: a major label opts in during FY2027 (+8pp step), then +2.5pp a year toward 50%.")

# --- d -------------------------------------------------------------------
section(wi, 25, "C. Discovery Mode commission on recording royalties in DM contexts - d")
dd = {
    "Bear": {y: 0.30 for y in YEARS[:7]} | {2028: 0.25, 2029: 0.25, 2030: 0.25},
    "Base": {y: 0.30 for y in YEARS},
    "Bull": {y: 0.30 for y in YEARS},
}
D_ROW = {}
for i, (name, vals) in enumerate(dd.items()):
    r = 26 + i
    D_ROW[name] = r
    row_values(wi, r, f"  {name}", "% of royalty", vals, INP, "0.0%")
put(wi, 29, 1, "  Selected scenario", BOLD)
put(wi, 29, 2, "% of royalty", NOTE)
for y in YEARS:
    put(wi, 29, COL[y], f"=CHOOSE($B$4,{COL[y]}26,{COL[y]}27,{COL[y]}28)", FMLB, "0.0%", RIGHT)
D_SEL = 29
note(wi, 30, "Spotify for Artists: 'A 30% commission is applied to recording royalties generated from all streams of selected songs ... in Discovery Mode contexts.' "
     "Unchanged under the Sept 2025 terms. Bear cuts it to 25% from FY2028 for regulatory or litigation pressure (House Judiciary letters 2021-22; Capolongo class action Nov 2025).")

# --- revenue build inputs ----------------------------------------------
section(wi, 32, "D. Revenue build inputs (placeholder; paste your own revenue in row 40 to override)")
put(wi, 33, 1, "Premium subscribers, year end", TXT); put(wi, 33, 2, "m", NOTE)
subs_hist = {2021: 180, 2022: 205, 2023: 236, 2024: 263, 2025: 290}
for y in HIST:
    put(wi, 33, COL[y], subs_hist[y], INP, "#,##0", RIGHT)
for y in FC:
    prev = COL[y - 1]
    put(wi, 33, COL[y], f"={prev}33+{COL[y]}34", FML, "#,##0", RIGHT)
put(wi, 34, 1, "  Net subscriber additions", TXT); put(wi, 34, 2, "m", NOTE)
for y, v in zip(FC, [28, 26, 24, 22, 20]):
    put(wi, 34, COL[y], v, INP, "#,##0", RIGHT)
put(wi, 35, 1, "Premium ARPU (monthly)", TXT); put(wi, 35, 2, "EUR", NOTE)
arpu_hist = {2021: 4.29, 2022: 4.52, 2023: 4.39, 2024: 4.69, 2025: 4.63}
for y in HIST:
    put(wi, 35, COL[y], arpu_hist[y], INP, "0.00", RIGHT)
for y in FC:
    put(wi, 35, COL[y], f"={COL[y - 1]}35*(1+{COL[y]}36)", FML, "0.00", RIGHT)
put(wi, 36, 1, "  ARPU growth", TXT); put(wi, 36, 2, "%", NOTE)
for y, v in zip(FC, [0.055, 0.04, 0.04, 0.035, 0.035]):
    put(wi, 36, COL[y], v, INP, "0.0%", RIGHT)
put(wi, 37, 1, "Premium revenue, reported", TXT); put(wi, 37, 2, "EUR m", NOTE)
prem_hist = {2021: 8460, 2022: 10251, 2023: 11566, 2024: 13819, 2025: 15350}
for y in HIST:
    put(wi, 37, COL[y], prem_hist[y], INP, "#,##0", RIGHT)
put(wi, 38, 1, "Ad-Supported revenue, reported / growth", TXT); put(wi, 38, 2, "EUR m", NOTE)
ad_hist = {2021: 1208, 2022: 1476, 2023: 1681, 2024: 1854, 2025: 1836}
for y in HIST:
    put(wi, 38, COL[y], ad_hist[y], INP, "#,##0", RIGHT)
put(wi, 39, 1, "  Ad-Supported revenue growth", TXT); put(wi, 39, 2, "%", NOTE)
for y, v in zip(FC, [0.02, 0.05, 0.05, 0.05, 0.05]):
    put(wi, 39, COL[y], v, INP, "0.0%", RIGHT)
put(wi, 40, 1, "Total revenue OVERRIDE (paste your revenue build here; blank = use placeholder)", BOLD); put(wi, 40, 2, "EUR m", NOTE)
for y in FC:
    put(wi, 40, COL[y], None, INP, "#,##0", RIGHT, KEYFILL)
put(wi, 41, 1, "Cost of revenue, reported", TXT); put(wi, 41, 2, "EUR m", NOTE)
cor_hist = {2021: 7077, 2022: 8801, 2023: 9849, 2024: 10955, 2025: 11690}
for y in HIST:
    put(wi, 41, COL[y], cor_hist[y], INP, "#,##0", RIGHT)
note(wi, 42, "History from 20-F filings (FY2021-FY2025); see Financials sheet. FY2026 run-rate check: H1 2026 revenue EUR 9.31bn, Q3 2026 guide ~EUR 5.0bn. "
     "The placeholder build is deliberately simple; the model only needs a revenue line to turn the DM % into EUR.")

section(wi, 44, "E. Gross margin EXCLUDING Discovery Mode, forecast (input; replace with your model's ex-DM margin path)")
put(wi, 45, 1, "Gross margin ex-DM", TXT); put(wi, 45, 2, "% of revenue", NOTE)
for y, v in zip(FC, [0.326, 0.331, 0.336, 0.341, 0.346]):
    put(wi, 45, COL[y], v, INP, "0.0%", RIGHT, KEYFILL)
GM_EX_ROW = 45
note(wi, 46, "History ex-DM is derived on the Revenue & GM sheet (reported margin less the DM contribution). Forecast defaults add +50bp a year to the FY2025 ex-DM base, "
     "so reported margin lands near the bottom of the 35-40% FY2030 target range (Investor Day, 21 May 2026). Everything above DM in the margin stack (price, mix, "
     "audiobooks, podcasts, bundle mechanicals, Marquee) belongs here.")
wi.freeze_panes = "C7"

# =============================================================================
# REVENUE & GM  (built before DM build so DM build can link revenue; references are by address so order is cosmetic)
# =============================================================================
wr = wb.create_sheet("Revenue & GM")
widths(wr, [62, 14] + [11] * 10)
put(wr, 1, 1, "Revenue build and gross margin bridge (selected scenario)", TITLE)
put(wr, 2, 1, "Green = link to another sheet; black = formula. Reported gross margin = margin ex-DM + Discovery Mode contribution.", NOTE)
year_header(wr, 4)

section(wr, 5, "Revenue")
put(wr, 6, 1, "Premium subscribers, year end", TXT); put(wr, 6, 2, "m", NOTE)
for y in YEARS:
    put(wr, 6, COL[y], f"=Inputs!{COL[y]}33", LNK, "#,##0", RIGHT)
put(wr, 7, 1, "Average subscribers", TXT); put(wr, 7, 2, "m", NOTE)
for y in YEARS[1:]:
    put(wr, 7, COL[y], f"=({COL[y - 1]}6+{COL[y]}6)/2", FML, "#,##0.0", RIGHT)
put(wr, 8, 1, "Premium ARPU (monthly)", TXT); put(wr, 8, 2, "EUR", NOTE)
for y in YEARS:
    put(wr, 8, COL[y], f"=Inputs!{COL[y]}35", LNK, "0.00", RIGHT)
put(wr, 9, 1, "Premium revenue", TXT); put(wr, 9, 2, "EUR m", NOTE)
for y in HIST:
    put(wr, 9, COL[y], f"=Inputs!{COL[y]}37", LNK, "#,##0", RIGHT)
for y in FC:
    put(wr, 9, COL[y], f"={COL[y]}7*{COL[y]}8*12", FML, "#,##0", RIGHT)
put(wr, 10, 1, "Ad-Supported revenue", TXT); put(wr, 10, 2, "EUR m", NOTE)
for y in HIST:
    put(wr, 10, COL[y], f"=Inputs!{COL[y]}38", LNK, "#,##0", RIGHT)
for y in FC:
    put(wr, 10, COL[y], f"={COL[y - 1]}10*(1+Inputs!{COL[y]}39)", FML, "#,##0", RIGHT)
put(wr, 11, 1, "Total revenue, placeholder build", TXT); put(wr, 11, 2, "EUR m", NOTE)
for y in YEARS:
    put(wr, 11, COL[y], f"={COL[y]}9+{COL[y]}10", FML, "#,##0", RIGHT)
put(wr, 12, 1, "Total revenue override (from Inputs row 40)", TXT); put(wr, 12, 2, "EUR m", NOTE)
for y in FC:
    put(wr, 12, COL[y], f'=IF(Inputs!{COL[y]}40="","",Inputs!{COL[y]}40)', LNK, "#,##0", RIGHT)
put(wr, 13, 1, "Total revenue USED", BOLD); put(wr, 13, 2, "EUR m", NOTE)
for y in HIST:
    put(wr, 13, COL[y], f"={COL[y]}11", FMLB, "#,##0", RIGHT, border=TOPLINE)
for y in FC:
    put(wr, 13, COL[y], f'=IF({COL[y]}12="",{COL[y]}11,{COL[y]}12)', FMLB, "#,##0", RIGHT, border=TOPLINE)
REV_USED = 13
put(wr, 14, 1, "  growth", TXT); put(wr, 14, 2, "%", NOTE)
for y in YEARS[1:]:
    put(wr, 14, COL[y], f"={COL[y]}13/{COL[y - 1]}13-1", FML, "0.0%", RIGHT)

section(wr, 16, "Reported cost base (history)")
put(wr, 17, 1, "Cost of revenue, reported", TXT); put(wr, 17, 2, "EUR m", NOTE)
for y in HIST:
    put(wr, 17, COL[y], f"=Inputs!{COL[y]}41", LNK, "#,##0", RIGHT)
put(wr, 18, 1, "Gross profit, reported", TXT); put(wr, 18, 2, "EUR m", NOTE)
for y in HIST:
    put(wr, 18, COL[y], f"={COL[y]}13-{COL[y]}17", FML, "#,##0", RIGHT)
put(wr, 19, 1, "Gross margin, reported", TXT); put(wr, 19, 2, "%", NOTE)
for y in HIST:
    put(wr, 19, COL[y], f"={COL[y]}18/{COL[y]}13", FML, "0.0%", RIGHT)

section(wr, 21, "Gross margin bridge")
put(wr, 22, 1, "Discovery Mode contribution (selected scenario)", TXT); put(wr, 22, 2, "% of revenue", NOTE)
DMC_ROW = 22   # filled after DM build rows are known
put(wr, 23, 1, "Gross margin ex-Discovery Mode", TXT); put(wr, 23, 2, "%", NOTE)
for y in HIST:
    put(wr, 23, COL[y], f"={COL[y]}19-{COL[y]}22", FML, "0.0%", RIGHT)
for y in FC:
    put(wr, 23, COL[y], f"=Inputs!{COL[y]}{GM_EX_ROW}", LNK, "0.0%", RIGHT)
put(wr, 24, 1, "Gross margin (reported history / forecast)", BOLD); put(wr, 24, 2, "%", NOTE)
for y in HIST:
    put(wr, 24, COL[y], f"={COL[y]}19", FMLB, "0.0%", RIGHT, border=TOPLINE)
for y in FC:
    put(wr, 24, COL[y], f"={COL[y]}23+{COL[y]}22", FMLB, "0.0%", RIGHT, border=TOPLINE)
GM_ROW = 24
put(wr, 25, 1, "Gross profit", TXT); put(wr, 25, 2, "EUR m", NOTE)
for y in HIST:
    put(wr, 25, COL[y], f"={COL[y]}18", FML, "#,##0", RIGHT)
for y in FC:
    put(wr, 25, COL[y], f"={COL[y]}13*{COL[y]}24", FML, "#,##0", RIGHT)
put(wr, 26, 1, "Cost of revenue", TXT); put(wr, 26, 2, "EUR m", NOTE)
for y in HIST:
    put(wr, 26, COL[y], f"={COL[y]}17", FML, "#,##0", RIGHT)
for y in FC:
    put(wr, 26, COL[y], f"={COL[y]}13-{COL[y]}25", FML, "#,##0", RIGHT)
put(wr, 27, 1, "  of which Discovery Mode commission retained (gross profit from DM)", TXT); put(wr, 27, 2, "EUR m", NOTE)
for y in YEARS:
    put(wr, 27, COL[y], f"={COL[y]}22*{COL[y]}13", FML, "#,##0", RIGHT)
put(wr, 28, 1, "  Discovery Mode contribution", TXT); put(wr, 28, 2, "bp of GM", NOTE)
for y in YEARS:
    put(wr, 28, COL[y], f"={COL[y]}22*10000", FML, "0", RIGHT)
put(wr, 29, 1, "  Change in DM contribution, y/y", TXT); put(wr, 29, 2, "bp", NOTE)
for y in YEARS[1:]:
    put(wr, 29, COL[y], f"={COL[y]}28-{COL[y - 1]}28", FML, "+0;-0;0", RIGHT)

section(wr, 31, "History check: how much of the FY2021-FY2025 margin expansion can Discovery Mode explain?")
put(wr, 32, 1, "Reported gross margin expansion FY2021 -> FY2025", TXT); put(wr, 32, 2, "bp", NOTE)
put(wr, 32, 3, "=(G24-C24)*10000", FML, "0", RIGHT)
put(wr, 33, 1, "Discovery Mode contribution change FY2021 -> FY2025", TXT); put(wr, 33, 2, "bp", NOTE)
put(wr, 33, 3, "=G28-C28", FML, "0", RIGHT)
put(wr, 34, 1, "Share of the expansion explained by Discovery Mode", TXT); put(wr, 34, 2, "%", NOTE)
put(wr, 34, 3, "=C33/C32", FML, "0%", RIGHT)
put(wr, 35, 1, "Cross-check: Investor Day 2026 said 'about a third of the gross margin expansion came from the music business' (music = price/mix, marketplace incl. DM, bundle mechanicals).", NOTE)
put(wr, 36, 1, "Share of the music-driven third explained by Discovery Mode", TXT); put(wr, 36, 2, "%", NOTE)
put(wr, 36, 3, "=C34/(1/3)", FML, "0%", RIGHT)

section(wr, 38, "FY2030 check against management targets")
put(wr, 39, 1, "FY2030 gross margin, this model (selected scenario + your ex-DM path)", TXT); put(wr, 39, 2, "%", NOTE)
put(wr, 39, 3, "=L24", FML, "0.0%", RIGHT)
put(wr, 40, 1, "Investor Day 21 May 2026 target range, FY2030", TXT); put(wr, 40, 2, "%", NOTE)
put(wr, 40, 3, 0.35, INP, "0%", RIGHT); put(wr, 40, 4, 0.40, INP, "0%", RIGHT)
wr.freeze_panes = "C5"

# =============================================================================
# DM BUILD
# =============================================================================
wd = wb.create_sheet("DM build")
widths(wd, [62, 16] + [11] * 10)
put(wd, 1, 1, "Discovery Mode gross margin build, all three scenarios", TITLE)
put(wd, 2, 1, "DM saving as % of revenue = s_ctx x s_dm x d x r_rec x m. Spotify retains the commission (20-F: cost of revenue 'reflects discounts provided by certain rights holders in return for promotional activities in connection with marketplace programs').", NOTE)
year_header(wd, 4)

BLOCK = {}


def dm_block(r0, name, ctx_ref, dm_ref, d_ref):
    """ctx_ref etc. are functions year -> formula string."""
    section(wd, r0, f"{name} scenario")
    put(wd, r0 + 1, 1, "DM-eligible context share of music streams (s_ctx)", TXT); put(wd, r0 + 1, 2, "% of music streams", NOTE)
    put(wd, r0 + 2, 1, "DM-enrolled share of context streams (s_dm)", TXT); put(wd, r0 + 2, 2, "% of context streams", NOTE)
    put(wd, r0 + 3, 1, "Discovery Mode streams as % of all music streams", TXT); put(wd, r0 + 3, 2, "% of music streams", NOTE)
    put(wd, r0 + 4, 1, "Commission on recording royalties (d)", TXT); put(wd, r0 + 4, 2, "% of royalty", NOTE)
    put(wd, r0 + 5, 1, "Recording royalties % of music revenue (r_rec) x music share of revenue (m)", TXT); put(wd, r0 + 5, 2, "% of total rev", NOTE)
    put(wd, r0 + 6, 1, "DM saving as % of total revenue", BOLD); put(wd, r0 + 6, 2, "% of total rev", NOTE)
    put(wd, r0 + 7, 1, "Total revenue used", TXT); put(wd, r0 + 7, 2, "EUR m", NOTE)
    put(wd, r0 + 8, 1, "Discovery Mode gross profit", BOLD); put(wd, r0 + 8, 2, "EUR m", NOTE)
    put(wd, r0 + 9, 1, "Gross margin contribution", BOLD); put(wd, r0 + 9, 2, "bp", NOTE)
    put(wd, r0 + 10, 1, "  change y/y", TXT); put(wd, r0 + 10, 2, "bp", NOTE)
    for y in YEARS:
        c = COL[y]
        put(wd, r0 + 1, c, ctx_ref(y), LNK, "0.0%", RIGHT)
        put(wd, r0 + 2, c, dm_ref(y), LNK, "0.0%", RIGHT)
        put(wd, r0 + 3, c, f"={c}{r0 + 1}*{c}{r0 + 2}", FML, "0.00%", RIGHT)
        put(wd, r0 + 4, c, d_ref(y), LNK, "0.0%", RIGHT)
        put(wd, r0 + 5, c, f"={R_REC}*{M_SHARE}", LNK, "0.0%", RIGHT)
        put(wd, r0 + 6, c, f"={c}{r0 + 3}*{c}{r0 + 4}*{c}{r0 + 5}", FMLB, "0.00%", RIGHT, border=TOPLINE)
        put(wd, r0 + 7, c, f"='Revenue & GM'!{c}{REV_USED}", LNK, "#,##0", RIGHT)
        put(wd, r0 + 8, c, f"={c}{r0 + 6}*{c}{r0 + 7}", FMLB, "#,##0", RIGHT)
        put(wd, r0 + 9, c, f"={c}{r0 + 6}*10000", FMLB, "0", RIGHT)
        if y > YEARS[0]:
            put(wd, r0 + 10, c, f"={c}{r0 + 9}-{COL[y - 1]}{r0 + 9}", FML, "+0;-0;0", RIGHT)
    BLOCK[name] = {"ctx": r0 + 1, "dm": r0 + 2, "share": r0 + 3, "d": r0 + 4, "pct": r0 + 6, "eur": r0 + 8, "bp": r0 + 9}


for i, name in enumerate(["Bear", "Base", "Bull"]):
    r0 = 6 + i * 13
    dm_block(r0, name,
             lambda y, n=name: f"=Inputs!{COL[y]}{CTX_ROW[n]}",
             lambda y, n=name: f"=Inputs!{COL[y]}{DM_ROW[n]}",
             lambda y, n=name: f"=Inputs!{COL[y]}{D_ROW[n]}")
r0 = 6 + 3 * 13
dm_block(r0, "Selected",
         lambda y: f"=Inputs!{COL[y]}{CTX_SEL}",
         lambda y: f"=Inputs!{COL[y]}{DM_SEL}",
         lambda y: f"=Inputs!{COL[y]}{D_SEL}")
put(wd, r0, 1, "Selected scenario (feeds Revenue & GM)", H2)
put(wd, r0, 3, f'=CHOOSE({SEL},"Bear","Base","Bull")', FMLB)
wd.freeze_panes = "C5"

# Now fill the DM contribution row on Revenue & GM from the Selected block.
for y in YEARS:
    put(wr, DMC_ROW, COL[y], f"='DM build'!{COL[y]}{BLOCK['Selected']['pct']}", LNK, "0.00%", RIGHT)

# =============================================================================
# TRIANGULATION
# =============================================================================
wt = wb.create_sheet("Triangulation")
widths(wt, [34, 12, 46, 40, 11, 11, 11])
put(wt, 1, 1, "Triangulating the two unknowns: s_ctx (context share) and s_dm (DM share of context)", TITLE)
put(wt, 2, 1, "Spotify has never disclosed either figure. Every row below is a public data point and what it bounds; the selection at the bottom of each section feeds Inputs.", NOTE)

section(wt, 4, "A. What share of music streams happens in Discovery Mode contexts (Radio, Autoplay, Mixes)?")
hdr = ["Source", "Date", "Figure (as published)", "Scope and what it implies for DM contexts", "Implied low", "Implied high", "Weight"]
for i, h in enumerate(hdr, 1):
    put(wt, 5, i, h, HDR, align=WRAP, fill=HFILL)
ev = [
    ("Spotify F-1 prospectus", "Feb 2018", "'We now program approximately 31% of all listening on Spotify across these and other playlists, compared to less than 20% two years ago.'",
     "All listening; editorial + algorithmic playlists. DM contexts are a subset of programmed listening, so 31% is a ceiling for all programmed, not a DM-context estimate.", 0.08, 0.20, "Bound"),
    ("Spotify for Artists, 'Made to Be Found'", "26 Jan 2022", "'The majority of streams' come from active sessions; 'more than half of new artist discoveries happen in programmed playlists - with over a quarter coming from Spotify Mixes, Radio, and Autoplay.'",
     "Programmed streams < 50%. The 'over a quarter' is a share of discoveries, which skew to algorithmic contexts, so the stream share of Mixes/Radio/Autoplay is below 25%.", 0.08, 0.22, "Bound"),
    ("Your Music Marketing sample, via Music Ally", "Feb 2024", "25.3bn streams, several hundred artists: 18.7% of streams from 'algorithmic playlists and mixes' (radio, Daily Mix, Discover Weekly, Release Radar, On Repeat, Repeat Rewind); 'just over 21%' in the last 12 months.",
     "Includes Discover Weekly / Release Radar / On Repeat (not DM contexts); Autoplay treatment unspecified. Stripping the non-DM playlists and adding Autoplay lands around 10-16%. Sample skews to marketed artists.", 0.10, 0.16, "Primary"),
    ("Anderson et al. (Spotify Research) WWW 2020; Bello & Garcia 2021", "2020-21", "'According to Spotify, up to one-fifth of their streams can be attributed to algorithmic recommendations.'",
     "All algorithmic recommendations, c.2019-20, before Mixes were DM contexts. Upper bound ~20% for everything algorithmic at that time.", 0.08, 0.20, "Bound"),
    ("r/musicmarketing corpus (this project)", "2023-26", "DM-context streams as % of enrolled artists' monthly streams: 3.5%, 3.9%, 4.0%, 5.0% (artists with 500k+ monthly streams); 10%; 33%; 33%; 50% (catalog-heavy, best month). Median 7.5%, n = 8.",
     "Indie artists only. Understated where only some songs are enrolled; overstated by the DM boost. Suggests big indie acts sit in single digits while catalog-heavy acts can be a third.", 0.04, 0.33, "Cross-check"),
    ("Spotify for Artists, Campaign Kit blog", "2024-25", "'In 2024, 35% of all discoveries ... [happened] in algorithmic contexts'; '16 billion artist discoveries every month, a third via algorithmic contexts' (2020).",
     "Discoveries, not streams. Confirms algorithmic contexts are growing in importance but gives no stream share.", None, None, "Context"),
]
for i, row in enumerate(ev):
    r = 6 + i
    for j, v in enumerate(row, 1):
        put(wt, r, j, v, INP if j in (5, 6) else TXT, "0%" if j in (5, 6) else None, WRAP if j in (1, 3, 4) else RIGHT if j in (5, 6) else None)
    wt.row_dimensions[r].height = 78
EV1 = 6 + len(ev) - 1
r = EV1 + 2
put(wt, r, 1, "Full span of the evidence rows above", TXT)
put(wt, r, 5, f"=MIN(E6:E{EV1})", FML, "0%", RIGHT)
put(wt, r, 6, f"=MAX(F6:F{EV1})", FML, "0%", RIGHT)
r += 1
put(wt, r, 1, "Bound and primary rows only (excludes the indie-only Reddit cross-check)", TXT)
put(wt, r, 5, "=MAX(E6:E9)", FML, "0%", RIGHT)
put(wt, r, 6, "=MIN(F6:F9)", FML, "0%", RIGHT)
r += 1
put(wt, r, 1, "Primary-source midpoint (Y2M sample, adjusted to DM contexts)", TXT)
put(wt, r, 5, "=AVERAGE(E8:F8)", FML, "0.0%", RIGHT)
r += 1
put(wt, r, 1, "Bookends used for Bear / Bull (FY2025)", TXT)
put(wt, r, 5, 0.09, INP, "0%", RIGHT); put(wt, r, 6, 0.20, INP, "0%", RIGHT)
r += 1
put(wt, r, 1, "Selected FY2025 base case (feeds Inputs row 13)", BOLD)
put(wt, r, 5, "=Inputs!G13", LNK, "0.0%", RIGHT)
put(wt, r, 6, "Low 9% / high 20% are the Bear-Bull bookends; before Mixes joined (Jan 2024) only Radio + Autoplay counted, modelled at 9-9.5%.", NOTE)
r += 2

section(wt, r, "B. What share of DM-context streams is Discovery Mode-enrolled? (cross-check on the 33% assumption)")
r += 1
put(wt, r, 1, "Logic: enrolled catalog starts with its natural share of context streams (e) and gets boosted b-fold by the DM signal inside a fixed inventory: s_dm = e*b / (e*b + (1 - e)).", NOTE)
wt.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
r += 1
TB0 = r
rows_b = [
    ("Streams from rights holders outside UMG, Sony, WMG and Merlin (FY2025 20-F: the four = ~72%)", 0.28, "0%", "20-F FY2025. These DIY distributors and non-Merlin indies are the catalog Discovery Mode is sold to today."),
    ("Share of that catalog enrolled, weighted by context streams", 0.45, "0%", "Assumption. Self-serve needs 25k+ monthly listeners and 3+ eligible songs; Believe says it moves 'hundreds of thousands of tracks every month' in and out."),
    ("Add-on: Merlin members and other labels enrolling via Spotify's partnerships team", 0.02, "0.0%", "Assumption (share of context streams). Majors have not opted in as far as public reporting shows."),
    ("Natural context share of enrolled catalog, e", None, "0.0%", "row 1 x row 2 + row 3"),
    ("In-context boost from the DM signal, b (campaign lift + 1)", 3.14, "0.00", "Median Spotify-reported lift across 13 artist screenshots was +214% (discovery_mode_efficacy.xlsx). 2023-24 campaigns: +406%; 2025-26: +78%."),
    ("Implied s_dm = e*b / (e*b + 1 - e)", None, "0.0%", "Compare with the 33% assumption in Inputs row 20."),
]
for i, (lab, val, fmt, src) in enumerate(rows_b):
    rr = TB0 + i
    put(wt, rr, 1, lab, TXT, align=WRAP)
    wt.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=3)
    if val is not None:
        put(wt, rr, 5, val, INP, fmt, RIGHT)
    put(wt, rr, 4, src, NOTE, align=WRAP)
    wt.row_dimensions[rr].height = 40
put(wt, TB0 + 3, 5, f"=E{TB0}*E{TB0 + 1}+E{TB0 + 2}", FML, "0.0%", RIGHT)
put(wt, TB0 + 5, 5, f"=E{TB0 + 3}*E{TB0 + 4}/(E{TB0 + 3}*E{TB0 + 4}+1-E{TB0 + 3})", FMLB, "0.0%", RIGHT)
E_ROW, B_ROW = TB0 + 3, TB0 + 4
r = TB0 + 7
put(wt, r, 1, "Sensitivity of implied s_dm to enrollment and the boost (what the 'ceiling' question turns on)", BOLD)
r += 1
put(wt, r, 1, "Natural context share of enrolled catalog, e  ↓   |   boost b  →", HDR, fill=HFILL)
bvals = [1.5, 1.78, 2.0, 2.5, 3.14, 4.0]
for j, b in enumerate(bvals):
    put(wt, r, 2 + j, b, INP, "0.00", RIGHT, HFILL)
SENSB = r
evals = [0.10, 0.14, 0.17, 0.20, 0.25, 0.30]
for i, e in enumerate(evals):
    rr = SENSB + 1 + i
    put(wt, rr, 1, e, INP, "0%", RIGHT)
    for j in range(len(bvals)):
        c = get_column_letter(2 + j)
        put(wt, rr, 2 + j, f"=$A{rr}*{c}${SENSB}/($A{rr}*{c}${SENSB}+1-$A{rr})", FML, "0%", RIGHT)
r = SENSB + 1 + len(evals)
note(wt, r, "Reading: with ~28% of streams outside the majors and Merlin, e cannot exceed ~30% unless a major opts in, which caps s_dm near 45-57% even at a 2-3x boost. "
     "If the per-track boost has faded to the 2025-26 level (b ~1.8), holding 33% needs enrollment closer to 70% of eligible catalog. That is the mechanism behind the Bear case.", 7)
r += 2

section(wt, r, "C. Sanity bound from Spotify's Marketplace disclosures")
r += 1
TC0 = r
rows_c = [
    ("Marketplace gross profit contribution, FY2021 (Investor Day, 8 Jun 2022: 'more than EUR 160m')", 160, "#,##0", "EUR m. Marketplace = Marquee, Showcase, Discovery Mode and related tools."),
    ("Multiple cited at Investor Day 21 May 2026 (third-party recap: 'about 4x 2021')", 4, "0.0x", "Not an official EUR figure; treat as order of magnitude."),
    ("Implied Marketplace gross profit, FY2025", None, "#,##0", "row 1 x row 2"),
    ("Discovery Mode gross profit FY2025, this model (Base)", None, "#,##0", "From DM build"),
    ("DM as share of implied Marketplace gross profit", None, "0%", "The rest is Marquee/Showcase advertising. Anything above ~50% would strain the 2021 base, where Marquee was the bulk."),
    ("Upper bound on s_ctx x s_dm if DM were ALL of Marketplace gross profit", None, "0.0%", "row 3 / (FY2025 revenue x d x r_rec x m). The model's FY2025 product is shown next to it."),
]
for i, (lab, val, fmt, src) in enumerate(rows_c):
    rr = TC0 + i
    put(wt, rr, 1, lab, TXT, align=WRAP)
    wt.merge_cells(start_row=rr, start_column=1, end_row=rr, end_column=3)
    if val is not None:
        put(wt, rr, 5, val, INP, fmt, RIGHT)
    put(wt, rr, 4, src, NOTE, align=WRAP)
    wt.row_dimensions[rr].height = 40
put(wt, TC0 + 2, 5, f"=E{TC0}*E{TC0 + 1}", FML, "#,##0", RIGHT)
put(wt, TC0 + 3, 5, f"='DM build'!G{BLOCK['Base']['eur']}", LNK, "#,##0", RIGHT)
put(wt, TC0 + 4, 5, f"=E{TC0 + 3}/E{TC0 + 2}", FML, "0%", RIGHT)
put(wt, TC0 + 5, 5, f"=E{TC0 + 2}/('Revenue & GM'!G{REV_USED}*Inputs!G27*{R_REC}*{M_SHARE})", FML, "0.0%", RIGHT)
put(wt, TC0 + 5, 6, f"='DM build'!G{BLOCK['Base']['share']}", LNK, "0.0%", RIGHT)
put(wt, TC0 + 5, 7, "model FY2025", NOTE)

# =============================================================================
# FINANCIALS (reported data)
# =============================================================================
wf = wb.create_sheet("Financials")
widths(wf, [44, 12, 12, 12, 12, 12, 60])
put(wf, 1, 1, "Spotify reported financials used in the model (EUR m unless stated)", TITLE)
put(wf, 2, 1, "Blue = as reported in 20-F / shareholder letters. Figures marked (v) were derived from disclosed items or search renderings and should be re-checked against the filing tables before external use.", NOTE)
hdrs = ["Annual", "FY2021", "FY2022", "FY2023", "FY2024", "FY2025", "Source / note"]
for i, h in enumerate(hdrs, 1):
    put(wf, 4, i, h, HDR, align=RIGHT if 1 < i < 7 else None, fill=HFILL)
fin = [
    ("Total revenue", [9668, 11727, 13247, 15673, 17186], "#,##0", "20-F FY2021-FY2025 [S1-S4]"),
    ("  Premium revenue", [8460, 10251, 11566, 13819, 15350], "#,##0", "20-F; FY2024 (v)"),
    ("  Ad-Supported revenue", [1208, 1476, 1681, 1854, 1836], "#,##0", "20-F; FY2024 (v)"),
    ("Cost of revenue", [7077, 8801, 9849, 10955, 11690], "#,##0", "20-F; FY2023-24 derived from reported gross margin (v)"),
    ("Gross profit", ["=B5-B8", "=C5-C8", "=D5-D8", "=E5-E8", "=F5-F8"], "#,##0", "formula"),
    ("Gross margin", ["=B9/B5", "=C9/C5", "=D9/D5", "=E9/E5", "=F9/F5"], "0.0%", "formula; reported: 26.8%, 25.0%, 25.6%, 30.1%, 32.0%"),
    ("  Premium gross margin", [0.29, 0.28, 0.288, 0.325, 0.337], "0.0%", "20-F; FY2021-22 approx (v)"),
    ("  Ad-Supported gross margin", [0.109, None, 0.037, 0.124, 0.18], "0.0%", "20-F; FY2022 not captured"),
    ("Premium subscribers, year end (m)", [180, 205, 236, 263, 290], "#,##0", "shareholder letters"),
    ("Monthly active users, year end (m)", [406, 489, 602, 675, 751], "#,##0", "shareholder letters"),
    ("Premium ARPU, monthly (EUR)", [4.29, 4.52, 4.39, 4.69, 4.63], "0.00", "shareholder letters; FY2025: FX -0.17, mix -0.14, price +0.25"),
    ("Streams from UMG, Sony, WMG and Merlin (share)", [None, 0.75, 0.74, 0.71, 0.72], "0%", "20-F risk factors; FY2022 via Music Ally"),
]
for i, (lab, vals, fmt, src) in enumerate(fin):
    r = 5 + i
    put(wf, r, 1, lab, TXT)
    for j, v in enumerate(vals):
        if v is None:
            continue
        put(wf, r, 2 + j, v, FML if isinstance(v, str) else INP, fmt, RIGHT)
    put(wf, r, 7, src, NOTE)
r = 5 + len(fin) + 1
put(wf, r, 1, "Quarterly (latest)", H2)
r += 1
qh = ["Quarter", "Revenue", "Gross margin", "Premium GM", "Ad GM", "Subs (m)", "Source / note"]
for i, h in enumerate(qh, 1):
    put(wf, r, i, h, HDR, align=RIGHT if 1 < i < 7 else None, fill=HFILL)
qs = [
    ("Q1 2025", 4190, 0.316, None, None, None, "6-K, 29 Apr 2025"),
    ("Q2 2025", 4190, 0.315, None, None, None, "6-K, 29 Jul 2025"),
    ("Q3 2025", 4270, 0.316, 0.332, 0.184, 281, "6-K, 4 Nov 2025"),
    ("Q4 2025", 4530, 0.331, None, None, 290, "deck, 10 Feb 2026; 'content cost favorability'"),
    ("Q1 2026", 4530, 0.330, 0.348, 0.13, 293, "6-K, 28 Apr 2026"),
    ("Q2 2026", 4780, 0.334, 0.349, 0.191, 300, "6-K, Aug 2026; ARPU EUR 4.89 (+7.4% cc)"),
    ("Q3 2026 guide", 5000, 0.329, None, None, None, "Q2 2026 letter guidance"),
]
for i, (q, rev, gm, pgm, agm, subs, src) in enumerate(qs):
    rr = r + 1 + i
    put(wf, rr, 1, q, TXT)
    put(wf, rr, 2, rev, INP, "#,##0", RIGHT)
    put(wf, rr, 3, gm, INP, "0.0%", RIGHT)
    if pgm is not None:
        put(wf, rr, 4, pgm, INP, "0.0%", RIGHT)
    if agm is not None:
        put(wf, rr, 5, agm, INP, "0.0%", RIGHT)
    if subs is not None:
        put(wf, rr, 6, subs, INP, "#,##0", RIGHT)
    put(wf, rr, 7, src, NOTE)
r = r + 1 + len(qs) + 1
put(wf, r, 1, "Management statements that anchor the mechanism", H2)
for i, s in enumerate([
    "20-F FY2024 and FY2025: cost of revenue 'also reflects discounts provided by certain rights holders in return for promotional activities in connection with marketplace programs'.",
    "20-F FY2025: Premium cost of revenue rose on 'increased rates for certain licensors ... partially offset by benefits from certain marketplace programs'.",
    "Q2 2024 call (Ben Kung): gross margin 'outperformance was driven primarily by music content cost favorability and marketplace'.",
    "Investor Day 8 Jun 2022: Marketplace gross profit 'more than EUR 160m' in 2021 (8x 2018); Discovery Mode revenue +224% y/y with 'over 50 labels and distributors'; marketplace 'the primary factor in growing our music gross margins'.",
    "Investor Day 21 May 2026: FY2030 targets of 35-40% gross margin and >20% operating margin; 'about a third of the gross margin expansion came from the music business'; Marketplace gross profit about 4x 2021 (third-party recap).",
    "MIDiA (2025): 'When a label uses Discovery Mode, Spotify gets an extra 17% of gross margin' on those streams, i.e. the 30% commission on a ~56% recording share.",
]):
    put(wf, r + 1 + i, 1, s, TXT, align=WRAP)
    wf.merge_cells(start_row=r + 1 + i, start_column=1, end_row=r + 1 + i, end_column=7)
    wf.row_dimensions[r + 1 + i].height = 30

# =============================================================================
# SOURCES
# =============================================================================
wsrc = wb.create_sheet("Sources")
widths(wsrc, [6, 70, 90])
put(wsrc, 1, 1, "Sources", TITLE)
put(wsrc, 2, 1, "Collected 2 Oct 2026. Primary documents were read through search-engine renderings because the research environment could not fetch sec.gov and spotify.com directly; re-open before quoting externally.", NOTE)
sources = [
    ("S1", "Spotify 20-F FY2025", "https://www.sec.gov/Archives/edgar/data/1639920/000162828026006874/ck0001639920-20251231.htm"),
    ("S2", "Spotify 20-F FY2024", "https://www.sec.gov/Archives/edgar/data/1639920/000163992025000003/ck0001639920-20241231.htm"),
    ("S3", "Spotify 20-F FY2023", "https://www.sec.gov/Archives/edgar/data/1639920/000163992024000004/ck0001639920-20231231.htm"),
    ("S4", "Spotify 20-F FY2022", "https://www.sec.gov/Archives/edgar/data/1639920/000163992023000004/ck0001639920-20221231.htm"),
    ("S5", "Q4 2025 shareholder letter (6-K)", "https://www.sec.gov/Archives/edgar/data/1639920/000114036126004482/ef20065075_ex99-1.htm"),
    ("S6", "Q1 2026 shareholder letter (6-K)", "https://www.sec.gov/Archives/edgar/data/0001639920/000114036126017211/ef20071303_ex99-1.htm"),
    ("S7", "Q2 2026 shareholder letter (6-K)", "https://www.sec.gov/Archives/edgar/data/0001639920/000114036126031044/ef20078867_ex99-1.htm"),
    ("S8", "Q3 2025 shareholder letter (6-K)", "https://www.sec.gov/Archives/edgar/data/1639920/000114036125040271/ef20057592_ex99-1.htm"),
    ("S9", "Q4 2025 shareholder deck", "https://s29.q4cdn.com/175625835/files/doc_financials/2025/q4/Q4-2025-Shareholder-Deck-FINAL.pdf"),
    ("S10", "Q2 2024 earnings call prepared remarks", "https://s29.q4cdn.com/175625835/files/doc_financials/2024/q2/Q2-24-Earnings-Call-Prepared-Remarks.pdf"),
    ("S11", "Investor Day 2022 transcript (8 Jun 2022)", "https://s29.q4cdn.com/175625835/files/doc_presentation/SPOTIFY-2022-INVESTOR-DAY-TRANSCRIPT.pdf"),
    ("S12", "Investor Day 2026 recap (21 May 2026)", "https://newsroom.spotify.com/2026-05-21/investor-day-recap/"),
    ("S13", "Investor Day 2026 third-party notes (Marketplace ~4x 2021)", "https://mbideepdives.substack.com/p/some-notes-from-spotifys-2026-investor"),
    ("S14", "Q4 2025 earnings call transcript", "https://www.fool.com/earnings/call-transcripts/2026/02/10/spotify-spot-q4-2025-earnings-transcript/"),
    ("S15", "Spotify F-1 prospectus (Feb 2018): ~31% of listening programmed", "https://www.sec.gov/Archives/edgar/data/0001639920/000119312518063434/d494294df1.htm"),
    ("S16", "Spotify newsroom, Discovery Mode launch (2 Nov 2020)", "https://newsroom.spotify.com/2020-11-02/amplifying-artist-input-in-your-personalized-recommendations/"),
    ("S17", "Q1 2021 shareholder letter: 'promotional recording royalty rate'", "https://www.sec.gov/Archives/edgar/data/1639920/000119312521135262/d162701dex991.htm"),
    ("S18", "Q2 2021 shareholder letter: test with majors, indies, distributors", "https://www.sec.gov/Archives/edgar/data/1639920/000119312521226476/d206900dex991.htm"),
    ("S19", "Spotify for Artists: Using Discovery Mode (30% commission, eligibility)", "https://support.spotify.com/us/artists/article/using-discovery-mode-in-spotify-for-artists/"),
    ("S20", "Spotify for Artists: Discovery Mode contexts (Radio, Autoplay, Mixes)", "https://support.spotify.com/us/artists/article/discovery-mode-contexts/"),
    ("S21", "Spotify for Artists: Getting access to Discovery Mode (participating licensors)", "https://support.spotify.com/us/artists/article/getting-access-to-discovery-mode/"),
    ("S22", "Spotify for Artists: Discovery Mode product page", "https://artists.spotify.com/discovery-mode"),
    ("S23", "Spotify for Artists: Campaign Kit (Mixes join DM from 3 Jan 2024)", "https://artists.spotify.com/blog/introducing-campaign-kit-campaign-tools-made-for-music"),
    ("S24", "Spotify for Artists: Source of streams taxonomy", "https://support.spotify.com/us/artists/article/source-of-streams/"),
    ("S25", "Spotify for Artists: 'Made to Be Found' (26 Jan 2022)", "https://artists.spotify.com/en/blog/how-fans-discover-music-on-spotify-playlists-made-to-be-found"),
    ("S26", "Music Ally on 'Made to Be Found'", "https://musically.com/2022/01/26/spotify-majority-streams-active-listening/"),
    ("S27", "Music Ally on Your Music Marketing stream-source study (Feb 2024)", "https://musically.com/2024/02/23/report-explores-how-spotify-algorithms-affect-music-listening/"),
    ("S28", "Anderson et al., Algorithmic effects on diversity of consumption on Spotify (WWW 2020)", "https://www.cs.toronto.edu/~ashton/pubs/alg-effects-spotify-www2020.pdf"),
    ("S29", "Bello & Garcia (2021): 'up to one-fifth of streams' algorithmic", "https://www.nature.com/articles/s41599-021-00855-1"),
    ("S30", "Spotify letter to Reps. Nadler and Johnson (16 Jun 2021)", "https://democrats-judiciary.house.gov/sites/evo-subsites/democrats-judiciary.house.gov/files/migrated/UploadedFiles/Spotify_Ltr_to_Reps._Nadler_Johnson_6_16_21.pdf"),
    ("S31", "Variety: second Congressional letter on Discovery Mode (Mar 2022)", "https://variety.com/2022/music/news/congress-spotify-troubling-discovery-mode-policy-1235226722/"),
    ("S32", "Billboard: Capolongo class action over Discovery Mode (Nov 2025)", "https://www.billboard.com/pro/spotify-lawsuit-discovery-mode-modern-payola/"),
    ("S33", "EmuBands: Discovery Mode terms update (Apr 2026)", "https://www.emubands.com/spotify-discovery-mode-april-2026-update/"),
    ("S34", "MBW: Believe CEO on Discovery Mode scale (2025)", "https://www.musicbusinessworldwide.com/denis-ladegaillerie-sees-the-future-music/"),
    ("S35", "MBW: indie labels vs DIY distributors on Discovery Mode (2021)", "https://www.musicbusinessworldwide.com/indie-labels-slam-spotifys-discovery-mode-but-diy-giants-love-it/"),
    ("S36", "TuneCore: Discovery Mode commission pass-through", "https://support.tunecore.com/hc/en-us/articles/9010994114836-Spotify-Discovery-Mode"),
    ("S37", "MIDiA: Spotify profitability and Discovery Mode margin (2025)", "https://www.midiaresearch.com/blog/why-spotify-only-hit-profitability-now-but-will-do-so-again"),
    ("S38", "Variety: MIDiA per-stream split 30/56/14 (2025)", "https://variety.com/2025/digital/news/spotify-paid-4-billion-music-songwriters-struggling-1236334752/"),
    ("S39", "Loud & Clear 2026 highlights (2025 payouts; independents ~50%)", "https://newsroom.spotify.com/2026-03-11/loud-and-clear-music-economics-highlights/"),
    ("S40", "Music Ally: DIY artists ~a quarter of Spotify music streams (2022)", "https://musically.com/2023/02/03/diy-artists-now-account-for-a-quarter-of-spotifys-music-streams/"),
    ("S41", "MBW: Spotify bundling estimate (MLC suit, EUR 46m for Mar-Jun 2024)", "https://www.musicbusinessworldwide.com/spotify-estimates-that-it-would-have-to-pay-out-50m-if-the-mlc-wins-its-bundling-lawsuit/"),
    ("S42", "Billboard: bundle reclassification ~$150m less US mechanicals", "https://www.billboard.com/business/streaming/spotify-songwriters-less-mechanical-royalties-audiobooks-bundle-1235673829/"),
    ("S43", "MBW: Q2 2026, 300m Premium subscribers", "https://www.musicbusinessworldwide.com/spotify-hits-300-million-premium-subscribers-in-q2-202/"),
    ("S44", "MBW: Q1 2026 call (DJ used by 94m subscribers)", "https://www.musicbusinessworldwide.com/spotifys-co-ceos-outline-ai-ambitions-and-more-on-q1-2026-earnings-call/"),
    ("S45", "Spotify newsroom: Smart Shuffle (Mar 2023)", "https://newsroom.spotify.com/2023-03-08/smart-shuffle-new-life-spotify-playlists/"),
    ("S46", "Spotify newsroom: AI DJ (Mar 2023)", "https://newsroom.spotify.com/2023-03-08/spotify-new-personalized-ai-dj-how-it-works/"),
    ("S47", "r/musicmarketing Discovery Mode evidence (this repo)", "analysis/discovery_mode_efficacy.xlsx"),
]
for i, h in enumerate(["#", "Document", "URL"], 1):
    put(wsrc, 4, i, h, HDR, fill=HFILL)
for i, (k, d, u) in enumerate(sources):
    put(wsrc, 5 + i, 1, k, TXT)
    put(wsrc, 5 + i, 2, d, TXT)
    put(wsrc, 5 + i, 3, u, TXT)

# =============================================================================
# SUMMARY (first sheet)
# =============================================================================
ws = wb.create_sheet("Summary", 0)
widths(ws, [58, 13, 13, 13, 13, 13, 13, 13, 13, 13])
put(ws, 1, 1, "Spotify Discovery Mode: from autoplay share of streams to gross margin", TITLE)
put(ws, 2, 1, "Chain: share of music streams in DM contexts (Radio, Autoplay, Mixes)  x  share of those that are DM-enrolled  x  30% commission  x  recording royalties as % of music revenue  x  music share of revenue  =  DM saving as % of revenue. Scenario and every assumption live on Inputs.", NOTE, align=WRAP)
ws.merge_cells("A2:J2"); ws.row_dimensions[2].height = 30

put(ws, 4, 1, "Selected scenario", BOLD); put(ws, 4, 2, f'=CHOOSE({SEL},"Bear","Base","Bull")', LNK)
put(ws, 4, 4, "(change on Inputs!B4)", NOTE)

section(ws, 6, "The chain, FY2025 (Base)")
G = "G"  # FY2025 column
chain = [
    ("Share of music streams in Discovery Mode contexts (s_ctx)", f"='DM build'!{G}{BLOCK['Base']['ctx']}", "0.0%"),
    ("Share of those streams that are DM-enrolled (s_dm)", f"='DM build'!{G}{BLOCK['Base']['dm']}", "0.0%"),
    ("-> Discovery Mode streams as % of all music streams", f"='DM build'!{G}{BLOCK['Base']['share']}", "0.00%"),
    ("x Commission on recording royalties (d)", f"='DM build'!{G}{BLOCK['Base']['d']}", "0%"),
    ("x Recording royalties % of music revenue x music share of revenue", f"={R_REC}*{M_SHARE}", "0.0%"),
    ("-> Discovery Mode saving as % of total revenue", f"='DM build'!{G}{BLOCK['Base']['pct']}", "0.00%"),
    ("-> Gross margin contribution (bp)", f"='DM build'!{G}{BLOCK['Base']['bp']}", "0"),
    ("-> Discovery Mode gross profit (EUR m)", f"='DM build'!{G}{BLOCK['Base']['eur']}", "#,##0"),
]
for i, (lab, f, fmt) in enumerate(chain):
    put(ws, 7 + i, 1, lab, BOLD if lab.startswith("->") else TXT)
    put(ws, 7 + i, 2, f, LNK, fmt, RIGHT)

section(ws, 16, "Scenario outputs")
heads = ["Scenario", "FY2025A bp", "FY2030E bp", "Change bp", "FY2030E EUR m", "s_ctx FY2030", "s_dm FY2030", "d FY2030"]
for i, h in enumerate(heads, 1):
    put(ws, 17, i, h, HDR, align=RIGHT if i > 1 else None, fill=HFILL)
for i, name in enumerate(["Bear", "Base", "Bull"]):
    r = 18 + i
    b = BLOCK[name]
    put(ws, r, 1, name, BOLD)
    put(ws, r, 2, f"='DM build'!G{b['bp']}", LNK, "0", RIGHT)
    put(ws, r, 3, f"='DM build'!L{b['bp']}", LNK, "0", RIGHT)
    put(ws, r, 4, f"=C{r}-B{r}", FML, "+0;-0;0", RIGHT)
    put(ws, r, 5, f"='DM build'!L{b['eur']}", LNK, "#,##0", RIGHT)
    put(ws, r, 6, f"='DM build'!L{b['ctx']}", LNK, "0.0%", RIGHT)
    put(ws, r, 7, f"='DM build'!L{b['dm']}", LNK, "0.0%", RIGHT)
    put(ws, r, 8, f"='DM build'!L{b['d']}", LNK, "0%", RIGHT)
put(ws, 22, 1, "FY2030E reported gross margin, selected scenario on your ex-DM path", TXT)
put(ws, 22, 2, f"='Revenue & GM'!L{GM_ROW}", LNK, "0.0%", RIGHT)
put(ws, 22, 4, "Investor Day target 35-40%", NOTE)
put(ws, 23, 1, "Share of FY2021-25 reported margin expansion explained by Discovery Mode", TXT)
put(ws, 23, 2, "='Revenue & GM'!C34", LNK, "0%", RIGHT)

section(ws, 25, "What the evidence supports")
pts = [
    "1. Spotify keeps the commission. The 20-F says cost of revenue 'reflects discounts provided by certain rights holders in return for promotional activities in connection with marketplace programs', and every 2025-26 letter attributes Premium margin gains to 'music costs net of marketplace programs'. So the 30% is a gross-margin item, not a redistribution to other labels.",
    "2. The context share is the softest number. Spotify has never disclosed Radio/Autoplay/Mixes as a share of streams. Public bounds (31% of listening programmed in 2018; majority of streams active in 2022; ~19-21% algorithmic in a 25bn-stream sample; 'up to one-fifth' in Spotify research) put DM contexts at roughly 9-20% of music streams. Base 14% for FY2025, 9-9.5% before Mixes joined in 2024.",
    "3. Your 33% DM share of context streams is consistent with the catalog math: ~28% of streams sit outside UMG/Sony/WMG/Merlin, about half of that is enrolled, and enrolled tracks get a ~3x in-context boost. The same math caps s_dm near 45-57% unless a major opts in, and drops it toward ~23% if the boost has faded to the 2025-26 level.",
    "4. Discovery Mode is worth about 70bp of gross margin today on Base inputs (~EUR 120m), roughly a tenth of the FY2021-25 expansion and a third of the 'music' third management cited. FY2030 runs 45-165bp across Bear-Bull, so DM moves the 2030 margin by about +/-50bp around Base. It is a real but second-order lever next to price, mix and the 35-40% target.",
    "5. Growth in lean-back listening does not automatically flow to DM: AI DJ, Smart Shuffle and Discover Weekly are not DM contexts. The Bull case needs either a context expansion or a major label, both of which are visible events you can watch for.",
]
for i, p in enumerate(pts):
    put(ws, 26 + i, 1, p, TXT, align=WRAP)
    ws.merge_cells(start_row=26 + i, start_column=1, end_row=26 + i, end_column=10)
    ws.row_dimensions[26 + i].height = 44

section(ws, 32, "Sensitivity: FY2030 gross margin contribution (bp) to the two unknowns, at Base commission and royalty assumptions")
put(ws, 33, 1, "s_ctx (context share of music streams)  ↓   |   s_dm (DM share of context streams)  →", HDR, fill=HFILL)
sdm_vals = [0.20, 0.25, 0.30, 0.33, 0.40, 0.50, 0.60]
for j, v in enumerate(sdm_vals):
    put(ws, 33, 2 + j, v, INP, "0%", RIGHT, HFILL)
sctx_vals = [0.10, 0.12, 0.14, 0.16, 0.18, 0.20, 0.22]
for i, v in enumerate(sctx_vals):
    r = 34 + i
    put(ws, r, 1, v, INP, "0%", RIGHT)
    for j in range(len(sdm_vals)):
        c = get_column_letter(2 + j)
        put(ws, r, 2 + j, f"=$A{r}*{c}$33*Inputs!$L$27*{R_REC}*{M_SHARE}*10000", FML, "0", RIGHT)
put(ws, 41, 1, "Each cell = s_ctx x s_dm x d (Base FY2030) x r_rec x m x 10,000. Base case is 16.5% x 38%.", NOTE)

# Charts
section(ws, 43, "Chart 1. Discovery Mode gross margin contribution by scenario (bp)")


def bp_chart():
    ch = LineChart()
    for name, col in (("Bear", AQUA), ("Base", BLUE), ("Bull", ORANGE)):
        b = BLOCK[name]
        data = Reference(wd, min_col=3, min_row=b["bp"], max_col=12, max_row=b["bp"])
        ch.add_data(data, from_rows=True, titles_from_data=False)
        s = ch.series[-1]
        from openpyxl.chart.series import SeriesLabel
        s.tx = SeriesLabel(v=name)
        s.graphicalProperties.line.solidFill = col
        s.graphicalProperties.line.width = 22000
        s.marker.symbol = "circle"
        s.marker.size = 6
        s.marker.graphicalProperties.solidFill = col
        s.marker.graphicalProperties.line.solidFill = col
        s.smooth = False
    ch.set_categories(Reference(wd, min_col=3, min_row=4, max_col=12, max_row=4))
    style_chart(ch, "Discovery Mode gross margin contribution (bp)", "bp of gross margin", "0")
    return ch


ws.add_chart(bp_chart(), "A44")
section(ws, 63, "Chart 2. Discovery Mode gross profit by scenario (EUR m)")


def eur_chart():
    ch = BarChart()
    ch.type = "col"
    ch.grouping = "clustered"
    ch.gapWidth = 80
    from openpyxl.chart.series import SeriesLabel
    for name, col in (("Bear", AQUA), ("Base", BLUE), ("Bull", ORANGE)):
        b = BLOCK[name]
        data = Reference(wd, min_col=7, min_row=b["eur"], max_col=12, max_row=b["eur"])  # FY2025-FY2030
        ch.add_data(data, from_rows=True, titles_from_data=False)
        s = ch.series[-1]
        s.tx = SeriesLabel(v=name)
        s.graphicalProperties.solidFill = col
        s.graphicalProperties.line.noFill = True
    ch.set_categories(Reference(wd, min_col=7, min_row=4, max_col=12, max_row=4))
    style_chart(ch, "Discovery Mode gross profit (EUR m)", "EUR m", "#,##0")
    return ch


ws.add_chart(eur_chart(), "A64")

section(ws, 83, "Legend")
for i, s in enumerate([
    "Blue text = hardcoded input (change freely). Black = formula. Green = link to another sheet. Yellow fill = the cells to edit first: scenario selector, revenue override, ex-DM margin path.",
    "Sheets: Inputs (all assumptions) -> DM build (three scenarios computed side by side) -> Revenue & GM (bridge) ; Triangulation (where the two unknowns come from) ; Financials (reported data) ; Sources.",
    "To wire into your revenue build: paste revenue into Inputs row 40 and your ex-DM margin into Inputs row 45, or link 'Revenue & GM'!row 22 (DM % of revenue) and row 27 (DM EUR) straight into your cost of revenue line.",
]):
    put(ws, 84 + i, 1, s, NOTE, align=WRAP)
    ws.merge_cells(start_row=84 + i, start_column=1, end_row=84 + i, end_column=10)
    ws.row_dimensions[84 + i].height = 28

for sh in wb.worksheets:
    sh.sheet_properties.pageSetUpPr.fitToPage = True
    sh.page_setup.fitToWidth = 1
    sh.page_setup.fitToHeight = 0
    sh.page_setup.orientation = "landscape"

wb.save(OUT)
print("saved", OUT)
