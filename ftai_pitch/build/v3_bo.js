const G = require("./g");
const { C, F } = G;

module.exports = async function (pres) {
  const s = pres.addSlide({ masterName: "Pitch" });
  G.title(s, "Business Overview – A Module Factory Scaling Through a Margin Reset");
  s.addText("($ in millions)", { x: 11.3, y: 0.52, w: 1.63, h: 0.3, align: "right", fontFace: F, fontSize: 13, italic: true, color: C.INK, margin: 0, isTextBox: true });
  G.sub(s, "FTAI offers 1) a CFM56 aftermarket business still winning share, 2) an asset-light leasing arm that feeds it, and 3) a new Power segment");

  // ---------------- Business segments (left)
  const lx = 0.68, lw = 8.62;
  G.banner(s, "Business Segments", lx, 1.3, lw, 0.34, 14);
  const seg = (y, h, head, items) => {
    G.para(s, head, lx, y, lw, 0.27, { size: 13 });
    G.bullets(s, items, lx + 0.25, y + 0.26, lw - 0.25, h - 0.26, { size: 11.5, psa: 1 });
  };
  seg(1.68, 1.3, "**1)  Aerospace Products** (77% of FY25 Revenue, 52% of Segment EBITDA^^1^^):", [
    "Swaps restored ++fan, core and LPT modules++ from its own pool: engines back in ++5–25 days vs. 120–180++ at a shop",
    "Feedstock is ++run-out engines++ bought from airlines, lessors and SCI; also sells used serviceable parts",
    "++757 modules (FY25) → 1,200 (FY26E) → 1,700 (FY27E)++; CFM56 module share ~10% → 14% in 1H26^^2^^",
    "Margin ++reset from ~35% to ~30%++ in 1H26 on heavier workscopes and large airline deals (United)",
  ]);
  s.addShape("line", { x: lx, y: 3.0, w: lw, h: 0, line: { color: C.TXT, width: 1, dashType: "dash" } });
  seg(3.04, 0.8, "**2)  Aviation Leasing + SCI** (23% of FY25 Revenue, 48% of Segment EBITDA):", [
    "Going asset-light: aircraft sold into ++SCI++, an FTAI-sponsored fund ($2.0bn equity, ~$6bn buying power)",
    "FTAI services SCI's fleet and ++receives all of its engine work++: SCI grows from 130 to ~316 aircraft by YE26E",
  ]);
  s.addShape("line", { x: lx, y: 3.88, w: lw, h: 0, line: { color: C.TXT, width: 1, dashType: "dash" } });
  seg(3.92, 0.8, "**3)  FTAI Power** (launched Dec-25; $450–750M FY27 EBITDA guidance):", [
    "Converts CFM56 cores into ++25 MW \"Mod-1\" gas turbines++ (~$1M per MW) sold as bridge power to AI data centers",
    "First order ++$1.465bn++ (Jul-26) via J&F, FTAI's JV with Jereh; delivered in batches through Nov-27",
  ]);

  // ---------------- Tables (right)
  const rx = 9.5, rw = 3.43;
  const y1 = G.finTable(s, "Key Aerospace Financials (FY25)", [
    ["Aerospace Revenue", "$1,936", "hi"], ["FY26E Revenue Growth (%)", "79.4%", "it ul"],
    ["Aerospace Adj. EBITDA", "$671", "hi"], ["EBITDA Margin (%)", "34.7%", "it"], ["Q2'26 EBITDA Margin (%)", "28.5%", "it ul"],
    ["Modules Produced", "757", "hi"], ["FY26E Guidance", "1,200", "it"],
  ], rx, 1.3, rw, { size: 10.5, rowH: 0.2 });
  G.finTable(s, "Cap Table", [
    ["Share Price (As of 10/2/26)", "$167.03"], ["(x) Diluted Shares", "104.0"], ["Market Cap", "$17,378", "hi"],
    ["(+) Total Debt", "3,453"], ["(–) Cash", "(337)"], ["(+) Preferred Equity", "65", "ul"], ["Enterprise Value", "$20,560", "hi"],
    ["EV / FY26E Adj. EBITDA", "15.7x"], ["EV / FY27E Adj. EBITDA", "9.2x"],
  ], rx, y1 + 0.03, rw, { size: 10.5, rowH: 0.2 });

  // ---------------- Revenue algorithm (bottom)
  G.banner(s, "Earnings Algorithm for Aerospace Products", lx, 5.12, 12.25, 0.34, 14);
  s.addText("Module Demand × FTAI Share × Revenue per Module × EBITDA Margin", { x: lx, y: 5.5, w: 12.25, h: 0.38, align: "center", valign: "middle", fontFace: F, fontSize: 19, bold: true, color: C.TXT, margin: 0, isTextBox: true });
  s.addShape("rect", { x: lx + 0.15, y: 5.93, w: 11.95, h: 0.42, fill: { type: "none" }, line: { color: C.TXT, width: 1.5 } });
  const parts = [
    ["[Fleet × Shop-Visit Rate × 3]", 0.85, 2.75, "Industry Demand"],
    ["× [3rd-Party Share + SCI Captive]", 3.65, 3.1, "Thesis II: Share"],
    ["× [Price + OEM Escalator]", 6.8, 2.45, "Pricing"],
    ["× [Mix + Feedstock + PMA]", 9.3, 2.75, "Thesis I: Margin"],
  ];
  parts.forEach(([t, x, w, lab]) => {
    s.addText(t, { x, y: 5.93, w, h: 0.42, align: "center", valign: "middle", fontFace: F, fontSize: 15, color: C.TXT, margin: 0, isTextBox: true });
    s.addShape("rightBrace", { x: x + w / 2 - 0.12, y: 6.47 - (w - 0.3) / 2, w: 0.24, h: w - 0.3, rotate: 90, line: { color: C.TXT, width: 1 } });
    s.addText(lab, { x, y: 6.64, w, h: 0.32, align: "center", valign: "middle", fontFace: F, fontSize: 14, bold: true, color: C.INK, margin: 0, isTextBox: true });
  });

  G.source(s, "Company Filings, Earnings Calls, Investor Presentation", ["Segment EBITDA mix excludes Corporate & Other.", "Module share of CFM56 third-party module demand, per management (Q2'26)."]);
};
