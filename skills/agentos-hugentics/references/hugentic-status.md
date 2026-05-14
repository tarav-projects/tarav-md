# Hugentic Status

Produce a structured status report for the active hugentic workflow. The report shape adapts to whichever workflow is active.

## Scope

This practice applies to any explicit hugentic workflow:

- **Design session** — report against `Design.Index`, `Session.Notes`, session state
- **Impl-req design** — report against `Impl.Index`, `Execution.Plan`, alignment progress
- **Impl execution** — report against `Impl.Log`, slice progress, deviations

The report target depends on which workflow is active. Report against whatever surfaces the current workflow maintains.

## Triggers

- User requests: "workflow status", "hugentic status", "where are we on the design?", "what's the plan status?"
- Agent suggests it when appropriate: after a long stretch, at natural checkpoints, or when the user seems disconnected from the workflow state.

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
