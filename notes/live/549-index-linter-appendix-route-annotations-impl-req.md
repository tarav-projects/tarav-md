# Index Linter Appendix Route Annotations - impl-req

## Impl.Abstract

- **scope:** extend `agentos index linter` with deterministic appendix route annotation checks
- **status:** implemented
- **source:** current linter design discussion on adding the next useful check after first-class `Index.Linter/Block.*` codes
- **target codebase:** `agentos-py`
- **target docs/index surface:** `agentos-md/skills/agentos-pkg`
- **primary command:** `agentos index linter --index <index-path> --appendix <appendix-path>`
- **current baseline:** the agentos-pkg index/appendix surface lints cleanly with 14 passed checks and no findings

## Impl.Index

### Appendix.Route.Annotation.Contract

- appendix discovery is implicit by filename, but router annotations make appendix depth visible at the always-loaded entry point
- when an appendix file exists for a routed concept, the router entry should expose that depth using the existing `[+N]` route notation
- page count is determined from appendix files:
    - `Concept.Name-appendix.md` is page 1
    - `Concept.Name-appendix-2.md` is page 2
    - `Concept.Name-appendix-3.md` is page 3, etc.
- the intended route display is `Concept.Name[+N]`, where `N` is the highest contiguous appendix page count available for that concept
- annotation checks should be warnings, not errors, because missing annotations reduce discoverability but do not make the index unparsable

****

### Router.Parser.Preservation

- the current router parser normalizes routed concepts before comparing to concept blocks
- the implementation must parse optional appendix annotations without breaking existing concept matching
- `Concept.Name[+1]` should normalize to `Concept.Name`
- `Concept.Name[+2]` should normalize to `Concept.Name`
- existing router forms without annotations must continue to work
- chained colon parameter concepts such as `Alignment.Backend:InChat:What[+1]` must remain valid

****

### Finding.Code.Surface

- new finding codes should use the established single-code system under `Index.Linter/...`
- add appendix documentation blocks in `skills/agentos-pkg/appendix/Index.Linter-appendix.md`
- proposed codes:
    - `Index.Linter/Appendix.RouteAnnotationMissing`
    - `Index.Linter/Appendix.RouteAnnotationStale`
    - `Index.Linter/Appendix.PageGap`
- use `Appendix.PageGap` when page files are non-contiguous, such as page 1 and page 3 with no page 2
- use `RouteAnnotationMissing` when an appendix exists but the router entry has no `[+N]`
- use `RouteAnnotationStale` when the router annotation exists but does not match discovered appendix page count

****

### State.Model.Extension

- extend linter state enough to compare router entries with appendix page inventory
- appendix filename parsing already exists for valid appendix names; reuse it rather than reparsing ad hoc
- router entries should retain both normalized concept and the raw displayed token or parsed annotation count
- both human and JSON output must continue to derive from the same linter state object
- blocked checks should remain explicit: if concept inventory, router inventory, or appendix filename inventory is unavailable, annotation checks should be blocked rather than noisy

## Execution.Plan

### Slice 1 - Parse appendix annotations without changing behavior

- update router entry parsing so each route concept captures:
    - normalized concept name
    - optional appendix annotation count from `[+N]`
    - route file, router path, and line
- path: router file text -> `_check_router_entries` -> `state.router_entries`
- observable: existing linter tests still pass, including router target checks
- check: add focused tests for `Concept.Name[+1]` normalization and current router behavior
- status: completed

### Slice 2 - Build appendix page inventory

- extend appendix filename processing to record discovered appendix page numbers per concept
- path: appendix file discovery -> filename regex -> state appendix inventory
- observable: page 1 and later page files can be counted per concept
- check: unit test with `Example.Concept-appendix.md` and `Example.Concept-appendix-2.md` records count 2
- status: completed

### Slice 3 - Add deterministic annotation checks

- add a new gated check after router entries and appendix filenames are available
- emit `Appendix.RouteAnnotationMissing` when a routed concept has appendix pages but no annotation
- emit `Appendix.RouteAnnotationStale` when routed annotation count differs from discovered page count
- emit `Appendix.PageGap` when appendix pages are non-contiguous
- path: linter state -> new check -> findings -> text/JSON output
- observable: linter surfaces route annotation problems as warnings with specific `Index.Linter/...` codes
- check: add tests for missing annotation, stale annotation, and page gap
- status: completed

### Slice 4 - Update agentos-pkg code documentation

- document new check and finding codes in `Index.Linter-appendix.md`
- add any needed route annotation wording to the `Index.Linter` block if the command surface needs discoverable help
- keep docs concise and agent-actionable
- observable: each new code resolves through `agentos-pkg` appendix discovery
- check: run the linter against `agentos-pkg` and ensure documentation changes do not introduce new findings
- status: completed

### Slice 5 - Verify installed command surface

- run focused tests and full `agentos-py` tests
- run `ruff` on touched linter/test files
- run the linter against `agentos-pkg`
- reinstall the editable `agentos` CLI wrapper if command code changed
- observable: installed `agentos index linter` reports the expected clean or intentionally updated baseline
- check:
    - `uv run pytest tests/test_index_linter.py`
    - `uv run pytest`
    - `uv run ruff check src/agentos/index/linter.py tests/test_index_linter.py`
    - `agentos index linter --index agentos-md/skills/agentos-pkg/index --appendix agentos-md/skills/agentos-pkg/appendix`
- status: completed

## Impl.Log

- 2026-05-23: Impl.Req created from the linter design discussion. The agreed next slice is appendix route annotation linting, because it is deterministic, index-specific, and improves agent discovery from the router.
- 2026-05-23: Implemented router appendix annotation parsing, appendix page inventory, and the gated `Index.Linter/Check.AppendixRouteAnnotations` check. Added warning findings for missing annotations, stale annotations, and non-contiguous appendix pages. Updated `agentos-pkg` route annotations and linter appendix code documentation. Verified with focused linter tests, full `agentos-py` tests, ruff, editable CLI reinstall, and installed `agentos index linter` against `agentos-pkg`.
