// Shared helpers for the FTAI pitch deck
const pptxgen = require("pptxgenjs");

const C = {
  NAVY: "0B1F44", NAVY2: "1F3A6B", ORANGE: "E8702A", TEAL: "2E8FAE", LBLUE: "DCE6F2",
  LTEAL: "BFE0EA", GRAY: "F2F2F2", MGRAY: "8C8C8C", DGRAY: "404040", GREEN: "2E7D4F",
  RED: "B03A2E", WHITE: "FFFFFF", GRID: "E3E3E3", SLATE: "5B7DB1",
};
const HF = "Cambria", BF = "Calibri";

function makePres() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
  pres.author = "Max Salomon";
  pres.company = "Global Platinum Securities";
  pres.title = "FTAI Aviation - Long Recommendation";
  pres.theme = { headFontFace: HF, bodyFontFace: BF };

  const wordmark = (x, y, size) => [
    { text: { text: "FTAI", options: { x: x + 0.2, y, w: 0.75, h: 0.5, align: "right", valign: "middle", bold: true, color: C.NAVY, fontFace: BF, fontSize: size, margin: 0 } } },
    { text: { text: "AVIATION", options: { x: x + 1.0, y, w: 1.55, h: 0.5, align: "left", valign: "middle", color: C.TEAL, fontFace: BF, fontSize: size, margin: 0 } } },
  ];

  pres.defineSlideMaster({
    title: "CONTENT",
    background: { color: C.WHITE },
    margin: [0.4, 0.45, 0.45, 0.45],
    objects: [
      { rect: { x: 12.42, y: 0.3, w: 0.08, h: 0.38, fill: { color: C.ORANGE } } },
      ...wordmark(9.7, 0.24, 18),
      { line: { x: 0.45, y: 1.0, w: 12.43, h: 0, line: { color: C.NAVY, width: 1.25 } } },
      { line: { x: 0.45, y: 7.0, w: 12.43, h: 0, line: { color: "BFBFBF", width: 0.75 } } },
      { text: { text: "GLOBAL PLATINUM SECURITIES", options: { x: 10.0, y: 7.06, w: 2.88, h: 0.3, align: "right", fontFace: HF, fontSize: 8, color: C.NAVY, bold: true, charSpacing: 2, margin: 0 } } },
      { placeholder: { options: { name: "title", type: "title", x: 0.45, y: 0.22, w: 9.3, h: 0.7, fontFace: HF, fontSize: 26, bold: true, color: C.NAVY, valign: "middle", align: "left", margin: 0 }, text: "" } },
    ],
    slideNumber: { x: 0.45, y: 7.08, w: 0.4, h: 0.25, fontFace: BF, fontSize: 9, color: C.NAVY, bold: true },
  });

  pres.defineSlideMaster({
    title: "BLANK_BRAND",
    background: { color: C.WHITE },
    objects: [
      { rect: { x: 12.42, y: 0.3, w: 0.08, h: 0.38, fill: { color: C.ORANGE } } },
      ...wordmark(9.7, 0.24, 18),
      { text: { text: "GLOBAL PLATINUM SECURITIES", options: { x: 10.0, y: 7.06, w: 2.88, h: 0.3, align: "right", fontFace: HF, fontSize: 8, color: C.NAVY, bold: true, charSpacing: 2, margin: 0 } } },
    ],
  });
  return pres;
}

// --- inline markup: **bold navy**, {{orange bold}}, [[teal bold]], __italic__
function parse(str, base = {}) {
  if (Array.isArray(str)) return str;
  const out = [];
  const re = /(\*\*[^*]+\*\*|\{\{[^}]+\}\}|\[\[[^\]]+\]\]|__[^_]+__)/g;
  let last = 0, m;
  while ((m = re.exec(str))) {
    if (m.index > last) out.push({ text: str.slice(last, m.index), options: { ...base } });
    const t = m[0];
    if (t.startsWith("**")) out.push({ text: t.slice(2, -2), options: { ...base, bold: true, color: base.boldColor || C.NAVY } });
    else if (t.startsWith("{{")) out.push({ text: t.slice(2, -2), options: { ...base, bold: true, color: C.ORANGE } });
    else if (t.startsWith("[[")) out.push({ text: t.slice(2, -2), options: { ...base, bold: true, color: C.TEAL } });
    else out.push({ text: t.slice(2, -2), options: { ...base, italic: true } });
    last = m.index + t.length;
  }
  if (last < str.length) out.push({ text: str.slice(last), options: { ...base } });
  out.forEach((r) => delete r.options.boldColor);
  return out;
}

