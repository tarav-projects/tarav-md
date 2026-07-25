# agentos-index --edit

> $kw: --from Capture.Offer --from Cited.Duplication --from Dotted.Notation --from Edition.Trigger.User.Gated --from Explicit.Namespace --from Index.Appendix --from Index.Chapter --from Index.Depot --from Index.Edit.Action --from Index.Edit.Modify.Line --from Index.Line --from Index.Ontology --from Kernel.Line --from Line.Type --from Name.As.Index --from User.Command --from Verbatim.User.Gated
> --dev-from references/index-capture-context-assembly.skw.md

The knowledge of writing Agentos index and appendix surfaces: gates, structure, naming, block quality, edit actions, and the landing procedure.

This module is a `Workflow.Neutral.Module`: it does not run a workflow — its rules bind whenever an index or appendix surface is written, whichever module has control. Workflow modules such as `references/capture.md`, `references/gr-review.md`, and `references/enrich.md` steer sessions and consume this knowledge.

`--edit`, `--write`, and `--append` all route here for direct edit work — a stale line to fix, a block to revise, an approved change to land. The context defines the edit action.

## Edit Gates

- index work is gated by `Edition.Trigger.User.Gated`
- wording-sensitive index-block work is also gated by `Verbatim.User.Gated`
- the agent may propose an edit path or draft, but must not land an index or appendix edit without explicit approval
- approval and landing are distinct acts: user approval accepts a form in chat; the write happens only on a landing trigger

## User.Command Transitions

- The declared `User.Command` transitions make the existing approval and landing gates explicit.
- `User.Command::Approve` (`::approve`, `::approved`) accepts the resolved draft exactly as shown, including its landing target, and records it as approved but unlanded.
- `User.Command::Land` (`::land`, `::write`) executes the `Landing Procedure` only for resolved approved material; it never supplies missing approval.
- `--write` invokes this skill module from a skill call. `::write` is a trigger inside an already-running workflow; the sigil keeps the two surfaces distinct.
- When a command target is not unique, ask for the target and do nothing. When approved wording or destination changes, invalidate that approval and require `User.Command::Approve` again.

## Structure

- depot router: `000-INDEX.md`
- public main surface: `Index.Ontology`
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
- place evidence links as trailing anchors inline on the lines they support (grounding is a line property, `Index.Line`) — anchors come from `references/link.md`

## Block Independence

> $kw: --derived
> --from Independent.Reader.Block
> --intent the section self-declares Cited.Duplication of the block: restate its
> --cont recoverable-cold / no-deixis / positive-statement / Name.As.Index lines
> --cont as the drafting checklist every index write enforces

`Cited.Duplication` of `[Independent.Reader.Block]` — the quality every drafted block must hold:

- a block must be recoverable cold by an independent reader holding only the block and the index it cites
- independence means independence from the writer's context, the producing conversation, and the block's position on the index surface
- inlining other concepts by `Dotted.Name` keeps independence — `Name.As.Index` anchors are durable and resolvable, not dependencies that break it
- what breaks independence is deixis: a reference whose meaning depends on the authoring context instead of on a named, resolvable concept
- the primary hazard is distilling a live conversation; strip the session's frame before committing
- define positively — say what the concept is, not what it is instead of
- extended depth belongs in `appendix/Independent.Reader.Block-appendix.md`

> $kw. end

## Edit Decision Mechanics

- use the context to choose the natural `Index.Edit.Action`
- create a block when the aligned content is a genuinely new named concept
- append a line when the content is a valuable point under an existing concept
- modify a line when an existing statement is wrong, stale, or imprecise
- revise a block when the current frame no longer holds its accumulated lines
- use `Index.Ontology` for routed fundamentals and `Index.Appendix` for tail, depth, history, scoped children, or loose but valuable material
- propose new lines typed (`- [CT] ...`); existing untyped lines are legacy, typed opportunistically on `Index.Edit.Modify.Line` or maintenance passes — never bulk-retyped inside an unrelated edit
- prefer the lowest-friction edit that captures the aligned content without losing meaning

## Drafting

When a draft is being shaped for an index or appendix surface — inside `references/capture.md`, a `Capture.Offer`, or direct edit work:

- show the landing target before the draft text; the user approves destination and wording together
- express the landing target as both file path and ontology location:
  - new block: `Landing: <file>` plus `Target: create block ## Concept.Name`
  - appended line: `Landing: <file>` plus `Target: append under ## Concept.Name`
  - modified line: `Landing: <file>` plus `Target: modify line under ## Concept.Name`
  - revised block: `Landing: <file>` plus `Target: revise block ## Concept.Name`
  - appendix material: `Landing: <appendix-file>` plus `Target: <Concept.Name>/<Section.Or.Child>`
  - grounding material: the exact inline line target the anchor will trail
- screen it for `Block Independence` — strip any deixis to the authoring conversation; state the concept positively
- screen each line's `Line.Type`: the line must perform its typed act (`references/type.md`); a line that takes no type belongs elsewhere — flag it, do not force a type
- review with the user and revise until accepted — acceptance is a chat state, not a write

Example approval screen:

```md
Landing: ~/projects/agentos-project/agentos-md/skills/agentos-pkg/design/107-design.md
Target: append under ## Capture.Offer

Draft:

- [DC] a capture offer shows its landing target before the proposed text, so the user approves destination and wording together ^<approval-anchor>
```

## Landing Procedure

When landing an approved edit:

1. Apply the approved edit to the natural surface.
2. Stamp grounding at landing: mint the approval-turn anchor (`references/link.md`) and set it as the trailing anchor on every landed line that has no more specific evidence turn — the fallback pointer per `Index.Line` grounding; line-specific turns win where they exist.
3. Update the router when concepts are added, renamed, moved, or gain appendix depth.
4. Run a linter check over the edited depot or explicit surfaces.

A cluster of edits approved together lands under one gate — the landing trigger covers the batch; each item's grounding still anchors its own approval turn.

## Capture.Offer Entry

- an accepted `Capture.Offer` is already drafted, typed, and landing-scouted; the user's destination pick (index main, appendix, agendix) sets the surface
- index main and appendix destinations land through the `Landing Procedure` above
- an offer routed to the agendix leaves this module: it lands through `references/agendix.md` rules (typed, anchored, trigger-gated)

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
