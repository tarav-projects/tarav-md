# Index System Architecture Alignment - impl-req

## Impl.Abstract

- **scope:** align index notes and skills with the redesigned index architecture from the design session (530)
- **status:** complete
- **source:** design session `notes/live/530-index-system-revisit-design-session.md` — items 1-8

## Impl.Index

### Kernel.Writing.Introduction

- `Kernel.Writing` and `Kernel.Block` are new base concepts — they don't exist in the index yet
- `Kernel.Block` defines the universal structure: fundamentals + `### appendix` + `### meta`
- all block types derive from `Kernel.Block` — this must be established before revising dependent concepts
- target note: new block in `100-index.md` or a dedicated flat file
- ontology entries needed in `001-ontology.md`

### Block.Structure.Revision

- block types are parameterizations of `Kernel.Block` using `Dotted.Parameterized.Notation`:
    - `Kernel.Block:Index` — Kernel.Block in `notes/index/`, tight space constraints; aliases: `Index.Block`, `Global.Block`
    - `Kernel.Block:Appendix` — Kernel.Block in `notes/appendix/`, relaxed space; aliases: `Appendix.Block`
    - `Kernel.Block:Design.Session` — Kernel.Block in session artifacts, draft quality; aliases: `Design.Session.Block`, `Design.Index.Block`
- aliases live in `### meta` — findability aids, not separate concepts
- `Complete.Index.Block` is removed — `Kernel.Block` already includes appendix + meta
- `Index.Block.Outlinks` section in `100-index.md` is removed — outlinks are now part of `### meta`
- `### index` and `### outlinks` are absorbed into `### meta`
- dividing rule: fundamentals and appendix are conceptual; meta is non-conceptual

### Appendix.Redesign

- appendix files change from numbered to concept-named: `Concept.Name-appendix.md`
- location stays `notes/appendix/`
- discovery is implicit — agents check if the file exists by convention, no outlink required
- existing files to rename:
    - `notes/appendix/125-Agentos.Surfaces.md` → determine concept name
    - `notes/appendix/125-Development.Principles.md` → determine concept name
- `Index.Appendix.Block` as a separate concept is removed — replaced by `Kernel.Block:Appendix`

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
- status: done

### Slice 2 — Reframe block types as Kernel.Block parameterizations

- rewrite `Index.Block` in `100-index.md` as `Kernel.Block:Index` — reference `Kernel.Block`, describe tight space constraints; add aliases in `### meta`
- rewrite `Index.Appendix.Block` in `100-index.md` as `Kernel.Block:Appendix` — reference `Kernel.Block`, describe relaxed space; add aliases in `### meta`
- rewrite `Design.Index.Block` in `100-index.md` as `Kernel.Block:Design.Session` — reference `Kernel.Block`, describe session draft quality; add aliases in `### meta`
- remove `Complete.Index.Block` block from `100-index.md` and `001-ontology.md`
- remove `Index.Block.Outlinks` block from `100-index.md` and `001-ontology.md`
- update ontology entries: rename to parameterized names, add alias entries
- path: `100-index.md` → `001-ontology.md`
- observable: block types use `Kernel.Block:X` naming with aliases; `Complete.Index.Block` and `Index.Block.Outlinks` gone
- check: grep for removed terms returns zero hits in `notes/index/`
- status: done

### Slice 3 — Introduce ontology system blocks

- add `Ontology.Registry`, `Ontology.Namespace`, `Index.Architecture` blocks to `001-ontology.md`
- add `Agentos.Index` as an `Ontology.Namespace` section
- path: `notes/index/001-ontology.md`
- observable: ontology system concepts are navigable from the ontology entry point
- check: blocks match the design session definitions
- status: done

### Slice 4 — Appendix redesign

- rename existing appendix files from numbered to concept-named
- update `agentos-index-appendix-base` skill to reflect new naming convention
- update `agentos-index/references/appendix.md`
- path: `notes/appendix/` → `skills/agentos-index-appendix-base/` → `skills/agentos-index/references/appendix.md`
- observable: appendix files follow `Concept.Name-appendix.md` convention; skill describes implicit discovery
- check: no numbered appendix files remain; skill references are consistent
- status: done

### Slice 5 — Wording revision and skill alignment

- revise "durable concept-note subsystem" wording in `000-index.md`, `100-index.md`, `001-ontology.md`
- update `agentos-index-writer` — `### index` handling → `### meta`
- update `agentos-index/references/block-syntax.md` — `### index` → `### meta`
- update `agentos-index` SKILL.md reference table
- path: index notes + affected skills
- observable: consistent terminology across index notes and skills
- check: grep for stale terms returns zero hits in `notes/index/` and `skills/`
- status: done

## Impl.Log

- 2026-05-15: Impl.Req created from design session 530, items 1-8
- 2026-05-15: Updated — block types reframed as `Kernel.Block:X` parameterizations with aliases in `### meta`; slice 2 rewritten
- 2026-05-15: Implementation complete — all 5 slices executed
    - Slice 1: `Kernel.Writing` and `Kernel.Block` added to `102-index.md` + ontology entries + routing
    - Slice 2: `Index.Block` → `Kernel.Block:Index`, `Index.Appendix.Block` → `Kernel.Block:Appendix`, `Design.Index.Block` → `Kernel.Block:Design.Session`; `Complete.Index.Block` and `Index.Block.Outlinks` removed; ontology entries updated
    - Slice 3: `Ontology.Registry`, `Ontology.Namespace`, `Index.Architecture`, `Agentos.Index` blocks added to `001-ontology.md`
    - Slice 4: appendix files renamed to `Concept.Name-appendix.md`; `agentos-index-appendix-base` and `agentos-index/references/appendix.md` rewritten for new convention
    - Slice 5: "durable concept-note subsystem" → Stable.Surface framing in index; `### index` → `### meta` in block-syntax and writer skills; reference table updated
