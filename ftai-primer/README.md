# FTAI Aviation deep primer

A first-principles reference on FTAI Aviation Ltd. (NASDAQ: FTAI) and the CFM56 engine aftermarket,
built with the deep-primer method on 3 October 2026. Descriptive throughout; takes no view.

## Deliverables
- `FTAI Deep Primer.pdf` — the master: cover, contents, the Spine, Parts I–XII.
- `parts/spine.md|pdf` — the Spine: the whole chain in one pass, about twelve two-page sections,
  each ending with a pointer to the Part that carries the depth. Read this first.
- `parts/part01…part12 .md|pdf` — the twelve Parts, each also rendered on its own.
  I the CFM56 as a machine · II how money moves around an engine · III context and the translation
  table · IV the shop-visit market and the OEM aftermarket · V used serviceable material and
  teardown · VI PMA parts and DER repairs · VII FTAI Aerospace Products (the deepest Part) ·
  VIII FTAI Aviation Leasing and the Strategic Capital Initiative · IX FTAI Power · X FTAI the
  company · XI margin pools and peers · XII reference (glossary, chain map, margin pool, company
  index, unknowns register, consolidated sources).

## How it was built (research/ and build/)
- `research/chain-map.md` — Phase 1 chain-mapping pass and the dossier segments.
- `research/agent-brief.md` — the brief every research agent followed.
- `research/dossiers/D1…D11` — eleven frame-free research dossiers (about 100,000 words).
- `research/edgar-index.md`, `research/orchestrator-notes.md` — filing URLs, gap-fill facts and
  post-reconciliation resolutions.
- `research/reconciliation.md` — Phase 2: 70 tensions, corroborations, 84 cross-dossier information
  needs, a 176-entry unknowns register, and the writers' binding-numbers table.
- `research/term-registry.md` — Phase 3: 302 terms with owner and first-use Parts.
- `outline.md`, `outline-skeleton.md`, `writer-brief.md` — Phase 4 structure and the writers' rules.
- `build/render.py`, `build/validate.py`, `build/fill_rows.py`, `build/compile_master.sh`,
  `build/assets/` — the render pipeline (EB Garamond stylesheet with primer components).

## Sourcing note
Direct EDGAR access was denied by the build environment's network policy, so filing figures were
reached through sec.gov-restricted web search and cited to the EDGAR URL returned. Earnings-call
content was reached through third-party coverage where stated. Consultancy blogs are labelled as
such wherever cited. Figures that come only from call coverage are labelled "call coverage".
