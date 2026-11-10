const G = require("./g");
const { C, F } = G;

const ax = { catAxisLabelFontFace: F, catAxisLabelFontSize: 9, catAxisLabelColor: "262626", catGridLine: { style: "none" }, valGridLine: { style: "none" }, catAxisLineColor: "7F7F7F",
  titleFontFace: F, titleFontSize: 10.5, titleColor: "262626", showTitle: true };

function tbl(s, hdr, rows, x, y, w, colW, o = {}) {
  const sz = o.size || 10;
  const H = hdr.map((t) => ({ text: t, options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontFace: F, fontSize: sz, align: "center" } }));
  s.addTable([H, ...rows.map((r, i) => r.map((c, j) => ({ text: G.parse(String(c) || " ", { fontFace: F, fontSize: sz, color: C.TXT }),
    options: { align: j === 0 ? "left" : "center", fill: { color: (o.hiRows || []).includes(i) ? "DDEBF7" : (o.hiCol === j ? "FBE5D6" : C.WHITE) },
      border: (o.topRows || []).includes(i) ? [{ type: "solid", pt: 1, color: C.TXT }, { type: "solid", pt: 0.5, color: "D9D9D9" }, { type: "solid", pt: 0.5, color: "D9D9D9" }, { type: "solid", pt: 0.5, color: "D9D9D9" }] : { type: "solid", pt: 0.5, color: "D9D9D9" } } })))],
    { x, y, w, colW, rowH: o.rowH || 0.21, margin: [1, 3, 1, 3] });
}
const vline = (s, x, y, h) => s.addShape("line", { x, y, w: 0, h, line: { color: C.TXT, width: 1, dashType: "sysDot" } });

