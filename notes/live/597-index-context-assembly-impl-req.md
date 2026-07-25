# Index Context Assembly - impl-req

## Impl.Abstract

- **scope:** adopt `Index.Context.Assembly` as the complete shared builder context for every managed `agentos-index` surface; prove `context-assembly-bypass` against the real package; align coverage terminology in Skillware; retire the superseded agendix candidate
- **status:** ready for execution
- **source:** current design and capture session, the existing `Index.Capture.Context.Assembly`, the complete `agentos-index/.skw/src` dependency graph, and current Skillware linter implementation
- **repositories:** `agentos-md`, `agentos-py`
- **out of scope:** runtime auto-loading, transitive or cross-package coverage inference, changes to direct dependency/materialization choices, and execution of model-backed testground scenarios

## Impl.Agendix

- **touched (chat):** a context assembly standardizes the complete subject context available to builders while leaving running-agent context selective to the active workflow ^c20260725-37u
- **touched (appendix):** `Skill.Module/Context.Assembly.Module` defines the complete coherent subject universe, builder/runtime split, non-ownership, overlapping coverage, and materialization freedom
- **touched (appendix):** `Skw.Ann.Dependency/Context.Assembly.Coverage` defines assembly-covered sources, companion `--dev-from` edges, and the semantic bypass POI
- **touched (index):** `Skill.Module`, `Skw.Ann.Dependency`, `Context.Loading.Path`, `Dynamic.Loading`, `POI.Linter`, `Index.Skillware`
- **structural:** `.skw/src/**/*.skw.md` compiles into the runnable `agentos-index` and `agentos-skillware` surfaces
- **open space:** completeness remains a curated builder responsibility; v1 mechanically supervises the declared direct coverage boundary only

## Impl.Index

### Index.Context.Assembly

- create `agentos-index/.skw/src/references/index-context-assembly.skw.md`
- its line-1 `--context-assembly` declaration covers the sorted union of current Dotted.Name dependencies declared by every existing managed `agentos-index` source
- its whole-file product gives a builder the general index system, surface, writing, grounding, gate, workflow, validation, and operational-module context needed to develop any `agentos-index` consumer
- the module explicitly distinguishes standardized builder context from selective runtime loading
- route and list the runnable `references/index-context-assembly.md` module from `SKILL.skw.md`

### Consumer Integration

- every existing managed `agentos-index` source declares `--dev-from references/index-context-assembly.skw.md`
- the general assembly does not depend on itself
- `Index.Capture.Context.Assembly` remains a specialized, overlapping context universe and declares the general assembly as development context
- existing consumers retain their capture-assembly dependencies where present; overlapping coverage intentionally accumulates applicable builder-context requirements
- no direct `--from`, `--copy`, `--derived`, or `--cite` choice is replaced or mediated

### Coverage Terminology

- use “covered source,” “coverage boundary,” and “covering assembly” for context-assembly mechanics
- remove context-assembly-specific “claimed,” “owned,” and “ownership” wording from maintained Skillware sources, generated docs, Python diagnostics, tests, and `agentos-py/AGENTS.md`
- preserve unrelated uses of ownership, claims, and “owns an end”
- rename private Python helper/local identifiers from claims to coverage; no compatibility alias
- keep the public POI kind `context-assembly-bypass`

### Candidate Reconciliation

- delete `agentos-pkg/agendix/Skill.Module-agendix.md` after confirming its candidate content is represented by the landed `Skill.Module` and `Skw.Ann.Dependency` appendix sections plus maintained Skillware documentation
- do not change the reviewed ontology blocks

## Execution.Plan

### Slice 1 - Prove package-level coverage supervision

- create the general assembly and its runnable route without adding consumer `--dev-from` edges
- build `agentos-index`, then run `agentos skw check --skill skills/agentos-index`
- observable RED: `context-assembly-bypass` appears on existing consumers that directly use covered sources
- record the observed targets/count in `Impl.Log`; do not bless the POIs
- status: completed

### Slice 2 - Wire the complete builder context

- add the general assembly `--dev-from` edge to every existing managed source, including the specialized capture assembly
- keep existing capture-specialization edges intact
- build and check `agentos-index`
- observable GREEN: all managed surfaces compile and `context-assembly-bypass` returns to zero
- check: `agentos skw check --skill skills/agentos-index`
- status: not started

### Slice 3 - Align coverage language and linter diagnostics

- add or update focused `agentos-py` tests for coverage-oriented bypass diagnostics and legends
- rename private context-assembly claim helpers/locals and update diagnostic text
- update `agentos-py/AGENTS.md`
- update maintained `agentos-skillware/.skw/src` language, authoring, doctrine, and check wording, then rebuild
- preserve generic ownership terminology unrelated to context assemblies
- checks: focused Skillware Python tests, focused Ruff, `agentos skw check --skill skills/agentos-skillware`
- status: not started

### Slice 4 - Reconcile the promoted candidate and close validation

- verify the old `Skill.Module` agendix candidate against the two landed appendix sections and maintained docs, then remove the superseded agendix file
- run the package index linter and no-legacy terminology searches
- run the complete `agentos-py` test suite
- checks: `agentos index linter --depot skills/agentos-pkg`, both managed-skill checks, `uv run pytest -q`, scoped Ruff, and `git diff --check`
- status: not started

## Risks And Deviation Triggers

- stop if the deterministic dependency union makes the general assembly cover concepts unrelated to index development rather than the package’s actual subject universe
- stop if a managed source cannot declare the general assembly without changing parser or closure semantics
- stop if removing the agendix candidate would discard a design decision not represented durably elsewhere
- preserve all pre-existing dirty changes through the mandatory execution checkpoint; concurrent edits in the same target lines trigger realignment
- do not broaden terminology replacement to legitimate ownership/claim language outside context-assembly semantics

## Acceptance Signals

- `Index.Context.Assembly` exists as a whole-file managed module and is routed by `agentos-index`
- every pre-existing managed `agentos-index` source carries the general `--dev-from`
- the real package produces `context-assembly-bypass` before wiring and 0 POIs after wiring
- specialized capture coverage remains intact
- maintained context-assembly language consistently describes coverage rather than ownership
- the obsolete `Skill.Module` agendix candidate is reconciled without losing durable content
- relevant Python, Skillware, and index checks pass

## Impl.Log

- develop workflow authorized ^c20260725-37u
- execution plan confirmed and authorized ^c20260725-39u
- current `agentos-md` worktree contains the landed context-assembly appendix material, `::land-all-approved`, and concurrent Skillware edition-history changes; the mandatory execution checkpoint must preserve all of them
- current `agentos-py` worktree is clean and requires an empty mandatory execution checkpoint
- RED observation: adding the general assembly produced 147 `context-assembly-bypass` POIs across all 14 managed surfaces; no POIs were blessed
- deviation: 15 concepts are covered by both the general and capture assemblies, so the symmetric checker requires the general assembly to `--dev-from` the capture specialization while the plan requires capture to `--dev-from` general; the resulting cycle makes the planned hierarchy non-executable without a hierarchy rule or a non-overlapping boundary
