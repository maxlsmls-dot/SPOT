import openpyxl, zipfile, io, sys
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
SRC, DST = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(SRC)
z = zipfile.ZipFile(SRC)
for ws in wb.worksheets:
    for img in getattr(ws, "_images", []):
        img.ref = io.BytesIO(z.read("xl/media/image1.jpeg"))

GF = "Garamond"
BLUE, BLACK, GREEN, NAVY = "FF0000FF", "FF000000", "FF008000", "FF002060"
def f(color=BLACK, b=False, i=False, sz=11): return Font(name=GF, size=sz, bold=b, italic=i, color=color)
YEL = PatternFill("solid", fgColor="FFFFFF00"); HDR = PatternFill("solid", fgColor="FF1F3864"); LB = PatternFill("solid", fgColor="FFDDEBF7")
thin = Side(style="thin", color="FF000000")
NUM = '#,##0.0_);[Red]\\(#,##0.0\\)'; USD = '_("$"* #,##0.00_);_("$"* \\(#,##0.00\\);_("$"* "-"??_);_(@_)'; PCT = '0.0%'; MX = '0.0"x"'

def put(ws, cell, v, font=None, fmt=None, fill=None, al=None):
    c = ws[cell]; c.value = v
    if font: c.font = font
    if fmt: c.number_format = fmt
    if fill: c.fill = fill
    if al: c.alignment = al
    return c
def hdr(ws, row, cols, labels):
    for col, lab in zip(cols, labels):
        put(ws, f"{col}{row}", lab, Font(name=GF, size=11, bold=True, color="FFFFFFFF"), fill=HDR, al=Alignment(horizontal="center"))

# ======================= 1Y Valuation
ws = wb.create_sheet("1Y Valuation", 2)
ws.sheet_view.showGridLines = False
for col, w in zip("ABCDEFGHIJKL", [2, 38, 14, 14, 14, 14, 3, 30, 12, 12, 12, 12]): ws.column_dimensions[col].width = w
put(ws, "B1", "FTAI Aviation", f(b=True, sz=14))
put(ws, "B2", "1-Year Valuation (target date Oct-27) – matches the pitch deck", f(b=True))
put(ws, "B3", "Case follows DCF!C3. NTM = Q4'27–Q3'28 ≈ ¼ FY27E + ¾ FY28E; net debt interpolated YE26E → YE27E. $ in millions except per share.", f(i=True, sz=10))

put(ws, "B5", "Case-specific multiples (EV / NTM EBITDA)", f(NAVY, b=True))
hdr(ws, 6, "BCDEF", ["Segment", "Bear", "Base", "Bull", "Active"])
mult = [("Aerospace Products", 10, 14, 16), ("FTAI Power", 8, 10, 12), ("Aviation Leasing + SCI", 8, 9, 9)]
for k, (n, b1, b2, b3) in enumerate(mult):
    r = 7 + k
    put(ws, f"B{r}", n, f())
    for col, val in zip("CDE", (b1, b2, b3)): put(ws, f"{col}{r}", val, f(BLUE), MX, YEL)
    put(ws, f"F{r}", f'=CHOOSE(MATCH(DCF!$C$3,{{"Bear","Base","Bull"}},0),C{r},D{r},E{r})', f(), MX)

put(ws, "B11", "NTM weights", f(NAVY, b=True))
put(ws, "B12", "Weight on FY27E", f()); put(ws, "C12", 0.25, f(BLUE), PCT)
put(ws, "B13", "Weight on FY28E", f()); put(ws, "C13", "=1-C12", f(), PCT)

put(ws, "B15", "Sum of the parts at Oct-27 (active case)", f(NAVY, b=True))
hdr(ws, 16, "BCDEF", ["Segment", "NTM EBITDA", "EV / EBITDA", "EV", "$ / share"])
rows = [("Aerospace Products", 14, "F7"), ("FTAI Power", 15, "F8"), ("Aviation Leasing + SCI", 16, "F9")]
for k, (n, om, m) in enumerate(rows):
    r = 17 + k
    put(ws, f"B{r}", n, f())
    put(ws, f"C{r}", f"=$C$12*'Operating Model'!E{om}+$C$13*'Operating Model'!F{om}", f(GREEN), NUM)
    put(ws, f"D{r}", f"={m}", f(), MX)
    put(ws, f"E{r}", f"=C{r}*D{r}", f(), NUM)
    put(ws, f"F{r}", f"=E{r}/DCF!$K$16", f(), USD)
