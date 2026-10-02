#!/usr/bin/env python3
"""
Analyse enriched play rows: label-group shares per surface, the three-major differential test,
the DIY positive control, optional external-baseline comparison, popularity strata, and a power
helper. All intervals are session-clustered (bootstrap over sessions), because Autoplay chains
within a session are strongly correlated.

Design logic (see analysis/dm-label-participation-method.md):
  * Treatment surface  = a Discovery Mode context (Autoplay; Radio or Daily Mix also work).
  * Control surface(s) = personalised but NOT a Discovery Mode context (Discover Weekly, Release
    Radar), dumped with dump_playlist.py. Optional but strongly recommended.
  * For each group g: R_g = ln( share_g(treatment) / share_g(control) ).
    - Equal participation by all three majors (all in, or all out) => R_UMG ~ R_SONY ~ R_WMG.
    - One major participating more than the others => its R is higher. That DIFFERENCE is what
      this experiment can identify. The absolute level (all in vs all out) is not identified.
  * Positive control: R_DIY - mean(R_majors) must be > 0 (self-released tracks go through
    DM-supporting distributors). If it is not, the setup cannot see DM at all and a null result
    on the majors is uninformative.

Example
  python3 analyze.py --inputs data/enriched.jsonl --treatment autoplay \
      --control discover_weekly,release_radar --baseline UMG=0.37,SONY=0.26,WMG=0.16 \
      --out ../../analysis/dm-autoplay-results.md
  python3 analyze.py --power 0.20 0.23      # n per arm to see a 3pp shift at 80% power
"""
from __future__ import annotations
import argparse
import collections
import glob
import json
import math
import random
import sys

FINE = ["UMG", "SONY", "WMG", "DIST_UMG", "DIST_SONY", "DIST_WMG", "INDIE", "DIY", "UNVERIFIED"]
MAJORS = ["UMG", "SONY", "WMG"]
COARSE_OF = {"UMG": "MAJOR_FRONTLINE", "SONY": "MAJOR_FRONTLINE", "WMG": "MAJOR_FRONTLINE",
             "DIST_UMG": "MAJOR_DIST", "DIST_SONY": "MAJOR_DIST", "DIST_WMG": "MAJOR_DIST",
             "INDIE": "NON_MAJOR", "DIY": "NON_MAJOR", "UNVERIFIED": "NON_MAJOR"}
COARSE = ["MAJOR_FRONTLINE", "MAJOR_DIST", "NON_MAJOR"]
Z = 1.959964


# ----------------------------------------------------------------------------- stats helpers
def _gammainc_upper_reg(a: float, x: float) -> float:
    """Regularised upper incomplete gamma Q(a, x) (Numerical Recipes gammq)."""
    if x <= 0:
        return 1.0
    gln = math.lgamma(a)
    if x < a + 1:  # series for P, return 1-P
        ap, s, d = a, 1.0 / a, 1.0 / a
        for _ in range(500):
            ap += 1
            d *= x / ap
            s += d
            if abs(d) < abs(s) * 1e-14:
                break
        return 1.0 - s * math.exp(-x + a * math.log(x) - gln)
    # continued fraction (modified Lentz)
    tiny = 1e-300
    b = x + 1 - a
    c = 1 / tiny
    d = 1 / b
    h = d
    for i in range(1, 500):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        d = tiny if abs(d) < tiny else d
        c = b + an / c
        c = tiny if abs(c) < tiny else c
        d = 1 / d
        delta = d * c
        h *= delta
        if abs(delta - 1) < 1e-14:
            break
    return math.exp(-x + a * math.log(x) - gln) * h


def chi2_sf(x: float, df: int) -> float:
    return _gammainc_upper_reg(df / 2.0, x / 2.0)


