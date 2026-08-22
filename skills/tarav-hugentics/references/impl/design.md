# Implementation.Design.Workflow.Module

Load this canonical workflow module for `--impl --design` and as the first phase of `Implementation.Develop.Workflow.Module`.

Operate as the `impl.designer.agent`: inspect the implementation context, design an implementation path, and produce an `Impl.Req` artifact.

Always load `references/impl/product-capture.md`. Its selective capture bar and `Index.Native.Surface` rules govern the `Impl.Req` produced here.

Always load `references/impl/general-practices.md` and `references/impl/general-preferences.md`. They carry design stances the plan commits to — `No.Legacy.Allowed`, dependency justification, what a slice's check should test — not only execution mechanics. A plan written without them can specify work its executer is instructed not to do.

## Alignment.Loop::How

Run `Alignment.Loop::How`, the `How.Design` specialization that converges on an implementation path for runnable product surfaces:

- `Alignment.Question::How` - drive toward implementation design and enrich the `Impl.Index` with `Hard.Evidence`
- `Alignment.Discussion::How` - resolve implementation concerns
- `Alignment.Consolidation::How` - write or update the `Impl.Req`

Continue until the implementation design is sufficiently aligned for execution.

## Alignment.Mode

Respect the mode resolved by the driver:

- `Interactive` - use declared checkpoints as alignment opportunities and raise unresolved needs to the user.
- `Autonomous` - resolve checkpoints without prompting, produce the `Impl.Req` as the audit trail, and abort only on hard failure.

At a design-reality deviation:

- `Interactive` - stop at the declared checkpoint and ask.
- `Autonomous` - record the deviation in `Impl.Index` or `Impl.Log` and continue with the most faithful action.

## Alignment.Checkpoint::Readiness

Immediately before writing the `Impl.Req`, confirm:

- scope and out-of-scope are explicit
- current state was inspected and cited
- every slice has an observable result and a check
- feedback loops and `RED.GREEN.Test.Suite` behaviors are named
- dependencies and ordering are explicit
- no unresolved decision is hidden inside an execution step
- every load-bearing element has more than one independent reason, or is named as provisional
- the plan is understandable without chat context

Close each gap yourself where possible. In `Interactive`, raise unresolved gaps and wait. In `Autonomous`, resolve them and record any conscious waiver.

Do not pad the artifact merely to satisfy the readiness check.

## Impl.Req Artifact

An `Impl.Req` is the implementation-request artifact passed from design to execution.

### Structure

- `Impl.Abstract` - scope, status, and source context; reevaluate it after each design change
- `Impl.Index` - implementation design alignment as `Design.Index.Blocks`
- `Execution.Plan` - ordered vertical slices, checks, risks, deviation triggers, acceptance signals, and slice status
- `Impl.Log` - deviations, blockers, and decisions made in open space

### Location

- use a filename ending in `-impl-req.md`
- store it in `notes/live/`
- use `tarav-live-surfaces` for location and numbering

### Writing

- write for an implementer who did not see the design discussion
- preserve the user's accepted intent
- prefer references to files, notes, commands, and surfaces over pasted code
- shape implementation without overspecifying incidental implementation detail
- use ordered `Vertical.Slice`s whose endpoints exercise a meaningful path through the system
- make each slice independently observable and checkable at a durable boundary
- where the `RED.GREEN.Test.Suite` applies, drive one boundary behavior RED then GREEN before moving to the next

The caller's explicit `--design` or `--develop` invocation authorizes writing the artifact. Do not write an `Impl.Req` from passive orientation alone.

See `references/impl/example.md` for a concrete artifact sample.

### Impl.Index Capture

`Impl.Index` is an `Index.Native.Surface`: it carries the implementation's typed `Index.Line`s directly and needs no `Skw.Annotation` wrapper or parallel `Impl.Agendix` reservoir.

Capture into it twice:

1. **before writing** — resolve the selected user messages and touched Index blocks that actually constrain the plan, then write their direct, typed implementation consequences;
2. **after writing** — audit the complete artifact, add any important supported line the plan exposed, and remove plan wording that overstates its evidence.

Use the loaded conversation to understand the design. Ask Chatlas2 only to resolve the exact user messages selected as support. Every authoritative line must have a qualifying `Support.Set`; every written anchor and address must resolve.

Material not supported by `Touched.Authority` may still be useful `Open.Inference`. Record consequential agent reasoning as a typed `Index.Presumption` in `Impl.Log`, and surface it in chat. Do not convert it into authority or annotate merely to fill the artifact.

The written `Impl.Index` describes plan constraints and decisions, not landed product state. Product-state capture begins during execution and is backpropagated only after its slice is verified.

## Updating And Feedback

- prefer focused updates over full rewrites
- update `Impl.Abstract` when the implementation request changes
- keep ordinary code changes out of `Impl.Log`; the diff already records them
- keep consequential open-space inference in `Impl.Log` as typed presumption rather than hiding or falsely grounding it
- when implementation design exposes a fundamentals-design problem, note it in the artifact and identify the source design surface that may need revision
- for realignment work, state the observed drift and corrective request explicitly

## Evidence Priority

1. The user's current explicit directions.
2. Confirmed understanding from the current discussion.
3. The source design artifact or context.
4. Current codebase state, diffs, and referenced surfaces.

## Output

Exit with the complete `Impl.Req` path and a concise readiness summary. Under `Implementation.Develop.Workflow.Module`, return control to `references/impl/develop.md` instead of ending the overall skill.
