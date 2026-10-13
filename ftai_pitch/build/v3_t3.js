const G = require("./g");
const { C, F } = G;

const ax = { catAxisLabelFontFace: F, valAxisLabelFontFace: F, catAxisLabelFontSize: 9, valAxisLabelFontSize: 9, catAxisLabelColor: "262626", valAxisLabelColor: "262626",
  dataLabelFontFace: F, dataLabelFontSize: 8.5, legendFontFace: F, legendFontSize: 9, catGridLine: { style: "none" }, valGridLine: { style: "none" }, catAxisLineColor: "7F7F7F",
  titleFontFace: F, titleFontSize: 10.5, titleColor: "262626", showTitle: true };

function tbl(s, hdr, rows, x, y, w, colW, o = {}) {
  const sz = o.size || 10;
  const H = hdr.map((t) => ({ text: t, options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontFace: F, fontSize: sz, align: "center" } }));
  s.addTable([H, ...rows.map((r, i) => r.map((c, j) => ({ text: G.parse(String(c), { fontFace: F, fontSize: sz, color: C.TXT }),
    options: { align: j === 0 || o.leftAll ? "left" : "center", fill: { color: o.hiRow === i ? "FBE5D6" : (i % 2 ? "F2F2F2" : C.WHITE) } } })))],
    { x, y, w, colW, rowH: o.rowH || 0.22, border: { type: "solid", pt: 0.5, color: "BFBFBF" }, margin: [1, 3, 1, 3] });
}
const vline = (s, x, y, h) => s.addShape("line", { x, y, w: 0, h, line: { color: C.TXT, width: 1, dashType: "sysDot" } });

