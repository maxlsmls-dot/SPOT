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
  const s = pres.addSlide({ masterName: "Pitch" });
  G.title(s, "Catalysts & Risks – Risks Sit in the Bear Case; Catalysts Land Within the Hold");
  const W = 3.95, xs = [0.68, 4.83, 8.98];
  ["Risks", "Mitigants", "Catalysts"].forEach((t, i) => {
    s.addShape("rect", { x: xs[i], y: 0.98, w: W, h: 0.34, fill: { color: SLATE }, line: { color: SLATE } });
    s.addText(t, { x: xs[i], y: 0.98, w: W, h: 0.34, align: "center", valign: "middle", fontFace: F, fontSize: 14, bold: true, color: C.WHITE, margin: 0, isTextBox: true });
  });

  const rows = [
    ["Margins keep falling (Thesis I)", "Heavier workscopes and a thinning supply of cheap engines take Aerospace margin below 30%, and the market keeps reading every print as the short thesis unwinding. **Value at risk:** ++~$22 / share++ (Thesis I, bear vs. base).",
      "Little cheap stock left to unwind", "Leasing-sourced engines are ++<8% of inventory++ and flows now run back to leasing. Heavy mix is capacity-capped and United is signed. Q3 printed ++31%++; our bear case holds 28.5% – worth ++$161, 19% below today++."],
    ["Fraud overhang never clears (Thesis I)", "Muddy Waters or a follow-on short revisits inventory accounting; the governance discount persists even if margins hold. **Value at risk:** each turn of Aerospace multiple is ++~$16 / share++.",
      "Claims reviewed; capital returned", "Audit-committee review found the claims ++without merit++; ++no restatement++. Buyback doubled to ++$1.0bn++ with a ++$500M ASR++ (Oct-26), and the 10-Q transfer disclosures let anyone track the stock."],
    ["CFM56 retires faster or LEAP catches up (Thesis II)", "The 2026 fuel shock or LEAP durability fixes push airlines to park CFM56s; independents (StandardAero, ST Eng., SRT, MTU) take the overflow instead of FTAI. **Value at risk:** ++~$62 / share++ (Thesis II).",
      "Retirements falling; FTAI's edge is speed", "GE (Q3): CFM56 retirements ++below ~2%++ vs. an original 3–4% plan; visits at the ++top of 2,300–2,400++. Retired jets become FTAI feedstock (WestJet). A ++5–25 day++ swap with owned parts beats a 120–180 day shop visit."],
    ["Power slips or the buyer walks (Thesis III)", "Mod-1 deliveries slip past Nov-27, output misses spec, or – like Crusoe with Boom – the customer walks. Jereh's Chinese ownership adds tariff / supply-chain risk. **Value at risk:** ++~$63 / share++ (Thesis III).",
      "Signed, paid for, and not in the price", "Signed PO with ++advance and milestone payments++; output penalty ++capped at 10%++. Testing hit 25 MW; ++>100 units++ now under contract vs. 45 in our base. Jereh packages in the US, Canada and UAE. Ex-Power, the target is still ++$239, 21% upside++."],
  ];
  const y0 = 1.42, h = 1.3, gap = 0.08;
  rows.forEach((r, i) => {
    const y = y0 + i * (h + gap);
    box(s, xs[0], y, W, h, PINK, r[0], r[1]);
    box(s, xs[1], y, W, h, GREEN, r[2], r[3]);
  });

  // catalysts
  G.dash(s, xs[2], y0, W, 1.08, C.RED);
  s.addText("Q3 delivered 31% and >100 Power units; one more ~30% print re-rates the stock within 12 months.", { x: xs[2] + 0.1, y: y0, w: W - 0.2, h: 1.08, align: "center", valign: "middle", fontFace: F, fontSize: 15, bold: true, color: C.TXT, margin: 0, isTextBox: true });
  const cats = [
    ["GE Q3 call (20-Oct-26) ✓ | Thesis II", "CFM56 visits at the top of 2,300–2,400; retirements below ~2%; the fleet is “still young”"],
    ["FTAI Q3'26 (29-Oct-26) ✓ | Thesis I", "Aerospace margin 31%, 311 modules (+50% y/y); guide reaffirmed; $1.0bn buyback"],
    ["Investor day (10-Dec-26) | I, II, III", "2027 framework: 1,700 modules, Jakarta / Cairo ramp, SCI II size, Power backlog"],
    ["Q4'26 + FY27 guide (Feb-27) | Thesis I", "Second ~30% print: 30% stops reading as a waypoint"],
    ["Power deliveries (2027) | III", ">100 units under contract for 2027–28; first revenue in 2027; each ~1 GW more adds ~$35 / share"],
  ];
  const cy0 = y0 + 1.16, ch = 0.75, cg = 0.065;
  cats.forEach((c, i) => box(s, xs[2], cy0 + i * (ch + cg), W, ch, C.NAVY, c[0], c[1], { color: C.WHITE, hs: 10.5, bs: 10 }));

  G.source(s, "Company Filings and Calls, Muddy Waters, GE Aerospace, J&F order release (Jul-26), TechCrunch (Boom–Crusoe)",
    ["Value at risk from the valuation bridge (bear → base by thesis). ✓ = already reported."]);
};