function title(s, t) { s.addText(t, { placeholder: "title" }); }

function source(s, t) {
  s.addText(parse("**Source:** " + t, { fontSize: 8, color: C.DGRAY, fontFace: BF }), {
    x: 0.95, y: 7.04, w: 8.9, h: 0.32, margin: 0, valign: "middle", isTextBox: true,
  });
}

function banner(s, t, x, y, w, h = 0.4, size = 15) {
  s.addShape("rect", { x, y, w, h, fill: { color: C.NAVY }, line: { color: C.NAVY } });
  s.addText(t, { x, y, w, h, align: "center", valign: "middle", fontFace: HF, fontSize: size, bold: true, color: C.WHITE, margin: 2, isTextBox: true });
}

function sub(s, t, x, y, w, h = 0.32, size = 12) {
  s.addShape("rect", { x, y, w, h, fill: { color: C.LBLUE }, line: { color: C.NAVY, width: 0.75 } });
  s.addText(t, { x, y, w, h, align: "center", valign: "middle", fontFace: HF, fontSize: size, bold: true, color: C.NAVY, margin: 2, isTextBox: true });
}

// dashed callout box with markup text
function box(s, text, x, y, w, h, o = {}) {
  s.addShape("roundRect", {
    x, y, w, h, rectRadius: 0.06,
    fill: { color: o.fill || C.WHITE },
    line: { color: o.lineColor || C.NAVY, width: o.lineW || 1, dashType: o.solid ? "solid" : "dash" },
  });
  if (text != null) {
    const base = { fontFace: BF, fontSize: o.size || 10, color: o.color || C.DGRAY, boldColor: o.boldColor };
    s.addText(Array.isArray(text) ? text : parse(text, base), {
      x: x + 0.06, y: y + 0.03, w: w - 0.12, h: h - 0.06, valign: o.valign || "middle",
      align: o.align || "left", margin: 3, isTextBox: true, paraSpaceAfter: o.psa || 0,
    });
  }
}

// solid filled panel (no border) with text
function panel(s, text, x, y, w, h, o = {}) {
  s.addShape(o.round === false ? "rect" : "roundRect", { x, y, w, h, rectRadius: 0.06, fill: { color: o.fill || C.GRAY }, line: { color: o.line || o.fill || C.GRAY, width: 0.75 } });
  if (text != null) {
    const base = { fontFace: o.font || BF, fontSize: o.size || 10, color: o.color || C.DGRAY, boldColor: o.boldColor };
    s.addText(parse(text, base), { x: x + 0.05, y, w: w - 0.1, h, valign: o.valign || "middle", align: o.align || "left", margin: 3, isTextBox: true });
  }
}

// bullet list; items are markup strings
function bullets(s, items, x, y, w, h, o = {}) {
  const size = o.size || 10;
  const runs = [];
  items.forEach((it, i) => {
    const r = parse(it, { fontFace: BF, fontSize: size, color: o.color || C.DGRAY, boldColor: o.boldColor });
    r[0].options.bullet = o.number ? { type: "number" } : { code: "25AA" };
    r[0].options.paraSpaceAfter = o.psa ?? 4;
    if (i < items.length - 1) r[r.length - 1].options.breakLine = true;
    runs.push(...r);
  });
  s.addText(runs, { x, y, w, h, valign: o.valign || "top", margin: 3, isTextBox: true });
}

