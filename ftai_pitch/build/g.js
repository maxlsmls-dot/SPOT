// House style (CarGurus deck): Garamond, navy rules, banner takeaways, underlined emphasis
const pptxgen = require("pptxgenjs");

const C = { NAVY: "1F3864", INK: "203040", TXT: "1A1A1A", GRAY: "D9D9D9", LGRAY: "EDEDED", BLUE: "9DC3E6", ORANGE: "E8702A", TEAL: "2E8FAE", WHITE: "FFFFFF", RED: "C00000", MUTE: "595959" };
const F = "Garamond";

function makePres() {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.author = "Max Salomon";
  pres.company = "FTAI Long Pitch";
  pres.title = "FTAI Aviation - Long Recommendation";
  pres.theme = { headFontFace: F, bodyFontFace: F };
  pres.defineSlideMaster({
    title: "Pitch",
    background: { color: C.WHITE },
    objects: [
      { line: { x: 0.68, y: 0.84, w: 12.25, h: 0, line: { color: C.NAVY, width: 3 } } },
      { line: { x: 0.68, y: 7.05, w: 12.25, h: 0, line: { color: C.NAVY, width: 3 } } },
      { text: { text: "FTAI", options: { x: 11.55, y: 0.12, w: 0.62, h: 0.32, align: "right", fontFace: "Calibri", fontSize: 15, bold: true, color: C.NAVY, margin: 0 } } },
      { text: { text: "AVIATION", options: { x: 12.2, y: 0.12, w: 1.1, h: 0.32, align: "left", fontFace: "Calibri", fontSize: 15, color: C.TEAL, margin: 0 } } },
      { placeholder: { options: { name: "title", type: "title", x: 0.68, y: 0.3, w: 12.25, h: 0.52, fontFace: F, fontSize: 25, color: C.INK, valign: "bottom", align: "left", margin: 0 }, text: "" } },
    ],
    slideNumber: { x: 12.55, y: 7.1, w: 0.4, h: 0.3, fontFace: F, fontSize: 12, color: C.TXT, align: "right" },
  });
  return pres;
}

// markup: **bold**  ++underline++  __italic__  ~~orange bold~~  ^^superscript^^
function parse(str, base = {}) {
  const out = [];
  const re = /(\*\*[^*]+\*\*|\+\+[^+]+\+\+|__[^_]+__|~~[^~]+~~|\^\^[^^]+\^\^)/g;
  let last = 0, m;
  const push = (t, o) => out.push({ text: t, options: { ...base, ...o } });
  while ((m = re.exec(str))) {
    if (m.index > last) push(str.slice(last, m.index), {});
    const t = m[0], inner = t.slice(2, -2);
    if (t.startsWith("**")) {
      // allow nested underline inside bold
      inner.split(/(\+\+[^+]+\+\+)/).filter(Boolean).forEach((p) => p.startsWith("++") ? push(p.slice(2, -2), { bold: true, underline: { style: "sng" } }) : push(p, { bold: true }));
    } else if (t.startsWith("++")) push(inner, { underline: { style: "sng" } });
    else if (t.startsWith("__")) push(inner, { italic: true });
    else if (t.startsWith("~~")) push(inner, { bold: true, color: C.ORANGE });
    else push(inner, { superscript: true });
    last = m.index + t.length;
  }
  if (last < str.length) push(str.slice(last), {});
  return out;
}

const base = (o = {}) => ({ fontFace: F, fontSize: o.size || 13, color: o.color || C.TXT });

function title(s, t) { s.addText(t, { placeholder: "title" }); }

// italic bold subtitle under the title rule
function sub(s, t, o = {}) {
  s.addText(parse(t, { ...base({ size: o.size || 14, color: o.color || C.NAVY }), bold: true, italic: true }), { x: 0.68, y: 0.9, w: 12.25, h: o.h || 0.36, margin: 0, valign: "middle", align: o.align || "left", isTextBox: true });
}

// navy bar with white bold centered text
function banner(s, t, x, y, w, h = 0.38, size = 14) {
  s.addShape("rect", { x, y, w, h, fill: { color: C.NAVY }, line: { color: C.NAVY } });
  s.addText(parse(t, { fontFace: F, fontSize: size, color: C.WHITE, bold: true }), { x, y, w, h, align: "center", valign: "middle", margin: 2, isTextBox: true });
}

