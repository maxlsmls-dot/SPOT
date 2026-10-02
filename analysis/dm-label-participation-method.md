# Are all three majors in Discovery Mode? — Autoplay label-mix experiment, method

Status: method + tooling drafted 2026-10-02. No live data yet. Tooling lives in `tools/dm_autoplay/`
(see its README for the runbook). Nothing here is an investment view.

---

## 0. The short version

**The naive design does not identify what we want.** Counting the label mix of what Autoplay serves
and asking "is it roughly a three-way split?" cannot answer whether the majors participate, for two
reasons:

1. Autoplay is overwhelmingly *organic* recommendation. Discovery Mode (DM) only tilts the draw toward
   enrolled tracks; it does not replace the pool. So the label mix of Autoplay is dominated by each
   label's organic share of listening (UMG > Sony > WMG, and together with Merlin they were 71% of all
   Spotify streams in 2024), not by who opted into DM. A three-way even split would never be expected,
   with or without DM.
2. "All three majors participate equally" and "none of them participate" produce the *same* Autoplay
   label mix. The absolute level of participation is not identified by any listener-side experiment.

**What a listener-side experiment can identify is *differential* participation**: whether one major's
content is lifted in DM surfaces relative to the other majors, and whether major content as a whole is
lifted relative to content we know is DM-eligible (self-released tracks via DistroKid, TuneCore, CD Baby
etc., which are on Spotify's published list of DM-supporting licensors).

So the design is two-armed: a DM surface (Autoplay) versus a personalised non-DM surface (Discover
Weekly + Release Radar) on the same accounts, with a positive control. Section 2 gives the logic,
section 3 the protocol, section 4 the readout, section 5 the sample size, section 6 the threats.

**Prior from public evidence** (worth stating before collecting anything): Spotify's own list of
licensors that support DM is made up of DIY and independent distributors (Amuse, CD Baby, DistroKid,
Stem, UnitedMasters, Vydia, TuneCore, Symphonic, Believe, RouteNote and others). The majors'
distribution arms (The Orchard and AWAL at Sony, ADA at Warner, Virgin Music Group and Ingrooves at
UMG) are not on it. Press reporting since 2021 has the majors publicly opposed to DM as payola-like, one
unnamed major running an early test, and Sony reportedly barring its use. The experiment is therefore
testing "has anything changed quietly", not "which of three obvious participants is in". The cheapest
direct evidence remains asking label-side experts whether the DM tab exists in their Spotify for Artists
accounts (section 7).

---

## 1. Facts about Discovery Mode that drive the design

| fact | why it matters |
|---|---|
| Opt-in per track by the *licensor* (label or distributor) in Spotify for Artists; Spotify takes a 30% commission on recording royalties for streams in DM contexts. | Participation is decided at the licensor level, so the unit of classification is the (P)-line owner / distributor, not the artist. |
| DM contexts as of the current Spotify support page: Spotify Radio, Autoplay, Daily Mix, and the Artist / Mood / Decade / Genre Mixes (Mixes were added Jan 2024). Discover Weekly, Release Radar, editorial playlists, search and library are *not* DM contexts; Smart Shuffle is not listed. | Autoplay is a valid treatment surface. Discover Weekly / Release Radar are the natural personalised controls. |
| DM is invisible to listeners and to the Web API: no flag on a track or a play says it was DM-served. | Participation must be inferred from over-representation, never observed directly. |
| Labels enrol a *subset* of catalogue, usually tracks they want to push. | The label-level effect is diluted; sample sizes must be large, and a null is only interpretable with a positive control. |
| Spotify 20-F: UMG + Sony + WMG + Merlin (including the majors' indie distribution arms) = 71% of streams in 2024, down from 87% in 2017; the FY2025 filing reports a small reversal upward. Luminate US 2024, by distribution: UMG ~37%, Sony ~26%, WMG ~16%, independents ~21%; by ownership, independents ~35%. | External baselines exist but measure total streams, not the organic Autoplay mix, so they are context, not the test. |
| Web API changes of 27 Nov 2024: new apps lose Recommendations, Related Artists, Audio Features, and access to Spotify-owned algorithmic/editorial playlists. Still available: playback control (Premium), currently-playing, albums (with `label` and `copyrights`), tracks (with `popularity`), user-owned playlists. | Capture via currently-playing polling; read Discover Weekly by copying it into a playlist you own. |

Sources: Spotify for Artists "Discovery Mode contexts" and "Getting access to Discovery Mode" support
pages; Spotify developer blog 2024-11-27; Music Business Worldwide on the 20-F stream-share series;
Luminate Year-End Report 2024; Digital Music News and Music Help Desk on major-label stance.

---

## 2. Identification: what the numbers can and cannot say

Write the share of Autoplay plays going to label group L as

    s_L(Autoplay)  ∝  b_L · (1 + e_L · (u − 1))

where `b_L` is L's organic share of what Autoplay would serve with DM switched off, `e_L` is the
fraction of L's Autoplay-eligible exposure that is DM-enrolled, and `u` is the DM uplift multiplier
on an enrolled track. We observe `s_L`; `b_L` is unknown and large; `e_L` is what we care about.

Dividing by the same group's share on a personalised *non-DM* surface removes `b_L` to the extent that
surface reflects the same taste profile:

    R_L = ln( s_L(Autoplay) / s_L(control) ) ≈ ln(1 + e_L (u − 1)) + δ_L

where `δ_L` is the surface-design term (Discover Weekly prefers unfamiliar tracks, Autoplay prefers
continuity). Among the three majors, `δ` should be close to common, because their content is the same
kind of content. So:

- **H0 (equal participation):** e_UMG = e_SONY = e_WMG, which includes "all out". Then R_UMG ≈ R_SONY ≈ R_WMG.
- **H1 (differential participation):** one major enrols materially more. Its R is higher; the pairwise
  differences R_i − R_j are the test statistics.
- **Positive control:** self-released content (group `DIY`) goes through licensors that support DM, so
  e_DIY > 0 and R_DIY − mean(R_majors) must be > 0. If it is not, the experiment cannot see DM at all
  and nothing about the majors can be concluded.
- **Not identified:** the level. Equal R across the majors is consistent with "all in" and "all out".
  Only the public licensor list and label-side testimony separate those.

A secondary comparison with real information in it: the three majors' *distribution arms*
(`DIST_SONY` = The Orchard/AWAL, `DIST_WMG` = ADA, `DIST_UMG` = Virgin/Ingrooves). If one of them has
quietly joined, its R will sit with `DIY`, not with its parent's frontline.

---

## 3. Protocol

### 3.1 Accounts

- One Premium account is enough for the primary test; two to six is better. A Premium Family plan gives
  six independent profiles for one fee and lets you (a) replicate across accounts, (b) randomise seed
  order across accounts so personalisation drift does not line up with label, (c) collect six Discover
  Weekly / Release Radar lists a week instead of one.
- Fresh accounts, US market (DM is live for US listeners), Autoplay ON in settings, nothing liked or
  followed, Private Session OFF. Private Session does stop listening from feeding recommendations, which
  would be useful, but it may also hide plays from the playback endpoints; test on one session before
  relying on it.
- Premium is required because playback-control endpoints are Premium-only and because the Free tier's
  mobile shuffle rules change what Autoplay does.

### 3.2 Seeds (stratified, single tracks, no context)

Autoplay is similarity-driven, so the seed's label neighbourhood leaks into what is served. Balance the
seeds so this cancels:

- Grid: seed group {UMG, SONY, WMG, INDIE, DIY} × genre (8–12: pop, hip-hop, R&B, rock, indie/alt,
  country, latin, electronic/dance, metal, lofi/instrumental, K-pop, jazz/classical as desired) ×
  popularity tier {≥70, 40–69}. That is 80–120 seeds; add a third tier (<40) if you want more.
- Each seed is used once per account. Shuffle the order (`--shuffle-seeds`) and keep the log order.
- Seed as a single track URI with no album or playlist context, so that when it ends the only thing that
  can continue playback is Autoplay. Everything after the seed is then Autoplay by construction, which
  sidesteps the known unreliability of the `context` field.
- Template: `tools/dm_autoplay/seeds.example.csv`.

### 3.3 Session

1. Start the seed on the experiment device (desktop app or web player logged into the account).
2. Let it finish. Autoplay begins.
3. Log the next K = 20 served tracks, played in full. Do not skip early: fast skips are negative
   feedback and may cause the batch to be regenerated. If you need throughput, `--dwell 35` skips after
   35 s (≥30 s counts as a stream), but validate first that the served list matches full-play runs.
4. The collector also snapshots `GET /me/player/queue` when Autoplay starts. If that queue already shows
   the upcoming Autoplay batch, later runs can read 20 tracks per seed in a few seconds; treat that as
   an optimisation to validate, not an assumption.
5. Pause, next seed.

Throughput at full play: roughly 75 minutes per session, so ~19 sessions and ~380 served tracks per
account-day. 150 sessions is about eight days on one account or a day and a half on six.

### 3.4 Control arm

- Each week, per account, copy Discover Weekly (30 tracks) and Release Radar (30 tracks) into a playlist
  you own (select all → add to playlist), then dump with `dump_playlist.py --surface discover_weekly`
  / `release_radar`. New API apps cannot read the algorithmic playlists directly.
- Optional second treatment for replication: Song Radio from the same seeds (also a DM context).
- Optional second control with a different bias: a fixed basket of editorial flagships (Today's Top
  Hits, RapCaviar, Rock This, Viva Latino, mint). Editorial is major-heavy for its own reasons, so use
  it only as a sensitivity check, never as the primary control.

### 3.5 Capture

`collect_autoplay.py` polls `GET /me/player/currently-playing` every 10 s and writes one JSON line per
served track: session id, account, surface, seed and its group/genre/tier, position in the chain,
track id, artists, album id, popularity, duration, context, timestamp. The recently-played endpoint is
not used: it returns `context: null` for many accounts and only keeps the last 50 plays.

### 3.6 Label classification

`enrich_labels.py` fetches each album's `label` and `copyrights` (the ℗ and © lines) and
`label_map.classify` maps them to:

| group | meaning | DM status |
|---|---|---|
| `UMG`, `SONY`, `WMG` | major-owned frontline imprint named in the ℗ line or label field | the question |
| `DIST_UMG`, `DIST_SONY`, `DIST_WMG` | content "under exclusive license to" a major, or via Virgin/Ingrooves, The Orchard/AWAL, ADA | not on the public licensor list; test separately |
| `INDIE` | known independents (Beggars, Domino, Concord, BMG, Believe, EMPIRE, ...) | mixed |
| `DIY` | self-released via DistroKid (`NNNNNNN Records DK`), TuneCore, CD Baby, UnitedMasters, Amuse ... or label == artist name | eligible: positive control |
| `UNVERIFIED` | nothing matched; treated as non-major and listed for review | review |

Rules: the ℗ line wins over the label field (it names the master owner); license/distribution phrases
turn a major match into `DIST_*`; "a division of" does not (that is frontline). Expect traps: some
major artists own their ℗ (Taylor Swift's label field is her name) — the review queue
(`data/review.csv`, sorted by served count) and `label_overrides.csv` exist for exactly this. Target
`UNVERIFIED` below 5% of served tracks, and hand-check every artist with three or more plays.

Two views of the same data: the ownership view (default, `DIST_*` kept separate) is the one that
matters for DM, because enrolment is by licensor and the majors' distribution arms are not listed as
supporting it; the distribution view (`--dist-as-major`) is only for comparability with Luminate.

---

## 4. Readout (`analyze.py`)

All intervals are session-clustered bootstraps (resampling sessions, not tracks), because the 20 tracks
in an Autoplay chain are strongly correlated. The report has seven sections:

1. **Data**: tracks, sessions, unique artists and the `UNVERIFIED` rate per surface.
2. **Shares by group** per surface, fine and coarse (`MAJOR_FRONTLINE`, `MAJOR_DIST`, `NON_MAJOR`).
3. **Differential test**: majors-only composition in each arm; R_g per major; pairwise R differences
   with CIs and a plain-language verdict; a naive chi-square for reference.
4. **Positive control**: R_DIY − mean(R_majors) and R_INDIE − mean(R_majors).
5. **External baseline** (optional): observed Autoplay shares vs Luminate / 20-F figures, descriptive only.
6. **Popularity strata**: shares within popularity <40 / 40–69 / ≥70, to check that the major-vs-major
   pattern is not an artefact of Discover Weekly skewing to lesser-known tracks.
7. **Top artists per group**: eyeball the classifier.

Decision rules:

| pattern | reading |
|---|---|
| Positive control CI includes or is below 0 | The setup cannot see DM. Do not interpret the majors. Check Autoplay is on, the account is US, N is adequate; consider Radio as a second treatment. |
| Positive control fires; pairwise major differences all include 0 with CIs narrower than about ±0.15 in log terms | The three majors are lifted equally. With the public licensor list and label testimony, the natural reading is "none, or token amounts". |
| One major's R is clearly higher than the other two | That major's frontline is enrolling materially more than the others. Follow up with popularity strata and the within-seed-group cut; then take it to an expert call. |
| A `DIST_*` group sits with `DIY` rather than with its parent | That distribution arm has joined DM even though the frontline has not. |
| Majors ≈ `INDIE` < `DIY` | DM lift is concentrated in DIY distributors; consistent with the public list. |

---

## 5. Sample size

From `analyze.py --power`: to see a 3-point move in one major's share of the majors pool (20% → 23%)
at 80% power you need about 2,900 major-label tracks per arm before clustering; a 5-point move needs
about 1,100. With roughly 60–65% of served tracks being major frontline, and a design effect of 1.5–2.5
for 20-track sessions, the treatment arm needs 5,000–8,000 Autoplay tracks (250–400 sessions). The
control arm is the constraint: Discover Weekly + Release Radar give only 60 tracks per account-week, so
six accounts over four weeks is about 1,440 tracks, ~950 of them major. That puts the minimum
detectable effect on a major's composition share near 5 points. Options if that is too coarse: run
more weeks, add Song Radio sessions as a second treatment (cheap, DM context) so the treatment arm is
not the bottleneck, and accept editorial baskets as a sensitivity control.

Recommended first pass: 300 Autoplay sessions across 2–6 accounts over four weeks, Discover Weekly and
Release Radar dumped weekly, then decide whether to extend.

---

## 6. Threats to validity and how the design handles them

- **Surface-design confound** (Discover Weekly favours novelty): read the pairwise differences among
  majors, which cancel the common term; check the popularity strata; replicate with Song Radio.
- **Personalisation drift** as the account accumulates history: randomise seed order, use several
  accounts, like nothing, compare early vs late sessions.
- **Seed neighbourhood**: stratified seeds by label group, genre and popularity; re-run the test within
  each seed group as a robustness cut.
- **Label mapping error**: ℗-line precedence, manual review of frequent artists, report with and
  without `UNVERIFIED`, two views (ownership vs distribution).
- **Dilution**: DM covers a subset of catalogue, so the label-level effect is small. This is why N is
  large and why a null without the positive control means nothing.
- **Geography**: DM lift is applied per listener market; keep every account in the US.
- **Platform drift**: Spotify changed the API in Nov 2024 and the DM context list in Jan 2024. Record
  the dates of every run and re-check the contexts page before interpreting.
- **Terms of service**: automated playback on your own accounts at human listening rates is ordinary
  use; do not scale to many accounts or try to simulate streams for anyone's benefit.

---

## 7. Cheaper direct evidence to run in parallel

- **Expert calls (this repo, Topics 2 and 3):** add to the question list: "Does your Spotify for Artists
  team see the Discovery Mode tab? Which of The Orchard, AWAL, ADA, Virgin have access? Has any major
  frontline enrolled tracks since 2024?" A label-side yes/no is dispositive in a way the experiment is not.
- **Spotify's supported-licensor page**: snapshot it monthly; a major distribution arm appearing on it
  answers the question directly.
- **Spotify investor commentary** on Discovery Mode scale (Loud & Clear, earnings calls) for the
  denominator of Topic 2.

---

## 8. Runbook

See `tools/dm_autoplay/README.md`. Order of operations: set up the app and account → fill `seeds.csv`
→ run `collect_autoplay.py` → weekly `dump_playlist.py` for Discover Weekly / Release Radar →
`enrich_labels.py` → work the review queue into `label_overrides.csv` → re-run `enrich_labels.py` →
`analyze.py --out analysis/dm-autoplay-results.md`.
