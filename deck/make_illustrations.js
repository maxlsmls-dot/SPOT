// Flat line illustrations for the Business Overview slide, in GPS navy / platinum.
// Renders SVG -> PNG with sharp. Output: deck/img/*.png
const fs = require("fs");
const path = require("path");
const sharp = require("sharp");

const NAVY = "#0A1C58", PLAT = "#847C7A", PLAT_LT = "#DCD8D3", WHITE = "#FFFFFF";
const OUT = path.join(__dirname, "img");
fs.mkdirSync(OUT, { recursive: true });

const wrap = (body) =>
  `<svg xmlns="http://www.w3.org/2000/svg" width="600" height="340" viewBox="0 0 600 340">${body}</svg>`;

// CFM56 turbofan, side profile facing left
const fanBlades = (() => {
  let s = "";
  for (let i = 0; i < 18; i++) {
    const a = (i / 18) * Math.PI * 2;
    const x1 = 84 + 7 * Math.cos(a), y1 = 180 + 22 * Math.sin(a);
    const x2 = 84 + 20 * Math.cos(a), y2 = 180 + 92 * Math.sin(a);
    s += `<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="${NAVY}" stroke-width="2.5"/>`;
  }
  return s;
})();
const engine = wrap(`
  <polygon points="150,84 182,30 318,30 336,100" fill="${NAVY}"/>
  <path d="M352,128 L452,140 Q472,143 472,160 L472,200 Q472,217 452,220 L352,232 Z" fill="${PLAT}" stroke="${NAVY}" stroke-width="5"/>
  <path d="M472,152 L548,180 L472,208 Z" fill="${PLAT_LT}" stroke="${NAVY}" stroke-width="5" stroke-linejoin="round"/>
  <path d="M86,78 Q58,78 58,180 Q58,282 86,282 L338,264 Q354,263 354,248 L354,112 Q354,97 338,96 Z"
        fill="${PLAT_LT}" stroke="${NAVY}" stroke-width="6" stroke-linejoin="round"/>
  <line x1="205" y1="87" x2="205" y2="273" stroke="${NAVY}" stroke-width="2.5"/>
  <line x1="290" y1="92" x2="290" y2="268" stroke="${NAVY}" stroke-width="2.5"/>
  <ellipse cx="86" cy="180" rx="24" ry="102" fill="${WHITE}" stroke="${NAVY}" stroke-width="6"/>
  ${fanBlades}
  <ellipse cx="84" cy="180" rx="9" ry="24" fill="${NAVY}"/>
`);

// Mobile gas-turbine power unit on a trailer
const louvres = Array.from({ length: 7 }, (_, i) =>
  `<line x1="116" y1="${152 + i * 11}" x2="186" y2="${152 + i * 11}" stroke="${NAVY}" stroke-width="3"/>`).join("");
const power = wrap(`
  <rect x="408" y="62" width="64" height="62" fill="${NAVY}"/>
  <rect x="398" y="50" width="84" height="14" rx="3" fill="${NAVY}"/>
  <rect x="108" y="86" width="118" height="38" fill="${PLAT}" stroke="${NAVY}" stroke-width="4"/>
  <rect x="88" y="120" width="452" height="130" rx="8" fill="${PLAT_LT}" stroke="${NAVY}" stroke-width="6"/>
  <rect x="106" y="142" width="90" height="88" fill="none" stroke="${NAVY}" stroke-width="3"/>
  ${louvres}
  <rect x="228" y="146" width="62" height="92" fill="none" stroke="${NAVY}" stroke-width="3"/>
  <circle cx="280" cy="194" r="4" fill="${NAVY}"/>
  <circle cx="420" cy="185" r="38" fill="${NAVY}"/>
  <polygon points="426,158 404,190 418,190 412,212 436,178 422,178" fill="${WHITE}"/>
  <path d="M30,262 L30,228 L88,228" fill="none" stroke="${NAVY}" stroke-width="8" stroke-linejoin="round"/>
  <rect x="30" y="250" width="540" height="18" fill="${NAVY}"/>
  ${[150, 196, 450, 496].map((x) => `<circle cx="${x}" cy="284" r="22" fill="${NAVY}"/><circle cx="${x}" cy="284" r="8" fill="${WHITE}"/>`).join("")}
`);

// Narrowbody aircraft (737NG / A320ceo class), side profile facing left
const windows = Array.from({ length: 19 }, (_, i) =>
  `<rect x="${118 + i * 18}" y="163" width="8" height="11" rx="3" fill="${NAVY}"/>`).join("");
const aircraft = wrap(`
  <polygon points="462,154 522,58 566,58 556,154" fill="${NAVY}"/>
  <path d="M30,184 C30,163 62,150 112,150 L500,150 C546,150 576,160 592,170 C576,192 546,206 500,206 L112,206 C62,206 30,202 30,184 Z"
        fill="${PLAT_LT}" stroke="${NAVY}" stroke-width="5"/>
  <line x1="70" y1="190" x2="560" y2="190" stroke="${PLAT}" stroke-width="5"/>
  ${windows}
  <polygon points="52,170 76,163 80,173 55,177" fill="${NAVY}"/>
  <polygon points="516,176 588,180 592,188 520,188" fill="${NAVY}"/>
  <polygon points="214,196 340,196 312,222 236,222" fill="${PLAT}" stroke="${NAVY}" stroke-width="4"/>
  <rect x="200" y="214" width="98" height="40" rx="20" fill="${NAVY}"/>
  <ellipse cx="206" cy="234" rx="7" ry="18" fill="${WHITE}"/>
`);

(async () => {
  for (const [name, svg] of [["cfm56", engine], ["power", power], ["aircraft", aircraft]]) {
    await sharp(Buffer.from(svg), { density: 200 }).png().toFile(path.join(OUT, `${name}.png`));
    console.log("wrote", name);
  }
})();
