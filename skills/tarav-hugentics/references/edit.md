# Index.Landing.Knowledge.Module

The knowledge of writing Agentos index and appendix surfaces: gates, structure, naming, block quality, edit actions, and the landing procedure.

This module is a `Workflow.Neutral.Module`: it does not run a workflow — its rules bind whenever an index or appendix surface is written, whichever module has control. Workflow modules such as `references/capture.md`, plus `tarav-pkg --index-retrofit`, steer sessions and consume this knowledge.

`--edit`, `--write`, and `--append` all route here for direct edit work — a stale line to fix, a block to revise, an approved change to land. The context defines the edit action.

## Edit Gates

- index work is gated by `Edition.Trigger.User.Gated`
- wording-sensitive index-block work is also gated by `Verbatim.User.Gated`
- the agent may propose an edit path or draft, but must not land an index or appendix edit without explicit approval
- approval and landing are distinct acts: user approval accepts a form in chat; the write happens only on a landing trigger

## User.Command Transitions

- The declared `User.Command` transitions make the existing approval and landing gates explicit.
- `User.Command::Approve` (`::approve`, `::approved`) accepts the resolved presented edition, including its landing target, and records it as approved but unlanded.
- `::approve <token>` binds approval to materially equivalent content presented with that `Edition.Approval.Token`. Index workflows require this form; a bare approval remains representable as semantic edit-event approval but does not satisfy the line gate.
- `User.Command::Land` (`::land`, `::write`) executes the `Landing Procedure` only for resolved approved material; it never supplies missing approval.
- `User.Command::LandAllApproved` (`::land-all-approved`) executes the `Landing Procedure` for the complete approved, unlanded cluster of one foreground index workflow; it takes no target argument and never supplies missing approval.
- `--write` invokes this skill module from a skill call. `::write` is a trigger inside an already-running workflow; the sigil keeps the two surfaces distinct.
- When a command target is not unique, ask for the target and do nothing. When `::land-all-approved` has no unique foreground workflow, ask for the workflow and do nothing. When approved wording or destination changes, invalidate that approval and require `User.Command::Approve` again.

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
- place each line's `Support.Set` as a trailing anchor inline on the line it supports (grounding is a line property, `Index.Line`) — anchors come from the internal `Real.Time.Grounding.Knowledge.Module` in `references/link.md`

## Block Independence

`Cited.Duplication` of `[Independent.Reader.Block]` — the quality every drafted block must hold:

- a block must be recoverable cold by an independent reader holding only the block and the index it cites
- independence means independence from the writer's context, the producing conversation, and the block's position on the index surface
- inlining other concepts by `Dotted.Name` keeps independence — `Name.As.Index` anchors are durable and resolvable, not dependencies that break it
- what breaks independence is deixis: a reference whose meaning depends on the authoring context instead of on a named, resolvable concept
- the primary hazard is distilling a live conversation; strip the session's frame before committing
- define positively — say what the concept is, not what it is instead of
- extended depth belongs in `tarav-pkg/appendix/Independent.Reader.Block-appendix.md`

## Edit Decision Mechanics

- use the context to choose the natural `Index.Edit.Action`
- treat a `POI.Instance` as an attention signal, not a prescribed edit
- create a block when the aligned content is a genuinely new named concept
- append a line when the content is a valuable point under an existing concept
- modify a line when an existing statement is wrong, stale, or imprecise
- revise a block when the current frame no longer holds its accumulated lines
- reconciliation may also keep, ground, replace, remove, reorganize, demote, or deliberately leave current material unresolved
- do not turn a `Live.Index.Line` into `Demoted.Index.Line` merely because newer evidence contradicts it; demotion occurs only when a gated reconciliation retires its live standing
- an ungrounded live line remains relevant through `Index.Presumption`; missing support is grounding debt rather than deletion authority
- use `Index.Ontology` for routed fundamentals and `Index.Appendix` for tail, depth, history, scoped children, or loose but valuable material
- propose new lines typed (`- [CT] ...`); existing untyped lines are legacy, typed opportunistically on `Index.Edit.Modify.Line` or maintenance passes — never bulk-retyped inside an unrelated edit
- prefer the lowest-friction edit that captures the aligned content without losing meaning

