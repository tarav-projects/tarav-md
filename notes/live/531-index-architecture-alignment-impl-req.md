# Index System Architecture Alignment - impl-req

## Impl.Abstract

- **scope:** align index notes and skills with the redesigned index architecture from the design session (530)
- **status:** ready for implementation
- **source:** design session `notes/live/530-index-system-revisit-design-session.md` — items 1-8

## Impl.Index

### Kernel.Writing.Introduction

- `Kernel.Writing` and `Kernel.Block` are new base concepts — they don't exist in the index yet
- `Kernel.Block` defines the universal structure: fundamentals + `### appendix` + `### meta`
- all block types derive from `Kernel.Block` — this must be established before revising dependent concepts
- target note: new block in `100-index.md` or a dedicated flat file
- ontology entries needed in `001-ontology.md`

### Block.Structure.Revision

- `### index` and `### outlinks` are absorbed into `### meta`
- `Complete.Index.Block` is removed — `Kernel.Block` already includes appendix + meta
- `Index.Block.Outlinks` section in `100-index.md` is removed — outlinks are now part of `### meta`
- `Design.Index.Block` revise to reference `Kernel.Block` instead of `Complete.Index.Block`
- dividing rule: fundamentals and appendix are conceptual; meta is non-conceptual

### Appendix.Redesign

- appendix files change from numbered to concept-named: `Concept.Name-appendix.md`
- location stays `notes/appendix/`
- discovery is implicit — agents check if the file exists by convention, no outlink required
- existing files to rename:
    - `notes/appendix/125-Agentos.Surfaces.md` → determine concept name
    - `notes/appendix/125-Development.Principles.md` → determine concept name
- `Index.Appendix.Block` as a separate concept is removed

### Ontology.System.Introduction

- `Ontology.Registry` needs a block in `001-ontology.md` — the concept graph layer of the index
- `Ontology.Namespace` needs a block — explicit bounded organizing view over concepts
- `Index.Architecture` needs a block — Global.Index.Scope vs Extended.Index.Scope
- `Agentos.Index` needs its own Ontology.Namespace in `001-ontology.md`

### Wording.Revision

- "durable concept-note subsystem" → Stable.Surface framing in `000-index.md`, `100-index.md`, `001-ontology.md`
- `Agentos.Index.Notes` description must reflect the four roles: conceptual implementation, discovery, development surface, main alignment surface

## Execution.Plan

### Slice 1 — Introduce Kernel.Writing and Kernel.Block in the index

- add `Kernel.Writing` and `Kernel.Block` blocks to the last flat index file
- add ontology entries in `001-ontology.md`
- path: flat index files → `notes/index/001-ontology.md`
- observable: both concepts exist as `Index.Blocks` with fundamentals
- check: blocks match the design session definitions
- status: not started

### Slice 2 — Revise Index.Block and remove Complete.Index.Block

- revise `Index.Block` in `100-index.md` to reference `Kernel.Block`, remove `### index`/`### outlinks` → `### meta`
- remove `Complete.Index.Block` block from `100-index.md` and `001-ontology.md`
- remove `Index.Block.Outlinks` block from `100-index.md` and `001-ontology.md`
- revise `Design.Index.Block` to reference `Kernel.Block`
- path: flat index files → `notes/index/001-ontology.md`
- observable: no references to `Complete.Index.Block` or `### outlinks` as a separate section in live index
- check: grep for removed terms returns zero hits in `notes/index/`
- status: not started

### Slice 3 — Introduce ontology system blocks

- add `Ontology.Registry`, `Ontology.Namespace`, `Index.Architecture` blocks to `001-ontology.md`
- add `Agentos.Index` as an `Ontology.Namespace` section
- path: `notes/index/001-ontology.md`
- observable: ontology system concepts are navigable from the ontology entry point
- check: blocks match the design session definitions
- status: not started

### Slice 4 — Appendix redesign

- rename existing appendix files from numbered to concept-named
- update `agentos-index-appendix-base` skill to reflect new naming convention
- update `agentos-index/references/appendix.md`
- path: `notes/appendix/` → `skills/agentos-index-appendix-base/` → `skills/agentos-index/references/appendix.md`
- observable: appendix files follow `Concept.Name-appendix.md` convention; skill describes implicit discovery
- check: no numbered appendix files remain; skill references are consistent
- status: not started

### Slice 5 — Wording revision and skill alignment

- revise "durable concept-note subsystem" wording in `000-index.md`, `100-index.md`, `001-ontology.md`
- update `agentos-index-writer` — `### index` handling → `### meta`
- update `agentos-index/references/block-syntax.md` — `### index` → `### meta`
- update `agentos-index` SKILL.md reference table
- path: index notes + affected skills
- observable: consistent terminology across index notes and skills
- check: grep for stale terms returns zero hits in `notes/index/` and `skills/`
- status: not started

## Impl.Log

- 2026-05-15: Impl.Req created from design session 530, items 1-8
