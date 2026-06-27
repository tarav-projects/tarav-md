# agentos-index --write

Use this module when the user has approved an index or appendix edit.

Drafting or revising block wording is also `--write` work, even before the user has approved a file mutation.

## Write Gates

- index work is gated by `Write.Trigger.Gated`
- wording-sensitive index-block work is also gated by `Content.Verbatim.Gated`
- the agent may propose a write path or draft, but must not commit an index or appendix edit without explicit approval

## Structure

- public routing table: `index/000-index.md`
- public flat files: `index/100-index.md`, `101-index.md`, ...
- public appendix files: `appendix/Concept.Name-appendix.md`
- local routing table: `notes/index/001-index.md`
- local flat files: `notes/index/300-index.md`, `301-index.md`, ...

## Naming And Placement

- name concepts in `Dotted.Notation`
- check overlap before creating a new concept
- place conceptual fundamentals in the index
- place extended depth, grounded history, scoped views, specs, and parked depth in the appendix
- place operational procedure in skills or references, not in the index

## Write Loop

1. Propose a full new block or a focused diff.
2. Review with the user.
3. Revise until accepted.
4. Commit the approved edit to the natural surface.
5. Update the router when concepts are added, renamed, moved, or gain appendix depth.

## Post-Write Maintenance

- update the routing table when the concept inventory changed
- add or update appendix route annotations when appendix depth changed
- update namespace membership in `### meta` when the concept belongs to an `Explicit.Namespace`
- check cited duplicates and related stable mentions when editing an existing concept

## Quality References

- load `agentos-pkg/references/index-block-catalog.md` before proposing new block wording or revising existing block wording
- use `agentos-pkg/references/index-block-catalog.md` for concrete block-quality calibration
- use the `agentos-pkg` index and appendix for the underlying design concepts that govern writing
