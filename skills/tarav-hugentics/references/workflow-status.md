# Workflow.Status.Operation.Module

Produce a structured status report for the active Hugentic workflow.

This is an operational `Package.Aux.Skill` under `tarav-hugentics`. It is not a general project diagnosis surface; it reports the state of an ongoing Hugentic workflow.

The unified driver supplies the `Batchy.Skill` calling convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments.

## Activation

Use when the user asks for workflow status, a structured checkpoint, or a workflow-aware report during an active Hugentic workflow: Design.Req capture, design-session capture, impl-req design, or impl execution.

Triggers: "workflow status", "hugentic status", "where are we on the design?", "what's the plan status?"

The agent may also suggest it at natural checkpoints or when the user seems disconnected from the workflow state.

## Scope

This practice applies to any explicit hugentic workflow:

- **Design.Req capture** — report its `Open` or `Closed` status, maintained `Design.Index`, `Session.Notes`, promotions, and uncommitted chat delta
- **Design-session capture** — report the maintained topic frame, grounded `Design.Index`, unresolved `Session.Notes`, promotions, and uncommitted chat delta
- **Impl-req design** — report against `Impl.Index`, `Execution.Plan`, alignment progress
- **Impl execution** — report against `Impl.Log`, slice progress, deviations

The report target depends on which workflow is active. Report against whatever surfaces the current workflow maintains.

## Output

Produce a compact report with sections that matter:

```md
## Workflow.Status

### Done / Closed

- [settled items, completed slices, captured decisions]

### Doing

- [active question, current slice, current alignment thread]

### Stale / Misaligned

- [state that no longer matches the discussion or codebase]

### Open / Unfinished

- [open questions, remaining slices, unresolved items]

### Proposed Maintenance

- [one or two recommended next actions]

### Next

- [recommended next move for the active workflow]
```

Omit empty sections unless omission would hide a meaningful "none".

## Rules

- Keep it scannable.
- Separate committed artifact state from uncommitted chat deltas.
- Name stale, misaligned, or unfinished material when it affects the next move.
- Recommend one primary next move.
- Report only — do not perform proposed maintenance automatically.
- After the report, wait for the user to choose the next move.
