> $kw: ^implementation-execute-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-skill-arg-contract

# Implementation.Execute.Workflow.Module

> $kw: --dev-from references/index-context-assembly.skw.md

Load this canonical workflow module for `--impl --execute` and as the second phase of `Implementation.Develop.Workflow.Module`.

Operate as the `impl.executer.agent`: load an `Impl.Req`, recover alignment, and execute its `Execution.Plan` through disciplined vertical slices.

## References

Always load:

- `references/impl/general-practices.md`
- `references/impl/general-preferences.md`
- `references/impl/product-capture.md`

Load additional language or pattern references when they are added and the target context matches them.

## Alignment.Loop::Exec

> $kw: ^exec-loop --derived --from Alignment.Loop::Exec
> --intent operationalize the Exec specialization: the recovery check
> --cont before execution, and both modes' checkpoint behavior

Before execution, run the lightweight execution realignment:

- `Alignment.Question::Exec` - review the `Impl.Index`, recover understanding, and surface ambiguities
- `Alignment.Discussion::Exec` - resolve final implementation constraints
- `Alignment.Consolidation::Exec` - update the `Impl.Req` when adjustment is needed

This is a recovery check, not a second implementation-design pass.

Respect the resolved `Alignment.Mode`:

- `Interactive` - declared plan-confirmation and deviation checkpoints may prompt the user.
- `Autonomous` - resolve every checkpoint without prompting and abort only on hard failure.

> $kw. end

## Orientation

Before editing:

1. Re-read the `Impl.Req`; treat any prior read as stale.
2. Read project and target-area instructions.
3. Load task-relevant package and index context.
4. Read the existing code, tests, types, and consumers in the target area.
5. Restate the implementation in design-level prose.
6. In `Interactive`, use the declared plan-confirmation checkpoint before coding. In `Autonomous`, the invocation is authorization.

## Alignment.Checkpoint::Executable

> $kw: --derived --from Alignment.Checkpoint::Executable
> --intent the cold-read executability gate: what to confirm and how
> --cont each mode resolves drift found by it

Read the `Impl.Req` cold and confirm:

- targeted files, modules, and symbols still exist
- named feedback loops and tests are runnable
- current code still matches the plan's assumptions
- the plan is followable without the original design chat

Resolve minor drift yourself. In `Interactive`, raise unresolved mismatches before editing. In `Autonomous`, record mismatches in `Impl.Log` and proceed only when the plan remains faithfully executable.

> $kw. end

## Execution Gate Line

The `--exec` invocation user message is the execution authorization gate. Record that fact as one typed, supported `Index.Line` in `Impl.Log`, using the normal Chatlas2 line-dossier path. `Impl.Log` is an `Index.Native.Surface`; do not add a `Skw.Annotation` wrapper.

## Git Checkpoint

Before the first implementation edit, create the mandatory git checkpoint used by the existing execution workflow:

- if the worktree is dirty, commit all existing changes so the checkpoint captures the repository exactly as found
- if the worktree is clean, create an empty checkpoint commit
- stop if the target is not a git repository, has unresolved conflicts, or the checkpoint cannot be completed
- do not create additional commits during per-slice execution or completion

This checkpoint is required in both alignment modes. Higher-priority project instructions still govern whether the checkpoint is authorized.

## Per-Slice Execution

> $kw: --derived --from Vertical.Slice --from RED.GREEN.Test.Suite --from Annotation.Point
> --intent the slice loop as numbered steps, with selective capture opening
> --cont and closing the verified product transaction

Follow `Execution.Plan` order. For each slice:

1. Read the target files.
2. **Slice.Open.Capture** — capture the typed, supported constraints that actually govern this slice into `Impl.Index`; do not assert product state yet.
3. For behavior covered by the `RED.GREEN.Test.Suite`, write one failing boundary test and confirm the correct failure.
4. Implement the minimum change that makes that behavior pass.
5. Run the slice check and relevant existing tests.
6. Review the diff for unintended scope.
7. **Product.Landing.Capture** — land only qualifying typed lines with the product edition: in `Skw.Annotation` on ordinary surfaces, directly on Index-native ones.
8. **Slice.Close.Capture** — audit the verified edition, finalize line dossiers, and run the shared `Index.HEAD.Backpropagation` batch.
9. Report concise slice and capture status, including retryable backpropagation gaps.
10. Record deviations, blockers, and consequential open-space presumptions in `Impl.Log`.

Do not write all tests up front. Keep each slice independently reviewable and observable. Do not mark a slice complete until its verified product edition has passed the close capture audit and its backpropagation was attempted.

> $kw. end

## Product.Surface Capture

> $kw: #touched-grounding --from Annotation.Authority --from Annotation.Point --from Skw.Network --from Skw.Address.Schema --from Open.Space --from Skw.Annotation
> --intent the executer's selective grounding discipline across native Index and ordinary Product surfaces

The executer grounds mostly against `Impl.Index` and the durable touched Index. It does not reconstruct previous chats. Understanding comes from the loaded conversation and artifact; Chatlas2 resolves only the exact user messages selected as support.

Capture has two product hosts:

- **`Index.Native.Surface`** — `Impl.Index` and `Impl.Log` carry typed `Index.Line`s directly.
- **ordinary `Product.Surface`** — code, tests, configuration, and documentation carry qualifying lines inside `Skw.Annotation`.

Attach at the coarsest `Annotation.Point` that honestly fits. A file point is available, but touching a file does not itself require an annotation. On each qualifying annotation:

- `--note`/`--supp ^anchor` carry typed, supported `Index.Line`s explaining why the product is as it is.
- `--from` carries the dependency, addressed by `Skw.Address.Schema`, in one of its two `Skw.Network` kinds: **structural** (the code derives from another surface — self-authorizing) or **touched** (an index block or annotation the code honors — carries `Annotation.Authority`). To link any point, fence it with a `Skw.Annotation` and reference its address.

Only direct material with ongoing maintenance value survives onto the product. Zero annotations is valid; never restate self-evident behavior or annotate for coverage.

Where a slice touches `Open.Space`, act provisionally and coherently. If the inference is consequential, surface it in chat and record a typed `Index.Presumption` in `Impl.Log`; otherwise leave it ordinary implementation detail. Never present it as touched authority.

## Deviation Handling

Design-reality mismatch activates the declared deviation checkpoint:

- `Interactive` - stop, describe the mismatch concretely, offer the viable adjustments, and wait.
- `Autonomous` - record the deviation and take the most faithful corrective action; abort only when external input is required.

Never silently adapt. When a user message resolves a deviation or changes scope, record the resolution as a typed, Chatlas2-supported `Index.Line` in `Impl.Log`.

## Completion

After all slices:

- run the final `Product.Surface` capture audit from `references/impl/product-capture.md`; an empty result is valid
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

> $kw: --from Alignment.Mode --from Impl.Req --from Index.Line --from Index.Presumption --from No.Legacy.Allowed --from Skw.Annotation
