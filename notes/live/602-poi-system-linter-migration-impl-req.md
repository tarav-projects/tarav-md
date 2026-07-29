# 602 - POI.System Linter Surface Migration - Impl.Req

## Impl.Abstract

- **Goal:** migrate the active Python Agentos linters identified in `agentos-py`, `agentos-chatlas-py`, and `agentos-canvas-py` onto the common `POI.System` representation and reporting path.
- **Status:** ready for execution.
- **Nature:** a marathon, behavior-preserving normalization. Checks keep deciding exactly what they decide today; this effort changes how their results are identified, registered, documented, rendered, explained, and, where already supported, blessed.
- **Source design:** `POI.System`, `POI.Check`, `POI.Class`, `POI.Instance`, `POI.Catalog`, `POI.Documentation`, `POI.Renderer`, `POI.Explain`, and `Poi.Bless` in `skills/agentos-pkg/design/107-design.md`; Wayfinder resolution in `skills/agentos-pkg/design/110-design.md`.
- **Predecessors:** `notes/live/601-poi-catalog-renderer-impl-req.md`, `agentos-py/notes/live/700-linter-core-unification-impl-req.md`, and `agentos-py/notes/live/706-skw-poi-unlock-token-mvp-impl-req.md`.
- **In scope:** shared POI/reporting foundations; catalog registration; package-owned POI chapters; adapters for all included validators; common text/JSON representation; explanation; preservation of existing instance and blessing identities; explicit documentation placeholders.
- **Out of scope:** changing check predicates, execution order, defaults, severity, exit policy, repair behavior, mutation behavior, blessing policy, unlock requirements, or domain interpretation; completing undocumented POI semantics; adding checks; converting ordinary status, health, query, runtime exception, or readiness-gate surfaces merely because they contain the word "check" or "POI"; inventorying or migrating Canvas JS, Iterante, or unrelated maintained projects.

## Migration Invariants

### Behavior Is Frozen

- Each migrated producer runs the same checks over the same input and emits the same situations with the same severity and command exit behavior.
- Existing check selectors, default-on state, structural tiers, blocked-check behavior, and check ordering remain unchanged.
- Existing repair and mutation paths remain command-owned. `POI.System` reports and resolves identity; it does not acquire domain repair logic in this migration.
- Any discovered semantic defect is recorded separately. It is not silently repaired while moving the producer.

### Meaning Is Not Invented

- If authoritative documentation already explains a class, migrate or reference that existing meaning at its natural package placement.
- If only a code, message, legend entry, or implementation branch exists, preserve it verbatim as the available description and mark the class documentation as incomplete.
- If the class meaning cannot be established without renewed design or historical grounding, create an honest placeholder class block. The placeholder names the producer and legacy code, states that interpretation is not yet established, and provides no fabricated evaluation or resolution guidance.
- Placeholder status must be visible to agents reading or explaining the class. Placeholder completion is a later documentation task, not an acceptance condition for this migration.

### Identity Is Preserved

- A migrated occurrence remains the same externally addressable situation whenever its legacy producer already exposes a stable identity.
- Skillware's 10-character `poi_hash` remains valid for `bless`, suppression, lock records, and scripts. The common model must support producer-established instance identity rather than recomputing a different 12-character identity.
- Other producer identities, ordering, targets, and evidence are preserved where they are already observable.
- New identity derivation is allowed only for producers that currently have no public occurrence identity, and must be deterministic from the existing situation.

### Diagnostics Stay Distinct

- `Closure.Parser` and other floor providers emit diagnostics below their processing floor; they do not become judgment POIs merely to fit a renderer.
- A common linter result may carry both diagnostics and `POI.Instance`s, but the two channels remain distinct in the model and structured output.
- Existing commands that historically label floor failures as POIs may preserve their user-visible compatibility during the cut, but the adapter must retain the diagnostic origin and must not create invented class semantics for parser failure.

## Current State

### Existing Common Cut

- `agentos.poi` already provides `POI.Instance`, `POI.Catalog`, grouped rendering, Wayfinder-backed class resolution, and `agentos poi explain`.
- The Index linter already adapts internal `LinterFinding`s into this model and composes Chatlas-owned registrations at the umbrella boundary.
- `agentos.skwlint` remains a parallel general-looking core with its own `Poi`, identity hash, check selection utilities, drift engine, and blessing helpers. It predates the current `POI.System` cut and must be decomposed rather than retained as a second POI model.

