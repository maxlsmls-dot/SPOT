const L = require("./lib");
const { C, HF, BF } = L;

const f0 = (v) => (v == null ? "" : v < 0 ? `(${Math.abs(v).toLocaleString("en-US", { maximumFractionDigits: 0 })})` : v.toLocaleString("en-US", { maximumFractionDigits: 0 }));
const p1 = (v) => (v == null ? "" : (v * 100).toFixed(1) + "%");
const YR = ["FY25A", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"];

function divider(pres, text) {
  const s = pres.addSlide({ masterName: "BLANK_BRAND", sectionTitle: "Appendix" });
  s.addText("FTAI Aviation", { x: 0.55, y: 0.35, w: 6, h: 0.45, fontFace: HF, fontSize: 22, bold: true, color: C.NAVY, margin: 0, isTextBox: true });
  s.addText("(NASDAQ: FTAI)", { x: 0.55, y: 0.8, w: 6, h: 0.35, fontFace: HF, fontSize: 16, color: C.NAVY, margin: 0, isTextBox: true });
  s.addText(text, { x: 1, y: 3.2, w: 11.33, h: 1, fontFace: HF, fontSize: 40, bold: true, color: C.NAVY, align: "center", margin: 0, isTextBox: true });
  return s;
}

function grid(s, header, rows, x, y, w, o = {}) {
  const size = o.size || 8.5;
  const hdr = header.map((h, i) => ({ text: h, options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontFace: BF, fontSize: size, align: i ? "right" : "left" } }));
  const body = rows.map((r) => {
    const bold = r.bold, sec = r.section;
    return r.cells.map((c, i) => ({ text: c, options: { fontFace: BF, fontSize: size, color: sec ? C.NAVY : C.DGRAY, bold: bold || sec, italic: r.italic, align: i ? "right" : "left",
      fill: { color: sec ? C.LBLUE : C.WHITE }, border: r.top ? [{ type: "solid", pt: 0.75, color: C.NAVY }, { type: "none" }, { type: "none" }, { type: "none" }] : { type: "none" } } }));
  });
  s.addTable([hdr, ...body], { x, y, w, colW: o.colW, rowH: o.rowH || 0.2, margin: [1, 4, 1, 4], autoPage: false });
}
const R = (label, vals, fmt = f0, o = {}) => ({ cells: [label, ...vals.map(fmt)], ...o });
const S = (label, n = 7) => ({ cells: [label, ...Array(n).fill("")], section: true });