// centered bold header with thin rule below (CARG "... that has been secularly taking share" style)
function head(s, t, x, y, w, o = {}) {
  s.addText(parse(t, { fontFace: F, fontSize: o.size || 14, color: o.color || C.INK, bold: true }), { x, y, w, h: 0.3, align: o.align || "center", valign: "bottom", margin: 0, isTextBox: true });
  s.addShape("line", { x, y: y + 0.33, w, h: 0, line: { color: C.INK, width: 0.75 } });
}

function para(s, t, x, y, w, h, o = {}) {
  s.addText(parse(t, base(o)), { x, y, w, h, margin: o.margin ?? 2, valign: o.valign || "top", align: o.align || "left", isTextBox: true, lineSpacingMultiple: o.ls || 1.0 });
}

function bullets(s, items, x, y, w, h, o = {}) {
  const runs = [];
  items.forEach((it, i) => {
    const sub = typeof it === "object" && it.sub;
    const r = parse(sub ? it.t : it, base(o));
    r[0].options.bullet = o.num && !sub ? { type: "number", indent: 18 } : { indent: sub ? 14 : 14 };
    if (sub) r[0].options.indentLevel = 1;
    r[0].options.paraSpaceAfter = o.psa ?? 2;
    if (i < items.length - 1) r[r.length - 1].options.breakLine = true;
    runs.push(...r);
  });
  s.addText(runs, { x, y, w, h, margin: 2, valign: o.valign || "top", isTextBox: true });
}

// gray quote box
function quote(s, t, x, y, w, h, o = {}) {
  s.addShape("rect", { x, y, w, h, fill: { color: C.GRAY }, line: { color: C.GRAY } });
  para(s, t, x + 0.05, y, w - 0.1, h, { ...o, valign: "middle" });
}

// dashed box
function dash(s, x, y, w, h, color = C.TXT) {
  s.addShape("rect", { x, y, w, h, fill: { type: "none" }, line: { color, width: 1.25, dashType: "dash" } });
}

function source(s, t, notes) {
  s.addText(parse("Source: " + t, { fontFace: F, fontSize: 11, color: C.TXT }), { x: 0.68, y: 7.08, w: notes ? 7.6 : 11.5, h: 0.38, margin: 0, valign: "top", isTextBox: true });
  if (notes) s.addText(notes.map((n, i) => ({ text: `${i + 1}.  ${n}`, options: { fontFace: F, fontSize: 7, color: C.TXT, breakLine: i < notes.length - 1 } })), { x: 8.5, y: 7.08, w: 3.95, h: 0.4, margin: 0, valign: "top", isTextBox: true });
}

// two-col financial table, CARG style: alternating light-blue bold rows, italic sub-rows, header bar
function finTable(s, hdrText, rows, x, y, w, o = {}) {
  const rh = o.rowH || 0.235, size = o.size || 11;
  s.addShape("rect", { x, y, w, h: rh + 0.02, fill: { color: C.NAVY }, line: { color: C.NAVY } });
  s.addText(hdrText, { x, y, w, h: rh + 0.02, align: "center", valign: "middle", fontFace: F, fontSize: size, bold: true, color: C.WHITE, margin: 0, isTextBox: true });
  rows.forEach((r, i) => {
    const yy = y + (i + 1) * rh + 0.02, kind = r[2] || "";
    if (kind.includes("hi")) s.addShape("rect", { x, y: yy, w, h: rh, fill: { color: "DDEBF7" }, line: { color: "DDEBF7" } });
    const it = kind.includes("it"), b = kind.includes("hi") || kind.includes("b");
    s.addText(r[0], { x: x + (it ? 0.12 : 0.03), y: yy, w: w * 0.68, h: rh, fontFace: F, fontSize: size - (it ? 1 : 0), italic: it, bold: b, color: C.TXT, valign: "middle", margin: 0, isTextBox: true });
    s.addText(r[1], { x: x + w * 0.6, y: yy, w: w * 0.4 - 0.04, h: rh, fontFace: F, fontSize: size - (it ? 1 : 0), italic: it, bold: b, color: C.TXT, align: "right", valign: "middle", margin: 0, isTextBox: true });
    if (kind.includes("ul")) s.addShape("line", { x: x + w * 0.62, y: yy + rh - 0.02, w: w * 0.38 - 0.04, h: 0, line: { color: C.TXT, width: 0.75 } });
  });
  return y + (rows.length + 1) * rh + 0.02;
}

module.exports = { C, F, makePres, parse, title, sub, banner, head, para, bullets, quote, dash, source, finTable };
