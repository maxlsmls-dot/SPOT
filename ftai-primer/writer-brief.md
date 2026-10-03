# Writer brief — every Part author reads this in full before writing

You are writing one Part of a deep primer on FTAI Aviation Ltd. and the CFM56 engine aftermarket.
The reader is a smart non-expert who will finish the Part understanding every concept in it, not
just the headline. The Part is a reference document. It is descriptive. It takes no view.

## The four files you must read before writing
1. This brief.
2. /home/user/SPOT/ftai-primer/outline.md — your Part's section numbers and titles. Keep them.
3. /home/user/SPOT/ftai-primer/research/reconciliation.md — tensions, corroborations, information
   needs, the unknowns register, and section E "Instructions to writers" with the binding numbers.
   Every tension that touches your Part must be honoured as section E says.
4. /home/user/SPOT/ftai-primer/research/term-registry.md — which terms your Part owns, which it
   uses first, and the Spine vocabulary.
Then your dossier(s) in /home/user/SPOT/ftai-primer/research/dossiers/, and
/home/user/SPOT/ftai-primer/research/orchestrator-notes.md (facts gathered after the dossiers).
If a preceding Part exists in /home/user/SPOT/ftai-primer/parts/, read it as the style exemplar.

## Posture
- Explain, do not opine. No themes, no "what this means for investors", no bull or bear framing,
  no recommendations, no ranking of factors by importance. Where a genuine debate exists, lay out
  both sides' arithmetic and stop.
- Cover everything material; rank nothing. Every factor the dossier surfaced gets its own proper
  treatment with its own numbers.
- Where sources disagree, present both figures with both sources. Never average. Never pick.
- Never fill an absence. If the dossier logged an unknown, say it is unknown and what would
  resolve it.

## Depth register: functional mechanics
Explain the level that determines product and market outcomes. "Why a shop visit costs what it
costs" is the right depth. "How a single-crystal blade is cast" is not. Go one level deeper than
you think the reader needs and let them skim; never one level shallower.

The depth standard, by example. Too shallow: "LLP replacement is expensive." Right: define the
life-limited part in a box, give the cycle limits per module, give the list price of a full set by
year with sources, derive the escalation rate, work the stub-life arithmetic with real numbers,
then explain why that arithmetic creates a market for used LLPs with cycles remaining.

## The prose standard (as binding as the depth standard)
- One idea per sentence. About 20 words. Every sentence has a verb.
- Name a thing in plain words before you use its technical name.
- Never make the reader hold three definitions at once to parse one clause.
- Density comes from covering more ground, never from packing clauses into a sentence. A longer
  passage that reads fast beats a shorter one that reads slow.
- Prose paragraphs, three to eight sentences. Bullets only for genuinely parallel short items.
- No em-dashes. Use a comma, a full stop, or parentheses sparingly.
- Numbers: give the figure, its unit, its date and its source, in that order when all four matter.

## Components (use these exact HTML forms; the renderer processes markdown inside them)

Definition box, at the first use of every term your Part owns or uses first (per the registry):
<div class="defn"><b>Life-limited part (LLP)</b><p>One sentence saying what it is in plain words. One or two more sentences on why it matters here.</p></div>

Worked example, at least one per quantitative section; real numbers; step by step; each input
labelled sourced or assumed:
<div class="worked"><div class="h">Worked example 7.1 — a performance-restoration shop visit with LLPs</div>
<p>Inputs: ... (source).</p>
<div class="eqblock">total = 2,150,000 + 5,700,000 = 7,850,000</div>
<p>So ... Limits of the example: ...</p></div>

Callout for a mechanism that deserves emphasis (never an investment theme):
<div class="box"><div class="h">Why the module is the unit</div><p>...</p></div>

Exhibit (every exhibit has a title, a markdown table and a source line; number them Part.Seq):
<div class="exh"><div class="exh-title">Exhibit 7.3 — CFM56 modules refurbished by period</div>

| Period | Modules | Source |
|---|---:|---|
| Q2 2025 | 184 | FTAI Q2 2025 release |

<cite>Source: ... URL ... Accessed 2026-10-03.</cite></div>

Inline equation: <span class="eq">LRF = 45,000 / 6,400,000 = 0.70% per month</span>

