# Wayfinder Index Resolver - Impl.Req

## Impl.Abstract

- **Goal:** implement `Agentos.Wayfinder` as a standalone `agentos-py` library, expose it through `agentos wayfinder`, and deliver the first end-to-end `index.block` reference path required by the POI system.
- **Status:** implemented and verified.
- **Source design:** `skills/tarav-pkg/design/110-design.md`, the Wayfinder-backed POI blocks in `skills/tarav-pkg/design/107-design.md`, and the execution authorization at `^c20260729-46u`.
- **In scope:** canonical typed references, global registry and relocation hints, deterministic resolver composition, structured resolution results and POIs, Index block resolution, POI-class reference helpers, migration of Index depot lookup to the shared registry, thin CLI registration, tests, and project guidance.
- **Out of scope:** project-local registry providers, non-Index reference types, semantic agent relocation, automatic filesystem search, `Poi.Bless`, and a complete generic POI runtime.

## Impl.Index

### Library Boundary

- `agentos.wayfinder` is importable without CLI or Chatlas dependencies.
- `Wayfinder.Reference` is represented by a strict versioned JSON object.
- `Wayfinder.Reference.Type::Index.Block` is the first supported type.
- Canonical Index references carry a `package.skill` root and a relative `Skw.Address.Schema` block address.
- `index://<package-id>/<block-path>` is the first parseable sugar.

### Registry

- The first `Wayfinder.Registry` provider is global-only at `~/.agentos/wayfinder/registry.json`; `AGENTOS_HOME` and a direct test override remain honored.
- Registrations bind a canonical root to a last verified absolute filesystem location and an open JSON list of relocation hints.
- Registry writes are locked and atomic.
- Registering an existing root replaces its remembered resolution while retaining caller-supplied hints exactly.
- Stored locations and hints are operational evidence, never reference identity.

### Resolution

- `Wayfinder` selects a resolver from the canonical reference type.
- The Index resolver obtains the package root from the registry, parses its `Index.Depot` through `agentos.index.model.parse_depot`, resolves exactly one matching `BlockHeading`, and returns the block text and coordinates.
- Normal inability to resolve returns a structured `WayfinderResolutionPOI`; malformed caller input remains a boundary error.
- Resolution traces expose registry lookup, domain lookup, and verification outcomes.
- Missing registration, stale root, missing block, and duplicate block cases are independently observable.

### POI Support

- `poi_class_reference(package_id, class_name)` produces the same canonical `index.block` reference used by normal Index resolution.
- A resolved block result contains enough authoritative content for a future `POI.Explain` consumer.
- Resolution failure retains the original class reference and deterministic POI instance identity.

### Existing Index Integration

- `agentos.index.depot_deps.load_depot_registry` reads package/depot roots from the Wayfinder registry rather than maintaining a second `index.depots` path registry.
- `index.default_depends` remains policy in global `config.json`; it is not reference-location state.
- No compatibility read of the superseded `index.depots` registry is added.

### CLI

- `agentos wayfinder register` accepts a canonical root or package convenience argument, an existing path, and open string/JSON hints.
- `agentos wayfinder resolve` accepts canonical reference JSON or `index://` sugar and always emits structured JSON.
- `agentos wayfinder check` validates registry structure and reports stale remembered locations without mutation.
- Resolution POIs render as JSON and return a nonzero command status.
- `agentos-cli` remains a thin composition root that imports the registrar from `agentos-py`.

## Execution.Plan

### Slice 1 - Canonical model and global registry

- Add `agentos.wayfinder` model and registry modules.
- RED: tests reject malformed references and prove a moved package root can replace remembered state without changing reference identity.
- GREEN: strict dataclasses, canonical JSON, locking, atomic persistence, open hints, and registry checks.
- Check: `uv run pytest tests/test_wayfinder.py -q`.

### Slice 2 - Index and POI resolution

- Add resolver orchestration, `index.block` domain resolution, block extraction, structured traces/results/POIs, and POI-class helpers.
- RED: tests cover successful block content retrieval plus missing, stale, absent, and duplicate outcomes.
- GREEN: resolve through `parse_depot`; no independent Markdown parser or filesystem search.
- Check: `uv run pytest tests/test_wayfinder.py tests/test_index_model_parser.py -q`.

