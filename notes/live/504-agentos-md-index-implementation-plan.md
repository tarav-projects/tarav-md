# Agentos-md Index Implementation Plan

Working plan for implementing the closed Agentos index-notes design session into the `agentos-md` index surface.

## Status

- `notes/live/501-agentos-index-notes-design-session.md` is closed.
- The design session is now a read-only evidence artifact.
- The implementation target is `notes/index/`.
- New durable design decisions should be written into index notes, not back into the closed session.
- Follow-up tasks that are not durable design truth should be parked in `notes/live/010.TODOS.md`.

## Goal

Make `notes/index/` the active `Design.Target.Model:Agentos` surface for the Agentos markdown implementation.

This means the closed design-session concepts should become stable index notes, registry entries, or explicit stubs. The session can remain as provenance, but it should no longer be the main source people or agents read to understand the design.

## Working Principles

- Build the new SSOT before cleaning legacy material.
- Promote durable concepts from the session into stable index notes.
- Keep migrated legacy notes available until their durable signal has been reviewed.
- Prefer small coherent passes over one large rewrite.
- Preserve low-friction capture while converging toward `Index.Note.Style`.
- Treat mismatch as consolidation debt, not failure.

## Pass 1: Target Index Skeleton

Create the first stable index structure.

Expected outputs:

- `notes/index/ontology.md` as the low-resolution ontology registry.
- First core concept notes, likely in the `100-499` range.
- Updated `notes/index/000-index.md` routing to the new stable notes.

Initial high-value notes:

- `Agentos.Index.Notes`
- `Md.Surface`
- `Dotted.Notation`
- `File.Numbering.Protocol`
- `Maintenance.System`

## Pass 2: Promote Closed Session Concepts

Compress closed design-session concepts into index-note style.

For each concept:

- write a compact definition
- preserve rationale and boundaries
- include rules and examples when they guide future work
- add related concepts
- add or update ontology registry entry
- link back to the closed session only as provenance when useful

The session artifact should not be updated during this pass.

## Pass 3: Reconcile Migrated Legacy Index

Review `notes/live/migrated-agentos-index/`.

For each migrated note or block:

- promote durable material into the new index
- mark superseded assumptions by omission or explicit replacement in new notes
- keep unresolved but valuable material as migration debt
- avoid deleting legacy material until its signal has been reviewed

The goal is to stop using migrated legacy notes as active authority.

## Pass 4: Align Derived Markdown Surfaces

After the new index is usable, update derived surfaces.

Relevant surfaces:

- `skills/`
- `AGENTS.md`
- `notes/live/`
- `notes/dev/` when introduced
- other markdown coordination files

Rule:

- derived surfaces may explain usage or development behavior
- durable design truth should point back to `notes/index/`
- if a derived surface contains independent design truth, promote or reference it from the index

## Pass 5: Drift And Cleanup Passes

Run repeated checks for remaining mismatch.

Check for:

- stale `agentos` repo paths
- legacy concept names
- duplicated definitions
- durable design rules outside `notes/index/`
- missing ontology registry entries
- broken index routing
- unclassified migrated notes

Each issue should produce one of:

- index-note update
- registry update
- TODO
- explicit legacy classification
- later cleanup task

## Completion Direction

The migration is sufficiently complete when:

- the current Agentos design can be understood from `notes/index/`
- the ontology registry gives a useful low-resolution map of the concept surface
- the closed design session is provenance, not required reading
- migrated legacy notes are no longer treated as active SSOT
- skills and other markdown surfaces derive from or route to the index for durable design truth
