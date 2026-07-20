# End-To-End Development Module

Load this module only for `Workflow:Develop`.

Develop takes an idea or design source through implementation design and execution in one skill call.

## Workflow

> $kw: derived --from references/design.skw.md^how-loop --from references/execute.skw.md^exec-loop
> $kw. --intent the two-phase composition contract: design produces the
> $kw. Impl.Req, the exact artifact is re-read and passed into execution,
> $kw. one mode preserved across both phases

1. Load `references/design.md`.
2. Run `Alignment.Loop::How` with the resolved `Input` and `Alignment.Mode`.
3. Produce a complete `Impl.Req`.
4. Capture the exact artifact path and re-read it from disk.
5. Load `references/execute.md`.
6. Pass that exact `Impl.Req` into `Alignment.Loop::Exec`.
7. Execute its `Execution.Plan` using the same resolved `Alignment.Mode`.
8. Complete only after the artifact and implementation state are updated.

The phase transition remains inside the same skill invocation. An `Interactive` checkpoint may pause the call, but resumption continues the same develop workflow rather than requiring a new invocation.

> $kw. end-derived

## Boundary Contract

- The generated `Impl.Req` is the mandatory handoff between phases.
- Do not execute directly from the original idea or an in-chat summary.
- Do not collapse the `impl.designer.agent` and `impl.executer.agent` responsibilities.
- Re-read the artifact before execution so the executer receives a cold, durable handoff.
- Preserve the same `Alignment.Mode` across both phases.

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
