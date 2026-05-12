# Index Reindex — design-session

## Session.Abstract

- intent: rebuild the Agentos Index from scratch using `Index.Block.Syntax`, evolving the conceptual model along the way
- active focus: `Design.Session` concept family — file plan for 121, 122, 123
- references: `517-index-migration-protocol.md`, `513-The.Agentos.Index.md`, `skills/agentos-index/`, `skills/agentos-design-session/`
- state: active
- next: draft `121-Design.Session.md`

## Design.Index

### Index.Migration.Protocol

- `Index.Migration.Protocol` is the operational protocol for the index reindex process
- see `517-index-migration-protocol.md`

#### meta

- status: settled

### Index.Block.Findability

- `Index.Block.Findability` is a field in the `### index` section of an `Index.Block`
- populated only on evidence of search misses, not as a summary of the block content
- during initial block creation, findability should be empty by default

#### meta

- status: settled — promoted

### Reindex.Not.Migration

- this process is a reindex, not a strict migration
- the old index is one source for building the new — `513-The.Agentos.Index.md` is more current
- we do not need to keep the same layout, concept design, or groupings

#### meta

- status: settled

### No.Fixed.Authority.Hierarchy

- the old fixed authority chain (`Md.Surface` → `Canonical.Reference.Implementation` → other impls) is dropped
- when surfaces drift, it is a context-dependent judgment call
- the system aims for alignment, not authority

#### meta

- status: settled — promoted into `Stable.Surface` block

### Ontology.Granularity

- the ontology is a high-level concept map — not every sub-concept needs its own entry
- a parent concept is the entry point; sub-concepts are findable through the note

#### meta

- status: settled

### Stable.Surface.Equal.Authority

- all `Stable.Surfaces` have equal authority — no surface is more important than another
- the index is special in function but not in authority

#### meta

- status: settled — promoted into `100-Agentos.Surfaces.md`

### Context.Minimal.Surface

- `Context.Minimal.Surface` is the set of files from a project that agents must ALWAYS load at session start
- measurable — `Agentos.CLI` can compute total tokens and report breakdown
- creates a budget constraint and optimization feedback loop

#### appendix

Agents have finite context windows — what you preload matters. Too much = waste and unfocused agent. Too little = lost agent that keeps asking questions or making wrong assumptions.

The minimal surface is the "boot sequence" — what the agent loads before it can do anything useful. Keeping it small and high-signal is a maintenance concern.

For Agentos, the minimal surface would likely include: `AGENTS.md` files, `000-index.md`, `001-ontology.md`, `002-surfaces.md`.

Possible CLI: `agentos context minimal`, `agentos context minimal --size`, `agentos context minimal --budget <tokens>`.

#### meta

- status: working — captured in `522`, not yet promoted

### Agentos.Mission.Parked

- `Agentos.Mission` (old source 107) is parked — no longer relevant for the new index
- superseded by Iterante as the coordination layer

#### meta

- status: parked

### Design.Session.File.Plan

- `Design.Session` concept family will be indexed across three files:
  - `121-Design.Session.md` — container: `Design.Session`, sub-concepts: `User.Gated.Trigger`, `User.Gated.Writing`, `Session.Runtime.Loop` (`User.Assistant.Turn`, `Session.Maintenance.Turn`), `InChat.Design.Session`, `Artifact.Design.Session`
  - `122-Alignment.Space.md` — container: `Alignment.Space`, sub-concepts: `Design.Alignment.Core`, `Design.Open.Space`, `Delegation.Frontier`, `Alignment.Sufficiency`
  - `123-Impl.Req.md` — container: `Impl.Req`, sub-concepts: `Vertical.Slice`, `Deep.Modules`, `No.Legacy.Allowed`, (more later)
- old source `111-Design.Session.md` is architecturally stale but its alignment-state concepts are alive
- old Core.Design / TODO.Design split is dead
- `Design.Index` and `Design.Index.Block` stay in `114` — they are index-notes concepts, not Design.Session concepts

#### meta

- status: settled

### Index.Block.Body.Rationale

- if an example or code is in a block body, it's fundamental to understanding the concept
- the old 513 four-layer model (heading → fundamentals → extra → index section) is simplified to three layers (heading → body → sections)
- everything in the body is fundamental by definition — if it's not fundamental, it doesn't belong in the block

#### meta

- status: settled — promoted into `Index.Block` in `114`

## Session.Notes

- migration progress: source files 100-106 processed, 107 parked, 108-110 + 112-113 pending triage
- 111 (Design.Session) being reindexed as 121-123
- `--project-base` must be used with all `agentos stdlib prefix next` calls — discovered during session
- correct invocation: `agentos stdlib prefix next --project /Users/pereiro/projects/agentos-project/agentos-md --project-base agentos-md --target <target>`

## Session.Log

- bootstrapped migration: moved `notes/index/` → `notes/index-migration/`, created fresh index
- Tier 1 complete: `000-index.md`, `001-ontology.md`, `002-surfaces.md` reserved notes set up
- migrated source files: 100 (Index.Notes), 101 (Md.Surface), 102 (Dotted.Notation), 103 (File.Numbering), 104 (Maintenance), 105 (Project), 106 (Skills)
- new concepts emerged during migration: `Natural.Placement`, `Placement.Balance`, `Index.Concept.Coverage`, `Index.Block.Outlinks`, `Context.Minimal.Surface`
- design pivot: old SSOT model dropped in favor of `Stable.Surface.Equal.Authority`
- design pivot: reframed migration as reindex — old index is one source, not the template
- upgraded to `Artifact.Session`
- updated artifact structure: `Session.Index` → `Design.Index`, `Session.Docs` removed, blocks converted to `Design.Index.Block` format
- parked `Agentos.Mission` (107) — superseded by Iterante
- settled file plan for Design.Session concept family: 121 (Design.Session), 122 (Alignment.Space), 123 (Impl.Req)
