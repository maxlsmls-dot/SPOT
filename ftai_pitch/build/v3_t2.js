const G = require("./g");
const { C, F } = G;

const ax = { catAxisLabelFontFace: F, valAxisLabelFontFace: F, catAxisLabelFontSize: 9.5, valAxisLabelFontSize: 9, catAxisLabelColor: "262626", valAxisLabelColor: "262626",
  dataLabelFontFace: F, dataLabelFontSize: 9, legendFontFace: F, legendFontSize: 9, catGridLine: { style: "none" }, valGridLine: { style: "none" }, catAxisLineColor: "7F7F7F",
  titleFontFace: F, titleFontSize: 10.5, titleColor: "262626", showTitle: true };

function tbl(s, hdr, rows, x, y, w, colW, o = {}) {
  const sz = o.size || 10.5;
  const H = hdr.map((t) => ({ text: t, options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontFace: F, fontSize: sz, align: "center" } }));
  s.addTable([H, ...rows.map((r, i) => r.map((c, j) => ({ text: G.parse(String(c), { fontFace: F, fontSize: sz, color: C.TXT }),
    options: { align: j === 0 ? "left" : (o.leftAll ? "left" : "center"), fill: { color: o.hiRow === i ? "FBE5D6" : (i % 2 ? "F2F2F2" : C.WHITE) } } })))],
    { x, y, w, colW, rowH: o.rowH || 0.22, border: { type: "solid", pt: 0.5, color: "BFBFBF" }, margin: [1, 3, 1, 3] });
}
const vline = (s, x, y, h) => s.addShape("line", { x, y, w: 0, h, line: { color: C.TXT, width: 1, dashType: "sysDot" } });

