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

## Execution Gate Anchor

The `--exec` invocation user message is the execution authorization gate: mint a generic Chatlas2 message-support anchor with `tarav chatlas2 anchory support` and cite it in the first `Impl.Log` entry. It has no Index-line attachment and is not a line-dossier review gate merely because it authorizes execution.

## Git Checkpoint

Before the first implementation edit, create the mandatory git checkpoint used by the existing execution workflow:

- if the worktree is dirty, commit all existing changes so the checkpoint captures the repository exactly as found
- if the worktree is clean, create an empty checkpoint commit
- stop if the target is not a git repository, has unresolved conflicts, or the checkpoint cannot be completed
- do not create additional commits during per-slice execution or completion

This checkpoint is required in both alignment modes. Higher-priority project instructions still govern whether the checkpoint is authorized.

## Per-Slice Execution

> $kw: --derived --from Vertical.Slice --from RED.GREEN.Test.Suite --from Annotation.Point
> --intent the slice loop as numbered steps, with grounding bracketing the
> --cont implementation: ground-before to follow directives, ground-after to annotate and gap-check

Follow `Execution.Plan` order. For each slice:

1. Read the target files.
2. **Ground before** — ground the slice against the index, pulling the touched blocks and directives it must honor (see `## Touched.Index Grounding`), so the code follows them.
3. For behavior covered by the `RED.GREEN.Test.Suite`, write one failing boundary test and confirm the correct failure.
4. Implement the minimum change that makes that behavior pass.
5. Run the slice check and relevant existing tests.
6. Review the diff for unintended scope.
7. **Ground after** — embed the touched lines as `Skw.Annotation`s at the code's `Annotation.Point`s and extend the `Impl.Agendix`; gap-check (see `## Touched.Index Grounding`).
8. Report concise slice status.
9. Record only deviations, blockers, and open-space decisions in `Impl.Log`.

Do not write all tests up front. Keep each slice independently reviewable and observable. The grounding steps bracket the implementation; they do not alter the slice, test-first, or minimal-change discipline between them.

> $kw. end

## Touched.Index Grounding

> $kw: #touched-grounding --from Annotation.Authority --from Annotation.Point --from Skw.Network --from Skw.Address.Schema --from Open.Space --from Skw.Annotation
> --intent the executer's grounding discipline: the index-first cost model, the
> --cont two destinations, where annotations attach, and Open.Space for ungrounded territory

The executer grounds mostly against the **index** — durable and cheap to read. It does **not** reconstruct previous chats. It mints generic Chatlas2 message-support anchors only on its own live exec-session user messages and reads the `Impl.Agendix` the designer seeded for prior chat grounding.

Grounding a slice has **two destinations**:

- the **`Impl.Agendix`** — the unstable working reservoir; extend it as execution touches new index material.
- the **code** — the implementation produces `Skw.Annotation`-annotated surfaces, embedded at the code's `Annotation.Point`s. This is where grounding **survives**; the reservoir is not the final home.

Attach at the **coarsest `Annotation.Point` that honestly fits**: the file is the universal floor — give every touched file a file-level `Skw.Annotation` — with finer function or section points only where the annotation's true scope needs them. On each annotation:

- `--note`/`--supp ^anchor` carry the grounding — *why* the code is as it is.
- `--from` carries the dependency, addressed by `Skw.Address.Schema`, in one of its two `Skw.Network` kinds: **structural** (the code derives from another surface — self-authorizing) or **touched** (an index block or annotation the code honors — carries `Annotation.Authority`). To link any point, fence it with a `Skw.Annotation` and reference its address.

Only touched material with ongoing maintenance value survives onto code; one-time decisions die with the `Impl.Agendix`. Per `Annotation.Authority`, only the file point is open to ungated agentic annotation — finer points are born touched.

Where a slice touches territory with no index home, that is **`Open.Space`**: act provisionally and coherently, embed nothing authoritative, and log nothing. It becomes a directive constraint only once touched.

## Deviation Handling

Design-reality mismatch activates the declared deviation checkpoint:

- `Interactive` - stop, describe the mismatch concretely, offer the viable adjustments, and wait.
- `Autonomous` - record the deviation and take the most faithful corrective action; abort only when external input is required.

Never silently adapt. When a user message resolves a deviation or changes scope, mint a generic Chatlas2 message-support anchor on it and trail it on the `Impl.Log` entry recording the resolution.

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

> $kw: --from Alignment.Mode --from Impl.Req --from No.Legacy.Allowed
