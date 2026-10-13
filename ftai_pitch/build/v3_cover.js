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
  s.addText("FTAI Aviation\n(NASDAQ: FTAI)", { x: 0.55, y: 1.9, w: 6.2, h: 1.5, fontFace: F, fontSize: 44, color: C.INK, margin: 0, isTextBox: true, valign: "bottom" });
  s.addText("Long Recommendation (1-Year Target $309, +85%)", { x: 0.55, y: 3.45, w: 6.3, h: 0.45, fontFace: F, fontSize: 21, color: C.INK, margin: 0, isTextBox: true });
  s.addText("By Sara Jankovic, Josephine Sun,\nAndrew Chen, and Max Salomon", { x: 0.55, y: 4.1, w: 6.1, h: 0.75, fontFace: F, fontSize: 18, color: C.INK, margin: 0, isTextBox: true, valign: "top" });
  s.addText("October 2026", { x: 0.55, y: 4.9, w: 6.2, h: 0.3, fontFace: F, fontSize: 13, color: C.INK, margin: 0, isTextBox: true });
  s.addText("A compounder still priced for a fraud.", { x: 0.55, y: 5.45, w: 6.2, h: 0.45, fontFace: F, fontSize: 21, bold: true, italic: true, color: C.TXT, margin: 0, isTextBox: true });
};
