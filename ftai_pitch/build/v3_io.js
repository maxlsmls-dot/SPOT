const G = require("./g");
const { C, F } = G;

const ax = { catAxisLabelFontFace: F, valAxisLabelFontFace: F, catAxisLabelFontSize: 11, valAxisLabelFontSize: 10, catAxisLabelColor: "262626", valAxisLabelColor: "262626",
  dataLabelFontFace: F, dataLabelFontSize: 10, legendFontFace: F, legendFontSize: 10, catGridLine: { style: "none" }, valGridLine: { style: "none" }, catAxisLineColor: "7F7F7F" };

module.exports = async function (pres) {
  const s = pres.addSlide({ masterName: "Pitch" });
  G.title(s, "Industry Overview – A Price-Taking Aftermarket Entering Its Heaviest Years");
  G.sub(s, "The CFM56 aftermarket is aging into heavier visits, with flat demand through 2028 and repair prices compounding ~6% a year. FTAI chose share over margin in 1H26 – a deliberate reset the market reads as structural.", { h: 0.6, size: 13.5 });

  const L = 0.68, R = 6.98, W = 5.95;

  // ---- TL: fleet aging
  G.head(s, "The CFM56 fleet is aging into repeat, heavier visits...", L, 1.55, W);
  s.addChart(pres.charts.BAR, [
    { name: "0 prior visits", labels: ["2024 Actual", "2028 OEM Projection"], values: [40, 26] },
    { name: "1 prior visit", labels: ["2024 Actual", "2028 OEM Projection"], values: [29, 31] },
    { name: "2+ prior visits", labels: ["2024 Actual", "2028 OEM Projection"], values: [31, 43] },
  ], { x: L, y: 1.95, w: 3.7, h: 2.2, barDir: "col", barGrouping: "percentStacked", chartColors: ["BDD7EE", "2E75B6", C.NAVY], barGapWidthPct: 55,
    showValue: true, dataLabelPosition: "ctr", dataLabelColor: C.WHITE, dataLabelFormatCode: '0"%"', valAxisHidden: true, showLegend: true, legendPos: "b", ...ax });
  s.addText("22,700", { x: L + 3.8, y: 2.0, w: 2.1, h: 0.42, align: "center", fontFace: F, fontSize: 26, bold: true, color: C.NAVY, margin: 0, isTextBox: true });
  G.para(s, "CFM56-5B/-7B engines in service: the ++largest fleet in aviation++", L + 3.8, 2.42, 2.1, 0.5, { size: 11, align: "center" });
  s.addText("43%", { x: L + 3.8, y: 3.0, w: 2.1, h: 0.42, align: "center", fontFace: F, fontSize: 26, bold: true, color: C.ORANGE, margin: 0, isTextBox: true });
  G.para(s, "of the fleet on its ++third or later visit by 2028++, when full restorations dominate", L + 3.8, 3.42, 2.1, 0.62, { size: 11, align: "center" });

  // ---- TR: shop visits plateau
  G.head(s, "... keeping shop-visit demand flat through 2028...", R, 1.55, W);
  s.addChart(pres.charts.BAR, [{ name: "CFM56 shop visits", labels: ["2025", "2026", "2027", "2028", "2029", "2030", "2031"], values: [2350, 2400, 2400, 2350, 2250, 2150, 2085] }],
    { x: R, y: 2.22, w: 3.85, h: 1.95, barDir: "col", chartColors: [C.NAVY], barGapWidthPct: 45, showValue: true, dataLabelPosition: "outEnd", dataLabelColor: "262626",
      dataLabelFormatCode: "#,##0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 2900, showLegend: false, ...ax, catAxisLabelFontSize: 10, dataLabelFontSize: 9,
    });
  s.addShape("rect", { x: R + 0.62, y: 2.28, w: 1.55, h: 1.62, fill: { type: "none" }, line: { color: C.RED, width: 1.5, dashType: "dash" } });
  s.addText("GE: plateau through 2028", { x: R + 0.4, y: 2.0, w: 2.0, h: 0.24, align: "center", fontFace: F, fontSize: 10, bold: true, color: C.RED, margin: 0, isTextBox: true });
  G.dash(s, R + 3.95, 2.0, 2.0, 2.1);
  G.para(s, "Retirements running ++1.5–2%++ vs. GE's 2–3% assumption\n\nLEAP durability fixes cut over only in ++early 2027++; GTF groundings persist", R + 4.0, 2.05, 1.9, 2.0, { size: 11, valign: "middle" });

  // ---- BL: pricing
  G.head(s, "... while third-party repair prices compound ~6% a year...", L, 4.25, W);
  s.addChart(pres.charts.BAR, [{ name: "Median list price change", labels: ["CFM56-5B\n2024–25", "CFM56-5B\n2025–26", "CFM56-7B\n2025–26"], values: [0.062, 0.062, 0.061] }],
    { x: L, y: 4.65, w: 3.7, h: 2.32, barDir: "col", chartColors: ["2E75B6"], barGapWidthPct: 60, showValue: true, dataLabelPosition: "outEnd", dataLabelColor: "262626",
      dataLabelFormatCode: "0.0%", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 0.08, showLegend: false, ...ax, catAxisLabelFontSize: 10,
      showTitle: true, title: "Median Repair List-Price Change (y/y)", titleFontFace: F, titleFontSize: 11, titleColor: "262626" });
  G.dash(s, L + 3.8, 4.7, 2.15, 2.2);
  G.para(s, "Of ++3,404 matched repair packages++, 3,376 rose and only 1 fell\n\nFTAI prices ++below OEM++ and has not passed through the escalator: headroom we model from FY28", L + 3.85, 4.75, 2.05, 2.1, { size: 11, valign: "middle" });

  // ---- BR: FTAI reset
  G.head(s, "However, FTAI deliberately traded margin for share in 1H26.", R, 4.25, W);
  G.quote(s, "“We're inclined to say yes and take market share.” – FTAI CEO, Q2'26 Earnings Call", R, 4.66, W, 0.36, { size: 11.5 });
  const q = ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26"];
  s.addChart(pres.charts.BAR, [{ name: "Modules", labels: q, values: [138, 184, 207, 228, 270, 296] }], { x: R, y: 5.08, w: 2.95, h: 1.92, barDir: "col",
    chartColors: [C.NAVY, C.NAVY, C.NAVY, C.NAVY, C.ORANGE, C.ORANGE], barGapWidthPct: 45, showValue: true, dataLabelPosition: "outEnd", dataLabelColor: "262626",
    dataLabelFormatCode: "#,##0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 350, showLegend: false, ...ax, catAxisLabelFontSize: 9, dataLabelFontSize: 9,
    showTitle: true, title: "Modules Produced (+61% y/y in Q2'26)", titleFontFace: F, titleFontSize: 11, titleColor: "262626" });
  s.addChart(pres.charts.LINE, [{ name: "Margin", labels: q, values: [0.359, 0.336, 0.348, 0.346, 0.299, 0.285] }], { x: R + 3.0, y: 5.08, w: 2.95, h: 1.92,
    chartColors: [C.ORANGE], lineSize: 2.25, lineDataSymbol: "circle", lineDataSymbolSize: 6, showValue: true, dataLabelPosition: "t", dataLabelColor: "262626",
    dataLabelFormatCode: "0.0%", valAxisHidden: true, valAxisMinVal: 0.24, valAxisMaxVal: 0.38, showLegend: false, ...ax, catAxisLabelFontSize: 9, dataLabelFontSize: 9,
    showTitle: true, title: "Aerospace Adj. EBITDA Margin", titleFontFace: F, titleFontSize: 11, titleColor: "262626" });
  G.source(s, "GE / Safran shop-visit outlook & cohort data, Aviation Week, SR Technics CFM56 catalogues (2024–26), Company Filings");
};
