const G = require("./g");
const { C, F } = G;

const ax = { catAxisLabelFontFace: F, valAxisLabelFontFace: F, catAxisLabelFontSize: 9.5, valAxisLabelFontSize: 9, catAxisLabelColor: "262626", valAxisLabelColor: "262626",
  dataLabelFontFace: F, dataLabelFontSize: 9, legendFontFace: F, legendFontSize: 9, catGridLine: { style: "none" }, valGridLine: { style: "none" }, catAxisLineColor: "7F7F7F",
  titleFontFace: F, titleFontSize: 10.5, titleColor: "262626", showTitle: true };

function tbl(s, hdr, rows, x, y, w, colW, o = {}) {
  const sz = o.size || 10.5;
  const H = hdr.map((t) => ({ text: t, options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontFace: F, fontSize: sz, align: "center" } }));
  s.addTable([H, ...rows.map((r, i) => r.map((c, j) => ({ text: G.parse(String(c), { fontFace: F, fontSize: sz, color: C.TXT }),
    options: { align: j === 0 ? "left" : "center", fill: { color: o.hi === j ? "FBE5D6" : (i % 2 ? "F2F2F2" : C.WHITE) } } })))],
    { x, y, w, colW, rowH: o.rowH || 0.22, border: { type: "solid", pt: 0.5, color: "BFBFBF" }, margin: [1, 3, 1, 3] });
}
const sub = (s, t, x, y, w) => G.para(s, `**++${t}++**`, x, y, w, 0.26, { size: 12, align: "center" });