def chi2_homogeneity(table: list[list[int]]):
    """table[r][c] counts. Returns (chi2, df, p)."""
    R, C = len(table), len(table[0])
    row = [sum(r) for r in table]
    col = [sum(table[r][c] for r in range(R)) for c in range(C)]
    N = sum(row)
    if N == 0:
        return 0.0, (R - 1) * (C - 1), 1.0
    chi = 0.0
    for r in range(R):
        for c in range(C):
            e = row[r] * col[c] / N
            if e > 0:
                chi += (table[r][c] - e) ** 2 / e
    df = (R - 1) * (C - 1)
    return chi, df, chi2_sf(chi, df)


def wilson(y: int, n: int, z: float = Z):
    if n == 0:
        return (float("nan"), float("nan"))
    p = y / n
    den = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return centre - half, centre + half


def two_prop_n(p0: float, p1: float, alpha: float = 0.05, power: float = 0.80) -> int:
    """n per arm, two-sided two-sample test of proportions."""
    za, zb = 1.959964 if alpha == 0.05 else _z(1 - alpha / 2), _z(power)
    pbar = (p0 + p1) / 2
    num = (za * math.sqrt(2 * pbar * (1 - pbar)) + zb * math.sqrt(p0 * (1 - p0) + p1 * (1 - p1))) ** 2
    return math.ceil(num / (p1 - p0) ** 2)


def one_prop_n(p0: float, p1: float, alpha: float = 0.05, power: float = 0.80) -> int:
    za, zb = 1.959964 if alpha == 0.05 else _z(1 - alpha / 2), _z(power)
    num = (za * math.sqrt(p0 * (1 - p0)) + zb * math.sqrt(p1 * (1 - p1))) ** 2
    return math.ceil(num / (p1 - p0) ** 2)


def _z(q: float) -> float:
    """Inverse normal CDF (Acklam's approximation; fine for power calcs)."""
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02, 1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02, 6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00, -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00, 3.754408661907416e+00]
    plow, phigh = 0.02425, 1 - 0.02425
    if q < plow:
        u = math.sqrt(-2 * math.log(q))
        return (((((c[0] * u + c[1]) * u + c[2]) * u + c[3]) * u + c[4]) * u + c[5]) / ((((d[0] * u + d[1]) * u + d[2]) * u + d[3]) * u + 1)
    if q > phigh:
        u = math.sqrt(-2 * math.log(1 - q))
        return -(((((c[0] * u + c[1]) * u + c[2]) * u + c[3]) * u + c[4]) * u + c[5]) / ((((d[0] * u + d[1]) * u + d[2]) * u + d[3]) * u + 1)
    u = q - 0.5
    t = u * u
    return (((((a[0] * t + a[1]) * t + a[2]) * t + a[3]) * t + a[4]) * t + a[5]) * u / (((((b[0] * t + b[1]) * t + b[2]) * t + b[3]) * t + b[4]) * t + 1)


# ----------------------------------------------------------------------------- data
def load(patterns, include_seed=False, dedupe=True, dist_as_major=False):
    rows = []
    for pat in patterns:
        for path in sorted(glob.glob(pat)) or [pat]:
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    r = json.loads(line)
                    if r.get("row_type") != "play" or "group" not in r:
                        continue
                    if not include_seed and r.get("position") == 0:
                        continue
                    g = r["group"]
                    if dist_as_major and g.startswith("DIST_"):
                        g = g[5:]
                    rows.append({"session": r["session_id"], "surface": r["surface"], "group": g,
                                 "popularity": r.get("popularity"), "track_id": r["track_id"],
                                 "artist": (r.get("artists") or [""])[0], "label": r.get("label")})
    if dedupe:
        seen, out = set(), []
        for r in rows:
            k = (r["session"], r["track_id"])
            if k in seen:
                continue
            seen.add(k)
            out.append(r)
        rows = out
    return rows


def session_counts(rows):
    """{session: Counter(group)} for one surface's rows."""
    sc = collections.defaultdict(collections.Counter)
    for r in rows:
        sc[r["session"]][r["group"]] += 1
    return sc


