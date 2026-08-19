# Implementation.Workflow.Router.Module

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
- detail: `tarav-hugentics/references/alignment-session.md`

## Batchy.Router

The implementation flags call the same running `Batchy.Router` as the root skill. The root `Routing.Table` (`^package-driver-router`) owns the namespaced configurations, shortcuts, matching policies, defaults, destinations, and load paths; this module consumes that resolved configuration rather than redeclaring a second table. Workflow selection is not a workflow-valued `Skill.Arg`.

Without an explicit workflow flag, the router may use the resolved input, live conversation, and declared defaults. Resolve the workflow in this order:

1. A composed namespaced workflow selector or its exact shortcut always wins.
2. Bare `--impl` or `--implementation` contributes only the namespace; it does not mean develop.
3. `--impl --capture` contributes `Implementation.Product.Capture.Workflow.Module`; it does not independently select design, execute, or develop, and mutating implementation workflows already compose it by default.
4. Without a workflow selector, resolve `Input` to `Implementation.Execute.Workflow.Module` when it is an `Impl.Req`.
5. Otherwise resolve to `Implementation.Design.Workflow.Module` when actionable implementation input or conversation exists.
6. Never infer `Implementation.Develop.Workflow.Module`; end-to-end execution requires `--impl --develop`, `--develop`, or `--dev`.
7. Never infer `Implementation.Review.Workflow.Module`; the blind-spot check requires `--impl --review` or `--review`.
8. Never infer `Implementation.Harvest.Workflow.Module`; selecting ready work requires `--impl --harvest` or `--impl-harvest`.

Treat input as an `Impl.Req` when it is:

- a path whose file is an `Impl.Req`, normally ending in `-impl-req.md`
- a note number or reference that resolves to such an artifact
- supplied artifact content carrying the `Impl.Abstract`, `Impl.Index`, `Execution.Plan`, and `Impl.Log` structure

If neither an input nor actionable current context exists, orient to the available workflows and do not guess a target.

Load only the selected workflow module. The develop module composes design and execute and therefore loads both in sequence. Review is designed to run in a fresh agent that did not design the artifact — that is where the blind-spot check has value.

## Shared Contract

- Preserve the selected `Alignment.Mode` across every phase.
- Treat the generated or supplied `Impl.Req` as the phase boundary and audit trail.
- Keep the `impl.designer.agent` and `impl.executer.agent` responsibilities distinct even when one agent runs both.
- Respect the project package orientation already supplied by local routing.
- Load the relevant Index module in this skill when the task needs index-grounded context or index mutation.
- Respect project-local `AGENTS.md` and repository instructions before any implementation edit.
- Every mutating implementation workflow composes `Implementation.Product.Capture.Workflow.Module`; capture is a selective slice companion, not a separately selected implementation workflow.
- `Impl.Index` and `Impl.Log` are `Index.Native.Surface`s. Ordinary product surfaces carry qualifying typed `Index.Line`s through `Skw.Annotation`.
