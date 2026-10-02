#!/usr/bin/env python3
"""Discovery Mode / autoplay gross-margin tabs styled to match the SPOT operating model
(same conventions as analysis/audiobooks_model_tabs.py: Calibri 11, gridlines off, content from B2,
navy header row with FY'24-FY'27E columns and a Notes column, blue inputs, black formulas,
light-gold placeholders to link into the model, yellow boxed output rows, Bear/Base/Bull case selector).

Tabs
  'DM Inputs'              reported anchors, marketplace disclosures, structural levers, scenario rows, case selector
  'DM GM Bridge'           FY'25 calibration -> D (Discovery Mode) + Q (Marquee/Showcase) = M -> y/y gross-margin effect
  'DM Sensitivity'         FY'27E Discovery Mode contribution by e x s; implied FY'25 enrolled share by e x DM share
  'DM Evidence'            what the two datasets say, every number a link to the data tabs
  'DM Data Sentiment'      r/spotify + r/truespotify corpus and themes by year; scored-sample stats via COUNTIFS
  'DM Data Scored Posts'   the 4,000 scored posts (text trimmed to 150 chars)
  'DM Data Campaigns'      Spotify for Artists campaign reports, engagement, on/off cases
  'DM Data Artist Reports' artist before/after pairs, direction by year and size, corpus counts, reference series

Sources: data/spotify_autoplay_sentiment.xlsx, data/discovery_mode_efficacy.xlsx
Output:  data/SPOT_DM_Tabs.xlsx.   Run: python3 analysis/dm_model_tabs.py   (then recalc with LibreOffice)
"""
import os, re
from datetime import datetime
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SRC_SENT = os.path.join(DATA, "spotify_autoplay_sentiment.xlsx")
SRC_DM = os.path.join(DATA, "discovery_mode_efficacy.xlsx")
OUT = os.path.join(DATA, "SPOT_DM_Tabs.xlsx")

# ----------------------------------------------------------------------------- house style
NAVY = PatternFill("solid", fgColor="FF002060"); BAND = PatternFill("solid", fgColor="FFE7E6E6")
GOLD = PatternFill("solid", fgColor="FFFFF2CC"); YELLOW = PatternFill("solid", fgColor="FFFFFF00")
F_HDR = Font(name="Calibri", size=11, bold=True, color="FFFFFFFF")
F_TXT = Font(name="Calibri", size=11); F_B = Font(name="Calibri", size=11, bold=True); F_I = Font(name="Calibri", size=11, italic=True)
F_IN = Font(name="Calibri", size=11, color="FF0070C0"); F_IN_B = Font(name="Calibri", size=11, bold=True, color="FF0070C0")
THIN = Side(style="thin"); CENTER = Alignment(horizontal="center"); LEFT = Alignment(horizontal="left")
NOTE = Alignment(wrap_text=True, vertical="top")
FM = '#,##0_);\\(#,##0\\)'; FBP = '0_);\\(0\\)'; FP0 = '0%'; FP1 = '0.0%'; FP2 = '0.00%'; F0 = '0'; F1 = '0.0'; FX = '0.00'; FMULT = '0.00"x"'; FDATE = 'yyyy-mm-dd'
YC = ["C", "D", "E", "F"]; YEARS = ["FY'24", "FY'25", "FY'26E", "FY'27E"]
CAL = ["2023", "2024", "2025", "2026 YTD"]

SH_IN, SH_BR, SH_SE, SH_EV, SH_DS, SH_SP, SH_DC, SH_DA = ("DM Inputs", "DM GM Bridge", "DM Sensitivity", "DM Evidence",
                                                          "DM Data Sentiment", "DM Data Scored Posts", "DM Data Campaigns", "DM Data Artist Reports")
def q(sheet): return f"'{sheet}'!"

def setup(ws, title, years=YEARS, year_cols=YC, notes_col="H", widths=None, spare=("G",)):
    """Navy title row 2 (title in B, period labels in year_cols, 'Notes' in notes_col), grey band row 3, freeze below."""
    ws.sheet_view.showGridLines = False
    widths = widths or {"A": 8.9, "B": 58, **{c: 13 for c in year_cols}, **{c: 13 for c in spare}, notes_col: 78}
    for c, w in widths.items(): ws.column_dimensions[c].width = w
    cols =[get_column_letter(i) for i in range(2, max(ord(c) for c in widths if len(c) == 1) - 64 + 1)]
    ws["B2"] = title
    for col in cols:
        ws[f"{col}2"].fill = NAVY; ws[f"{col}2"].font = F_HDR; ws[f"{col}3"].fill = BAND
    for col, y in zip(year_cols, years):
        ws[f"{col}2"] = y; ws[f"{col}2"].alignment = CENTER
    if notes_col: ws[f"{notes_col}2"] = "Notes"
    ws.freeze_panes = "A4"
    return cols

class Writer:
    """Row writer: label in B, values in year columns, optional G value, note in the notes column."""
    def __init__(self, ws, notes_col="H", year_cols=YC): self.ws = ws; self.r = 3; self.nc = notes_col; self.yc = year_cols
    def row(self, label=None, vals=None, note=None, bold=False, italic=False, fill=None, top=False, box=False, g=None, fmt=None, align=CENTER, label_font=None, fmts=None):
        self.r += 1; ws = self.ws; rr = self.r
        if label is not None:
            c = ws.cell(row=rr, column=2, value=label); c.font = label_font or (F_B if bold else (F_I if italic else F_TXT))
            if italic: c.alignment = LEFT
        if vals:
            for i, (col, v) in enumerate(zip(self.yc, vals)):
                if v is None or v == "": continue
                self._cell(f"{col}{rr}", v, bold, (fmts[i] if fmts else fmt), align)
        if g is not None: self._cell(f"G{rr}", g, bold, fmt, align)
        if note:
            c = ws[f"{self.nc}{rr}"]; c.value = note; c.font = F_I; c.alignment = NOTE
        if fill:
            for col in ["B"] + self.yc: ws[f"{col}{rr}"].fill = fill
        if top:
            for col in ["B"] + self.yc: ws[f"{col}{rr}"].border = Border(top=THIN)
        if box:
            ws[f"B{rr}"].border = Border(left=THIN, top=THIN, bottom=THIN)
            for col in self.yc: ws[f"{col}{rr}"].border = Border(top=THIN, bottom=THIN)
        return rr
    def _cell(self, ref, v, bold, fmt, align):
        c = self.ws[ref]; c.value = v; c.alignment = align
        is_formula = isinstance(v, str) and v.startswith("=")
        c.font = (F_B if bold else F_TXT) if is_formula else (F_IN_B if bold else F_IN)
        if fmt: c.number_format = fmt
    def blank(self): self.r += 1
    def section(self, label): return self.row(label, bold=True)
    def subhdr(self, labels, g=None):
        rr = self.row(labels[0], label_font=F_I)
        for col, t in zip(self.yc, labels[1:]):
            c = self.ws[f"{col}{rr}"]; c.value = t; c.font = F_B; c.alignment = CENTER; c.border = Border(bottom=THIN)
        if g: c = self.ws[f"G{rr}"]; c.value = g; c.font = F_B; c.alignment = CENTER; c.border = Border(bottom=THIN)
        return rr

def gridcell(ws, ref, v, fmt=None, bold=False, inp=False, align=CENTER, border=None):
    c = ws[ref]; c.value = v; c.alignment = align
    c.font = (F_IN_B if bold else F_IN) if inp else (F_B if bold else F_TXT)
    if fmt: c.number_format = fmt
    if border: c.border = border
    return c

# ----------------------------------------------------------------------------- source data
def read_sources():
    s = load_workbook(SRC_SENT, data_only=True); d = load_workbook(SRC_DM, data_only=True)
    by = s["By Year"]; th = s["Themes by Year"]; sp = s["Scored Posts"]; notes = s["Notes"]
    years = {}
    for r in range(4, 8):
        years[int(by.cell(r, 1).value)] = dict(all=by.cell(r, 2).value, topic=by.cell(r, 3).value)
    themes = []
    for r in range(5, 13):
        themes.append((th.cell(r, 1).value, [th.cell(r, c).value for c in range(2, 6)]))
    patterns = {notes.cell(r, 1).value: notes.cell(r, 2).value for r in range(1, 17) if notes.cell(r, 1).value}
    churn_re = re.compile(r"cancel|unsubscrib|switch(?:ed|ing)? to (?:apple|tidal|youtube|deezer|qobuz|amazon)|goodbye spotify|leaving spotify|moved to (?:apple|tidal|youtube)", re.I)
    posts = []
    hdr = [c.value for c in sp[1]]
    for row in sp.iter_rows(min_row=2, values_only=True):
        if row[0] is None: continue
        text = str(row[2]) if row[2] is not None else ""
        posts.append(dict(date=row[0], sub=row[1], text=text[:150], up=row[3], sent=row[4], pn=row[5], pu=row[6], pp=row[7],
                          themes=list(row[8:16]), link=row[16],
                          removed=1 if re.search(r"\[removed\]|\[deleted\]", text) else 0, churn=1 if churn_re.search(text) else 0))
    theme_names = hdr[8:16]
    cl = d["Campaign lifts"]
    camps = []
    for r in list(range(5, 12)) + [20, 21]:
        v = [cl.cell(r, c).value for c in range(1, 17)]
        camps.append(dict(month=v[0], label=v[1], src=v[2], songs=v[3], during=v[4], prior=v[5], listeners=v[10], new=v[11], intent=v[12], gained=v[13], reported=v[14], note=v[15]))
    en = d["Engagement"]
    overall = [(en.cell(r, 2).value, en.cell(r, 3).value, en.cell(r, 5).value) for r in range(13, 17)]
    oo = d["On-off cases"]
    onoff = [[oo.cell(r, c).value for c in range(1, 8)] for r in range(5, 11)]
    ap = d["Artist pairs"]
    pairs = [[ap.cell(r, c).value for c in (1, 3, 4, 6, 7, 10, 11)] for r in range(5, 23)]
    size = [[ap.cell(r, c).value for c in range(1, 5)] for r in range(34, 37)]
    ref = d["Reference"]
    corpus = [(ref.cell(r, 1).value, ref.cell(r, 2).value) for r in range(4, 15)]
    lifts = [ref.cell(r, 2).value for r in range(18, 31)]
    intents = [ref.cell(r, 2).value for r in range(34, 45)]
    dmshare = [(ref.cell(r, 1).value, ref.cell(r, 2).value) for r in range(48, 56)]
    return dict(years=years, themes=themes, theme_names=theme_names, patterns=patterns, posts=posts, camps=camps, overall=overall,
                onoff=onoff, pairs=pairs, size=size, corpus=corpus, lifts=lifts, intents=intents, dmshare=dmshare)

