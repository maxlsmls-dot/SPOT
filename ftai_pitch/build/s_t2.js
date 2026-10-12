const L = require("./lib");
const { C, HF, BF } = L;
const D = require("./data");

module.exports = async function (pres) {
  // ---------- 2.1 OEMs MOVE TO LEAP
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 2: Share" });
    L.title(s, "Thesis 2 (1/4): OEMs Leave Whitespace Behind");
    L.banner(s, "OEMs And Large MROs Are Pouring New Capacity Into LEAP While CFM56 Demand Plateaus At ~2,350 Visits A Year", 0.45, 1.15, 12.43, 0.4, 14);
    L.sub(s, "Where New Capacity Is Going", 0.45, 1.68, 6.1);
    L.table(s, ["Player", "Recent capacity move", "Engine"], [
      ["GE Aerospace", "**>$1bn** over 5 yrs; ~half of MRO spend now on LEAP", "**LEAP**"],
      ["Safran", "**>€1bn** over 5 yrs; Querétaro sized for 350 LEAP visits/yr by 2030", "**LEAP**"],
      ["CFM open network", "35 licensed LEAP sites", "**LEAP**"],
      ["ST Engineering", "300 CFM engines/yr by 2027, weighted to LEAP", "Mixed"],
      ["MTU / LHT / AFI KLM", "LEAP lines ramping; CFM56 slots **sold out into 2027**", "Mixed"],
      ["**FTAI**", "**2,000 → 3,000 modules/yr**, all CFM56 (+ Jakarta, Cairo)", "**CFM56**"],
    ], 0.45, 2.05, 6.1, { colW: [1.6, 3.5, 1.0], rowH: 0.36, size: 9, highlightRow: 5 });
    L.box(s, "\"The variability in capital investment required to capture the LEAP is extremely low versus what it took them to capture the CFM.\" — **Former executive, engine MRO shop**", 0.45, 4.65, 6.1, 0.72, { size: 9.5 });
    L.sub(s, "GE Commercial MRO Spend Mix", 0.45, 5.45, 3.0);
    L.bar(s, pres, 0.45, 5.78, 3.0, 1.17, ["2025", "2030E"], [{ name: "CFM56", values: [68, 49] }, { name: "LEAP", values: [32, 51] }],
      { stacked: true, pct100: true, dir: "bar", legend: true, colors: [C.TEAL, C.NAVY], fmt: "0\"%\"", gap: 35 });
    L.stat(s, "+50%", "LEAP shop visits y/y (GE, 2026)", 3.55, 5.45, 1.45, 1.45, { bigSize: 20 });
    L.stat(s, "40%", "GE shop-visit slots **oversubscribed**", 5.1, 5.45, 1.45, 1.45, { bigSize: 20 });
    L.sub(s, "CFM56 Demand Stays Put While Supply Leaves", 6.78, 1.68, 6.1);
    L.bar(s, pres, 6.78, 2.02, 6.1, 2.6, ["FY25", "FY26", "FY27", "FY28", "FY29", "FY30", "FY31"], [{ name: "Module demand", values: D.moduleDemand }],
      { colors: [C.NAVY], title: "CFM56 module demand (3 per shop visit), base case", min: 0 });
    L.bullets(s, [
      "Module demand only falls **~2% a year** after the 2026–28 plateau; LEAP/GTF visits do not pass CFM56/V2500 until the **mid-2030s** (FTAI)",
      "~45% of CFM56s have **not had a first shop visit** (CFM): the heaviest second and third visits are still ahead",
      "Every slot an OEM or MRO moves to LEAP is a CFM56 visit that has to go **somewhere else**. FTAI is the only scaled player adding CFM56 capacity",
    ], 6.78, 4.7, 6.1, 1.6, { size: 9.5, psa: 5 });
    L.panel(s, "**Whitespace: shrinking supply + flat demand = share for the last scaled builder**", 6.78, 6.35, 6.1, 0.55, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 11, align: "center", round: false });
    L.source(s, "GE Aerospace and Safran investor materials; Aviation Week; CFM; ST Engineering; FTAI Q4'25 and Q2'26 calls; expert call; GPS model");
  }

  // ---------- 2.2 CFM56 KEEPS FLYING
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 2: Share" });
    L.title(s, "Thesis 2 (2/4): LEAP Keeps The CFM56 Flying");
    L.banner(s, "LEAP Is Late, Grounded Or Stuck In The Shop; The Fuel Shock Has Not Moved Retirements", 0.45, 1.15, 12.43);
    L.sub(s, "Why The Replacements Aren't Arriving", 0.45, 1.68, 4.0);
    const why = [
      ["LEAP-1B durability", "HPT kit certified **Jul-26**; full production cutover only **early 2027**"],
      ["LEAP-1A durability", "Only **~40%** of fleet kitted; 70% has reverse-bleed fix"],
      ["GTF groundings", "**~835** PW1100G aircraft grounded or stored (late 2025); relief \"a few more years\" away"],
      ["Delivery backlog", "Airbus/Boeing still behind plan; airlines **cannot retire** what isn't replaced"],
    ];
    why.forEach((w, i) => {
      L.panel(s, `**${w[0]}**`, 0.45, 2.05 + i * 0.78, 1.3, 0.68, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 9, align: "center", round: false });
      L.box(s, w[1], 1.8, 2.05 + i * 0.78, 2.65, 0.68, { size: 9 });
    });
    L.box(s, "LEAP time-on-wing issues persist **into 2027**, which pushes utilisation back onto CFM56-5B/-7B and keeps them in the shop-visit pool", 0.45, 5.2, 4.0, 0.72, { size: 9.5 });
    L.sub(s, "CFM56 Retirement Rate: Assumed vs Actual", 4.65, 1.68, 4.0);
    L.bar(s, pres, 4.65, 2.02, 4.0, 3.15, ["GE prior\n2026 view", "GE revised\n2026 view", "Actual\n(mid-2026)", "Our FY27E\n(-7B / -5B)"], [{ name: "Retirement", values: [0.035, 0.025, 0.0175, 0.0225] }],
      { fmt: "0.0%", colors: [C.MGRAY, C.SLATE, C.ORANGE, C.NAVY], varyColors: true, min: 0, max: 0.042 });
    L.box(s, "Midpoints of GE's 3–4% and 2–3% ranges vs 1.5–2% actual. Our base case **still steps retirements up** to 2–4% by FY31", 4.65, 5.2, 4.0, 0.72, { size: 9 });
    L.sub(s, "The Fuel-Shock Bear Case", 8.85, 1.68, 4.03);
    L.panel(s, "**Bear:** jet fuel more than doubled from Feb-26 (Hormuz); IATA cut 2026 profit to ~$23bn. Old, thirsty CFM56 jets get parked first", 8.85, 2.05, 4.03, 0.95, { fill: C.LBLUE, size: 9.5, round: false });
    L.text(s, "**Our view: no evidence, and fleets can't turn on a dime**", 8.85, 3.08, 4.03, 0.3, { size: 10, color: C.NAVY });
    L.bullets(s, [
      "GE's mid-2026 data shows retirements at **1.5–2%**, below its own 2–3% assumption",
      "IBA (Sep-26): CFM56 values **\"broadly stabilised\"**; -5B lease rates **+11%**. Retired engines would push values down",
      "Retirement plans are set by **lease terms, delivery slots and crew/sim training** years ahead",
      "WestJet's 737-700 retirement is real — and **FTAI is the buyer** (10 aircraft to AP feedstock)",
    ], 8.85, 3.4, 4.03, 2.55, { size: 9.5, psa: 5 });
    L.panel(s, "**Bear case cuts -5B retirements to 4–5%/yr: still $173 SOTP**", 0.45, 6.05, 12.43, 0.82, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 12, align: "center", round: false });
    L.source(s, "GE Aerospace (Morgan Stanley Laguna conf., via Aviation Week); GE Q2'26 release; Leeham; The Air Current; Cirium; IATA (Jun-26); IBA (H1'26, Sep-26); WestJet / FTAI (28-Sep-26); GPS model");
  }

  // ---------- 2.3 WHY FTAI WINS
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 2: Share" });
    L.title(s, "Thesis 2 (3/4): Why FTAI Wins The Whitespace");
    L.banner(s, "Cheaper, Faster, And With Its Own Feedstock: FTAI Sells Airlines Time They Can't Buy Elsewhere", 0.45, 1.15, 12.43);
    L.sub(s, "Days Off Wing", 0.45, 1.68, 6.1);
    L.bar(s, pres, 0.45, 2.02, 6.1, 1.9, ["Conventional shop visit", "FTAI module swap"], [{ name: "Days", values: [150, 15] }],
      { dir: "bar", colors: [C.MGRAY, C.ORANGE], varyColors: true, fmt: "0\" days\"", gap: 40 });
    L.text(s, "Shop visit 120–180 days incl. 2–6 months waiting for a slot; FTAI swap 5–25 days", 0.45, 3.92, 6.1, 0.25, { size: 8, italic: true, color: C.MGRAY });
    L.sub(s, "Lease Cost While Grounded ($K)", 0.45, 4.25, 3.0);
    L.bar(s, pres, 0.45, 4.6, 3.0, 1.55, ["Shop visit", "FTAI swap"], [{ name: "Cost", values: [493, 66] }], { colors: [C.NAVY, C.TEAL], varyColors: true, fmt: "$#,##0\"K\"" });
    L.stat(s, "~7x", "faster back in service", 3.6, 4.25, 1.4, 1.9, { bigSize: 24 });
    L.stat(s, "$427K", "lease cost saved per event", 5.1, 4.25, 1.45, 1.9, { bigSize: 20 });
    L.box(s, "\"FTAI's advantage is basically turnaround time and cheaper sourcing.\" — **Industry expert**", 0.45, 6.25, 6.1, 0.62, { size: 9.5 });
    L.sub(s, "FTAI vs A Conventional Shop", 6.78, 1.68, 6.1);
    L.table(s, ["Edge", "FTAI", "MTU / LHT / SRT / OEM shops"], [
      ["**Feedstock**", "1,000+ owned CFM56s; WestJet, United run-outs; AAR USM through 2030", "Buy new OEM parts at list (+6%/yr)"],
      ["**Parts cost**", "PMA (3 of 5 approved), USM, in-house repairs", "OEM-licensed, little PMA"],
      ["**Model**", "Swap a restored module from the pool", "Repair the engine in sequence"],
      ["**Labour**", "Montreal, Miami, Lisbon, Jakarta, Cairo", "High-wage Europe"],
      ["**Slots**", "1,800 modules of unused capacity in 2026", "Sold out into 2027"],
      ["**Captive volume**", "SCI: 482 modules FY27E, contracted", "None"],
    ], 6.78, 2.05, 6.1, { colW: [1.2, 2.75, 2.15], rowH: 0.38, size: 8 });
    L.sub(s, "Proof It's Working", 6.78, 4.95, 6.1);
    L.bullets(s, [
      "**United:** V2500 exchange expanded to a multi-year **CFM56-7B MRE** for the 737NG fleet (8-Oct-26); FTAI buys the run-outs",
      "**Share:** ~10% → 12% (Q1'26) → **14% (Q2'26)** of the CFM56/V2500 market; modules **+61% y/y** in Q2",
      "**Guidance:** 2026 modules raised twice, 1,000 → 1,050 → **1,200**; 2027 target **1,700**",
    ], 6.78, 5.3, 6.1, 1.65, { size: 9.5, psa: 4 });
    L.source(s, "FTAI Q2'24 call (TAT); IBA (2024) lease rates; FTAI Q1'26, Q2'26 calls and releases; United / FTAI (8-Oct-26); AAR; expert call. Step lengths illustrative");
  }

  // ---------- 2.4 CAPACITY BUILT, PATH TO ~25%
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 2: Share" });
    L.title(s, "Thesis 2 (4/4): Capex Spent, Share To ~25%");
    L.banner(s, "3,000 Modules Of Capacity vs 1,200 Produced: Jakarta And Cairo Ramp In 2027 And Accelerate Volume Adds", 0.45, 1.15, 12.43);
    const alg = [["2,386", "CFM56 shop visits"], ["× 3", "modules each"], ["× 16.8%", "FTAI third-party share"], ["+ 482", "SCI modules"], ["= 1,687", "FY27E modules"]];
    alg.forEach((a, i) => L.stat(s, a[0], a[1], 0.45 + i * 2.5, 1.68, 2.38, 0.85, { bigSize: 17, size: 9, fill: i === 4 ? C.NAVY : C.GRAY, bigColor: i === 4 ? C.WHITE : C.NAVY, smallColor: i === 4 ? C.WHITE : C.DGRAY }));
    L.sub(s, "FTAI Share Of CFM56 Module Demand", 0.45, 2.68, 6.1);
    L.line(s, pres, 0.45, 3.0, 6.1, 2.6, ["FY25", "FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"], [
      { name: "Incl. SCI captive (base)", values: [0.107, 0.167, 0.236, 0.285, 0.312, 0.332, 0.346] },
      { name: "Third-party only (base)", values: [0.096, 0.124, 0.168, 0.19, 0.195, 0.2, 0.2] },
    ], { fmt: "0%", legend: true, colors: [C.ORANGE, C.NAVY, C.TEAL], min: 0, max: 0.4 });
    L.box(s, "Management sized 3,000 modules for **25% of the market**. Including SCI's contracted volume, FTAI touches **~24% of all CFM56 module demand in FY27E**; third-party share alone only needs to grow **half as fast** as it did in 1H26. Bull: third-party **25%** by FY31", 0.45, 5.7, 6.1, 1.2, { size: 9.5 });
    L.sub(s, "Output vs Capacity (Modules)", 6.78, 2.68, 3.0);
    L.bar(s, pres, 6.78, 3.0, 3.0, 2.6, ["2025", "2026E", "2027E"], [{ name: "Output", values: [757, 1200, 1700] }, { name: "Unused", values: [1243, 1800, 1300] }],
      { stacked: true, legend: true, colors: [C.NAVY, C.LTEAL], dlColor: C.NAVY, dlSize: 8 });
    L.sub(s, "The Network", 9.88, 2.68, 3.0);
    L.table(s, ["Site", "Role"], [
      ["Montreal", "Flagship, up to ~900"], ["Miami", "~475 in 2026E"], ["Rome", "QuickTurn; CFM56/LEAP test cell"], ["Lisbon", "+113k sq ft → 300+"],
      ["**Jakarta (GMF)**", "**Heavy; 200+ techs; 5-yr deal**"], ["**Cairo (EgyptAir)**", "**-7B; ~120 techs**"],
    ], 9.88, 3.0, 3.0, { colW: [1.05, 1.95], rowH: 0.36, size: 8 });
    L.panel(s, "Capex already in the ground; Jakarta and Cairo are **partner-funded**. Volume adds need working capital, not new buildings", 6.78, 5.7, 6.1, 0.55, { fill: C.LBLUE, size: 9.5, round: false });
    L.panel(s, "**Each +1 pt of third-party share ≈ 70 modules ≈ $65M EBITDA ≈ $10 / share**", 6.78, 6.33, 6.1, 0.57, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 11, align: "center", round: false });
    L.source(s, "FTAI Q2'26 supplement (1,200 / 1,700 modules, 3,000 capacity, 25% target); GMF / FTAI (23-Sep-26); Aviation Week (Aug-26); GPS model (RPM build)");
  }
};
