"""Render FTAI catalyst map pages (HTML with inline SVG) for screenshotting to PNG."""
import csv, html, math, os
from datetime import date

from prices import P
from events import ERAS, E

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "build")
os.makedirs(OUT, exist_ok=True)

C = dict(line="#2a78d6", up="#1f8a4c", down="#c93a3a", mech="#7d7c77", ink="#0b0b0b", ink2="#52514e",
         ink3="#8a8984", grid="#e7e6e1", surface="#fcfcfb", band="#f2f1ec", card="#ffffff", border="#e2e1db")
GLYPH = dict(up="▲", down="▼", mech="◆")
CONF = dict(verified=("Move size sourced", "#1f6f8b"), estimated=("Move size estimated", "#9a6b00"),
            context=("Catalyst from macro context", "#7d7c77"))


def d(s):
    return date.fromisoformat(s)


def esc(s):
    return html.escape(s, quote=True)


def load_prices():
    """Prefer a real daily CSV if one is dropped in data/, else the reconstructed series."""
    path = os.path.join(ROOT, "data", "ftai_daily.csv")
    if os.path.exists(path):
        with open(path) as f:
            rows = [(r["Date"], float(r["Close"]), True) for r in csv.DictReader(f) if r.get("Close")]
        return [(d(a), b, c) for a, b, c in rows], True
    return [(d(a), b, c) for a, b, c in P], False


PRICES, REAL = load_prices()


class Scale:
    def __init__(self, d0, d1, y0, y1, x, w, y, h, log=False):
        self.d0, self.d1, self.y0, self.y1 = d0, d1, y0, y1
        self.x, self.w, self.y, self.h, self.log = x, w, y, h, log

    def X(self, dt):
        return self.x + (dt - self.d0).days / (self.d1 - self.d0).days * self.w

    def Y(self, v):
        if self.log:
            t = (math.log(v) - math.log(self.y0)) / (math.log(self.y1) - math.log(self.y0))
        else:
            t = (v - self.y0) / (self.y1 - self.y0)
        return self.y + self.h - t * self.h


def nice_ticks(lo, hi, n=6):
    span = hi - lo
    step = 10 ** math.floor(math.log10(span / n))
    for m in (1, 2, 2.5, 5, 10):
        if span / (step * m) <= n:
            step *= m
            break
    t = math.ceil(lo / step) * step
    out = []
    while t <= hi + 1e-9:
        out.append(round(t, 6))
        t += step
    return out


def place_badges(evs, sc, r=11, bounds=None):
    """Greedy collision-avoiding badge placement. Up events prefer above the line, down below."""
    placed = []  # (cx, cy)
    out = []
    for e in sorted(evs, key=lambda e: e["date"]):
        px, py = sc.X(d(e["date"])), sc.Y(e["px"])
        pref = -1 if e["dir"] == "up" else 1
        cands = []
        for k in range(1, 9):
            cands += [(px, py + pref * (14 + 24 * k)), (px, py - pref * (14 + 24 * k))]
        best = None
        for cx, cy in cands:
            if bounds and not (bounds[0] + r <= cy <= bounds[1] - r):
                continue
            if all((cx - qx) ** 2 + (cy - qy) ** 2 >= (2 * r + 3) ** 2 for qx, qy in placed):
                best = (cx, cy)
                break
        if best is None:
            best = cands[0]
        placed.append(best)
        out.append((e, px, py, best[0], best[1]))
    return out


