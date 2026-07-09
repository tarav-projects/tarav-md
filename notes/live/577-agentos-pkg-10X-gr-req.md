# agentos-pkg 10X gr-req

Date: 2026-07-08

## Gr.Abstract

- scope: `skills/agentos-pkg/design/10X-design.md` (`100`-`107`)
- baseline: `agentos index linter --depot skills/agentos-pkg --warn-unlinked --json`
- coverage before: `1202` `Index.Linter/Line.Unlinked` findings inside the chapter set (`1208` by the review's recount method)
- coverage after review sitting 2026-07-09: `1200` (same-method baseline `1208` — the 8 landed inline anchors account for the full delta)
- status: `landed` — no `proposed` entries remain; 2 `ambiguous` entries pending discovery
- report mode: survey only; no index or appendix files changed (review sitting 2026-07-09 applied the gated landings)
- dominant evidence session: `99144906-781e-43cc-9d27-b40f166e2acf` (`identity_hash` `9d194db7...`)

## Gr.Set

### 1. `Grounding.Hugentic.Authority`

- target: [105-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/105-design.md:81)
- proposed anchor: `@20260708-8`
- hint: user says chat/index anchors should always target user turns; approval-turn authority rule
- why: exact user-side authority for the user-turn-only grounding rule; stronger than assistant-side explanation and matches the approval-turn authority judgment
- landing form:
  - block-level `[GR]` in `appendix/Grounding.Hugentic.Authority-appendix.md`
  - optional inline anchors at `105-design.md:83-87`
- status: `landed`

### 2. `Anchory.System`

- target: [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:324)
- proposed anchor: `@20260706-1`
- hint: user says Anchory is an Agentos subsystem, not per-project, and connects with Chatlas
- why: exact user correction for subsystem scope and Chatlas coupling
- landing form:
  - block-level `[GR]` in `appendix/Anchory.System-appendix.md`
  - optional inline anchors at `107-design.md:326-333`
- status: `landed`

### 3. `Writing.Friction.Reduction`

- target: [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:173)
- proposed anchor: `@20260705-3`
- hint: user lays out the friction gradient: chat, agendix, appendix, index main
- why: exact user-side statement of the friction gradient and the "do not flush the index" floor
- landing form:
  - block-level `[GR]` in `appendix/Writing.Friction.Reduction-appendix.md` if we want the extra head evidence despite no meter movement
  - optional inline anchors at `107-design.md:175,177,178,179`
- status: `landed`

### 4. `Index.Agendix`

- target: [107-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md:183)
- proposed anchor: `@20260705-2`
- hint: user authority for agendix as the untouched-member / grounded-summary layer
- why: already-supported authority turn remains the strongest fit for the block's current core claim set
- landing form:
  - optional inline anchors if the user wants a meter-moving pass here
  - no additional mint required for the current proposal
- status: `landed`

### 5. `Grounding.Retrieval.Boundary`

- target: [105-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/105-design.md:59)
- searched:
  - 2026-07-05 grounding redesign neighborhood
  - session recovered through truth-tier queries, then narrowed with user-turn views
- missing: a crisp user turn narrower than the large redesign summary/replay neighborhood
- landing form: unresolved
- status: `ambiguous`

### 6. `Chat.Grounding.Target.Block`

- target: [105-design.md](/Users/pereiro/projects/agentos-project/agentos-md/skills/agentos-pkg/design/105-design.md:69)
- searched:
  - survivor-revisit thread
  - nearby authority turns around the block rewrite window
- missing: a tight user turn that supports the block without weak-link stretch
- landing form: unresolved
- status: `ambiguous`

## Gr.Log

- truth-tier note:
  - `--file-write 105-design.md` and `--file-write 107-design.md` did not yield usable hits for this pass
  - `--tool-contains ... --tool-name Bash` produced the useful session hits
- meter caveat:
  - `Kernel.Block.Grounding` already has a `Grounding.Head` line in its appendix, but the linter still reports lines `7-15` in `105-design.md` as unlinked
  - because of that, projected meter movement is based on the optional inline subset; block-level `[GR]` additions alone are currently projected to leave the chapter-set count at `1202`
- density caveat:
  - `Index.Agendix` likely has more support than one anchor can comfortably summarize; a later cleanup pass may want more than one landing
- unattached minted anchors: none in this pass
- commands used:
  - `agentos --help`
  - `agentos index linter --help`
  - `agentos index linter --depot skills/agentos-pkg --warn-unlinked --json`
  - `git log -L ...`
  - `agentos chatlas query --project-base agentos-project --file-write ...`
  - `agentos chatlas query --project-base agentos-project --tool-contains ... --tool-name Bash`
  - `agentos chatlas query --project-base agentos-project --message-contains ...`
  - `agentos chatlas views inline --identity-hash ... --contains ... --role user --around ... --radius 6 --filter turns --format json`
  - `agentos chatlas anchory register --identity-hash ... --at ... --hint ...`
- review sitting 2026-07-09 (batch-approved: "land all"):
  - entries 1-4 landed: 3 `[GR]` head lines (`Grounding.Hugentic.Authority`, `Anchory.System` — new `Grounding.Head` sections; `Writing.Friction.Reduction` — second head line) + 8 inline anchors (`105:86`; `107:175,177,178,179` @20260705-3; `107:187,191` @20260705-2; `107:329` @20260706-1)
  - entry 4 landed as inline-only: `@20260705-2` spread to the two block lines its turn verbatim supports (ontology-primes, `Block.Line.Gradient`) — no stretch onto the rest
  - close-out lint: `0 error(s), 0 warning(s)`, 17 checks — provenance bridge re-verified all four anchors landing on user turns
  - meter method note: the survey's `1202` baseline and this review's `1208` differ by counting filter; same-method before/after is `1208 → 1200`, exactly the 8 inline landings
  - entries 5-6 remain `ambiguous` — need a fresh `--gr-survey` discovery pass (or an approval-turn mint), not review time