// ======================= SLIDE 1: shortfall + the first order
async function slide1(pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "Thesis III: Variance on Power – The Grid Gap Is Where the First Order Came From");
  const X = 0.68, W = 12.25, L = 0.68, LW = 6.0, R = 6.93, RW = 6.0;

  // ---- top tier
  G.head(s, "Hyperscaler capex is outrunning contracted power – and NERC reserves go short from 2029.", X, 0.88, W, { size: 13.5 });
  s.addChart(pres.charts.BAR, [{ name: "Capex", labels: ["2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026E"], values: [69, 95, 128, 151, 147, 228, 376, 733] }],
    { x: L, y: 1.28, w: 3.0, h: 1.72, barDir: "col", chartColors: [C.NAVY], barGapWidthPct: 35, showValue: true, dataLabelPosition: "outEnd", dataLabelColor: "262626",
      dataLabelFormatCode: "#,##0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 860, showLegend: false, ...ax, catAxisLabelFontSize: 8, title: "Big Four Capex ($bn)" });
  s.addChart(pres.charts.BAR, [{ name: "PPA", labels: ["2019", "2020", "2021", "2022", "2023", "2024", "2025"], values: [16, 16, 19, 21, 17, 29.1, 29.5] }],
    { x: L + 3.05, y: 1.28, w: 2.95, h: 1.72, barDir: "col", chartColors: ["2E75B6"], barGapWidthPct: 35, showValue: true, dataLabelPosition: "outEnd", dataLabelColor: "262626",
      dataLabelFormatCode: "0", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 36, showLegend: false, ...ax, catAxisLabelFontSize: 8, title: "US Corporate PPAs Signed (GW)" });
  G.bullets(s, [
    "Capex and PPAs tracked each other for a decade (++0.89 correlation++); in 2025 capex rose ++65%++ while PPAs were ++flat at ~29.5 GW++",
    "**Our build:** $733bn × 65% US × 25% facility ÷ $12M / MW ≈ ++9.9 GW of shells funded in 2026 alone++",
  ], L, 3.03, LW, 0.78, { size: 10.5, psa: 1 });
  vline(s, R - 0.12, 1.3, 2.5);
  s.addChart(pres.charts.BAR, [
    { name: "PJM", labels: ["2026", "2027", "2028", "2029", "2030", "2031"], values: [0, 0, 0, 8.4, 21.6, 36.9] },
    { name: "MISO", labels: ["2026", "2027", "2028", "2029", "2030", "2031"], values: [0, 0, 0, 0, 5.5, 9.0] },
    { name: "Other", labels: ["2026", "2027", "2028", "2029", "2030", "2031"], values: [0, 0, 0, 0, 0, 1.2] },
  ], { x: R, y: 1.28, w: 2.9, h: 2.0, barDir: "col", barGrouping: "stacked", chartColors: [C.NAVY, C.ORANGE, "A6A6A6"], barGapWidthPct: 40, showValue: false,
    valAxisHidden: true, showLegend: true, legendPos: "b", ...ax, title: "Reserve Shortfall (GW)^1".slice(0, -2) });
  [["8.4", 1.67, 2.3], ["27.2", 2.14, 1.9], ["47.2", 2.62, 1.5]].forEach(([t, dx, y]) => s.addText(t, { x: R + dx - 0.25, y, w: 0.5, h: 0.18, align: "center", fontFace: F, fontSize: 9, bold: true, color: C.TXT, margin: 0, isTextBox: true }));
  G.bullets(s, [
    "US DC demand ++298 → 746 TWh++ (2026–31)",
    "ERCOT large-load queue ++~475 GW++, 90% data centers",
    "PJM auctions cleared ++~6.8 GW short++ (2028/29)",
    "Grid interconnection: median ++>5 yrs++",
    "OEM gas-turbine backlog ++~220 GW++; new slots ++2028 onward++",
  ], R + 2.95, 1.3, RW - 2.95, 2.0, { size: 10, psa: 2, valign: "middle" });
  s.addShape("rect", { x: R, y: 3.32, w: RW, h: 0.48, fill: { color: C.GRAY }, line: { color: C.GRAY } });
  G.para(s, "~57% of hyperscaler power contracted lands ++2029 or later++ – a 2–3 year gap only ++fast, on-site generation++ can fill", R + 0.04, 3.32, RW - 0.08, 0.48, { size: 10.5, valign: "middle" });

  // ---- bottom tier
  G.head(s, "The $1.465bn first order came from a site at exactly that stage: built, energized on mobile gas, and out of turbines.", X, 3.88, W, { size: 13.5 });
  tbl(s, ["Term", "The order (22-Jul-26)"], [
    ["Seller", "J&F Power Systems (FTAI × Jereh JV)"], ["Buyer", "“Leading international cloud provider” – ++reported xAI++"],
    ["Size", "++$1.465bn++ initial PO; 5-yr MSA, re-order w/o renegotiation"], ["Implied", "~58 Mod-1 units at ~$25M ≈ ++1.45 GW++"],
    ["Delivery", "Batches through ++Nov-27++; advance + milestone pay"],
  ], L, 4.28, 4.1, [0.85, 3.25], { rowH: 0.27, size: 9.5, leftAll: true });
  G.para(s, "**++What “the xAI stage” looked like (Colossus 2 / Southaven)++**", L + 4.25, 4.26, W - 4.25, 0.26, { size: 11.5, align: "center" });
  const stage = [
    ["1", "Shell built, GPUs committed", "~1 GW live Jan-26; $20bn Southaven DC under way"],
    ["2", "No grid for the next phase", "MLGW supplies ++no power++ to Colossus 2; no TVA allocation"],
    ["3", "Behind-the-meter gas permitted", "++41 turbines (~1.2 GW)++ permitted Mar-26; gas lateral in place"],
    ["4", "Incumbent supply tapped out", "Solaris ~900 MW fleet committed; OEM aero slots ++2028 onward++"],
  ];
  stage.forEach((r, i) => {
    const y = 4.54 + i * 0.36;
    s.addShape("ellipse", { x: L + 4.27, y: y + 0.06, w: 0.26, h: 0.26, fill: { color: C.ORANGE }, line: { color: C.ORANGE } });
    s.addText(r[0], { x: L + 4.27, y: y + 0.06, w: 0.26, h: 0.26, align: "center", valign: "middle", fontFace: F, fontSize: 10.5, bold: true, color: C.WHITE, margin: 0, isTextBox: true });
    G.para(s, `**${r[1]}**`, L + 4.6, y, 2.7, 0.38, { size: 10.5, valign: "middle" });
    G.para(s, r[2], L + 7.3, y, W - 7.3, 0.38, { size: 10.5, valign: "middle" });
  });
  G.para(s, "Diligence flag: FTAI hasn't named the buyer; the xAI link rests on Jereh gensets on the Southaven equipment list (CV Research). ++The order is signed either way++.", L, 6.0, W, 0.4, { size: 10, color: C.MUTE });

  G.banner(s, "The grid falls 8–47 GW short from 2029; sites at the first buyer's stage need power in 2027–28 that only mobile units can deliver.", X, 6.48, W, 0.44, 14);
  G.source(s, "Company filings (AMZN, GOOGL, META, MSFT), BCSE / BNEF, NERC 2025 LTRA, ERCOT, PJM, FTAI release (22-Jul-26), MDEQ, DCD, SemiAnalysis, GPS Model",
    ["GPS regional model: NERC demand vs. anticipated capacity + 67 tracked hyperscaler power agreements."]);
}

// ======================= SLIDE 2: pipeline + ramp + right to win
async function slide2(pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "Thesis III: Variance on Power – A Pipeline at the First Buyer's Stage and a Right to Win");
  const X = 0.68, W = 12.25, L = 0.68;

  G.head(s, "We screened 24 US AI campuses: 9 meet the first buyer's conditions – ~10 GW of load with no locked bridge supplier.", X, 0.88, W, { size: 13.5 });
  tbl(s, ["Project (tenant)", "Location", "Target", "Power plan today", "Grid timing", "Need", "FTAI win"], [
    ["Amazon “GW Ranch”", "Pecos Co., TX", "≤7.6 GW gen", "Off-grid; 35-turbine permit, mixed sizes", "Undefined", "High", "**High**"],
    ["Poolside / CoreWeave “Horizon”", "Pecos Co., TX", "2 GW", "Behind-the-meter; no supplier named", "None planned", "High", "**High**"],
    ["Project Jade (Tallgrass)", "Cheyenne, WY", "1.8 GW", "CCGT + “++temporary aeroderivatives++”", "Off-grid", "High", "**High**"],
    ["Google / Crusoe “Goodnight”", "Armstrong Co., TX", "Multi-100 MW", "933 MW aeros, not sourced from GE", "Partial", "High", "Med"],
    ["Meta El Paso", "El Paso, TX", "1 GW", "366 MW utility plant stalled at PUC", "2027 if approved", "High", "Med"],
    ["Microsoft / Chevron “Kilby”", "Pecos area, TX", "2–2.5 GW", "Chevron BTM; first power 2028", "n/a", "Med-High", "Med"],
    ["Cipher “Colchis” / Stargate Milam / Nebius", "TX, MO", "~3.3 GW", "AEP 2028; solar + storage; new plant Oct-27", "2027–28", "Med", "Med"],
  ], L, 1.28, W, [2.75, 1.4, 1.15, 3.8, 1.3, 0.95, 0.9], { rowH: 0.24, size: 9.5 });
  G.para(s, "**Screened out:** Stargate Jupiter → Bloom; Frontier → VoltaGrid; Prometheus → Williams; Homer City → GE 7HA. **Grid-led:** Saline, Lighthouse, Fairwater, Helios, Sweetwater. ++One High site ≈ another first order++.", L, 3.28, W, 0.48, { size: 10.5 });

  G.head(s, "FTAI can roll units faster than the street models – and its units are cheap, available now and mobile.", X, 3.84, W, { size: 13.5 });
  s.addChart(pres.charts.BAR, [
    { name: "Bear", labels: ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E"], values: [0, 30, 45, 50, 50] },
    { name: "Base", labels: ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E"], values: [2, 45, 90, 110, 120] },
    { name: "Bull", labels: ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E"], values: [2, 55, 130, 150, 160] },
  ], { x: L, y: 4.22, w: 3.3, h: 2.2, barDir: "col", chartColors: ["A6A6A6", C.NAVY, C.ORANGE], barGapWidthPct: 35, showValue: true, dataLabelPosition: "outEnd",
    dataLabelColor: "262626", dataLabelFontSize: 7.5, dataLabelFormatCode: "0;;;", valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 185, showLegend: true, legendPos: "b", ...ax, title: "Mod-1 Units Delivered" });
  G.bullets(s, [
    "**Feedstock in hand:** 1,000+ owned CFM56s; no new hot section",
    "**Capacity:** 100+ units / yr; ~$400M of Power WC built / planned",
    "**Packaging outsourced** to Jereh (US, Canada, UAE, China)",
    "**Base 45 units FY27** < the ~58 implied by the signed order; mgmt's $450M assumes “materially less” than 100",
    "**Path:** launch Dec-25 → prototype 1H26 → order Jul-26 → first deliveries 2027",
  ], L + 3.35, 4.22, 3.0, 2.2, { size: 9.5, psa: 1, valign: "middle" });
  vline(s, L + 6.45, 4.24, 2.17);
  const R = L + 6.55, RW = W - 6.55;
  tbl(s, ["Supplier", "Earliest slot", "$ / kW"], [["**FTAI Mod-1**", "**2027**", "**~$1,000**"], ["GE Vernova aeros", "2028–30", "$1,400–2,000"], ["MHI / Siemens frames", "2028–30 / 3+ yrs", "~$2,000+"], ["Boom (Crusoe exited)", "250 MW 2027", "~$1,030"]],
    R, 4.22, 3.4, [1.55, 1.05, 0.8], { rowH: 0.24, size: 9, hiRow: 0 });
  G.bullets(s, [
    "Turbines ≈ ++13% of shell cost++ (~2% all-in)",
    "Idle AI site ≈ ++$1M / MW / month++ → a $1M/MW unit ++pays back in ~1 month++",
    "**Mobile:** redeploys when the grid arrives",
  ], R + 3.45, 4.22, RW - 3.45, 1.25, { size: 9.5, psa: 1, valign: "middle" });
  tbl(s, ["FY27E", "Units", "Power EBITDA", "Value @ 12x"], [["Signed order only", "45", "$450M", "$52 / sh"], ["+1 contract (~1 GW)", "~90", "~$750M", "**+$35 / sh**"], ["+2 contracts", "~130", "~$1.05bn", "**+$70 / sh**"]],
    R, 5.58, RW, [1.75, 0.8, 1.35, 1.8], { rowH: 0.22, size: 9.5 });

  G.banner(s, "Power is a free call option: ~10 GW sits at the first buyer's stage, and each ~1 GW contract FTAI wins adds ~$35 / share.", X, 6.48, W, 0.44, 14);
  G.source(s, "Company releases, TCEQ / MDEQ filings, Cleanview, Epoch AI, DCD, GE Vernova / Siemens Energy / MHI Q2'26, GridLab, JLL, FTAI calls, GPS Model",
    ["Win-ability = gas access + BTM permitting + no locked supplier + 2026–28 load date. Value per share at 12x Power EBITDA, 104.0M shares."]);
}

module.exports = async function (pres) { await slide1(pres); await slide2(pres); };
