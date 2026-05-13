# Session.Log

`Session.Log` records meaningful events in a `Design.Session`.

It is a chronological event log, not a transcript.

## Role

Use `Session.Log` for:

- session created
- artifact initialized
- concept added, renamed, rejected, or settled
- docs section added
- open question parked
- session split
- impl-req produced
- session closed

## Shape

Prefer concise dated entries:

```md
## Session.Log

- 2026-05-11: Created session artifact for [topic].
- 2026-05-11: Settled `Concept.Name` as [short result].
- 2026-05-11: Produced `NNN-topic-impl-req.md` from current session state.
```

## Writing Guidance

- Log meaningful state changes only.
- Keep entries short.
- Include artifact filenames when another artifact is created.
- Include negative decisions when they close off a path.
- Do not record every user message or agent response.

## User Gate

Log entries are artifact writes and require approval unless included in an already approved update.
