# Index Linter — New Index Model Update — Impl.Req

## Impl.Abstract

- **Goal**: update `agentos index linter` to the new index model (540 / 561): `000-INDEX.md` router at the depot root, `Index.Chapter` folders with `NNN-<chapter>.md` files, `Block.Path` headings.
- **Scope**: basics first — structural port of the existing 14 checks to the new layout, plus a `--depot` invocation mode and the chapter-suffix filename rule. New-model semantic checks (`namespace-members` resolution, `./Child` legality, meta alias parsing) are a later iteration.
- **Repos**: code in `agentos-py` (`src/agentos/index/linter.py`, `src/agentos/index/commands.py`, `tests/test_index_linter.py`). The `agentos` executable is owned by `agentos-cli`; CLI-flag additions require `uv tool install --reinstall --editable .` from `agentos-cli/` (per `agentos-py/AGENTS.md`).
- **Compat**: no legacy recognition — old router names `000-index.md`/`001-index.md` are a plain **ERROR** (user decision; matches the repo Compatibility Policy).
- **Source**: `notes/live/540-index-architecture-redesign-design-session.md` (the model), `561-index-arch-migration-impl-req.md` (the deployed layout), live reference depots: `agentos-md/skills/agentos-pkg/`, `agentos-chatlas-md/skills/agentos-chatlas-pkg/`.
- **Status**: implemented (2026-07-05)

## Impl.Index

