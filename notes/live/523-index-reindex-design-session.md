# Index Reindex — design-session

## Session.Abstract

- intent: rebuild the Agentos Index from scratch using `Index.Block.Syntax`, evolving the conceptual model along the way
- active focus: Tier 3 migration (continuing with `107-Agentos.Mission.md`) + surface design concepts
- references: `517-index-migration-protocol.md`, `513-The.Agentos.Index.md`, `skills/agentos-index/`
- state: active
- next: continue migration from `107-Agentos.Mission.md`, capture `Context.Minimal.Surface`

## Session.Index

### Index.Migration.Protocol

- `Index.Migration.Protocol` is the operational protocol for the index reindex process
- see `517-index-migration-protocol.md`
- status: settled

### Index.Block.Findability

- `Index.Block.Findability` is a field in the `### index` section of an `Index.Block`
- populated only on evidence of search misses, not as a summary of the block content
- during initial block creation, findability should be empty by default
- status: settled — promoted

### Reindex.Not.Migration

- this process is a reindex, not a strict migration
- the old index is one source for building the new — `513-The.Agentos.Index.md` is more current
- we do not need to keep the same layout, concept design, or groupings
- status: settled

### No.Fixed.Authority.Hierarchy

- the old fixed authority chain (`Md.Surface` → `Canonical.Reference.Implementation` → other impls) is dropped
- when surfaces drift, it is a context-dependent judgment call
- the system aims for alignment, not authority
- status: settled — promoted into `Stable.Surface` block

### Ontology.Granularity

- the ontology is a high-level concept map — not every sub-concept needs its own entry
- a parent concept is the entry point; sub-concepts are findable through the note
- status: settled

### Stable.Surface.Equal.Authority

- all `Stable.Surfaces` have equal authority — no surface is more important than another
- the index is special in function but not in authority
- status: settled — promoted into `100-Agentos.Surfaces.md`

### Context.Minimal.Surface

- `Context.Minimal.Surface` is the set of files from a project that agents must ALWAYS load at session start
- measurable — `Agentos.CLI` can compute total tokens and report breakdown
- creates a budget constraint and optimization feedback loop
- status: working — captured in `522`, not yet promoted

## Session.Docs

(to discuss)

## Session.Notes

- migration progress: source files 100-106 processed, 107-113 pending
- `--project-base` must be used with all `agentos stdlib prefix next` calls — discovered during session
- correct invocation: `agentos stdlib prefix next --project /Users/pereiro/projects/agentos-project/agentos-md --project-base agentos-md --target <target>`
- `Agentos.Mission` block was proposed but not yet approved (interrupted by surface design discussion)

## Session.Log

- bootstrapped migration: moved `notes/index/` → `notes/index-migration/`, created fresh index
- Tier 1 complete: `000-index.md`, `001-ontology.md`, `002-surfaces.md` reserved notes set up
- migrated source files: 100 (Index.Notes), 101 (Md.Surface), 102 (Dotted.Notation), 103 (File.Numbering), 104 (Maintenance), 105 (Project), 106 (Skills)
- new concepts emerged during migration: `Natural.Placement`, `Placement.Balance`, `Index.Concept.Coverage`, `Index.Block.Outlinks`, `Context.Minimal.Surface`
- design pivot: old SSOT model dropped in favor of `Stable.Surface.Equal.Authority`
- design pivot: reframed migration as reindex — old index is one source, not the template
- upgraded to `Artifact.Session`
