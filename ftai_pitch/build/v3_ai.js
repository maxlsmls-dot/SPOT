const G = require("./g");
const { C, F } = G;

function tbl(s, hdr, rows, x, y, w, colW, o = {}) {
  const sz = o.size || 10;
  const H = hdr.map((t) => ({ text: t, options: { bold: true, color: C.WHITE, fill: { color: C.NAVY }, fontFace: F, fontSize: sz, align: "center", valign: "middle" } }));
  s.addTable([H, ...rows.map((r, i) => r.map((c, j) => ({ text: G.parse(String(c) || " ", { fontFace: F, fontSize: sz, color: C.TXT }),
    options: { align: j === 3 ? "center" : "left", valign: "middle", fill: { color: i % 2 ? "F2F2F2" : C.WHITE } } })))],
    { x, y, w, colW, rowH: o.rowH || 0.3, border: { type: "solid", pt: 0.5, color: "BFBFBF" }, margin: [1, 4, 1, 4] });
}

module.exports = async function (pres) {
  const s = pres.addSlide({ masterName: "Pitch" });
  G.title(s, "Appendix: How We Used AI – Scrapes at Scale, Judgment Kept Human");
  const X = 0.68, W = 12.25;

  G.head(s, "AI let four analysts build datasets the street doesn't have – every number it pulled was traced back to a primary source.", X, 0.88, W, { size: 13.5 });
  tbl(s, ["Workstream", "What AI did", "What it produced", "Used on"], [
    ["**Repair-price scrape**", "Parsed SR Technics CFM56 catalogues (2024–26) and matched repair packages line by line across years", "++3,404 matched packages++: 3,376 rose, 1 fell → ~6% / yr escalator", "Industry"],
    ["**10-Q footnote extraction**", "Pulled leasing ↔ inventory transfers from every quarter's non-cash cash-flow disclosures", "Q1'26 transfers ++$89.6M vs. ~$1.4bn++ of inventory; flow now reverses", "Thesis I"],
    ["**Outsourcing flip tracker**", "Scraped releases, filings and trade press for 14 tier-1 shops; classified each shop's CFM56 / LEAP stance", "Positioning map: OEMs pulling back, ++independents adding++", "Thesis II"],
    ["**Test cell tracker**", "Searched shop announcements and trade press for engine test cells; tagged engine types per cell", "18 cells: ++9 adapted to LEAP, 0 dropped CFM56++", "Thesis II"],
    ["**Fuel & retirement check**", "Assembled jet-fuel series, GE / Safran commentary, airline capacity and hedge disclosures", "Fuel up ~2.3x, ++parked CFM56s falling++", "Thesis II"],
    ["**AI campus & permit screen**", "Read TCEQ / MDEQ permits, utility filings and project trackers; scored 37 sites on 7 win factors", "Site-level next-order model: ++~75% odds++ in 12M", "Thesis III"],
    ["**Jereh order ledger**", "Translated Chinese-language filings and press (Jiemian, NBD, TMTPost) into one reconciled ledger", "7 orders, ++$2.6bn++; J&F routing share for the Poisson check", "Thesis III"],
    ["**Grid gap model**", "Compiled NERC LTRA demand vs. capacity and 67 hyperscaler power agreements by region", "++8–47 GW++ reserve shortfall from 2029", "Thesis III"],
  ], X, 1.26, W, [2.1, 5.0, 4.1, 1.05], { rowH: 0.33, size: 10 });

  G.head(s, "AI did the reading and the arithmetic; the team made every call that moves the price target.", X, 4.36, W, { size: 13.5 });
  const LW = 6.0, R = X + 6.25;
  G.para(s, "**++Where AI helped++**", X, 4.74, LW, 0.26, { size: 11.5, align: "center" });
  G.bullets(s, [
    "**Scale:** thousands of catalogue lines and dozens of filings read in days, not weeks",
    "**Reach:** Chinese-language and state-permit sources the street rarely reads",
    "**Consistency:** one model feeds every slide; AI re-checked each figure across the deck",
  ], X, 5.0, LW, 1.4, { size: 11, psa: 3, valign: "top" });
  s.addShape("line", { x: R - 0.12, y: 4.76, w: 0, h: 1.62, line: { color: C.TXT, width: 1, dashType: "sysDot" } });
  G.para(s, "**++Guardrails we kept++**", R, 4.74, LW, 0.26, { size: 11.5, align: "center" });
  G.bullets(s, [
    "**Source or cut:** every AI-pulled number was checked against the document; claims with no source were dropped",
    "**Say what we didn't find:** no public case of an OEM cutting CFM56 cells – so we frame it as LEAP sharing slots",
    "**Human judgment:** probabilities, win scores, multiples and cases were set by the team; public information only",
  ], R, 5.0, LW, 1.4, { size: 11, psa: 3, valign: "top" });

  G.banner(s, "AI widened what we could check; it never decided what we believe – the thesis rests on sourced, team-verified data.", X, 6.48, W, 0.44, 14);
  G.source(s, "Team diligence files: flip tracker, test cell tracker, Power next-contract model, repair-price scrape; sources as cited on each slide");
};