Citations: after the load-bearing sentence, <span class="cite">[FTAI 10-K FY2025, segment note]</span>
or <span class="cite">[IBA, Sept 2025]</span>. Cite filings, releases, regulators and trade press by
short name and date. Every source used appears in the Part's final "Sources" section as a numbered
list with publisher, title, date and URL, copied from the dossier. Never invent a citation. If a
figure in the dossier carries no source, either drop it or label it "unsourced in the research".

Cross-reference other Parts as "see Part V §33" using outline.md section numbers.

## Structure of a Part file
Start with YAML front matter:
---
title: Part VII — FTAI Aerospace Products: the Module Factory
header: FTAI Deep Primer — Part VII
as_of: Research as of 3 October 2026
subtitle: Descriptive reference. Sources are cited inline and listed at the end. Takes no view.
toc: true
---
Then a part-divider block:
<div class="part-divider"><div class="pn">Part VII</div><h1>FTAI Aerospace Products: the Module Factory</h1><p>Two or three sentences on what this Part covers and what the reader will be able to do after it.</p></div>

Then, for Parts IV to XI, a short opening section (unnumbered, as a paragraph under a `### Translation-table rows answered` heading) naming the rows of the Part III translation table this Part answers. Parts I to III instead state in one paragraph where they sit in the first-principles build.

Then the numbered sections exactly as outline.md lists them: `## 45. What the segment sells, in FTAI's words`, with `### 45.1 ...` subsections as needed. Do not add an H1 inside the body. Do not renumber.

End with:
`## Tensions carried in this Part` (a short table: id from reconciliation, the two figures, where in the Part each appears),
`## Unknowns carried in this Part` (from the reconciliation register, verbatim questions),
`## Sources` (numbered).

## Length
Length is an output. Cover each section to its natural completion. A typical Part runs 9,000 to
16,000 words. Part VII should run 15,000 to 22,000. Never pad; never cut material to hit a number.

## Before you return
1. Render: `cd /home/user/SPOT/ftai-primer/build && python3 render.py ../parts/<file>.md --out ../parts/<file>.pdf`
2. Validate: `python3 validate.py ../parts/<file>.pdf ../parts/<file>.md` and fix every PROBLEM line
   (near-blank pages, exhibits without tables, unbalanced divs). Re-render until clean.
3. Lint acronyms: `python3 /root/.claude/skills/synced/95e68869-9677-4a7d-ba8b-37bc6b2958f4_75bf5e57-f4aa-4271-accb-4eb16a937fc2/writer/scripts/jargon_lint.py ../parts/<file>.md --allow FTAI,CFM,GE,IAE,SEC,NASDAQ,NYSE,LLC,LLP,JV,SPV,LP,URL,PDF` and gloss any acronym it flags that the registry says you define.
4. Checklist: every tension touching your Part presented both-sided; every owned or first-use term boxed; at least one worked example per quantitative section; no themes or recommendations; every exhibit has a table and a source; cross-references point to real section numbers.

## Return value
Return only: the markdown and PDF paths, page count, word count, the validator's last output,
the list of terms you defined, the list of reconciliation ids you presented, and any binding number
you could not source. Do not return the Part text.

## Refinements after Part I (binding for Parts II onward)
- Exemplar: /home/user/SPOT/ftai-primer/parts/part01-cfm56-machine.md. Read its §1 to §4 and §7 for
  style before writing; you need not read all of it.
- Citations: cite the underlying source (filing, release, regulator, trade article) by short name and
  date. Cite a dossier ("D3 §2.4") only when the dossier itself produced the figure (a derived number
  or a definition it assembled), and then say "derived in the research" in the sentence. A reader
  should rarely see a dossier id.
- Definition boxes: box only the terms the registry assigns to your Part as owner or first use. A term
  an earlier Part boxed gets a short in-prose reminder with a cross-reference, not a new box. A
  mechanism is not a term; it goes in prose or a callout.
- Section D of the reconciliation is the unknowns register; carry only the entries whose source
  dossier is yours or whose cluster touches your Part.
- Part I ran 63 pages and 22,000 words because it owns 53 terms. Expect your Part to run shorter
  unless the outline says otherwise; Part VII is the exception.
