# Capture Audit

Scan the chat to verify that all relevant user ideas, approvals, and decisions have been captured in the active workflow's artifacts.

## Scope

This practice applies to any hugentics workflow:

- **Design session** — audit against `Design.Index`, `Session.Notes`
- **Impl-req design** — audit against `Impl.Index`, `Execution.Plan`
- **Impl execution** — audit against `Impl.Log`, deviation notes

The audit target depends on which workflow is active. Audit against whatever surfaces the current workflow maintains.

## Triggers

- User requests: "capture-audit", "did we miss anything?", "scan the chat", "check what we missed"
- Agent suggests it when appropriate: after a long discussion stretch, before ending a session or workflow phase, or when multiple items were discussed rapidly without artifact updates.

## Output

Produce a short report — do not auto-update the artifacts:

```
Capture audit:
- [surface] / [section] / [subsection]: [missing material description]
- [new]: [concept/task/plan material mentioned but not yet placed]
```

If nothing is missing: "Capture audit: artifacts are in sync."

## Audit Rules

- Compact settled or working concept fundamentals should be in the active design surface (Design.Index or Impl.Index)
- Explanation, rationale, examples, pressure tests, tradeoffs, rejected alternatives, and design depth should be in appendix sections
- Session/concept-level mechanics should be in meta sections
- Unsettled significant design material should be visible in notes (Session.Notes or equivalent)
- Task-shaped observations can stay in notes until they are ready for an execution plan
- Implementation-ready scope, vertical slices, ordered work, checks, risks, and acceptance signals should be in the execution plan
- User-gated writes or settlements should not be treated as captured unless the user explicitly approved them

## After The Report

The user decides what to update. The agent may propose specific edits based on the report, but waits for approval as usual.
