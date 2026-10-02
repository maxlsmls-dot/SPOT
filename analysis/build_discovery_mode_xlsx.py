"""Build the Discovery Mode efficacy workbook from the coded report data."""
from datetime import date

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.chart.label import DataLabel, DataLabelList
from openpyxl.chart.shapes import GraphicalProperties
from openpyxl.drawing.line import LineProperties
from openpyxl.chart.text import RichText, Text
from openpyxl.chart.title import Title
from openpyxl.drawing.text import CharacterProperties, Font as DFont, Paragraph, ParagraphProperties, RegularTextRun
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

import sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "discovery_mode_efficacy.xlsx"

F = "Arial"
TITLE = Font(name=F, size=14, bold=True)
H2 = Font(name=F, size=11, bold=True)
HDR = Font(name=F, size=10, bold=True, color="52514E")
TXT = Font(name=F, size=10)
INP = Font(name=F, size=10, color="0000FF")      # hardcoded input
FML = Font(name=F, size=10)                      # formula
LNK = Font(name=F, size=10, color="008000")      # link to another sheet
NOTE = Font(name=F, size=9, italic=True, color="52514E")
HFILL = PatternFill("solid", fgColor="F0EFEC")
WRAP = Alignment(wrap_text=True, vertical="top")
TOP = Alignment(vertical="top")

BLUE, ORANGE, RED, GRAY, GRID = "2A78D6", "EB6834", "E34948", "898781", "E1E0D9"


def put(ws, r, c, v, font=TXT, fmt=None, align=None, fill=None):
    cell = ws.cell(row=r, column=c, value=v)
    cell.font = font
    if fmt:
        cell.number_format = fmt
    if align:
        cell.alignment = align
    if fill:
        cell.fill = fill
    return cell


def header(ws, r, labels, c0=1):
    for i, l in enumerate(labels):
        put(ws, r, c0 + i, l, HDR, align=WRAP, fill=HFILL)