### Included Producers

| Producer | Current result surface | Natural class owner | Documentation state |
| --- | --- | --- | --- |
| Index linter | common `POI.System` adapter over `LinterFinding` | `agentos-pkg`; injected Chatlas checks in `agentos-chatlas-pkg` | partially complete; preserve unresolved classes |
| Skillware check/project check | `agentos.skwlint.Poi`, `CheckReport`, bespoke renderer and blessing | `agentos-pkg` | strong existing `references/check.md`; some classes still need placeholders |
| Skillware edition-history check | `EditionHistoryFinding` | `agentos-pkg` | implementation and developer reference are usable |
| Markdown blocks lint | issue dictionaries | `agentos-pkg` | partial; Index mappings document many classes |
| Anchory depot check | `AnchoryCheckFinding` | `agentos-pkg` | system semantics documented; class-level guidance incomplete |
| Bloberia check | `BloberiaCheckFinding` | `agentos-pkg` | system semantics documented; class-level guidance incomplete |
| Wayfinder registry and resolution checks | `WayfinderRegistryFinding` and `WayfinderResolutionPOI` | `agentos-pkg` | model is documented; bootstrap handling required |
| Tara tape check | `list[str]` issue messages | `agentos-pkg` | insufficiently structured; mostly placeholder migration |
| Chatlas zip-transcript summary commit linter | immediate `CliError` refusal branches | `agentos-chatlas-pkg` | invariant is clear in code; class guidance is absent |
| Canvas render lint | `RenderError` embedded in render flow | `agentos-canvas-pkg` | protocol documentation exists; class guidance is partial |

### Explicitly Adjacent, Not Automatically Included

- Chatlas `file-edition-pois` is an evidence-discovery query over a session model, not currently a linter verdict surface. Keep it unchanged unless execution proves it participates in a validation/refusal workflow.
- Chatlas index doctor is a legacy system with unsettled maintenance status. Do not migrate it before a separate retain-or-retire decision.
- Agent profile check is a pre-run fitness gate, not a POI linter.
- `agentos forum check`, project/system doctor summaries, and similar status queries are not POI producers.
- Runtime lock violations, mission validation exceptions, and UI checkpoints remain in their owning error or gate models.

## Target System

### Common Linter Boundary

- `agentos.poi` is the sole common POI identity, catalog, report, renderer, and explanation boundary.
- A producer may retain an internal domain finding or diagnostic type when it is useful, but exactly one adapter converts reportable findings into `POI.Instance`s.
- The common report envelope supports POIs, floor diagnostics, check status/coverage, and command-specific summary data without flattening them into one finding list.
- Common check selection utilities currently in `agentos.skwlint` move under the POI linter boundary; the `Skw.Network` drift algorithm remains domain logic and emits through the common boundary.
- `agentos.skwlint.Poi` is retired after Skillware and its consumers no longer depend on it.

### Catalog And Ownership

- Every emitted POI class has one canonical Wayfinder `index.block` reference.
- The owning Package.Skill contains a `poi` chapter that serves as the catalog root.
- The package that owns the meaning owns the class documentation, even when another package's linter executes the check.
- The umbrella CLI composes engaged package catalogs; foundation packages do not import feature packages to discover their classes.
- Catalog completeness tests prove that every runtime-emittable class code has exactly one registration.

### Documentation Migration

- Existing authoritative text is moved or referenced without semantic expansion.
- Every missing class receives a minimal placeholder block so `poi explain` reaches a real owned surface instead of failing only because migration is incomplete.
- A placeholder contains: canonical class name, legacy producer/code, preserved legacy description if one exists, and an explicit statement that evaluation/resolution guidance is not yet established.
- A placeholder must not declare blessability, allowed dispositions, or context gates unless those are already enforced and documented by the current system.
- Completing placeholders requires a separate review of the POI's purpose and is not bundled into this mechanical effort.

### Rendering And CLI Compatibility

- All included linter commands expose the common grouped class plus compact-instance text representation and the common structured POI representation.
- An included lifecycle linter that must refuse an act may preserve its exception boundary, but the refusal carries or renders the same canonical POI instance rather than maintaining an unaddressable error-only class.
- Domain summaries, diagnostics, blocked checks, render actions, and similar non-POI data remain available in dedicated fields or sections.
- Command names, arguments, selectors, defaults, and exit codes do not change.
- Legacy JSON keys may be removed only where the command has no documented compatibility promise; otherwise provide a deliberate compatibility transition without maintaining a second semantic model.