// ======================= SLIDE 1: CFM56 keeps flying
async function slide1(pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "Thesis II: Variance on CFM56 Life – LEAP Can't Replace It and Fuel Hasn't Moved It");
  const X = 0.68, W = 12.25, L = 0.68, LW = 6.35, R = 7.18, RW = 5.75;

  // ---- top tier: outsourcing flip tracker (14 tier-1 shops)
  G.head(s, "Every tier-1 shop is adding LEAP; OEMs are trimming CFM56, independents are catching it, and Lufthansa now sends its own out.", X, 0.88, W, { size: 13 });
  tbl(s, ["Shops (14)", "Reviewed", "Add LEAP", "Pull back", "Win CFM56", "Pulling back on CFM56", "Holding CFM56", "Adding CFM56"], [
    ["**OEM network**", "2", "2", "1", "2", "GE / CFM, Safran", "–", "–"],
    ["**Airline-owned**", "8", "8", "1", "3", "Lufthansa", "AFI KLM, Delta, Iberia (planned), Turkish (exploring), Korean Air", "–"],
    ["**Independent**", "4", "4", "–", "4", "–", "–", "MTU, StandardAero, ST Engineering, SR Technics, **FTAI**"],
  ], L, 1.26, W, [1.35, 0.75, 0.75, 0.75, 0.8, 2.05, 3.0, 2.8], { rowH: 0.3, size: 9.5 });
  G.para(s, "**++CFM56 work flows from OEMs and airline shops to independents++**^^1^^", L, 2.5, W, 0.24, { size: 10.5, align: "center", color: C.ORANGE });
  G.bullets(s, [
    "**OEMs:** all new sites ++LEAP-only++ (Brazil, India, Mexico, Belgium); CFM ++gives up Ryanair CFM56 labor from 2029++ – its largest CFM56 account – keeping only parts",
    "**First airline flip:** Lufthansa Group sends its ++own CFM56 to FL Technics++ (Oct-26) as Hamburg turns LEAP",
  ], L, 2.78, 6.0, 0.98, { size: 10.5, psa: 2 });
  G.bullets(s, [
    "**Moving to independents:** EVA Air → MTU (first non-OEM, May-26); ++United → FTAI++ CFM56-7B MRE (Oct-26)",
    "**Counter:** Korean Air keeps CFM56, outsources LEAP; independents add CFM56 too – ++overflow is real, but contested++",
  ], L + 6.25, 2.78, 6.0, 0.98, { size: 10.5, psa: 2 });

  // ---- bottom tier: fuel
  G.head(s, "Bears fear the 2026 fuel shock accelerates retirements – the data shows parked CFM56s falling, not rising.", X, 3.84, W, { size: 13.5 });
  s.addChart(pres.charts.BAR, [{ name: "Jet fuel", labels: ["Jan-26", "3-Apr (peak)", "17-Apr", "14-Aug", "15-Sep"], values: [85, 209, 185, 159, 198] }],
    { x: L, y: 4.24, w: 3.1, h: 2.18, barDir: "col", chartColors: [C.ORANGE], barGapWidthPct: 40, showValue: true, dataLabelPosition: "outEnd",
      dataLabelColor: "262626", dataLabelFormatCode: "$0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 240, showLegend: false, ...ax, catAxisLabelFontSize: 8.5, title: "Jet Fuel ($ / bbl)" });
  s.addChart(pres.charts.BAR, [{ name: "Retirement", labels: ["Original", "Jan-26", "Spring", "Sep-26"], values: [0.035, 0.025, 0.02, 0.0175] }],
    { x: L + 3.2, y: 4.24, w: 3.15, h: 2.18, barDir: "col", chartColors: ["A6A6A6", "A6A6A6", "A6A6A6", C.NAVY], barGapWidthPct: 40, showValue: true, dataLabelPosition: "outEnd",
      dataLabelColor: "262626", dataLabelFormatCode: "0.0%", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 0.042, showLegend: false, ...ax, catAxisLabelFontSize: 8.5, title: "GE CFM56 Retirement View, 2026" });
  vline(s, R - 0.12, 4.26, 2.15);
  G.bullets(s, [
    "**Parked CFM56s down since March:** “no meaningful change in customer behavior” – GE CEO, Jul-26; Safran H1 spares up ++27.9%++ on CFM56; Q1 retirements <1%",
    "**Airlines trimmed growth and hedged, not parked:** United –5%, Delta –3.5% growth; Ryanair ++80% hedged at ~$67++",
    "**Replacing an NG on fuel alone** breaks even only at a sustained ++$170–200 / bbl++ – and needs a slot that isn't there^^3^^",
    "**History:** 2022 fuel +95–150%, retirements only ++325 vs. 502 in 2019++",
  ], R, 4.24, RW, 1.62, { size: 10.5, psa: 1 });
  s.addShape("rect", { x: R, y: 5.88, w: RW, h: 0.52, fill: { color: C.GRAY }, line: { color: C.GRAY } });
  G.para(s, "**Bear watch:** all-type retirements +15% in 9M26 (low base), Spirit's ~57 A320ceos back to lessors, GE sees ~3% in 2027 – retirements also ++feed FTAI's feedstock++", R + 0.04, 5.88, RW - 0.08, 0.52, { size: 10, valign: "middle" });

  G.banner(s, "LEAP can't replace the CFM56 before 2027–28 and fuel hasn't moved retirements: demand holds at ~2,400 visits a year.", X, 6.48, W, 0.44, 14);
  G.source(s, "GPS CFM56 Outsourcing Flip Tracker (14 tier-1 shops, Oct-26), Company Releases, GE / Safran, IATA / Platts, Aviation Week",
    ["Tracker: public releases, filings, trade press; not exhaustive (a floor).", "Fuel: IATA / Platts avg.; Jan, 15-Sep USGC.", "GPS est.: 15% fuel saving vs. $2–2.6M / yr MAX lease premium."]);
}

// ======================= SLIDE 2: FTAI wins the whitespace
async function slide2(pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "Thesis II: Variance on Share – FTAI Fills the Whitespace With Capacity Already Built");
  const X = 0.68, W = 12.25, L = 0.68, LW = 6.0, R = 6.93, RW = 6.0;

  // ---- top tier: why FTAI wins
  G.head(s, "FTAI takes the CFM56 visits the LEAP-focused shops can\u2019t turn fast enough: an engine back in weeks, not months.", X, 0.88, W, { size: 13.5 });
  s.addChart(pres.charts.BAR, [{ name: "Days", labels: ["Shop visit", "FTAI swap"], values: [150, 15] }],
    { x: L, y: 1.28, w: 1.95, h: 1.72, barDir: "col", chartColors: ["A6A6A6", C.ORANGE], barGapWidthPct: 45, showValue: true, dataLabelPosition: "outEnd", dataLabelColor: "262626",
      dataLabelFormatCode: "0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 180, showLegend: false, ...ax, title: "Days Off Wing" });
  G.para(s, "**++Test cells: LEAP now shares CFM56's scarcest slot++**^^1^^", L + 2.05, 1.26, LW - 2.05, 0.24, { size: 10.5, align: "center" });
  tbl(s, ["Engine test cells tracked (18)", "Cells"], [
    ["Existing cells adapted to test LEAP", "**9**"], ["...still testing CFM56 (where disclosed)", "4 of 4"], ["...dropped CFM56", "**0**"],
    ["New cells built for LEAP", "7"], ["New cell built first for CFM56 (Willis + GEM)", "**1**"],
  ], L + 2.05, 1.5, LW - 2.05, [3.15, 0.8], { rowH: 0.2, size: 9 });
  G.para(s, "\u201C++Ongoing shortage of testing capacity++\u201D – Willis Lease; \u201CEurope-wide testing capacity constraints\u201D – SR Technics", L + 2.05, 2.72, LW - 2.05, 0.36, { size: 9, color: C.MUTE });
  tbl(s, ["Edge", "FTAI", "OEM / large MRO shops"], [
    ["Feedstock", "1,000+ owned engines; run-outs; AAR USM", "OEM parts at list (+6% / yr)"],
    ["Parts", "PMA (3 of 5), USM, in-house repair", "HPT blade shortage; OEM parts only"],
    ["Slots", "~1,800 spare modules (2026)", "Waits +2–6 mo.; capex to LEAP"],
    ["Test", "Rome adding a cell; Jakarta, Cairo come with cells", "LEAP competes for same cells"],
  ], L, 3.1, LW, [0.95, 2.8, 2.25], { rowH: 0.21, size: 9.5 });
  vline(s, R - 0.12, 1.3, 2.85);
  G.para(s, "**++FTAI's share of CFM56 module demand++**", R, 1.26, RW, 0.26, { size: 12, align: "center" });
  s.addChart(pres.charts.LINE, [
    { name: "Incl. SCI captive", labels: ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E"], values: [0.167, 0.236, 0.285, 0.312, 0.332] },
    { name: "Third-party only (base)", labels: ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E"], values: [0.124, 0.168, 0.19, 0.195, 0.2] },
  ], { x: R, y: 1.5, w: 3.6, h: 2.65, chartColors: [C.ORANGE, C.NAVY], lineSize: 2.25, lineDataSymbol: "circle", lineDataSymbolSize: 6, showValue: true, dataLabelPosition: "t",
    dataLabelColor: "262626", dataLabelFormatCode: "0%", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 0.4, showLegend: true, legendPos: "b", ...ax, showTitle: false });
  G.bullets(s, [
    "**Proof:** share ~10% → 12% → ++14%++ in 1H26; Q2 modules up ++61% y/y++",
    "**Guide raised twice:** 1,000 → 1,050 → ++1,200++ (2026); ++1,700++ in 2027",
    "**United** expanded to a multi-year ++CFM56-7B MRE++ (Oct-26)",
    "Bull case: third-party alone reaches ++25%++ by FY31",
  ], R + 3.65, 1.52, RW - 3.65, 2.62, { size: 10.5, psa: 3, valign: "middle" });

  // ---- bottom tier: capacity built
  G.head(s, "The capex is already spent: 3,000 modules of capacity vs. 1,200 produced, with Jakarta and Cairo adding volume in 2027.", X, 4.2, W, { size: 13.5 });
  s.addChart(pres.charts.BAR, [
    { name: "Modules produced", labels: ["2025\n757", "2026E\n1,200", "2027E\n1,700"], values: [757, 1200, 1700] },
    { name: "Spare capacity", labels: ["2025\n757", "2026E\n1,200", "2027E\n1,700"], values: [1243, 1800, 1300] },
  ], { x: L, y: 4.6, w: 2.4, h: 1.82, barDir: "col", barGrouping: "stacked", chartColors: [C.NAVY, "BDD7EE"], barGapWidthPct: 40, showValue: false, valAxisHidden: true, showLegend: true, legendPos: "b", ...ax, title: "Output vs. Capacity^^2^^".replace("^^2^^", "") });
  tbl(s, ["Shop", "Role"], [
    ["Montreal / Miami", "Core module shops"], ["Rome", "QuickTurn; adding test cell"], ["Lisbon", "+113k sq ft; 300+ modules"],
    ["**Jakarta (GMF)**", "**Heavy repair; 200+ techs; 5-yr deal (Sep-26)**"], ["**Cairo (EgyptAir)**", "**-7B; ~120 techs; test cell**"],
  ], L + 2.5, 4.62, LW - 2.5, [1.25, 2.25], { rowH: 0.27, size: 9.5 });
  vline(s, R - 0.12, 4.62, 1.8);
  const alg = [["2,386", "visits"], ["× 3", "modules"], ["× 16.8%", "3rd-party share"], ["+ 482", "SCI"], ["= 1,687", "FY27E"]];
  alg.forEach((a, i) => {
    const x = R + i * 1.2;
    s.addShape("rect", { x, y: 4.62, w: 1.12, h: 0.62, fill: { color: i === 4 ? C.NAVY : "F2F2F2" }, line: { color: i === 4 ? C.NAVY : "F2F2F2" } });
    s.addText([{ text: a[0], options: { bold: true, fontSize: 13, breakLine: true } }, { text: a[1], options: { fontSize: 9 } }],
      { x, y: 4.62, w: 1.12, h: 0.62, align: "center", valign: "middle", fontFace: F, color: i === 4 ? C.WHITE : C.TXT, margin: 0, isTextBox: true });
  });
  G.bullets(s, [
    "**Partner-funded growth:** Jakarta and Cairo are ++partner shops with guaranteed capacity++ – volume adds need working capital, not new buildings",
    "**Each +1 pt of third-party share** ≈ 70 modules ≈ ++$65M EBITDA ≈ $10 / share++ at 16x",
    "**Downside covered:** independents (StandardAero, ST Eng., SRT, MTU) also chase the overflow; our bear case caps share at ++15%++ and still yields ++$173++",
  ], R, 5.3, RW, 1.1, { size: 10.5, psa: 2 });

  G.banner(s, "With slots built and partners funding new shops, FTAI reaches ~25% of CFM56 module demand; each point of share is ~$10 / share.", X, 6.48, W, 0.44, 14);
  G.source(s, "FTAI Calls and Supplement, United / FTAI (Oct-26), GMF / FTAI (Sep-26), Willis Lease, SR Technics, In Practise, GPS Model",
    ["GPS Test Cell Tracker (18 cells, Oct-26); no public case of a cell dropping CFM56 for LEAP.", "Physical capacity 2,000 (2025) and 3,000 modules (from Q2'26) per management."]);
}

module.exports = async function (pres) { await slide1(pres); await slide2(pres); };