### Slice 3 - Unify existing Index depot registration

- Replace `index.depot_deps` location lookup with Wayfinder registry entries while retaining direct/non-transitive dependency policy.
- RED: update depot dependency tests so obsolete `index.depots` config no longer establishes reachability.
- GREEN: dependency lookup consumes the shared root registry.
- Check: `uv run pytest tests/test_depot_deps.py tests/test_index_drift.py tests/test_index_linter.py -q`.

### Slice 4 - CLI composition

- Add `agentos.wayfinder.commands.register_wayfinder_commands`.
- Register it in `agentos-cli`, add end-to-end tests, and update both project `AGENTS.md` files where their architecture/CLI descriptions change.
- RED: CLI test requires command discovery, register/resolve round trip, canonical JSON input, POI failure, and check output.
- GREEN: thin command handlers over the library.
- Check: focused tests in both repositories and `agentos wayfinder --help`.

### Slice 5 - Installed runtime and completion

- Refresh the editable `agentos-cli` tool.
- Register current package roots through the new command so the live global registry can resolve the Agentos package indexes.
- Run relevant full suites, Ruff, diff checks, and real `agentos wayfinder resolve index://tarav-pkg/POI.Catalog`.
- Audit every objective requirement against source, tests, and installed runtime output.

## Risks And Deviation Triggers

- Stop and record if `parse_depot` cannot provide sufficient block identity/content without modifying the Index model.
- Preserve unrelated `agentos-py` agent-config edits; the mandatory execution checkpoint records them before Wayfinder work.
- Do not make heuristic search part of deterministic resolution to compensate for missing registrations.
- Do not add compatibility handling for `index.depots`; current global entries are re-registered explicitly through Wayfinder.
- If CLI installation exposes dependency drift, repair the editable composition rather than testing only an uninstalled source path.

## Acceptance Signals

- `from agentos.wayfinder import Wayfinder, WayfinderReference` works.
- A canonical reference round-trips through JSON and `index://` sugar.
- A global registration resolves a real indexed `POI.Class` block after package relocation/update.
- Resolution failures produce stable structured POIs with traces and hints.
- `Index.Depot.Dependency` consumes the Wayfinder registry.
- `agentos wayfinder register|resolve|check` works through the installed executable.
- Focused and relevant repository tests and Ruff pass.

## Impl.Agendix

- [touched] autonomous design and execution authorization ^c20260729-46u
- [touched] `Agentos.Wayfinder` and its resolution boundary from `skills/tarav-pkg/design/110-design.md`
- [touched] `Wayfinder.Reference`, `Wayfinder.Registry`, `Wayfinder.Resolver`, and `Wayfinder.Resolution` from `skills/tarav-pkg/design/110-design.md`
- [touched] `Wayfinder.Reference.Type::Index.Block` from `skills/tarav-pkg/design/110-design.md`
- [touched] Wayfinder-backed `POI.Class`, `POI.Catalog`, `POI.Documentation`, and `POI.Explain` from `skills/tarav-pkg/design/107-design.md`

## Impl.Log

- 2026-07-29: design phase completed in `Alignment.Mode::Autonomous`; baseline focused tests passed in `agentos-py` (13) and `agentos-cli` (7).
- 2026-07-29: implemented strict canonical references, the locked global registry, Index-backed resolution, deterministic resolution POIs, POI-class helpers, shared Index depot lookup, and the thin umbrella CLI.
- 2026-07-29: focused Wayfinder and depot tests passed (20); the complete `agentos-cli` suite passed (64); Ruff and `git diff --check` passed in both repositories.
- 2026-07-29: refreshed the installed editable CLI, registered `tarav-pkg`, `tarav-chatlas-pkg`, and `md-library-pkg`, confirmed `agentos wayfinder check`, and resolved `index://tarav-pkg/POI.Catalog` to the canonical `design/107-design.md` block.
- 2026-07-29: an initial full regression briefly intersected concurrent support-set grounding edits; after that work aligned its tests, the final complete `agentos-py` suite passed (563).
- 2026-07-29: project-scope `agentos skw check` found no package POIs and stopped on 11 pre-existing edition-history POIs (nine v1 support records and two missing associations), outside this implementation boundary.
