const L = require("./lib");
const { C, HF, BF } = L;
const { icon } = require("./icons");
const D = require("./data");

module.exports = async function (pres) {
  // ---------- 1. COVER
  {
    const s = pres.addSlide({ masterName: "BLANK_BRAND", sectionTitle: "Introduction" });
    s.addText("FTAI Aviation (NASDAQ: FTAI)", { x: 0.55, y: 1.15, w: 8.5, h: 0.6, fontFace: HF, fontSize: 32, bold: true, color: C.NAVY, margin: 0, isTextBox: true });
    s.addText("Long Recommendation: The Trough Is Priced As A Cliff", { x: 0.55, y: 1.75, w: 8.5, h: 0.5, fontFace: HF, fontSize: 22, bold: true, color: C.ORANGE, margin: 0, isTextBox: true });
    L.bar(s, pres, 0.5, 2.45, 7.9, 3.55, D.yrs, [
      { name: "Aerospace Products", values: D.aeroEbitda },
      { name: "Leasing + SCI", values: D.leaseEbitda },
      { name: "FTAI Power", values: D.powerEbitda },
    ], { stacked: true, legend: true, colors: [C.NAVY, C.TEAL, C.ORANGE], title: "Segment Adj. EBITDA, FY25A–FY31E ($M, pre-corporate) — our base case", dlSize: 8, fmt: "#,##0;;;" });
    s.addText(parse2("October 2026  |  **Max Salomon**"), { x: 0.55, y: 6.15, w: 7, h: 0.3, margin: 0, isTextBox: true });
    s.addText(parse2("Current Price: **$167.03** (10/2/26)   |   Target Price: **$277** ({{+66%}})   |   Reward / Risk: **3.4x**"), { x: 0.55, y: 6.45, w: 8.5, h: 0.3, margin: 0, isTextBox: true });

    // key financials box
    const x = 8.95, y = 1.25, w = 3.95;
    s.addShape("rect", { x, y, w, h: 0.5, fill: { color: C.NAVY }, line: { color: C.NAVY } });
    s.addText("Key Financials", { x, y, w, h: 0.5, align: "center", valign: "middle", fontFace: HF, fontSize: 15, bold: true, color: C.WHITE, isTextBox: true });
    const rows = [
      ["Share price (2-Oct-26)", "$167.03"], ["Market cap", "$17.4bn"], ["Enterprise value", "$20.6bn"],
      ["EV / FY26E EBITDA", "15.7x"], ["EV / FY27E EBITDA", "9.2x"], ["FY27E UFCF conversion", "47%"],
      ["Net debt / FY26E EBITDA", "2.3x"], ["SOTP target (FY27E)", "$277"],
    ];
    s.addShape("rect", { x, y: y + 0.5, w, h: rows.length * 0.53 + 0.1, fill: { color: C.WHITE }, line: { color: C.NAVY, width: 1.25 } });
    rows.forEach((r, i) => {
      const yy = y + 0.6 + i * 0.53;
      s.addText(r[0], { x: x + 0.15, y: yy, w: 2.5, h: 0.45, fontFace: HF, fontSize: 11.5, bold: true, color: C.NAVY, valign: "middle", margin: 0, isTextBox: true });
      s.addText(r[1], { x: x + 2.5, y: yy, w: 1.3, h: 0.45, fontFace: HF, fontSize: 11.5, color: C.NAVY, align: "right", valign: "middle", margin: 0, isTextBox: true });
      if (i < rows.length - 1) s.addShape("line", { x: x + 0.15, y: yy + 0.49, w: w - 0.3, h: 0, line: { color: "D9D9D9", width: 0.5 } });
    });
    function parse2(t) { return L.parse(t, { fontFace: HF, fontSize: 13, color: C.NAVY }); }
    s.addNotes("Cover. Price as of 10/2/26 per model Cover tab. Target = FY27E SOTP (Aerospace 16x, Power 12x, Leasing+SCI 9x). R/R = blended DCF bull upside (+132%) / bear downside (-39%).");
  }

  // ---------- 2. PITCH PRE-REQUISITES
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Introduction" });
    L.title(s, "Pitch Pre-Requisites & Beliefs");
    L.banner(s, "What You Need To Believe For This Pitch", 0.45, 1.15, 12.43);
    const cols = [
      ["FaChartLine", "~30% Is The Floor, Not A Waypoint", "Cheap leasing stock is **<8% of inventory**, heavy-scope mix is capped by shop capacity, and **PMA runs through SCI's own engines**. Two more ~30% prints prove the trough and the multiple re-rates."],
      ["FaPlane", "The CFM56 Whitespace Becomes FTAI's", "OEMs and big MROs are moving slots to LEAP while LEAP keeps CFM56s flying. FTAI's capacity is **already built**; Cairo and Jakarta ramp in 2027 and take FTAI to **~25% of CFM56 module demand**."],
      ["FaBolt", "Power Is A Call Option, Paid For Free", "The grid falls **8–47 GW short from 2029**. FTAI's xAI order came at the shell-and-GPU stage; a long list of sites sit at that stage today without power. Turbines are **~13% of build cost** and move with the tenant."],
    ];
    for (let i = 0; i < 3; i++) {
      const x = 0.55 + i * 4.15;
      s.addShape("ellipse", { x: x + 0.05, y: 1.75, w: 1.1, h: 1.1, fill: { color: C.WHITE }, line: { color: C.NAVY, width: 2.5 } });
      s.addImage({ data: await icon(cols[i][0], "#0B1F44"), x: x + 0.33, y: 2.03, w: 0.54, h: 0.54 });
      L.text(s, cols[i][1], x + 1.3, 1.72, 2.75, 0.4, { font: HF, size: 12.5, bold: true, color: C.NAVY });
      L.text(s, cols[i][2], x + 1.3, 2.1, 2.75, 1.45, { size: 10, valign: "top" });
    }
    L.banner(s, "Pre-Requisites For Understanding", 0.45, 3.75, 6.1, 0.38, 13);
    const pre = [
      "**Aerospace Products is a module factory:** FTAI swaps restored CFM56 modules from its own pool, so margin is driven by feedstock cost, workscope mix and price, not labour hours",
      "**Two denominators matter:** FTAI's share of third-party module work (12% → 20%) and its share of **all** CFM56 module demand once captive SCI volume is added (17% → ~25%)",
      "**Power is valued on the signed order only.** Every new contract is upside; our bear case assumes half the JV economics and 30% margins",
    ];
    pre.forEach((t, i) => {
      L.badge(s, i + 1, 0.55, 4.33 + i * 0.86, 0.48);
      L.box(s, t, 1.15, 4.25 + i * 0.86, 5.4, 0.7, { size: 9.5 });
    });
    L.banner(s, "Valuation Summary", 6.78, 3.75, 6.1, 0.38, 13);
    const cases = [
      ["Bear Case", "20% Probability: $173 SOTP (+4%)", C.SLATE],
      ["Base Case", "60% Probability: $277 SOTP (+66%)", C.NAVY],
      ["Bull Case", "20% Probability: $308 SOTP (+85%)", C.TEAL],
    ];
    cases.forEach((c, i) => {
      const y = 4.3 + i * 0.6;
      L.panel(s, c[0], 6.78, y, 2.5, 0.45, { fill: c[2], color: C.WHITE, font: HF, size: 13, align: "center", round: false });
      L.box(s, `**${c[1]}**`, 9.45, y, 3.43, 0.45, { size: 10.5, align: "center" });
    });
    L.panel(s, "**Probability-weighted: $262 (+57%)  |  DCF cross-check: $308 (+84%)**", 6.78, 6.2, 6.1, 0.42, { fill: C.LBLUE, size: 11.5, align: "center", round: false });
    L.source(s, "FTAI filings; GPS model (FY27E SOTP by case, blended DCF)");
  }

  // ---------- 3. BUSINESS OVERVIEW
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Introduction" });
    L.title(s, "Business Overview");
    L.banner(s, "One Engine Family, Three Ways To Earn: Fix It, Own The Planes It Flies On, Power With It", 0.45, 1.15, 12.43);
    L.sub(s, "FY25 Revenue & EBITDA Mix", 0.45, 1.68, 4.0);
    s.addChart(pres.charts.DOUGHNUT, [{ name: "Revenue", labels: ["Aerospace Products", "Leasing + SCI"], values: [1936, 571] }], {
      x: 0.45, y: 2.05, w: 2.0, h: 2.2, holeSize: 55, chartColors: [C.NAVY, C.TEAL], showPercent: true, showValue: false, showLegend: false,
      dataLabelColor: C.WHITE, dataLabelFontSize: 9, dataLabelFontFace: BF, showTitle: true, title: "Revenue $2.5bn", titleFontSize: 9.5, titleColor: C.NAVY, titleFontFace: BF,
    });
    s.addChart(pres.charts.DOUGHNUT, [{ name: "EBITDA", labels: ["Aerospace Products", "Leasing + SCI"], values: [671, 609] }], {
      x: 2.45, y: 2.05, w: 2.0, h: 2.2, holeSize: 55, chartColors: [C.NAVY, C.TEAL], showPercent: true, showValue: false, showLegend: false,
      dataLabelColor: C.WHITE, dataLabelFontSize: 9, dataLabelFontFace: BF, showTitle: true, title: "Segment EBITDA $1.3bn", titleFontSize: 9.5, titleColor: C.NAVY, titleFontFace: BF,
    });
    L.text(s, "■ Aerospace Products   ■ Leasing + SCI", 0.45, 4.22, 4.0, 0.22, { size: 8.5, align: "center", color: C.NAVY });
    L.box(s, "Aerospace Products is **77% of revenue** but only half of EBITDA today; by FY27E it is **~63% of segment EBITDA** and Power adds a third leg", 0.45, 4.5, 4.0, 0.62, { size: 9.5 });
    L.sub(s, "How The Segments Work", 4.65, 1.68, 4.15);
    const segs = [
      ["Aerospace Products", "Restores and exchanges CFM56-5B/-7B modules (fan, core, LPT) and sells USM parts. FY25: **757 modules, $1.94bn revenue, 34.7% margin**"],
      ["Leasing + SCI", "Mid-life jets and engines. Leasing assets are being sold into **SCI**, an FTAI-sponsored fund that buys aircraft and sends **all engine work to FTAI** (316 aircraft YE26E)"],
      ["FTAI Power", "Converts CFM56-7B cores into **25 MW mobile gas turbines** for data centers. First order **$1.465bn** via JV; FY27 Power EBITDA guide **$450–750M**"],
    ];
    segs.forEach((g, i) => {
      const y = 2.08 + i * 1.02;
      L.panel(s, g[0], 4.65, y, 1.35, 0.9, { fill: [C.NAVY, C.TEAL, C.ORANGE][i], color: C.WHITE, font: HF, size: 11, align: "center", round: false });
      L.box(s, g[1], 6.05, y, 2.75, 0.9, { size: 9 });
    });
    L.sub(s, "Cap Table", 9.0, 1.68, 3.88);
    L.table(s, ["Item", "Value"], [
      ["Share price (10/2/26)", "$167.03"], ["Diluted shares (mm)", "104.0"], ["Market cap ($mm)", "17,378"], ["(-) Cash ($mm)", "(337)"],
      ["(+) Total debt ($mm)", "3,453"], ["(+) Preferred ($mm)", "65"], ["**Enterprise value ($mm)**", "**20,560**"], ["EV / FY27E EBITDA", "9.2x"],
    ], 9.0, 2.08, 3.88, { colW: [2.4, 1.48], rowH: 0.29, size: 9 });
    L.sub(s, "Financial Highlights (Base Case)", 0.45, 5.25, 12.43);
    L.bar(s, pres, 0.45, 5.6, 4.1, 1.38, ["FY25A", "FY26E", "FY27E", "FY28E"], [{ name: "Revenue", values: [2508, 3854, 6575, 8793] }], { title: "Total revenue ($M)", colors: [C.NAVY] });
    L.bar(s, pres, 4.6, 5.6, 4.1, 1.38, ["FY25A", "FY26E", "FY27E", "FY28E"], [{ name: "Modules", values: [757, 1193, 1687, 1981] }], { title: "Modules produced", colors: [C.TEAL] });
    L.bar(s, pres, 8.75, 5.6, 4.13, 1.38, ["FY25A", "FY26E", "FY27E", "FY28E"], [{ name: "EBITDA", values: [1198, 1310, 2239, 3045] }], { title: "Total adj. EBITDA ($M)", colors: [C.ORANGE] });
    L.source(s, "FTAI 10-K FY25, Q2'26 supplement; GPS model");
  }

  // ---------- 4. INDUSTRY OVERVIEW
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Introduction" });
    L.title(s, "Industry Overview: The CFM56 Aftermarket");
    L.banner(s, "The Best-Selling Engine Ever Built Is Entering Its Heaviest, Most Repeat-Heavy Maintenance Years", 0.45, 1.15, 12.43);
    L.sub(s, "Installed Fleet & OEM Shop-Visit Outlook", 0.45, 1.68, 6.1);
    L.bar(s, pres, 0.45, 2.05, 6.1, 2.65, ["FY25", "FY26", "FY27", "FY28", "FY29", "FY30", "FY31"],
      [{ name: "Shop visits", values: [2350, 2400, 2400, 2350, 2250, 2150, 2085] }], { colors: [C.NAVY], title: "CFM56-5B/-7B shop visits (GE central case); fleet 22.7k → 19.5k engines" });
    L.box(s, "**~22,700 engines** in service, **~2,350 shop visits/yr** → **~7,000 modules/yr** of demand. GE expects visits to **plateau through 2028**, and our base case only declines 2% a year after that", 0.45, 4.78, 6.1, 0.62, { size: 9.5 });
    L.sub(s, "Fleet By Completed Shop Visits: Older Engines Need More Work", 0.45, 5.5, 6.1);
    L.bar(s, pres, 0.45, 5.85, 6.1, 1.12, ["2024 actual", "2028 OEM projection"], [
      { name: "0 visits", values: [40, 26] }, { name: "1 visit", values: [29, 31] }, { name: "2+ visits", values: [31, 43] },
    ], { stacked: true, pct100: true, dir: "bar", colors: [C.LTEAL, C.TEAL, C.NAVY], legend: true, fmt: "0\"%\"", gap: 40 });

    L.sub(s, "Who Services The CFM56", 6.78, 1.68, 6.1);
    L.table(s, ["Provider", "Model", "CFM56 posture"], [
      ["OEM (GE / Safran / CFM)", "Licensor, parts seller, own shops", "Shifting slots and capex to **LEAP**"],
      ["Large MROs (MTU, LHT, SRT, AFI KLM)", "Full shop visit, 90–180 days", "Adding LEAP lines; CFM56 slots **sold out**"],
      ["Airline shops (Delta, UAL in-house)", "Own fleet first", "Feeding own fleets; UAL now **outsources to FTAI**"],
      ["**FTAI**", "**Module exchange, 5–25 days**", "**Only scaled player adding CFM56 capacity**"],
    ], 6.78, 2.05, 6.1, { colW: [1.95, 1.95, 2.2], rowH: 0.36, size: 8.5 });
    L.sub(s, "Industry Growth Algorithm", 6.78, 4.2, 6.1);
    const alg = [["Engines in fleet", "× Shop-visit rate", "= Shop visits"], ["Shop visits", "× 3 modules", "= Module demand"], ["Module demand", "× FTAI share (+ SCI)", "= FTAI modules"]];
    alg.forEach((r, i) => {
      const y = 4.58 + i * 0.47;
      r.forEach((c, j) => L.panel(s, `**${c}**`, 6.78 + j * 2.05, y, 1.95, 0.42, { fill: j === 2 ? C.NAVY : C.LBLUE, color: j === 2 ? C.WHITE : C.NAVY, boldColor: j === 2 ? C.WHITE : C.NAVY, align: "center", size: 10, round: false }));
    });
    L.box(s, "Margin then depends on **feedstock cost** (USM / part-out engines), **workscope mix** (light 42% vs heavy 25% margin per job), **price** (third-party repair catalogues up **6.2%/yr**) and **PMA** content", 6.78, 6.05, 6.1, 0.85, { size: 9.5 });
    L.source(s, "GE / CFM shop-visit outlook; Safran, MTU fleet counts; OEM cohort projection; SR Technics catalogues; GPS model");
  }

  // ---------- 5. OPPORTUNITY 1/2
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Introduction" });
    L.title(s, "The Opportunity (1/2): A Reset Read As Fraud");
    L.banner(s, "In One Quarter Aerospace Margins Fell ~500 bps And Management Guided ~30%; The Market Assumed The Short Thesis Was Unwinding", 0.45, 1.15, 12.43, 0.4, 13.5);
    L.sub(s, "Aerospace Products Adj. EBITDA Margin", 0.45, 1.7, 6.1);
    L.bar(s, pres, 0.45, 2.05, 6.1, 2.75, ["Q1'25", "Q2'25", "Q3'25", "Q4'25", "Q1'26", "Q2'26", "FY26E", "FY27E"], [{ name: "Margin", values: [0.359, 0.336, 0.348, 0.346, 0.299, 0.285, 0.301, 0.299] }],
      { fmt: "0.0%", colors: [C.NAVY, C.NAVY, C.NAVY, C.NAVY, C.ORANGE, C.ORANGE, C.TEAL, C.TEAL], varyColors: true, min: 0.2, max: 0.38 });
    L.box(s, "**Q1'26: –470 bps q/q to 29.9%**, Q2'26 28.5%. Management: more full performance restorations and large-airline deals; share over margin. Q2 call: **\"around 30% for the next 1–2 years\"**. Stock fell ~19% to $162 after Q2", 0.45, 4.85, 6.1, 0.7, { size: 9.5 });
    L.sub(s, "Management's Job Economics (Q2'26 Call): Blend ≈ 30%", 0.45, 5.65, 6.1);
    L.table(s, ["Engine at visit", "Workscope", "Margin", "Dollars per engine"], [["~6,000 cycles", "Light", "~40%", "Similar"], ["~10,000 cycles", "Heavy", "~25%", "Similar, more capital"]], 0.45, 6.0, 6.1, { colW: [1.6, 1.3, 1.2, 2.0], rowH: 0.3, size: 9.5 });

    s.addShape("rect", { x: 6.78, y: 1.7, w: 3.0, h: 0.32, fill: { color: C.NAVY } });
    L.text(s, "The market thinks…", 6.78, 1.7, 3.0, 0.32, { font: HF, size: 12, bold: true, color: C.WHITE, align: "center" });
    s.addShape("rect", { x: 9.88, y: 1.7, w: 3.0, h: 0.32, fill: { color: C.ORANGE } });
    L.text(s, "…but in reality", 9.88, 1.7, 3.0, 0.32, { font: HF, size: 12, bold: true, color: C.WHITE, align: "center" });
    const rows = [
      ["The reset is the Muddy Waters thesis unwinding: cheap, depreciated leasing engines are running out", "Even if true, **<8% of inventory** came from leasing. The cheap stock is nearly gone and margins **already** show the core business"],
      ["Heavy-scope mix keeps rising, so 30% is a waypoint", "Heavy work is **capacity-limited** and was taken to win airline contracts (UAL). Management has no incentive to go further"],
      ["PMA penetration will stay negligible: supply chains and lessors object", "FTAI **is the lessor** for SCI's growing fleet: SCI is **~30–40% of modules** and can run PMA without asking anyone"],
      ["CFM56 is a melting ice cube; fuel shock speeds retirements", "LEAP is grounded or slow in the shop, so CFM56s keep flying. **No evidence** of faster retirement in 2026 data"],
      ["Power is a press release", "A signed **$1.465bn** order; the grid is short from 2029 and dozens of sites are at the stage xAI was"],
    ];
    rows.forEach((r, i) => {
      const y = 2.1 + i * 0.97;
      L.panel(s, r[0], 6.78, y, 3.0, 0.88, { fill: C.LBLUE, size: 9, round: false });
      L.panel(s, r[1], 9.88, y, 3.0, 0.88, { fill: C.GRAY, size: 9, round: false });
    });
    L.source(s, "FTAI Q4'25–Q2'26 earnings calls and supplements; Muddy Waters (Jan-25); GPS model");
  }

  // ---------- 6. OPPORTUNITY 2/2
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Introduction" });
    L.title(s, "The Opportunity (2/2): $167 Prices The Bear Case");
    L.banner(s, "Hold Margins At 28.5%, Share At 15%, Power At Half Economics: You Still Get $173", 0.45, 1.15, 12.43);
    L.sub(s, "FY27E SOTP By Case ($ / Share)", 0.45, 1.68, 6.1);
    L.bar(s, pres, 0.45, 2.05, 6.1, 3.2, ["Today", "Bear", "Base", "Bull"], [{ name: "Price", values: [167.03, 173.0, 276.7, 308.4] }],
      { fmt: "$0", colors: [C.MGRAY, C.SLATE, C.NAVY, C.TEAL], varyColors: true, min: 0 });
    L.box(s, "The bear case strips out **every** thesis: no margin recovery, no share gain beyond 15%, Power at 30% margin and 50% JV capture. It lands **above** today's price", 0.45, 5.35, 6.1, 0.7, { size: 9.5 });
    L.panel(s, "**Bear-case DCF ($103) is the real downside**: it also assumes CFM56 retirements accelerate and inventory never normalises", 0.45, 6.15, 6.1, 0.72, { fill: C.LBLUE, size: 9.5, round: false });
    L.sub(s, "What Each Case Assumes (FY27E unless noted)", 6.78, 1.68, 6.1);
    L.table(s, ["Driver", "Bear", "Base", "Bull"], [
      ["Aerospace margin FY27E / FY31E", "28.5% / 28.5%", "29.9% / 32.5%", "31.2% / 34.5%"],
      ["Third-party CFM56 share FY30E", "15%", "20%", "24%"],
      ["Modules FY27E / FY30E", "1,387 / 1,382", "1,687 / 2,112", "1,752 / 2,366"],
      ["PMA penetration FY31E", "0%", "9%", "9%"],
      ["Power units FY27E / FY29E", "30 / 50", "45 / 110", "55 / 150"],
      ["Power EBITDA FY27E", "$113M", "$450M", "$550M"],
      ["SCI aircraft FY28E", "375", "550", "550"],
      ["Total adj. EBITDA FY27E", "$1.47bn", "$2.24bn", "$2.47bn"],
      ["**SOTP / share**", "**$173**", "**$277**", "**$308**"],
    ], 6.78, 2.05, 6.1, { colW: [2.5, 1.2, 1.2, 1.2], rowH: 0.34, size: 9, highlightRow: 8 });
    L.box(s, "At $167 the stock trades at **9.2x FY27E EBITDA** versus **16x** we apply to Aerospace and **~20x** for the aftermarket peer median: the fraud discount is pricing a business that no longer exists", 6.78, 5.35, 6.1, 0.7, { size: 9.5 });
    L.panel(s, "**Upside skew: +66% base, +85% bull, +4% bear on SOTP**", 6.78, 6.15, 6.1, 0.72, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 12, align: "center", round: false });
    L.source(s, "GPS model case toggle (Bear / Base / Bull), FY27E SOTP at Aerospace 16x, Power 12x, Leasing + SCI 9x; aftermarket peer median per FactSet");
  }
};