def shares_from_counts(counters, groups):
    tot = collections.Counter()
    for c in counters:
        tot.update(c)
    N = sum(tot.values())
    return {g: (tot[g] / N if N else float("nan")) for g in groups}, N


def cluster_se(sc, g):
    """Analytic cluster-robust SE for the pooled proportion of group g over sessions sc."""
    ys = [(c[g], sum(c.values())) for c in sc.values()]
    N = sum(n for _, n in ys)
    Y = sum(y for y, _ in ys)
    if N == 0:
        return float("nan"), float("nan"), 0, 0
    p = Y / N
    m = len(ys)
    if m > 1:
        var = m / (m - 1) * sum((y - p * n) ** 2 for y, n in ys) / N ** 2
    else:
        var = p * (1 - p) / N
    return p, math.sqrt(var), N, m


def bootstrap(sc_T, sc_C, groups, reps=2000, seed=1):
    """Resample sessions within each arm; return dict stat -> list of replicate values."""
    rng = random.Random(seed)
    T = list(sc_T.values())
    C = list(sc_C.values()) if sc_C else None
    stats = collections.defaultdict(list)
    for _ in range(reps):
        bT = [T[rng.randrange(len(T))] for _ in T]
        sT, _ = shares_from_counts(bT, groups)
        for g in groups:
            stats[f"share_T[{g}]"].append(sT[g])
        if C:
            bC = [C[rng.randrange(len(C))] for _ in C]
            sC, _ = shares_from_counts(bC, groups)
            R = {}
            for g in groups:
                stats[f"share_C[{g}]"].append(sC[g])
                R[g] = math.log(sT[g] / sC[g]) if sT[g] > 0 and sC[g] > 0 else float("nan")
                stats[f"R[{g}]"].append(R[g])
            for i, a in enumerate(MAJORS):
                for b in MAJORS[i + 1:]:
                    stats[f"R[{a}]-R[{b}]"].append(R[a] - R[b])
            mj = [R[g] for g in MAJORS if not math.isnan(R[g])]
            if mj and not math.isnan(R.get("DIY", float("nan"))):
                stats["R[DIY]-mean(R[majors])"].append(R["DIY"] - sum(mj) / len(mj))
            if mj and not math.isnan(R.get("INDIE", float("nan"))):
                stats["R[INDIE]-mean(R[majors])"].append(R["INDIE"] - sum(mj) / len(mj))
            # majors-only composition in each arm
            mT = sum(sT[g] for g in MAJORS)
            mC = sum(sC[g] for g in MAJORS)
            for g in MAJORS:
                stats[f"majshare_T[{g}]"].append(sT[g] / mT if mT else float("nan"))
                stats[f"majshare_C[{g}]"].append(sC[g] / mC if mC else float("nan"))
                stats[f"majshare_T-C[{g}]"].append((sT[g] / mT if mT else float("nan")) - (sC[g] / mC if mC else float("nan")))
    return stats


def ci(vals, lo=2.5, hi=97.5):
    v = sorted(x for x in vals if not (isinstance(x, float) and math.isnan(x)))
    if not v:
        return float("nan"), float("nan")
    def q(p):
        k = (len(v) - 1) * p / 100
        f, c = math.floor(k), math.ceil(k)
        return v[f] + (v[c] - v[f]) * (k - f)
    return q(lo), q(hi)


def fmt_p(x):
    return "n/a" if x is None or (isinstance(x, float) and math.isnan(x)) else f"{100 * x:.1f}%"


def fmt_ci(lo, hi, pct=True):
    if math.isnan(lo):
        return "n/a"
    return f"[{100 * lo:.1f}%, {100 * hi:.1f}%]" if pct else f"[{lo:+.3f}, {hi:+.3f}]"