// ======================= SLIDE 1: <8% + heavy scope
async function slide1(pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "Thesis I: Variance on Margins – The Unwind Is Done and Heavy Mix Has Peaked");
  const X = 0.68, W = 12.25, L = 0.68, LW = 6.35, R = 7.18, RW = 5.75;

  // ---- top tier
  G.head(s, "Bears read the 1H26 reset as the fraud unwinding; the 10-Qs show leasing-sourced stock is <8% of inventory.", X, 0.88, W, { size: 13.5 });
  G.quote(s, "“AP inventory has been largely comprised of depreciated Leasing Equipment”, producing margins ~10 pts above peers. – Muddy Waters, Jan-25", L, 1.28, LW, 0.48, { size: 11 });
  G.bullets(s, [
    "**Small:** Q1'26 leasing-to-inventory transfers were ++$89.6M vs. ~$1.4bn of inventory (6.4%)++, down from 10.5% a year earlier as purchased feedstock scaled",
    "**Reversing:** ++$169M moved back++ from inventory to leasing in 1H26 for rebuild and sale – more than came in",
    "**Shrinking source:** leasing equipment fell ++$2.06bn → $1.53bn++ (Dec-25 → Jun-26) as aircraft are sold into SCI",
    "**Bought at market:** new feedstock comes from ++United run-outs++ (Oct-26 MRE), ++WestJet 737-700s++ (Sep-26) and AAR used parts",
    "**Already in the bear case:** 6.4% × ~40% cost edge × ~55% material ≈ ++~140 bps++ of margin^^1^^; audit review found the claims without merit",
  ], L, 1.8, LW, 2.0, { size: 11, psa: 1 });
  s.addChart(pres.charts.BAR, [
    { name: "From leasing", labels: ["Q1'25", "Q1'26"], values: [68, 90] },
    { name: "Purchased & WIP", labels: ["Q1'25", "Q1'26"], values: [577, 1310] },
  ], { x: R, y: 1.28, w: 2.82, h: 2.5, barDir: "col", barGrouping: "stacked", chartColors: [C.ORANGE, C.NAVY], barGapWidthPct: 50,
    showValue: false, valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 1750, showLegend: true, legendPos: "b", ...ax, title: "Aerospace Inventory ($M)" });
  s.addText("$645M | 10.5%", { x: R + 0.1, y: 2.2, w: 1.35, h: 0.2, align: "center", fontFace: F, fontSize: 9.5, bold: true, color: C.ORANGE, margin: 0, isTextBox: true });
  s.addText("$1.4bn | 6.4%", { x: R + 1.35, y: 1.56, w: 1.35, h: 0.2, align: "center", fontFace: F, fontSize: 9.5, bold: true, color: C.ORANGE, margin: 0, isTextBox: true });
  s.addChart(pres.charts.BAR, [
    { name: "Leasing → inv.", labels: ["1H25", "1H26"], values: [129, 85] },
    { name: "Inv. → leasing", labels: ["1H25", "1H26"], values: [160, 169] },
  ], { x: R + 2.93, y: 1.28, w: 2.82, h: 2.5, barDir: "col", chartColors: [C.ORANGE, "2E75B6"], barGapWidthPct: 45, showValue: true, dataLabelPosition: "outEnd",
    dataLabelColor: "262626", dataLabelFormatCode: "#,##0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 200, showLegend: true, legendPos: "b", ...ax, title: "Engine Transfers ($M)^^2^^".replace("^^2^^", "") });
  s.addShape("line", { x: R - 0.12, y: 1.3, w: 0, h: 2.45, line: { color: C.TXT, width: 1, dashType: "sysDot" } });

  // ---- bottom tier
  G.head(s, "With the unwind done, the reset is workscope mix – and the shift to heavy work has peaked.", X, 3.86, W, { size: 13.5 });
  G.quote(s, "~6,000-cycle engine ~40%, ~10,000-cycle ~25%, blend ~30%: “similar dollars per engine, but more investment.” – FTAI CEO, Q2'26^^2^^", L, 4.26, LW, 0.48, { size: 11 });
  G.bullets(s, [
    "**Capacity-capped:** heavy jobs need core disassembly and test cells (~50% of visits open the core); Jakarta's heavy shop only ++adds capacity from 2027++",
    "**No incentive:** heavy work was the price of ++winning airline contracts++ – United is signed (V2500 exchange, then CFM56-7B MRE), so more heavy jobs add capital, not customers",
    "**FTAI chooses:** “++supply-constrained, not demand-constrained++” (Q2'26) – it turns work away; the 2027 plan targets volume (1,700 modules), not heavier jobs",
    "**Slow fleet drift:** visits needing broader work rise only ++48% → 52% by FY30++; the 1H26 step-change was a ++one-quarter mix shift++",
  ], L, 4.78, LW, 1.62, { size: 11, psa: 1 });
  s.addChart(pres.charts.BAR, [{ name: "Margin", labels: ["~6k-cycle\n(light)", "Blend\n(1H26)", "~10k-cycle\n(heavy)"], values: [0.40, 0.30, 0.25] }],
    { x: R, y: 4.26, w: 2.82, h: 2.15, barDir: "col", chartColors: ["2E75B6", C.ORANGE, C.NAVY], barGapWidthPct: 50, showValue: true, dataLabelPosition: "outEnd",
      dataLabelColor: "262626", dataLabelFormatCode: "0%", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 0.48, showLegend: false, ...ax, title: "Margin by Workscope" });
  sub(s, "Mix back to light = margin", R + 2.93, 4.28, 2.82);
  tbl(s, ["Light share", "Margin"], [["33% (1H26)", "30.0%"], ["40%", "31.0%"], ["50%", "32.5%"], ["60%", "34.0%"]], R + 2.93, 4.6, 2.82, [1.5, 1.32], { rowH: 0.24 });
  G.para(s, "Each 10 pts of mix back to light adds ++~1.5 pts++; our base case assumes ++none++", R + 2.93, 5.85, 2.82, 0.55, { size: 10.5 });
  s.addShape("line", { x: R - 0.12, y: 4.28, w: 0, h: 2.12, line: { color: C.TXT, width: 1, dashType: "sysDot" } });

  G.banner(s, "Even granting the short thesis, it is <8% of the stock – and heavy mix is capacity-capped: ~30% is the floor, not a waypoint.", X, 6.48, W, 0.44, 14);
  G.source(s, "10-Q disclosures, Muddy Waters, Earnings Calls, In Practise, OEM cohort data, GPS Model",
    ["Illustrative: stock share × cost edge vs. market feedstock × material share of revenue. 1H26 transfers per Q2'26 10-Q summary.", "Paraphrase of the CEO's cycle/margin example; quoted phrase per call summary."]);
}

// ======================= SLIDE 2: PMA via SCI + two prints
async function slide2(pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "Thesis I: Variance on Margins – PMA Through SCI and Two Prints Re-Rate the Trough");
  const X = 0.68, W = 12.25, L = 0.68, LW = 6.0, R = 6.93, RW = 6.0;
  G.head(s, "The market prices ~0% PMA and reads 30% as a waypoint; FTAI controls its own PMA channel and only needs 30% to hold.", X, 0.88, W, { size: 13.5 });

  // ---- left: PMA via SCI
  sub(s, "PMA: at SCI, FTAI is the lessor that says yes", L, 1.26, LW);
  G.quote(s, "PMA hesitation sits mainly with lessors – conformity, residual values, return conditions – though it is “softening.” – AviTrader, May-26", L, 1.56, LW, 0.48, { size: 11 });
  const flow = [["FTAI sponsors SCI", "$2.0bn equity"], ["SCI owns the jets", "SCI is the lessor"], ["Engine work → FTAI", "FTAI is servicer"], ["FTAI sets parts policy", "no outside consent"]];
  flow.forEach((f, i) => {
    const x = L + i * 1.52;
    s.addShape("rect", { x, y: 2.1, w: 1.4, h: 0.58, fill: { color: i === 3 ? C.ORANGE : C.NAVY }, line: { color: i === 3 ? C.ORANGE : C.NAVY } });
    s.addText([{ text: f[0], options: { bold: true, fontSize: 10, breakLine: true } }, { text: f[1], options: { fontSize: 9 } }],
      { x, y: 2.1, w: 1.4, h: 0.58, align: "center", valign: "middle", fontFace: F, color: C.WHITE, margin: 2, isTextBox: true });
    if (i < 3) s.addText("►", { x: x + 1.4, y: 2.25, w: 0.12, h: 0.28, fontSize: 10, color: C.TXT, margin: 0, align: "center", isTextBox: true });
  });
  G.bullets(s, [
    "**Program built:** Chromalloy has ++3 of 5 CFM56 hot-section PMA parts approved++, incl. the HPT blade (Oct-25, >7 yrs, >$100M); “80% of the savings come from the first three parts” (Chromalloy CEO)",
    "**Captive channel:** SCI grows from ++11% to ~40% of FTAI's modules++ (130 → 700 aircraft) – ~4x our base-case PMA penetration, no outside lessor needed",
    "**Worth:** 50% of SCI modules on PMA at $0.4M each = ++~$130M of FY28 EBITDA (~2.1 pts of margin, ~$20 / share)++",
    "**Diligence:** SCI's LP / lender terms on PMA are ++not disclosed++",
  ], L, 2.74, LW, 1.98, { size: 11, psa: 1 });
  s.addChart(pres.charts.BAR, [
    { name: "Base case PMA", labels: ["FY27E", "FY28E", "FY29E", "FY30E", "FY31E"], values: [6, 24, 42, 59, 77] },
    { name: "50% of SCI modules on PMA", labels: ["FY27E", "FY28E", "FY29E", "FY30E", "FY31E"], values: [96, 132, 156, 168, 180] },
  ], { x: L, y: 4.72, w: 3.0, h: 1.68, barDir: "col", chartColors: ["A6A6A6", C.ORANGE], barGapWidthPct: 40, showValue: true, dataLabelPosition: "outEnd",
    dataLabelColor: "262626", dataLabelFontSize: 8, dataLabelFormatCode: "#,##0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 215, showLegend: true, legendPos: "b", ...ax, title: "PMA EBITDA Uplift ($M)" });
  s.addChart(pres.charts.BAR, [
    { name: "Third-party", labels: ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E"], values: [865, 1206, 1321, 1298, 1272] },
    { name: "SCI captive", labels: ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E"], values: [328, 482, 660, 780, 840] },
  ], { x: L + 3.05, y: 4.72, w: 2.95, h: 1.68, barDir: "col", barGrouping: "stacked", chartColors: [C.NAVY, C.ORANGE], barGapWidthPct: 40, showValue: false,
    valAxisHidden: true, showLegend: true, legendPos: "b", ...ax, title: "FTAI Modules: SCI Share Rising" });
  s.addShape("line", { x: R - 0.12, y: 1.28, w: 0, h: 5.12, line: { color: C.TXT, width: 1, dashType: "sysDot" } });

  // ---- right: rebuild + prints
  sub(s, "Price and PMA rebuild margin; two prints prove the trough", R, 1.26, RW);
  s.addChart(pres.charts.BAR, [
    { name: "base", labels: ["FY27E", "Price", "PMA", "FY31E"], values: [0, 29.9, 31.6, 0] },
    { name: "val", labels: ["FY27E", "Price", "PMA", "FY31E"], values: [29.9, 1.7, 0.9, 32.5] },
  ], { x: R, y: 1.56, w: 2.6, h: 1.95, barDir: "col", barGrouping: "stacked", chartColors: ["FFFFFF", C.NAVY], showValue: false, valAxisHidden: true, valAxisMinVal: 27, valAxisMaxVal: 33.5,
    ...ax, title: "Aerospace Margin Bridge (%)", showLegend: false, barGapWidthPct: 45 });
  [["29.9%", 0.28], ["+1.7", 0.84], ["+0.9", 1.4], ["32.5%", 1.95]].forEach(([t, x]) => s.addText(t, { x: R + x - 0.05, y: 1.8, w: 0.55, h: 0.2, align: "center", fontFace: F, fontSize: 9.5, bold: true, color: C.TXT, margin: 0, isTextBox: true }));
  G.bullets(s, [
    "**Price:** repair catalogues rose a median ++6.2% / yr++ across 3,404 matched packages (3,376 up, 1 down); FTAI priced below OEM to win share – we pass through ++half from FY28++",
    "**Per module:** EBITDA ++$913K → $1,139K++ (FY27E → FY31E)",
    "**No mix recovery** and no outside-lessor PMA in the base case",
  ], R + 2.65, 1.56, RW - 2.65, 1.95, { size: 10.5, psa: 1, valign: "middle" });
  const cats = [
    ["Q3'26 | Oct", "First print after the reset: Aerospace margin ++≥~30%++, modules on track for 1,200, PMA usage"],
    ["Inv. day | 10-Dec", "2027 framework: 1,700 modules, Jakarta / Cairo ramp, SCI II size, Power backlog"],
    ["Q4'26 | Feb-27", "++Second ~30% print++ + FY27 guide: 30% stops reading as a waypoint"],
  ];
  cats.forEach((c, i) => {
    const y = 3.58 + i * 0.47;
    s.addShape("rect", { x: R, y, w: 1.3, h: 0.41, fill: { color: C.NAVY }, line: { color: C.NAVY } });
    s.addText(c[0], { x: R, y, w: 1.3, h: 0.41, align: "center", valign: "middle", fontFace: F, fontSize: 10, bold: true, color: C.WHITE, margin: 0, isTextBox: true });
    G.dash(s, R + 1.35, y, RW - 1.35, 0.41);
    G.para(s, c[1], R + 1.4, y, RW - 1.45, 0.41, { size: 10.5, valign: "middle" });
  });
  sub(s, "What $167 implies for Aerospace", R, 5.04, RW);
  tbl(s, ["Aero EV / NTM EBITDA (Oct-27)", "5.3x", "10x", "12x", "14x"], [["Implied price / share^^1^^", "**$167**", "$244", "$277", "**$309**"], ["Upside vs. $167", "–", "+46%", "+66%", "+85%"]],
    R, 5.33, RW, [2.4, 0.9, 0.9, 0.9, 0.9], { rowH: 0.23, hi: 1 });
  G.para(s, "On base earnings, $167 pays only ++~5x++ for Aerospace a year out; ++each turn ≈ $16 / share++.", R, 6.07, RW, 0.3, { size: 11 });

  G.banner(s, "PMA through SCI and price pass-through rebuild margin to 32.5%; two ~30% prints re-rate a business priced at ~5x.", X, 6.48, W, 0.44, 14);
  G.source(s, "Chromalloy / FAA, Aviation Week, AviTrader, SR Technics catalogues, FTAI filings, GPS Model",
    ["1-yr base SOTP (NTM ≈ ¼ FY27E + ¾ FY28E), holding Power 10x, Leasing + SCI 9x and Sep-27 net debt."]);
}

module.exports = async function (pres) { await slide1(pres); await slide2(pres); };