### Wayfinder Bootstrap

- Wayfinder resolution can fail while resolving a POI class, so `Wayfinder.Resolution.POI` cannot require successful catalog resolution to exist or render.
- Preserve one bootstrap-safe, inline representation for Wayfinder resolution failure, with canonical class identity and stable instance identity.
- Once Wayfinder can resolve its own class documentation, explanation may enrich the bootstrap result, but failure rendering must never recurse.

## Execution Plan

### Slice 0 - Baseline And Migration Matrix

- Capture text, JSON, exit code, ordering, selector registry, and stable IDs for representative clean/failing fixtures of every included producer.
- Record every emitted code, its package owner, current description source, blessability, identity source, and documentation status.
- Add no production behavior.
- **Check:** committed golden/contract fixtures can detect predicate, severity, identity, ordering, and exit-policy drift during later slices.

### Slice 1 - Complete The Common Boundary

- Extend the common model to accept producer-established instance identity.
- Add the report envelope with separate POI and diagnostic channels plus optional domain summary/status data.
- Move generic check-selection helpers from `agentos.skwlint` into the common linter boundary without changing their CLI behavior.
- Add a standard placeholder-class convention and catalog completeness support.
- **Observable:** the existing Index adapter still produces equivalent POIs; an adapter can preserve a legacy 10-character identity; diagnostics serialize separately.
- **Check:** focused `agentos.poi`, Index, selector, renderer, and Wayfinder tests.

### Slice 2 - Index Completion And Package Catalog Skeletons

- Keep all Index checks unchanged and migrate currently unresolved registrations to explicit owner-package placeholder blocks.
- Create or complete `poi` chapter roots for `agentos-pkg`, `agentos-chatlas-pkg`, and `agentos-canvas-pkg`.
- Preserve the existing Chatlas injection boundary.
- **Observable:** every Index-emittable class explains to either authoritative documentation or an explicit placeholder; no class disappears behind a resolution failure.
- **Check:** catalog completeness plus before/after Index linter parity for situations, severity, ordering, blocked checks, and exit code.

### Slice 3 - Foundation Validators

- Adapt markdown blocks, Anchory, and Bloberia checks at their reporting boundaries.
- Keep their internal finding types where useful; do not rewrite predicates merely to share a model.
- Populate class blocks from existing code/messages and documented system contracts; use placeholders for unresolved interpretation.
- **Observable:** each command renders common POI classes/instances while reporting exactly the baseline findings.
- **Check:** focused module tests, CLI goldens, and catalog completeness.

### Slice 4 - Wayfinder Bootstrap

- Adapt Wayfinder registry findings to common instances.
- Align `WayfinderResolutionPOI` with common identity/serialization while retaining bootstrap-safe nonrecursive rendering.
- Prove POI documentation resolution failure cannot recursively generate an unrenderable POI.
- **Observable:** missing, stale, ambiguous, malformed, and unreachable references remain inspectable through one stable Wayfinder resolution POI shape.
- **Check:** registry checks, successful resolution, missing class, ambiguous class, stale root, and recursion-guard tests.

### Slice 5 - Skillware Core And Blessing Preservation

- Adapt Skillware check and project-check reports to the common report envelope.
- Preserve parser-floor diagnostics as diagnostics while retaining intentional command compatibility.
- Move Skillware POI classes into the `agentos-pkg` catalog using the existing check reference as authoritative input.
- Route text/JSON through the common renderer while retaining status entries and project summaries.
- Rewire `bless` and suppression to common instances without changing accepted kinds, unlock requirements, lock format, or existing `poi_hash` values.
- Retire `agentos.skwlint.Poi`; retain `Skw.Network` algorithms in an appropriately domain-owned module.
- **Observable:** every pre-migration blessing command still addresses the same current situation by the same hash, and a further situation change still mints the same new hash it would have minted before migration.
- **Check:** byte-level lock comparisons, blessing/unlock tests, text/JSON parity, project-check parity, and the full Skillware suite.

### Slice 6 - Edition History And Tara

