# Session.Interruption

`Session.Interruption` is a temporary break from the main one-question design loop.

It does not end the session and does not imply implementation. It changes the next response shape so the agent can answer a session-management need.

An interruption can be user-triggered or agent-suggested. If agent-suggested, the transition is user-gated.

## Common Interruptions

### Status.Report

The user asks for status, catch-up, what's next, what is stale, or where the session stands.

Use `status-report.md`.

### Capture.Audit

The user asks whether anything from the chat is missing, or the agent recommends a sync check after a long discussion.

Use `capture-audit.md`.

### Consolidation.Plan

The user asks for capture, consolidation, what should be updated, or how to apply the current alignment.

Use `discussion.md` usage histories and `consolidation-plan-example.md`.

### Artifact.Upgrade

The user asks to persist the session, or the agent recommends upgrading from `Alignment.Backend::InChat::What` to `Alignment.Backend::Artifact::What`.

Use `backend-artifact.md`.

### Impl.Req.Handoff

The user asks to move toward implementation or wants an execution-ready handoff.

Use `impl-req.md`.

### Session.Split

The session has become too long, crossed into a different design target, or has separate threads with different lifecycles.

Use `backend-artifact.md` split guidance when an artifact exists.

### Close.Topic

A topic has converged enough for the current session and the user wants to close it.

Capture the closure in the active backend when useful.

### Park.Topic

A topic is useful but not the current path.

Record the parked material in `Session.Notes` for artifact mode, or in a compact printed note for in-chat mode.

## Rules

- Treat interruptions as temporary.
- Choose the response shape that matches the interruption.
- Do not combine unrelated interruptions unless the user asks for a broad checkpoint.
- Do not write artifacts during an interruption without user approval.
- Return to the active session flow after the interruption unless the user chooses another next move.
