# Import Manifest Tooling — Impl.Req

## Impl.Abstract

- **Goal**: mechanize `Module.Import` — the `Import.Manifest` format lands as files, the CPU-checkable bindings (`pointer`, `copy`) get a deterministic check command, and the builder skill migrates from the old derivation-manifest system to the import system.
- **Split** (user-settled): pointer and copy are CPU-checkable — deterministic findings; `derived` stays agentic (the builder's semantic `--check`). One manifest parse feeds both.
- **Format** (user-settled, block-per-import): one manifest per consuming module, flat naming `build/<expanded-relative-path>-<file-name>-imports.md` (e.g. `references/gr-survey.md` → `build/references-gr-survey-imports.md`); `-` joins path segments — ambiguity is a non-problem, agents resolve corner cases. Inside: one `Kernel.Block` per import — heading = target (any legal block name, 582 locator forms included), field lines `binding:` (`pointer`|`copy`|`derived`), `lands:` (region locator in the consumer; omit = whole file), `context:` (derived only, free depth), extensible by adding lines. Absence of manifest = no imports.
- **Out of scope**: the agentic `derived` check redesign (the builder's existing `--manifest-checks` behavior ports with vocabulary updates, not new mechanics); `block-craft.md` authoring (separate content work — it becomes the first heavy SSOT *after* this tooling exists); auto-regeneration policies (workflow-level, per `Module.Import`).
- **Repos**: `agentos-py` (manifest model + checks + CLI), `agentos-md` (builder skill modules, catalog manifest migration, one index line). Reinstall from `agentos-cli/` after CLI changes.
- **Source**: user turns 2026-07-09 evening (session `9d194db7...`): flat naming rule, format A block-per-import ("we need space to specify all we want"), "binding: copy / pointer — this ones we can check it on the linter"; index blocks `Module.Import`, `Import.Manifest`, `Import.Management`, `Derivation.Rule` (107, all landed `^20260709-12..16`); prior art: `agentos-skill-pkg-builder` `references/derivation.md` + `manifest-checks.md`, `build/derivation/catalog.md`.
- **Status**: designed; ready for execution

## Impl.Index

### Design.Decisions

- **manifest parsing reuses the index parser** (`agentos.index.model.parse_index_file`) — format A blocks are `BlockHeading` + `KernelLine` nodes already; a thin `agentos/skills_pkg/imports.py` (module name executer-open) maps them to an `ImportDeclaration` model (`consumer`, `target`, `binding`, `lands`, `context_lines`)
- **discovery**: glob `build/*-imports.md` under a package root; the consumer module path is recovered by expanding the filename rule against the package tree (resolve by existence — the "smart agent" rule mechanized as: try segment splits until a real file matches; zero or multiple matches = finding, not crash)
- **CPU checks** (new command):
  - `pointer` → the target resolves: file-space locators resolve on disk; ontology names resolve in the supplied index depot(s) via `parse_depot` + heading match
  - `copy` → the target's content equals the `lands` region content in the consumer (region = heading section; whole-file = file body); normalized only by trailing-whitespace — verbatim means verbatim
  - `derived` → reported as `skipped (agentic)` with a count, so the CPU report shows the full import inventory
- **CLI placement**: `agentos skills imports --package <path> [--depot <index-depot>]... [--json]` — joins the existing `agentos skills` namespace (list/import/status/path); findings-and-summary output in the linter's report style; exit non-zero on findings
- **builder skill migration** (`agentos-md/skills/agentos-skill-pkg-builder`):
  - `references/derivation.md` → `references/imports.md`: the `Import.Manifest` format A spec; old ops re-map — `copy` → binding `copy`, `projection`/`transform` → binding `derived` with the op intent folded into `context:`
  - `references/manifest-checks.md` → `references/import-checks.md`: step 0 runs the CPU command and takes its pointer/copy verdicts as given; the agentic pass covers only `derived` blocks
  - `references/check.md` + `SKILL.md`: registered-check names and routing rows updated
  - `build/derivation/catalog.md` migrates to `build/references-index-block-catalog-imports.md` in format A (its projections become `derived` imports); the `build/derivation/` folder is then removed (`No.Legacy.Allowed`)
- **index touch** (gated, verbatim at landing): `Import.Manifest` line "`build/imports/`" updates to the flat rule `build/<expanded-relative-path>-<file-name>-imports.md`
- **naming ambiguity is accepted** per the user: single `-` joiner, no escaping — resolution-by-existence handles it; a genuinely ambiguous expansion is reported as a finding

### Current.State *(inspect before coding)*

- `agentos skills` CLI: `src/agentos/` — find the registration module (pattern: `register_*_commands` like `agentos/index/commands.py`); subcommands list/import/status/path exist
- index parser: `agentos.index.model` — `parse_index_file(path, surface_kind=...)`; format A manifests parse as generic surfaces (verify heading/field-line node output on a sample before building the mapper)
- 582 naming schema: `Locator.Name` (`@path`, `#region`, `:line`) is `converging`, not landed — the tooling should parse `@`-prefixed file locators and bare `Dotted.Name`s now, and stay lenient on forms it does not know (report `unresolvable`, never crash)
- builder skill: `skills/agentos-skill-pkg-builder/` — SKILL.md (~registered checks table), references/{build,check,derivation,inline-drift,manifest-checks}.md; live manifest: `build/derivation/catalog.md` in agentos-md (one real migration case)
- tests: mirror `tests/test_index_blocks.py` fixture-depot style in `agentos-py`

## Execution.Plan

*(test-first; fixture: a small package tree with one module file, a `build/references-<module>-imports.md` manifest declaring one pointer (to a fixture depot block), one copy (region equal / then perturbed), one derived; plus a manifest whose filename expansion is ambiguous)*

### S1 — manifest model + discovery
- what: `ImportDeclaration` parse from format A via the index parser; filename-rule expansion with resolve-by-existence
- RED: unit tests — field extraction (binding/lands/context), whole-file default, discovery glob, ambiguous expansion → finding
- check: suite green
- status: pending

### S2 — pointer/copy checks + CLI
- what: check functions + `agentos skills imports` command (findings report, `--json`, exit code)
- RED: e2e — pointer resolves (file + depot block) and fails on a missing target; copy passes on equality and fails after perturbing the region; derived counted as skipped; report shape
- check: suite green; ruff clean
- status: pending

### S3 — builder skill migration + catalog manifest
- what: the module renames/rewrites listed in Design.Decisions; migrate `build/derivation/catalog.md` to the new format and location; remove `build/derivation/`; update the `Import.Manifest` index line (gated verbatim)
- check: `agentos skills imports --package skills/agentos-pkg` runs over the migrated manifest live — pointer/copy findings sane, derived inventory listed; both depots lint clean
- status: pending

### S4 — live acceptance
- what: reinstall; run the CPU check over agentos-pkg and agentos-index packages; record counts in `Impl.Log`
- check: full agentos-py suite green; the command is documented in `agentos-py/AGENTS.md`
- status: pending

### Acceptance signals
- one deterministic command reports every declared import's status: resolved / equal / drifted / unresolvable / skipped-agentic
- the builder skill speaks only the import vocabulary; no `build/derivation/` remains
- `No.Regression.Tests.Allowed`; index linter behavior untouched

### Risks / deviation triggers
- if format A field-line extraction via the generic parser is awkward (manifests are not index chapters), parse manifests with `surface_kind="unknown"` and read `KernelLine.src` directly — do not grow the index parser for manifest-specific needs
- if ontology-name resolution needs depot knowledge the CLI lacks, require `--depot` explicitly for pointer checks on ontology targets and report `unresolvable (no depot supplied)` otherwise
- if the catalog migration loses nuance (the old rules carry "on drift" prose), fold that prose into `context:` verbatim — no information dropped

## Impl.Log

- (empty — no execution yet)