function text(s, str, x, y, w, h, o = {}) {
  s.addText(parse(str, { fontFace: o.font || BF, fontSize: o.size || 10, color: o.color || C.DGRAY, bold: o.bold, italic: o.italic, boldColor: o.boldColor }), {
    x, y, w, h, align: o.align || "left", valign: o.valign || "middle", margin: o.margin ?? 2, isTextBox: true,
  });
}

// numbered circle
function badge(s, n, x, y, d = 0.42, fill = C.NAVY, size = 13) {
  s.addShape("ellipse", { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill } });
  s.addText(String(n), { x, y, w: d, h: d, align: "center", valign: "middle", fontFace: HF, fontSize: size, bold: true, color: C.WHITE, margin: 0, isTextBox: true });
}

function stat(s, big, small, x, y, w, h, o = {}) {
  panel(s, null, x, y, w, h, { fill: o.fill || C.GRAY });
  s.addText(big, { x, y: y + 0.04, w, h: h * 0.55, align: "center", valign: "bottom", fontFace: HF, fontSize: o.bigSize || 20, bold: true, color: o.bigColor || C.ORANGE, margin: 0, isTextBox: true });
  s.addText(parse(small, { fontFace: BF, fontSize: o.size || 9, color: o.smallColor || C.DGRAY }), { x: x + 0.05, y: y + h * 0.58, w: w - 0.1, h: h * 0.4, align: "center", valign: "top", margin: 0, isTextBox: true });
}

// --- charts
const axisTxt = { catAxisLabelColor: "595959", valAxisLabelColor: "595959", catAxisLabelFontSize: 9, valAxisLabelFontSize: 8, catAxisLabelFontFace: BF, valAxisLabelFontFace: BF };

function chartTitle(s, t, x, y, w) {
  s.addText(t, { x, y, w, h: 0.26, align: "center", valign: "middle", fontFace: BF, fontSize: 10.5, bold: true, color: C.NAVY, margin: 0, isTextBox: true });
}

function bar(s, pres, x, y, w, h, labels, series, o = {}) {
  if (o.title) { chartTitle(s, o.title, x, y, w); y += 0.26; h -= 0.26; }
  const data = series.map((se) => ({ name: se.name, labels, values: se.values }));
  const opts = {
    x, y, w, h, barDir: o.dir || "col", barGrouping: o.stacked ? (o.pct100 ? "percentStacked" : "stacked") : "clustered",
    chartColors: o.colors || [C.NAVY, C.TEAL, C.ORANGE, C.SLATE],
    showValue: o.showValue !== false, dataLabelFontSize: o.dlSize || 8.5, dataLabelFontFace: BF,
    dataLabelColor: o.dlColor || (o.stacked ? C.WHITE : "262626"), dataLabelPosition: o.stacked ? "ctr" : (o.dlPos || "outEnd"),
    dataLabelFormatCode: o.fmt || "#,##0", valAxisLabelFormatCode: o.axFmt || o.fmt || "#,##0",
    valAxisHidden: o.hideVal !== false, valGridLine: o.grid ? { color: C.GRID, size: 0.5 } : { style: "none" }, catGridLine: { style: "none" },
    showLegend: !!o.legend, legendPos: "b", legendFontSize: 8.5, legendFontFace: BF, legendColor: "404040",
    barGapWidthPct: o.gap ?? 60, valAxisMinVal: o.min, valAxisMaxVal: o.max, catAxisLineShow: true, catAxisLineColor: "BFBFBF",
    ...axisTxt, catAxisLabelFontSize: o.catSize || 9, catAxisLabelRotate: o.rot || 0, valAxisLineShow: false,
  };
  if (o.varyColors) opts.chartColors = o.colors;
  s.addChart(pres.charts.BAR, data, opts);
}

