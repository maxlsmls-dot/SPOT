const G = require("./g");
const { C, F } = G;

const SLATE = "5B7189", PINK = "F4A6A6", GREEN = "B9DFA6";

function box(s, x, y, w, h, fill, head, body, o = {}) {
  s.addShape("rect", { x, y, w, h, fill: { color: fill }, line: { color: fill } });
  const runs = [{ text: head, options: { bold: true, fontFace: F, fontSize: o.hs || 11, color: o.color || C.TXT, breakLine: true } },
    ...G.parse(body, { fontFace: F, fontSize: o.bs || 10, color: o.color || C.TXT })];
  s.addText(runs, { x: x + 0.12, y: y + 0.03, w: w - 0.24, h: h - 0.06, valign: "middle", margin: 0, isTextBox: true });
}

module.exports = async function (pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "Catalysts & Risks – Risks Sit in the Bear Case; Catalysts Land Within the Hold");
  const W = 3.95, xs = [0.68, 4.83, 8.98];
  ["Risks", "Mitigants", "Catalysts"].forEach((t, i) => {
    s.addShape("rect", { x: xs[i], y: 0.98, w: W, h: 0.34, fill: { color: SLATE }, line: { color: SLATE } });
    s.addText(t, { x: xs[i], y: 0.98, w: W, h: 0.34, align: "center", valign: "middle", fontFace: F, fontSize: 14, bold: true, color: C.WHITE, margin: 0, isTextBox: true });
  });

  const rows = [
    ["Margins keep falling (Thesis I)", "Heavier workscopes and a thinning supply of cheap engines take Aerospace margin below 30%, and the market keeps reading every print as the short thesis unwinding. **Value at risk:** ++~$22 / share++ (Thesis I, bear vs. base).",
      "Little cheap stock left to unwind", "Leasing-sourced engines are ++<8% of inventory++ and flows now run back to leasing. Heavy mix is capacity-capped and United is signed. Our bear case holds ++28.5%++ – and that outcome is ++$161, about today's price++."],
    ["Fraud overhang never clears (Thesis I)", "Muddy Waters or a follow-on short revisits inventory accounting; the governance discount persists even if margins hold. **Value at risk:** each turn of Aerospace multiple is ++~$16 / share++.",
      "Claims reviewed; capital returned", "Audit-committee review found the claims ++without merit++; ++no restatement++. Management is buying back stock (++$500M++, Sep-26) and the 10-Q transfer disclosures let anyone track the stock."],
    ["CFM56 retires faster or LEAP catches up (Thesis II)", "The 2026 fuel shock or LEAP durability fixes push airlines to park CFM56s; independents (StandardAero, ST Eng., SRT, MTU) take the overflow instead of FTAI. **Value at risk:** ++~$62 / share++ (Thesis II).",
      "Retirements falling; FTAI's edge is speed", "GE's 2026 retirements run ++1.5–2%++ vs. an original 3–4% plan; parked CFM56s are ++down since March++. Retired jets become FTAI feedstock (WestJet). A ++5–25 day++ swap with owned parts beats a 120–180 day shop visit."],
    ["Power slips or the buyer walks (Thesis III)", "Mod-1 deliveries slip past Nov-27, output misses spec, or – like Crusoe with Boom – the customer walks. Jereh's Chinese ownership adds tariff / supply-chain risk. **Value at risk:** ++~$63 / share++ (Thesis III).",
      "Signed, paid for, and not in the price", "Signed PO with ++advance and milestone payments++; output penalty ++capped at 10%++. Base case uses 45 units vs. ~58 implied by the order. Jereh packages in the US, Canada and UAE. Ex-Power, the target is still ++$239, 43% upside++."],
  ];
  const y0 = 1.42, h = 1.3, gap = 0.08;
  rows.forEach((r, i) => {
    const y = y0 + i * (h + gap);
    box(s, xs[0], y, W, h, PINK, r[0], r[1]);
    box(s, xs[1], y, W, h, GREEN, r[2], r[3]);
  });

  // catalysts
  G.dash(s, xs[2], y0, W, 1.08, C.RED);
  s.addText("Two clean ~30% prints and a second Power order re-rate the stock within 12 months.", { x: xs[2] + 0.1, y: y0, w: W - 0.2, h: 1.08, align: "center", valign: "middle", fontFace: F, fontSize: 15, bold: true, color: C.TXT, margin: 0, isTextBox: true });
  const cats = [
    ["GE Q3 call (late Oct-26) | Thesis II", "CFM56 retirement and shop-visit update; confirms the 2,300–2,400 visit plateau"],
    ["FTAI Q3'26 (late Oct-26) | Thesis I", "First print after the reset: margin ≥~30%, modules on track for 1,200, PMA usage"],
    ["Investor day (10-Dec-26) | I, II, III", "2027 framework: 1,700 modules, Jakarta / Cairo ramp, SCI II size, Power backlog"],
    ["Q4'26 + FY27 guide (Feb-27) | Thesis I", "Second ~30% print: 30% stops reading as a waypoint"],
    ["Power deliveries / new order (2027) | III", "First revenue from the $1.465bn order; a second order adds ~$35 / share"],
  ];
  const cy0 = y0 + 1.16, ch = 0.75, cg = 0.065;
  cats.forEach((c, i) => box(s, xs[2], cy0 + i * (ch + cg), W, ch, C.NAVY, c[0], c[1], { color: C.WHITE, hs: 10.5, bs: 10 }));

  G.source(s, "Company Filings and Calls, Muddy Waters, GE Aerospace, J&F order release (Jul-26), TechCrunch (Boom–Crusoe), GPS Model",
    ["Value at risk from the valuation bridge (bear → base by thesis). FTAI Q3 date to confirm (26- or 29-Oct)."]);
};
