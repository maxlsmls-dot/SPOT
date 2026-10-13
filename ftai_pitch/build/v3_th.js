const G = require("./g");
const { C, F } = G;

function num(s, n, x, y, fill) {
  s.addShape("ellipse", { x, y, w: 0.3, h: 0.3, fill: { color: fill }, line: { color: fill } });
  s.addText(String(n), { x, y, w: 0.3, h: 0.3, align: "center", valign: "middle", fontFace: F, fontSize: 13, color: C.WHITE, margin: 0, isTextBox: true });
}

module.exports = async function (pres) {
  const s = pres.addSlide({ masterName: "GPS" });
  G.title(s, "The Story: The Fraud Discount Frames Our Three Bets");

  const cols = [
    { x: 0.68, head: "Consensus FTAI Story", circ: "7F7F7F", line: "7F7F7F",
      intro: "FTAI's margins were flattered by the fraud. Now that it is unwinding:",
      items: [
        "The ~500 bps reset is the ++short thesis unwinding++: cheap leasing engines are running out, and heavier workscopes push margin ++below 30%++.",
        "The CFM56 is a melting ice cube: the fuel shock ++accelerates retirements++ and FTAI's share gains ++stall at ~15%++.",
        "Power is ++a press release++: one unnamed buyer, no deliveries until 2027 and no proof FTAI can ramp units.",
      ] },
    { x: 4.83, head: "Why consensus misses our points", circ: C.NAVY, line: C.TXT,
      intro: "We did the work the market skipped:",
      items: [
        "The market never sized the claim. We traced ++leasing-to-inventory transfers in the 10-Qs++: $90M vs. ~$1.4bn of inventory, and the flow now runs the other way.",
        "The street models retirements off assumptions. ++GE's own 2026 data++ shows 1.5–2%, and ++OEMs are moving slots to LEAP++, leaving visits to FTAI.",
        "Power is valued off one order. We ++built a NERC reserve-shortfall model++ and ++a site-level next-order model++ across 37 AI campuses.",
      ] },
    { x: 8.98, head: "Our FTAI Story", circ: "2E9BD6", line: "2E9BD6",
      intro: "The reset is a choice to win share in a supply-constrained market.",
      items: [
        "~30% is ++the floor, not a waypoint++: heavy mix is capped by capacity, PMA enters through SCI, and price pass-through ++rebuilds margin to 32.5%++.",
        "FTAI fills the whitespace OEMs leave behind: built capacity and partner shops take it to ++~25% of CFM56 module demand++ incl. SCI.",
        "Power is a call option: we see ++~75% odds of another order++ in 12 months (61% ex-xAI); one more contract is worth ++~$35/share++.",
      ] },
  ];
  const W = 3.95;
  cols.forEach((c) => {
    G.banner(s, c.head, c.x, 0.98, W, 0.36, 14);
    G.para(s, c.intro, c.x, 1.38, W, 0.5, { size: 13 });
    c.items.forEach((t, i) => {
      const y = 1.95 + i * 1.33;
      s.addShape("rect", { x: c.x, y, w: W, h: 1.2, fill: { type: "none" }, line: { color: c.line, width: 1.25, dashType: "dash" } });
      num(s, i + 1, c.x - 0.12, y - 0.13, c.circ);
      G.para(s, t, c.x + 0.08, y + 0.04, W - 0.14, 1.14, { size: 13, valign: "middle" });
    });
  });
  s.addShape("rect", { x: 0.68, y: 5.93, w: W, h: 0.45, fill: { color: C.GRAY }, line: { color: C.GRAY } });
  G.para(s, "Thus, consensus prices a ++fraud discount on a shrinking business++: 9.2x FY27E EBITDA.", 0.73, 5.93, W - 0.1, 0.45, { size: 12, valign: "middle" });
  G.para(s, "Diligence: 10-Q cash-flow footnotes, GE retirement data, SR Technics catalogues, NERC LTRA, site permits.", 4.83, 5.93, W, 0.45, { size: 12, valign: "middle", color: C.MUTE });
  G.para(s, "Catalysts: Q3'26 (late Oct), investor day (10-Dec), Q4'26 print and FY27 guide (Feb-27).", 8.98, 5.93, W, 0.45, { size: 12, valign: "middle", color: C.MUTE });

  s.addShape("rect", { x: 0.68, y: 6.43, w: 12.25, h: 0.52, fill: { type: "none" }, line: { color: C.RED, width: 1.5, dashType: "dash" } });
  G.para(s, "**Taking the other side of the fraud discount is a highly attractive proposition: two more ~30% prints prove the trough. Our bets playing out yield $309 in a year, 85% upside.**",
    0.75, 6.43, 12.1, 0.52, { size: 14.5, align: "center", valign: "middle" });
};