# ----------------------------------------------------------------------------- build
def build():
    S = read_sources()
    wb = Workbook(); wb.properties.creator = "SPOT"; wb.properties.lastModifiedBy = "SPOT"
    A = {}   # absolute refs to inputs
    IN = q(SH_IN)

    # ======================================================================= DM Inputs
    ws = wb.active; ws.title = SH_IN; setup(ws, "Discovery Mode & Marketplace Assumptions"); w = Writer(ws)
    rr = w.row("Case selector (repoint to Valuation!$C$3 when the tabs are added to the model)", ["Base"],
               "Drives the FY'26E-FY'27E paths in section E. Bear = adverse for SPOT (autoplay surfaces shrink, enrollment capped, Marquee flat); Bull = the street-style continuation.", fmt=None)
    ws[f"C{rr}"].fill = GOLD; A["case"] = f"{IN}$C${rr}"; sel = A["case"]
    w.blank()
    w.section("A. Group revenue, €M (denominator for basis points)")
    rr = w.row("Total revenue", [15673, 17186, 19500, 21300], "FY'24-FY'25: Form 20-F (FY'25 Premium 15,350, Ad-Supported 1,836). FY'26E-FY'27E: same placeholders as the audiobook tabs; link to IS total revenue.", fmt=FM)
    for col in ["E", "F"]: ws[f"{col}{rr}"].fill = GOLD
    for col, k in zip(YC, ["rev24", "rev25", "rev26", "rev27"]): A[k] = f"{IN}${col}${rr}"
    rr = w.row("% y/y growth", ["", f"=D{rr}/C{rr}-1", f"=E{rr}/D{rr}-1", f"=F{rr}/E{rr}-1"], "Marketplace gross profit must grow at least this fast to hold its margin contribution flat.", italic=True, fmt=FP1)
    for col, k in zip(YC[1:], ["g25", "g26", "g27"]): A[k] = f"{IN}${col}${rr}"
    w.blank()
    w.section("B. Reported gross margin and reference points")
    rr = w.row("Consolidated gross margin", [0.301, 0.320, 0.332, 0.345], "FY'24: 30.1% (Q1-Q4 27.6/29.2/31.1/32.2 weighted). FY'25: 32.0% (20-F; Q4 33.1%). FY'26E-FY'27E: consensus placeholders, link to the consensus tab.", fmt=FP1)
    for col in ["E", "F"]: ws[f"{col}{rr}"].fill = GOLD
    for col, k in zip(YC, ["gm24", "gm25", "gm26c", "gm27c"]): A[k] = f"{IN}${col}${rr}"
    rr = w.row("Premium gross margin", [0.33, 0.34], "20-F: 29% FY'23, 33% FY'24, 34% FY'25; Q2-26 35%. Discovery Mode accrues almost entirely here ('music royalty costs net of certain marketplace programs').", fmt=FP0)
    rr = w.row("Latest quarter: Q2-26 reported (FY'26E col) and Q3-26 guided (FY'27E col)", ["", "", 0.334, 0.329], "Q2-26 letter: 33.4%, +193 bp y/y; Q3-26 guide 32.9% on €5.0bn revenue.", fmt=FP1)
    rr = w.row("2030 target: gross margin, low end (FY'24 col) and high end (FY'25 col)", [0.35, 0.40], "Investor Day 21 May 2026: 35-40% gross margin by 2030, mid-teens revenue CAGR, operating margin above 20%.", fmt=FP0)
    A["t_lo"] = f"{IN}$C${rr}"; A["t_hi"] = f"{IN}$D${rr}"
    rr = w.row("Consensus y/y gross-margin expansion, bp (context)", ["", "", 120, 130], "Placeholders: 33.2% vs 32.0% and ~34.5% vs 33.2%. Link to the consensus tab (same cells as the audiobook tabs).", fmt=FBP)
    for col in ["E", "F"]: ws[f"{col}{rr}"].fill = GOLD
    A["cons26"] = f"{IN}$E${rr}"; A["cons27"] = f"{IN}$F${rr}"
    rr = w.row("Non-marketplace y/y gross-margin expansion, bp (pricing, audiobooks, podcasts, ad mix)", ["", "", 100, 80], "Placeholder so the illustrative path on the bridge lands near H1-26 actuals (33.0-33.4%) and the Q3 guide under the Base case. Replace with the model's own GM build excluding marketplace.", fmt=FBP)
    for col in ["E", "F"]: ws[f"{col}{rr}"].fill = GOLD
    A["oth26"] = f"{IN}$E${rr}"; A["oth27"] = f"{IN}$F${rr}"
    w.blank()
    w.section("C. Marketplace disclosures (Discovery Mode + Marquee + Showcase), €M")
    rr = w.row("Marketplace gross profit contribution, 2021", [160], "Investor Day 8 Jun 2022: 'more than €160 million' in 2021 (under €20 million in 2018). Treated as the floor.", fmt=FM); A["mk21"] = f"{IN}$C${rr}"
    rr = w.row("Marketplace gross profit, 2025 as a multiple of 2021", [4.0], "Investor Day 21 May 2026: 2025 marketplace gross profit was four times 2021. Implies a ~41% CAGR 2021-25.", fmt=FMULT); A["mult"] = f"{IN}$C${rr}"
    rr = w.row("Marketplace gross profit, €M", [f"={A['mk21']}*{A['mult']}^(3/4)", f"={A['mk21']}*{A['mult']}"], "FY'25 = 2021 x multiple (floor). FY'24 is not disclosed: interpolated at the 2021-25 CAGR, so the FY'25 y/y effect on the bridge is an estimate.", fmt=FM)
    A["mk24"] = f"{IN}$C${rr}"; A["mk25"] = f"{IN}$D${rr}"
    rr = w.row("Discovery Mode share of marketplace gross profit (FY'25 col)", ["", 0.80], "KEY LEVER. Not disclosed. Marquee/Showcase are booked as Ad-Supported revenue and that whole segment earned only €330M of gross profit in FY'25 (20-F), which caps them at roughly €150-250M and puts Discovery Mode at 60-80% of marketplace. Used in 'DM share' calibration mode to solve the enrolled share on the bridge; ignored in 'Measured s' mode.", fmt=FP0)
    ws[f"D{rr}"].fill = YELLOW; A["dmsh"] = f"{IN}$D${rr}"
    rr = w.row("Calibration mode, FY'25: 'DM share' solves s from the share above; 'Measured s' solves the share from the measured s in section E", ["", "DM share"],
               "The FY'25 identity D = pool x e x s x discount has one free variable. Type exactly 'DM share' or 'Measured s'. Never overwrite the solved cell on the bridge (D12): that breaks the identity and makes FY'25 look like a decline against FY'24.", fmt=None)
    ws[f"D{rr}"].fill = GOLD; A["mode"] = f"{IN}$D${rr}"
    w.blank()
    w.section("D. Music royalty pool, €M (the pool the Discovery Mode discount is taken from)")
    rr = w.row("Royalties paid to music rights holders", [9250, 10100, f"={A['rev26']}*$D${w.r+2}", f"={A['rev27']}*$D${w.r+2}"], "Loud & Clear: $10bn in 2024 and $11bn in 2025, converted at ~1.08 / ~1.09. After all discounts, so the pre-discount pool is ~3% higher. FY'26E-FY'27E scale with revenue at the FY'25 ratio (royalties are the greater of a % of revenue and per-subscriber minimums).", fmt=FM)
    for col, k in zip(YC, ["pool24", "pool25", "pool26", "pool27"]): A[k] = f"{IN}${col}${rr}"
    rp = rr
    rr = w.row("   as % of total revenue", [f"=C{rp}/{A['rev24']}", f"=D{rp}/{A['rev25']}", f"=E{rp}/{A['rev26']}", f"=F{rp}/{A['rev27']}"], italic=True, fmt=FP1)
    assert rr == rp + 1
    w.blank()
    w.section("E. Discovery Mode structural levers")
    rr = w.row("DM royalty discount on DM-context streams", [0.30, 0.30, 0.30, 0.30], "Program term: the rights holder accepts a 30% lower royalty on streams served in Radio, Autoplay and (from Jan 2024) Mixes. Set a lower FY'27E value to model a claw-back at the major-label renewals.", fmt=FP0)
    for col, k in zip(YC, ["d24", "d25", "d26", "d27"]): A[k] = f"{IN}${col}${rr}"
    FDELTA = '+0.0%;-0.0%;0.0%'
    rr = w.row("e: share of all streams served from DM-eligible surfaces (Radio + Autoplay + Mixes), FY'25", ["", 0.33], "KEY LEVER (Topic 3). Not disclosed. The 2018 prospectus put Spotify-programmed listening at ~30% before Autoplay became default-on and before Smart Shuffle and the Mixes expansion; Spotify says 33% of discoveries happen in algorithmic contexts. Range 25-35%. 'Autoplay growth' moves this lever.", fmt=FP0)
    ws[f"D{rr}"].fill = YELLOW; A["e25"] = f"{IN}$D${rr}"; e25row = rr
    rr_e = w.row("e, FY'26E-FY'27E (active case) = FY'25 + case change below", ["", "", None, None], "Bull: autoplay / programmed listening keeps gaining share and new surfaces (Smart Shuffle, DJ sessions) are added. Base: slow drift (Reddit mentions of autoplay/recs peaked in 2025; DJ/Smart Shuffle discussion halved since 2024; Smart Shuffle removable from Apr-25). Bear: no growth, or surfaces lose share (users disable autoplay, AI-slop clean-up trims recommendation volume). Case rows are changes vs FY'25 in points.", fmt=FP1)
    eb, ebase, ebu = rr_e + 1, rr_e + 2, rr_e + 3
    for col in ["E", "F"]:
        c = ws[f"{col}{rr_e}"]; c.value = f'=$D${e25row}+IF({sel}="Bear",{col}{eb},IF({sel}="Bull",{col}{ebu},{col}{ebase}))'; c.font = F_TXT; c.alignment = CENTER; c.number_format = FP1; c.fill = GOLD
    for name, vals, bd in [("Bear", [0.0, 0.01], Border(left=THIN, top=THIN)), ("Base", [0.005, 0.01], Border(left=THIN)), ("Bull", [0.015, 0.02], Border(left=THIN, bottom=THIN))]:
        r2 = w.row(name, ["", "", vals[0], vals[1]], fmt=FDELTA); ws[f"B{r2}"].border = bd
    A["e26"] = f"{IN}$E${rr_e}"; A["e27"] = f"{IN}$F${rr_e}"
    A["e_rows"] = dict(Bear=eb, Base=ebase, Bull=ebu)
    rr = w.row("Measured s, FY'25: enrolled share of eligible-surface streams from sampling (used only in 'Measured s' mode)", ["", 0.33], "Spotify burner-account method (tools/dm_autoplay): share of tracks served in Autoplay / Radio sessions that are Discovery Mode-enrolled, weighted by plays. Enter the sampled figure here and switch the calibration mode in section C; the bridge then back-solves the DM share of marketplace.", fmt=FP1)
    A["smeas"] = f"{IN}$D${rr}"
    rr = w.row("s: enrolled share of eligible-surface streams, FY'25 (active)", ["", f"='{SH_BR}'!$D$12"], "KEY LEVER (Topic 2). In 'DM share' mode this is solved on the bridge: s = Discovery Mode gross profit / (pool x e x discount). In 'Measured s' mode it is the measured figure above. Do not type over this cell or bridge D12.", fmt=FP1)
    ws[f"D{rr}"].fill = YELLOW; A["s25"] = f"{IN}$D${rr}"; s25row = rr
    rr_s = w.row("s, FY'26E-FY'27E (active case) = FY'25 + case change below", ["", "", None, None], "Bull: enrollment keeps rising. Base: creeps up because staying in is defensive (opting out cut radio/autoplay streams 50-70% in the charted cases) even as the lift fades. Bear: flat to down (label pushback, Congressional scrutiny, lifts too small to justify 30%). Case rows are changes vs FY'25 in points, so they stay valid whichever calibration mode is on.", fmt=FP1)
    sb, sbase, sbu = rr_s + 1, rr_s + 2, rr_s + 3
    for col in ["E", "F"]:
        c = ws[f"{col}{rr_s}"]; c.value = f'=$D${s25row}+IF({sel}="Bear",{col}{sb},IF({sel}="Bull",{col}{sbu},{col}{sbase}))'; c.font = F_TXT; c.alignment = CENTER; c.number_format = FP1; c.fill = GOLD
    for name, vals, bd in [("Bear", [-0.01, -0.005], Border(left=THIN, top=THIN)), ("Base", [0.0, 0.01], Border(left=THIN)), ("Bull", [0.01, 0.025], Border(left=THIN, bottom=THIN))]:
        r2 = w.row(name, ["", "", vals[0], vals[1]], fmt=FDELTA); ws[f"B{r2}"].border = bd
    A["s26"] = f"{IN}$E${rr_s}"; A["s27"] = f"{IN}$F${rr_s}"
    A["s_rows"] = dict(Bear=sb, Base=sbase, Bull=sbu)
    rr_m = w.row("Marquee + Showcase gross profit growth, % y/y (active case)", ["", "", None, None], "Marquee (sponsored recommendation, CPC) and Showcase (home banner) sold to labels; near-100% margin Ad-Supported revenue. Bull +20% (extends 2021-25); Base +10% (below revenue growth, so a small drag in bp); Bear flat.", fmt=FP0)
    mb, mbase, mbu = rr_m + 1, rr_m + 2, rr_m + 3
    for col in ["E", "F"]:
        c = ws[f"{col}{rr_m}"]; c.value = f'=IF({sel}="Bear",{col}{mb},IF({sel}="Bull",{col}{mbu},{col}{mbase}))'; c.font = F_TXT; c.alignment = CENTER; c.number_format = FP0; c.fill = GOLD
    for name, vals, bd in [("Bear", [0.0, 0.0], Border(left=THIN, top=THIN)), ("Base", [0.10, 0.10], Border(left=THIN)), ("Bull", [0.20, 0.20], Border(left=THIN, bottom=THIN))]:
        r2 = w.row(name, ["", "", vals[0], vals[1]], fmt=FP0); ws[f"B{r2}"].border = bd
    A["mq26"] = f"{IN}$E${rr_m}"; A["mq27"] = f"{IN}$F${rr_m}"
    A["m_rows"] = dict(Bear=mb, Base=mbase, Bull=mbu)
    w.blank()
    w.row("Colour key: blue = hard-coded input (notes give source or derivation); light gold = forecast assumption, case-driven cell or placeholder to link to the model; yellow = key lever; black = formula.", label_font=F_I)

    # ======================================================================= DM GM Bridge
    bs = wb.create_sheet(SH_BR); setup(bs, "Discovery Mode & Marketplace Gross Margin Bridge"); b = Writer(bs); BR = q(SH_BR); R = {}
    b.row("€ in millions unless stated.  M = D + Q:  D = Discovery Mode royalty discount retained (a reduction of cost of revenue),  Q = Marquee and Showcase gross profit (Ad-Supported revenue).  Discovery Mode reallocates a fixed pool of Radio / Autoplay / Mixes slots; it does not create streams, so D = pool x e x s x discount whether or not the artist gains.", label_font=F_I)
    b.blank()
    b.section("1. Calibration at FY'25 (values in the FY'25 column)")
    R["mk"] = b.row("Marketplace gross profit (disclosed: 4x 2021)", [f"={A['mk24']}", f"={A['mk25']}"], "FY'24 interpolated, FY'25 floor; see inputs section C.", fmt=FM)
    R["dmsh"] = b.row("Discovery Mode share of marketplace gross profit (input in 'DM share' mode; solved in 'Measured s' mode)", ["", f"=IF({A['mode']}=\"Measured s\",IF(D{R['mk']}=0,0,{A['pool25']}*{A['e25']}*{A['smeas']}*{A['d25']}/D{R['mk']}),{A['dmsh']})"], "Calibration mode is set on the inputs tab (section C). FY'24 uses the same share, so both years sit on one definition.", fmt=FP0)
    R["D25"] = b.row("D: Discovery Mode gross profit", [f"=C{R['mk']}*D{R['dmsh']}", f"=D{R['mk']}*D{R['dmsh']}"], "FY'24 at the same share: estimate.", fmt=FM)
    R["Q25"] = b.row("Q: Marquee + Showcase gross profit", [f"=C{R['mk']}-C{R['D25']}", f"=D{R['mk']}-D{R['D25']}"], fmt=FM)
    R["poole"] = b.row("Royalty pool on eligible surfaces = pool x e", ["", f"={A['pool25']}*{A['e25']}"], fmt=FM)
    assert b.r + 1 == 12, b.r   # inputs tab links s25 to bridge D12
    R["s25"] = b.row("s: enrolled share of eligible-surface streams = D / (pool x e x discount), or the measured figure", ["", f"=IF({A['mode']}=\"Measured s\",{A['smeas']},IF(D{R['poole']}*{A['d25']}=0,0,D{R['D25']}/(D{R['poole']}*{A['d25']})))"], "Topic 2 of the triangulation matrix. Solved cell: do not type over it. Above 100% means the DM share or e is set too high.", bold=True, fill=YELLOW, box=True, fmt=FP1)
    R["exs"] = b.row("DM-context enrolled streams as a share of all streams = e x s", ["", f"={A['e25']}*D{R['s25']}"], "'Share of streams via Discovery Mode' as the calls will phrase it.", fmt=FP1)
    R["ceil"] = b.row("Ceiling: D at 100% enrollment of today's surfaces", ["", f"=D{R['poole']}*{A['d25']}"], fmt=FM)
    R["run"] = b.row("Remaining runway at today's surfaces and discount, €M", ["", f"=D{R['ceil']}-D{R['D25']}"], "The whole remaining Discovery Mode lever, before any new surface or a bigger discount.", fmt=FM)
    R["runbp"] = b.row("   as bp of FY'25 revenue", ["", f"=D{R['run']}/{A['rev25']}*10000"], italic=True, fmt=FBP)
    b.blank()
    b.section("2. Discovery Mode Gross Profit (D)")
    R["e"] = b.row("e: eligible-surface share of streams", ["", f"={A['e25']}", f"={A['e26']}", f"={A['e27']}"], "FY'26E-FY'27E follow the case selector on the inputs tab.", fmt=FP1)
    R["s"] = b.row("s: enrolled share of eligible-surface streams", ["", f"=D{R['s25']}", f"={A['s26']}", f"={A['s27']}"], fmt=FP1)
    R["es"] = b.row("   e x s: enrolled DM-context streams, share of all streams", ["", f"=D{R['e']}*D{R['s']}", f"=E{R['e']}*E{R['s']}", f"=F{R['e']}*F{R['s']}"], italic=True, fmt=FP1)
    R["pool"] = b.row("Music royalty pool", [f"={A['pool24']}", f"={A['pool25']}", f"={A['pool26']}", f"={A['pool27']}"], fmt=FM)
    R["d"] = b.row("DM royalty discount", [f"={A['d24']}", f"={A['d25']}", f"={A['d26']}", f"={A['d27']}"], fmt=FP0)
    R["D"] = b.row("D: Discovery Mode gross profit = pool x e x s x discount", [f"=C{R['D25']}", f"=D{R['pool']}*D{R['es']}*D{R['d']}", f"=E{R['pool']}*E{R['es']}*E{R['d']}", f"=F{R['pool']}*F{R['es']}*F{R['d']}"],
                   "FY'24 from the marketplace estimate (section 1); FY'25 reproduces the calibration by construction.", bold=True, top=True, fmt=FM)
    b.blank()
    b.section("3. Marquee + Showcase Gross Profit (Q)")
    R["qg"] = b.row("% y/y Growth", ["", f"=D{R['Q25']}/C{R['Q25']}-1", f"={A['mq26']}", f"={A['mq27']}"], "FY'25 implied by the interpolation; FY'26E-FY'27E follow the case selector.", italic=True, fmt=FP0)
    rq = b.r + 1
    R["Q"] = b.row("Q: Marquee + Showcase gross profit", [f"=C{R['Q25']}", f"=D{R['Q25']}", f"=D{rq}*(1+E{R['qg']})", f"=E{rq}*(1+F{R['qg']})"], bold=True, top=True, fmt=FM)
    b.blank()
    b.section("4. Marketplace Contribution to Gross Profit and Gross Margin")
    R["D2"] = b.row("D: Discovery Mode gross profit", [f"={c}{R['D']}" for c in YC], fmt=FM)
    R["Q2"] = b.row("Q: Marquee + Showcase gross profit", [f"={c}{R['Q']}" for c in YC], fmt=FM)
    R["M"] = b.row("Marketplace Contribution to Gross Profit (M)", [f"={c}{R['D2']}+{c}{R['Q2']}" for c in YC], "Level. Already inside reported FY'24-FY'25 gross profit; for the forecast use the y/y effect row below, not this level.", bold=True, fill=YELLOW, box=True, fmt=FM)
    R["rev"] = b.row("Total Revenue", [f"={A[k]}" for k in ["rev24", "rev25", "rev26", "rev27"]], fmt=FM)
    R["Mbp"] = b.row("% Contribution to Gross Margin, bp", [f"={c}{R['M']}/{c}{R['rev']}*10000" for c in YC], "Level: what marketplace does to gross margin in each year versus no marketplace.", italic=True, fmt=FBP)
    R["dM"] = b.row("Y/y Change in Contribution, €M", ["", f"=D{R['M']}-C{R['M']}", f"=E{R['M']}-D{R['M']}", f"=F{R['M']}-E{R['M']}"], fmt=FM)
    R["eff"] = b.row("Y/y Gross Margin Effect, bp", ["", f"=D{R['Mbp']}-C{R['Mbp']}", f"=E{R['Mbp']}-D{R['Mbp']}", f"=F{R['Mbp']}-E{R['Mbp']}"],
                     "Add to the model's y/y gross-margin expansion from other drivers (negative = drag). FY'25 is an estimate of what marketplace contributed to the +190 bp reported; management says about a third of expansion came from the music business.", bold=True, fill=YELLOW, box=True, fmt=FBP)
    R["effD"] = b.row("   of which Discovery Mode (change in D), bp", ["", f"=(D{R['D2']}/D{R['rev']}-C{R['D2']}/C{R['rev']})*10000", f"=(E{R['D2']}/E{R['rev']}-D{R['D2']}/D{R['rev']})*10000", f"=(F{R['D2']}/F{R['rev']}-E{R['D2']}/E{R['rev']})*10000"], italic=True, fmt=FBP)
    R["effQ"] = b.row("   of which Marquee + Showcase (change in Q), bp", ["", f"=D{R['eff']}-D{R['effD']}", f"=E{R['eff']}-D{R['effD']}", f"=F{R['eff']}-F{R['effD']}"], italic=True, fmt=FBP)
    bs[f"E{R['effQ']}"].value = f"=E{R['eff']}-E{R['effD']}"
    R["mg"] = b.row("Implied marketplace gross profit growth, % y/y", ["", f"=D{R['M']}/C{R['M']}-1", f"=E{R['M']}/D{R['M']}-1", f"=F{R['M']}/E{R['M']}-1"], "2021-25 disclosed CAGR ~41%.", fmt=FP0)
    R["need"] = b.row("Growth needed to hold the contribution flat = revenue growth, % y/y", ["", f"={A['g25']}", f"={A['g26']}", f"={A['g27']}"], "Gross margin is a ratio: a marketplace growing slower than this is a drag in bp while still growing in euros.", italic=True, fmt=FP1)
    R["cons"] = b.row("Consensus y/y gross-margin expansion, bp (context)", ["", "", f"={A['cons26']}", f"={A['cons27']}"], fmt=FBP)
    b.row("Marketplace effect as % of consensus expansion (context)", ["", "", f"=IF(E{R['cons']}=0,0,E{R['eff']}/E{R['cons']})", f"=IF(F{R['cons']}=0,0,F{R['eff']}/F{R['cons']})"], "Positive = marketplace supplies that share of the expansion the Street expects; negative = it eats into it.", italic=True, fmt=FP0)
    b.blank()
    b.section("5. Illustrative gross-margin path (context; replace the non-marketplace placeholder with the model's own build)")
    R["gmr"] = b.row("Reported (FY'24-FY'25) / consensus (FY'26E-FY'27E) gross margin", [f"={A['gm24']}", f"={A['gm25']}", f"={A['gm26c']}", f"={A['gm27c']}"], fmt=FP1)
    R["oth"] = b.row("Non-marketplace y/y expansion, bp (placeholder from inputs)", ["", "", f"={A['oth26']}", f"={A['oth27']}"], fmt=FBP)
    rg = b.r + 1
    R["gmi"] = b.row("Illustrative gross margin = prior year + non-marketplace + marketplace effect", [f"={A['gm24']}", f"={A['gm25']}", f"=D{rg}+(E{R['oth']}+E{R['eff']})/10000", f"=E{rg}+(F{R['oth']}+F{R['eff']})/10000"], bold=True, top=True, fmt=FP1)
    b.row("   Gap to consensus, bp", ["", "", f"=(E{R['gmi']}-E{R['gmr']})*10000", f"=(F{R['gmi']}-F{R['gmr']})*10000"], italic=True, fmt=FBP)
    b.row("   Reference: 2030 target range", [f"={A['t_lo']}", f"={A['t_hi']}"], "Low end in the FY'24 column, high end in the FY'25 column; direction marker only.", italic=True, fmt=FP0)
    b.blank()
    b.section("6. The three cases side by side (computed from the scenario rows on the inputs tab; independent of the selector)")
    CASE = {}
    for name in ["Bull", "Base", "Bear"]:
        er, sr, mr = A["e_rows"][name], A["s_rows"][name], A["m_rows"][name]
        rD = b.row(f"{name}: D, Discovery Mode gross profit", [f"=C{R['D']}", f"=D{R['D']}", f"=E{R['pool']}*(D{R['e']}+{IN}$E${er})*(D{R['s']}+{IN}$E${sr})*E{R['d']}", f"=F{R['pool']}*(D{R['e']}+{IN}$F${er})*(D{R['s']}+{IN}$F${sr})*F{R['d']}"], fmt=FM)
        rQ = b.row(f"{name}: Q, Marquee + Showcase gross profit", [f"=C{R['Q']}", f"=D{R['Q']}", f"=D{b.r+1}*(1+{IN}$E${mr})", f"=E{b.r+1}*(1+{IN}$F${mr})"], fmt=FM)
        rM = b.row(f"{name}: M = D + Q", [f"={c}{rD}+{c}{rQ}" for c in YC], fmt=FM)
        rE = b.row(f"{name}: y/y gross margin effect, bp", ["", f"=D{R['eff']}", f"=(E{rM}/E{R['rev']}-D{rM}/D{R['rev']})*10000", f"=(F{rM}/F{R['rev']}-E{rM}/E{R['rev']})*10000"], bold=True, fmt=FBP)
        rG = b.row(f"{name}: illustrative gross margin", [f"={A['gm24']}", f"={A['gm25']}", f"=D{b.r+1}+(E{R['oth']}+E{rE})/10000", f"=E{b.r+1}+(F{R['oth']}+F{rE})/10000"],
                   {"Bull": "Surfaces and enrollment both keep rising; marketplace keeps adding margin.",
                    "Base": "What the two datasets describe: slow drift in surfaces, enrollment creeping up because staying in is defensive; marketplace roughly neutral to slightly positive for the margin path.",
                    "Bear": "Enrollment slips and Marquee stalls; marketplace becomes a drag because it grows slower than revenue."}[name], bold=True, top=True, fmt=FP1)
        CASE[name] = dict(D=rD, Q=rQ, M=rM, E=rE, G=rG)
        if name != "Bear": b.blank()
    R["case"] = CASE

    # ======================================================================= DM Sensitivity
    se = wb.create_sheet(SH_SE); setup(se, "Discovery Mode Sensitivities", years=["", "", "", ""], widths={"A": 8.9, "B": 46, **{get_column_letter(i): 12 for i in range(3, 11)}}, notes_col=None, spare=())
    se.freeze_panes = "A4"; s = Writer(se, notes_col="J")
    s.row("FY'27E Discovery Mode contribution to gross margin, bp, for e (rows) x s (columns). Uses the FY'27E royalty pool, discount and revenue from the bridge. Compare with the FY'25 level at the bottom.", label_font=F_I)
    rr = s.row("e  \\  s", label_font=F_B)
    s_vals = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]; e_vals = [0.12, 0.15, 0.18, 0.21, 0.24]
    for j, sv in enumerate(s_vals): gridcell(se, f"{get_column_letter(3+j)}{rr}", sv, FP0, bold=True, inp=True, border=Border(bottom=THIN))
    for ev in e_vals:
        r2 = s.row(None); gridcell(se, f"B{r2}", ev, FP0, inp=True, align=LEFT)
        for j in range(len(s_vals)):
            col = get_column_letter(3 + j)
            gridcell(se, f"{col}{r2}", f"={BR}$F${R['pool']}*$B{r2}*{col}${rr}*{BR}$F${R['d']}/{BR}$F${R['rev']}*10000", FBP)
    s.row("FY'25 Discovery Mode contribution, bp (bridge)", [f"={BR}D{R['D']}/{BR}D{R['rev']}*10000"], fmt=FBP)
    s.row("FY'25 e and s (bridge)", [f"={BR}D{R['e']}", f"={BR}D{R['s']}"], fmt=FP1)
    s.row("Reading: each 10 pt of enrolled share is worth pool x e x 10% x discount / revenue (roughly 55 bp in FY'27E at e = 33%); with e and s flat the lever adds nothing further in bp. Cells beyond s = 100% are impossible.", label_font=F_I)
    s.blank()
    s.row("Implied FY'25 enrolled share s for e (rows) x Discovery Mode share of marketplace gross profit (columns). The expert-call answers on Topics 2 and 3 should land in one of these cells; above 100% is impossible.", label_font=F_I)
    rr2 = s.row("e  \\  DM share of marketplace GP", label_font=F_B)
    d_vals = [0.35, 0.45, 0.55, 0.65]
    for j, dv in enumerate(d_vals): gridcell(se, f"{get_column_letter(3+j)}{rr2}", dv, FP0, bold=True, inp=True, border=Border(bottom=THIN))
    for ev in e_vals:
        r2 = s.row(None); gridcell(se, f"B{r2}", ev, FP0, inp=True, align=LEFT)
        for j in range(len(d_vals)):
            col = get_column_letter(3 + j)
            gridcell(se, f"{col}{r2}", f"=IF($B{r2}*{A['d25']}=0,0,({A['mk25']}*{col}${rr2})/({A['pool25']}*$B{r2}*{A['d25']}))", FP0)
    s.blank()
    s.row("FY'27E y/y marketplace gross margin effect, bp, for the active case with e (rows) x s (columns) in FY'27E; Q and FY'26E held at the active case.", label_font=F_I)
    rr3 = s.row("e  \\  s", label_font=F_B)
    for j, sv in enumerate(s_vals): gridcell(se, f"{get_column_letter(3+j)}{rr3}", sv, FP0, bold=True, inp=True, border=Border(bottom=THIN))
    for ev in e_vals:
        r2 = s.row(None); gridcell(se, f"B{r2}", ev, FP0, inp=True, align=LEFT)
        for j in range(len(s_vals)):
            col = get_column_letter(3 + j)
            gridcell(se, f"{col}{r2}", f"=(({BR}$F${R['pool']}*$B{r2}*{col}${rr3}*{BR}$F${R['d']}+{BR}$F${R['Q']})/{BR}$F${R['rev']}-{BR}$E${R['Mbp']}/10000)*10000", FBP)

    # ======================================================================= DM Data Scored Posts
    sp = wb.create_sheet(SH_SP)
    sp.sheet_view.showGridLines = False
    hdrs = ["Date", "Year", "Subreddit", "Post text (title. body; first 150 chars)", "Upvotes", "Sentiment", "P(negative)", "P(neutral)", "P(positive)"] + list(S["theme_names"]) + ["Removed / deleted (1 = yes)", "Cancel / switch language (1 = yes)", "Reddit link"]
    widths = [8.9, 12, 7, 11, 60, 9, 11, 10, 10, 10] + [12] * 8 + [12, 12, 36]
    for i, wd in enumerate(widths): sp.column_dimensions[get_column_letter(i + 1)].width = wd
    sp["B2"] = "Scored autoplay / recommendation posts, r/spotify + r/truespotify (random sample of up to 1,000 per year, 2023 - Oct 1 2026)"
    for i, h in enumerate(hdrs):
        col = get_column_letter(2 + i)
        c = sp[f"{col}3"]; c.value = h; c.font = F_B; c.fill = BAND; c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")
        sp[f"{col}2"].fill = NAVY; sp[f"{col}2"].font = F_HDR
    sp.row_dimensions[3].height = 45; sp.freeze_panes = "A4"
    for i, p in enumerate(S["posts"]):
        r = 4 + i
        vals = [p["date"], f"=YEAR(B{r})", p["sub"], p["text"], p["up"], p["sent"], p["pn"], p["pu"], p["pp"]] + p["themes"] + [p["removed"], p["churn"], p["link"]]
        for j, v in enumerate(vals):
            col = get_column_letter(2 + j); c = sp[f"{col}{r}"]; c.value = v
            c.font = F_TXT if (isinstance(v, str) and v.startswith("=")) else F_IN
            if j == 0: c.number_format = FDATE
            elif j in (6, 7, 8): c.number_format = FX
            elif j == 4: c.number_format = FM
    SP_FIRST, SP_LAST = 4, 3 + len(S["posts"])
    SPR = lambda col: f"{q(SH_SP)}${col}${SP_FIRST}:${col}${SP_LAST}"
    YEARCOL, TEXTCOL, SENTCOL, REMCOL, CHURNCOL = "C", "E", "G", "S", "T"
    THEMECOL = {name: get_column_letter(11 + i) for i, name in enumerate(S["theme_names"])}

    # ======================================================================= DM Data Sentiment
    ds = wb.create_sheet(SH_DS); setup(ds, "Autoplay & Recommendation Discussion on Reddit, by Year", years=CAL); d = Writer(ds); DS = q(SH_DS); DSR = {}
    d.row("Every post in r/spotify and r/truespotify, Jan 2023 - Oct 1 2026 (210,365 posts; Arctic Shift archive; posts only, no comments). Topic posts match the filter in the notes column below and are at least 20 characters. 2026 covers Jan 1 - Oct 1 and the archive thins out after June.", label_font=F_I)
    d.blank()
    d.section("A. Corpus by year (full population)")
    yrs = [2023, 2024, 2025, 2026]
    DSR["all"] = d.row("All posts", [S["years"][y]["all"] for y in yrs], "Counts from the archive.", fmt=FM)
    DSR["topic"] = d.row("Posts about autoplay / recommendations", [S["years"][y]["topic"] for y in yrs], "Topic filter: " + S["patterns"].get("Pattern: Topic filter", ""), fmt=FM)
    DSR["topicsh"] = d.row("   share of all posts", [f"={c}{DSR['topic']}/{c}{DSR['all']}" for c in YC], italic=True, fmt=FP1)
    d.blank()
    d.section("B. Themes by year (keyword patterns on topic posts; a post can carry several themes)")
    DSR["theme"] = {}
    for name, counts in S["themes"]:
        rr = d.row(name, counts, "Pattern: " + S["patterns"].get("Pattern: " + name, ""), fmt=FM)
        rs = d.row("   share of topic posts", [f"={c}{rr}/{c}{DSR['topic']}" for c in YC], italic=True, fmt=FP1)
        DSR["theme"][name] = dict(n=rr, share=rs)
    d.blank()
    d.section(f"C. Scored sample (COUNTIFS on '{SH_SP}'; cardiffnlp/twitter-roberta-base-sentiment-latest, overall tone)")
    def cnt(y, *pairs):
        crit = "".join(f",{SPR(col)},{val}" for col, val in pairs)
        return f"=COUNTIFS({SPR(YEARCOL)},{y}{crit})"
    DSR["n"] = d.row("Posts scored", [cnt(y) for y in yrs], fmt=FM)
    DSR["neg"] = d.row("Negative", [cnt(y, (SENTCOL, '"negative"')) for y in yrs], fmt=FM)
    DSR["neu"] = d.row("Neutral", [cnt(y, (SENTCOL, '"neutral"')) for y in yrs], fmt=FM)
    DSR["pos"] = d.row("Positive", [cnt(y, (SENTCOL, '"positive"')) for y in yrs], fmt=FM)
    DSR["negsh"] = d.row("Share negative, all scored posts", [f"={c}{DSR['neg']}/{c}{DSR['n']}" for c in YC], fmt=FP1)
    DSR["possh"] = d.row("Share positive, all scored posts", [f"={c}{DSR['pos']}/{c}{DSR['n']}" for c in YC], fmt=FP1)
    DSR["net"] = d.row("Net sentiment, pp (positive minus negative share)", [f"=({c}{DSR['pos']}-{c}{DSR['neg']})/{c}{DSR['n']}*100" for c in YC], fmt=F1)
    DSR["rem"] = d.row("Removed / deleted posts in sample (title only)", [cnt(y, (REMCOL, 1)) for y in yrs], "Post body shows [removed] or [deleted]; the model scores the title alone.", fmt=FM)
    DSR["remneg"] = d.row("   of which negative", [cnt(y, (REMCOL, 1), (SENTCOL, '"negative"')) for y in yrs], fmt=FM)
    DSR["remsh"] = d.row("   share negative among removed / deleted", [f"=IF({c}{DSR['rem']}=0,0,{c}{DSR['remneg']}/{c}{DSR['rem']})" for c in YC], italic=True, fmt=FP1)
    DSR["intneg"] = d.row("Share negative, intact posts only", [f"=({c}{DSR['neg']}-{c}{DSR['remneg']})/({c}{DSR['n']}-{c}{DSR['rem']})" for c in YC], "The cleaner series: removed posts score ~21% negative vs ~40% for intact ones and were a quarter of the 2023 sample.", fmt=FP1)
    DSR["churn"] = d.row("Posts with cancel / switch language", [cnt(y, (CHURNCOL, 1)) for y in yrs], "Regex: cancel | unsubscrib | switch(ed|ing) to (apple|tidal|youtube|deezer|qobuz|amazon) | goodbye spotify | leaving spotify | moved to (apple|tidal|youtube). Flag computed in Python from the full post text.", fmt=FM)
    DSR["churnsh"] = d.row("   share of scored posts", [f"={c}{DSR['churn']}/{c}{DSR['n']}" for c in YC], italic=True, fmt=FP1)
    d.blank()
    d.subhdr(["Share negative within theme (scored posts carrying the theme)", *CAL])
    DSR["tneg"] = {}; DSR["tn"] = {}
    for name in S["theme_names"]:
        col = THEMECOL[name]
        rn = d.row(f"{name}: posts in sample", [cnt(y, (col, '"Yes"')) for y in yrs], fmt=FM)
        rs = d.row("   share negative", [f"=IF({c}{rn}=0,0,COUNTIFS({SPR(YEARCOL)},{y},{SPR(col)},\"Yes\",{SPR(SENTCOL)},\"negative\")/{c}{rn})" for c, y in zip(YC, yrs)], italic=True, fmt=FP1)
        DSR["tn"][name] = rn; DSR["tneg"][name] = rs
    name = "Discovery love"; col = THEMECOL[name]
    DSR["lovepos"] = d.row(f"{name}: share positive", [f"=IF({c}{DSR['tn'][name]}=0,0,COUNTIFS({SPR(YEARCOL)},{y},{SPR(col)},\"Yes\",{SPR(SENTCOL)},\"positive\")/{c}{DSR['tn'][name]})" for c, y in zip(YC, yrs)], "The pro-recommendation pocket: stable at ~1-2% of topic posts, mostly positive.", fmt=FP1)
    d.blank()
    d.row("Caveats: keyword themes are approximate ('radio', 'the DJ' match unrelated uses); the model scores overall tone, not tone toward the algorithm, and misreads sarcasm; counts are from the archive and fall with subreddit activity, so use shares. Reproduce: autoplay.py -> export_autoplay_excel.py (earlier session).", label_font=F_I)

    # ======================================================================= DM Data Campaigns
    dc = wb.create_sheet(SH_DC)
    hdr_c = ["Campaign", "Month", "Source (r/musicmarketing id)", "Songs enrolled", "DM-context streams, campaign", "DM-context streams, prior 28 days", "Reported lift", "Era", "Campaign listeners", "New listeners", "Saves + adds per listener", "Songs that gained", "Songs reported", "Note"]
    cols_c = [get_column_letter(i) for i in range(2, 2 + len(hdr_c))]   # B..O
    setup(dc, "Spotify for Artists Campaign Reports: Discovery Mode-context Streams, Before vs During", years=[], year_cols=[], notes_col="O",
          widths={"A": 8.9, "B": 24, "C": 11, "D": 16, "E": 10, "F": 13, "G": 13, "H": 11, "I": 10, "J": 12, "K": 11, "L": 13, "M": 10, "N": 10, "O": 70}, spare=())
    for col, h in zip(cols_c, hdr_c):
        c = dc[f"{col}3"]; c.value = h; c.font = F_B; c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")
    dc["O3"].value = "Note"; dc.row_dimensions[3].height = 45
    DCR = {"camp": []}
    r = 4
    for cp in S["camps"]:
        vals = [cp["label"], cp["month"], cp["src"], cp["songs"], cp["during"], cp["prior"], f'=IF(G{r}="","",F{r}/G{r}-1)', f'=IF(YEAR(C{r})<=2024,"2023-24","2025-26")', cp["listeners"], cp["new"], cp["intent"], cp["gained"], cp["reported"], cp["note"]]
        for col, v in zip(cols_c, vals):
            if v is None: continue
            c = dc[f"{col}{r}"]; c.value = v
            c.font = F_TXT if (isinstance(v, str) and v.startswith("=")) else (F_I if col == "O" else F_IN)
            c.alignment = NOTE if col == "O" else (LEFT if col == "B" else CENTER)
        dc[f"C{r}"].number_format = 'mmm-yy'; dc[f"H{r}"].number_format = FMULT; dc[f"L{r}"].number_format = FP2
        for col in "EFGJK": dc[f"{col}{r}"].number_format = FM
        DCR["camp"].append(r); r += 1
    first7 = DCR["camp"][:7]
    r += 1
    def crow(label, vals, fmt, bold=False, top=False, note=None):
        nonlocal r
        c = dc[f"B{r}"]; c.value = label; c.font = F_B if bold else F_TXT
        for col, v in vals.items():
            cc = dc[f"{col}{r}"]; cc.value = v; cc.font = F_B if bold else F_TXT; cc.alignment = CENTER; cc.number_format = fmt
            if top: cc.border = Border(top=THIN)
        if top: dc[f"B{r}"].border = Border(top=THIN)
        if note: n = dc[f"O{r}"]; n.value = note; n.font = F_I; n.alignment = NOTE
        rr = r; r += 1; return rr
    DCR["med2324"] = crow("Median reported lift, campaigns Aug 2023 - Nov 2024", {"H": f"=MEDIAN(H{first7[0]}:H{first7[3]})", "I": f'=COUNT(H{first7[0]}:H{first7[3]})&" campaigns"'}, FMULT, bold=True, top=True, note="n = 4 vs 3: not statistically meaningful (rank test p ~ 0.1) and the metric rewards songs with a tiny prior base (the 7.4x campaign had 359 prior streams). Direction, not magnitude.")
    DCR["med2526"] = crow("Median reported lift, campaigns Jan 2025 - Jul 2026", {"H": f"=MEDIAN(H{first7[4]}:H{first7[6]})", "I": f'=COUNT(H{first7[4]}:H{first7[6]})&" campaigns"'}, FMULT, bold=True)
    DCR["medall"] = crow("Median reported lift, all campaigns with a before figure", {"H": f"=MEDIAN(H{first7[0]}:H{first7[6]})"}, FMULT)
    DCR["latest"] = crow("Latest campaign lift as a share of the earliest", {"H": f"=H{first7[6]}/H{first7[0]}"}, FP0)
    DCR["intmed"] = crow("Median saves + adds per Discovery Mode listener (all campaign reports)", {"L": f"=MEDIAN(L{DCR['camp'][0]}:L{DCR['camp'][-1]})"}, FP2, bold=True, note="Spotify's own 'intent' measure for a Discovery Mode song: (saves + playlist adds) / campaign listeners.")
    r += 1
    c = dc[f"B{r}"]; c.value = "Reported lift = campaign streams / prior-28-day streams - 1. Where the screenshot showed only the lift, the prior figure is streams / (1 + lift). Counts cover Radio, Autoplay and Mixes only: they do not show whether total streams rose (the Jan 2025 artist checked: Spotify reported +55%, total streams fell). Source: screenshots posted to r/musicmarketing, read by hand."; c.font = F_I; r += 2
    # Engagement comparison
    c = dc[f"B{r}"]; c.value = "Artists' overall audience: saves per listener (Spotify for Artists dashboards)"; c.font = F_B; r += 1
    for col, h in zip(["B", "D", "L"], ["Artist", "Source", "Saves per listener"]):
        c = dc[f"{col}{r}"]; c.value = h; c.font = F_B; c.alignment = CENTER if col != "B" else LEFT; c.border = Border(bottom=THIN)
    r += 1; ov = []
    for label, src, rate in S["overall"]:
        dc[f"B{r}"].value = label; dc[f"B{r}"].font = F_TXT
        dc[f"D{r}"].value = src; dc[f"D{r}"].font = F_IN; dc[f"D{r}"].alignment = CENTER
        dc[f"L{r}"].value = rate; dc[f"L{r}"].font = F_IN; dc[f"L{r}"].alignment = CENTER; dc[f"L{r}"].number_format = FP1
        ov.append(r); r += 1
    DCR["ovmed"] = crow("Median saves per listener, overall audience", {"L": f"=MEDIAN(L{ov[0]}:L{ov[-1]})"}, FP1, bold=True, top=True, note="Saves only, 12 months, different artists: read against the campaign rate as an order of magnitude, not a like-for-like.")
    DCR["ratio"] = crow("Overall audience keeps the song this many times more often", {"L": f"=L{DCR['ovmed']}/L{DCR['intmed']}"}, F1)
    DCR["first7"] = first7; DCR["ov"] = ov
    r += 1
    # On-off cases
    c = dc[f"B{r}"]; c.value = "What happened when Discovery Mode was switched on or off (artists' own graphs)"; c.font = F_B; r += 1
    for col, h in zip(["B", "C", "D", "F", "G", "H", "O"], ["Source", "Change", "Measure", "Before", "After", "Change", "What happened"]):
        c = dc[f"{col}{r}"]; c.value = h; c.font = F_B; c.alignment = CENTER if col not in ("B", "O") else LEFT; c.border = Border(bottom=THIN)
    r += 1; oo_rows = []
    for src, chg, meas, before, after, _, what in S["onoff"]:
        for col, v in zip(["B", "C", "D", "F", "G"], [src, chg, meas, before, after]):
            if v is None: continue
            c = dc[f"{col}{r}"]; c.value = v; c.font = F_IN; c.alignment = LEFT if col == "B" else CENTER
            if col in "FG": c.number_format = FM
        dc[f"H{r}"].value = f'=IF(OR(F{r}="",G{r}=""),"",G{r}/F{r}-1)'; dc[f"H{r}"].font = F_TXT; dc[f"H{r}"].alignment = CENTER; dc[f"H{r}"].number_format = FP0
        dc[f"O{r}"].value = what; dc[f"O{r}"].font = F_I; dc[f"O{r}"].alignment = NOTE
        oo_rows.append(r); r += 1
    DCR["oo"] = oo_rows
    DCR["offavg"] = crow("Average change when switched off, the two charted radio / autoplay cases", {"H": f"=AVERAGE(H{oo_rows[2]},H{oo_rows[3]})"}, FP0, bold=True, top=True, note="Artists who stay enrolled describe it as defensive (re-enrolled out of fear; 'would not take it out again'). For a first-time enrollee the pitch has become 'pay 30% to avoid losing ground'.")
    dc.freeze_panes = "A4"
    DC = q(SH_DC)

    # ======================================================================= DM Data Artist Reports
    da = wb.create_sheet(SH_DA)
    hdr_a = ["Date posted", "Year", "Measure", "Monthly listeners at start", "Size band", "Before", "After", "Change", "Direction", "Source", "What the artist said"]
    cols_a = [get_column_letter(i) for i in range(2, 2 + len(hdr_a))]   # B..L
    setup(da, "Artists' Own Before / After Numbers and Hand-coded Corpus (r/musicmarketing, Oct 2020 - Oct 2026)", years=[], year_cols=[], notes_col="L",
          widths={"A": 8.9, "B": 12, "C": 7, "D": 22, "E": 13, "F": 11, "G": 11, "H": 11, "I": 10, "J": 10, "K": 20, "L": 70}, spare=())
    for col, h in zip(cols_a, hdr_a):
        c = da[f"{col}3"]; c.value = h; c.font = F_B; c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")
    da.row_dimensions[3].height = 45
    r = 4; pr = []
    for date, meas, mls, before, after, src, said in S["pairs"]:
        vals = [date, f"=YEAR(B{r})", meas, mls, f'=IF(E{r}="","not stated",IF(E{r}<10000,"Under 10k",IF(E{r}<50000,"10k-50k","50k+")))', before, after, f"=H{r}/G{r}-1", f'=IF(ABS(I{r})<0.05,"Flat",IF(I{r}>0,"Up","Down"))', src, said]
        for col, v in zip(cols_a, vals):
            if v is None: continue
            c = da[f"{col}{r}"]; c.value = v
            c.font = F_TXT if (isinstance(v, str) and v.startswith("=")) else (F_I if col == "L" else F_IN)
            c.alignment = NOTE if col == "L" else (LEFT if col == "D" else CENTER)
        da[f"B{r}"].number_format = FDATE
        for col in "EGH": da[f"{col}{r}"].number_format = FM
        da[f"I{r}"].number_format = FP0
        pr.append(r); r += 1
    P0, P1 = pr[0], pr[-1]; r += 1
    DAR = {}
    c = da[f"B{r}"]; c.value = "Direction by year posted (these 18 numeric pairs)"; c.font = F_B; r += 1
    for col, h in zip(["B", "D", "E", "F", "G", "H"], ["Year", "Up", "Down", "Flat", "Total", "Avg listeners at start, Down cases"]):
        c = da[f"{col}{r}"]; c.value = h; c.font = F_B; c.alignment = CENTER; c.border = Border(bottom=THIN)
    da.row_dimensions[r].height = 30; da[f"H{r}"].alignment = Alignment(horizontal="center", wrap_text=True); r += 1
    DAR["byyear"] = {}
    for y in [2023, 2024, 2025, 2026]:
        da[f"B{r}"].value = y; da[f"B{r}"].font = F_IN; da[f"B{r}"].alignment = CENTER
        for col, lab in zip("DEF", ["Up", "Down", "Flat"]):
            da[f"{col}{r}"].value = f'=COUNTIFS($C${P0}:$C${P1},B{r},$J${P0}:$J${P1},"{lab}")'; da[f"{col}{r}"].font = F_TXT; da[f"{col}{r}"].alignment = CENTER
        da[f"G{r}"].value = f"=SUM(D{r}:F{r})"; da[f"G{r}"].font = F_TXT; da[f"G{r}"].alignment = CENTER
        da[f"H{r}"].value = f'=IFERROR(AVERAGEIFS($E${P0}:$E${P1},$C${P0}:$C${P1},B{r},$J${P0}:$J${P1},"Down"),"size not stated")'; da[f"H{r}"].font = F_TXT; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FM
        DAR["byyear"][y] = r; r += 1
    c = da[f"B{r}"]; c.value = "Caveat: by year these pairs trend toward 'Up', not away from it. The 2023 losers were all 30k-80k-listener artists in the early rollout; most later winners are small artists. Read it as a change in who posts, not proof the program improved."; c.font = F_I; r += 2
    c = da[f"B{r}"]; c.value = "Direction by audience size at the start (all first-hand reports that stated a size, n = 26; hand-coded)"; c.font = F_B; r += 1
    for col, h in zip(["B", "D", "E", "F", "G", "H"], ["Size band", "Up", "Mixed / flat", "Down", "Total", "Share up"]):
        c = da[f"{col}{r}"]; c.value = h; c.font = F_B; c.alignment = CENTER; c.border = Border(bottom=THIN)
    r += 1; sz = []
    for band, up, mixed, down in S["size"]:
        da[f"B{r}"].value = band; da[f"B{r}"].font = F_IN; da[f"B{r}"].alignment = CENTER
        for col, v in zip("DEF", [up, mixed, down]): da[f"{col}{r}"].value = v; da[f"{col}{r}"].font = F_IN; da[f"{col}{r}"].alignment = CENTER
        da[f"G{r}"].value = f"=SUM(D{r}:F{r})"; da[f"H{r}"].value = f"=D{r}/G{r}"
        for col in "GH": da[f"{col}{r}"].font = F_TXT; da[f"{col}{r}"].alignment = CENTER
        da[f"H{r}"].number_format = FP0; sz.append(r); r += 1
    da[f"B{r}"].value = "10k and above"; da[f"B{r}"].font = F_B; da[f"B{r}"].alignment = CENTER
    for col in "DEFG": da[f"{col}{r}"].value = f"=SUM({col}{sz[1]}:{col}{sz[2]})"; da[f"{col}{r}"].font = F_B; da[f"{col}{r}"].alignment = CENTER; da[f"{col}{r}"].border = Border(top=THIN)
    da[f"H{r}"].value = f"=D{r}/G{r}"; da[f"H{r}"].font = F_B; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FP0; da[f"H{r}"].border = Border(top=THIN); da[f"B{r}"].border = Border(top=THIN)
    DAR["under10k"] = sz[0]; DAR["over10k"] = r; r += 2
    c = da[f"B{r}"]; c.value = "Corpus (hand-coded from 130 Discovery Mode threads and 1,953 comments; second-hand stories excluded; repeat comments by one person merged)"; c.font = F_B; r += 1
    DAR["corpus"] = {}
    for label, val in S["corpus"]:
        da[f"B{r}"].value = label; da[f"B{r}"].font = F_TXT
        da[f"H{r}"].value = val; da[f"H{r}"].font = F_IN; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FM
        DAR["corpus"][label.strip()] = r; r += 1
    fh = DAR["corpus"]["of which first-hand"]; fu = DAR["corpus"]["first-hand: streams went up"]; dw = DAR["corpus"]["First-hand reports saying Discover Weekly / algorithmic streams fell after opting in"]
    da[f"B{r}"].value = "Share of first-hand reports that went up"; da[f"B{r}"].font = F_B; da[f"H{r}"].value = f"=H{fu}/H{fh}"; da[f"H{r}"].font = F_B; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FP0; da[f"H{r}"].border = Border(top=THIN); da[f"B{r}"].border = Border(top=THIN)
    DAR["shareup"] = r; DAR["fh"] = fh; DAR["dw"] = dw; r += 2
    c = da[f"B{r}"]; c.value = "Discovery Mode share of an artist's monthly streams (as reported)"; c.font = F_B; r += 1
    for col, h in zip(["B", "D", "H", "L"], ["Source id", "Artist type", "Share", "Note"]):
        c = da[f"{col}{r}"]; c.value = h; c.font = F_B; c.alignment = CENTER if col == "H" else LEFT; c.border = Border(bottom=THIN)
    r += 1; est = []; allsh = []
    for src, val in S["dmshare"]:
        typ = "Established (500k+ monthly streams)" if val <= 0.06 else ("Range 5-15%" if val == 0.1 else "Catalog-heavy or small")
        da[f"B{r}"].value = src; da[f"B{r}"].font = F_IN
        da[f"D{r}"].value = typ; da[f"D{r}"].font = F_TXT
        da[f"H{r}"].value = val; da[f"H{r}"].font = F_IN; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FP1
        if val <= 0.06: est.append(r)
        allsh.append(r); r += 1
    da[f"B{r}"].value = "Median, established artists only"; da[f"B{r}"].font = F_B; da[f"H{r}"].value = f"=MEDIAN(H{est[0]}:H{est[-1]})"; da[f"H{r}"].font = F_B; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FP1; da[f"H{r}"].border = Border(top=THIN); da[f"B{r}"].border = Border(top=THIN)
    da[f"L{r}"].value = "The source workbook's 7.5% 'median' mixes both groups; use this for an enrolled established artist."; da[f"L{r}"].font = F_I; da[f"L{r}"].alignment = NOTE
    DAR["dmmed"] = r; DAR["est"] = est; r += 1
    da[f"B{r}"].value = "Median, all reports"; da[f"B{r}"].font = F_TXT; da[f"H{r}"].value = f"=MEDIAN(H{allsh[0]}:H{allsh[-1]})"; da[f"H{r}"].font = F_TXT; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FP1; r += 2
    c = da[f"B{r}"]; c.value = "Intent rate per song quoted by artists (saves + adds / listeners), order as extracted"; c.font = F_B; r += 1
    it = []
    for i, v in enumerate(S["intents"]):
        da[f"B{r}"].value = f"Intent {i+1}"; da[f"B{r}"].font = F_TXT; da[f"H{r}"].value = v; da[f"H{r}"].font = F_IN; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FP2; it.append(r); r += 1
    da[f"B{r}"].value = "Median"; da[f"B{r}"].font = F_B; da[f"H{r}"].value = f"=MEDIAN(H{it[0]}:H{it[-1]})"; da[f"H{r}"].font = F_B; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FP2; da[f"H{r}"].border = Border(top=THIN); da[f"B{r}"].border = Border(top=THIN)
    DAR["intmed"] = r; r += 2
    c = da[f"B{r}"]; c.value = "Spotify-reported 'stream lift' figures quoted in posts (order as extracted; undated; the list mixes multiples such as 2.77 with percentages such as 20, so no median is taken)"; c.font = F_B; r += 1
    for i, v in enumerate(S["lifts"]):
        da[f"B{r}"].value = f"Lift {i+1}"; da[f"B{r}"].font = F_TXT; da[f"H{r}"].value = v; da[f"H{r}"].font = F_IN; da[f"H{r}"].alignment = CENTER; da[f"H{r}"].number_format = FX; r += 1
    r += 1
    c = da[f"B{r}"]; c.value = "Self-selected stories: people post when results surprise. Discovery Mode's start often coincides with releases, ads or TikTok moments, and the algorithm changes over time (several artists report platform-wide drops in 2026). Not a controlled experiment; 35 screenshots read (7 deleted)."; c.font = F_I
    da.freeze_panes = "A4"
    DA = q(SH_DA)

    # ======================================================================= DM Evidence (links only)
    ev = wb.create_sheet(SH_EV); setup(ev, "What the Two Datasets Say, Mapped to the Levers", years=CAL); e = Writer(ev); EV = {}
    ev.column_dimensions["G"].width = 14
    e.row(f"Every number on this tab is a link to '{SH_DS}', '{SH_DC}' or '{SH_DA}'. Column G names the lever on the inputs tab the item informs: e = eligible-surface share (autoplay), s = enrolled share, quality = engagement of DM streams, backlash = regulatory / listener risk.", label_font=F_I)
    e.blank()
    e.section("1. Autoplay / recommendation discussion, r/spotify + r/truespotify (lever: e)")
    def L(sheet, col, row): return f"={q(sheet)}{col}{row}"
    e.row("Posts about autoplay / recommendations, share of all posts", [L(SH_DS, c, DSR["topicsh"]) for c in YC], "Rose through 2025 and slipped in 2026 YTD. Weak evidence of a plateau: the 2026 archive is thin after June and total subreddit volume is falling.", g="e", fmt=FP1)
    e.row("Posts mentioning DJ / daylist / Smart Shuffle, share of topic posts", [L(SH_DS, c, DSR["theme"]["Feature: DJ / daylist / Smart Shuffle"]["share"]) for c in YC], "The AI DJ / Smart Shuffle novelty is fading: mention share down from 20% to 14-16%, and Smart Shuffle became removable in April 2025 (959-upvote post).", g="e", fmt=FP1)
    e.row("Posts mentioning Discover Weekly / Release Radar, share of topic posts", [L(SH_DS, c, DSR["theme"]["Feature: Discover Weekly / Release Radar"]["share"]) for c in YC], g="e", fmt=FP1)
    e.row("Posts on AI-generated music, share of topic posts", [L(SH_DS, c, DSR["theme"]["AI-generated music"]["share"]) for c in YC], "From 0.3% to 4.6%. The clean-up Spotify announced in Sept 2025 (AI labels, spam filter) trims recommendation inventory: the main channel by which e could fall.", g="e (quality)", fmt=FP1)
    e.row("Posts on repetitive / same songs, share of topic posts", [L(SH_DS, c, DSR["theme"]["Repetitive / same songs"]["share"]) for c in YC], "The listener-side symptom of low-intent DM streams; rising every year.", g="quality", fmt=FP1)
    e.row("Posts on paid / pushed content (Discovery Mode, payola, sponsored), share of topic posts", [L(SH_DS, c, DSR["theme"]["Paid / pushed content"]["share"]) for c in YC], "Small but at its highest in 2026. Listeners do not see the program by name (one post in 4,000 says 'discovery mode'); they see 'sponsored recs'.", g="backlash", fmt=FP1)
    e.blank()
    e.section("2. Sentiment of the scored sample, 1,000 posts per year (lever: e, churn)")
    e.row("Share negative, headline", [L(SH_DS, c, DSR["negsh"]) for c in YC], fmt=FP1)
    e.row("Share negative, intact posts only (the cleaner series)", [L(SH_DS, c, DSR["intneg"]) for c in YC], "Removed posts score ~21% negative vs ~40% for intact ones and were 26% of the 2023 sample but 4-5% in 2025-26. On intact posts the deterioration is ~5-6 pt, not 8; still rising, 2026 H1 the worst half, 2026 Q3 back to 39%.", g="e, churn", fmt=FP1)
    e.row("Net sentiment, pp", [L(SH_DS, c, DSR["net"]) for c in YC], fmt=F1)
    e.row("Share of scored posts with cancel / switch language", [L(SH_DS, c, DSR["churnsh"]) for c in YC], "56 posts in total; directional only.", g="churn", fmt=FP1)
    e.row("Discovery love posts, share positive", [L(SH_DS, c, DSR["lovepos"]) for c in YC], "The pro-recommendation pocket is stable: the base is polarising, not uniformly souring.", fmt=FP1)
    e.row("DJ / daylist / Smart Shuffle posts, share negative", [L(SH_DS, c, DSR["tneg"]["Feature: DJ / daylist / Smart Shuffle"]) for c in YC], fmt=FP1)
    e.row("Discover Weekly / Release Radar posts, share negative", [L(SH_DS, c, DSR["tneg"]["Feature: Discover Weekly / Release Radar"]) for c in YC], fmt=FP1)
    e.blank()
    e.subhdr(["3. Discovery Mode efficacy, artist side (levers: s, quality)", "Value", "n", "", ""], g="Lever")
    f7 = DCR["first7"]; cr = DCR["camp"]; ov = DCR["ov"]
    e.row("Median Spotify-reported lift, campaigns Aug 2023 - Nov 2024", [L(SH_DC, "H", DCR["med2324"]), f"=COUNT({DC}H{f7[0]}:H{f7[3]})"], "Lift = DM-context streams in campaign / prior 28 days - 1. Direction consistent with a crowded pool; magnitude not evidence (n = 4 vs 3).", g="s", fmts=[FMULT, F0])
    e.row("Median Spotify-reported lift, campaigns Jan 2025 - Jul 2026", [L(SH_DC, "H", DCR["med2526"]), f"=COUNT({DC}H{f7[4]}:H{f7[6]})"], "Billboard reports the same fade from managers: 200-300% gains in year one, 20-30% later.", g="s", fmts=[FMULT, F0])
    e.row("Saves + playlist adds per Discovery Mode listener, median", [L(SH_DC, "L", DCR["intmed"]), f"=COUNT({DC}L{cr[0]}:L{cr[-1]})"], "Spotify's own intent metric; 0.7-4.8% per campaign, latest (Sep 2026) the lowest.", g="quality", fmts=[FP2, F0])
    e.row("Saves per listener, artists' overall audience, median", [L(SH_DC, "L", DCR["ovmed"]), f"=COUNT({DC}L{ov[0]}:L{ov[-1]})"], "Different definition, so an order of magnitude: DM streams are ~16x lower intent. They still carry a royalty, at 70%.", g="quality", fmts=[FP1, F0])
    e.row("Overall audience keeps the song this many times more often", [L(SH_DC, "L", DCR["ratio"])], g="quality", fmt=F1)
    e.row("Share of first-hand reports that went up: artists under 10k listeners", [L(SH_DA, "H", DAR["under10k"]), L(SH_DA, "G", DAR["under10k"])], "All eight small artists went up; the long tail keeps enrolling.", g="s", fmts=[FP0, F0])
    e.row("Share of first-hand reports that went up: artists 10k+ listeners", [L(SH_DA, "H", DAR["over10k"]), L(SH_DA, "G", DAR["over10k"])], "Above 10k it is a coin flip; mid-size independents are the enrollment that can leave.", g="s", fmts=[FP0, F0])
    e.row("Share of first-hand reports that went up: all", [L(SH_DA, "H", DAR["shareup"]), L(SH_DA, "H", DAR["fh"])], g="s", fmts=[FP0, F0])
    e.row("First-hand reports saying Discover Weekly / algorithmic streams fell after opting in", [L(SH_DA, "H", DAR["dw"]), L(SH_DA, "H", DAR["fh"])], "The 'suppression' complaint: enrolling may trade editorial / Discover Weekly reach for Radio / Autoplay reach.", g="s", fmts=[F0, F0])
    e.row("DM-context streams as share of an enrolled established artist's streams, median", [L(SH_DA, "H", DAR["dmmed"]), f"=COUNT({DA}H{DAR['est'][0]}:H{DAR['est'][-1]})"], "3.5-5% for 500k+ monthly-stream artists; 33-50% for catalog-heavy or tiny artists.", g="e", fmts=[FP1, F0])
    e.row("Switching Discovery Mode off: average change in radio / autoplay streams (two charted cases)", [L(SH_DC, "H", DCR["offavg"]), f"=COUNT({DC}H{DCR['oo'][2]},{DC}H{DCR['oo'][3]})"], "Enrollment has become defensive, which supports enrollment creeping up even as the lift fades: good for s, bad for the program's reputation.", g="s (defensive)", fmts=[FP0, F0])
    e.row("Artist pairs: up / down in 2023 (early rollout)", [L(SH_DA, "D", DAR["byyear"][2023]), L(SH_DA, "E", DAR["byyear"][2023])], "The 18 numeric pairs trend toward 'Up' over time (mix shift toward small artists); they cannot support the time claim either way.", g="s", fmts=[F0, F0])
    e.row("Artist pairs: up / down in 2025-26", [f"={DA}D{DAR['byyear'][2025]}+{DA}D{DAR['byyear'][2026]}", f"={DA}E{DAR['byyear'][2025]}+{DA}E{DAR['byyear'][2026]}"], g="s", fmts=[F0, F0])
    e.blank()
    e.row("Both datasets support the direction (plateauing autoplay salience, fading lift, defensive enrollment) but not magnitudes: self-selected Reddit samples, tiny n on the campaign side, a tone model that is not aspect-based. Treat them as inputs to the Base-case paths, worth about a point a year on e, and as the reason s is modelled as creeping rather than compounding.", label_font=F_I)

    order = [SH_IN, SH_BR, SH_SE, SH_EV, SH_DS, SH_SP, SH_DC, SH_DA]
    wb._sheets = [wb[n] for n in order]
    wb.active = 0
    wb.save(OUT); print("saved", OUT)

if __name__ == "__main__":
    build()