def svg_chart(d0, d1, W, H, log, evs, bands=None, pad=(64, 24, 34, 40), ylim=None, r=11, fs=11.5):
    L, R, T, B = pad
    inside = [i for i, (a, _, _) in enumerate(PRICES) if d0 <= a <= d1]
    pts = PRICES[max(0, inside[0] - 1): inside[-1] + 2]  # one neighbour each side, clipped below
    lo = min(PRICES[i][1] for i in inside)
    hi = max(PRICES[i][1] for i in inside)
    if log is None:
        log = hi / lo > 3
    if ylim:
        y0, y1 = ylim
    elif log:
        y0, y1 = lo * 0.7, hi * 1.9
    else:
        y0, y1 = max(0, lo - (hi - lo) * 0.3), hi + (hi - lo) * 0.38
    sc = Scale(d0, d1, y0, y1, L, W - L - R, T, H - T - B, log)
    s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" '
         f'font-family="Liberation Sans, DejaVu Sans, sans-serif">']
    # era bands
    if bands:
        for i, (b0, b1, lab) in enumerate(bands):
            x0, x1 = sc.X(max(b0, d0)), sc.X(min(b1, d1))
            if i % 2 == 0:
                s.append(f'<rect x="{x0:.1f}" y="{T}" width="{x1 - x0:.1f}" height="{H - T - B}" fill="{C["band"]}"/>')
            s.append(f'<text x="{(x0 + x1) / 2:.1f}" y="{T + 16}" text-anchor="middle" font-size="12" '
                     f'font-weight="700" fill="{C["ink2"]}" letter-spacing=".04em">{esc(lab)}</text>')
    # y grid
    if log:
        ticks = [t for t in (2, 3, 5, 7, 10, 15, 20, 30, 50, 75, 100, 150, 200, 300, 500) if y0 <= t <= y1]
    else:
        ticks = nice_ticks(y0, y1, 6)
    for t in ticks:
        y = sc.Y(t)
        s.append(f'<line x1="{L}" x2="{W - R}" y1="{y:.1f}" y2="{y:.1f}" stroke="{C["grid"]}" stroke-width="1"/>')
        s.append(f'<text x="{L - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="12" fill="{C["ink3"]}">${t:g}</text>')
    # x ticks: years (or quarters for short spans)
    span_days = (d1 - d0).days
    yr = d0.year
    while date(yr, 1, 1) <= d1:
        for mth in ((1,) if span_days > 900 else (1, 4, 7, 10)):
            dt = date(yr, mth, 1)
            if d0 <= dt <= d1:
                x = sc.X(dt)
                major = mth == 1
                s.append(f'<line x1="{x:.1f}" x2="{x:.1f}" y1="{H - B}" y2="{H - B + (6 if major else 4)}" stroke="{C["ink3"]}"/>')
                lab = str(yr) if major else ["", "Q1", "", "", "Apr", "", "", "Jul", "", "", "Oct"][mth]
                s.append(f'<text x="{x:.1f}" y="{H - B + 20}" text-anchor="middle" font-size="12" '
                         f'font-weight="{700 if major else 400}" fill="{C["ink2"] if major else C["ink3"]}">{lab}</text>')
        yr += 1
    s.append(f'<line x1="{L}" x2="{W - R}" y1="{H - B}" y2="{H - B}" stroke="{C["ink3"]}"/>')
    # price line
    s.append(f'<clipPath id="plot"><rect x="{L}" y="{T}" width="{W - L - R}" height="{H - T - B}"/></clipPath>')
    path = " ".join(f'{"M" if i == 0 else "L"}{sc.X(a):.1f},{sc.Y(b):.1f}' for i, (a, b, _) in enumerate(pts))
    s.append(f'<path d="{path}" fill="none" stroke="{C["line"]}" stroke-width="2.2" stroke-linejoin="round" clip-path="url(#plot)"/>')
    if not REAL:
        for a, b, c in pts:
            if c and d0 <= a <= d1:
                s.append(f'<circle cx="{sc.X(a):.1f}" cy="{sc.Y(b):.1f}" r="2.6" fill="{C["surface"]}" stroke="{C["line"]}" stroke-width="1.4"/>')
    # events
    for e, px, py, bx, by in place_badges(evs, sc, r=r, bounds=(T + 22, H - B - 2)):
        col = C[e["dir"]]
        s.append(f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="{col}" stroke-width="1" stroke-dasharray="2 2"/>')
        s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3.6" fill="{col}" stroke="{C["surface"]}" stroke-width="1.5"/>')
        s.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="{r}" fill="{col}" stroke="{C["surface"]}" stroke-width="2"/>')
        s.append(f'<text x="{bx:.1f}" y="{by + fs * 0.36:.1f}" text-anchor="middle" font-size="{fs}" font-weight="700" fill="#fff">{e["n"]}</text>')
    s.append("</svg>")
    return "\n".join(s)


CSS = f"""
*{{box-sizing:border-box}}
body{{margin:0;background:{C['surface']};color:{C['ink']};font-family:"Liberation Sans","DejaVu Sans",sans-serif;}}
.page{{width:1600px;padding:40px 48px 36px}}
.kicker{{font-size:13px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:{C['line']}}}
h1{{font-size:34px;line-height:1.15;margin:6px 0 8px;letter-spacing:-.01em}}
.sub{{font-size:16.5px;line-height:1.5;color:{C['ink2']};max-width:1340px;margin:0 0 18px}}
.stats{{display:flex;gap:12px;margin:0 0 18px}}
.stat{{border:1px solid {C['border']};background:{C['card']};border-radius:10px;padding:10px 16px;min-width:170px}}
.stat b{{display:block;font-size:24px;letter-spacing:-.01em}}
.stat span{{font-size:12.5px;color:{C['ink2']}}}
.chart{{border:1px solid {C['border']};border-radius:12px;background:{C['card']};padding:8px 6px 2px}}
.legend{{display:flex;gap:22px;font-size:13px;color:{C['ink2']};margin:10px 4px 0;flex-wrap:wrap}}
.legend i{{font-style:normal;font-weight:700}}
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:22px}}
.card{{border:1px solid {C['border']};background:{C['card']};border-radius:12px;padding:16px 18px 14px;break-inside:avoid}}
.ch{{display:flex;align-items:center;gap:10px;margin-bottom:6px}}
.num{{flex:0 0 28px;height:28px;border-radius:50%;color:#fff;font-weight:700;font-size:14px;display:flex;align-items:center;justify-content:center}}
.date{{font-size:13px;color:{C['ink2']};font-weight:700}}
.move{{margin-left:auto;font-size:13.5px;font-weight:700;padding:3px 10px;border-radius:999px;background:#f4f3ef;color:{C['ink']};white-space:nowrap}}
.card h3{{font-size:17.5px;line-height:1.3;margin:4px 0 8px}}
.lbl{{font-size:11.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:{C['ink3']};margin:8px 0 3px}}
.card ul{{margin:0;padding-left:18px}}
.card li{{font-size:14px;line-height:1.45;margin:2px 0;color:{C['ink']}}}
.why{{font-size:14px;line-height:1.5;color:{C['ink']};background:#f7f6f2;border-left:3px solid {C['line']};padding:8px 12px;border-radius:0 8px 8px 0}}
.conf{{font-size:11.5px;margin-top:9px;font-weight:700}}
.foot{{font-size:12px;line-height:1.5;color:{C['ink3']};margin-top:20px;border-top:1px solid {C['border']};padding-top:12px}}
.key{{display:grid;grid-template-columns:repeat(3,1fr);gap:4px 26px;margin-top:20px}}
.k{{display:flex;align-items:baseline;gap:8px;font-size:13.5px;line-height:1.35;padding:3px 0;border-bottom:1px solid #efeee9}}
.k .kn{{flex:0 0 22px;height:22px;border-radius:50%;color:#fff;font-weight:700;font-size:11.5px;display:flex;align-items:center;justify-content:center;align-self:center}}
.k .kd{{color:{C['ink2']};flex:0 0 66px;font-size:12.5px}}
.k .km{{margin-left:auto;font-weight:700;white-space:nowrap;font-size:12.5px}}
table.t{{border-collapse:collapse;width:100%;font-size:14px}}
table.t th{{text-align:left;font-size:11.5px;letter-spacing:.07em;text-transform:uppercase;color:{C['ink3']};padding:8px 10px;border-bottom:1px solid {C['border']}}}
table.t td{{padding:9px 10px;border-bottom:1px solid #efeee9;vertical-align:top;line-height:1.4}}
.panel{{border:1px solid {C['border']};background:{C['card']};border-radius:12px;padding:18px 20px}}
.panel h2{{font-size:19px;margin:0 0 4px}}
.panel p.s{{font-size:13.5px;color:{C['ink2']};margin:0 0 10px}}
"""

FOOT = ("Prices are nominal (not adjusted for dividends or the Aug-2022 FTAI Infrastructure spin-off). "
        + ("Price line: daily closes from data/ftai_daily.csv. " if REAL else
           "No price feed was reachable when this was built, so the line is rebuilt from sourced anchors (open dots: 10-K quarterly "
           "data, offering prospectuses, quoted closes) joined by month-end estimates (±10%); short-term wiggles are not shown. ")
        + "Catalysts come from company releases and SEC filings, earnings coverage (StockStory, Zacks, Benzinga, Investing.com), "
          "short reports (Muddy Waters, Snowcap) and sell-side notes as reported. Analysis as of Oct 3, 2026. Not investment advice.")


def fmt_date(s):
    dt = d(s)
    return dt.strftime("%b %-d, %Y")


def page(title, body):
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{esc(title)}</title><style>{CSS}</style></head><body><div class='page'>{body}</div></body></html>"


def legend():
    return (f"<div class='legend'><span><i style='color:{C['line']}'>━</i> FTAI share price (nominal)</span>"
            + ("" if REAL else f"<span><i style='color:{C['line']}'>○</i> sourced price anchor</span>")
            + f"<span><i style='color:{C['up']}'>▲</i> catalyst for an up-move</span>"
              f"<span><i style='color:{C['down']}'>▼</i> catalyst for a down-move</span>"
              f"<span><i style='color:{C['mech']}'>◆</i> mechanical (spin-off)</span>"
              "<span>Numbers match the catalyst cards</span></div>")


def overview():
    d0, d1 = date(2015, 4, 1), date(2026, 10, 15)
    bands = [(d(x["start"]), d(x["end"]), lab) for x, lab in zip(
        ERAS, ["FORTRESS HOLDCO", "COVID · RUSSIA · SPIN", "AEROSPACE RE-RATING", "SHORT ATTACK", "POWER & RESET"])]
    svg = svg_chart(d0, d1, 1500, 640, True, E, bands=bands, pad=(60, 20, 30, 40), ylim=(2.6, 420), r=11, fs=11)
    stats = [("$17.00", "IPO price · May 2015"), ("$3.69", "COVID low · Mar 18, 2020"),
             ("~$300", "All-time high · Feb 2026"), ("$167.10", "Latest close found · Sep 28, 2026"),
             ("41", "Catalysts mapped")]
    key = "".join(
        f"<div class='k'><span class='kn' style='background:{C[e['dir']]}'>{e['n']}</span>"
        f"<span class='kd'>{d(e['date']).strftime('%b %Y')}</span><span>{esc(e['short'])}</span>"
        f"<span class='km' style='color:{C[e['dir']]}'>{GLYPH[e['dir']]} {esc(e['move'].split(' (')[0])}</span></div>" for e in E)
    body = (f"<div class='kicker'>FTAI · Price action since IPO</div>"
            f"<h1>FTAI: from a $17 Fortress yield vehicle to an engine-aftermarket and power story</h1>"
            f"<p class='sub'>41 catalysts behind every meaningful move from the May 2015 IPO to today (log scale, so equal % moves look equal). "
            f"Five eras: a high-yield infrastructure LLC driven by oil and credit (2015–19) → COVID, Russia and the spin-off (2020–22) → "
            f"re-rating as a CFM56 engine-module business (2023–24) → a short-seller attack and recovery (2025) → data-center power hype and a margin reset (2026).</p>"
            + "<div class='stats'>" + "".join(f"<div class='stat'><b>{a}</b><span>{b}</span></div>" for a, b in stats) + "</div>"
            + f"<div class='chart'>{svg}</div>{legend()}<div class='key'>{key}</div><div class='foot'>{FOOT}</div>")
    return page("FTAI catalyst map", body)


def era_page(era):
    evs = [e for e in E if e["era"] == era["key"]]
    d0, d1 = d(era["start"]), d(era["end"])
    svg = svg_chart(d0, d1, 1500, 470, None, evs, pad=(60, 24, 20, 40), r=13, fs=13)
    cards = []
    for e in evs:
        lab, ccol = CONF[e["conf"]]
        col = C[e["dir"]]
        cards.append(
            f"<div class='card'><div class='ch'><span class='num' style='background:{col}'>{e['n']}</span>"
            f"<span class='date'>{fmt_date(e['date'])}</span>"
            f"<span class='move' style='color:{col}'>{GLYPH[e['dir']]} {esc(e['move'])}</span></div>"
            f"<h3>{esc(e['title'])}</h3><div class='lbl'>What happened</div><ul>"
            + "".join(f"<li>{esc(w)}</li>" for w in e["what"])
            + f"</ul><div class='lbl'>Why the stock moved</div><div class='why'>{esc(e['why'])}</div>"
              f"<div class='conf' style='color:{ccol}'>● {lab}</div></div>")
    body = (f"<div class='kicker'>FTAI catalyst map · Era {ERAS.index(era) + 1} of 5</div><h1>{esc(era['title'])}</h1>"
            f"<p class='sub'>{esc(era['sub'])}</p><div class='chart'>{svg}</div>{legend()}"
            f"<div class='cards'>{''.join(cards)}</div><div class='foot'>{FOOT}</div>")
    return page(era["title"], body)


# --------- playbook page: aerospace segment + earnings scorecard ---------
AERO = [  # quarter, Aerospace Products adj. EBITDA $M, margin % (None = not disclosed / not found), derived?
    ("Q1'23", 27.4, None, False), ("Q2'23", 30.1, 44, False), ("Q3'23", 40.6, 38, False), ("Q4'23", 55.0, None, False),
    ("Q1'24", 70.3, 37, False), ("Q2'24", 91.2, 37, False), ("Q3'24", 101.8, 34, False), ("Q4'24", 117.7, None, True),
    ("Q1'25", 131.0, 36, False), ("Q2'25", 164.9, 39, False), ("Q3'25", 180.4, 35, False), ("Q4'25", 195.0, None, True),
    ("Q1'26", 222.6, 30, False), ("Q2'26", 249.7, 29, False),
]

SCORE = [  # report date, quarter, EPS actual vs est, the line that mattered, reaction, dir
    ("Apr 2023", "Q1'23", "$0.22 vs $0.41 ✗", "Aerospace $27M; '$100M+ in 2023 very doable'", "Shrugged off; 2023 +182%", "up"),
    ("Feb 2024", "Q4'23", "$1.09 vs $0.44 ✓", "178 modules to 30 customers in 2023", "Rally continued", "up"),
    ("Jul 2024", "Q2'24", "−$2.26 vs $0.32 ✗", "Aero guide ~$250M → $325–350M; loss was one-time internalization fee", "Rally to ATH $124", "up"),
    ("Oct 2024", "Q3'24", "$0.76 vs $0.77 ≈", "Leasing helped by asset-sale gains; module counts no longer disclosed", "−11.1%", "down"),
    ("Feb 2025", "Q4'24", "$0.84 vs $0.89 ✗", "EBITDA $252M vs $240M beat; came days after the audit review cleared FTAI", "≈ −5%", "down"),
    ("May 2025", "Q1'25", "$0.87 vs $0.95 ✗", "Aero margin 36% (from ~40%); fewer asset-sale gains", "−14.8%", "down"),
    ("Jul 2025", "Q2'25", "$1.57 vs $1.30 ✓", "184 modules, 39% margin, >$400M FCF", "+14.3%", "up"),
    ("Oct 2025", "Q3'25", "$1.10 vs $1.21 ✗", "First 2026 guide: Aerospace $1.0B; dividend raised", "≈ +2%", "up"),
    ("Feb 2026", "Q4'25", "$1.08 vs $1.25 ✗", "2026 guide +$100M; Mod-1 turbine timeline", "≈ −4% pre-mkt", "down"),
    ("Apr 2026", "Q1'26", "$1.29 vs $1.54 ✗", "Revenue +12% beat; modules 270 vs 138; margin ~30% by design", "+17.2%", "up"),
    ("Jul 2026", "Q2'26", "$1.13 vs ~$1.35+ ✗", "Margin ~30% guided for 1–2 yrs; leasing guide $575M → $475M", "−19% AH, closed flat", "down"),
]


def aero_svg():
    W, H = 720, 400
    L, R, T, B = 56, 16, 20, 50
    n = len(AERO)
    bw = (W - L - R) / n
    top = 260
    s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Liberation Sans, DejaVu Sans, sans-serif">']
    # top: EBITDA bars
    bh = 210
    for t in (0, 50, 100, 150, 200, 250):
        y = T + bh - t / top * bh
        s.append(f'<line x1="{L}" x2="{W - R}" y1="{y:.1f}" y2="{y:.1f}" stroke="{C["grid"]}"/>')
        s.append(f'<text x="{L - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="11.5" fill="{C["ink3"]}">${t}M</text>')
    for i, (q, v, m, der) in enumerate(AERO):
        x = L + i * bw + 7
        h = v / top * bh
        y = T + bh - h
        fill = C["line"] if not der else "#9ec5f4"
        s.append(f'<path d="M{x:.1f},{T + bh} V{y + 4:.1f} Q{x:.1f},{y:.1f} {x + 4:.1f},{y:.1f} H{x + bw - 18:.1f} '
                 f'Q{x + bw - 14:.1f},{y:.1f} {x + bw - 14:.1f},{y + 4:.1f} V{T + bh} Z" fill="{fill}"/>')
        s.append(f'<text x="{x + (bw - 14) / 2:.1f}" y="{y - 5:.1f}" text-anchor="middle" font-size="11" fill="{C["ink2"]}">{v:.0f}</text>')
        s.append(f'<text x="{x + (bw - 14) / 2:.1f}" y="{T + bh + 16:.1f}" text-anchor="middle" font-size="11" fill="{C["ink2"]}">{q}</text>')
    # bottom: margin dots
    y0m, y1m, mt, mh = 25, 47, T + bh + 34, 110
    MY = lambda v: mt + mh - (v - y0m) / (y1m - y0m) * mh
    for t in (30, 35, 40, 45):
        s.append(f'<line x1="{L}" x2="{W - R}" y1="{MY(t):.1f}" y2="{MY(t):.1f}" stroke="{C["grid"]}"/>')
        s.append(f'<text x="{L - 8}" y="{MY(t) + 4:.1f}" text-anchor="end" font-size="11.5" fill="{C["ink3"]}">{t}%</text>')
    pts = [(L + i * bw + 7 + (bw - 14) / 2, MY(m), m) for i, (q, v, m, der) in enumerate(AERO) if m]
    s.append('<path d="' + " ".join(f'{"M" if j == 0 else "L"}{x:.1f},{y:.1f}' for j, (x, y, m) in enumerate(pts))
             + f'" fill="none" stroke="{C["down"]}" stroke-width="2"/>')
    for x, y, m in pts:
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{C["down"]}" stroke="#fff" stroke-width="2"/>')
        s.append(f'<text x="{x:.1f}" y="{y - 9:.1f}" text-anchor="middle" font-size="11" font-weight="700" fill="{C["ink"]}">{m}%</text>')
    s.append("</svg>")
    return "\n".join(s)


def playbook():
    rows = "".join(
        f"<tr><td style='white-space:nowrap'><b>{q}</b><br><span style='color:{C['ink3']};font-size:12.5px'>{r}</span></td>"
        f"<td style='white-space:nowrap'>{esc(eps)}</td><td>{esc(line)}</td>"
        f"<td style='white-space:nowrap;font-weight:700;color:{C[dr]}'>{GLYPH[dr]} {esc(rx)}</td></tr>"
        for r, q, eps, line, rx, dr in SCORE)
    rules = [
        ("1 · Aerospace guidance moves the stock; GAAP EPS doesn't",
         "FTAI missed EPS consensus in 8 of the 11 reports tracked here and rose after half of them. The market values the "
         "Aerospace Products EBITDA trajectory (guide raised from $200–250M for 2024 to ~$1.05B for 2026) plus module volume. "
         "When those rise, a miss is ignored (Q1'23, Q2'24, Q3'25, Q1'26)."),
        ("2 · Earnings-quality doubts cause the big drops",
         "The largest company-specific falls all came from questions about how the profit is made, not how much: asset-sale gains "
         "and reduced disclosure (Q3'24, −11%), the Muddy Waters/Snowcap gains-on-sale and depreciation claims (−24%, −23%, −10%), "
         "lighter gains plus margin slip (Q1'25, −15%), and the ~30% margin reset (Q2'26, −19% after hours)."),
        ("3 · Aerospace margins are trending down",
         "44% → 37% → 34% → 39% → 35% → 30% → 29%. The 2023–24 multiple assumed HEICO-like 40% aftermarket margins. Management now "
         "trades margin for volume (full-restoration work, large airline programs). Dollar EBITDA still compounds, but the multiple "
         "investors will pay for it is being re-set."),
        ("4 · Oil and credit shocks hit every era",
         "2015–16 oil crash (−43%), Q4-2018 credit/oil sell-off (−35%), COVID plus the oil price war (−80%), Russia sanctions (−35%), "
         "tariffs (−37%), and the 2026 Iran war with Brent above $100 (−30%). Fuel and credit stress hit the same lessees whose flight "
         "hours drive FTAI's shop visits."),
        ("5 · Simplifying the structure preceded each re-rating",
         "Spinning off infrastructure (Aug 2022) → C-corp conversion with no K-1 (Nov 2022) → internalizing Fortress (May 2024) → "
         "asset-light SCI (Dec 2024). Each removed a discount, and the 10x run came after them. Common-equity raises did the "
         "opposite and marked local tops (Jan 2018, Sep 2021)."),
    ]
    margin_rule = rules.pop(2)
    rule_html = "".join(f"<div class='card'><h3 style='margin-top:0'>{esc(a)}</h3><div class='why'>{esc(b)}</div></div>" for a, b in rules)
    body = (f"<div class='kicker'>FTAI catalyst map · The playbook</div>"
            f"<h1>What actually moves FTAI: five recurring patterns</h1>"
            f"<p class='sub'>Drawn from the 41 catalysts. Left: the business the market is paying for. Right: how each print was actually "
            f"judged. EPS beat or miss explains little; guidance trajectory and earnings quality explain most.</p>"
            f"<div style='display:grid;grid-template-columns:760px 1fr;gap:18px'>"
            f"<div class='panel'><h2>Aerospace Products: EBITDA is compounding, margin is fading</h2>"
            f"<p class='s'>Quarterly segment Adjusted EBITDA ($M, top) and EBITDA margin where reported (bottom). Light bars = derived "
            f"from full-year totals minus reported quarters.</p>{aero_svg()}"
            f"<h3 style='font-size:17px;margin:14px 0 8px'>{esc(margin_rule[0])}</h3><div class='why'>{esc(margin_rule[1])}</div></div>"
            f"<div class='panel'><h2>Earnings scorecard: EPS vs the line that mattered</h2>"
            f"<p class='s'>Reaction = next-session move where sourced; 2023–early 2024 rows describe the trend.</p>"
            f"<table class='t'><tr><th>Quarter</th><th>EPS vs est.</th><th>What the market traded on</th><th>Reaction</th></tr>{rows}</table></div></div>"
            f"<div class='cards'>{rule_html}</div><div class='foot'>{FOOT}</div>")
    return page("FTAI playbook", body)


if __name__ == "__main__":
    files = {"00_overview": overview(), "06_playbook": playbook()}
    for era in ERAS:
        files[era["file"]] = era_page(era)
    for name, h in files.items():
        with open(os.path.join(OUT, name + ".html"), "w") as f:
            f.write(h)
    print("\n".join(sorted(files)))
