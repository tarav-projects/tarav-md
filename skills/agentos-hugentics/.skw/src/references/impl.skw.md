# Implementation.Workflow.Router.Module

> $kw: --dev-from references/index-context-assembly.skw.md

`Implementation.Workflow.Router.Module` is the internal namespace router for implementation work in the Hugentic system.

The skill routes into implementation design, implementation execution, or both in sequence while keeping each workflow in an on-demand `Skill.Module`.

The unified driver supplies the `Batchy.Skill` calling convention.

- `-h` / `--help` prints usage and exits without running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved run configuration as its first step (`Batchy.Skill.Banner`).
- explicit workflow flags configure `Batchy.Router`; input flags and applicable conversational data bind the `Skill.Arg` names below.

## Skill.Arg.Section

### Skill.Arg::Input
- the implementation source: an idea, direct request, design artifact, design summary, or `Impl.Req`
- required: false
- default: the caller's current explicit request or supplied context
- help: "the idea, design source, or Impl.Req to operate on"
- examples: --input "add project-scoped configuration"

### Skill.Arg::Alignment.Mode
- whether the workflow prompts at declared `Alignment.Checkpoint`s or resolves them autonomously
- required: false
- default: Interactive
- type: switch
- help: "run the selected workflow autonomously"
- examples: --AUTO
- aliases: --auto, --autonomous
- detail: `agentos-hugentics/references/alignment-session.md`

## Batchy.Router

The implementation flags call the same running `Batchy.Router` as the root skill. They select rows in the `Routing.Table` below; they are not a workflow-valued `Skill.Arg`.

| Explicit configuration | Selected row |
|---|---|
| `--impl --design` | `Implementation.Design.Workflow.Module` |
| `--impl --review` | `Implementation.Review.Workflow.Module` |
| `--impl --execute` | `Implementation.Execute.Workflow.Module` |
| `--impl --develop` | `Implementation.Develop.Workflow.Module` |
| `--impl --capture` | `Implementation.Capture.Workflow.Module` |

`--implementation` is an alias for the `--impl` namespace. The shortcuts `--impl-design`, `--review`, `--execute`, `--exec`, `--develop`, `--dev`, and `--impl-capture` normalize to the corresponding namespaced calls above.

Without an explicit workflow flag, the router may use the resolved input, live conversation, and declared defaults. Resolve the workflow in this order:

1. A composed namespaced workflow flag or its exact shortcut always wins.
2. Bare `--impl` or `--implementation` contributes only the namespace; it does not mean develop.
3. Without a workflow selector, resolve `Input` to `Implementation.Execute.Workflow.Module` when it is an `Impl.Req`.
4. Otherwise resolve to `Implementation.Design.Workflow.Module` when actionable implementation input or conversation exists.
5. Never infer `Implementation.Develop.Workflow.Module`; end-to-end execution requires `--impl --develop`, `--develop`, or `--dev`.
6. Never infer `Implementation.Review.Workflow.Module`; the blind-spot check requires `--impl --review` or `--review`.
7. Never infer `Implementation.Capture.Workflow.Module`; harvesting ready work requires `--impl --capture` or `--impl-capture`.

Treat input as an `Impl.Req` when it is:

- a path whose file is an `Impl.Req`, normally ending in `-impl-req.md`
- a note number or reference that resolves to such an artifact
- supplied artifact content carrying the `Impl.Abstract`, `Impl.Index`, `Execution.Plan`, and `Impl.Log` structure

If neither an input nor actionable current context exists, orient to the available workflows and do not guess a target.

## Routing.Table

> $kw: ^workflow-router

> $kw: --when
`Implementation.Design.Workflow.Module` is selected - the caller wants implementation planning.

> $kw: --then
Load `references/impl/design.md` — produce an implementation-ready `Impl.Req`.

> $kw: --when
`Implementation.Review.Workflow.Module` is selected - the caller wants an `Impl.Req` double-checked.

> $kw: --then
Load `references/impl/review.md` — verify the artifact's claims against `Hard.Evidence` and report readiness in chat; read-only.

> $kw: --when
`Implementation.Execute.Workflow.Module` is selected - the caller wants an existing `Impl.Req` executed.

> $kw: --then
Load `references/impl/execute.md` — execute the artifact's `Execution.Plan`.

> $kw: --when
`Implementation.Develop.Workflow.Module` is selected - the caller wants an idea taken through both phases.

> $kw: --then
Load `references/impl/develop.md` — produce an `Impl.Req`, then execute that exact artifact.

> $kw: --when
`Implementation.Capture.Workflow.Module` is selected - the caller wants the session's ready implementation work banked and the rest parked.

> $kw: --then
Load `references/impl/impl-capture.md` — rank the touched, implementation-ready candidates, gate on the best pick, and hand it to develop.

> $kw. end

Load only the selected workflow module. The develop module composes design and execute and therefore loads both in sequence. Review is designed to run in a fresh agent that did not design the artifact — that is where the blind-spot check has value.

## Shared Contract

- Preserve the selected `Alignment.Mode` across every phase.
- Treat the generated or supplied `Impl.Req` as the phase boundary and audit trail.
- Keep the `impl.designer.agent` and `impl.executer.agent` responsibilities distinct even when one agent runs both.
- Respect the project package orientation already supplied by local routing.
- Load the relevant Index module in this skill when the task needs index-grounded context or index mutation.
- Respect project-local `AGENTS.md` and repository instructions before any implementation edit.

> $kw: --from Alignment.Checkpoint --from Alignment.Mode --from Batchy.Router --from Batchy.Skill --from Batchy.Skill.Banner --from Batchy.Skill.Help --from Hard.Evidence --from Impl.Req --from Routing.Table --from Skill.Arg --from Skill.Module
