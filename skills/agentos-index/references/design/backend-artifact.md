# Alignment.Backend::Artifact::What

This detailed product-design module is owned by `agentos-index --design`.

`Alignment.Backend::Artifact::What` is the file-backed `What.Design.Session` workflow.

It materializes session state into one live-note artifact and continues the same alignment loop with durable working state.

## Role

Use `Alignment.Backend::Artifact::What` when:

- the user asks for an artifact, file, live note, or durable capture,
- an `Alignment.Backend::InChat::What` session is upgraded,
- the session is too large or important for chat-only state,
- the work needs future handoff,
- an `Impl.Req` is likely or requested.

## Artifact

Create one live note by default:

```txt
NNN-timetag-design-session.md
```

Use the structure from `artifact.md`:

```md
# [Short Title] - design-session

## Session.Abstract

## Design.Index

## Session.Notes

## Session.Log
```

## Workflow

1. Propose the artifact frame and source material.
2. Wait for user approval before creating or updating the file.
3. Initialize or update the standard sections.
4. Continue the one-question-at-a-time alignment loop.
5. Capture settled or useful working material into the right section.
6. Log meaningful state changes.
7. Produce `Impl.Req` artifacts only on demand.

## User Gate

Artifact writes are user-gated.

Before writing:

- name the target file,
- name the sections to update,
- summarize the intended change or provide exact proposed text when the wording matters.

After writing:

- summarize what changed,
- mention any important uncommitted discussion,
- recommend the next alignment question or handoff.

## Split Rule

Prefer one artifact by default.

Suggest a second `*-design-session.md` only when:

- the file becomes too long to stay usable,
- two convergence threads have separate audiences or lifecycles,
- one thread is ready to close while another remains exploratory,
- the session has crossed into a substantially different design target.

Do not split merely because a new section or concept exists.

## Relationship To Alignment.Backend::InChat::What

`Alignment.Backend::Artifact::What` is an upgrade of `Alignment.Backend::InChat::What`, not a different conceptual model.

The same `Session.Abstract` and `Design.Index` sections are preserved. Artifact mode adds `Session.Notes` and `Session.Log` for working state and event history.