put(ws, "B20", "Corporate & eliminations (at blended multiple)", f())
put(ws, "C20", "=$C$12*'Operating Model'!E17+$C$13*'Operating Model'!F17", f(GREEN), NUM)
put(ws, "D20", "=SUM(E17:E19)/SUM(C17:C19)", f(), MX)
put(ws, "E20", "=C20*D20", f(), NUM); put(ws, "F20", "=E20/DCF!$K$16", f(), USD)
put(ws, "B21", "Enterprise value", f(b=True)); put(ws, "C21", "=SUM(C17:C20)", f(b=True), NUM)
put(ws, "D21", "=E21/C21", f(b=True), MX); put(ws, "E21", "=SUM(E17:E20)", f(b=True), NUM); put(ws, "F21", "=E21/DCF!$K$16", f(b=True), USD)
put(ws, "B22", "(–) Net debt (Sep-27E)", f())
put(ws, "E22", "=-($C$12*'Operating Model'!D79+$C$13*'Operating Model'!E79)", f(GREEN), NUM); put(ws, "F22", "=E22/DCF!$K$16", f(), USD)
put(ws, "B23", "(–) Preferred equity", f()); put(ws, "E23", "=DCF!K13", f(GREEN), NUM); put(ws, "F23", "=E23/DCF!$K$16", f(), USD)
put(ws, "B24", "1-year target (equity value / share)", f(b=True)); put(ws, "E24", "=SUM(E21:E23)", f(b=True), NUM); put(ws, "F24", "=E24/DCF!$K$16", f(b=True), USD, LB)
put(ws, "B25", "Current price", f()); put(ws, "F25", "=DCF!K18", f(GREEN), USD)
put(ws, "B26", "Return", f(b=True)); put(ws, "F26", "=F24/F25-1", f(b=True), PCT, LB)
for col in "BCDEF": ws[f"{col}21"].border = Border(top=thin); ws[f"{col}24"].border = Border(top=thin)

put(ws, "B28", "Cross-checks (active case)", f(NAVY, b=True))
put(ws, "B29", "EV / NTM EBITDA today (NTM ≈ ¼ FY26E + ¾ FY27E)", f())
put(ws, "F29", "=Cover!C21/($C$12*'Operating Model'!D18+$C$13*'Operating Model'!E18)", f(), MX)
put(ws, "B30", "EV / NTM EBITDA at target", f()); put(ws, "F30", "=D21", f(), MX)
put(ws, "B31", "Target ex-Power (Power multiple = 0)", f())
put(ws, "F31", "=((E17+E19)*(1+C20/SUM(C17:C19))+E22+E23)/DCF!$K$16", f(), USD)
put(ws, "B32", "Aerospace multiple implied by today's price", f())
put(ws, "F32", "=((F25*DCF!$K$16-E22-E23)/(1+C20/SUM(C17:C19))-E18-E19)/C17", f(), MX)
put(ws, "B33", "$ / share per 1x of Aerospace multiple", f())
put(ws, "F33", "=C17*(1+C20/SUM(C17:C19))/DCF!$K$16", f(), USD)
put(ws, "B34", "Blended DCF rolled forward 1 year (– dividends)", f())
put(ws, "F34", "=DCF!N29*(1+'WACC Calculation'!B19)-C35", f(), USD)
put(ws, "B35", "Dividends next 12 months ($ / share)", f()); put(ws, "C35", 2.0, f(BLUE), USD)

put(ws, "B37", "Sensitivity: 1-year target, Aerospace × Power multiple (active case)", f(NAVY, b=True))
hdr(ws, 38, "BCDEF", ["Aero \\ Power", 6, 8, 10, 12])
for k, ma in enumerate([10, 12, 14, 16]):
    r = 39 + k
    put(ws, f"B{r}", ma, f(BLUE, b=True), MX, al=Alignment(horizontal="center"))
    for col in "CDEF":
        put(ws, f"{col}{r}", f"=(($B{r}*$C$17+{col}$38*$C$18+$D$19*$C$19)*(1+$C$20/SUM($C$17:$C$19))+$E$22+$E$23)/DCF!$K$16", f(), USD)
for col in "CDEF": ws[f"{col}38"].number_format = MX

# right side: pasted case outputs + bridge
put(ws, "H5", "Case outputs (pasted values from the case toggle)", f(NAVY, b=True))
hdr(ws, 6, "HIJK", ["", "Bear", "Base", "Bull"])
case = [("NTM adj. EBITDA ($M)", 1562.1, 2843.4, 3402.0, NUM), ("1-year target ($ / share)", 113.52, 309.32, 429.94, USD),
        ("Return vs. $167.03", -0.320, 0.852, 1.574, PCT), ("Probability", 0.2, 0.6, 0.2, PCT)]
