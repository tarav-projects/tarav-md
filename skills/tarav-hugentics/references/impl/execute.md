# Implementation Execute Workflow

Load this module for `--impl --execute` and as Develop's second phase. Also load
[`product-capture.md`](product-capture.md),
[`general-practices.md`](general-practices.md), and
[`general-preferences.md`](general-preferences.md).

Operate as the implementation executer: cold-load one live-note `Impl.Req`,
recover its User-Touched context through `Impl.Req.Diagram`, and execute its
`Execution.Plan` through verified vertical slices. When explicit Execute input
does not resolve to an existing Impl.Req, perform Direct-Input Bootstrap first.

## Direct-Input Bootstrap

An explicit `--execute` or `--exec` may carry direct implementation input. It
still requires the same two Impl.Req surfaces as any other execution:

1. Run the ordinary capture Contextualize path from
   [`../capture.md`](../capture.md): resolve the current chat, Project Diagram
   configuration, Project.Model, current Model context, and Object.Type
   registry.
2. Through one ordinary automatic Capture.Manifest, introduce exactly one
   `Impl.Req.Block` and capture the qualifying User-Touched requirements from
   the direct request into that Block.
3. Create the live-note Impl.Req with the resulting Namespace, Model ship,
   Block ship, and an executable plan.
4. Cold-reload both surfaces and continue with Execution Realignment.

This is not a reduced implementation-specific bootstrap. It is regular
capture with `Block.Type: Impl.Req.Block` fixed as the target. Never mint or
record Diagram identities without a successful landing, and never treat the
live note as a substitute for that landing.

If shared capture is unavailable, report a capture POI and mark the live note's
`Impl.Req.Diagram` incomplete. Foreground implementation may continue when the
request remains executable, but implementation capture remains explicitly
unreconciled.

## Execution Realignment

After any Direct-Input Bootstrap, and before editing:

1. Re-read the Impl.Req from disk; treat any prior read as stale.
2. Read project and target-area instructions.
3. Resolve the Project Model and exact `Impl.Req.Block` recorded by
   `Impl.Req.Diagram`.
4. Contextualize from that Block and expand support when a Line is ambiguous,
   disputed, or consequential.
5. Inspect the current code, tests, types, consumers, and worktree.
6. Restate the implementation in design-level prose.

Confirm that targets still exist, checks are runnable, current reality still
fits the plan, and the request remains followable without its design chat.
Resolve minor drift yourself. At a material mismatch, Interactive mode pauses
for alignment; Autonomous mode records the deviation and proceeds only when a
faithful corrective path remains.

The Execute invocation is the User's execution authorization. Capture that
User touch into the same `Impl.Req.Block` as the request's current execution
standing; do not store an unsupported Agent paraphrase.

## Git Checkpoint

Before the first product edit, create the workflow's recoverable Git
checkpoint:

- commit all existing changes when the worktree is dirty;
- create an empty checkpoint commit when it is clean;
- stop for unresolved conflicts, a non-Git target, or an impossible
  checkpoint; and
- create no additional automatic commits during slice execution or completion.

Project instructions or a narrower User instruction may override this
workflow-owned checkpoint behavior.

## Per-Slice Execution

Follow `Execution.Plan` order. For each vertical slice:

1. Read the exact target surfaces.
2. Run **Slice.Open.Capture** from the shared capture module.
3. Where the plan calls for boundary-first testing, establish the expected
   failing behavior.
4. Implement the minimum coherent change.
5. Run the slice check and relevant existing tests.
6. Review the diff for unintended scope.
7. Run **Product.Landing.Capture** and **Slice.Close.Capture**.
8. Update slice status and consequential coordination facts in the live note.
9. Report concise product, verification, capture, and POI status.

Do not write all tests up front. Keep every slice independently observable and
reviewable. Diagram capture failure does not invalidate successful product
work; report it as a retryable POI. Product verification failure does prevent
the slice from being presented as complete.

## Deviation Handling

Never silently adapt to design-reality mismatch.

- Interactive mode describes the mismatch and viable adjustments, then waits
  at the declared checkpoint.
- Autonomous mode records the deviation in `Impl.Log`, takes the most faithful
  available path, and stops only when external input is required.

When the User resolves a deviation or changes scope, update the live note and
capture the supported consequence into the same `Impl.Req.Block`. Agent-only
observations remain in `Impl.Log` unless another Diagram Annotation type and
evidence policy explicitly owns them.

## Completion

After all slices:

- run the final Product.Surface and Impl.Req.Diagram audit;
- confirm the implementation-driving checks and relevant existing tests pass;
- update `Impl.Abstract`, slice statuses, and `Impl.Log`;
- summarize the result, deviations, blockers, and deferred work;
- report the associated Block and outstanding POIs; and
- leave post-checkpoint implementation changes uncommitted for User review.
