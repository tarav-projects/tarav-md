# Alias-Aware Resolution + Baseline Depends — Impl.Req

## Impl.Abstract

- close the two follow-ups from the 592 dependency-sync acceptance (`agentos-md/notes/live/592-dependency-sync-lint-impl-req.md`, Impl.Log 2026-07-16): the motivating drift — `Index.Main`, `Edit.Trigger.Gated`, `Content.Verbatim.Gated` still cited in `agentos-index` references — is invisible to the check because retired names do not resolve (the depot resolver ignores block-meta aliases) and no `depends` declarations exist yet
- deliverables: (a) alias-aware `Dotted.Name` resolution in the skillware depot resolver, (b) baseline `depends` declarations on the `agentos-index` skill, (c) resolution of the exposed drift POIs by updating the stale citations to current names, ending with a clean check
- scope: `agentos-py/src/agentos/skillware/build.py` + tests; `agentos-md/skills/agentos-pkg/design/107-design.md` (one meta data fix); `agentos-md/skills/agentos-index/.skillware/src/**` (declarations + drift fixes, then rebuild)
- out of scope: index-linter changes; alias support anywhere outside the skillware resolver; declaring or fixing skills other than `agentos-index`; the project-root `.claude/skills` copies (they regenerate from the same src)
- status: ready

## Impl.Index

### Current.State (inspected 2026-07-16)

- resolver: `_resolve_locator` (`build.py` ~150) resolves bare `Dotted.Name`s via `parse_depot` + `_depot_block_body` (~196), which matches **heading paths only** and collects `KernelLine` nodes until the next `BlockHeading`
- the index model already parses meta: `parse_depot` yields `MetaHeading` / `MetaLine` nodes inside a block (verified on `Index.Ontology` in `107-design.md`); alias lines look like `- aliases: \`Index.Main\`, \`Index.Fundamentals\`` with backticked names
- data bug found during design: the `Index.Ontology` block meta (`107-design.md` ~284) lists `aliases: \`Index.Ontology\`, \`Index.Fundamentals\`` — the first entry should be the retired `Index.Main` (the approved design kept `Index.Main` and `Index.Fundamentals` as aliases; see session artifact `591-touched-surface-index-design-session.md`). Without this fix alias resolution still misses the motivating drift
- `104-design.md` metas are correct: `Verbatim.User.Gated` ← alias `Content.Verbatim.Gated`; `Edition.Trigger.User.Gated` ← alias `Edit.Trigger.Gated`
- current acceptance state: `agentos skillware check --skill agentos-md/skills/agentos-index` → 77 `undeclared-dependency` POIs, 41 distinct names, 13 files; zero declarations, zero blessings
- drift sites: `SKILL.md` (1× `Index.Main`), `references/edit.md` (2× `Index.Main`, 1× `Edit.Trigger.Gated`, 1× `Content.Verbatim.Gated`) — edit the `.skillware/src/**.skw.md` sources, never the compiled targets
- dependency-sync internals (from 592): declared set = `depends` froms + recipe froms; mention set = backticked dotted names in `expansion.fresh_lines` that resolve; POI identity `(file, name, resolution-hash)`; bulk bless `bless --kind <poi-kind> --all`
- read `agentos-py/AGENTS.md` and `agentos-md/AGENTS.md` before editing

### Design.Decisions (resolved in AUTO mode — recorded, not hidden)

