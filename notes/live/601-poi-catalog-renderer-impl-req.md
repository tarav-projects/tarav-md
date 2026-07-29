# POI Catalog And Renderer - Impl.Req

## Impl.Abstract

- **Goal:** implement the first shared `POI.System` runtime cut by adapting Index linter findings into deterministic `POI.Instance`s, resolving their registered `POI.Class` references through Wayfinder, grouping output by class, and exposing `agentos poi explain`.
- **Status:** implemented and verified.
- **Source design:** the POI blocks in `skills/agentos-pkg/design/107-design.md`, Wayfinder in `skills/agentos-pkg/design/110-design.md`, and the execution authorization at `^c20260729-47u`.
- **In scope:** common POI models/catalog/rendering, Index finding adaptation, complete core and injected-Chatlas class registration, grouped text/JSON output, package-owned documentation resolution, explain CLI, tests, and architecture guidance.
- **Out of scope:** blessing, dispositions, context gates, authoring missing POI documentation blocks, changing check execution/state dependencies, and converting Skillware or other linters.

## Impl.Index

### Common POI Boundary

- `agentos.poi` is an importable foundation package with no dependency on Chatlas or the umbrella CLI.
- A `POI.Instance` carries a deterministic instance ID, canonical class reference, target location, severity, current situation, and concrete evidence.
- Instance identity hashes canonical class identity plus occurrence data, so repeated checks produce the same ID while the occurrence remains materially unchanged.
- A `POI.Catalog` maps producer finding codes to canonical `Wayfinder.Reference.Type::Index.Block` class identities.
- Duplicate finding-code registrations are rejected; catalogs compose explicitly at application boundaries.

### Class Ownership And Resolution

- Core Index finding codes resolve to class references rooted at `agentos-pkg`.
- Chatlas-powered Index finding codes resolve to class references rooted at `agentos-chatlas-pkg` and are injected by `agentos-cli`.
- The class block path matches the emitted finding code.
- Existing class blocks are resolved and rendered from their authoritative Index content.
- Missing or ambiguous class blocks remain registered identities and produce visible Wayfinder resolution POIs without suppressing their original instances.
- This implementation does not manufacture fallback class semantics or write gated Index blocks without their review workflow.

### Index Adapter

- The Index linter retains `LinterFinding` as its check-internal compatibility model for this cut.
- A single adapter at the reporting boundary converts every scoped finding into a `POI.Instance`.
- Every core finding code that checks can emit is registered and covered by a catalog-completeness test.
- Externally injected checks provide matching class registrations through the same command composition socket.
- Unknown emitted finding codes fail clearly at the adapter boundary rather than silently creating undocumented classes.

### Renderer

- The shared renderer groups instances by canonical class reference in first-seen order.
- Each group resolves its class once, prints the class identity and short description once, then prints compact instance rows.
- A resolved class description is derived from the authoritative class block rather than copied into instances.
- Each instance row retains severity, target, stable identity, and current situation.
- Structured output exposes grouped classes and a flat POI instance list; legacy `findings` output is not retained as a second public representation.
- Blocked checks, coverage, summaries, and linter exit policy remain unchanged.

### POI Explain

- `agentos poi explain <class>` accepts a registered finding code, `index://` sugar, or canonical Wayfinder reference JSON.
- Registered codes are resolved through the composed catalog; direct references use normal Wayfinder parsing.
- Successful text output presents the canonical class reference, verified source coordinates, and authoritative block content.
- `--json` returns the structured resolution.
- Resolution failure presents the `Wayfinder.Resolution.POI` and exits nonzero.

### CLI Composition

- `agentos-py` owns the POI command registrar and the core Index catalog.
- `agentos-chatlas-py` owns registrations for its injected Index findings.
- `agentos-cli` composes the catalogs, passes the result to the Index renderer, and registers the top-level `poi` command.
- Dependency direction remains foundation outward: `agentos-py` does not import Chatlas.

## Execution.Plan

### Slice 1 - Common POI model and catalog

- Add deterministic model serialization, class-reference sugar, catalog registration/composition, and focused tests.
- RED: prove stable instance identity, duplicate rejection, lookup, composition, and unknown-code failure.
- GREEN: implement the minimum importable `agentos.poi` model and catalog.
- Check: `uv run pytest tests/test_poi.py -q`.

### Slice 2 - Shared renderer and explain

