const L = require("./lib");
const { C, HF, BF } = L;
const D = require("./data");

module.exports = async function (pres) {
  // ---------- 3.1 POWER SHORTFALL BUILD
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 3: Power" });
    L.title(s, "Thesis 3 (1/5): The Power Hole Behind The Capex");
    L.banner(s, "Hyperscalers Fund ~10 GW Of New US Data Center Shells In 2026 Alone; NERC Reserves Go Short From 2029", 0.45, 1.15, 12.43);
    L.sub(s, "Capex Is Outrunning Contracted Power", 0.45, 1.68, 6.1);
    L.bar(s, pres, 0.45, 2.02, 3.6, 2.6, D.capexYrs, [{ name: "Capex", values: D.capex }], { colors: [C.NAVY], title: "Big Four capex ($bn)", catSize: 8, dlSize: 8 });
    L.bar(s, pres, 4.1, 2.02, 2.45, 2.6, D.capexYrs.slice(0, 8), [{ name: "PPA", values: D.ppaGW.slice(0, 8) }], { colors: [C.TEAL], title: "US corporate PPAs (GW)", catSize: 7, dlSize: 7.5, fmt: "0" });
    L.box(s, "Capex and PPAs moved together for a decade (**0.89 correlation in levels**). In 2025 capex rose **+65%** but PPAs were **flat at ~29.5 GW**: the money is arriving faster than contracted power", 0.45, 4.68, 6.1, 0.68, { size: 9.5 });
    L.sub(s, "Our Rough Power Build", 0.45, 5.45, 6.1);
    const steps = [["$733bn", "Big Four 2026 capex"], ["× 65%", "US share"], ["× 25%", "facility (non-GPU)"], ["÷ $12M/MW", "facility cost"], ["= 9.9 GW", "funded in 2026"]];
    steps.forEach((t, i) => L.stat(s, t[0], t[1], 0.45 + i * 1.235, 5.82, 1.15, 1.05, { bigSize: 15, size: 8.5, fill: i === 4 ? C.LBLUE : C.GRAY, bigColor: i === 4 ? C.NAVY : C.ORANGE }));

    L.sub(s, "US Reserve Shortfall vs Requirement (GW), Base Case", 6.78, 1.68, 6.1);
    L.bar(s, pres, 6.78, 2.02, 6.1, 2.6, ["2026", "2027", "2028", "2029", "2030", "2031"], [
      { name: "PJM", values: D.pjm }, { name: "MISO", values: D.miso }, { name: "Other", values: [0, 0, 0, 0, 0, 1.2] },
    ], { stacked: true, legend: true, colors: [C.NAVY, C.TEAL, C.ORANGE], fmt: "0.0;;;" });
    L.table(s, ["", "2026", "2028", "2029", "2030", "2031"], [
      ["US DC energy demand (TWh)", "298", "464", "549", "649", "746"],
      ["Tracked new hyperscaler capacity (GW)", "1.5", "5.9", "7.7", "9.6", "11.2"],
      ["**Reserve shortfall (GW)**", "0", "0", "**8.4**", "**27.2**", "**47.2**"],
    ], 6.78, 4.68, 6.1, { colW: [2.35, 0.75, 0.75, 0.75, 0.75, 0.75], rowH: 0.25, size: 8.5 });
    L.box(s, "Data center demand **2.5x by 2031** while new contracted supply adds only ~11 GW. **57%** of power hyperscalers have contracted lands **2029 or later**: a 2–3 year gap that only on-site, fast-to-deploy generation can fill. ERCOT's large-load queue is **~475 GW**, 90% data centers", 6.78, 5.82, 6.1, 1.1, { size: 9 });
    L.source(s, "Company filings (AMZN, GOOGL, META, MSFT); BCSE/BNEF (PPAs); NERC 2025 LTRA; 67 hyperscaler power agreements tracked in GPS model; ERCOT Senate testimony (Jul-26)");
  }

  // ---------- 3.2 THE FIRST ORDER & THE STAGE
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 3: Power" });
    L.title(s, "Thesis 3 (2/5): What The First Order Tells Us");
    L.banner(s, "$1.465bn Came From A Site That Was Built, Energized On Mobile Gas, And Out Of Turbines", 0.45, 1.15, 12.43);
    L.sub(s, "The Order (22-Jul-26)", 0.45, 1.68, 4.0);
    L.table(s, ["Term", "Detail"], [
      ["Seller", "J&F Power Systems (FTAI × Jereh JV)"], ["Buyer", "\"Leading international cloud service provider\"; **reported to be xAI** (not confirmed)"],
      ["Size", "**$1.465bn** initial PO under a 5-yr MSA"], ["Implied units", "~58 Mod-1 at ~$25M (~1.45 GW)"],
      ["Delivery", "Batches through **Nov-27**"], ["Terms", "Advance + milestone payments; output penalty capped at 10%"],
    ], 0.45, 2.05, 4.0, { colW: [1.0, 3.0], rowH: 0.34, size: 8.5 });
    L.box(s, "The MSA lets the buyer **re-order without renegotiating**: further xAI-scale orders need no new contract", 0.45, 4.95, 4.0, 0.95, { size: 9.5 });
    L.sub(s, "Reference Site: xAI Colossus 2 / Southaven", 4.65, 1.68, 8.23);
    const tl = [
      ["Feb–Mar 25", "Land + 186 ac bought in Memphis"], ["Apr 25", "Solaris JV: ~900 MW mobile gas"], ["Jul 25", "Buys ex-Duke plant, Southaven MS"],
      ["Jan 26", "1 GW online; $20bn Southaven DC"], ["Mar 26", "Permit for 41 turbines (~1.2 GW)"], ["Jul 26", "{{FTAI / J&F order}}"],
    ];
    s.addShape("line", { x: 4.85, y: 2.42, w: 7.85, h: 0, line: { color: C.NAVY, width: 2 } });
    tl.forEach((t, i) => {
      const x = 4.75 + i * 1.36;
      s.addShape("ellipse", { x: x + 0.52, y: 2.32, w: 0.2, h: 0.2, fill: { color: i === 5 ? C.ORANGE : C.NAVY }, line: { color: C.WHITE } });
      L.text(s, `**${t[0]}**`, x, 2.05, 1.25, 0.25, { size: 9, align: "center" });
      L.text(s, t[1], x, 2.58, 1.25, 0.62, { size: 8.5, align: "center", valign: "top" });
    });
    L.sub(s, "\"The xAI Stage\": What Was True When It Signed", 4.65, 3.32, 8.23);
    const stage = [
      ["1", "Shell built, GPUs committed", "~1 GW live; next GW ($20bn Southaven) under construction"],
      ["2", "No grid for the next phase", "MLGW supplies **no power** to Colossus 2; no TVA allocation"],
      ["3", "Behind-the-meter gas permitted", "41 permanent turbines permitted; gas lateral in place"],
      ["4", "Incumbent supply tapped out", "Solaris fleet committed; OEM aero slots **2028+**"],
    ];
    stage.forEach((r, i) => {
      const y = 3.72 + i * 0.4;
      L.badge(s, r[0], 4.7, y + 0.02, 0.32, C.ORANGE, 11);
      L.text(s, `**${r[1]}**`, 5.1, y, 2.65, 0.36, { size: 9.5 });
      L.text(s, r[2], 7.75, y, 5.1, 0.36, { size: 9.5 });
    });
    L.box(s, "We use these four conditions as the screen on the next page: a site that meets all four needs **bridge power in 2027–28** and has no OEM alternative before 2029", 4.65, 5.38, 8.23, 0.55, { size: 9.5 });
    L.panel(s, "**Diligence flag:** FTAI has not named the buyer and xAI was folded into SpaceX in Feb-26. The xAI link comes from Jereh gensets on the Southaven equipment list (CV Research). Our thesis does not depend on the name: the order is signed, priced and has a delivery schedule", 0.45, 6.05, 12.43, 0.82, { fill: C.LBLUE, size: 9.5, round: false });
    L.source(s, "FTAI release (22-Jul-26); Q2'26 call; Solaris 8-K; MDEQ permit (10-Mar-26); Mississippi Governor's office (8-Jan-26); DCD; SemiAnalysis; CV Research");
  }

  // ---------- 3.3 PIPELINE DILIGENCE
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 3: Power" });
    L.title(s, "Thesis 3 (3/5): Sites At The xAI Stage");
    L.banner(s, "We Screened 24 US AI Campuses: 9 Meet The xAI Conditions, ~10 GW Of Load With No Locked Bridge Supplier", 0.45, 1.15, 12.43, 0.4, 14);
    L.table(s, ["Project (tenant)", "Location", "Target", "Stage", "Power plan today", "Grid timing", "Bridge need", "FTAI win"], [
      ["Amazon \"GW Ranch\" (ex-Pacifico)", "Pecos Co., TX", "Up to 7.6 GW gen", "Bldgs 1–3 under constr.", "Off-grid; 35-turbine permit, mixed sizes", "Undefined", "**High**", "{{High}}"],
      ["Poolside / CoreWeave \"Horizon\"", "Pecos Co., TX", "2 GW (8×250 MW)", "Under constr.; Ph1 1Q27", "Behind-the-meter; no supplier named", "None planned", "**High**", "{{High}}"],
      ["Project Jade (Tallgrass)", "Cheyenne, WY", "1.8 GW", "Plans approved; 2028", "CCGT + **\"temporary aeroderivatives\"**", "Off-grid", "**High**", "{{High}}"],
      ["Google / Crusoe \"Goodnight\"", "Armstrong Co., TX", "Multi-100 MW", "Under constr.; Ph1 2027", "933 MW aeros, **not sourced from GE**", "Partial", "**High**", "Med"],
      ["Meta El Paso", "El Paso, TX", "1 GW", "Under constr.", "366 MW utility plant, stalled at PUC", "2027 if approved", "**High**", "Med"],
      ["Microsoft / Chevron \"Kilby\"", "Pecos area, TX", "2–2.5 GW", "PPA signed; FID 2026", "Chevron BTM; first power **2028**", "n/a", "Med-High", "Med"],
      ["Cipher \"Colchis\"", "West TX", "1 GW", "Land + AEP deal", "AEP direct connect", "**2028**", "Med-High", "Med"],
      ["Stargate Milam (SB Energy)", "Milam Co., TX", "1.2 GW", "First bldg ~Oct-26", "Solar + storage; no firm gas", "ERCOT, n.d.", "Med", "Med"],
      ["Nebius Independence", "Independence, MO", "0.8–1.1 GW", "Early constr.", "New private plant, fuel n.d.", "Oct-27 Ph1", "Med", "Med"],
    ], 0.45, 1.7, 12.43, { colW: [2.35, 1.25, 1.2, 1.55, 2.6, 1.15, 1.13, 1.2], rowH: 0.34, size: 8.5 });
    L.box(s, "**Already locked (screened out):** Stargate Jupiter → Bloom fuel cells (2.45 GW); Vantage Frontier → VoltaGrid; Meta Prometheus → Williams; Homer City → GE 7HA; Fermi → owns SGT-800s, no tenant; Abilene Ph3 → GE + third-party aeros (Med). **Grid-led (low need):** Saline MI, Lighthouse WI, Fairwater WI, Galaxy Helios, IREN Sweetwater, Applied Digital ND", 0.45, 5.45, 7.4, 1.45, { size: 9 });
    L.stat(s, "60 units", "**per 1 GW of load** at 50% redundancy (~$1.5bn of orders)", 8.0, 5.45, 2.35, 1.45, { bigSize: 20 });
    L.stat(s, "3 sites", "**High win-ability** = ~5 GW of load. One of them = **another first order**", 10.5, 5.45, 2.38, 1.45, { bigSize: 20 });
    L.source(s, "Company releases; TCEQ / MDEQ filings; Cleanview behind-the-meter tracker (2026); Epoch AI; DCD; Texas Tribune; World Oil; GPS analysis. Win-ability = gas access + BTM permitting + no locked supplier + 2026–28 load date");
  }

  // ---------- 3.4 DELIVERY RAMP
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 3: Power" });
    L.title(s, "Thesis 3 (4/5): A Faster Ramp Than The Street Thinks");
    L.banner(s, "Prototype To Order In Seven Months; The Feedstock (1,000+ Owned CFM56s) And The Shops Already Exist", 0.45, 1.15, 12.43);
    L.sub(s, "Mod-1 Units Delivered By Case", 0.45, 1.68, 6.1);
    L.bar(s, pres, 0.45, 2.02, 6.1, 2.85, ["FY26E", "FY27E", "FY28E", "FY29E", "FY30E", "FY31E"], [
      { name: "Bear", values: [0, 30, 45, 50, 50, 50] }, { name: "Base", values: [2, 45, 90, 110, 120, 130] }, { name: "Bull", values: [2, 55, 130, 150, 160, 170] },
    ], { legend: true, colors: [C.SLATE, C.NAVY, C.TEAL], dlSize: 7.5, gap: 40 });
    L.box(s, "Management's $450M FY27 Power planning base assumes **\"materially less\" than its 100+ unit capacity** — essentially the signed order. Our base case of **45 units** sits below even that; every unit above it is upside", 0.45, 4.95, 6.1, 0.75, { size: 9.5 });
    L.sub(s, "Path To First Power", 0.45, 5.8, 6.1);
    const path = [["Dec-25", "FTAI Power launched"], ["1H26", "Prototype tested in Montreal"], ["Jul-26", "$1.465bn order; unit in Miami"], ["4Q26", "Commercial launch"], ["2027", "Batch deliveries to Nov-27"]];
    path.forEach((p, i) => {
      L.panel(s, `**${p[0]}**`, 0.45 + i * 1.235, 6.15, 1.15, 0.3, { fill: i < 3 ? C.NAVY : C.ORANGE, color: C.WHITE, boldColor: C.WHITE, size: 9, align: "center", round: false });
      L.text(s, p[1], 0.45 + i * 1.235, 6.47, 1.15, 0.45, { size: 8.5, align: "center", valign: "top" });
    });
    L.sub(s, "Why The Ramp Is Credible", 6.78, 1.68, 6.1);
    L.bullets(s, [
      "**Feedstock in hand:** FTAI owns **1,000+ CFM56 engines**; 22,000+ were built. No new-build hot section is needed, only the core it already overhauls",
      "**Capacity:** launch release targets **100+ units a year**; ~$150M of Power inventory built in 4Q25 and ~$250M of working capital planned for 2027",
      "**Packaging outsourced:** Jereh supplies the package, generator and gearbox from US, Canadian, UAE and Chinese plants, so FTAI's own shops only do the turbine",
      "**Learning curve already run:** the same technicians restore ~1,200 CFM56 modules a year; a conversion is reported at **30–45 days**",
      "**First power:** management says it is \"prudent to expect deliveries in 2027\"; we model **2 units in 4Q26** and 45 in FY27",
    ], 6.78, 2.05, 6.1, 2.25, { size: 9.5, psa: 3 });
    L.table(s, ["Power economics", "Base", "Mgmt framing"], [
      ["Price per unit (25 MW)", "$25M ($1M/MW)", "~$1M/MW"], ["EBITDA margin", "40%", "\"As good or better\" than Aerospace"],
      ["EBITDA per unit", "$10M", "$7–8M"], ["FY27E Power EBITDA", "**$450M**", "**$450–750M**"],
    ], 6.78, 4.35, 6.1, { colW: [2.1, 1.6, 2.4], rowH: 0.3, size: 9 });
    L.box(s, "**Order math:** $1.465bn ÷ ~$25M per unit ≈ **58 units ≈ 1.45 GW**, i.e. more than our entire FY27E base case. Every unit FTAI ships beyond 45 is upside to our numbers", 6.78, 6.0, 6.1, 0.85, { size: 9.5 });
    L.source(s, "FTAI Power launch release (30-Dec-25); Q4'25, Q1'26, Q2'26 calls; J&F order release (22-Jul-26); GPS model");
  }

  // ---------- 3.5 RIGHT TO WIN
  {
    const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Thesis 3: Power" });
    L.title(s, "Thesis 3 (5/5): Why FTAI Has The Right To Win");
    L.banner(s, "Cheap, Available Now, And Mobile: The Units Leave When The Grid Arrives", 0.45, 1.15, 12.43);
    L.sub(s, "Cost To Power 100 MW Of Load ($M)", 0.45, 1.68, 4.0);
    L.bar(s, pres, 0.45, 2.02, 4.0, 2.2, ["Data center shell", "FTAI turbines (6 units)"], [{ name: "Cost", values: [1200, 150] }],
      { dir: "bar", colors: [C.TEAL, C.NAVY], varyColors: true, fmt: "$#,##0\"M\"", gap: 45 });
    L.stat(s, "~13%", "of build cost ex-GPUs, with 50% spare units; **~2%** of an all-in AI site ($50–60M/MW)", 0.45, 4.3, 4.0, 1.05, { bigSize: 22 });
    L.sub(s, "When New Supply Can Arrive", 4.65, 1.68, 4.0);
    L.table(s, ["Supplier", "Earliest slot", "$/kW"], [
      ["**FTAI Mod-1**", "**2027**", "**~$1,000**"], ["GE Vernova aeros (LM6000)", "2028–30", "$1,400–2,000"], ["Siemens Energy", "3+ yrs", "n.d."],
      ["MHI large frame", "2028–30", "~$2,000+"], ["Caterpillar recips", "72–104 wks", "n.d."], ["Boom Superpower", "250 MW in 2027", "~$1,030"],
    ], 4.65, 2.05, 4.0, { colW: [1.8, 1.1, 1.1], rowH: 0.3, size: 8.5, highlightRow: 0 });
    L.box(s, "OEM gas backlog incl. reservations: **~220 GW** (GEV 116, SE 95 incl. reservations, MHI 35). Crusoe **walked away** from Boom in Sep-26: unproven new entrants carry the risk FTAI's flown core avoids", 4.65, 4.2, 4.0, 1.15, { size: 9 });
    L.sub(s, "Transitory Units Accelerate ROIC", 8.85, 1.68, 4.03);
    L.bullets(s, [
      "An idle AI site burns **~$1M per MW per month** (GPU depreciation + cost of capital). A $1M/MW unit **pays back in about a month** of earlier energization",
      "Units are **mobile**: once the grid arrives they redeploy to the next site, so the owner is not stranded with a 20-year plant",
      "A behind-the-meter fleet keeps working as **backup and peak** under PJM's bring-your-own-capacity rules from 2027",
    ], 8.85, 2.05, 4.03, 2.2, { size: 9.5, psa: 5 });
    L.stat(s, "~1 month", "of earlier energization pays for a **$1M/MW** unit", 8.85, 4.3, 4.03, 1.05, { bigSize: 22 });
    L.sub(s, "What One More Contract Is Worth", 0.45, 5.48, 12.43);
    const ws = [["Signed order only", "45 units", "$450M", "+$52 / share"], ["+1 contract (~1 GW)", "~90 units", "~$750M", "+$35 / share"], ["+2 contracts", "~130 units", "~$1.05bn", "+$70 / share"]];
    ws.forEach((w, i) => {
      const x = 0.45 + i * 4.18;
      L.panel(s, `**${w[0]}**`, x, 5.85, 1.75, 1.05, { fill: [C.SLATE, C.TEAL, C.NAVY][i], color: C.WHITE, boldColor: C.WHITE, size: 10.5, align: "center", round: false });
      L.box(s, `**${w[1]}** in FY27E\n**${w[2]}** Power EBITDA\n{{${w[3]}}} at 12x`, x + 1.8, 5.85, 2.25, 1.05, { size: 10 });
    });
    L.source(s, "CNBC (Jun-26); JLL, Turner & Townsend build costs; GE Vernova, Siemens Energy, MHI Q2'26 filings; Rabobank; GridLab; TechCrunch; GPS model (12x Power EBITDA, 104.0mm shares; incremental value vs signed order)");
  }
};
