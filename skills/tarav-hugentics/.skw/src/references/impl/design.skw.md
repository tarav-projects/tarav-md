> $kw: ^implementation-design-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^hugentics-batchy-runtime-contract
> --loading-dep SKILL.skw.md^hugentics-skill-arg-contract

# Implementation.Design.Workflow.Module

> $kw: --dev-from references/index-context-assembly.skw.md

Load this canonical workflow module for `--impl --design` and as the first phase of `Implementation.Develop.Workflow.Module`.

Operate as the `impl.designer.agent`: inspect the implementation context, design an implementation path, and produce an `Impl.Req` artifact.

## Alignment.Loop::How

> $kw: ^how-loop --derived --from Alignment.Loop::How --from Alignment.Loop
> --intent operationalize the How specialization of the loop as
> --cont designer instructions: the three moves and the continue-until bar

Run the `How.Design` specialization of `Alignment.Loop`:

- `Alignment.Question::How` - drive toward implementation design and enrich the `Impl.Index` with `Hard.Evidence`
- `Alignment.Discussion::How` - resolve implementation concerns
- `Alignment.Consolidation::How` - write or update the `Impl.Req`

Continue until the implementation design is sufficiently aligned for execution.

> $kw. end

## Alignment.Mode

> $kw: --derived --from Alignment.Mode
> --intent the mode contract scoped to design-phase checkpoints:
> --cont what Interactive prompts on, what Autonomous records instead

Respect the mode resolved by the driver:

- `Interactive` - use declared checkpoints as alignment opportunities and raise unresolved needs to the user.
- `Autonomous` - resolve checkpoints without prompting, produce the `Impl.Req` as the audit trail, and abort only on hard failure.

At a design-reality deviation:

- `Interactive` - stop at the declared checkpoint and ask.
- `Autonomous` - record the deviation in `Impl.Index` or `Impl.Log` and continue with the most faithful action.

> $kw. end

## Alignment.Checkpoint::Readiness

> $kw: --derived --from Alignment.Checkpoint::Readiness
> --intent the checkpoint as the pre-write gate list an agent runs
> --cont immediately before writing the Impl.Req; keep the no-padding rule

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

> $kw. end

## Impl.Req Artifact

An `Impl.Req` is the implementation-request artifact passed from design to execution.

### Structure

> $kw: --derived --from Impl.Req
> --intent the artifact's four parts as a compact list a designer
> --cont fills; keep the reevaluation duty on the abstract

- `Impl.Abstract` - scope, status, and source context; reevaluate it after each design change
- `Impl.Index` - implementation design alignment as `Design.Index.Blocks`
- `Execution.Plan` - ordered vertical slices, checks, risks, deviation triggers, acceptance signals, and slice status
- `Impl.Log` - deviations, blockers, and decisions made in open space

> $kw. end

### Location

- use a filename ending in `-impl-req.md`
- store it in `notes/live/`
- use `tarav-live-surfaces` for location and numbering

### Writing

> $kw: --derived --from Impl.Req --from Vertical.Slice --from RED.GREEN.Test.Suite
> --intent the writing rules: cold-reader orientation, references over
> --cont pasted code, ordered independently-checkable slices, RED-GREEN where it applies

- write for an implementer who did not see the design discussion
- preserve the user's accepted intent
- prefer references to files, notes, commands, and surfaces over pasted code
- shape implementation without overspecifying incidental implementation detail
- use ordered `Vertical.Slice`s
- make each slice independently observable and checkable
- include RED-then-GREEN behavior tests where the `RED.GREEN.Test.Suite` applies

The caller's explicit `--design` or `--develop` invocation authorizes writing the artifact. Do not write an `Impl.Req` from passive orientation alone.

See `references/impl/example.md` for a concrete artifact sample.

> $kw. end

### Impl.Agendix

> $kw: --from Annotation.Authority --from Skw.Network --from Skw.Address.Schema --from Skw.Annotation --from Open.Space
> --intent the living grounding reservoir on the Impl.Req: what it is,
> --cont the designer's before/after dual-level capture, and the record-by-kind rule

The `Impl.Req` carries a living **`Impl.Agendix`**: the touched-authority reservoir the implementation grounds against. It accumulates ungated, the way the index agendix does, and is never the durable home of what it holds — durable grounding survives on the code, not here (see `references/impl/execute.md`). The `Impl.Agendix` is the working reservoir the executer both consumes and extends.

The designer captures into it **twice, bracketing the write** — before, from the design chat that shaped the plan; after, grounding the produced artifact. Because it holds the design chat live, the designer grounds at **both levels**:

- **chat → touched**: use `tarav chatlas2 anchory support` to mint generic message-support anchors on the user messages that authorize and shape the plan — the ordering request, readiness approval, and each message that settles a `Design.Decisions` line. These records have no Index-line attachment or review gate.
- **index → touched**: cite the index blocks the implementation must honor, each addressed by its `Skw.Address.Schema`.

Record every dependency by its `Skw.Network` kind:

- **structural** — the surface is derived or copied from another surface; self-authorizing, no grounding needed (the derivation is the evidence).
- **touched** — a link to a touched index block or user `Chat.Message.Ref` carrying a decision; it carries `Annotation.Authority`, and each `--from` addresses another annotation by its `Skw.Address.Schema` — to link any point, fence it with a `Skw.Annotation` and reference its address.

Discipline:

- every written anchor and address must resolve — wildcard or unresolvable citations are worse than none.
- in `Autonomous` mode the invocation turn is the coarse gate; one anchor may cover the artifact, with finer touches anchored as they settle.
- where the plan reaches territory with no index home, that is `Open.Space` — leave it provisional and unanchored, never a logged gap.

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

Exit with the complete `Impl.Req` path and a concise readiness summary. Under `Implementation.Develop.Workflow.Module`, return control to `references/impl/develop.md` instead of ending the overall skill.

> $kw: --from Hard.Evidence