function line(s, pres, x, y, w, h, labels, series, o = {}) {
  if (o.title) { chartTitle(s, o.title, x, y, w); y += 0.26; h -= 0.26; }
  const data = series.map((se) => ({ name: se.name, labels, values: se.values }));
  s.addChart(pres.charts.LINE, data, {
    x, y, w, h, chartColors: o.colors || [C.NAVY, C.TEAL, C.ORANGE], lineSize: 2.25, lineDataSymbol: "circle", lineDataSymbolSize: 6,
    showValue: o.showValue !== false, dataLabelFontSize: 8.5, dataLabelFontFace: BF, dataLabelColor: "262626", dataLabelPosition: "t",
    dataLabelFormatCode: o.fmt || "#,##0", valAxisLabelFormatCode: o.axFmt || o.fmt || "#,##0", valAxisHidden: o.hideVal !== false,
    valGridLine: o.grid ? { color: C.GRID, size: 0.5 } : { style: "none" }, catGridLine: { style: "none" },
    showLegend: !!o.legend, legendPos: "b", legendFontSize: 8.5, legendFontFace: BF, valAxisMinVal: o.min, valAxisMaxVal: o.max,
    catAxisLineColor: "BFBFBF", ...axisTxt, valAxisLineShow: false,
  });
}

// bars on primary + line on secondary axis
function combo(s, pres, x, y, w, h, labels, barSeries, lineSeries, o = {}) {
  if (o.title) { chartTitle(s, o.title, x, y, w); y += 0.26; h -= 0.26; }
  const types = [
    { type: pres.charts.BAR, data: barSeries.map((se) => ({ name: se.name, labels, values: se.values })),
      options: { barDir: "col", chartColors: o.barColors || [C.NAVY], barGapWidthPct: 55, showValue: true, dataLabelPosition: "outEnd",
        dataLabelFontSize: 8, dataLabelFontFace: BF, dataLabelColor: "262626", dataLabelFormatCode: o.fmt || "#,##0" } },
    { type: pres.charts.LINE, data: lineSeries.map((se) => ({ name: se.name, labels, values: se.values })),
      options: { chartColors: o.lineColors || [C.ORANGE], lineSize: 2.25, lineDataSymbol: "circle", lineDataSymbolSize: 6, secondaryValAxis: true, secondaryCatAxis: true,
        showValue: o.lineLabels !== false, dataLabelPosition: "t", dataLabelFontSize: 8, dataLabelFontFace: BF, dataLabelColor: C.ORANGE, dataLabelFormatCode: o.fmt2 || "0%" } },
  ];
  s.addChart(types, {
    x, y, w, h, showLegend: true, legendPos: "b", legendFontSize: 8.5, legendFontFace: BF,
    valAxes: [
      { showValAxisTitle: false, valAxisHidden: true, valGridLine: { style: "none" }, valAxisMinVal: o.min1 ?? 0, valAxisMaxVal: o.max1 },
      { showValAxisTitle: false, valAxisHidden: true, valGridLine: { style: "none" }, valAxisMinVal: o.min2 ?? 0, valAxisMaxVal: o.max2 },
    ],
    catAxes: [{ catAxisTitle: "", catAxisLabelColor: "595959", catAxisLabelFontSize: 9, catAxisLabelFontFace: BF }, { catAxisHidden: true }],
  });
}

// table: header row navy; rows are arrays of strings (markup allowed)
function table(s, header, rows, x, y, w, o = {}) {
  const size = o.size || 9;
  const hdr = header.map((h) => ({ text: h, options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontFace: BF, fontSize: size, align: "center", valign: "middle" } }));
  const body = rows.map((r, ri) => r.map((c, ci) => {
    const fill = o.highlightRow === ri ? C.LBLUE : (ri % 2 ? C.GRAY : C.WHITE);
    return { text: parse(String(c), { fontFace: BF, fontSize: size, color: C.DGRAY }), options: { fill: { color: fill }, align: ci === 0 && !o.centerFirst ? "left" : (o.align || "center"), valign: "middle", bold: o.boldFirst && ci === 0 } };
  }));
  s.addTable([hdr, ...body], { x, y, w, colW: o.colW, rowH: o.rowH || 0.26, border: { type: "solid", pt: 0.5, color: "D0D0D0" }, margin: [2, 4, 2, 4], autoPage: false });
}

module.exports = { C, HF, BF, makePres, parse, title, source, banner, sub, box, panel, bullets, text, badge, stat, bar, line, combo, table, chartTitle };
