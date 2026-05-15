# Index Flat Migration - impl-req

## Impl.Abstract

- **scope:** migrate all concept blocks from semantic index files to flat anonymous files; update routing in 000-index.md; retire semantic files
- **status:** ready for implementation
- **source:** design session `notes/live/530-index-system-revisit-design-session.md` — flat index architecture decision
- **constraint:** no concept loss — every block that exists today must exist after migration
- **dependency:** execute BEFORE 531 (conceptual changes) — 531 operates on the new flat structure

## Impl.Index

### Flat.Index.Architecture

- index concept files become flat anonymous containers: `100-index.md`, `101-index.md`, ...
- file names carry no semantic meaning — the number is just a stable handle
- ~20 concept blocks per file — hard cap
- writing always appends to the last file
- splitting overfull files is maintenance, not a writing concern
- `000-index.md` is the concept→file routing table — always loaded by agents
- `001-ontology.md` stays as-is — the ontology entry point is not affected by this migration
- `002-surfaces.md` stays as-is

### Migration.Principle

- move blocks, don't rewrite them — content stays verbatim
- update `000-index.md` to map every concept to its new file
- the old semantic file groupings become candidates for future Ontology.Namespaces (not created in this pass)
- reserved files (`000`, `001`, `002`) are not touched

## Execution.Plan

### Slice 1 — Create flat files and move blocks from semantic files

- create `100-index.md` through `103-index.md` (or as many as needed)
- move all concept blocks from the 13 semantic files (`100-127`) into flat files, ~20 per file
- preserve block content verbatim — no edits to block text
- ordering within files: append in the order encountered (no semantic grouping)
- path: `notes/index/1*.md` → `notes/index/100-index.md` ... `103-index.md`
- observable: all concept blocks exist in flat files
- check: count of H2 blocks in new files matches count in old files
- status: not started

### Slice 2 — Update 000-index.md routing table

- rewrite `000-index.md` to map every concept name to its new flat file
- remove references to old semantic file names
- path: `notes/index/000-index.md`
- observable: every concept in the index has a routing entry
- check: every H2 heading in flat files has a corresponding entry in `000-index.md`
- status: not started

### Slice 3 — Retire semantic files

- delete the old semantic files (`100-Agentos.Surfaces.md`, `114-Agentos.Index.Notes.md`, etc.)
- verify no broken references remain in `000-index.md`, `001-ontology.md`, or `002-surfaces.md`
- path: `notes/index/`
- observable: only `000-index.md`, `001-ontology.md`, `002-surfaces.md`, and `1XX-index.md` flat files remain
- check: no references to retired filenames in remaining index files
- status: not started

### Slice 4 — Update ontology entries that reference old filenames

- scan `001-ontology.md` for "see `1XX-*.md`" references pointing to retired semantic files
- update to point to the new flat file where the block now lives
- path: `notes/index/001-ontology.md`
- observable: all "see" references in ontology resolve to existing files
- check: grep for retired filenames returns zero hits
- status: not started

## Impl.Log

- 2026-05-15: Impl.Req created — flat index migration, prerequisite for 531
