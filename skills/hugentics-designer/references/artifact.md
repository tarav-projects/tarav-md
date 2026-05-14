# Design Session Artifact

`*-design-session.md` is the file artifact used by `Alignment.Backend:Artifact:What`.

It is the externalized state of the session: conceptual background, working notes, and event log in one file.

## Filename

Use:

```txt
NNN-timetag-design-session.md
```

Store it in `notes/live/` using `agentos-live-note-base` numbering guidance.

Prefer one artifact once the session is in artifact mode. Create another `*-design-session.md` only for length, scope, lifecycle, or audience reasons.

## Structure

```md
# [Short Title] - design-session

## Session.Abstract

## Design.Index

## Session.Notes

## Session.Log
```

## Authority

The artifact is working state.

- It can record settled session-local meaning.
- It does not override durable index notes.
- Durable design truth belongs in `notes/index/` after the appropriate index workflow.

## Writing Guidance

- Keep `Design.Index` concept-shaped.
- Use `Design.Index.Block` fundamentals for compact meaning.
- Use `Design.Index.Block` appendix for rationale, examples, pressure tests, tradeoffs, rejected alternatives, and design depth.
- Use `Design.Index.Block` meta for session mechanics.
- Put unresolved working material in `Session.Notes`, not hidden in chat.
- Use `Session.Log` for meaningful events, not every conversational turn.
- Preserve negative decisions when they prevent future confusion.
- Do not turn the artifact into a transcript.

## User Gate

Create or update the artifact only after user approval.

For small updates, propose a concise write target:

```txt
I'd update Session.Abstract and add one Design.Index block for [Concept.Name]. OK?
```

For larger updates, present exact proposed text or a concise diff summary before writing.
