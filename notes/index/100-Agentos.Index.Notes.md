# Agentos.Index.Notes

`Agentos.Index.Notes` is the durable concept-note subsystem of an Agentos-style project.

It is the high-signal markdown surface where important concepts, constraints, rationale, naming conventions, reusable patterns, steering decisions, boundaries, consequences, and exclusions are preserved so they can guide future work.

## Role

`Agentos.Index.Notes` is the SSOT for public markdown-surface design knowledge in an Agentos-style project.

This does not mean every useful thought must start in perfect index-note form. Rough material may temporarily live in live notes, skills, `AGENTS.md`, code, or other surfaces while the system is evolving. When that material becomes durable design truth, the convergence direction is promotion into `notes/index/`.

## What Belongs Here

Index notes capture material that changes future judgment.

Good index material includes:

- named concepts
- rationale behind decisions
- constraints and boundaries
- reusable patterns
- naming conventions
- steering rules
- consequences and tradeoffs
- explicit exclusions

Index notes should not become transcripts, changelogs, progress dashboards, implementation dumps, task lists, or generic tutorials unless the tutorial itself is the durable concept.

## Low-Friction Capture

The first priority is preserving important knowledge where future agents and humans can find it.

Useful material can enter before it has mature structure. An essay, rough note, partial concept, awkward placement, or stub can be acceptable when the information is important enough. Later maintenance can improve naming, placement, structure, and compression.

The desired mature shape is `Index.Note.Style`; it is a convergence target, not a gate that blocks capture.

## Relationship To Other Surfaces

Other markdown surfaces derive durable design truth from `Agentos.Index.Notes`.

Examples:

- `Usage.Skill` should explain public use while deriving durable concepts from index notes.
- `Agentos.Dev.Notes` should explain internal development work without becoming a competing design SSOT.
- `AGENTS.md` can route and remind agents, but durable design rules should be promoted into the index.
- skills can operationalize workflows, but they should not be the only place where major design concepts are defined.

If a source outside `notes/index/` is repeatedly being used as durable design truth, that material should probably be promoted into `Agentos.Index.Notes`.

## Internal Concepts

- `Index.Note`: the durable note unit
- `Index.Block`: a high-signal block carrying one steering idea
- `Index.Note.Style`: the desired mature note shape
- `Agentos.Index.Writing.Principles`: judgment about what is worth preserving
- `Agentos.Index.Ontology.Registry`: the low-resolution concept inventory; `001-ontology.md` is its reserved entrypoint, and additional ontology files use ordinary dynamically allocated prefixes
- `Agentos.Ontology.Workflows`: the workflows around concept emergence, lookup, registration, promotion, rename, and maintenance
- `Ontology.Namespace`: an explicit organizing view over ontology concepts; namespaces can overlap and are not inferred from dotted notation alone
- `Ontology.Integration.Hook`: a namespace for external concepts consumed locally, including local interpretation, mode, constraints, or mappings

## Maintenance State

Captured material may need later note-level review:

- reformatting
- relocation
- deduplication
- naming cleanup
- registry and index-link updates

This is note maintenance, not project progress tracking.

## Related Concepts

- `Md.Surface`
- `Design.Target.Model`
- `Current.Implementation`
- `Design.Implementation.CoEvolution`
- `Agentos.Index.Ontology.Registry`
- `Index.Note.Style`
- `Stub.Convention`

## Provenance

Promoted from the closed design session at `../live/501-agentos-index-notes-design-session.md`.
