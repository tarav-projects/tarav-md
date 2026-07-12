# Session.Log

`Session.Log` records session-level events that would be **lost** if
removed — events not reconstructible from the rest of the artifact.

It is not a changelog of decisions and not a transcript of actions.

## Orthogonality Rule

A log entry must be **orthogonal** to the rest of the document.

Before writing an entry, ask: *can a future reader recover this fact
by reading `Session.Abstract` + `Design.Index` + `Session.Notes`?*

- If yes → do not log. The artifact already carries it; git history
  carries the timing.
- If no → log it. This is the kind of fact `Session.Log` exists for.

A resolved open question is **not** a log entry: the resolution is
the index edit. "Settled `Concept.Name` as X" is redundant when X
already appears under `Concept.Name`.

## Role

Use `Session.Log` for:

- session created / paused / resumed / closed
- backend chosen or switched
- session split, merged, or handed off to another agent/session
- abandoned directions or rejected framings (the path *not* in the
  index — without a log entry, this disappears entirely)
- external events that shaped the session (a referenced chat, an
  out-of-band user decision, a sibling artifact created)

Do not use `Session.Log` for:

- concept added, renamed, or settled — visible in `Design.Index`
- open question parked — visible in the relevant `#### meta`
- routine agent actions (writes, edits, reads)
- restating decisions already captured elsewhere

## Shape

Concise dated entries:

```md
## Session.Log

- 2026-05-11: Session opened. Backend: `Alignment.Backend::Artifact::What`.
- 2026-05-12: Abandoned "single-layer" framing — collapses
  user/system boundary the session is here to draw.
- 2026-05-13: Produced `NNN-topic-impl-req.md`; session closed.
```

## Writing Guidance

- Apply the orthogonality rule on every candidate entry.
- Keep entries short.
- Include artifact filenames when another artifact is created or
  referenced.
- Record abandoned directions with enough context that a future
  reader understands *why* they were dropped — that context is the
  whole point of the entry.

## User Gate

Log entries are artifact writes and require approval unless included
in an already approved update.
