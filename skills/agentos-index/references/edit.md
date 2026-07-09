# agentos-index --edit

Use this module when the user has approved an index or appendix edit.

Drafting or revising block wording is also edit work, even before the user has approved a file mutation.

`--edit`, `--write`, and `--append` all call this module. The context defines the edit action.

## Edit Gates

- index work is gated by `Edit.Trigger.Gated`
- wording-sensitive index-block work is also gated by `Content.Verbatim.Gated`
- the agent may propose an edit path or draft, but must not commit an index or appendix edit without explicit approval

## Structure

- depot router: `000-INDEX.md`
- public main surface: `Index.Main`
- public chapter files: `<chapter>/NNN-<chapter>.md`, defaulting to `design/NNN-design.md`
- public appendix depth: shared `Index.Appendix` files under `appendix/Concept.Name-appendix.md`
- local index: an `Index.Depot` with the same structure, differing only in location — rooted in the project rather than inside a shippable skill bundle
- local surfaces mirror the public ones: `notes/index/000-INDEX.md` router, `<chapter>/NNN-<chapter>.md` chapter files, `appendix/` depth
- `--depot` scopes edits to engaged `Index.Depot`s; otherwise use task-relevant engaged depots
- `--chapter` scopes main-surface edits to an `Index.Chapter`; default is `design`

## Naming And Placement

- name concepts in `Dotted.Notation`
- check overlap before creating a new concept
- place conceptual fundamentals in the index
- place extended depth, grounded history, scoped views, specs, and parked depth in the appendix
- place operational procedure in skills or references, not in the index
- place evidence links in grounding surfaces: `[GR]` lines in the appendix `Concept.X/Grounding.Head` block (demotions to `Concept.X/Grounding.Drift`), or a trailing anchor inline on the line it supports — anchors come from `references/link.md`

## Block Independence

`Cited.Duplication` of `[Independent.Reader.Block]` — the quality every drafted block must hold:

- a block must be recoverable cold by an independent reader holding only the block and the index it cites
- no deixis to the authoring conversation: no "the new model", "as discussed", "the thing the user wants" — the reader meets the block cold, without the session that produced it
- define positively — say what the concept is, not what it is instead of a rejected alternative
- inlining other concepts by `Dotted.Name` keeps independence — `Name.As.Index` anchors are resolvable, not dependencies that break it
- the primary hazard is distilling a live conversation; strip the session's frame before committing

## Edit Decision Mechanics

- use the context to choose the natural `Index.Edit.Action`
- create a block when the aligned content is a genuinely new named concept
- append a line when the content is a valuable point under an existing concept
- modify a line when an existing statement is wrong, stale, or imprecise
- revise a block when the current frame no longer holds its accumulated lines
- use `Index.Main` for routed fundamentals and `Index.Appendix` for tail, depth, history, scoped children, or loose but valuable material
- propose new lines typed (`- [CT] ...`); existing untyped lines are legacy, typed opportunistically on `Index.Edit.Modify.Line` or maintenance passes — never bulk-retyped inside an unrelated edit
- prefer the lowest-friction edit that captures the aligned content without losing meaning

## Capture.Offer Entry

- an accepted `Capture.Offer` enters the loop below at step 3 — the draft already exists, typed and landing-scouted; the user's destination pick (index main, appendix, agendix) sets the surface
- an offer routed to the agendix leaves this module: it lands through `references/agendix.md` rules (typed, anchored, ungated)

## Edit Loop

1. Propose a full new block or a focused diff.
2. Screen it for `Block Independence` — strip any deixis to the authoring conversation; state the concept positively. Screen each line's `Line.Type`: the line must perform its typed act (`references/type.md`); a line that takes no type belongs elsewhere — flag it, do not force a type.
3. Review with the user.
4. Revise until accepted.
5. Apply the approved edit to the natural surface.
6. Stamp grounding at landing: mint the approval-turn anchor (`references/link.md`) and set it as the trailing anchor on every landed line that has no more specific evidence turn — the fallback pointer per `Inline.Grounding`; line-specific turns win where they exist.
7. Update the router when concepts are added, renamed, moved, or gain appendix depth.
8. Run a linter check over the edited depot or explicit surfaces.

## Post-Edit Maintenance

- update the router when the concept inventory changed
- add or update appendix route annotations when appendix depth changed
- update namespace membership in `### meta` when the concept belongs to an `Explicit.Namespace`
- check cited duplicates and related stable mentions when editing an existing concept
- run `agentos index linter --depot <depot>` after depot edits, or explicit `--index` / `--appendix` checks when the edit is scoped to individual surfaces

## Quality References

- load `agentos-pkg/references/index-block-catalog.md` before proposing new block wording or revising existing block wording
- load `references/type.md` before drafting or judging `Kernel.Line`s — a line is drafted as an act: pick its `Line.Type` first, then word the line to pass that type's validation point
- use `agentos-pkg/references/index-block-catalog.md` for concrete block-quality calibration
- use the `agentos-pkg` index and appendix for the underlying design concepts that govern editing
