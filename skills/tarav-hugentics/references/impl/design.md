# Implementation Design Workflow

Load this module for `--impl --design` and as Develop's first phase. Also load
[`product-capture.md`](product-capture.md),
[`general-practices.md`](general-practices.md), and
[`general-preferences.md`](general-preferences.md).

Operate as the implementation designer: inspect the current product, converge
on an implementation path, create the live-note `Impl.Req`, and establish its
`Impl.Req.Diagram`.

## Alignment Loop

Use the same implementation-design loop as the former workflow:

1. **Question** — inspect implementation reality and identify the decisions
   needed for an executable path.
2. **Discuss** — resolve implementation concerns with the User when the chosen
   Alignment.Mode requires it.
3. **Consolidate** — write or update the durable `Impl.Req`.

Interactive mode uses readiness and design-reality checkpoints as alignment
opportunities. Autonomous mode resolves them without prompting, records
consequential assumptions in `Impl.Log`, and stops only when faithful progress
requires external input.

## Readiness Checkpoint

Before declaring the request executable, confirm:

- scope and out-of-scope are explicit;
- current product state was inspected and cited;
- every vertical slice has an observable result and a check;
- dependencies and ordering are explicit;
- risks and deviation triggers are named;
- no unresolved User decision is hidden inside an execution step; and
- the artifact is understandable without the design chat.

Close gaps yourself where possible. Do not pad the artifact merely to satisfy
the checklist.

## Live-Note Impl.Req

The live note is the Agent's main coordination artifact and the mandatory
handoff to execution. Store it under the target project's `notes/live/` using
the project's established numbering and naming convention, normally:

```text
<number>-<slug>-impl-req.md
```

Its required structure is:

- `Impl.Abstract` — scope, status, source context, and important boundaries;
- `Impl.Req.Diagram` — Namespace, Model, and `Impl.Req.Block` identities;
- `Execution.Plan` — ordered vertical slices, checks, risks, deviation
  triggers, acceptance signals, and slice status;
- `Impl.Log` — consequential assumptions, deviations, blockers, and decisions
  made while coordinating the implementation.

Write for an executer who did not see the design chat. Prefer precise pointers
to product and design surfaces over pasted code. Shape the plan without fixing
incidental implementation details prematurely.

See [`example.md`](example.md) for the expected live-note/Diagram split.

The explicit Design or Develop invocation authorizes writing this artifact. It
does not authorize unrelated product mutation.

## Impl.Req.Diagram

Create exactly one `Impl.Req.Block` in the Project's configured main Model, or
reuse it only when updating the same existing implementation request lineage.
Its human-facing label normally shares the live-note number:

```text
502.Impl.Req
```

The Block ship UUID is its identity; the numerical label is only a convenient
address. Record the Namespace, Model ship, Block ship, and label under the live
note's `Impl.Req.Diagram` section.

The Block is not the live note and does not reproduce its Agent-generated plan.
It contains only supported User-Touched Lines relevant to the implementation
request: requirements, decisions, constraints, rejections, principles,
freedoms, examples, and later User resolutions. Use `Impl.Req.Block` with the
same full Line.Type vocabulary as `Design.Block`.

Capture the first bounded set while designing:

1. resolve the current Project Model and relevant existing Diagram context;
2. select exact User turns that materially constrain this request;
3. create the Block declaration and supported Line Annotations through the
   ordinary Tarav2 Capture.Manifest path;
4. use reviewed Gates only when the actual conversation provides them; never
   manufacture approval evidence; and
5. retain the resulting identities in `Impl.Req.Diagram`.

Agent-only analysis may remain valuable in `Execution.Plan` or `Impl.Log`. It
must not be promoted into the User-Touched Block merely to make the request
look complete.

## Updating

- Prefer focused live-note edits over full rewrites.
- Reevaluate `Impl.Abstract` when scope changes.
- Keep ordinary code changes out of `Impl.Log`; Git already records them.
- When a User message changes or resolves the implementation during design,
  capture the relevant supported consequence into the same Block.
- When the design exposes a fundamentals-design problem, point to the owning
  design surface and keep the implementation request honest about the gap.

## Output

Return the complete live-note path, its `Impl.Req.Block` address, and a concise
readiness summary. Under Develop, return control to the Develop module.