def pop_bin(p):
    if p is None:
        return "unknown"
    return "low (<40)" if p < 40 else ("mid (40-69)" if p < 70 else "high (>=70)")


# ----------------------------------------------------------------------------- report
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inputs", nargs="*", default=[])
    ap.add_argument("--treatment", default="autoplay")
    ap.add_argument("--control", default="", help="comma-separated control surfaces (pooled)")
    ap.add_argument("--baseline", default="", help="external shares, e.g. UMG=0.37,SONY=0.26,WMG=0.16")
    ap.add_argument("--include-seed", action="store_true")
    ap.add_argument("--no-dedupe", action="store_true", help="count repeat plays of a track within a session")
    ap.add_argument("--dist-as-major", action="store_true", help="fold DIST_X into X (distribution view)")
    ap.add_argument("--reps", type=int, default=2000)
    ap.add_argument("--out", default="")
    ap.add_argument("--power", nargs=2, type=float, metavar=("P0", "P1"))
    args = ap.parse_args()

    L = []
    if args.power:
        p0, p1 = args.power
        L.append(f"Power (alpha 0.05, power 0.80): two-arm n per arm = {two_prop_n(p0, p1)}; "
                 f"one-arm vs fixed baseline n = {one_prop_n(p0, p1)}  (for shares {p0:.3f} -> {p1:.3f}).")
        L.append("Multiply by the design effect for session clustering (typically 1.5-2.5 for 20-track Autoplay sessions).")
        if not args.inputs:
            print("\n".join(L))
            return

    rows = load(args.inputs, include_seed=args.include_seed, dedupe=not args.no_dedupe, dist_as_major=args.dist_as_major)
    if not rows:
        sys.exit("no enriched play rows found")
    groups = [g for g in FINE if not (args.dist_as_major and g.startswith("DIST_"))]
    controls = [c for c in args.control.split(",") if c]
    T = [r for r in rows if r["surface"] == args.treatment]
    C = [r for r in rows if r["surface"] in controls]
    if not T:
        sys.exit(f"no rows for treatment surface {args.treatment!r}; surfaces present: {sorted({r['surface'] for r in rows})}")
    sc_T = session_counts(T)
    sc_C = session_counts(C) if C else {}

    L.append("# Discovery Mode label-participation readout\n")
    L.append(f"Treatment surface: `{args.treatment}`. Control surface(s): `{','.join(controls) or 'none'}`. "
             f"Seed tracks {'included' if args.include_seed else 'excluded'}; repeats within a session "
             f"{'counted' if args.no_dedupe else 'deduped'}; major-owned distributors "
             f"{'folded into majors' if args.dist_as_major else 'kept separate'}.\n")

    # 1. data summary
    L.append("## 1. Data\n")
    L.append("| surface | served tracks | sessions | unique tracks | unique artists | UNVERIFIED share |")
    L.append("|---|---:|---:|---:|---:|---:|")
    for s in sorted({r["surface"] for r in rows}):
        rs = [r for r in rows if r["surface"] == s]
        unv = sum(r["group"] == "UNVERIFIED" for r in rs) / len(rs)
        L.append(f"| {s} | {len(rs)} | {len({r['session'] for r in rs})} | {len({r['track_id'] for r in rs})} | "
                 f"{len({r['artist'] for r in rs})} | {fmt_p(unv)} |")
    L.append("")

    # 2. shares by group
    boot = bootstrap(sc_T, sc_C, groups, reps=args.reps)
    L.append("## 2. Share of served tracks by label group (95% session-bootstrap CI)\n")
    hdr = "| group | " + args.treatment + " | " + (" | ".join([f"control ({','.join(controls)})"]) if C else "") + " |"
    L.append(hdr if C else f"| group | {args.treatment} |")
    L.append("|---|---:|" + ("---:|" if C else ""))
    sT, NT = shares_from_counts(sc_T.values(), groups)
    sC, NC = shares_from_counts(sc_C.values(), groups) if C else ({}, 0)
    for g in groups:
        cell_T = f"{fmt_p(sT[g])} {fmt_ci(*ci(boot[f'share_T[{g}]']))}"
        cell_C = f"{fmt_p(sC[g])} {fmt_ci(*ci(boot[f'share_C[{g}]']))}" if C else ""
        L.append(f"| {g} | {cell_T} |" + (f" {cell_C} |" if C else ""))
    for cg in COARSE:
        members = [g for g in groups if COARSE_OF[g] == cg]
        vT = [sum(boot[f"share_T[{g}]"][i] for g in members) for i in range(args.reps)]
        cell_T = f"{fmt_p(sum(sT[g] for g in members))} {fmt_ci(*ci(vT))}"
        if C:
            vC = [sum(boot[f"share_C[{g}]"][i] for g in members) for i in range(args.reps)]
            cell_C = f"{fmt_p(sum(sC[g] for g in members))} {fmt_ci(*ci(vC))}"
        L.append(f"| **{cg}** | {cell_T} |" + (f" {cell_C} |" if C else ""))
    L.append(f"\nServed tracks: treatment N={NT} over {len(sc_T)} sessions" + (f"; control N={NC} over {len(sc_C)} sessions." if C else "."))
    L.append("")

    # 3. differential test across the majors
    L.append("## 3. Differential test: do the three majors move together?\n")
    if C:
        L.append("Majors-only composition (share of UMG/SONY/WMG among major-frontline tracks) in each arm, and the "
                 "log-ratio R_g = ln(share in treatment / share in control) per group.\n")
        L.append("| major | comp. in treatment | comp. in control | difference (pp) 95% CI | R_g 95% CI |")
        L.append("|---|---:|---:|---:|---:|")
        for g in MAJORS:
            mT = ci(boot[f"majshare_T[{g}]"])
            mC = ci(boot[f"majshare_C[{g}]"])
            d = ci(boot[f"majshare_T-C[{g}]"])
            r = ci(boot[f"R[{g}]"])
            L.append(f"| {g} | {fmt_p(sT[g] / sum(sT[x] for x in MAJORS) if sum(sT[x] for x in MAJORS) else float('nan'))} {fmt_ci(*mT)} | "
                     f"{fmt_p(sC[g] / sum(sC[x] for x in MAJORS) if sum(sC[x] for x in MAJORS) else float('nan'))} {fmt_ci(*mC)} | "
                     f"{fmt_ci(*d)} | {fmt_ci(*r, pct=False)} |")
        tab = [[sum(c[g] for c in sc_T.values()) for g in MAJORS], [sum(c[g] for c in sc_C.values()) for g in MAJORS]]
        chi, df, p = chi2_homogeneity(tab)
        L.append(f"\nNaive (unclustered) chi-square of homogeneity, majors-only 2x3 table: chi2={chi:.2f}, df={df}, p={p:.4f}. "
                 "Treat as optimistic; the bootstrap CIs above are the ones to quote.\n")
        L.append("Pairwise differences in R (positive = first major over-represented in the DM surface relative to the second):\n")
        L.append("| pair | R difference 95% CI | reads as |")
        L.append("|---|---:|---|")
        for i, a in enumerate(MAJORS):
            for b in MAJORS[i + 1:]:
                lo, hi = ci(boot[f"R[{a}]-R[{b}]"])
                verdict = "no detectable difference" if lo <= 0 <= hi else (f"{a} relatively over-represented in DM surface" if lo > 0 else f"{b} relatively over-represented in DM surface")
                L.append(f"| {a} vs {b} | {fmt_ci(lo, hi, pct=False)} | {verdict} |")
        L.append("")
        L.append("## 4. Positive control (can this setup see Discovery Mode at all?)\n")
        L.append("| contrast | 95% CI | reads as |")
        L.append("|---|---:|---|")
        for key, label in (("R[DIY]-mean(R[majors])", "DIY (self-released, DM-eligible) vs majors"),
                           ("R[INDIE]-mean(R[majors])", "INDIE (known independents) vs majors")):
            if boot.get(key):
                lo, hi = ci(boot[key])
                verdict = ("DM lift visible: non-major content over-represented in the DM surface" if lo > 0 else
                           "no lift detected: a null on the majors is NOT informative" if lo <= 0 <= hi else
                           "non-major content UNDER-represented in the DM surface (check surface design confounds)")
                L.append(f"| {label} | {fmt_ci(lo, hi, pct=False)} | {verdict} |")
        L.append("")
    else:
        L.append("No control surface supplied. Without one you can only compare to an external baseline (section 5), "
                 "and you cannot run the positive control. Dump Discover Weekly / Release Radar with dump_playlist.py "
                 "and pass --control discover_weekly,release_radar.\n")

    # 5. external baseline
    L.append("## 5. Treatment shares vs an external baseline\n")
    if args.baseline:
        base = {k.strip().upper(): float(v) for k, v in (kv.split("=") for kv in args.baseline.split(","))}
        L.append("| group | observed | baseline | z (cluster-robust) | reads as |")
        L.append("|---|---:|---:|---:|---|")
        for g, b in base.items():
            if g in groups:
                p, se, N, m = cluster_se(sc_T, g)
            elif g in COARSE:
                # pool members
                merged = {s: collections.Counter({g: sum(c[x] for x in groups if COARSE_OF[x] == g), "_other": sum(c[x] for x in groups if COARSE_OF[x] != g)}) for s, c in sc_T.items()}
                p, se, N, m = cluster_se(merged, g)
            else:
                continue
            z = (p - b) / se if se and se > 0 else float("nan")
            verdict = "above baseline" if z > Z else ("below baseline" if z < -Z else "consistent with baseline")
            L.append(f"| {g} | {fmt_p(p)} | {fmt_p(b)} | {z:+.2f} | {verdict} |")
        L.append("\nCaveat: an external stream-share baseline is not the organic Autoplay mix, so read this section as "
                 "descriptive context, not as the test.\n")
    else:
        L.append("No --baseline supplied. Example: --baseline UMG=0.37,SONY=0.26,WMG=0.16 (Luminate US, by distribution) "
                 "or MAJOR_FRONTLINE=0.71 (Spotify 20-F, majors+Merlin, 2024).\n")

    # 6. popularity strata
    L.append("## 6. Shares within popularity strata (surface design confound check)\n")
    bins = ["low (<40)", "mid (40-69)", "high (>=70)", "unknown"]
    surfaces = [args.treatment] + (["control"] if C else [])
    L.append("| popularity bin | surface | n | " + " | ".join(groups) + " |")
    L.append("|---|---|---:|" + "---:|" * len(groups))
    for b in bins:
        for s in surfaces:
            rs = [r for r in (T if s == args.treatment else C) if pop_bin(r["popularity"]) == b]
            if not rs:
                continue
            cnt = collections.Counter(r["group"] for r in rs)
            L.append(f"| {b} | {s} | {len(rs)} | " + " | ".join(fmt_p(cnt[g] / len(rs)) for g in groups) + " |")
    L.append("")

    # 7. top artists per group (sanity check on the classifier)
    L.append("## 7. Most-served artists per group in the treatment surface (classifier sanity check)\n")
    for g in groups:
        cnt = collections.Counter((r["artist"], r["label"] or "") for r in T if r["group"] == g)
        if cnt:
            top = "; ".join(f"{a} [{lab}] x{n}" for (a, lab), n in cnt.most_common(8))
            L.append(f"- **{g}** ({sum(cnt.values())}): {top}")
    L.append("")

    text = "\n".join(L)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
        print(f"report -> {args.out}")
    else:
        print(text)


if __name__ == "__main__":
    main()
