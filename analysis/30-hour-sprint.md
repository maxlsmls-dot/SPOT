# 30-hour sprint — transcript-only diligence

Constraints: no live calls; Tegus transcript library (plus BamSEC / Canalyst if the seat includes them); public record. Goal: grade each of the five thesis points Confirmed / Supported / Unproven / Contradicted before the pitch, and rewrite the weak ones.

## Already settled on the public record (do not spend hours here)

| Item | Finding | Effect on thesis |
|---|---|---|
| DM eligible contexts | Still Radio, Autoplay, Mixes (Daily/Artist/Mood/Decade/Genre). Eligibility: 25k monthly listeners, 3 eligible songs. 30% haircut unchanged. | Point 4: "no new surface since 2024" holds |
| Majors and DM | Majors have historically refused the program ("race to the bottom", dilutes stream share). Distributors in: DistroKid, TuneCore/Believe, CD Baby, OneRPM, RouteNote, Stem, Symphonic, Vyja. | Point 4: drop "majors began participating". Majors joining is a risk to the short, not a spent driver |
| Audiobooks | Company: listening hours +37% y/y, 700k+ titles, >50% of eligible Premium users have played one, Audiobooks+ consumption +18%. | Drop "audiobook growth slowing". Keep: cost scales with usage, no pricing power vs Audible $8.95 / Amazon bundle |
| FY-25 20-F opex | R&D −€93M (social costs −€108M, SBC −€12M) but IT costs +€30M on cloud usage. GCP minimum-spend commitment exists; table amounts need the filing itself. | Point 5: cloud line was already rising before the 2026 step-up |
| Regional mix Q2-26 | MAU: RoW ~37%, LatAm ~21%, Europe ~25%, NA ~17%. Subs: Europe 36%, NA 25%, LatAm 24%, RoW 15%. Implied conversion: RoW ~16%, LatAm ~44%, Europe ~56%, NA ~57%. | Point 3: the EM funnel converts at a quarter of the mature-market rate |
| UMG Q2 call (30 Jul) | Grainge: "additional pricing coming through in the back half of the year"; on Spotify's AI tier, "very important for us to work to get our artists to opt in to support the launch". | Point 1: check whether an Aug/Sep-26 international Spotify round happened (shifts the lapping schedule). Point 2: artist opt-in is a gating item, supports delay |
| Antenna (public) | Spotify monthly churn ~2%, lowest of major streamers; Gen Z subscription fatigue rising in 2026. | Point 1: churn is low in level; the argument must be about the change after the Feb-26 hike, not the level |
| Music Pro teardowns | No 2026 APK strings for a "Music Pro" tier in the public teardown coverage. | Point 2: weak support for "not imminent" |

## Hour 0–2 — Tegus library sweep, build the reading list

Search strings, in order. Filter to calls dated 2025–2026 first, then 2024. Read the Tegus summary and expert bio only; keep or skip in under a minute each.

