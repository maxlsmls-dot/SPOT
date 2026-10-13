const G = require("./g");
const { C, F } = G;

function num(s, n, x, y, fill = C.NAVY) {
  s.addShape("ellipse", { x, y, w: 0.3, h: 0.3, fill: { color: fill }, line: { color: fill } });
  s.addText(String(n), { x, y, w: 0.3, h: 0.3, align: "center", valign: "middle", fontFace: F, fontSize: 13, color: C.WHITE, margin: 0, isTextBox: true });
}

module.exports = async function (pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "Opportunity Summary – A Compounder Still Priced for a Fraud");
  const X = 0.68, W = 12.25;

  G.banner(s, "The Set-up: A Short Report That Never Proved Out, and a Margin Reset That Looked Like Proof", X, 0.98, W, 0.36, 14);
  num(s, 1, X + 0.05, 1.45);
  G.para(s, "**++FTAI trades under a fraud overhang++**: Muddy Waters (Jan-25) alleged ++depreciated leasing engines were moved into Aerospace inventory at book value++, inflating margins; the stock fell 24% in a day. An ++audit-committee review found the claims without merit++ and nothing was restated, yet ++the discount never closed++.", X + 0.45, 1.4, W - 0.45, 0.8, { size: 14 });
  num(s, 2, X + 0.05, 2.27);
  G.para(s, "**++The 1H26 reset looked like confirmation++**: Aerospace margin fell ~500 bps in one quarter and management swapped its 40% target for ~30%. The market read it as ++the cheap leasing stock running out++ – the short thesis finally unwinding – and the stock now sits ++~48% below its $324 high at 9.2x FY27E EBITDA++.", X + 0.45, 2.22, W - 0.45, 0.8, { size: 14 });

  G.banner(s, "We believe the reset is a choice, not a confession – and place three trackable bets on FTAI.", X, 3.08, W, 0.36, 14);
  G.para(s, "Two observations underpin our theses: (i) ++even if the bears were right, leasing-sourced engines are <8% of inventory++ and (ii) ++the CFM56 aftermarket is supply-constrained++, so FTAI chose volume over margin.", X, 3.48, W, 0.55, { size: 14 });

  const boxes = [
    "**++Margins have bottomed at ~30%:++** Q1'26 leasing transfers were $90M against ~$1.4bn of inventory, and engines now flow the other way. Heavy-scope mix is capped by shop capacity, and ++PMA enters through SCI++, where FTAI is the lessor. Two more ~30% prints prove the trough.",
    "**++FTAI takes the CFM56 whitespace to ~25% share:++** OEMs and MROs are moving capacity to LEAP while LEAP problems keep CFM56s flying. FTAI's 3,000-module capacity is ++already built++; Jakarta and Cairo ramp in 2027.",
    "**++Power is a free call option:++** a ++signed $1.465bn order++; the grid falls 8–47 GW short from 2029 and many campuses sit at the stage the first buyer was. Today's price ++pays nothing for it++.",
  ];
  const ys = [4.08, 5.0, 5.67], hs = [0.85, 0.6, 0.6];
  boxes.forEach((t, i) => {
    s.addShape("rect", { x: X, y: ys[i], w: W, h: hs[i], fill: { color: C.BLUE }, line: { color: C.BLUE } });
    num(s, i + 1, X + 0.1, ys[i] + (hs[i] - 0.3) / 2);
    G.para(s, t, X + 0.5, ys[i] + 0.02, W - 0.6, hs[i] - 0.04, { size: 13.5, valign: "middle" });
  });

  s.addShape("rect", { x: X, y: 6.35, w: W, h: 0.62, fill: { color: "5B7189" }, line: { color: "5B7189" } });
  G.para(s, "**All we need is for margins to hold ~30% for two more prints. At $167 the market pays for our bear case; we see ++$309 in a year, 85% upside,++ with ++~5x reward-to-risk++.**^^1^^",
    X + 0.1, 6.35, W - 0.2, 0.62, { size: 14, color: C.WHITE, align: "center", valign: "middle" });

  G.source(s, "Company Filings, Muddy Waters Research (Jan-25), Earnings Calls, Bloomberg, GPS Model", ["1-year base-case sum of the parts (Oct-27); reward-to-risk = bull upside (+157%) / bear downside (–32%)."]);
};
