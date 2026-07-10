# agentos-index2 Parity Refactor — Impl.Req

## Impl.Abstract

- **Goal**: bring `agentos-md/skills/agentos-index2` to full feature and content parity with `agentos-index` (SKILL.md + all 11 reference modules), with every surface Skillware-managed and the module dependency graph restructured to declare the *real* span-level derivations — imports only where genuine content relations exist, inline mentions everywhere else.
- **Parity contract**: each compiled `agentos-index2` file equals its `agentos-index` original modulo the skill name (`agentos-index` → `agentos-index2` in titles/self-references). Acceptance is mechanical: `diff <(sed s/agentos-index2/agentos-index/g <compiled>) <original>` empty for every module; SKILL.md may additionally carry the POC banner block (documented delta).
- **Efficiency principle** (the restructure): a Skillware import is declared only for a real span-level relation — a section whose content is a transformation or duplication of another surface. One-line cross-references (`see references/type.md`, `Grounding.Hugentic.Authority applies`) are `Inline.Relatedness` mentions and stay plain prose. No forced imports, no library files that exist only to be imported.
- **Out of scope**: changing any module's operational content beyond the name adaptation; index (107/105) edits; skillware engine changes; removing the POC framing entirely (the SKILL.md banner shrinks to a provenance note but index2 remains non-canonical).
- **Repos**: `agentos-md` only.
- **Source**: goal `/agentos-hugentics-impl --dev --AUTO` (this session, 2026-07-10); prior art: `584-skillware-v1-impl-req.md` (the engine + initial POC).
- **Status**: designed; executing under `--dev --AUTO`

## Impl.Index

### Design.Decisions

- **all 12 surfaces become Skillware-managed** — `.skillware/src/SKILL.skw.md` + `references/{agendix,back-link,check,edit,enrich,gr-review,gr-survey,ground,link,search,type}.skw.md`. The 584 POC's hand-owned `references/gr-survey.md` demo case is retired (it served its purpose; uniformity wins), deleted before build so the compiled file replaces it.
- **the dependency graph** (from a full read of all 724 lines of agentos-index):
  - **root modules (recipe-free passthrough src)**: `search` (retrieval doctrine — canonical home of Search Model + Citation Behavior), `type` (vocabulary surface), `link` (linking pipeline + anchor discipline), `agendix`, `enrich`, `gr-survey`, `gr-review` (workflow modules; their overlaps with link/edit are one-line mentions, not spans)
  - **derived consumers** (recipe per section; derived body = the original's wording, so parity holds):
    - `ground.skw.md` — `#Grounding Levels` ← `Context.Grounding` (index block; the section restates its levels/read-only lines); `#Grounding Model` ← `references/search.skw.md#Search Model` + `Context.Grounding` (retrieval base adapted to grounding scope)
    - `check.skw.md` — `#Beyond The Linter` ← `references/type.skw.md#Semantic Lints` (the section is its summary; original text even points there)
    - `back-link.skw.md` — `#Back-Link Pipeline` ← `references/link.skw.md#Linking Pipeline` (the archaeology inversion: block→time→session→turn→anchor, minting through link's step 3)
    - `edit.skw.md` — `#Block Independence` ← `Independent.Reader.Block` (105; the section self-declares `Cited.Duplication` of that block — the flagship derived recipe)
    - `SKILL.skw.md` — `#Index Operating Behavior` ← `references/search.skw.md#Search Model` + `references/search.skw.md#Citation Behavior` (the operating list restates both, plus edit-gate lines)
  - no `copy` recipes: no verbatim span duplication exists between the real modules — the graph is honest, not decorative
- **name adaptation rule**: title lines and self-references `agentos-index` → `agentos-index2`; sibling references (`references/type.md` etc.) stay — they resolve inside index2; `agentos-pkg` and CLI references unchanged.
- **settings**: `.skillware/skillware.json` unchanged (`depots: ["../agentos-pkg"]`) — needed for the `Context.Grounding` and `Independent.Reader.Block` deps.
- **SKILL.md POC banner**: shrinks to a two-line provenance note (Skillware-built, agentos-index canonical); the rest reaches full parity including Skill.Arg.Section, Router Table, Boundary, module list.

### Current.State *(inspected)*

- `agentos-index` inventory: SKILL.md (191 lines) + 11 references (724 total) — all read this session; section map and overlaps identified above.
- `agentos-index2` current: SKILL.md (POC banner), src for `search` (trimmed) + `ground` (non-parity structure with an extra `#Citation Behavior` section the original lacks), hand `references/gr-survey.md` stub, lock present, all-ok check.
- `Independent.Reader.Block` block: `agentos-pkg/design/105-design.md:185`; `Context.Grounding`: `107-design.md:315`.
- Skillware engine: 584, all green; `agentos skillware build/check/status` installed.

## Execution.Plan

### S1 — root module srcs
- what: author full-parity passthrough srcs for `search`, `type`, `link`, `agendix`, `enrich`, `gr-survey`, `gr-review` (verbatim originals + name adaptation); delete the hand `references/gr-survey.md` stub
- check: after S4's build, the parity diff for these seven modules is empty
- status: pending

### S2 — derived consumer srcs
- what: author `ground`, `check`, `back-link`, `edit` srcs with the recipes listed in Design.Decisions; derived bodies carry the original wording; intents state the transformation
- check: recipes resolve (no findings); parity diff empty for the four modules
- status: pending

### S3 — SKILL src
- what: `SKILL.skw.md` — full parity content, provenance note, `#Index Operating Behavior` derived recipe
- check: compiled SKILL.md matches original modulo name + provenance note; recipe resolves
- status: pending

### S4 — build, check, parity verification
- what: `agentos skillware build` + `check` over index2; run the mechanical parity diff for all 12 surfaces; record results; update this note and the 584 note's POC framing
- check: check exit 0 (all ok); parity diffs empty (SKILL.md delta = provenance note only); status inventories 12 managed files
- status: pending

### Acceptance signals
- every agentos-index2 surface is compiled from src; `agentos skillware check` exits 0
- parity diffs clean across all 12 surfaces (documented SKILL.md delta only)
- the dependency graph declares exactly the five derived sections listed — nothing forced, nothing missed among real span relations

### Risks / deviation triggers
- if a derived body's original wording cannot be reproduced under a recipe without content change, prefer parity (exact original text) and note the weaker derivation in the intent
- if a region locator collides (duplicate heading titles within a source), scope by the first-match rule and record it
- if the `[!skw]` form appears in original content (none observed), escalate the escaping note in the builder reference

## Impl.Log

- (empty — execution follows in this --dev run)