- **All Spotify transcripts dated after 4 Aug 2026.** Read every one first. These carry the post-Q2 read on MAU friction, opex and add-ons.
- **Point 4 (8–10 transcripts):** "Discovery Mode"; "Marquee"; "Showcase"; "Spotify marketplace"; "two-sided marketplace"; "Spotify recommendations"; "Spotify algorithm promoted". Experts: distributor execs (DistroKid, TuneCore, Believe, CD Baby, Downtown, Symphonic, Stem, OneRPM, Amuse), former Spotify marketplace PM/BD, former Spotify personalization or recs engineers, Merlin-member label heads, major-label digital strategy.
- **Point 1 (5–6):** "Spotify price increase"; "Spotify churn"; "Spotify elasticity"; "Spotify ARPU"; "Streaming 2.0"; "wholesale" + "Spotify"; "Spotify Premium" + "pricing". Experts: former Spotify Premium/pricing/revenue management, former Spotify FP&A, former UMG/WMG/Sony commercial, former Apple Music / YouTube Music / Amazon Music commercial.
- **Point 3 (3–4):** "Spotify India"; "Spotify Indonesia"; "Premium Lite"; "Spotify emerging markets"; "Spotify free tier"; "Spotify telco"; "JioSaavn"; "Gaana". Experts: former Spotify country managers or growth leads for India/SEA/MENA/LatAm, former Spotify growth analytics, ex-JioSaavn/Gaana.
- **Point 2 (3–4):** "Music Pro"; "Supremium"; "superfan" + "Spotify"; "Spotify HiFi"; "lossless"; "AI remix" + "Spotify"; "Reserved" + "Live Nation"; "Audiobooks+". Experts: former Spotify Premium product, former Spotify audiobooks, former label digital (superfan-tier negotiations), former Live Nation/Ticketmaster partnerships.
- **Point 5 (3–4):** "Spotify Google Cloud"; "Spotify infrastructure"; "Spotify machine learning"; "Spotify inference"; "AI DJ"; "Spotify content moderation"; "AI-generated music" + "Spotify"; "Spotify marketing budget". Experts: former Spotify platform/ML infra engineering leads, former Spotify FP&A, former Spotify trust & safety, ex-Deezer/Suno/Udio.

Target 20–30 transcripts. Paste each into `transcripts/` using the README naming convention and add a row to `calls-index.md`.

## Hour 2–16 — Read and extract

Ten minutes per transcript after the first pass. For each, record in the matrix: the claim, the quote, the number, the vantage (first-hand dashboard / first-hand internal / second-hand), and the call date. Do not summarize the whole call; only lines that bear on a topic. Transcripts pasted into the repo get triangulated into `topic-matrix.md` as they land.

Priority within the block: Topic 2 and 3 first (they decide whether point 4 is a variant view or a guess), then Topic 4, then 5, then 1 and 6.

## Hour 16–22 — Public-record checks (BamSEC / Canalyst / IR site)

- **20-F contractual obligations table**, FY-23, FY-24, FY-25: GCP minimum-spend commitment by year. A step-up is the hardest evidence available that compute is not temporary.
- **Regional back-solve** from the quarterly decks, Q1-24 to Q2-26: MAU and subs by region from the stated percentages; conversion by region; NA q/q series (confirms the Q1-26 decline).
- **ARPU bridge** (price / mix / FX) each quarter from the decks; lay the lapping schedule over it.
- **Opex by line** ex social charges, ex FX, each quarter; Q4 S&M as % of revenue 2023–25 (the seasonality consensus needs opex to fall into).
- **Confirm whether Spotify ran an international price round in Aug–Sep 2026.** Newsroom, support pages, MBW. If yes, the Q4-26 lapping date moves and point 1 must be stated for the US/Europe core only.
- **Label Q2 transcripts** (UMG 30 Jul, WMG early Aug): escalator mechanics, "additional pricing in H2", superfan tier timing, artist opt-in for the AI tier.
- **Canalyst or Visible Alpha quarterlies** for ARPU, subs, MAU, GM, opex, OI through Q4-27; replace the reconstructed consensus in the pitch's delta table.

## Hour 22–27 — Grade and rewrite

Grade each point from the matrix readouts. Rules: a point graded Unproven stays in the pitch only as a stated hypothesis with the evidence that would prove it; a point graded Contradicted comes out. Recompute the 2027 delta table with whatever changed. Expected outcome on current evidence: point 1 Supported, point 2 Supported, point 3 Supported, point 4 Unproven until Topics 2–3 fill, point 5 Supported.

## Hour 27–30 — Q&A prep

Write one-line answers to: How do you know DM is saturated? Do majors use DM? What is the audiobook royalty liability? What is the November catalyst? What if they hike in Q1? What if Music Pro launches? Why is the stock not already pricing this at 35% off the high? What is the FCF floor? What is your stop? Which of the five points has the most dollars behind it? Which has the least? What did you learn from the calls that the Street does not know?