def widths(ws, ws_widths):
    for i, w in enumerate(ws_widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


def bar_series_style(s, color, label_fmt=None):
    s.graphicalProperties.solidFill = color
    s.graphicalProperties.line.noFill = True
    if label_fmt:
        s.dLbls = DataLabelList()
        s.dLbls.showVal = True
        s.dLbls.showSerName = False
        s.dLbls.showCatName = False
        s.dLbls.showLegendKey = False
        s.dLbls.numFmt = label_fmt


def rich_title(text, size, bold):
    cp = CharacterProperties(sz=size, b=bold, latin=DFont(typeface=F), solidFill="0B0B0B")
    para = Paragraph(pPr=ParagraphProperties(defRPr=cp), r=[RegularTextRun(rPr=cp, t=text)])
    return Title(tx=Text(rich=RichText(p=[para])), overlay=False)


def small_text(size=900):
    cp = CharacterProperties(sz=size, latin=DFont(typeface=F), solidFill="52514E")
    return RichText(p=[Paragraph(pPr=ParagraphProperties(defRPr=cp), endParaRPr=cp)])


def style_chart(ch, title, y_title=None, y_fmt=None, w=18, h=8.5):
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

# --------------------------------------------------------------------------
# Campaign lifts (Spotify's own campaign reports)
# --------------------------------------------------------------------------
wc = wb.active
wc.title = "Campaign lifts"
widths(wc, [13, 14, 16, 9, 14, 14, 10, 10, 11, 11, 12, 12, 13, 10, 10, 60])
put(wc, 1, 1, "Spotify campaign reports: Discovery Mode-context streams, before vs during", TITLE)
put(wc, 2, 1, "Streams in Radio, Autoplay and Mixes during the campaign vs the 28 days before, as shown in artists' "
    "Spotify for Artists screenshots. Blue = input read from the screenshot; black = formula.", NOTE)

campaigns = [
    # month, label, source, songs, during, before, listeners, new, engagement, songs_up, songs_n, note
    (date(2023, 8, 1), "Aug 2023", "15woi7w", None, 445475, 91662, 192090, 105307, 0.010573168827112291, None, None, "Aug 1-20 only; 'results insane'"),
    (date(2024, 10, 1), "Oct 2024 (a)", "1g1fk0o", 8, 5658, 1076, 4755, None, 0.011987381703470032, 8, 8, ""),
    (date(2024, 10, 1), "Oct 2024 (b)", "1geig0k", 4, 3011, 359, 1723, 932, 0.0481717933836332, 3, 4, ""),
    (date(2024, 11, 1), "Nov 2024", "1h46nzy", 4, 46995, 16336, 25167, 21328, 0.01072833472404339, None, None, "~25k monthly listeners"),
    (date(2025, 1, 1), "Jan 2025", "1ig7963 (text)", 1, 7404, 4777, None, None, None, None, None,
     "Spotify reported +55% lift, but the same song's TOTAL streams fell from ~46k/month (Oct-Dec) to 43k in Jan"),
    (date(2025, 10, 1), "Oct 2025", "1omcbrg", 7, 39156, 10195, 27807, None, 0.017333764879346927, 7, 7, ""),
    (date(2026, 7, 1), "Jul 2026", "1uy70w1 (text)", 3, 7675, 4312, 5911, 5243, 0.012857384537303333, 3, 3, ""),
]
no_before = [
    (date(2023, 12, 1), "Dec 2023", "18lveoc", 6, 1816, None, 1306, None, 0.018376722817764167, 2, 6, "4 of 6 songs got 0 DM streams (incl. top songs)"),
    (date(2026, 9, 1), "Sep 2026", "1wu7cam", 7, 27994, None, 22689, None, 0.006831504253162326, None, None, "Intent 0.19-1.10% per song"),
]
cols = ["Campaign month", "Label", "Source (r/musicmarketing id)", "Songs enrolled", "DM-context streams, campaign",
        "DM-context streams, prior 28 days", "Reported lift", "Era", "Lift: 2023-24 campaigns", "Lift: 2025-26 campaigns",
        "Campaign listeners", "New listeners", "Saves + adds per listener", "Songs that gained", "Songs reported", "Note"]
header(wc, 4, cols)
wc.row_dimensions[4].height = 42
R0 = 5
for i, (m, lab, src, songs, during, before, lis, new, eng, s_up, s_n, note) in enumerate(campaigns):
    r = R0 + i
    put(wc, r, 1, m, INP, "mmm yyyy")
    put(wc, r, 2, lab, INP)
    put(wc, r, 3, src, INP)
    put(wc, r, 4, songs, INP, "0")
    put(wc, r, 5, during, INP, "#,##0")
    put(wc, r, 6, before, INP, "#,##0")
    put(wc, r, 7, f'=IF(F{r}="","",E{r}/F{r}-1)', FML, "0%")
    put(wc, r, 8, f'=IF(YEAR(A{r})<=2024,"2023-24","2025-26")', FML)
    # Chart helper columns: the lift lands in the column of its era so the chart can color by era.
    if m.year <= 2024:
        put(wc, r, 9, f"=G{r}", FML, "0%")
    else:
        put(wc, r, 10, f"=G{r}", FML, "0%")
    put(wc, r, 11, lis, INP, "#,##0")
    put(wc, r, 12, new, INP, "#,##0")
    put(wc, r, 13, eng, INP, "0.0%")
    put(wc, r, 14, s_up, INP, "0")
    put(wc, r, 15, s_n, INP, "0")
    put(wc, r, 16, note, INP, align=WRAP)
R1 = R0 + len(campaigns) - 1          # last row with a before figure (11)

r = R1 + 2
put(wc, r, 1, "Median reported lift, 2023-24 campaigns", H2)
put(wc, r, 7, f"=MEDIAN(G{R0}:G{R0 + 3})", FML, "0%")
put(wc, r, 8, f'=COUNT(G{R0}:G{R0 + 3})&" campaigns"', FML)
MED_EARLY = f"'Campaign lifts'!$G${r}"
r += 1
put(wc, r, 1, "Median reported lift, 2025-26 campaigns", H2)
put(wc, r, 7, f"=MEDIAN(G{R0 + 4}:G{R1})", FML, "0%")
put(wc, r, 8, f'=COUNT(G{R0 + 4}:G{R1})&" campaigns"', FML)
MED_LATE = f"'Campaign lifts'!$G${r}"
r += 1
put(wc, r, 1, "Median reported lift, all campaigns with a before figure", H2)
put(wc, r, 7, f"=MEDIAN(G{R0}:G{R1})", FML, "0%")
r += 1
put(wc, r, 1, "Latest campaign lift as a share of the earliest", H2)
put(wc, r, 7, f"=G{R1}/G{R0}", FML, "0%")

r += 2
put(wc, r, 1, "Campaign reports without a prior-28-day figure (engagement only)", H2)
r += 1
header(wc, r, cols)
wc.row_dimensions[r].height = 42
NB0 = r + 1
for i, (m, lab, src, songs, during, before, lis, new, eng, s_up, s_n, note) in enumerate(no_before):
    rr = NB0 + i
    put(wc, rr, 1, m, INP, "mmm yyyy")
    put(wc, rr, 2, lab, INP)
    put(wc, rr, 3, src, INP)
    put(wc, rr, 4, songs, INP, "0")
    put(wc, rr, 5, during, INP, "#,##0")
    put(wc, rr, 6, before, INP, "#,##0")
    put(wc, rr, 7, f'=IF(F{rr}="","",E{rr}/F{rr}-1)', FML, "0%")
    put(wc, rr, 8, f'=IF(YEAR(A{rr})<=2024,"2023-24","2025-26")', FML)
    put(wc, rr, 11, lis, INP, "#,##0")
    put(wc, rr, 12, new, INP, "#,##0")
    put(wc, rr, 13, eng, INP, "0.0%")
    put(wc, rr, 14, s_up, INP, "0")
    put(wc, rr, 15, s_n, INP, "0")
    put(wc, rr, 16, note, INP, align=WRAP)
r = NB0 + len(no_before) + 1
for line in [
    "Reported lift = campaign streams / prior-28-day streams - 1. Where the screenshot showed only the lift, the prior-28-day figure is streams / (1 + lift).",
    "These counts cover only Radio, Autoplay and Mixes. They do not show whether the song's total streams rose; the Jan 2025 case is the one artist who checked, and total streams fell.",
    "Saves + adds per listener = (saves + playlist adds) / campaign listeners, from the same screenshot.",
    "Source: screenshots posted to r/musicmarketing, identified by post id. Collected via the Arctic Shift archive, read by hand.",
]:
    put(wc, r, 1, line, NOTE)
    r += 1
wc.freeze_panes = "A5"


def lift_chart():
    ch = BarChart()
    ch.type = "col"
    ch.grouping = "clustered"
    ch.gapWidth = 60
    ch.overlap = 100  # the two era series never share a row, so overlap keeps bars full width
    data = Reference(wc, min_col=9, min_row=4, max_col=10, max_row=R1)
    cats = Reference(wc, min_col=2, min_row=R0, max_row=R1)
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(cats)
    bar_series_style(ch.series[0], BLUE, "0%")
    bar_series_style(ch.series[1], ORANGE, "0%")
    style_chart(ch, "Spotify-reported Discovery Mode lift, by campaign date", "Lift vs prior 28 days", "0%")
    return ch


wc.add_chart(lift_chart(), "R4")

# --------------------------------------------------------------------------
# Artist pairs (first-hand before/after numbers)
# --------------------------------------------------------------------------
wp = wb.create_sheet("Artist pairs")
widths(wp, [12, 7, 26, 14, 11, 13, 13, 10, 10, 24, 70])
put(wp, 1, 1, "Artists' own before/after numbers (every first-hand report that gave both)", TITLE)
put(wp, 2, 1, "Blue = as reported by the artist; black = formula. 'Flat' = change within +/-5%.", NOTE)
pairs = [
    (date(2023, 10, 13), "Monthly listeners", 37500, 37500, 19000, "176v311/k2zctt7/k3tx6dh", "Organic 35-40k listeners; after 3 months of DM down to 19k, no follows/saves from DM, Fans Also Like 'destroyed'."),
    (date(2023, 10, 14), "Monthly listeners", 80000, 80000, 52000, "k4ox17o", "Discover Weekly streams fell, radio rose; saves/adds from DM 'terrible'."),
    (date(2023, 10, 14), "Monthly listeners", 80000, 80000, 40000, "k4pk3ug", "Blames Spotify pushing Discover Weekly less after DM."),
    (date(2023, 10, 27), "Radio streams / month", None, 1800, 20000, "k6lhdlu", "Radio ~1,800/month before DM -> ~20,000/month after several months (releases weekly)."),
    (date(2023, 11, 10), "Monthly listeners", 30000, 30000, 8700, "k79yvek", "One song on DM in Sept (0.90% intent); skipped Oct and Discover Weekly 'suppressed'; re-enrolled out of fear."),
    (date(2023, 12, 1), "Monthly listeners", 30000, 30000, 5000, "kbb4arn", "Beta: first campaign gave a bump; second campaign listeners fell 30k -> 5k (normal range 10-20k)."),
    (date(2024, 2, 27), "Streams / month", None, 10000, 50000, "kspq2mj", "'Totally down to discovery mode'; not every song works."),
    (date(2024, 3, 1), "Streams / day", None, 40000, 15000, "1b43vbm", "Song at ~40k/day; fell the month it was enrolled and never recovered; also pulled from Discover Weekly."),
    (date(2024, 3, 1), "Radio streams / month", None, 4000, 150, "ksx3w9s", "Last DM month: 150 streams; month without DM: 4k on radio alone."),
    (date(2024, 3, 1), "Monthly listeners", 2000, 2000, 7500, "kszo2zz", ""),
    (date(2024, 3, 13), "Streams / month", None, 1000000, 300000, "ktmj79o", "~1M streams/month -> 300k 'literally overnight'; never came back after stopping."),
    (date(2024, 8, 14), "Discover Weekly streams / week", None, 5000, 190, "li52lv4/lve66bg", "Best track ~5k DW streams/week; 3 weeks on DM = 567 DW streams total; took 4 months to recover."),
    (date(2024, 12, 23), "Monthly listeners", 25000, 25000, 60000, "m3i1jez", "~30k DM streams month 1, 40k month 2."),
    (date(2024, 12, 27), "Monthly listeners", 5000, 5000, 44000, "m3ys1wz", "Meta ads + DM; much of growth via radio."),
    (date(2025, 2, 2), "Streams / month", 60000, 36655, 36549, "1ig7963", "Song A: Dec 36,655 streams -> Jan 36,549 while Spotify reported +69% lift. Song B: ~46k/month -> 43k while Spotify credited 7,404 DM streams (+55%)."),
    (date(2025, 9, 9), "Monthly listeners", 10000, 10000, 20000, "nd42847", ""),
    (date(2025, 9, 9), "Monthly listeners", 100, 100, 700, "nd5w63f", "One track on DM ~800 streams/month; fans at shows cite it."),
    (date(2026, 2, 14), "Streams / day", 100000, 500, 1000, "1r4op37", "Taking the song OUT of DM cut it from ~1,000 to ~500 streams/day; 'would not take it out again'."),
]
header(wp, 4, ["Date posted", "Year", "Measure", "Monthly listeners at start", "Size band", "Before", "After", "Change", "Direction", "Source", "What the artist said"])
wp.row_dimensions[4].height = 30
P0 = 5
for i, (d, metric, ml, before, after, src, note) in enumerate(pairs):
    r = P0 + i
    put(wp, r, 1, d, INP, "yyyy-mm-dd")
    put(wp, r, 2, f"=YEAR(A{r})", FML, "0")
    put(wp, r, 3, metric, INP)
    put(wp, r, 4, ml, INP, "#,##0")
    put(wp, r, 5, f'=IF(D{r}="","not stated",IF(D{r}<10000,"Under 10k",IF(D{r}<50000,"10k-50k","50k+")))', FML)
    put(wp, r, 6, before, INP, "#,##0")
    put(wp, r, 7, after, INP, "#,##0")
    put(wp, r, 8, f"=G{r}/F{r}-1", FML, "+0%;-0%;0%")
    put(wp, r, 9, f'=IF(ABS(H{r})<0.05,"Flat",IF(H{r}>0,"Up","Down"))', FML)
    put(wp, r, 10, src, INP)
    put(wp, r, 11, note, INP, align=WRAP)
P1 = P0 + len(pairs) - 1

r = P1 + 2
put(wp, r, 1, "Direction by year posted (these 18 numeric pairs)", H2)
r += 1
header(wp, r, ["Year", "Up", "Down", "Flat", "Total", "Avg listeners at start, Down cases"])
YR0 = r + 1
for i, y in enumerate([2023, 2024, 2025, 2026]):
    rr = YR0 + i
    put(wp, rr, 1, str(y), INP)
    for c, d in zip((2, 3, 4), ("Up", "Down", "Flat")):
        put(wp, rr, c, f'=COUNTIFS($B${P0}:$B${P1},VALUE(A{rr}),$I${P0}:$I${P1},"{d}")', FML, "0")
    put(wp, rr, 5, f"=SUM(B{rr}:D{rr})", FML, "0")
    put(wp, rr, 6, f'=IFERROR(AVERAGEIFS($D${P0}:$D${P1},$B${P0}:$B${P1},VALUE(A{rr}),$I${P0}:$I${P1},"Down"),"size not stated")', FML, "#,##0")
r = YR0 + 4
put(wp, r, 1, "Caveat: by year, these pairs trend toward 'Up', not away from it. The 2023 losers were all 30k-80k-listener artists in the "
    "early rollout; most later winners are small artists. Read it as a change in who posts, not proof the program improved.", NOTE)
wp.row_dimensions[r].height = 30
wp.merge_cells(start_row=r, start_column=1, end_row=r, end_column=11)
wp.cell(row=r, column=1).alignment = WRAP

r += 2
put(wp, r, 1, "Direction by audience size at the start (all first-hand reports that stated a size, n = 26)", H2)
r += 1
header(wp, r, ["Size band", "Up", "Mixed / flat", "Down", "Total", "Share up"])
SZ0 = r + 1
by_size = [("Under 10k", 8, 0, 0), ("10k-50k", 4, 1, 4), ("50k+", 3, 3, 3)]
for i, (band, up, mid, down) in enumerate(by_size):
    rr = SZ0 + i
    put(wp, rr, 1, band, INP)
    put(wp, rr, 2, up, INP, "0")
    put(wp, rr, 3, mid, INP, "0")
    put(wp, rr, 4, down, INP, "0")
    put(wp, rr, 5, f"=SUM(B{rr}:D{rr})", FML, "0")
    put(wp, rr, 6, f"=B{rr}/E{rr}", FML, "0%")
SZ1 = SZ0 + 2
rr = SZ1 + 1
put(wp, rr, 1, "10k and above", FML)
put(wp, rr, 2, f"=SUM(B{SZ0 + 1}:B{SZ1})", FML, "0")
put(wp, rr, 3, f"=SUM(C{SZ0 + 1}:C{SZ1})", FML, "0")
put(wp, rr, 4, f"=SUM(D{SZ0 + 1}:D{SZ1})", FML, "0")
put(wp, rr, 5, f"=SUM(B{rr}:D{rr})", FML, "0")
put(wp, rr, 6, f"=B{rr}/E{rr}", FML, "0%")
SHARE_SMALL = f"'Artist pairs'!$F${SZ0}"
SHARE_BIG = f"'Artist pairs'!$F${rr}"
put(wp, rr + 1, 1, "Counts come from the hand-coded set of 70 first-hand reports (not only the 18 with numbers); 26 of them stated an audience size. "
    "'Mixed / flat' pools the report's 'mixed' and 'flat' codes.", NOTE)
wp.freeze_panes = "A5"


def size_chart():
    ch = BarChart()
    ch.type = "bar"
    ch.grouping = "stacked"
    ch.overlap = 100
    ch.gapWidth = 60
    data = Reference(wp, min_col=2, min_row=SZ0 - 1, max_col=4, max_row=SZ1)
    cats = Reference(wp, min_col=1, min_row=SZ0, max_row=SZ1)
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(cats)
    bar_series_style(ch.series[0], BLUE, "0;-0;;@")   # hide zero-count segments' labels
    bar_series_style(ch.series[1], GRAY, "0;-0;;@")
    bar_series_style(ch.series[2], RED, "0;-0;;@")
    for si, col in ((1, 3), (2, 4)):
        hidden = [DataLabel(idx=i, showVal=False, showSerName=False, showCatName=False, showLegendKey=False)
                  for i, (band, up, mid, down) in enumerate(by_size) if (mid if col == 3 else down) == 0]
        if hidden:
            ch.series[si].dLbls.dLbl = hidden
    ch.x_axis.scaling.orientation = "maxMin"  # keep "Under 10k" on top
    ch.y_axis.crosses = "max"                 # value axis stays at the bottom
    ch.x_axis.tickLblSkip = 1
    style_chart(ch, "Did streams go up? First-hand reports by artist size", "Number of reports", "0", h=6.5)
    return ch


wp.add_chart(size_chart(), "H24")

# --------------------------------------------------------------------------
# Engagement
# --------------------------------------------------------------------------
we = wb.create_sheet("Engagement")
widths(we, [24, 30, 18, 13, 16, 16, 16])
put(we, 1, 1, "How often listeners keep the song: saves + playlist adds per listener", TITLE)
put(we, 2, 1, "Discovery Mode campaign listeners (Spotify campaign report) vs artists' overall audience (Spotify for Artists dashboard). Blue = input.", NOTE)
header(we, 4, ["Group", "Campaign / artist", "Source", "Listeners", "Saves + adds per listener", "Discovery Mode listeners", "Overall audience"])
we.row_dimensions[4].height = 42
eng_rows = [
    ("Discovery Mode listeners", "Aug 2023 campaign", "15woi7w", 192090, 0.010573168827112291),
    ("Discovery Mode listeners", "Dec 2023 campaign", "18lveoc", 1306, 0.018376722817764167),
    ("Discovery Mode listeners", "Oct 2024 campaign (a)", "1g1fk0o", 4755, 0.011987381703470032),
    ("Discovery Mode listeners", "Oct 2024 campaign (b)", "1geig0k", 1723, 0.0481717933836332),
    ("Discovery Mode listeners", "Nov 2024 campaign", "1h46nzy", 25167, 0.01072833472404339),
    ("Discovery Mode listeners", "Oct 2025 campaign", "1omcbrg", 27807, 0.017333764879346927),
    ("Discovery Mode listeners", "Jul 2026 campaign", "1uy70w1", 5911, 0.012857384537303333),
    ("Discovery Mode listeners", "Sep 2026 campaign", "1wu7cam", 22689, 0.006831504253162326),
    ("Overall audience", "Artist 17gqiej, 12 months", "17gqiej", None, 0.24525391551969625),
    ("Overall audience", "Artist 1q4bb7s, all time", "1q4bb7s", None, 0.18248587915984057),
    ("Overall audience", "Artist 1rvflj9, 12 months", "1rvflj9", None, 0.2146131941755588),
    ("Overall audience", "Kublaii (1hn3dhf), 12 months", "1hn3dhf", None, 0.0806229419475458),
]
E0 = 5
for i, (grp, name, src, lis, rate) in enumerate(eng_rows):
    r = E0 + i
    put(we, r, 1, grp, INP)
    put(we, r, 2, name, INP)
    put(we, r, 3, src, INP)
    put(we, r, 4, lis, INP, "#,##0")
    put(we, r, 5, rate, INP, "0.0%")
    put(we, r, 6 if grp.startswith("Discovery") else 7, f"=E{r}", FML, "0.0%")
E_DM1 = E0 + 7
E1 = E0 + len(eng_rows) - 1
r = E1 + 2
put(we, r, 1, "Median, Discovery Mode listeners", H2)
put(we, r, 5, f"=MEDIAN(E{E0}:E{E_DM1})", FML, "0.0%")
MED_DM = f"Engagement!$E${r}"
r += 1
put(we, r, 1, "Median, overall audience", H2)
put(we, r, 5, f"=MEDIAN(E{E_DM1 + 1}:E{E1})", FML, "0.0%")
MED_OVR = f"Engagement!$E${r}"
r += 1
put(we, r, 1, "Overall audience keeps the song this many times more often", H2)
put(we, r, 5, f"=E{r - 1}/E{r - 2}", FML, '0.0"x"')
r += 2
put(we, r, 1, "Discovery Mode rate = (saves + playlist adds) / campaign listeners, from the campaign report. Overall rate = saves / listeners from the artist's dashboard. "
    "Different artists and definitions, so read as orders of magnitude.", NOTE)
we.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
we.cell(row=r, column=1).alignment = WRAP
we.row_dimensions[r].height = 30
we.freeze_panes = "A5"


def eng_chart():
    ch = BarChart()
    ch.type = "bar"
    ch.grouping = "clustered"
    ch.overlap = 100
    ch.gapWidth = 50
    data = Reference(we, min_col=6, min_row=4, max_col=7, max_row=E1)
    cats = Reference(we, min_col=2, min_row=E0, max_row=E1)
    ch.add_data(data, titles_from_data=True)
    ch.set_categories(cats)
    bar_series_style(ch.series[0], BLUE, "0.0%")
    bar_series_style(ch.series[1], ORANGE, "0.0%")
    ch.x_axis.scaling.orientation = "maxMin"
    ch.y_axis.crosses = "max"
    ch.x_axis.tickLblSkip = 1
    style_chart(ch, "Discovery Mode listeners rarely keep the song", "Saves + adds per listener", "0%", h=13)
    return ch


we.add_chart(eng_chart(), "I4")

# --------------------------------------------------------------------------
# On/off cases
# --------------------------------------------------------------------------
wo = wb.create_sheet("On-off cases")
widths(wo, [16, 26, 30, 12, 12, 11, 80])
put(wo, 1, 1, "What happened when Discovery Mode was switched on or off", TITLE)
put(wo, 2, 1, "Cases where an artist's own graphs show the switch. Blue = as reported; black = formula.", NOTE)
header(wo, 4, ["Source", "Change", "Measure", "Before", "After", "Change", "What happened"])
onoff = [
    ("1and042", "DM on (Apr 2023)", "Radio & autoplay listeners / day", 70, 900, "~70/day before -> ~400 right after -> ~900-1,200 a year later; weekly releases throughout."),
    ("1q4bb7s", "DM on (Dec 1, 2025)", "Artist streams / month", 195000, 280000, "Nov ~195k -> Dec ~280k (back to Oct level). Song-level daily streams: 2,646 -> ~4,500; 270 -> ~900; 553 -> ~1,300. Popularity of 4 promoted songs +4-6 points, top song -2. Followers/day unchanged."),
    ("1rvflj9", "DM off (Oct 2025) then on", "Radio & autoplay streams / day", 7000, 2000, "~6-9k/day Jul-Sep with DM -> ~2k/day in October with DM off -> 6-11k/day after re-enrolling. Then an ~80% collapse in Mar 2026 with DM on."),
    ("1r4op37 (text)", "DM off", "Song streams / day", 1000, 500, "Spotify flagged the song 'not recommended'; removing it halved daily streams."),
    ("ksx3w9s (text)", "DM off", "Radio streams / month", 150, 4000, "Opposite case: 150 DM streams in last DM month; 4k radio the month after leaving."),
    ("1t81jjd", "DM off + Meta ads", "Song radio streams (28 days)", None, 74, "7 of 12 songs had fallen to 0-100 radio streams in DM; after opting out, radio stayed at 74 even with ads (saves +270%)."),
]
for i, (src, ev, metric, before, after, note) in enumerate(onoff):
    r = 5 + i
    put(wo, r, 1, src, INP)
    put(wo, r, 2, ev, INP)
    put(wo, r, 3, metric, INP)
    put(wo, r, 4, before, INP, "#,##0")
    put(wo, r, 5, after, INP, "#,##0")
    put(wo, r, 6, f'=IF(OR(D{r}="",E{r}=""),"",E{r}/D{r}-1)', FML, "+0%;-0%;0%")
    put(wo, r, 7, note, INP, align=WRAP)
    wo.row_dimensions[r].height = 30
put(wo, 12, 1, "Why it matters for the framing: artists who stay enrolled describe it as defensive (re-enrolled out of fear; 'would not take it out again'). "
    "Switching off cut radio streams by 50-70% in two charted cases. For an artist deciding whether to enroll for the first time, the pitch has become 'pay 30% to avoid losing ground'.", NOTE)
wo.merge_cells("A12:G12")
wo.cell(row=12, column=1).alignment = WRAP
wo.row_dimensions[12].height = 42

# --------------------------------------------------------------------------
# Reference
# --------------------------------------------------------------------------
wr = wb.create_sheet("Reference")
widths(wr, [52, 14, 14, 60])
put(wr, 1, 1, "Corpus, extra series and method", TITLE)
r = 3
put(wr, r, 1, "Corpus", H2)
r += 1
corpus = [
    ("r/musicmarketing posts since Oct 2020 (Arctic Shift archive)", 27088),
    ("Posts mentioning Discovery Mode", 130),
    ("Comments in those threads", 1953),
    ("Artist experiences coded", 73),
    ("  of which first-hand", 70),
    ("  first-hand: streams went up", 39),
    ("  first-hand: streams went down", 21),
    ("  first-hand: mixed", 7),
    ("  first-hand: flat", 3),
    ("First-hand reports saying Discover Weekly / algorithmic streams fell after opting in", 12),
    ("Spotify for Artists screenshots read (7 more had been deleted)", 35),
]
CORP = {}
for lab, v in corpus:
    put(wr, r, 1, lab, TXT)
    put(wr, r, 2, v, INP, "#,##0")
    CORP[lab.strip()] = f"Reference!$B${r}"
    r += 1
put(wr, r, 1, "Share of first-hand reports that went up", TXT)
put(wr, r, 2, f"=B{r-6}/B{r-7}", FML, "0%")
r += 2

put(wr, r, 1, "Spotify-reported 'stream lift' figures quoted in posts and screenshots (%)", H2)
put(wr, r, 4, "Order as extracted; dates not attached, so this list cannot be used for a time trend.", NOTE)
r += 1
lifts = [277, 915, 1192, 150, 2000, 3000, 6000, 153, 69, 55, 78, 214, 169]
L0 = r
for v in lifts:
    put(wr, r, 1, f"Lift {r - L0 + 1}", TXT)
    put(wr, r, 2, v / 100, INP, "0%")
    r += 1
put(wr, r, 1, "Median", H2)
put(wr, r, 2, f"=MEDIAN(B{L0}:B{r - 1})", FML, "0%")
r += 2

put(wr, r, 1, "Intent rate per song quoted by artists (saves + adds / listeners, %)", H2)
put(wr, r, 4, "Spotify's own engagement measure for a Discovery Mode song. Order as extracted.", NOTE)
r += 1
intent = [1.5, 0.9, 2.0, 2.66, 1.0, 0.79, 1.0, 1.21, 0.4, 0.7, 0.9]
I0 = r
for v in intent:
    put(wr, r, 1, f"Intent {r - I0 + 1}", TXT)
    put(wr, r, 2, v / 100, INP, "0.00%")
    r += 1
put(wr, r, 1, "Median", H2)
put(wr, r, 2, f"=MEDIAN(B{I0}:B{r - 1})", FML, "0.00%")
r += 2

put(wr, r, 1, "Discovery Mode share of an artist's monthly streams", H2)
put(wr, r, 4, "Established artists (500k+ monthly streams) report 3-5%; catalog-heavy artists up to a third.", NOTE)
r += 1
share = [("m8up79g", 0.03496503496503497), ("lzx6qd3", 0.04), ("m3ivdij", 0.03879310344827586), ("m49nghw", 0.05),
         ("1deqxiz (range 5-15%)", 0.10), ("mkxt4r8", 0.3333333333333333), ("m3suhdk", 0.3333333333333333), ("m3su5uz (best month)", 0.5)]
S0 = r
for src, v in share:
    put(wr, r, 1, src, TXT)
    put(wr, r, 2, v, INP, "0.0%")
    r += 1
put(wr, r, 1, "Median", H2)
put(wr, r, 2, f"=MEDIAN(B{S0}:B{r - 1})", FML, "0.0%")
MED_SHARE = f"Reference!$B${r}"
r += 2

put(wr, r, 1, "Method and caveats", H2)
r += 1
for line in [
    "Source: every r/musicmarketing post since Oct 2020 (Arctic Shift archive), filtered to the 130 that mention Discovery Mode, plus all 1,953 comments in those threads. r/SpotifyForArtists has no posts after Feb 2020, so it could not be used.",
    "Each first-hand artist experience was read and coded by hand: audience size, the before/after measure they gave, and direction. Repeat comments by the same person were merged. Second-hand stories are excluded.",
    "35 screenshots were downloaded and read (7 had been deleted). Spotify campaign reports give Discovery Mode-context streams and the 'stream lift' versus the 28 days before. Where only the lift was shown, the before figure is streams / (1 + lift).",
    "Engagement for Discovery Mode listeners = (saves + playlist adds) / campaign listeners. Overall rates are saves / listeners from four artists' 12-month dashboards. Different artists and definitions, so read them as orders of magnitude.",
    "These are self-selected stories. People post when results are surprising, good or bad. Discovery Mode's start often coincides with releases, ads or TikTok moments, and Spotify's algorithm changes over time (several artists report sudden platform-wide drops in 2026). None of this is a controlled experiment.",
    "Sample sizes are small: 7 campaign reports with a before figure, 18 artist-reported before/after pairs, 26 reports with a stated audience size. The workbook illustrates a thesis; it cannot carry one on its own.",
    "Reproduce: collect_dm.py -> dm_export_reading.py -> dm_reports.py -> dm_download_images.py -> build_dm_report.py (pipeline from the earlier session; not in this repository).",
]:
    put(wr, r, 1, line, TXT, align=WRAP)
    wr.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
    wr.row_dimensions[r].height = 42
    r += 1

# --------------------------------------------------------------------------
# Summary (first sheet)
# --------------------------------------------------------------------------
ws = wb.create_sheet("Summary", 0)
widths(ws, [74, 16, 14, 14, 14, 14, 14, 14])
put(ws, 1, 1, "Spotify Discovery Mode: is the boost fading?", TITLE)
put(ws, 2, 1, "Evidence from 70 first-hand artist reports on r/musicmarketing (Oct 2020 - Oct 2026) and 35 Spotify for Artists screenshots. "
    "Green cells link to the data sheets.", NOTE)

r = 4
put(ws, r, 1, "Key numbers", H2)
r += 1
stats = [
    ("Median Spotify-reported lift, campaigns Aug 2023 - Nov 2024 (n = 4)", f"={MED_EARLY}", "+0%"),
    ("Median Spotify-reported lift, campaigns Jan 2025 - Jul 2026 (n = 3)", f"={MED_LATE}", "+0%"),
    ("Median saves + adds per Discovery Mode listener (8 campaigns)", f"={MED_DM}", "0.0%"),
    ("Median saves per listener, artists' overall audience (4 dashboards)", f"={MED_OVR}", "0.0%"),
    ("Share of first-hand reports that went up: artists under 10k listeners", f"={SHARE_SMALL}", "0%"),
    ("Share of first-hand reports that went up: artists with 10k+ listeners", f"={SHARE_BIG}", "0%"),
    ("First-hand reports saying Discover Weekly / algorithmic streams fell", f'={CORP["First-hand reports saying Discover Weekly / algorithmic streams fell after opting in"]}&" of "&{CORP["of which first-hand"]}', None),
    ("Median Discovery Mode share of monthly streams (established artists)", f"={MED_SHARE}", "0.0%"),
]
for lab, fml, fmt in stats:
    put(ws, r, 1, lab, TXT)
    put(ws, r, 2, fml, LNK, fmt, align=Alignment(horizontal="right"))
    r += 1

r += 1
put(ws, r, 1, "The argument", H2)
r += 1
points = [
    "1. Mechanism first. Discovery Mode is a relative boost inside a fixed pool of Radio and Autoplay slots. Every new enrollee dilutes the others, so the per-track payoff must fall as enrollment grows. Symptoms: in one Dec 2023 campaign 4 of 6 enrolled songs got zero Discovery Mode streams; in 2025 one artist found 7 of 12 enrolled songs at 0-100 radio streams while still enrolled.",
    "2. Spotify's own lift metric is shrinking. Even on the flattering Radio/Autoplay-only measure, the 2025-26 campaign reports show a fraction of the 2023-24 lifts (chart 1; 'Campaign lifts' sheet).",
    "3. The lift is hollow. The one artist who checked total streams found Spotify claiming +55% while the song's total fell. Discovery Mode listeners keep the song about 1% of the time versus roughly 20% for an artist's normal audience, and the latest campaign in the set has the lowest engagement of all (chart 2; 'Engagement' sheet).",
    "4. Enrollment has become defensive. Artists who stay say they re-enrolled out of fear or 'would not take it out again'; opting out halved one song's daily streams. For a new artist the pitch is now 'give up 30% to avoid losing ground', not 'give up 30% to grow' ('On-off cases' sheet).",
    "5. It still works only where the royalties barely matter. Every report from artists under 10k listeners went up; above 10k it is a coin flip (chart 3; 'Artist pairs' sheet). The addressable pool for the margin lever is the long tail.",
]
for p in points:
    put(ws, r, 1, p, TXT, align=WRAP)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
    ws.row_dimensions[r].height = 48
    r += 1

r += 1
put(ws, r, 1, "Where it breaks", H2)
r += 1
for p in [
    "The 18 artist-reported before/after pairs trend toward 'Up' over time (2023: 1 up / 5 down; 2025-26: 3 up / 0 down). The defensible reading is mix shift: the 2023 losers were 30k-80k-listener artists in the early rollout, the later winners are mostly small. State that; do not rely on the pairs for the time claim.",
    "Sample sizes are tiny (7 campaign lifts, 18 pairs) and self-selected from one subreddit. The 2026 platform-wide drops some artists report could be an algorithm change unrelated to the program.",
]:
    put(ws, r, 1, p, TXT, align=WRAP)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=8)
    ws.row_dimensions[r].height = 42
    r += 1

r += 1
put(ws, r, 1, "Chart 1. Spotify-reported lift by campaign date (the headline chart)", H2)
ws.add_chart(lift_chart(), f"A{r + 1}")
r += 19
put(ws, r, 1, "Chart 2. Discovery Mode listeners rarely keep the song", H2)
ws.add_chart(eng_chart(), f"A{r + 1}")
r += 28
put(ws, r, 1, "Chart 3. Reports of streams going up, by artist size", H2)
ws.add_chart(size_chart(), f"A{r + 1}")

for sh in wb.worksheets:
    sh.sheet_properties.pageSetUpPr.fitToPage = True
    sh.page_setup.fitToWidth = 1
    sh.page_setup.fitToHeight = 0
    sh.page_setup.orientation = "landscape"

wb.save(OUT)
print("saved", OUT)
