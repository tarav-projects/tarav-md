# Capture Audit

Scan the chat to verify that all relevant user ideas, approvals, and decisions have been captured in the appropriate design-session artifacts.

## Triggers

- User requests: "capture-audit", "did we miss anything?", "scan the chat", "check what we missed"
- Agent suggests it when appropriate: after a long discussion stretch, before ending a session, or when multiple items were discussed rapidly without document updates.

## Output

Produce a short report — do not auto-update the artifacts:

```
Capture audit:
- Core.Design / [item]: [missing concept, judgment, correction, relation, open space]
- TODO.Design / [item]: [missing objective, evidence, guidance, validation, boundary]
- Exec.Plan / [section]: [missing step, command, check, risk, deviation]
- [new]: [concept/task/plan material mentioned but not yet placed]
```

If nothing is missing: "Capture audit: document is in sync."

Audit against the layer model:

- settled design material should be in `Core.Design`
- unsettled significant design material should be visible as open space
- task objectives, validation, evidence, and boundaries should be in `TODO.Design`
- concrete ordered steps and checks should be in `Exec.Plan`
- user-gated writes or settlements should not be treated as captured unless the user explicitly approved them

## After The Report

The user decides what to update. The agent may propose specific edits based on the report, but waits for approval as usual.
