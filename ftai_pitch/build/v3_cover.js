const G = require("./g");
const { C, F } = G;

module.exports = async function (pres) {
  const s = pres.addSlide();
  s.background = { color: C.WHITE };
  // right panel
  const PX = 6.9;
  s.addShape("rect", { x: PX, y: 0, w: 13.333 - PX, h: 7.5, fill: { color: C.NAVY }, line: { color: C.NAVY } });
  s.addText([{ text: "FTAI", options: { bold: true, color: C.WHITE } }, { text: " AVIATION", options: { color: "9DC3E6" } }],
    { x: PX + 0.5, y: 0.45, w: 5.5, h: 0.4, fontFace: "Calibri", fontSize: 18, margin: 0, isTextBox: true });
  const stats = [
    ["$167", "Share price (10/2/26)"], ["$309", "1-year target (+85%)"], ["~5x", "Reward-to-risk (+157% / –32%)"], ["$161", "Bear-case value ≈ today's price"],
  ];
  stats.forEach(([big, lab], i) => {
    const x = PX + 0.5 + (i % 2) * 2.9, y = 1.45 + Math.floor(i / 2) * 1.55;
    s.addText(big, { x, y, w: 2.7, h: 0.75, fontFace: F, fontSize: 42, bold: true, color: i === 1 ? C.ORANGE : C.WHITE, margin: 0, isTextBox: true });
    s.addText(lab, { x, y: y + 0.75, w: 2.7, h: 0.4, fontFace: F, fontSize: 13, color: "D9E2F0", margin: 0, isTextBox: true });
  });
  s.addShape("line", { x: PX + 0.5, y: 4.7, w: 5.4, h: 0, line: { color: "9DC3E6", width: 1 } });
  const th = [["I", "Margins have bottomed at ~30%: the fraud unwind is <8% of inventory"], ["II", "FTAI catches the CFM56 work OEMs and airlines are sending out"], ["III", "Power is a free call option on the grid gap"]];
  th.forEach(([n, t], i) => {
    const y = 4.9 + i * 0.62;
    s.addShape("ellipse", { x: PX + 0.5, y, w: 0.42, h: 0.42, fill: { color: C.ORANGE }, line: { color: C.ORANGE } });
    s.addText(n, { x: PX + 0.5, y, w: 0.42, h: 0.42, align: "center", valign: "middle", fontFace: F, fontSize: 13, bold: true, color: C.WHITE, margin: 0, isTextBox: true });
    s.addText(t, { x: PX + 1.05, y: y - 0.04, w: 4.9, h: 0.5, valign: "middle", fontFace: F, fontSize: 14, color: C.WHITE, margin: 0, isTextBox: true });
  });

  // left text (CARG cover style)
  s.addText("FTAI Aviation\n(NASDAQ: FTAI)", { x: 0.55, y: 0.45, w: 6.2, h: 1.45, fontFace: F, fontSize: 40, color: C.INK, margin: 0, isTextBox: true, valign: "bottom" });
  s.addText("Long Recommendation (1-Year Target $309, +85%)", { x: 0.55, y: 1.98, w: 6.3, h: 0.4, fontFace: F, fontSize: 19, color: C.INK, margin: 0, isTextBox: true });
  s.addText("By Sara Jankovic, Josephine Sun, Andrew Chen, and Max Salomon  |  October 2026", { x: 0.55, y: 2.42, w: 6.2, h: 0.3, fontFace: F, fontSize: 12.5, color: C.INK, margin: 0, isTextBox: true });
  s.addText("A compounder still priced for a fraud.", { x: 0.55, y: 2.85, w: 6.2, h: 0.42, fontFace: F, fontSize: 20, bold: true, italic: true, color: C.TXT, margin: 0, isTextBox: true });

  // share-price chart, last 12 months
  const px = require("./px_1y.json");
  const keep = new Set(["Nov-25", "Jan-26", "Mar-26", "May-26", "Jul-26", "Sep-26"]);
  const labels = px.labels.map((l) => (keep.has(l) ? l : ""));
  s.addShape("line", { x: 0.55, y: 3.45, w: 6.0, h: 0, line: { color: C.NAVY, width: 1 } });
  s.addText("FTAI share price, last 12 months ($)", { x: 0.55, y: 3.5, w: 4.0, h: 0.28, fontFace: F, fontSize: 12, bold: true, color: C.INK, margin: 0, isTextBox: true });
  s.addText("Roughly halved from the Feb-26 peak on the 1H26 margin reset", { x: 0.55, y: 3.78, w: 6.0, h: 0.26, fontFace: F, fontSize: 10.5, italic: true, color: C.MUTE, margin: 0, isTextBox: true });
  s.addChart(pres.charts.LINE, [
    { name: "FTAI", labels, values: px.values },
    { name: "1-yr target $309", labels, values: px.values.map(() => 309) },
  ], { x: 0.4, y: 4.05, w: 6.25, h: 3.0, chartColors: [C.NAVY, C.ORANGE], lineSize: 1.5, lineDataSymbol: "none",
    valAxisMinVal: 100, valAxisMaxVal: 350, valAxisMajorUnit: 50, valAxisLabelFormatCode: "$0",
    catAxisLabelFrequency: 1, catAxisLabelFontSize: 9, valAxisLabelFontSize: 9, catAxisLabelFontFace: F, valAxisLabelFontFace: F,
    catAxisLabelColor: "595959", valAxisLabelColor: "595959", catAxisLineColor: "A6A6A6", valAxisLineShow: false,
    valGridLine: { color: "E7E6E6", size: 0.5 }, catGridLine: { style: "none" }, catAxisMajorTickMark: "none",
    showLegend: true, legendPos: "t", legendFontFace: F, legendFontSize: 9, showValue: false });
  s.addText("$165 (10/13/26)", { x: 5.3, y: 6.3, w: 1.3, h: 0.22, fontFace: F, fontSize: 9.5, bold: true, color: C.NAVY, align: "right", margin: 0, isTextBox: true });
  s.addText("Daily closes traced from team price chart; approximate.", { x: 0.55, y: 7.12, w: 6.0, h: 0.2, fontFace: F, fontSize: 8, italic: true, color: C.MUTE, margin: 0, isTextBox: true });
};