- **alias resolution layer** — per-depot name index built once and cached alongside the parsed model: map canonical heading path → block body, then add each block's meta aliases pointing at the same body. Canonical names always win; an alias that collides with a canonical name or an earlier alias is skipped (deterministic depot iteration order). Aliases resolve everywhere bare `Dotted.Name`s resolve (mentions, `depends` froms, `copy`/`derived` froms)
- **no canonicalization in the sync** — this is the crux: mentions and declarations compare by **literal name**. An alias mention (e.g. `Index.Main`) now *resolves*, so it surfaces as an `undeclared-dependency` POI under its literal name — that POI *is* the retired-name drift signal. Mapping alias mentions onto their canonical declaration would silently swallow exactly the drift this feature exists to catch
- **alias POI identity** — resolution hash of an alias mention is the canonical block's body hash; identity stays `(file, literal-name, body-hash)`, so a blessed alias mention re-mints when the target block changes, same as canonical
- **baseline declaration rule** — per src file, declare the **canonical names** of all its resolving mentions (alias-resolved mentions map to their canonical name for the *declaration*, per the normative-intent reading: the surface MUST depend on the concept, under its current name). Grouped in one `$kw: depends` stanza near the top of each src file. Consequence: files citing retired names show both `undeclared-dependency` (literal alias mention) and `unhonored-dependency` (canonical declared, not mentioned) until the text is fixed — that pairing is the intended detection signature
- **drift resolution = content fix, not bless** — update the five stale citations in src to the current names (`Index.Main` → `Index.Ontology`; `Edit.Trigger.Gated` → `Edition.Trigger.User.Gated`; `Content.Verbatim.Gated` → `Verbatim.User.Gated`), rebuild, re-check. No blessing of drift POIs
- **meta data fix** — `107-design.md` `Index.Ontology` meta first alias `\`Index.Ontology\`` → `\`Index.Main\``. This corrects the landed batch to the user-approved design (aliases `Index.Main`, `Index.Fundamentals`); it is a meta line, not a kernel line — no anchor or gate implications
- **v1 boundary kept** — names that resolve in no configured depot (e.g. chatlas-pkg blocks if that depot is not configured for `agentos-index`) stay invisible; unchanged from 592

## Execution.Plan

Run `python -m pytest agentos-py/tests/test_skillware.py` per slice (RED→GREEN where marked). Create pre-edit checkpoints per the execution workflow before touching either repo.

### Slice 1 — alias-aware depot resolution (`agentos-py`)
- build the per-depot name index (canonical + meta aliases) and route `_depot_block_body` / the bare-`Dotted.Name` branch of `_resolve_locator` through it; import the meta node types from the index model
- RED: fixture depot with a block carrying `### meta` aliases — alias resolves to the canonical body; canonical still resolves; an alias colliding with a canonical name resolves to the canonical block
- GREEN: implement; existing 60 tests stay green

### Slice 2 — alias mentions in the sync (`agentos-py`)
- RED: fixture where compiled text mentions a block by alias with no declaration → `undeclared-dependency` POI under the **literal alias name**; declaring the canonical name does not cover the alias mention (POI persists) and additionally yields `unhonored-dependency` for the canonical name when unmentioned
- GREEN: expected to pass mostly from slice 1 (no canonicalization is the absence of code); adjust only if the resolution-hash path needs it
- check: POI hashes stable across runs; blessing an alias POI suppresses it; editing the target block re-mints

### Slice 3 — meta data fix (`agentos-md`)
- `107-design.md` `Index.Ontology` meta: first alias `\`Index.Ontology\`` → `\`Index.Main\``
- check: `agentos index linter` clean on agentos-pkg; `Index.Main` now resolves via the skillware resolver

### Slice 4 — baseline `depends` on `agentos-index` (`agentos-md`)
- for each of the 13 src files: run check, take its resolving mentions, canonicalize alias hits, write one `$kw: depends --from <name> ...` stanza near the top of the src file; rebuild the skill
- expected observable after this slice: the only remaining POIs are the drift signature — `undeclared-dependency` for literal `Index.Main` / `Edit.Trigger.Gated` / `Content.Verbatim.Gated` mentions plus matching `unhonored-dependency` for their canonical names where unmentioned
- check: no other POI kinds appear; report the exact POI list before slice 5

### Slice 5 — resolve the drift (`agentos-md`)
- fix the five stale citations in src (mapping in Design.Decisions), rebuild, re-check
- acceptance: `agentos skillware check --skill agentos-md/skills/agentos-index` → **0 POIs**; introducing a scratch undeclared mention → exactly 1 new POI (then revert the scratch)

### Risks / deviation triggers
- meta node type names differ from `MetaHeading`/`MetaLine` in imports → inspect `agentos.index.model` exports; adapt, log
- alias lists elsewhere in the depots may collide → the canonical-wins/skip rule covers it; log any collision encountered
- some of the 41 mentioned names may be incidental (mentioned once in passing, not real dependencies) → still declare them in the baseline; pruning declarations is future curation, not this task; log any that feel wrong
- `depends` stanza placement may collide with front-matter or copy regions in a src file → place after front-matter, outside any construct body; log deviations

### Acceptance signals
- full suite green including new alias tests
- slice 4 exposes exactly the retired-name drift signature and nothing else new
- slice 5 ends at 0 POIs without any blessing, and the scratch-mention probe re-flags

## Impl.Log

- (empty — execution not started)
