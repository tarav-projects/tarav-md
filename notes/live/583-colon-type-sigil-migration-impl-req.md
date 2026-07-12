# Colon Type-Sigil Migration - impl-req

## Impl.Abstract

- **scope:** migrate single-colon type statements (`Concept.Name:Param`) to the `::` form (`Concept.Name::Param`) across markdown surfaces, code docstrings, and the index linter, per `Naming.Sigil.Vocabulary` (`design/108-design.md`)
- **status:** complete
- **source:** `Block.Naming.Schema` design session (`notes/live/582-block-naming-schema-design-session.md`), landed to the index 2026-07-12 with anchors `^20260712-0`…`-6`; this migration was recorded there as the landing-phase follow-up
- **out of scope:** the `:` line-position form itself (already defined in the index, nothing to migrate); `path.py::symbol` pytest-style code references (coexisting convention, see `Impl.Index`); `_DEPRECATED/` trees; re-syncing imported skill copies in other projects (follow-up)

## Impl.Index

### Colon.Migration.Pattern

- the rewrite is `([A-Z][A-Za-z0-9]*(\.[A-Z][A-Za-z0-9]*)+):(?=[A-Z])` → `\1::` applied globally, so chained parameters migrate whole: `Alignment.Backend:Artifact:What` → `Alignment.Backend::Artifact::What`
- the capital-after-colon lookahead is the discriminator: it excludes `path:line` references (digit follows), prose colons (space follows), scoped skill names (`agentos-md:agentos-pkg`, lowercase follows), URLs, and timestamps
- survey evidence (2026-07-12): 533 hits across 99 `*.md` files in `agentos-md` + `agentos-chatlas-md` (canvas/iterante scanned, negligible); top names: `Alignment.Backend:Artifact` (35), `Alignment.Backend:InChat` (32), `Alignment.Loop:What` (21), `Alignment.Mode:Autonomous` (17)
- code side: 5 hits, all Python docstrings (`agentos-py/src/agentos/agent/auth_method.py:3`, four `Normalization.Pipeline:Chatlas.Session.Model` docstrings under `agentos-chatlas-py/src/agentos_chatlas/normalization/`) — no runtime semantics, safe to rewrite
- zero numeric false positives under the discriminator regex (verified by survey grep)

### Colon.Migration.Scope.Rule

- rule over list: every `*.md` file under `agentos-md/`, `agentos-chatlas-md/`, `agentos-canvas-md/`, `agentos-iterante-md/` matching the pattern is in scope, plus the 5 Python docstring hits
- exclusions: `_DEPRECATED/` trees; this artifact; the migration-describing note in `notes/live/582-block-naming-schema-design-session.md` (its `Session.Notes` line documents the pre-migration state by design — rewriting it would corrupt the record); acceptance greps carry these exclusions
- skillware-managed skills (`agentos-md/skills/agentos-index2`, `agentos-md/skills/agentos-skillware`) migrate at their `.skillware/src/*.skw.md` sources, then rebuild with `agentos skillware build --skill <path>` and verify with `agentos skillware check --skill <path>` (canonical workflow: `agentos-skillware/references/author.md`, `references/build.md`) — never hand-edit the compiled SKILL.md
- `.claude/skills/` entries are symlinks into source trees in this workspace — no second copy
- index blocks are `Content.Verbatim.Gated`; the user's approval of this Impl.Req gates the mechanical rewrite — no textual change beyond the pattern

### Coexisting.DoubleColon.Convention

- `::` already appears on md surfaces as pytest-style code references: `src/agentos/agent/monitor/models.py::MonitorAccountRow`
- no collision: the left side of a code reference is a lowercase path; the left side of a type statement is a capitalized `Dotted.Name` — the migration regex and the linter check both key on the capitalized form
- accepted coexistence, recorded here so a later reader does not "fix" one into the other

### Legacy.Colon.Linter.Check