for k, (n, a, b, c, fm) in enumerate(case):
    r = 7 + k
    put(ws, f"H{r}", n, f())
    for col, val in zip("IJK", (a, b, c)): put(ws, f"{col}{r}", val, f(BLUE), fm)
put(ws, "H11", "Probability-weighted target", f(b=True)); put(ws, "J11", "=SUMPRODUCT(I8:K8,I10:K10)", f(b=True), USD)
put(ws, "H12", "Probability-weighted return", f()); put(ws, "J12", "=J11/F25-1", f(), PCT)
put(ws, "H13", "Reward / risk (bull up / bear down)", f(b=True)); put(ws, "J13", "=K9/-I9", f(b=True), MX)

put(ws, "H15", "Value bridge by thesis (base multiples)", f(NAVY, b=True))
hdr(ws, 16, "HIJ", ["Step", "$ / share", "Cumulative"])
bridge = [("Bear-case outcomes (≈ today's $167)", 161.2), ("+ Thesis I: margins (margin, PMA, pass-through, escalator, inventory)", 22.3),
          ("+ Thesis II: share (retirements, SV rates, share, SCI fleet, leasing)", 62.4), ("+ Thesis III: Power (units, JV share, margin)", 63.4)]
for k, (n, val) in enumerate(bridge):
    r = 17 + k
    put(ws, f"H{r}", n, f())
    put(ws, f"I{r}", val, f(BLUE), USD)
    put(ws, f"J{r}", f"=SUM($I$17:I{r})", f(), USD)
put(ws, "H21", "Base-case 1-year target", f(b=True)); put(ws, "J21", "=J20", f(b=True), USD)
put(ws, "H22", "Method: starting from the Bear case, each thesis's Assumptions bear rows were set to base values in order (I → II → III) and the SOTP re-run at base multiples. Order-dependent; values pasted.", f(i=True, sz=9))
ws["H22"].alignment = Alignment(wrap_text=True, vertical="top"); ws.merge_cells("H22:L25")

# ======================= Diligence
wd = wb.create_sheet("Diligence", 3)
wd.sheet_view.showGridLines = False
for col, w in zip("ABCDEFGH", [2, 44, 12, 12, 14, 16, 60, 3]): wd.column_dimensions[col].width = w
put(wd, "B1", "FTAI Aviation", f(b=True, sz=14))
put(wd, "B2", "Diligence summary behind the Thesis II assumptions (search-based, Oct-26; counts are a floor)", f(b=True))

r = 4
put(wd, f"B{r}", "1. CFM56 Outsourcing Flip Tracker – 14 tier-1 engine shops", f(NAVY, b=True)); r += 1
hdr(wd, r, "BCDEF", ["Shop type", "Reviewed", "Add LEAP", "Pull back CFM56", "Win outside CFM56"]); r += 1
for n, a, b, c, d in [("Airline-owned", 8, 8, 1, 3), ("OEM network", 2, 2, 1, 2), ("Independent", 4, 4, 0, 4)]:
    put(wd, f"B{r}", n, f())
    for col, val in zip("CDEF", (a, b, c, d)): put(wd, f"{col}{r}", val, f(BLUE), "0", al=Alignment(horizontal="center"))
    r += 1
put(wd, f"B{r}", "Total", f(b=True))
for col in "CDEF": put(wd, f"{col}{r}", f"=SUM({col}{r-3}:{col}{r-1})", f(b=True), "0", al=Alignment(horizontal="center"))
r += 1
for t in ["OEMs: all new sites LEAP-only; CFM gives up Ryanair CFM56 labor from 2029 (keeps parts).",
          "First airline flip: Lufthansa Group sends own CFM56 to FL Technics (Oct-26). EVA Air → MTU (May-26); United → FTAI CFM56-7B MRE (Oct-26).",
          "Counter: Korean Air keeps CFM56, outsources LEAP; independents also add CFM56 (overflow is real but contested)."]:
    put(wd, f"B{r}", "• " + t, f(sz=10)); r += 1
