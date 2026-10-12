const L = require("./lib");
const { C, HF, BF } = L;
const D = require("./data");

const THESES = [
  ["I", "Margins Have Bottomed: ~30% Is The Floor", "Even if the short thesis is right, depreciated leasing stock is <8% of inventory. Heavy-scope mix is capped by capacity and incentive, and PMA enters through SCI, where FTAI is the lessor. Two more stable prints re-rate the trough"],
  ["II", "FTAI Takes The CFM56 Whitespace To ~25% Share", "OEMs and MROs move capacity to LEAP while LEAP problems keep CFM56s flying and retirements run below plan. FTAI's cost and turnaround edge wins the visits, and its capacity is already built"],
  ["III", "Power Is A Call Option The Market Isn't Paying For", "The grid is short from 2029 and hyperscaler capex outruns contracted power. The first order came from a site at a stage many campuses share today. Mobile units are ~13% of build cost and pay back in about a month of earlier revenue"],
];

function thesesSlide(pres, active, section) {
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: section });
  L.title(s, "Theses Summary");
  L.banner(s, "Three Theses: The Trough Is A Floor, The Share Is Coming, And Power Is Free", 0.45, 1.15, 12.43);
  THESES.forEach((t, i) => {
    const y = 1.85 + i * 1.7, on = active == null || active === i;
    s.addShape("roundRect", { x: 0.45, y, w: 12.43, h: 1.4, rectRadius: 0.08, fill: { color: on ? C.LBLUE : "F7F8FA" }, line: { color: on ? C.NAVY : "F7F8FA", width: 1.5 } });
    s.addShape("rect", { x: 0.45, y, w: 1.3, h: 1.4, fill: { color: on ? C.NAVY : "AEB7C7" }, line: { color: on ? C.NAVY : "AEB7C7" } });
    L.text(s, t[0], 0.45, y, 1.3, 1.4, { font: HF, size: 30, bold: true, color: C.WHITE, align: "center" });
    L.text(s, t[1], 1.95, y + 0.12, 10.7, 0.4, { font: HF, size: 15, bold: true, color: on ? C.NAVY : "B8BFCC", align: "center" });
    L.text(s, t[2], 1.95, y + 0.5, 10.7, 0.82, { size: 11, color: on ? C.DGRAY : "C4C9D2", align: "center", valign: "top" });
  });
}

