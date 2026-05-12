# Agentos.Index.Notes

## Agentos.Index.Notes

- `Agentos.Index.Notes` is the durable concept-note subsystem of an Agentos-style project
- implements the `Agentos.Index` — a `Soft.Programming.Language` for project knowledge
- the `Alignment.Surface` between humans and agents — shared ground for what things mean
- contains `Named.Concepts` written in `Index.Blocks`, organized in `Index.Notes`, registered in the `Ontology.Registry`
- agents execute the index at runtime through the `Index.Eval.Loop` — resolving names, loading blocks, detecting gaps
- lives at `notes/index/` with numbered concept notes, each centered on one concept or tight cluster

****

## Agentos.Index.Writing.Principles

- `Agentos.Index.Writing.Principles` defines what belongs in durable index notes
- index notes capture material that changes future judgment
- all index content is organized as `Named.Concepts` in `Index.Blocks`
    - a concept can carry rationale, constraints, boundaries, reusable patterns, naming conventions, steering rules, consequences, or exclusions
    - but it is always a named block — not loose prose, not unstructured material
- index notes should NOT become transcripts, changelogs, progress dashboards, task lists, or implementation dumps
- first priority is preserving important knowledge where future agents can find it
    - useful material can enter before it has mature structure
    - `Index.Note.Style` is a convergence target, not a gate that blocks capture

****

## Index.Concept.Coverage

- the index is the collection point for all `Named.Concepts` in the project's stable surfaces
- any `Dotted.Name` that appears in a stable surface should have an index entry
- each concept block must carry enough signal for an agent to reason correctly — not just a pointer
- the index is the first line of context for agents
- blocks can link out to other surfaces rather than define everything inline
    - skills, docs, and other surfaces can own the source of truth of a topic
- concepts can emerge anywhere — authors use `Dotted.Notation` naturally in their work without worrying about index maintenance
    - the system detects new `Named.Concepts` and triggers index updates separately

****

## Index.Block

- `Index.Block` is the fundamental semantic unit of the index — the loadable unit of meaning
- anchored by a heading (H2–H6) that names the concept using `Dotted.Notation`
- must carry enough signal for an agent to reason correctly about the concept
- the index must have at least a block for any meaningful concept in the system
    - blocks can link out to other surfaces rather than define everything inline
- three layers: heading (identity) → body (bullet-point sentences) → sections (`### index`, `### outlinks`)
- `### index` — findability hints and related concepts (populated on evidence of search misses)
- `### outlinks` — where else the concept is treated across surfaces
- compressed fundamentals only, space-constrained — for extended material see `Complete.Index.Block`

****

## Index.Block.Outlinks

- `Index.Block.Outlinks` is a fixed section (`### outlinks`) in an `Index.Block`
- maps where else the concept is treated across surfaces — the discovery path from index to distributed facets
- a maintenance surface — keep current as the concept grows across surfaces
- if empty, leave a placeholder: `(no outlinks yet — add links to other surfaces where this concept is treated)`

### example

```
### outlinks

- skill: `agentos-index-writer` — operational write loop
- docs: `notes/docs/NNN-whatever.md` — extended design
- code: `agentos_py/index/writer.py` — implementation
```

****

## Complete.Index.Block

- `Complete.Index.Block` is an `Index.Block` with an `### appendix` section for extended material
- the fundamentals part is equivalent to an `Index.Block` — same meaning, same restrictions
- `### appendix` — examples, use cases, reasoning, pros/cons, extended design material
    - no line count constraint, line length limit still applies

****

## Index.Appendix.Block

- `Index.Appendix.Block` is an appendix-only block hosted at `notes/appendix/`
- no fundamentals — those live in the `Index.Block` at `notes/index/`
- extended material: examples, use cases, reasoning, pros/cons, design depth
    - no line count constraint, line length limit still applies
- a `Stable.Surface` — maintained, not throwaway
- not part of `Context.Minimal.Surface` — agents reach it only on explicit need

****

## Design.Index.Block

- `Design.Index.Block` is a session-local `Complete.Index.Block` used in `Design.Session` artifacts
- captures the relevant conceptual value produced by session discussion about a subject concept
- fundamentals have the same semantic role as `Index.Block` fundamentals
    - draft quality may vary during the session, but the meaning target is the same
- inherits `### appendix` from `Complete.Index.Block`
    - carries extended conceptual value: examples, rationale, pressure tests, tradeoffs, rejected alternatives, design depth
- adds `### meta` for session mechanics: status, sources, open questions, promotion notes, stale or misaligned markers
- at promotion time: fundamentals compress into `Index.Block`, appendix material goes to `Index.Appendix.Block`, meta gets dropped or is used as workflow state
