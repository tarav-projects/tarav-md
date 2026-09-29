# Implementation Workflow Router

This module routes `tarav-hugentics --impl` into one implementation workflow.
It preserves the former Hugentics implementation workflow while replacing the
legacy Index, Agendix, Anchory, and Chat.Index backend with the current Tarav
Diagram.

## Input

Implementation input may be an idea, direct request, design artifact, supplied
context, or an existing live-note `Impl.Req`. `Alignment.Mode` is Interactive
unless `--auto` or `--autonomous` selects Autonomous operation.

At the start of every run, render one compact banner naming the resolved
implementation workflow, input, and Alignment.Mode.

### Impact input

`--impact` selects the actionable implementation delta from recent design in
the current chat. A trailing value narrows that discussion; it is not an
Impl.Req path or a general artifact selector. Load
[`design-impact.md`](design-impact.md) and perform its Scope and Assessment
steps against current code before starting the selected implementation phase.
Reuse recent assessment evidence when still current; inspect changed surfaces
before treating an earlier conclusion as the present delta.

Carry the supported design, affected surfaces, required changes, and unresolved
decisions into the selected workflow as direct input. Preserve distinctions
between requirements and suggestions. Already aligned behavior requires no
implementation work. If no actionable delta remains, report that and stop
without creating empty implementation artifacts. If the design target itself
is ambiguous, clarify it; do not invent implementation work.

The selector does not add a phase, execution permission, or an approval gate:

- `--impl --impact` and `--impl --design --impact` select Design.
- `--impl --dev --impact` and `--impl --develop --impact` select Develop.
- Explicit Execute with `--impact` receives direct input and follows its
  ordinary Direct-Input Bootstrap.

Keep the selected workflow's alignment, capture, and mutation boundaries.
Impact input does not satisfy Review's requirement for an existing Impl.Req;
ask for that artifact if Review was selected rather than synthesizing one.

## Routing

Select the knowledge surface before applying the phase rules below.
New requests default to Wiki; `--model` explicitly selects Model-backed work.
Resume existing notes on their recorded surface; legacy Impl.Req.Diagram
means Model-backed. Reject combined `--wiki` and `--model` selectors.
For Wiki selection (default, explicit `--wiki`, or retained Wiki surface),
load [`impl/wiki.md`](impl/wiki.md) and stop routing through this module.
The remaining phase modules and shared contract here are Model-backed.
For new Model-backed notes, record `Knowledge.Surface: model` alongside
Impl.Req.Diagram. An ambiguous existing note requires clarification.
Wiki notes use `Impl.Req.Wiki` instead of `Impl.Req.Diagram`; recognize
either as a request when accompanied by Impl.Abstract, Execution.Plan, and
Impl.Log. Reject an explicit surface that conflicts with the retained note.

Resolve exactly one workflow:

1. An explicit selector or exact shortcut wins.
   `--dev` is an alias of `--develop`, including after `--impl`.
2. Bare `--impl` contributes only the implementation namespace.
3. `--impl --capture` contributes the shared implementation-capture module; it
   does not independently select Design, Execute, or Develop.
4. An existing `Impl.Req` defaults to Execute.
5. Other actionable implementation input defaults to Design.
6. Develop, Review, and Harvest are never inferred; they require their explicit
   selectors.
7. If there is neither input nor actionable context, orient to the available
   workflows and stop.

Load only the selected module:

- Design: [`impl/design.md`](impl/design.md)
- Review: [`impl/review.md`](impl/review.md)
- Execute: [`impl/execute.md`](impl/execute.md)
- Develop: [`impl/develop.md`](impl/develop.md)
- Harvest: [`impl/harvest.md`](impl/harvest.md)
- shared implementation capture: [`impl/product-capture.md`](impl/product-capture.md)

Treat input as an `Impl.Req` when a path, note number, or supplied artifact
resolves to a live note containing `Impl.Abstract`, `Impl.Req.Diagram`,
`Execution.Plan`, and `Impl.Log`.

An explicit Execute selector may receive direct implementation input. In that
case Execute first grounds the Project Model and bootstraps the missing live
note, `Impl.Req.Collection`, and durable `Diagram.Draft`; it must not pretend
the direct prompt was an already materialized Impl.Req.

## Shared Contract

- The live-note `Impl.Req` is the durable design-to-execution handoff and main
  Agent coordination surface.
- Name new implementation-request live notes
  `<number>-<descriptive-name>-impl-req.md` under the product's notes/live/.
  Follow its numbering convention; preserve existing filenames on resume.
- `Impl.Req.Diagram` identifies the Project Model, one
  `Impl.Req.Collection`, and one durable `Diagram.Draft`.
- Ground or refresh the `Diagram.View` before deciding whether candidate Lines
  continue existing Blocks or require a new Block.
- The Collection hosts implementation-specific editions; their semantic Block
  attachment remains independent from that organizational host.
- Agent-only planning, status, reasoning, and logs remain in the live note or
  product surfaces.
- Preserve `Alignment.Mode` across composed phases.
- Keep designer and executer responsibilities distinct even when one Agent
  performs both.
- Re-read project instructions before editing and re-read the durable Impl.Req
  at every phase boundary.
- Every mutating implementation workflow composes implementation capture; it is
  a selective companion, not another phase.
- Implementation capture uses the complete ordinary Capture path but writes
  into the request's Draft throughout execution. Reconcile that Draft across
  slices and apply it once when the request closes.
- The mutating invocation supplies a `Capture.Authorization.Gate`; it does not
  manufacture wording review.
- A Closed Impl.Req is a bounded historical edition. Later ordinary writes
  produce lifecycle POIs unless it is validly reopened inside its window.
- A live note may record a capture failure for recovery, but it never satisfies
  or replaces the `Impl.Req.Diagram` contract.
- Validation and POIs never block Diagram capture. Hard implementation blockers
  may still stop product mutation when faithful execution is impossible.
