# Status.Report

`Status.Report` is a `Session.Interruption` that summarizes current session state.

It is report-only by default. It does not update artifacts unless the user asks.

## Triggers

Use when the user asks:

- "status"
- "catch me up"
- "where are we?"
- "what's next?"
- "what's stale?"
- "anything missing?"
- "what should we do now?"

The agent may suggest a status report when the session is long, stale, or multi-threaded.

## Format

Use a compact report with sections that matter:

```md
## Session.Status

### Done / Closed

- [settled concept, closed question, captured decision]

### Doing

- [active question or current convergence thread]

### Stale / Misaligned

- [state that no longer matches the discussion]

### Open / Unfinished

- [open questions, unresolved names, missing docs]

### Proposed Maintenance

- [one or two recommended repairs, captures, or upgrades]

### Next Question

- [recommended next design question]
```

Omit empty sections unless omission would hide a meaningful "none".

## Rules

- Keep it scannable.
- Separate committed state from uncommitted chat deltas.
- Name stale, misaligned, or unfinished material when it affects the next move.
- Recommend one primary next move.
- Do not perform proposed maintenance automatically.
- After the report, wait for the user to choose the next move.