### Target.Model
- an `Index.Depot` is marked by `000-INDEX.md` at its root (`Index.Discovery`); chapters are folders of `NNN-<chapter>.md` files (`design/100-design.md`); one shared `appendix/` of `Concept.Name-appendix.md` pages
- router entries route `- \`<chapter>/<NNN-<chapter>.md>\` — Concept, ...` — route files are depot-root-relative (today they resolve relative to the router's parent, `linter.py:898`, which coincides once the router sits at the root)
- block headings are `Block.Path`s: a root `Dotted.Name` plus zero or more `/` segments, each a `Dotted.Name` or a free label (`Appendix`, `Grounding`, `Flat.File.Design`)

### Current.Hardcodes *(inspected, cited)*
- `linter.py:29` `INDEX_FILENAME_RE` — `NNN-index.md` only
- `linter.py:614` router detection — `{000-index.md, 001-index.md}` inside the `--index` dir
- `linter.py:582` unanchored-section exemption — same two router names
- `linter.py:25` `CONCEPT_NAME_RE` — max one `/`, all segments full dotted concepts
- `commands.py:50-61` — only `--index`/`--appendix` append flags; epilog examples use old paths

### Invocation.Design
- new `--depot <root>` flag (repeatable): auto-derives router (`<root>/000-INDEX.md`), index surfaces (every direct subfolder containing `NNN-<that-folder>.md` files), appendix (`<root>/appendix/` if present)
- `--index`/`--appendix` stay as explicit-surface flags (advanced/partial linting); `--depot` and explicit flags may combine
- router presence for a depot: exactly `000-INDEX.md` at the root — missing → `Router.Missing` (error); a `000-index.md`/`001-index.md` found anywhere in the depot → error finding (new code `Index.Linter/Router.LegacyName`)

### Filename.Rules
- chapter files: `NNN-<chapter>.md` where `<chapter>` == the containing folder name; three-digit `NNN`; violation → `Index.InvalidFilename` (warning, as today)
- with bare `--index <dir>`: the expected suffix is the dir's own name (same rule, no special case)
- appendix rules unchanged (`Concept.Name-appendix.md`, `-appendix-N.md` pages)

### Heading.Rules
- `CONCEPT_NAME_RE` → `BLOCK_PATH_RE`: `Root.Dotted(:param)*(/Segment)*` where `Segment` is a dotted concept ref or a free label (`[A-Z][A-Za-z0-9]*` single word allowed)
- the appendix-orphan check stays file-level (filename concept must exist as an index concept) — unchanged semantics
- router-entry concepts use the same relaxed pattern

### Test.Model
- `tests/test_index_linter.py` (454 lines) builds fixture trees — port fixtures to the new layout; `RED.GREEN.Test.Suite` drives each slice
- live acceptance target: `agentos index linter --depot skills/agentos-pkg` run from `agentos-md` must come out clean (the depot was hand-validated in 561 S3); same for `--depot skills/agentos-chatlas-pkg` from `agentos-chatlas-md`

### Scope.Boundary
- **in**: the 14 existing checks on the new layout; `--depot`; legacy-router ERROR; `Block.Path` heading pattern; chapter-suffix rule; CLI help/epilog text; test-suite port; `agentos-py/AGENTS.md` refresh (required by that repo's policy)
- **out (later iteration)**: `namespace-members` inventory validation; `./Child` resolution; meta alias parsing; local depot `notes/` shape (pending its own migration); multi-depot composition checks (`Index.Discovery` collision surfacing)

## Execution.Plan

### S1 — Heading + filename rules (pure regex, test-first)
- what changes: `BLOCK_PATH_RE` replaces `CONCEPT_NAME_RE` usage; `INDEX_FILENAME_RE` → chapter-aware check (folder-name suffix)
- RED: tests for `Agentos.Index.System/Appendix`, `Block.Path/Concept.Scoping`, multi-segment paths, free labels, `design/100-design.md` valid / `design/100-index.md` invalid
- GREEN: regexes + `_check_index_filenames` folder-suffix logic
- check: new tests pass; old-pattern tests updated, suite green

### S2 — Router at depot root + legacy ERROR
- what changes: `_check_router_presence` looks for `000-INDEX.md`; new `Router.LegacyName` error finding for `000-index.md`/`001-index.md`; unanchored-section exemption updated to `000-INDEX.md`
- RED: fixture with root `000-INDEX.md` passes presence; fixture with old names errors
- check: suite green; codes documented in the findings list

### S3 — `--depot` mode
- what changes: `commands.py` gains `--depot` (repeatable); a resolver derives router/index/appendix surfaces from the depot root; epilog examples updated to new paths
- RED: CLI-level test invoking the linter on a new-layout fixture depot via `--depot`
- check: `agentos index linter --depot <fixture>` clean on a valid fixture; erroring fixtures produce the expected codes
- note: reinstall `agentos-cli` editable to refresh the executable if verifying via installed `agentos`

### S4 — Live acceptance + docs
- what changes: nothing in code (fix stragglers only)
- check: `--depot skills/agentos-pkg` (agentos-md) and `--depot skills/agentos-chatlas-pkg` (chatlas-md) — expect clean or only justified findings; update `agentos-py/AGENTS.md` CLI-surface notes; update `Index.Linter` concept/appendix in the agentos-md index (**content-gated — propose to user, do not self-write**)
- closes: the TOOLING DEBT note in 540 Session.Notes and the deferred item in 561 Scope.Boundary

### Acceptance signals
- both migrated depots lint clean via `--depot`
- old router names produce `Router.LegacyName` ERROR
- full `agentos-py` test suite green; no regression-test slop (`No.Regression.Tests.Allowed`)

### Risks / deviation triggers
- fixture-port breadth: 454 test lines assume old names — if the port balloons, split the test refresh into its own slice, do not weaken assertions
- `[+N]` annotation semantics unchanged (counts appendix *pages*) — do not reinterpret
- if `--depot` surface derivation meets an ambiguous folder (non-chapter markdown dirs at depot root, e.g. `references/`, `testing/`), chapters are only folders whose files match `NNN-<folder>.md`; others are ignored, never linted implicitly

## Impl.Log

- 2026-07-05: Executed in `Alignment.Mode::Autonomous` through `hugentics-impl-executer`.
- 2026-07-05: Open-space decision: explicit `--index` directory linting keeps working under the new chapter rule by validating `NNN-<directory>.md` against the containing folder name, while `000-INDEX.md` is treated as the depot router rather than a chapter file.
- 2026-07-05: Open-space decision: router discovery now derives depot roots from configured surfaces (`--depot`, chapter dirs/files, appendix dirs/files, or `000-INDEX.md`) so the same router/annotation checks apply consistently across explicit-surface and depot modes.
