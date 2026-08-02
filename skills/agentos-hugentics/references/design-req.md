# Design.Req.Knowledge.Module

`Design.Req.Knowledge.Module` is the `Workflow.Neutral` contract for using a `Design.Req` as the durable target of `Hugentic.Capture.Workflow.Module`, which operationalizes `Hugentic.Capture.Workflow`. It owns the artifact boundary, writing model, lifecycle, and promotion rules; it does not create another conversation mode or workflow.

`--design` routes to `Hugentic.Capture.Workflow.Module` and loads this module as target knowledge. Conversation, aliases, and defaults may resolve the same module through `Batchy.Router` without creating another module identity.

## When To Use

Use a `Design.Req` when design work is large, unstable, important enough to maintain durably, likely to need handoff, or explicitly requested as a live artifact.

Keep small exploratory work in conversation until durable maintenance becomes useful. Conversation is flexible working state; it is not a second backend and does not override the maintained artifact.

## Artifact Contract

Use one live note by default:

```txt
NNN-timetag-design-req.md
```

Store it under the owning project's `notes/live/` according to `agentos-live-surfaces` guidance.

```md
# [Short Title] - design-req

status: Open

## Session.Abstract

## Design.Index

## Session.Notes

## Session.Log
```

The required status field has only two values: `Open` and `Closed`.

- The `Session.Abstract` section states the target, current concern, settled frame, and next useful move.
- The `Design.Index` section holds compact concept-shaped design state in `Design.Index.Block` form.
- The `Session.Notes` section holds unresolved questions, provisional material, and work that must not disappear in chat.
- The `Session.Log` section records meaningful lifecycle events, approvals, promotions, and deviations; it is not a transcript.

## Design Writing

- Write settled design as `Design.Block`s in `Kernel.Writing`: orthogonal fundamentals first, then only useful depth.
- Keep rationale, examples, pressure tests, tradeoffs, and rejected alternatives adjacent to the concept they explain.
- Keep session mechanics and open items explicit without mixing them into settled fundamentals.
- Preserve negative decisions when they prevent future ambiguity.
- Ground material direction, warnings, and readiness claims in `Hard.Evidence`.
- Update only the affected blocks and sections; do not rewrite the full artifact for a local change.
- Do not turn the request into a transcript, progress diary, or wall of prose.

## Capture Behavior

`Hugentic.Capture.Workflow.Module` owns the conversational loop. With this knowledge module loaded, it should:

1. Resolve an existing `Design.Req` or propose one when durable state is warranted.
2. Ground the active concern against touched design and adjacent evidence.
3. Work one highest-leverage unresolved concern at a time unless the user is driving another thread.
4. Respond as a design partner: propose, critique, reframe, pressure-test, and name meaningful tradeoffs.
5. Keep the maintained artifact aligned with settled discussion while it is open and active.
6. Use the capture gate and `Edition.Trigger.User.Gated` for every creation, update, promotion record, reopen, and close transition.

Each material design decision applies `Touched.Decision.Cycle`: contextualize against touched constraints, act through the open region, then reconcile maintained state.

Feedback, critique, and continuation prompts continue the current discussion. They do not implicitly request implementation, artifact mutation, status reporting, or the next design question.

When the user requests capture or consolidation, propose what should change, where it should land, and why. Do not write until the applicable user gate resolves.

## Maintenance And Closure

- While `status: Open` and the workflow is active, continuously evaluate the delta between conversation and the maintained request.
- Before workflow completion, update settled design, approvals, promotions, unresolved material, and meaningful lifecycle events.
- Only after that maintenance pass may the workflow offer closure.
- Changing `status` to `Closed` is user-gated.
- A closed request may be reopened through a user-gated change to `Open`.
- Every reopened lifecycle repeats maintenance before closure; never restore a stale prior state after an interruption.

No additional status machine is required. The agent evaluates the artifact and live conversation directly.

## Promotion

`Design.Req.Promotion` is a first-class interruption of the active capture workflow. It temporarily changes the target; it does not start a second alignment workflow.

- The agent may propose approved content for the Index, an `Impl.Req`, or both.
- Already-approved verbatim may be reused as a proposal, but every destination keeps its own landing gate.
- The typical path is Index first, implementation later, so durable design truth and the product surface remain aligned.
- Promotion may use a bounded approved cluster or other approved material resolved from the request and conversation.
- On completion, maintain the source `Design.Req` with what landed, what remains approved or open, and any resulting next concern.
- Return to the maintained current state, never to a stale pre-interruption snapshot.

## Implementation Fork

When stable design is ready for implementation, route through the Implementation namespace:

```text
--impl --design
```

This selects `Implementation.Design.Workflow.Module`, which creates or updates an `Impl.Req`. Prefer promoting stable design into the Index before the implementation fork unless the user deliberately chooses another order.

## Split Rule

Prefer one `Design.Req` for one design lifecycle. Propose another only when length, target, audience, or lifecycle genuinely separates the work, such as one thread being ready to close while another remains exploratory.

Do not split merely because the request contains several concepts or sections.

## Status And Read-Only Capture

- `Workflow.Status.Operation.Module` reports maintained artifact state and uncommitted conversational delta.
- `--capture --audit` uses `Hugentic.Capture.Workflow.Module` read-only to find converged material that remains upstream of its appropriate durable surface.

These are routed capabilities, not Design.Req submodules.
