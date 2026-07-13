# Implementation Design Module

Load this module for `Workflow:Design` and as the first phase of `Workflow:Develop`.

Operate as the `impl.designer.agent`: inspect the implementation context, design an implementation path, and produce an `Impl.Req` artifact.

## Alignment.Loop::How

> $kw: derived ^how-loop --from Alignment.Loop::How --from Alignment.Loop
> $kw. --intent operationalize the How specialization of the loop as
> $kw. designer instructions: the three moves and the continue-until bar

Run the `How.Design` specialization of `Alignment.Loop`:

- `Alignment.Question::How` - drive toward implementation design and enrich the `Impl.Index` with `Hard.Evidence`
- `Alignment.Discussion::How` - resolve implementation concerns
- `Alignment.Consolidation::How` - write or update the `Impl.Req`

Continue until the implementation design is sufficiently aligned for execution.

> $kw. end-derived

## Alignment.Mode

> $kw: derived --from Alignment.Mode
> $kw. --intent the mode contract scoped to design-phase checkpoints:
> $kw. what Interactive prompts on, what Autonomous records instead

Respect the mode resolved by the driver:

- `Interactive` - use declared checkpoints as alignment opportunities and raise unresolved needs to the user.
- `Autonomous` - resolve checkpoints without prompting, produce the `Impl.Req` as the audit trail, and abort only on hard failure.

At a design-reality deviation:

- `Interactive` - stop at the declared checkpoint and ask.
- `Autonomous` - record the deviation in `Impl.Index` or `Impl.Log` and continue with the most faithful action.

> $kw. end-derived

## Alignment.Checkpoint::Readiness

> $kw: derived --from Alignment.Checkpoint::Readiness
> $kw. --intent the checkpoint as the pre-write gate list an agent runs
> $kw. immediately before writing the Impl.Req; keep the no-padding rule

Immediately before writing the `Impl.Req`, confirm:

- scope and out-of-scope are explicit
- current state was inspected and cited
- every slice has an observable result and a check
- feedback loops and `RED.GREEN.Test.Suite` behaviors are named
- dependencies and ordering are explicit
- no unresolved decision is hidden inside an execution step
- the plan is understandable without chat context

Close each gap yourself where possible. In `Interactive`, raise unresolved gaps and wait. In `Autonomous`, resolve them and record any conscious waiver.

Do not pad the artifact merely to satisfy the readiness check.

> $kw. end-derived

## Impl.Req Artifact

An `Impl.Req` is the implementation-request artifact passed from design to execution.

### Structure

> $kw: derived --from Impl.Req
> $kw. --intent the artifact's four parts as a compact list a designer
> $kw. fills; keep the reevaluation duty on the abstract

- `Impl.Abstract` - scope, status, and source context; reevaluate it after each design change
- `Impl.Index` - implementation design alignment as `Design.Index.Blocks`
- `Execution.Plan` - ordered vertical slices, checks, risks, deviation triggers, acceptance signals, and slice status
- `Impl.Log` - deviations, blockers, and decisions made in open space

> $kw. end-derived

### Location

- use a filename ending in `-impl-req.md`
- store it in `notes/live/`
- use `agentos-live-surfaces` for location and numbering

### Writing

> $kw: derived --from Impl.Req --from Vertical.Slice --from RED.GREEN.Test.Suite
> $kw. --intent the writing rules: cold-reader orientation, references over
> $kw. pasted code, ordered independently-checkable slices, RED-GREEN where it applies

- write for an implementer who did not see the design discussion
- preserve the user's accepted intent
- prefer references to files, notes, commands, and surfaces over pasted code
- shape implementation without overspecifying incidental implementation detail
- use ordered `Vertical.Slice`s
- make each slice independently observable and checkable
- include RED-then-GREEN behavior tests where the `RED.GREEN.Test.Suite` applies

The caller's explicit `--design` or `--develop` invocation authorizes writing the artifact. Do not write an `Impl.Req` from passive orientation alone.

See `references/example.md` for a concrete artifact sample.

> $kw. end-derived

## Updating And Feedback

- prefer focused updates over full rewrites
- update `Impl.Abstract` when the implementation request changes
- keep ordinary code changes out of `Impl.Log`; the diff already records them
- when implementation design exposes a fundamentals-design problem, note it in the artifact and identify the source design surface that may need revision
- for realignment work, state the observed drift and corrective request explicitly

## Evidence Priority

1. The user's current explicit directions.
2. Confirmed understanding from the current discussion.
3. The source design artifact or context.
4. Current codebase state, diffs, and referenced surfaces.

## Output

Exit with the complete `Impl.Req` path and a concise readiness summary. Under `Workflow:Develop`, return control to `references/develop.md` instead of ending the overall skill.