module.exports = async function (pres) {
  const s = pres.addSlide({ masterName: "Pitch" });
  G.title(s, "Valuation – 1-Year Target of $304 (+54%) With ~3x Reward-to-Risk");
  s.addText("($ in millions, except per share)", { x: 9.9, y: 0.52, w: 3.03, h: 0.3, align: "right", fontFace: F, fontSize: 11, italic: true, color: C.INK, margin: 0, isTextBox: true });
  const X = 0.68, W = 12.25, L = 0.68, LW = 6.0, R = 6.93, RW = 6.0;

  G.head(s, "We value FTAI as of Oct-27 on NTM EBITDA (¼ FY27E + ¾ FY28E) and net debt at Sep-27 – a 1-year hold.", X, 0.88, W, { size: 13 });

  // ---- left: base SOTP
  G.para(s, "**++Base case: sum of the parts at Oct-27++**", L, 1.26, LW, 0.26, { size: 11.5, align: "center" });
  tbl(s, ["Segment", "NTM EBITDA", "EV / EBITDA", "EV", "$ / share"], [
    ["Aerospace Products", "1,825", "13.7x", "24,943", "$239.8"],
    ["FTAI Power", "788", "10.0x", "7,875", "$75.7"],
    ["Aviation Leasing + SCI", "444", "9.0x", "3,994", "$38.4"],
    ["Corporate & eliminations", "(213)", "12.0x", "(2,565)", "($24.7)"],
    ["**Enterprise value**", "**2,843**", "**12.0x**", "**34,247**", "**$329.3**"],
    ["(–) Net debt (Sep-27E)", "", "", "(2,566)", "($24.7)"],
    ["(–) Preferred", "", "", "(65)", "($0.6)"],
    ["**1-year target (equity / share)**", "", "", "**31,616**", "**$304.0**"],
    ["**Return vs. $198.00**", "", "", "", "**+54%**"],
  ], L, 1.54, LW, [2.2, 0.95, 0.95, 0.95, 0.95], { rowH: 0.23, size: 9.5, hiRows: [4, 7, 8], topRows: [4, 7] });
  G.para(s, "Multiples: Aerospace ++13.7x++ (a discount to aftermarket peers), Power ++10x++ (contract risk), Leasing + SCI 9x; corporate at the blended multiple.", L, 3.88, LW, 0.48, { size: 10 });

  // ---- right: cases
  vline(s, R - 0.12, 1.28, 3.1);
  G.para(s, "**++Bear / base / bull++**", R, 1.26, RW, 0.26, { size: 11.5, align: "center" });
  tbl(s, ["", "Bear", "Base", "Bull"], [
    ["**I. Margins**", "Short thesis right: stuck at 28.5%, no PMA", "~30% is the trough; price + PMA via SCI rebuild", "Light-work mix returns; full PMA ramp"],
    ["**II. Share**", "Fuel shock bites; share stalls at 15%", "Retirements ~2%; FTAI catches OEM overflow", "Overflow flows to FTAI; 25% share"],
    ["**III. Power**", "Ramp slips; half the JV economics", "Signed order delivered; ramp to 90 units", "One more ~1 GW contract"],
    ["**Fraud discount**", "Persists", "Partly closes", "Fully closes"],
    ["**1-yr target**", "**$114**", "**$304**", "**$430**"],
    ["**Return / probability**", "**–43%** / 20%", "**+54%** / 60%", "**+117%** / 20%"],
  ], R, 1.54, RW, [1.2, 1.6, 1.6, 1.6], { rowH: 0.3, size: 9, hiRows: [4, 5], hiCol: 2 });
  s.addShape("rect", { x: R, y: 3.72, w: RW, h: 0.62, fill: { color: C.NAVY }, line: { color: C.NAVY } });
  G.para(s, "**Probability-weighted: $291 (+47%)\nReward / risk: +117% / –43% ≈ 2.7x**", R, 3.72, RW, 0.62, { size: 12, color: C.WHITE, align: "center", valign: "middle" });

  // ---- bottom
  G.head(s, "Today's $198 pays for margins holding ($180) and ~30% of share – Power is still free: margins +$22, share +$61, Power +$63.", X, 4.42, W, { size: 13 });
  const lab = ["Bear-case\noutcomes", "Thesis I\nMargins", "Thesis II\nShare", "Thesis III\nPower", "1-yr target"];
  s.addChart(pres.charts.BAR, [
    { name: "base", labels: lab, values: [0, 157.8, 179.6, 240.7, 0] },
    { name: "val", labels: lab, values: [157.8, 21.8, 61.1, 63.3, 304.0] },
  ], { x: L, y: 4.8, w: LW, h: 1.62, barDir: "col", barGrouping: "stacked", chartColors: ["FFFFFF", C.NAVY], barGapWidthPct: 45, showValue: false,
    valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 360, showLegend: false, ...ax, showTitle: false, catAxisLabelFontSize: 9 });
  [["$158", 0, 157.8, 0.26], ["+$22", 1, 157.8, 0.02], ["+$61", 2, 240.7, 0], ["+$63", 3, 304.0, 0], ["$304", 4, 304.0, 0]].forEach(([t, k, val, dy]) =>
    s.addText(t, { x: L + 0.33 + k * 1.15, y: 4.83 + 1.2 * (1 - val / 360) - 0.21 + (dy ? dy + 0.21 : 0), w: 0.7, h: 0.18, align: "center", fontFace: F, fontSize: 10, bold: true, color: k === 0 ? C.WHITE : (k < 4 ? C.ORANGE : C.TXT), margin: 0, isTextBox: true }));
  s.addShape("line", { x: L + 0.3, y: 4.83 + 1.2 * (1 - 198 / 360), w: 3.3, h: 0, line: { color: C.RED, width: 1.25, dashType: "dash" } });
  s.addText("today $198", { x: L + 0.3, y: 4.83 + 1.2 * (1 - 198 / 360) - 0.42, w: 0.85, h: 0.18, align: "center", fontFace: F, fontSize: 9, italic: true, color: C.RED, margin: 0, isTextBox: true });
  vline(s, R - 0.12, 4.82, 1.6);
  G.para(s, "**++Cross-checks++**", R, 4.78, 2.6, 0.24, { size: 11, align: "center" });
  tbl(s, ["DCF rolled 1 yr", "Target"], [["Bear", "$111"], ["Base", "$337"], ["Bull", "$425"]], R, 5.04, 2.6, [1.4, 1.2], { rowH: 0.21, size: 9.5, hiRows: [1] });
  G.para(s, "Ex-Power base: **$234**, 18% upside", R, 5.92, 2.6, 0.24, { size: 10 });
  G.para(s, "EV / NTM: ++11.8x++ today → ++12.0x++", R, 6.14, 2.6, 0.3, { size: 10 });
  G.para(s, "**++Base target: Aero × Power multiple++**", R + 2.75, 4.78, RW - 2.75, 0.24, { size: 11, align: "center" });
  tbl(s, ["Aero \\ Power", "6x", "8x", "10x", "12x"], [["12x", "$249", "$263", "$277", "$291"], ["13.7x", "$276", "$290", "**$304**", "$318"], ["16x", "$314", "$328", "$342", "$356"]],
    R + 2.75, 5.04, RW - 2.75, [0.85, 0.6, 0.6, 0.6, 0.6], { rowH: 0.21, size: 9.5, hiRows: [1] });
  G.para(s, "12x Aero, 6x Power: **$249**, 26% upside", R + 2.75, 5.92, RW - 2.75, 0.3, { size: 10 });

  G.banner(s, "Base $304 (+54%) in 12 months; probability-weighted $291 (+47%); bear $114 (–43%) – roughly 3x reward-to-risk.", X, 6.48, W, 0.44, 14);
  G.source(s, "FTAI filings (Q3'26); $198.00 (11/9/26); 104.0M diluted shares (pre-ASR)",
    ["NTM ≈ ¼ FY27E + ¾ FY28E. Bridge: each thesis's model drivers switched bear → base in order, at base multiples."]);
};
