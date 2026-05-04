# Agentos.Index.Notes - draft

Draft of the future stable index note for `Agentos.Index.Notes`.

---

## What It Is

- `Agentos.Index.Notes` is the durable concept-note system for Agentos projects.
- It stores knowledge that should shape future judgment:
  - high-signal concepts
  - rationale
  - constraints
  - naming conventions
  - reusable patterns
  - steering decisions
- It is broader than a spec system.
  - Some index notes may behave like specs.
  - The index also holds principles, ontology entries, design concepts, exclusions, and durable coordination knowledge.

## Core Purpose

- `Agentos.Index.Notes` must maximize durable capture while continuously improving toward curated coherence.
- First priority: preserve important knowledge where future agents and humans can find it.
- Second priority: refine that knowledge into a clearer, smaller, better connected concept surface.
- Captured material may need later note-level review:
  - reformatting
  - relocation
  - deduplication
  - naming cleanup
  - registry and index-link updates

## High-Signal Surface

- The index is a high-signal surface, not general documentation.
- Include material that changes future judgment:
  - durable concepts
  - design rationale
  - architectural constraints
  - naming conventions
  - reusable patterns
  - steering decisions
  - explicit exclusions or "not this" boundaries
- Avoid material that is:
  - transient
  - easily derived from code
  - useful only as status reporting

## Low-Friction Capture

- The path from idea to durable storage should have low friction.
- Useful material may enter the index before it has the desired stable shape.
- Acceptable temporary forms include:
  - rough note
  - essay
  - partial concept
  - awkward placement
  - incomplete synthesis
- The threshold is importance: preserve the information when it is important enough to guide future work.
- Putting material in the index makes it reviewable.
  - Review exposes duplication, misalignment, weak naming, missing concepts, and unclear boundaries.
  - Later maintenance can refactor the material toward a better shape.

## Desired Outcome

- `Index.Note.Style` is a `Desired.Outcome`, not an admission gate.
- Agentos can define a clear target shape for mature index notes while still accepting work-in-progress content.
- The system should remain usable while it evolves.
- Maintenance should move the surface toward the desired outcome over time.

## Relationship To Other Surfaces

- `Agentos.Index.Notes` is distinct from other Agentos writing surfaces.
- `notes/live/` captures active design work, session state, and in-progress thinking.
- Structured artifacts capture specific outcomes such as design summaries, implementation requests, or issue reports.
- Skills package reusable agent behavior and operational workflows.
- Docs explain usage for human readers.
- Code is the implementation reality.
- Index notes preserve the durable concepts and constraints that should guide judgment across those surfaces.

## Index.Note

- `Index.Note` is a durable note inside the index surface.
- A stable index note usually defines:
  - one important concept, or
  - one tightly related concept cluster
- A stable index note should make these clear:
  - what the concept is
  - why it matters
  - what boundaries apply
  - what consequences follow
- Some index files have special roles.
  - `Index.md.Note` or `000-index.md` is an index note for routing and orientation.
  - Its job is not deep concept definition.

## Index.Block

- `Index.Block` is the index-specific use of the more general `Md.Block` primitive.
- An `Index.Block` is a high-signal heading-scoped section that carries one steering idea.
- Common block payloads:
  - definition
  - constraint
  - rationale
  - pattern
  - boundary
  - consequence
  - anti-pattern
- Files organize reading; blocks carry meaning.

## Ontology Awareness

- `Agentos.Index.Notes` is concept-driven.
- Dotted notation signals named concepts.
- `Ontology.Registry` curates the current concept surface by listing:
  - registered names
  - one-paragraph definitions
  - references to fuller notes when they exist
- Dedicated notes expand concepts that need more than registry treatment.
- Agents should consult the registry when concept identity matters:
  - during design discussions
  - when the user uses dotted notation
  - when an approximate name should be mapped to the registered name

## Maintenance

- Index quality improves through maintenance.
- Maintenance passes can:
  - consolidate rough notes into stable concept notes
  - detect unregistered dotted names
  - update stale registry references
  - find likely duplicates or renamed concepts
  - improve index routing
  - move material between files when discoverability improves
- The index is expected to evolve.
- Incomplete shape is acceptable when the material is valuable.
- Permanent neglect is not the desired outcome.

## What This Is Not

- `Agentos.Index.Notes` is not:
  - a transcript store
  - a changelog
  - a generic documentation folder
  - a task tracker
  - a progress tracking surface
  - a code-level implementation dump
  - a requirement that every thought be formalized before being written

## Open Design Dependencies

- `Agentos.Index.Writing.Principles` should define the writing philosophy in more detail.
- `Index.Note.Style` should define the desired stable note shape.
- `Agentos.Index.Ontology.Registry` should define registry structure and concept inventory behavior.
- `Agentos.Ontology.Workflows` should define concept lifecycle and agent behaviors around ontology navigation.
- `Agentos.Maintenance.System` should define how index-note checks hook into broader maintenance.
- `Agentos.Index.Structure` should define index layout, `000-index.md`, placement, and routing.

## Style Loss Check

- Preserved:
  - durable concept-note system definition
  - broader-than-spec framing
  - durable capture plus curated coherence purpose
  - high-signal and low-friction principles
  - `Desired.Outcome` relationship
  - relationships to live notes, artifacts, skills, docs, and code
  - `Index.Note` and special index note roles
  - ontology registry awareness
  - maintenance role
  - exclusions and open design dependencies
- Added:
  - explicit `Index.Block` section
  - "files organize reading; blocks carry meaning"
- Intentionally changed:
  - compressed explanatory prose into block-structured bullets
  - made repeated concepts more scannable for style testing
- Lost information:
  - none identified