module.exports = {
  thesesSlide,
  valuation: async function (pres) {
    // ---------- CASES OVERVIEW
    {
      const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Valuation & Risks" });
      L.title(s, "Valuation: Cases Overview");
      L.banner(s, "FY27E Sum Of The Parts By Case, Cross-Checked With A Blended DCF", 0.45, 1.15, 12.43);
      const cases = [
        ["Bear Case", C.SLATE, [
          "Aerospace margin stuck at **28.5%** through FY31; no PMA",
          "Third-party share stalls at **15%**; modules ~1,400",
          "-5B retirements **4–5%**/yr; inventory stays bloated",
          "Power: **30 units** FY27, 50 a year after; **30%** margin, **50%** of JV",
          "SCI stops at 400 aircraft",
        ], "$173", "+4%", "$103 (–39%)", "20%"],
        ["Base Case", C.NAVY, [
          "Aerospace margin **~30%** FY26–27, rebuilding to **32.5%** by FY31 (half price pass-through + PMA 0.9→9%)",
          "Third-party share **17% → 20%** by FY30; **1,687** modules FY27E",
          "Power: **45 units** FY27 (signed order), 110 by FY29 at 40%",
          "SCI to 700 aircraft by FY30",
        ], "$277", "+66%", "$308 (+84%)", "60%"],
        ["Bull Case", C.TEAL, [
          "Margin recovers to **31%** FY27E and **34.5%** FY31 as light work returns",
          "Third-party share **25%** by FY31",
          "Power: one more contract, **130–170 units** a year",
          "Base-case SCI and PMA",
        ], "$308", "+85%", "$387 (+132%)", "20%"],
      ];
      cases.forEach((c, i) => {
        const x = 0.45 + i * 4.2;
        L.panel(s, c[0], x + 0.9, 1.75, 2.2, 0.42, { fill: c[1], color: C.WHITE, font: HF, size: 14, align: "center", round: false });
        L.box(s, null, x, 2.3, 4.03, 2.85, { lineColor: c[1] });
        L.text(s, "**Key assumptions**", x, 2.35, 4.03, 0.3, { size: 11, align: "center" });
        L.bullets(s, c[2], x + 0.1, 2.72, 3.85, 2.4, { size: 10.5, psa: 6 });
        [["SOTP target: " + c[3], C.LBLUE], ["Implied return: " + c[4], C.LBLUE], ["DCF: " + c[5], C.GRAY], ["Weighting: " + c[6], C.GRAY]].forEach((r, j) =>
          L.panel(s, `**${r[0]}**`, x + 0.5, 5.25 + j * 0.37, 3.03, 0.32, { fill: r[1], size: 10, align: "center", round: false }));
      });
      L.panel(s, "**Probability-weighted SOTP: $262 (+57%)   |   Base target: $277 (+66%)   |   R/R (blended DCF bull vs bear): 3.4x**", 0.45, 6.75, 12.43, 0.22, { fill: C.WHITE, size: 11, align: "center", round: false });
      L.source(s, "GPS model case toggle; SOTP at Aerospace 16x, Power 12x, Leasing + SCI 9x, corporate at blended multiple; DCF 9.5% WACC, 3% TGR / 13x exit, 50/50 blend");
    }

    // ---------- SOTP BRIDGE + DCF
    {
      const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Valuation & Risks" });
      L.title(s, "Valuation: Sum Of The Parts & DCF");
      L.banner(s, "At $167 The Market Pays For The Bear Case; Each Thesis Adds Value From There", 0.45, 1.15, 12.43);
      L.sub(s, "From Today To Our Base Case ($ / Share)", 0.45, 1.68, 6.9);
      const labels = ["Today", "Margins", "Share", "Power", "Base case"];
      s.addChart(pres.charts.BAR, [
        { name: "base", labels, values: [0, 167, 185, 219, 0] },
        { name: "val", labels, values: [167, 18, 34, 58, 277] },
      ], { x: 0.45, y: 2.05, w: 6.9, h: 3.1, barDir: "col", barGrouping: "stacked", chartColors: ["FFFFFF", C.NAVY], showValue: false, valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 300,
        valGridLine: { style: "none" }, catGridLine: { style: "none" }, catAxisLabelFontSize: 9.5, catAxisLabelColor: "595959", catAxisLabelFontFace: BF, showLegend: false, barGapWidthPct: 45 });
      [["$167", 167], ["+$18", 185], ["+$34", 219], ["+$58", 277], ["$277", 277]].forEach(([t, v], i) =>
        L.text(s, `**${t}**`, 0.75 + i * 1.3, 2.05 + 3.1 * (1 - v / 300) - 0.12 - 0.15, 1.0, 0.25, { size: 10, align: "center" }));
      L.box(s, "Today's price is roughly our bear case. Switching each thesis from bear to base: **margins +$18, share +$34, Power +$58** (signed order only)", 0.45, 5.25, 6.9, 0.65, { size: 9.5 });
      L.sub(s, "FY27E Sum Of The Parts (Base)", 0.45, 6.0, 6.9);
      L.text(s, "Aerospace $1,541M × 16x = **$237** | Power $450M × 12x = **$52** | Leasing+SCI $455M × 9x = **$39** | Corp. **–$28** | Net debt & pref. **–$24** → **$277**", 0.45, 6.35, 6.9, 0.55, { size: 9.5 });

      L.sub(s, "DCF Cross-Check (Base)", 7.55, 1.68, 5.33);
      L.table(s, ["", "Perpetuity", "Exit multiple"], [
        ["WACC", "9.5%", "9.5%"], ["Terminal assumption", "3.0% TGR", "13.0x EBITDA"], ["PV of FY26–31 UFCF ($M)", "7,288", "7,288"],
        ["PV of terminal value ($M)", "25,106", "30,778"], ["Enterprise value ($M)", "32,394", "38,066"], ["Implied share price", "**$280.77**", "**$335.29**"],
        ["Implied cross-check", "10.6x exit", "4.2% TGR"],
      ], 7.55, 2.05, 5.33, { colW: [2.13, 1.6, 1.6], rowH: 0.3, size: 9 });
      L.panel(s, "**Blended DCF: $308 (+84%)**", 7.55, 4.55, 5.33, 0.45, { fill: C.NAVY, color: C.WHITE, boldColor: C.WHITE, size: 12, align: "center", round: false });
      L.sub(s, "Implied Price: WACC vs Terminal Growth", 7.55, 5.1, 5.33);
      L.table(s, ["WACC \\ TGR", "2.5%", "3.0%", "3.5%"], [["9.0%", "$286", "$307", "$331"], ["9.5%", "$263", "**$280**", "$299"], ["10.0%", "$242", "$257", "$273"]],
        7.55, 5.45, 5.33, { colW: [1.73, 1.2, 1.2, 1.2], rowH: 0.29, size: 9 });
      L.source(s, "GPS model (FY27E SOTP; DCF tab); price $167.03 (2-Oct-26); 104.0mm diluted shares");
    }

    // ---------- CATALYST PATH
    {
      const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Valuation & Risks" });
      L.title(s, "Catalyst Path");
      const cats = [
        ["29-Oct-26", "Q3'26 results: first print after the 30% reset", ["Aerospace margin **≥30%** with modules on track for 1,200; first PMA usage and pricing commentary", "Leasing-to-inventory transfers keep shrinking; SCI II fundraising update"], C.NAVY],
        ["10-Dec-26", "Investor day (New York)", ["2027 framework: **1,700 modules**, Jakarta/Cairo ramp, United CFM56 MRE scope", "Power: delivery schedule for the $1.465bn order and **backlog beyond it**"], C.SLATE],
        ["Feb-27", "Q4'26 print and FY27 guide", ["**Second ~30% print**: the market stops reading 30% as a waypoint", "FY27 guide vs. $2.3bn segment EBITDA framework; buyback pace ($500M authorised)"], C.TEAL],
        ["2027", "Power deliveries and new contracts", ["Batch deliveries through **Nov-27**; first revenue recognition", "Any second hyperscaler order (+$35/share per ~1 GW contract) from the sites on our screen"], C.ORANGE],
      ];
      cats.forEach((c, i) => {
        const y = 1.2 + i * 1.42;
        s.addShape("rect", { x: 0.55, y, w: 0.55, h: 0.95, fill: { color: c[3] }, line: { color: c[3] } });
        s.addShape("triangle", { x: 0.55, y: y + 0.95, w: 0.55, h: 0.28, rotate: 180, fill: { color: c[3] }, line: { color: c[3] } });
        if (i < 3) s.addShape("line", { x: 0.825, y: y + 1.23, w: 0, h: 0.19, line: { color: C.NAVY, width: 1.25, dashType: "dash" } });
        L.panel(s, `**${c[0]}**`, 1.35, y, 1.9, 1.0, { fill: C.GRAY, size: 15, align: "center", font: HF, round: false, line: C.NAVY });
        L.text(s, c[1], 3.45, y - 0.02, 9.4, 0.38, { font: HF, size: 15, bold: true, color: C.NAVY });
        L.bullets(s, c[2], 3.45, y + 0.38, 9.4, 0.85, { size: 10.5, psa: 3 });
      });
      L.source(s, "FTAI (Q3'26 timing release; Q2'26 supplement; buyback 15-Sep-26); GPS analysis");
    }

    // ---------- RISKS
    {
      const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: "Valuation & Risks" });
      L.title(s, "Risks & Mitigants");
      s.addShape("rect", { x: 0.45, y: 1.15, w: 4.6, h: 0.4, fill: { color: C.NAVY } });
      L.text(s, "Risk", 0.45, 1.15, 4.6, 0.4, { font: HF, size: 14, bold: true, color: C.WHITE, align: "center" });
      s.addShape("rect", { x: 5.6, y: 1.15, w: 7.28, h: 0.4, fill: { color: C.NAVY } });
      L.text(s, "Mitigants", 5.6, 1.15, 7.28, 0.4, { font: HF, size: 14, bold: true, color: C.WHITE, align: "center" });
      const risks = [
        ["I", "Margins keep falling: 30% is a waypoint, not a floor", ["<8% of inventory came from leasing; worst-case residual drag ≤150 bps, inside our 28.5% bear case", "Bear case already holds 28.5% with zero PMA and still prints **$173**"]],
        ["II", "Short-report overhang: governance discount never closes", ["Audit-committee review found claims without merit; no restatement; transfers now flow **inventory → leasing**", "$500M buyback authorised Sep-26; each clean print shrinks the discount"]],
        ["III", "CFM56 retirements accelerate (fuel shock, LEAP fixes)", ["Actual retirements **1.5–2%** vs GE's 2–3% assumption; IBA values stable, lease rates up", "LEAP durability cutover only in 2027; FTAI buys retiring fleets as feedstock (WestJet)"]],
        ["IV", "Power slips or the buyer walks (Boom/Crusoe precedent)", ["Signed PO with advance and milestone payments; delivery penalty capped at 10%", "Base case uses 45 units vs 100+ capacity; bear case haircuts Power to $113M EBITDA"]],
        ["V", "Jereh JV: China supply-chain, tariff and FEOC exposure", ["Jereh packages from US, Canadian and UAE plants as well as China; FTAI supplies the turbine", "Key diligence item; Power is <20% of our FY27E SOTP ex-net debt"]],
      ];
      risks.forEach((r, i) => {
        const y = 1.7 + i * 1.04;
        L.panel(s, r[0], 0.45, y, 0.6, 0.92, { fill: C.NAVY, color: C.WHITE, font: HF, size: 15, align: "center", round: false });
        L.panel(s, `**${r[1]}**`, 1.05, y, 4.0, 0.92, { fill: C.LBLUE, size: 11, align: "center", round: false });
        s.addShape("rightArrow", { x: 5.12, y: y + 0.26, w: 0.4, h: 0.4, fill: { color: C.LBLUE }, line: { color: C.NAVY, width: 0.75 } });
        L.box(s, null, 5.6, y, 7.28, 0.92, { solid: true });
        L.bullets(s, r[2], 5.7, y + 0.05, 7.1, 0.85, { size: 9.5, psa: 3, valign: "middle" });
      });
      L.source(s, "FTAI filings and calls; GE Aerospace; IBA; J&F order release (22-Jul-26); TechCrunch / CryptoBriefing (Boom–Crusoe); GPS model");
    }
  },
};