module.exports = async function (pres) {
  divider(pres, "Q&A");
  divider(pres, "Appendix");

  // ---------- Operating model
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Appendix" });
    L.title(s, "Appendix: Operating Model & Cash Flow (Base)");
    grid(s, ["$M", ...YR], [
      S("Revenue"),
      R("Aerospace Products", [1936, 3474, 5150, 6258, 6794, 7147, 7473]),
      R("FTAI Power", [0, 50, 1125, 2250, 2750, 3000, 3250]),
      R("Aviation Leasing + SCI", [571, 330, 300, 285, 275, 265, 255]),
      R("Total revenue", [2508, 3854, 6575, 8793, 9819, 10412, 10978], f0, { bold: true, top: true }),
      R("   y/y growth", [null, 0.537, 0.706, 0.337, 0.117, 0.06, 0.054], p1, { italic: true }),
      S("Adj. EBITDA"),
      R("Aerospace Products", [671, 1045, 1541, 1920, 2134, 2289, 2431]),
      R("   margin", [0.347, 0.301, 0.299, 0.307, 0.314, 0.32, 0.325], p1, { italic: true }),
      R("FTAI Power", [0, 20, 450, 900, 1100, 1200, 1300]),
      R("Aviation Leasing + SCI", [609, 475, 455, 440, 430, 420, 410]),
      R("Corporate & eliminations", [-82, -230, -207, -215, -225, -235, -245]),
      R("Total adj. EBITDA", [1198, 1310, 2239, 3045, 3439, 3674, 3896], f0, { bold: true, top: true }),
      R("   margin", [0.478, 0.34, 0.34, 0.346, 0.35, 0.353, 0.355], p1, { italic: true }),
      S("Unlevered free cash flow"),
      R("NOPAT", [null, 683, 1388, 1975, 2253, 2417, 2571]),
      R("(+) D&A and SBC", [null, 225, 230, 229, 229, 232, 235]),
      R("(–) Change in NWC", [null, -355, -476, -190, -232, -147, -138]),
      R("(–) Capex (leasing + PP&E)", [null, -229, -156, -172, -175, -176, -177]),
      R("(+) Leasing asset sales", [null, 410, 250, 25, 0, 0, 0]),
      R("(–) SCI investment, net of distributions", [null, -221, -191, -89, -89, -89, -89]),
      R("UFCF", [null, 512, 1045, 1778, 1987, 2237, 2403], f0, { bold: true, top: true }),
      R("   % of adj. EBITDA", [null, 0.391, 0.467, 0.584, 0.578, 0.609, 0.617], p1, { italic: true }),
      R("Net debt / adj. EBITDA", [2.63, 2.32, 1.08, 0.35, -0.14, -0.61, -1.06], (v) => v.toFixed(1) + "x"),
      S("vs. Jefferies (2-Aug-26)"),
      R("Total adj. EBITDA: Jefferies", [null, 1289, 2099, 3023, null, null, null]),
      R("   GPS vs Jefferies", [null, 21, 140, 22, null, null, null]),
    ], 0.45, 1.15, 12.43, { colW: [3.73, 1.24, 1.24, 1.24, 1.24, 1.24, 1.24, 1.26], rowH: 0.205, size: 8.5 });
    L.source(s, "GPS model (Operating Model tab); Jefferies estimates (2-Aug-26)");
  }

  // ---------- Revenue build
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Appendix" });
    L.title(s, "Appendix: Aerospace Products Revenue Build (Base)");
    grid(s, ["", ...YR], [
      S("CFM56 fleet & shop demand"),
      R("CFM56-7B EoP fleet", [13809, 13654, 13381, 13114, 12786, 12466, 12092]),
      R("   retirement rate", [0.013, 0.015, 0.02, 0.02, 0.025, 0.025, 0.03], p1, { italic: true }),
      R("CFM56-5B EoP fleet", [8903, 8759, 8540, 8284, 7994, 7714, 7406]),
      R("   retirement rate", [0.013, 0.02, 0.025, 0.03, 0.035, 0.035, 0.04], p1, { italic: true }),
      R("Total shop visits", [2350, 2385, 2386, 2318, 2219, 2120, 2056]),
      R("Module demand (3 per visit)", [7050, 7156, 7159, 6953, 6656, 6359, 6168], f0, { bold: true, top: true }),
      S("FTAI volume"),
      R("FTAI third-party share", [0.096, 0.124, 0.168, 0.19, 0.195, 0.2, 0.2], p1),
      R("Third-party modules", [675, 865, 1206, 1321, 1298, 1272, 1234]),
      R("SCI aircraft (EoP)", [130, 316, 450, 550, 650, 700, 750]),
      R("SCI modules (20% SV rate, 2 engines)", [82, 328, 482, 660, 780, 840, 900]),
      R("FTAI modules produced", [757, 1193, 1687, 1981, 2078, 2112, 2134], f0, { bold: true, top: true }),
      S("Price & margin"),
      R("Revenue per module ($M)", [2.558, 2.911, 3.052, 3.159, 3.27, 3.384, 3.502], (v) => v.toFixed(2)),
      R("Aerospace revenue ($M)", [1936, 3474, 5150, 6258, 6794, 7147, 7473]),
      R("EBITDA margin ex-PMA", [0.347, 0.301, 0.298, 0.303, 0.308, 0.312, 0.315], p1),
      R("PMA penetration", [0, 0, 0.009, 0.03, 0.05, 0.07, 0.09], p1),
      R("PMA uplift ($M, $0.4M / module)", [0, 0, 6, 24, 42, 59, 77]),
      R("Aerospace adj. EBITDA ($M)", [671, 1045, 1541, 1920, 2134, 2289, 2431], f0, { bold: true, top: true }),
      R("EBITDA per module ($K)", [887, 876, 913, 969, 1027, 1084, 1139]),
    ], 0.45, 1.15, 12.43, { colW: [3.73, 1.24, 1.24, 1.24, 1.24, 1.24, 1.24, 1.26], rowH: 0.24, size: 8.5 });
    L.source(s, "GPS model (RPM, Assumptions tabs); GE / CFM shop-visit outlook");
  }

  // ---------- DCF sensitivities
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Appendix" });
    L.title(s, "Appendix: DCF Sensitivities");
    const tg = [["8.5%", 293.41, 314.17, 338.69, 368.13, 404.10], ["9.0%", 269.08, 286.45, 306.71, 330.66, 359.40], ["9.5%", 248.01, 262.71, 279.68, 299.47, 322.85],
      ["10.0%", 229.6, 242.16, 256.52, 273.09, 292.41], ["10.5%", 213.37, 224.2, 236.47, 250.49, 266.67], ["11.0%", 198.97, 208.36, 218.94, 230.92, 244.62]];
    const em = [["8.5%", 304.41, 328.31, 352.22, 376.12, 400.03], ["9.0%", 296.82, 320.13, 343.44, 366.75, 390.06], ["9.5%", 289.46, 312.19, 334.92, 357.65, 380.38],
      ["10.0%", 282.3, 304.47, 326.63, 348.8, 370.97], ["10.5%", 275.34, 296.96, 318.58, 340.21, 361.83], ["11.0%", 268.58, 289.67, 310.76, 331.85, 352.94]];
    const heat = (v) => (v >= 330 ? "B7DDBF" : v >= 280 ? "DCEFD9" : v >= 240 ? "FFF2CC" : "F8D7CF");
    const mk = (title, hdr, rows, x) => {
      L.sub(s, title, x, 1.2, 6.1);
      const h = [{ text: "WACC", options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontSize: 9, fontFace: BF, align: "center" } },
        ...hdr.map((t) => ({ text: t, options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontSize: 9, fontFace: BF, align: "center" } }))];
      const b = rows.map((r) => [{ text: r[0], options: { bold: true, fontSize: 9, fontFace: BF, color: C.NAVY, fill: { color: C.LBLUE }, align: "center" } },
        ...r.slice(1).map((v, j) => ({ text: "$" + v.toFixed(0), options: { fontSize: 9, fontFace: BF, color: C.DGRAY, align: "center", fill: { color: heat(v) }, bold: r[0] === "9.5%" && j === 2 } }))]);
      s.addTable([h, ...b], { x, y: 1.6, w: 6.1, colW: [1.1, 1, 1, 1, 1, 1], rowH: 0.36, border: { type: "solid", pt: 0.5, color: "FFFFFF" } });
    };
    mk("Perpetuity Growth Method (Terminal Growth Rate)", ["2.0%", "2.5%", "3.0%", "3.5%", "4.0%"], tg, 0.45);
    mk("Exit Multiple Method (EV / EBITDA)", ["11.0x", "12.0x", "13.0x", "14.0x", "15.0x"], em, 6.78);
    L.sub(s, "WACC Build", 0.45, 4.35, 6.1);
    L.table(s, ["Input", "Value"], [["Risk-free rate", "4.2%"], ["Market risk premium", "4.5%"], ["Adjusted beta (0.67 × 1.51 raw + 0.33)", "1.34"], ["Cost of equity", "10.2%"], ["After-tax cost of debt (7.2% pre-tax, 21.4% tax)", "5.7%"], ["E / (D+E)", "83% / 17%"], ["**WACC**", "**9.5%**"]],
      0.45, 4.7, 6.1, { colW: [4.3, 1.8], rowH: 0.29, size: 9 });
    L.sub(s, "Reward / Risk (Blended DCF By Case)", 6.78, 4.35, 6.1);
    L.table(s, ["Case", "Perpetuity", "Exit", "Blended", "vs $167"], [["Bull", "$356", "$419", "$387", "+132%"], ["Base", "$281", "$335", "$308", "+84%"], ["Bear", "$87", "$118", "$103", "–39%"]],
      6.78, 4.7, 6.1, { colW: [1.3, 1.2, 1.2, 1.2, 1.2], rowH: 0.3, size: 9, highlightRow: 1 });
    L.panel(s, "**R/R skew: 132% / 39% = 3.4x**", 6.78, 5.95, 6.1, 0.5, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 12, align: "center", round: false });
    L.source(s, "GPS model (DCF, WACC tabs; case toggle recalculated)");
  }

  // ---------- Power model
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Appendix" });
    L.title(s, "Appendix: Power Model & Market Build");
    grid(s, ["FTAI Power (base)", ...YR], [
      R("Mod-1 units delivered", [0, 2, 45, 90, 110, 120, 130]),
      R("MW per unit", [25, 25, 25, 25, 25, 25, 25]),
      R("MW delivered", [0, 50, 1125, 2250, 2750, 3000, 3250]),
      R("$M per MW", [1, 1, 1, 1, 1, 1, 1], (v) => v.toFixed(2)),
      R("FTAI Power revenue ($M)", [0, 50, 1125, 2250, 2750, 3000, 3250], f0, { bold: true, top: true }),
      R("EBITDA margin", [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4], p1, { italic: true }),
      R("FTAI Power adj. EBITDA ($M)", [0, 20, 450, 900, 1100, 1200, 1300], f0, { bold: true }),
      R("Bear units / Bull units", [0, 0, 30, 45, 50, 50, 50], (v) => String(v)),
      R("", [0, 2, 55, 130, 150, 160, 170], (v) => String(v), { italic: true }),
    ], 0.45, 1.15, 12.43, { colW: [3.73, 1.24, 1.24, 1.24, 1.24, 1.24, 1.24, 1.26], rowH: 0.24, size: 9 });
    grid(s, ["US power market (GW unless noted)", "2026", "2027", "2028", "2029", "2030", "2031"], [
      R("US data center energy demand (TWh)", [298, 372, 464, 549, 649, 746]),
      R("Tracked hyperscaler planning capacity", [1.5, 3.9, 5.9, 7.7, 9.6, 11.2], (v) => v.toFixed(1)),
      R("Reserve shortfall: PJM", [0, 0, 0, 8.4, 21.6, 36.9], (v) => v.toFixed(1)),
      R("Reserve shortfall: MISO", [0, 0, 0, 0, 5.5, 9.0], (v) => v.toFixed(1)),
      R("Reserve shortfall: total", [0, 0, 0, 8.4, 27.2, 47.2], (v) => v.toFixed(1), { bold: true, top: true }),
      R("Regions below requirement", [0, 0, 0, 1, 2, 5], (v) => String(v)),
    ], 0.45, 3.65, 12.43, { colW: [3.73, 1.45, 1.45, 1.45, 1.45, 1.45, 1.45], rowH: 0.24, size: 9 });
    L.box(s, "**Method:** NERC 2025 LTRA regional demand and anticipated capacity by assessment area, reserve margin requirement applied; 67 hyperscaler power agreements tracked by COD and delivery haircut (no incremental capacity credited to NERC in base). Big Four CY26 capex $732.5bn; capex/PPA correlation 0.89 in levels, 0.34 in log growth", 0.45, 5.6, 12.43, 0.9, { size: 9.5 });
    L.source(s, "GPS model (Power outlook, Power Market Assumptions, Regional model, Power agreements tabs); NERC 2025 LTRA");
  }
};
