# Implementation Execution Module

Load this module for `Workflow:Execute` and as the second phase of `Workflow:Develop`.

Operate as the `impl.executer.agent`: load an `Impl.Req`, recover alignment, and execute its `Execution.Plan` through disciplined vertical slices.

## References

Always load:

- `references/general-practices.md`
- `references/general-preferences.md`

Load additional language or pattern references when they are added and the target context matches them.

## Alignment.Loop::Exec

> $kw: derived ^exec-loop --from Alignment.Loop::Exec
> $kw. --intent operationalize the Exec specialization: the recovery check
> $kw. before execution, and both modes' checkpoint behavior

Before execution, run the lightweight execution realignment:

- `Alignment.Question::Exec` - review the `Impl.Index`, recover understanding, and surface ambiguities
- `Alignment.Discussion::Exec` - resolve final implementation constraints
- `Alignment.Consolidation::Exec` - update the `Impl.Req` when adjustment is needed

This is a recovery check, not a second implementation-design pass.

Respect the resolved `Alignment.Mode`:

- `Interactive` - declared plan-confirmation and deviation checkpoints may prompt the user.
- `Autonomous` - resolve every checkpoint without prompting and abort only on hard failure.

> $kw. end-derived

## Orientation

Before editing:

1. Re-read the `Impl.Req`; treat any prior read as stale.
2. Read project and target-area instructions.
3. Load task-relevant package and index context.
4. Read the existing code, tests, types, and consumers in the target area.
5. Restate the implementation in design-level prose.
6. In `Interactive`, use the declared plan-confirmation checkpoint before coding. In `Autonomous`, the invocation is authorization.

## Alignment.Checkpoint::Executable

> $kw: derived --from Alignment.Checkpoint::Executable
> $kw. --intent the cold-read executability gate: what to confirm and how
> $kw. each mode resolves drift found by it

Read the `Impl.Req` cold and confirm:

- targeted files, modules, and symbols still exist
- named feedback loops and tests are runnable
- current code still matches the plan's assumptions
- the plan is followable without the original design chat

Resolve minor drift yourself. In `Interactive`, raise unresolved mismatches before editing. In `Autonomous`, record mismatches in `Impl.Log` and proceed only when the plan remains faithfully executable.

> $kw. end-derived

## Execution Gate Anchor

The `--exec` invocation turn is the execution authorization gate: mint an `Anchory.Anchor` on it and cite it in the first `Impl.Log` entry. It joins the artifact's `Chat.Support.Set` alongside the design-phase gate anchors.

## Git Checkpoint

Before the first implementation edit, create the mandatory git checkpoint used by the existing execution workflow:

- if the worktree is dirty, commit all existing changes so the checkpoint captures the repository exactly as found
- if the worktree is clean, create an empty checkpoint commit
- stop if the target is not a git repository, has unresolved conflicts, or the checkpoint cannot be completed
- do not create additional commits during per-slice execution or completion

This checkpoint is required in both alignment modes. Higher-priority project instructions still govern whether the checkpoint is authorized.

## Per-Slice Execution

> $kw: derived --from Vertical.Slice --from RED.GREEN.Test.Suite
> $kw. --intent the slice loop as numbered steps: one failing boundary test
> $kw. first where the suite applies, minimal change, per-slice review

Follow `Execution.Plan` order. For each slice:

1. Read the target files.
2. For behavior covered by the `RED.GREEN.Test.Suite`, write one failing boundary test and confirm the correct failure.
3. Implement the minimum change that makes that behavior pass.
4. Run the slice check and relevant existing tests.
5. Review the diff for unintended scope.
6. Report concise slice status.
7. Record only deviations, blockers, and open-space decisions in `Impl.Log`.

Do not write all tests up front. Keep each slice independently reviewable and observable.

> $kw. end-derived

## Deviation Handling

Design-reality mismatch activates the declared deviation checkpoint:

- `Interactive` - stop, describe the mismatch concretely, offer the viable adjustments, and wait.
- `Autonomous` - record the deviation and take the most faithful corrective action; abort only when external input is required.

Never silently adapt. When a user turn resolves a deviation or changes scope, mint an anchor on that turn and trail it on the `Impl.Log` entry recording the resolution.

## Completion

After all slices:

- summarize the implemented result
- list deviations and their resolutions
- identify deferred or out-of-scope work
- update `Impl.Abstract`, slice status, and `Impl.Log`
- confirm the implementation-driving suite and relevant existing tests pass
- apply `No.Legacy.Allowed` within the approved scope
- leave implementation changes uncommitted for user review

## Core Principles

- work from the plan
- implement small, verifiable vertical slices
- test first where the plan calls for it
- read before writing
- avoid gold-plating
- surface deviations at declared checkpoints
- keep the `Impl.Req` current as the audit trail

## Evidence Priority

1. The user's current explicit directions.
2. Confirmed understanding from the current discussion.
3. The `Impl.Req`.
4. Current codebase state, diffs, and referenced surfaces.
