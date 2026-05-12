# Index Migration — 2026-05-11

Migration session notes for the `Agentos.Index` rebuild.
Protocol: `517-index-migration-protocol.md`

---

## Index.Block.Findability

- `Index.Block.Findability` is a field in the `### index` section of an `Index.Block`
- populated only when there is evidence of search misses — not as a summary of the block content
- typical evidence: the user calls the block using an unexpected context or name
- during initial block creation, findability should be empty by default
- the block body itself is the primary search surface — findability is a supplementary hint for known gaps

****

## Reindex.Not.Migration

- this process is a reindex, not a strict migration
- the old index is one source for building the new — not the template
- `notes/live/513-The.Agentos.Index.md` is a more current source for the index's own conceptual model
- we do not need to keep the same layout, concept design, or groupings from the old index
- the old "SSOT/derive from index" model is outdated
    - now there are `Stable.Surfaces`, each authoritative for its own slice
    - the index is specifically for conceptual mapping, not the single source of truth for all project knowledge

****

## No.Fixed.Authority.Hierarchy

- the old model had a fixed authority chain: `Md.Surface` → `Canonical.Reference.Implementation` → other implementations
- this is dropped — there is no fixed hierarchy where markdown always wins
- when surfaces drift (index vs code vs skills), it is a context-dependent judgment call
    - sometimes the index is stale, sometimes the codebase, sometimes the skills
    - the user decides, or the agent if prompted
- the system aims for alignment across surfaces, not authority of one over another

****

## Resolved: Index.Block link-out rule

- captured in `Index.Block` and `Index.Block.Outlinks` blocks in `114-Agentos.Index.Notes.md`

****

## Ontology.Granularity

- the ontology is a high-level concept map — not every sub-concept needs its own ontology entry
- a parent concept (e.g. `Agentos.Skills`) is the entry point in the ontology
- sub-concepts (e.g. `Skill.Source`, `Skill.Profile`) are findable through the note, not individually listed in the ontology
- the ontology links to the note; the note contains all the blocks

****

## Index.As.Concept.Registry

- the index is the collection point for all `Named.Concepts` in the `Stable.Md.Surface` of a project
- any `Dotted.Name` that appears anywhere in a stable surface should have an index entry
- the index is not the place for all documentation — it is curated, efficient, first-line agent context
- each concept block must carry enough signal for an agent to reason correctly, not just a pointer
- documentation lives wherever it naturally fits — authors write freely and use `Dotted.Notation` for concepts
- the system detects `Dotted.Names` from any surface and triggers index updates
- ergonomic write path: write freely anywhere → use `Dotted.Notation` → system detects → index captures the concept

****

## Stable.Surface.Equal.Authority

- all `Stable.Surfaces` have equal authority — no surface is positioned as more important than another
- the index is special in function (concept mapping, first-line agent context) but not in authority
- misalignments between surfaces are resolved context-dependently, not by a fixed hierarchy
- the system must be aligned — drift is a problem to solve, not a hierarchy to invoke
