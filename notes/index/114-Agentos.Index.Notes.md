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