- Adapt edition-history findings with existing structured codes and evidence.
- Give Tara's existing issue branches stable class codes at the adapter boundary without changing validation conditions or messages.
- Use placeholders where Tara's purpose cannot be recovered from current authoritative surfaces.
- **Observable:** both commands emit common POIs for exactly their baseline issue set.
- **Check:** fixture parity, deterministic IDs, ordering, exit codes, and package catalog completeness.

### Slice 7 - Chatlas Commit Linter

- Adapt the zip-transcript agent-summary commit linter's existing refusal branches into canonical Chatlas-owned POI classes while preserving the exact commit refusal point and invariant checks.
- Keep Chatlas as semantic and catalog owner.
- Do not convert general Chatlas query, file-edition discovery, or legacy doctor surfaces.
- **Observable:** commit-invalid summary artifacts still refuse the same act and expose the corresponding POI identity.
- **Check:** every existing commit-linter invariant and the Chatlas full suite.

### Slice 8 - Canvas Render Lint

- Adapt `RenderError` at the render command boundary without changing canvas parsing, rule execution, generated actions, apply behavior, or output file handling.
- Keep the render result's actions separate from POI instances.
- Register Canvas-owned class blocks, using existing protocol text where clear and placeholders otherwise.
- **Observable:** the same invalid canvas produces the same rules and actions, now with stable POI identities and explainable classes.
- **Check:** render/apply fixtures, no-mutation-on-failure behavior, catalog completeness, and Canvas full suite.

### Slice 9 - Consolidation And Runtime Audit

- Remove obsolete renderers and parallel POI models only after all consumers have moved.
- Audit the umbrella CLI composition and installed editable runtime across all included commands.
- Run package checks for every modified Package.Skill and verify every registered class through `agentos poi explain`.
- **Check:** complete suites for `agentos-py`, `agentos-chatlas-py`, `agentos-canvas-py`, and `agentos-cli`; Ruff/format/diff checks; real command smoke tests; repository-wide search proving no included producer exposes an unadapted public finding list.

## Risks And Deviation Triggers

- Stop if preserving an existing check requires changing its predicate or interpretation. Record a follow-up instead.
- Stop if a stable public identity cannot be carried into `POI.Instance` without invalidating blessings or persisted suppressions.
- Stop if common rendering would discard domain diagnostics, summaries, actions, blocked checks, or other command-contract data.
- Stop if a class owner cannot be determined mechanically; use an explicitly provisional placeholder only after recording the ownership uncertainty.
- Stop if Wayfinder failure rendering invokes Wayfinder class resolution recursively.
- Do not use this migration to bless baseline floods, repair findings, rewrite user content, or complete speculative documentation.
- Keep subsystem slices independently landable. A blocked later producer does not justify leaving earlier producers in a mixed or partially removed state.

## Acceptance Signals

- One importable common POI model and report boundary serves every included linter.
- Every emitted POI instance names exactly one package-owned class reference.
- Every registered class resolves to authoritative documentation or an explicit placeholder block.
- `agentos poi explain` works across engaged `agentos-pkg`, `agentos-chatlas-pkg`, and `agentos-canvas-pkg` catalogs.
- Parser/floor diagnostics remain distinguishable from POIs.
- Existing Skillware POI hashes, blessings, suppression records, unlock gates, and re-drift behavior remain valid.
- Wayfinder resolution failures render without catalog recursion.
- All included commands retain their check set, findings, severity, ordering, selectors, mutation behavior, and exit policy.
- No excluded status, query, readiness-gate, or runtime-error surface is converted merely for naming consistency.

## Impl.Agendix

- [touched] the request is mechanical migration into `POI.System`, not a redesign of checks or an attempt to infer missing POI meaning.
- [touched] clear existing documentation should migrate; unclear semantics should remain explicit placeholders until context is reloaded and reviewed.
- [touched] the Index linter is the first common-runtime cut, not proof that the rest of Agentos already shares one linter system.
- [touched] Skillware identity and Wayfinder bootstrap behavior are the two hard architectural constraints discovered during repository grounding.

## Impl.Log

- 2026-07-29: implementation design started from a repository-wide linter usage inventory.
- 2026-07-29: classified deterministic actionable validators separately from parsers, diagnostics, status commands, readiness gates, runtime errors, and evidence queries.
- 2026-07-29: established behavior freeze, honest-placeholder, identity-preservation, diagnostic-separation, package-ownership, and Wayfinder-bootstrap requirements.
