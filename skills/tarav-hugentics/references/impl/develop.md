# Implementation.Develop.Workflow.Module

Load this canonical workflow module only for `--impl --develop` or one of its exact shortcuts.

Develop takes an idea or design source through implementation design and execution in one skill call.

Load `references/impl/product-capture.md` once and preserve its capture state across the design-to-execution handoff.

## Workflow

1. Load `references/impl/design.md`.
2. Run `Alignment.Loop::How` with the resolved `Input` and `Alignment.Mode`, converging on an implementation path for the runnable product surfaces.
3. Produce a complete `Impl.Req`.
4. Capture the exact artifact path and re-read it from disk.
5. Load `references/impl/execute.md`.
6. Pass that exact `Impl.Req` into `Alignment.Loop::Exec`.
7. Execute its `Execution.Plan` using the same resolved `Alignment.Mode`.
8. Complete only after the artifact and implementation state are verified, the final Product.Surface audit is complete, and the resulting capture manifest was landed or its retryable gaps were reported.

The phase transition remains inside the same skill invocation. An `Interactive` checkpoint may pause the call, but resumption continues the same develop workflow rather than requiring a new invocation.

## Boundary Contract

- The generated `Impl.Req` is the mandatory handoff between phases.
- Do not execute directly from the original idea or an in-chat summary.
- Do not collapse the `impl.designer.agent` and `impl.executer.agent` responsibilities.
- Re-read the artifact before execution so the executer receives a cold, durable handoff.
- Preserve the same `Alignment.Mode` across both phases.
- Preserve exact support and capture state across the phase boundary; do not replace it with a summary.

## Failure Behavior

- If implementation design cannot produce an executable `Impl.Req`, stop before execution.
- If the executable check finds hard drift, follow the selected mode's checkpoint behavior.
- If execution fails, preserve the `Impl.Req` and record the blocker in `Impl.Log`.

## Completion

Return one concise report covering:

- the generated `Impl.Req` path
- the implemented result
- verification performed
- deviations, blockers, or deferred work