## Drafting

When a draft is being shaped for an index or appendix surface — inside `references/capture.md`, a `Capture.Offer`, or direct edit work — render an `Index.Edition.Turn`:

- show the landing target and edit operation before the proposed content
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
- for modifications, show `Before` and `After · Verbatim`; additions need only proposed content and removals need only current content
- place every proposed landing line undecorated somewhere in the turn; presentation layout is not gate syntax
- do not resolve support or allocate a new anchor while the proposal remains open to revision
- when the proposed rendering needs to mark the future trailing anchor, use `^<anchor-on-landing>`; it is an inert landing placeholder, not an allocated support reference
- mint a fresh opaque `Edition.Approval.Token` for the proposal and show it with the proposed landing content
- rotate the token when materially significant wording or the landing destination changes; spacing, wrapping, capitalization, and presentation layout alone do not spend another attention checkpoint

Example approval screen:

```md
Landing: ~/projects/agentos-project/agentos-md/skills/tarav-pkg/design/107-design.md
Target: append under ## Capture.Offer

After · Verbatim:

- [DC] a capture offer shows its landing target before the proposed text, so the user approves destination and wording together ^<anchor-on-landing>

Approval:

`::approve idx-edition:7d2f91c4`
```

## Landing Procedure

When landing an approved edit:

Support resolution begins only after both gates have been crossed: the final proposal has token approval and a landing command has selected it. Do not run this procedure while wording or destination remains open to revision.

1. Resolve the final agent proposal and user approval as exact Chatlas2 `Chat.Message.Ref` assertions.
2. Locate and qualify the substantive user messages that support each approved line's claim.
3. Confirm that the approval message qualifies under the current chat `Touch.Authority.Surface` protocol.
4. Author one `Capture.Manifest`. Put qualifying user messages in `support`; record token, agent proposal, and user approval independently under `gates.tokenized_verbatim_approval`. Use structured message identity fields and `expect.contains_all`; omit `side`, which the relationship role determines.
5. Run `tarav index capture preview --project <root> --manifest <capture.json>` and inspect the exact planned editions. Any manifest or evidence defect stops before stable writes.
6. Run the corresponding `land` command. It mints anchors, applies every approved source edit, creates its `LineRecord`, backpropagates Chat.Index, and runs the final exact audit. The support relationship grounds the claim; the gate relationship independently makes the line eligible for `Reviewed.Content`.
7. Update the router when concepts are added, renamed, moved, or gain appendix depth.
8. Run `Real.Time.Validation.Knowledge.Module` over the landing report and escalate only failed exact items.
9. Re-run `Touched.Decision.Cycle` contextualization over the changed live cut and report any remaining POIs separately from the completed edit.

The opt-in material-equivalence check implements `Line.Verbatim.Gate`.

A cluster of edits approved together lands under one gate — the landing trigger covers the batch; each item still resolves its own substantive support and approval evidence.

## Capture.Offer Entry

- an accepted `Capture.Offer` is already drafted, typed, and landing-scouted; the user's destination pick (index main, appendix, agendix) sets the surface
- index main and appendix destinations land through the `Landing Procedure` above
- an offer routed to the agendix leaves this module: it lands through `references/agendix.md` rules (typed, anchored, trigger-gated)

## Post-Edit Maintenance

- update the router when the concept inventory changed
- add or update appendix route annotations when appendix depth changed
- update namespace membership in `### meta` when the concept belongs to an `Explicit.Namespace`
- check cited duplicates and related stable mentions when editing an existing concept
- run `Real.Time.Validation.Knowledge.Module` after the primary landing and before Chat.Index backpropagation
- use repeated `--anchor` selectors so validation remains bounded to the exact newly landed editions

## Quality References

- load `tarav-pkg/references/index-block-catalog.md` before proposing new block wording or revising existing block wording
- load `references/type.md` before drafting or judging `Kernel.Line`s — a line is drafted as an act: pick its `Line.Type` first, then word the line to pass that type's validation point
- use `tarav-pkg/references/index-block-catalog.md` for concrete block-quality calibration
- use the `tarav-pkg` index and appendix for the underlying design concepts that govern editing