- add `Index.Linter/TypeStatement.LegacySigil` to the `CHECKS` registry in `agentos-py/src/agentos/index/linter.py` (19 checks post-580), following the `Anchor.LegacySigil` pattern (`linter.py:1262` area) with one deliberate divergence: surface coverage
- surface coverage MUST include routers: `_check_legacy_anchor_sigil` filters to `{"chapter", "appendix", "agendix"}` (`linter.py:1386`), which is correct for anchors (never legal in routers) but wrong here — routers carry type statements (18 legacy hits across the two `000-INDEX.md` routers today, e.g. `Normalization.Pipeline:Chatlas.Session.Model` in the chatlas router); without router coverage the linter goes green while routers stay unguarded
- finding pattern: `[A-Z][A-Za-z0-9]*(\.[A-Z][A-Za-z0-9]*)+:(?=[A-Z])` — a single-colon type statement is a legacy sigil with a fix hint pointing to `::`
- the check must not flag `::` (require the match's colon is not part of `::`) nor `path:line` (the capital lookahead already excludes)

## Execution.Plan

### Slice 1 - Legacy-sigil linter check (RED then GREEN)

- add a RED test to `agentos-py/tests/test_index_linter.py`: a fixture line carrying `Alignment.Mode:Autonomous` produces the finding; `Alignment.Mode::Autonomous` and `parser.py:41` produce none; a router fixture (`000-INDEX.md`) carrying a legacy type statement also produces the finding — the router-coverage divergence must be RED-tested, not assumed
- implement `Index.Linter/TypeStatement.LegacySigil` per `Legacy.Colon.Linter.Check`, including router surfaces
- observable: `agentos index linter --depot agentos-md/skills/agentos-pkg` reports legacy findings across the pre-migration depot
- check: new test GREEN; existing linter tests pass; record the pre-migration finding count as the Slice 3 baseline
- status: complete (2026-07-12)

### Slice 2 - Skillware source migration and rebuild

- apply the rewrite to `.skillware/src/*.skw.md` in `agentos-index2` and `agentos-skillware`, then run `agentos skillware build --skill <path>` for each
- observable: compiled SKILL.md files carry `::` forms
- check: `agentos skillware check --skill <path>` exits zero (no drift) for both skills; compiled and source hit counts match
- status: complete (2026-07-12)

### Slice 3 - Markdown and docstring sweep

- script the `Colon.Migration.Pattern` rewrite across `Colon.Migration.Scope.Rule` targets (excluding skillware-derived files already rebuilt in Slice 2); include the 5 Python docstrings
- verify: the survey grep, minus exclusions, returns zero; the `::` count gained ≈533
- observable: `agentos index linter --depot agentos-md/skills/agentos-pkg` reports zero `TypeStatement.LegacySigil` findings and no grounding regressions
- check: linter clean (20 checks); `agentos-py` and `agentos-chatlas-py` test suites still pass (docstring-only code changes)
- status: complete (2026-07-12)

### Slice 4 - Convention-teaching surfaces

- sweep prose that teaches the single-colon form (not just uses it): `agentos-batchy-skills` references, `agentos-pkg/design/101-design.md` Batchy blocks, `hugentics` skill references describing `Alignment.Backend:*` — the pattern rewrite covers the tokens; this slice spot-reads that surrounding prose still reads correctly (e.g. "colon parameters" phrasing → "`::` type statements")
- observable: `grep -rn 'colon parameter' agentos-md --include='*.md' | grep -v _DEPRECATED | grep -v 58[23]` returns nothing needing rewording
- check: spot-read of the five files with the highest hit counts (survey table) confirms prose coherence
- status: complete (2026-07-12)

## Impl.Log

- 2026-07-12 review pass (two confirmed findings): Slice 2 toolchain corrected from `agentos-skill-pkg-builder` to the canonical `agentos skillware build`/`check` commands; `Legacy.Colon.Linter.Check` now mandates router surface coverage as a recorded divergence from the `Anchor.LegacySigil` pattern, with a router fixture added to the Slice 1 RED test — 18 legacy router hits exist today and would otherwise be linter-invisible
- Autonomous-mode design decisions (recorded, not prompted): 582 session note excluded from rewrite (documents pre-migration state); historical `notes/live/` otherwise in scope per the 580 precedent (grep-consistency surfaces, not protected history); `path.py::symbol` coexistence accepted rather than renamed; linter check named `TypeStatement.LegacySigil` mirroring `Anchor.LegacySigil`
- 2026-07-12 execution deviation: the workflow's mandatory git checkpoint could not be created because the target repo already had a dirty worktree and project instructions prohibit commits without an explicit user commit request; proceeded uncommitted and preserved all pre-existing edits
- 2026-07-12 execution deviation: the planned one-colon rewrite regex was too narrow to rewrite chained tokens whose later parameters are undotted (`Alignment.Backend:Artifact:What` would stall after the first replacement). Implemented the mechanical sweep with the broader full-token pattern the linter now uses, replacing every type-statement colon in one pass
- 2026-07-12 execution deviation: verification exposed a hidden dependency outside the original plan — the index parser/linter grammar still treated single-colon type statements as the only valid block/router/appendix syntax. Resolved by broadening the shared concept-reference grammar to accept both `:` and `::` during the migration window, adding GREEN tests for `::` headings/router+appendix forms, and renaming `appendix/Alignment.Loop:What-appendix.md` to `appendix/Alignment.Loop::What-appendix.md`
- 2026-07-12 results: Slice 1 landed `Index.Linter/TypeStatement.LegacySigil` with router coverage and RED/GREEN tests; the pre-migration baseline on `agentos-md/skills/agentos-pkg` was 107 legacy findings. Slice 2 rebuilt `agentos-index2` and `agentos-skillware` cleanly through `agentos skillware build/check`. Slices 3-4 completed the markdown/docstring sweep, cleared the acceptance greps, and updated lingering convention-teaching prose in historical notes
- 2026-07-12 verification: `uv run pytest tests/test_index_linter.py` (34 passed) in `agentos-py`; `agentos skillware check --skill agentos-md/skills/agentos-index2` clean; `agentos skillware check --skill agentos-md/skills/agentos-skillware` clean; `agentos index linter --depot agentos-md/skills/agentos-pkg --json` clean (20 checks, 0 findings); `uv run pytest` in `agentos-py` (338 passed); `uv run pytest` in `agentos-chatlas-py` (151 passed)
