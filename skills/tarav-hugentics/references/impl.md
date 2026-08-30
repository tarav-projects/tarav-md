# Implementation Workflow Router

This module routes `tarav-hugentics --impl` into one implementation workflow.
It preserves the former Hugentics implementation workflow while replacing the
legacy Index, Agendix, Anchory, and Chat.Index backend with the current Tarav2
Diagram.

## Input

Implementation input may be an idea, direct request, design artifact, supplied
context, or an existing live-note `Impl.Req`. `Alignment.Mode` is Interactive
unless `--auto` or `--autonomous` selects Autonomous operation.

At the start of every run, render one compact banner naming the resolved
implementation workflow, input, and Alignment.Mode.

## Routing

Resolve exactly one workflow:

1. An explicit selector or exact shortcut wins.
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

## Shared Contract

- The live-note `Impl.Req` is the durable design-to-execution handoff and main
  Agent coordination surface.
- `Impl.Req.Diagram` identifies the associated Project Model and
  `Impl.Req.Block`; it does not duplicate the Block's Lines.
- The Block contains only supported User-Touched material relevant to the
  request. Agent-only planning, status, reasoning, and logs remain in the live
  note or product surfaces.
- Preserve `Alignment.Mode` across composed phases.
- Keep designer and executer responsibilities distinct even when one Agent
  performs both.
- Re-read project instructions before editing and re-read the durable Impl.Req
  at every phase boundary.
- Every mutating implementation workflow composes implementation capture; it is
  a selective companion, not another phase.
- Validation and POIs never block Diagram capture. Hard implementation blockers
  may still stop product mutation when faithful execution is impossible.