r += 1
put(wd, f"B{r}", "2. Test Cell Tracker – 18 engine test cells", f(NAVY, b=True)); r += 1
hdr(wd, r, "BC", ["Category", "Cells"]); r += 1
for n, v in [("Existing cells adapted to test LEAP (incl. 1 likely)", 9), ("…still testing CFM56, where disclosed", "4 of 4"), ("…dropped CFM56", 0),
             ("New cells built for LEAP", 7), ("New cell built first for CFM56 (Willis Lease + GEM)", 1), ("Unknown (LHT Hamburg, StandardAero)", 2)]:
    put(wd, f"B{r}", n, f()); put(wd, f"C{r}", v, f(BLUE), al=Alignment(horizontal="center")); r += 1
put(wd, f"B{r}", "• 'Ongoing shortage of testing capacity' – Willis Lease; 'Europe-wide testing capacity constraints' – SR Technics. LEAP shares cells; no cell dropped CFM56.", f(sz=10)); r += 2

put(wd, f"B{r}", "3. Retirements, fuel and OEM capacity – evidence vs. model inputs", f(NAVY, b=True)); r += 1
hdr(wd, r, "BCDEFG", ["Evidence", "Value", "", "Model input", "Model value", "Read-across"]); r += 1
ev = [
    ("GE 2026 CFM56 retirements (actual, Sep-26)", "1.5–2.0%", "FY26 retirement -7B / -5B", "=TEXT(Assumptions!F10,\"0.0%\")&\" / \"&TEXT(Assumptions!F15,\"0.0%\")", "Consistent – base retained"),
    ("GE view of 2027 retirements", "~3%", "FY27 retirement -7B / -5B", "=TEXT(Assumptions!K10,\"0.0%\")&\" / \"&TEXT(Assumptions!K15,\"0.0%\")", "Base ~2.2% blended is below GE's ~3%; GE has cut its view four times. Bear (2.5% / 4.0%) covers GE's number"),
    ("GE CFM56 shop visits 2026 / 2027", "~2,400 / ~2,400", "Total shop visits FY26 / FY27", "=TEXT(RPM!L26,\"#,##0\")&\" / \"&TEXT(RPM!Q26,\"#,##0\")", "Consistent – base retained"),
    ("Jet fuel peak (IATA, 3-Apr-26) / 15-Sep-26", "$209 / $198 bbl", "Retirement rates", "No change", "Parked CFM56s down since March; 2022 analog shows no retirement spike"),
    ("FTAI 2026 module guide", "1,200", "FTAI modules FY26E", "=TEXT(RPM!L42,\"#,##0\")", "Consistent – base retained"),
    ("Mgmt share of CFM56 market (Q2'26)", "14%", "3rd-party share FY27E (base)", "=TEXT(Assumptions!K46,\"0.0%\")", "Tracker shows OEM / airline work moving to independents; base ramp retained, bull 25%"),
    ("GE LEAP internal shop visits (Q2'26)", "+50% y/y", "—", "—", "OEM growth capacity going to LEAP"),
    ("OEM share of LEAP vs. CFM56 shop visits", "~85% vs. ~1/3", "—", "—", "Two-thirds of CFM56 work already with independents"),
]
for e in ev:
    put(wd, f"B{r}", e[0], f(sz=10)); put(wd, f"C{r}", e[1], f(BLUE, sz=10)); put(wd, f"E{r}", e[2], f(sz=10))
    put(wd, f"F{r}", e[3], f(GREEN if str(e[3]).startswith("=") else BLACK, sz=10)); put(wd, f"G{r}", e[4], f(sz=10))
    wd[f"G{r}"].alignment = Alignment(wrap_text=True, vertical="top"); r += 1
r += 1
put(wd, f"B{r}", "Conclusion: the new diligence confirms the base-case Thesis II inputs; no driver changes were needed. Valuation updated to the 1-year framework on '1Y Valuation'.", f(b=True, sz=10))
r += 1
put(wd, f"B{r}", "Sources: Flip Tracker and Test Cell Tracker workbooks (Oct-26); GE Aerospace (Q2'26, MS Laguna Sep-26, Reuters Jul-26); IATA / Platts; Safran H1'26; CFM; FTAI Q2'26.", f(i=True, sz=9))

# ======================= Cover additions
wc = wb["Cover"]
put(wc, "B29", "1-Year Valuation (Oct-27)", f(b=True))
for k, (lab, frm, fm) in enumerate([("1-year target (active case)", "='1Y Valuation'!F24", USD), ("Return", "='1Y Valuation'!F26", PCT),
                                     ("Probability-weighted target", "='1Y Valuation'!J11", USD), ("Reward / risk", "='1Y Valuation'!J13", MX)]):
    put(wc, f"B{30+k}", lab, f()); put(wc, f"C{30+k}", frm, f(GREEN), fm)

wb.save(DST)
print("saved", DST)
