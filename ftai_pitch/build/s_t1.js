const L = require("./lib");
const { C, HF, BF } = L;
const D = require("./data");

module.exports = async function (pres) {
  // ---------- 1.1 EVEN IF THE BEARS ARE RIGHT
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 1: Margins" });
    L.title(s, "Thesis 1 (1/4): Even If The Bears Are Right, It's Over");
    L.banner(s, "Depreciated Leasing Engines Are <8% Of Current Inventory: Today's ~30% Is Already Core-Business Margin", 0.45, 1.15, 12.43);
    L.sub(s, "The Short Thesis, Step By Step (Muddy Waters, Jan-25)", 0.45, 1.68, 6.1);
    const flow = ["Leasing engines depreciated on the books, even off-lease", "Transferred into Aerospace Products inventory at book value", "Sold at market prices: low cost basis inflates AP margin"];
    flow.forEach((f, i) => {
      L.panel(s, f, 0.45 + i * 2.07, 2.05, 1.95, 0.85, { fill: i === 2 ? C.NAVY : C.LBLUE, color: i === 2 ? C.WHITE : C.NAVY, size: 9.5, align: "center", round: false });
      if (i < 2) s.addText("▶", { x: 2.38 + i * 2.07, y: 2.3, w: 0.16, h: 0.35, fontSize: 12, color: C.ORANGE, margin: 0, isTextBox: true });
    });
    L.sub(s, "Share Of Inventory From Leasing", 0.45, 3.05, 2.6);
    s.addChart(pres.charts.DOUGHNUT, [{ name: "Inv", labels: ["From leasing (Q1'26 transfer)", "Purchased feedstock & WIP"], values: [6.4, 93.6] }], {
      x: 0.45, y: 3.4, w: 2.6, h: 2.3, holeSize: 62, chartColors: [C.ORANGE, "D9D9D9"], showValue: false, showPercent: false, showLegend: false, dataLabelColor: C.WHITE,
    });
    s.addText([{ text: "<8%", options: { fontFace: HF, fontSize: 24, bold: true, color: C.NAVY, breakLine: true } }, { text: "left to unwind", options: { fontFace: BF, fontSize: 9, color: C.DGRAY } }],
      { x: 0.95, y: 4.15, w: 1.6, h: 0.8, align: "center", valign: "middle", margin: 0, isTextBox: true });
    L.bullets(s, [
      "Q1'26 leasing→inventory transfers: **$89.6M** vs inventory of **~$1.4bn** (**~6%**)",
      "Flow now runs the **other way**: **$169M** moved inventory→leasing in 1H26 for rebuild and sale",
      "Leasing equipment net down to **$1.53bn** (Jun-26) from $2.06bn (Dec-25) as aircraft go to SCI",
    ], 3.15, 3.05, 3.4, 2.7, { size: 9.5, psa: 6 });
    L.box(s, "Audit-committee review with independent advisors found the claims **without merit**; 10-K filed on time, **no restatement**", 0.45, 5.8, 6.1, 0.55, { size: 9.5 });
    L.panel(s, "**Bear math, worst case:** <8% of stock at a ~40% cost advantage × ~50% material content = **≤150 bps** of residual drag — already inside our 28.5% bear case", 0.45, 6.4, 6.1, 0.52, { fill: C.LBLUE, size: 9.5, round: false });

    L.sub(s, "Inventory Is Now Bought, Not Transferred ($M)", 6.78, 1.68, 6.1);
    L.bar(s, pres, 6.78, 2.05, 6.1, 2.65, ["FY25A", "FY26E", "FY27E", "FY28E", "FY29E"], [
      { name: "AP inventory", values: D.inventory.slice(0, 5) }, { name: "Leasing equipment & PP&E", values: D.leaseEquip.slice(0, 5) },
    ], { legend: true, colors: [C.NAVY, C.TEAL], gap: 50 });
    L.sub(s, "Where The Feedstock Comes From Now", 6.78, 4.8, 6.1);
    L.table(s, ["Source", "Example", "Cost basis"], [
      ["Airline run-outs under MRE", "**United** 737NG -7B program (8-Oct-26)", "Market"],
      ["Fleet retirements", "**WestJet**: 10 of 27 737-700s to AP (28-Sep-26)", "Market"],
      ["USM agreements", "AAR exclusive CFM56 USM through 2030", "Market"],
      ["Legacy leasing pool", "Off-lease engines (shrinking)", "Depreciated"],
    ], 6.78, 5.15, 6.1, { colW: [1.8, 3.1, 1.2], rowH: 0.33, size: 8.5 });
    L.source(s, "Muddy Waters (Jan-25); FTAI 10-Q Q1'26, Q2'26 cash-flow disclosures; FTAI releases; GPS model. Share = Q1'26 transfer / inventory");
  }

  // ---------- 1.2 HEAVY SCOPE HAS RUN ITS COURSE
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 1: Margins" });
    L.title(s, "Thesis 1 (2/4): Heavy-Scope Mix Has Peaked");
    L.banner(s, "Heavy Work Was A Customer-Acquisition Tool; It Is Capacity-Limited And Management Has No Reason To Push It Further", 0.45, 1.15, 12.43, 0.4, 14);
    L.sub(s, "Management's Job Economics (Q2'26 call)", 0.45, 1.68, 4.0);
    L.bar(s, pres, 0.45, 2.02, 4.0, 2.4, ["6,000-cycle\n(light)", "Blend today", "10,000-cycle\n(heavy)"], [{ name: "Margin", values: [0.40, 0.30, 0.25] }],
      { fmt: "0%", colors: [C.TEAL, C.ORANGE, C.NAVY], varyColors: true, min: 0, max: 0.48 });
    L.box(s, "\"Similar dollars per engine, but more investment.\" Heavier jobs carry **lower margin but more EBITDA dollars** and lock in the airline", 0.45, 4.5, 4.0, 0.75, { size: 9.5 });
    L.sub(s, "Bears Say Mix Has More Room To Run…", 4.65, 1.68, 4.0);
    L.bullets(s, [
      "Fleet is ageing: **repeat-visit share** rises from 59% to 72% by 2030",
      "Airline deals (UAL, large carriers) skew to full performance restorations",
      "Management guided \"around 30% for the next 1–2 years\" and chose share over margin",
    ], 4.65, 2.05, 4.0, 1.5, { size: 9.5, psa: 5 });
    L.sub(s, "…But The Constraints Say Otherwise", 4.65, 3.55, 4.0);
    L.bullets(s, [
      "**Capacity-capped:** heavy work needs core disassembly and test cells. Jakarta (heavy) only adds capacity from 2027",
      "**Incentive:** the purpose was winning airline contracts. UAL is **signed** (V2500, now CFM56-7B MRE); more heavy work adds capital, not customers",
      "**Supply-constrained market:** management says CFM56 is \"supply-constrained, not demand-constrained\". FTAI can choose its mix",
    ], 4.65, 3.92, 4.0, 1.9, { size: 9.5, psa: 5 });
    L.sub(s, "Broader-Work Share Only Drifts ~1 pt A Year", 8.85, 1.68, 4.03);
    L.line(s, pres, 8.85, 2.02, 4.03, 2.4, ["FY25", "FY26", "FY27", "FY28", "FY29", "FY30"], [
      { name: "Repeat-visit share", values: [0.585, 0.62, 0.648, 0.675, 0.699, 0.722] }, { name: "Broader-work share", values: [0.482, 0.492, 0.5, 0.507, 0.514, 0.519] },
    ], { fmt: "0%", legend: true, colors: [C.MGRAY, C.NAVY], min: 0.4, max: 0.8 });
    L.box(s, "Even as engines age, the share of visits needing broader work rises only **48% → 52%** by 2030. The step-change already happened in **1H26** as FTAI won airline contracts", 8.85, 4.5, 4.03, 0.75, { size: 9.5 });
    L.sub(s, "AP Margin vs Light-Scope Share Of Jobs", 8.85, 5.35, 4.03);
    L.table(s, ["Light share", "30%", "40%", "50%", "60%", "70%"], [["AP margin", "28%", "29%", "31%", "32%", "34%"]], 8.85, 5.72, 4.03, { colW: [1.03, 0.6, 0.6, 0.6, 0.6, 0.6], rowH: 0.3, size: 9 });
    L.panel(s, "**Every 10 pts of mix back to light work = +1.5–2 pts margin**", 4.65, 5.95, 4.0, 0.9, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 11, align: "center", round: false });
    L.panel(s, "**Our base case holds ~30% through FY27: no mix recovery assumed**", 0.45, 5.35, 4.0, 0.62, { fill: C.LBLUE, size: 10, align: "center", round: false });
    L.source(s, "FTAI Q1'26 and Q2'26 calls; United / FTAI release (8-Oct-26); OEM cohort data (CFM56 fleet by completed shop visits); GPS model");
  }

  // ---------- 1.3 PMA VIA SCI
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 1: Margins" });
    L.title(s, "Thesis 1 (3/4): PMA Gets In Through FTAI's Own Fleet");
    L.banner(s, "The Market Prices ~0% PMA Because Lessors Object; At SCI, FTAI Is The Lessor", 0.45, 1.15, 12.43);
    L.sub(s, "The Street's Objection", 0.45, 1.68, 4.0);
    L.bullets(s, [
      "**Lessor resistance:** PMA parts can hurt asset conformity, residual values and return conditions",
      "**Supply chain:** Chromalloy's 2025 output sold out; LPT blades not yet approved",
      "**Result:** consensus gives PMA almost no value; our base case uses only **0.9% → 9%** penetration",
    ], 0.45, 2.05, 4.0, 1.7, { size: 9.5, psa: 5 });
    L.sub(s, "What's Already Approved (Chromalloy)", 0.45, 3.8, 4.0);
    L.table(s, ["Part", "Status"], [["HPT stage 1 vane", "**Approved**"], ["LPT stage 1 NGV", "**Approved**"], ["HPT blade", "**Approved (Oct-25)**"], ["LPT stage 1 & 2 blades", "Pending"]],
      0.45, 4.15, 4.0, { colW: [2.4, 1.6], rowH: 0.29, size: 9 });
    L.box(s, "Chromalloy's CEO: **\"80% of the savings will come from the first three parts\"**, and all three are approved. In Apr-26 a US airline adopted the HPT blade", 0.45, 5.7, 4.0, 0.9, { size: 9.5 });

    L.sub(s, "SCI Is A Growing Share Of FTAI's Modules", 4.65, 1.68, 4.0);
    L.bar(s, pres, 4.65, 2.02, 4.0, 2.55, ["FY25", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E"], [
      { name: "Third-party", values: D.mroModules.slice(0, 6) }, { name: "SCI captive", values: D.sciModules.slice(0, 6) },
    ], { stacked: true, legend: true, colors: [C.NAVY, C.ORANGE], dlSize: 7.5 });
    L.box(s, "SCI owns the aircraft and sends **all engine work to FTAI**. SCI rises from **11% to ~40%** of modules (130 → 700 aircraft); FTAI sponsors and services the fund, so it **sets the parts policy**", 4.65, 4.65, 4.0, 1.0, { size: 9.5 });
    L.panel(s, "**Diligence item:** confirm SCI's LP and lender terms allow PMA (no public disclosure either way)", 4.65, 5.75, 4.0, 0.85, { fill: C.LBLUE, size: 9.5, round: false });

    L.sub(s, "PMA EBITDA Uplift: Base vs SCI-Led ($M)", 8.85, 1.68, 4.03);
    L.bar(s, pres, 8.85, 2.02, 4.03, 2.55, ["FY27E", "FY28E", "FY29E", "FY30E", "FY31E"], [
      { name: "Base (0.9–9% of all modules)", values: [6, 24, 42, 59, 77] }, { name: "50% of SCI modules on PMA", values: [96, 132, 156, 168, 180] },
    ], { legend: true, colors: [C.MGRAY, C.ORANGE], gap: 40, dlSize: 8 });
    L.table(s, ["", "Base", "SCI-led"], [["Uplift per PMA module", "$0.4M", "$0.4M"], ["FY28E AP margin uplift", "+0.4 pts", "+2.1 pts"], ["FY28E value at 16x / share", "$4", "$20"]],
      8.85, 4.65, 4.03, { colW: [2.03, 1.0, 1.0], rowH: 0.27, size: 8.5 });
    L.panel(s, "**SCI alone can take AP margin back above 32% without a single outside lessor signing up**", 8.85, 5.95, 4.03, 0.75, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 10.5, align: "center", round: false });
    L.source(s, "Chromalloy / FAA PMA releases; Aviation Week; AviTrader (May-26); FTAI 10-K (SCI); GPS model (PMA uplift $0.4M per module; SCI modules from RPM build)");
  }

  // ---------- 1.4 MARGIN PATH & CATALYST
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 1: Margins" });
    L.title(s, "Thesis 1 (4/4): Two Stable Prints Re-Rate The Trough");
    L.banner(s, "Price Catch-Up Plus PMA Rebuild Margins To 32.5%; The Market Only Needs To See ~30% Hold", 0.45, 1.15, 12.43);
    L.sub(s, "Aerospace Margin: Trough, Then Rebuild (Base Case)", 0.45, 1.68, 6.1);
    L.bar(s, pres, 0.45, 2.02, 6.1, 2.6, ["FY25", "Q1'26", "Q2'26", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"], [{ name: "m", values: [0.347, 0.299, 0.285, 0.301, 0.299, 0.307, 0.314, 0.32, 0.325] }],
      { fmt: "0.0%", colors: [C.NAVY, C.ORANGE, C.ORANGE, C.TEAL, C.TEAL, C.TEAL, C.TEAL, C.TEAL, C.TEAL], varyColors: true, min: 0.2, max: 0.37, dlSize: 8 });
    L.sub(s, "Bridge FY27E → FY31E", 0.45, 4.7, 6.1);
    s.addChart(pres.charts.BAR, [
      { name: "base", labels: ["FY27E", "Price pass-through", "PMA", "FY31E"], values: [0, 29.9, 31.5, 0] },
      { name: "value", labels: ["FY27E", "Price pass-through", "PMA", "FY31E"], values: [29.9, 1.6, 1.0, 32.5] },
    ], { x: 0.45, y: 5.05, w: 6.1, h: 1.9, barDir: "col", barGrouping: "stacked", chartColors: ["FFFFFF", C.NAVY], showValue: false, valAxisHidden: true, valAxisMinVal: 25, valAxisMaxVal: 33.5,
      valGridLine: { style: "none" }, catGridLine: { style: "none" }, catAxisLabelFontSize: 9, catAxisLabelColor: "595959", catAxisLabelFontFace: BF, showLegend: false, barGapWidthPct: 50 });
    [["29.9%", 0.95], ["+1.6", 2.42], ["+1.0", 3.88], ["32.5%", 5.35]].forEach(([t, x]) => L.text(s, `**${t}**`, x - 0.2, 5.05, 0.9, 0.25, { size: 9, align: "center" }));
    L.sub(s, "Pricing Headroom", 6.78, 1.68, 6.1);
    L.table(s, ["Catalogue", "Matched parts", "Median Δ", "Higher / Lower"], [
      ["CFM56-5B 2024→25", "1,342", "6.2%", "1,338 / 1"], ["CFM56-5B 2025→26", "1,070", "6.2%", "1,057 / 0"], ["CFM56-7B 2025→26", "992", "6.1%", "981 / 0"],
    ], 6.78, 2.05, 6.1, { colW: [1.9, 1.3, 1.2, 1.7], rowH: 0.29, size: 9 });
    L.box(s, "Third-party repair prices rise **~6% a year** with almost none falling. FTAI held price to win share; we assume it passes through **half** of the escalator from FY28, lifting **EBITDA per module from $0.91M to $1.14M**", 6.78, 3.25, 6.1, 0.8, { size: 9.5 });
    L.sub(s, "Catalyst: The Next Two Prints", 6.78, 4.15, 6.1);
    const cats = [["Q3'26 (29-Oct)", "First print after the guide. ~30% holds while modules run toward 1,200; first PMA usage commentary"],
      ["Investor day (10-Dec)", "2027 framework: 1,700 modules, Power backlog, SCI II size"], ["Q4'26 (Feb-27)", "Second ~30% print + FY27 guide: the market stops reading 30% as a waypoint"]];
    cats.forEach((c, i) => {
      L.panel(s, `**${c[0]}**`, 6.78, 4.52 + i * 0.62, 1.75, 0.54, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 9.5, align: "center", round: false });
      L.box(s, c[1], 8.6, 4.52 + i * 0.62, 4.28, 0.54, { size: 9 });
    });
    L.panel(s, "**Each +1x on Aerospace EBITDA = ~$15 / share**", 6.78, 6.4, 6.1, 0.48, { fill: C.LBLUE, size: 11, align: "center", round: false });
    L.source(s, "SR Technics CFM56 capabilities & price catalogues (2024–26, ~3,400 matched packages); FTAI Q2'26 call; GPS model (FY27E AP EBITDA $1,541M / 104.0mm shares)");
  }
};