- Add one-resolution-per-class grouping, authoritative description extraction, unresolved-class preservation, and command handling.
- RED: cover grouped text/JSON, compact repeated instances, successful explain, and resolution POI failure.
- GREEN: implement renderer and thin command registrar over Wayfinder.
- Check: `uv run pytest tests/test_poi.py tests/test_wayfinder.py -q`.

### Slice 3 - Index adaptation

- Declare the complete core finding catalog and add the reporting-boundary adapter.
- Replace public Index linter finding rendering with grouped POI rendering while retaining check internals.
- RED: require deterministic instance IDs, class grouping, new JSON shape, and complete registration for emitted core codes.
- GREEN: adapt scoped findings once and preserve summaries, blocked checks, coverage, and exit behavior.
- Check: `uv run pytest tests/test_index_linter.py -q`.

### Slice 4 - Chatlas ownership and CLI composition

- Add Chatlas-owned registrations for every Chatlas Index finding code.
- Inject the composed catalog into Index and `agentos poi`.
- RED: umbrella tests require Chatlas class identity, top-level command discovery, successful core explain, and visible unresolved Chatlas documentation.
- GREEN: keep the umbrella package as the only cross-package composition point.
- Check: focused suites in `agentos-chatlas-py` and `agentos-cli`.

### Slice 5 - Runtime and completion audit

- Refresh the editable CLI and exercise a real Index linter run plus `agentos poi explain`.
- Run relevant complete suites, Ruff, `git diff --check`, and Skillware checks where applicable.
- Audit every requirement against source, tests, text output, JSON output, and installed runtime behavior.

## Risks And Deviation Triggers

- Stop if a class reference cannot remain the canonical identity without introducing a second class namespace.
- Do not place Chatlas semantics in `agentos-pkg` merely because the Index linter emits the finding.
- Do not duplicate documentation text into the runtime catalog to conceal unresolved package documentation.
- Do not redesign `LinterState` or check dependency execution in this cut; that mutable-state cleanup is explicitly deferred.
- Preserve unrelated worktree changes and checkpoint every execution target before implementation edits.

## Acceptance Signals

- `from agentos.poi import POICatalog, POIInstance` works.
- Every core and injected Chatlas Index finding code has exactly one package-owned class reference.
- Repeated equivalent Index findings produce stable instance IDs.
- Index linter text prints one class heading/description followed by compact instances.
- Index linter JSON exposes POI groups and instances rather than legacy finding records.
- Missing class documentation produces a Wayfinder resolution POI while original instances remain visible.
- `agentos poi explain Index.Linter/Block.TooLong` resolves the authoritative class block.
- `agentos poi explain index://agentos-pkg/Index.Linter/Block.TooLong` resolves the same class.
- Focused and relevant full suites, Ruff, and diff checks pass.

## Impl.Agendix

- [touched] autonomous design and execution authorization ^c20260729-47u
- [touched] `POI.System`, `POI.Check`, `POI.Class`, `POI.Instance`, `POI.Catalog`, `POI.Documentation`, `POI.Renderer`, and `POI.Explain` from `skills/agentos-pkg/design/107-design.md`
- [touched] `Agentos.Wayfinder` and `Wayfinder.Reference.Type::Index.Block` from `skills/agentos-pkg/design/110-design.md`
- [touched] existing class roots in `skills/agentos-pkg/appendix/Index.Linter-appendix.md`

## Impl.Log

- 2026-07-29: design phase completed in `Alignment.Mode::Autonomous`; repository grounding confirmed addressable core class blocks, newer undocumented core codes, and Chatlas-owned injected findings.
- 2026-07-29: implemented the shared POI model, strict composable catalogs, deterministic occurrence identity, one-resolution grouped rendering, and `POI.Explain`.
- 2026-07-29: adapted scoped Index findings at the reporting boundary, replaced public `findings` JSON with `poi_classes` and `pois`, and registered all core and injected Chatlas finding codes under their owning packages.
- 2026-07-29: complete suites passed in `agentos-py` (574), `agentos-chatlas-py` (257), and `agentos-cli` (66); scoped Ruff, format, and diff checks passed for every changed Python surface.
- 2026-07-29: refreshed the installed editable CLI, resolved `Index.Linter/Block.TooLong` through the live Wayfinder registry, and verified real grouped text/JSON linter output with a stable POI instance ID.
