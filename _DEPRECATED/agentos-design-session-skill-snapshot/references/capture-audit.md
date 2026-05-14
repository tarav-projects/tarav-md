# Capture Audit

Scan the chat to verify that all relevant user ideas, approvals, and decisions have been captured in the appropriate design-session artifacts.

## Triggers

- User requests: "capture-audit", "did we miss anything?", "scan the chat", "check what we missed"
- Agent suggests it when appropriate: after a long discussion stretch, before ending a session, or when multiple items were discussed rapidly without document updates.

## Output

Produce a short report — do not auto-update the artifacts:

```
Capture audit:
- Design.Index / [concept] / fundamentals: [missing fundamental, judgment, correction, relation, open space]
- Design.Index / [concept] / appendix: [missing rationale, example, tradeoff, explanation, pressure test]
- Design.Index / [concept] / meta: [missing source, state, open question, stale marker, alignment issue]
- Session.Notes / [section]: [missing open question, reference, assumption, parked idea]
- Impl.Req / [section]: [missing requested change, slice, step, command, check, risk, deviation]
- [new]: [concept/task/plan material mentioned but not yet placed]
```

If nothing is missing: "Capture audit: document is in sync."

Audit against the component model:

- compact settled or working concept fundamentals should be in `Design.Index` fundamentals
- explanation, rationale, examples, pressure tests, tradeoffs, rejected alternatives, and design depth should be in `Design.Index` appendix
- concept-level session mechanics should be in `Design.Index` meta
- unsettled significant design material should be visible in `Session.Notes`
- task-shaped observations can stay in `Session.Notes` until they are ready for an `Impl.Req`
- implementation-ready scope, vertical slices, ordered work when useful, checks, risks, and acceptance signals should be in `Impl.Req`
- user-gated writes or settlements should not be treated as captured unless the user explicitly approved them

## After The Report

The user decides what to update. The agent may propose specific edits based on the report, but waits for approval as usual.
