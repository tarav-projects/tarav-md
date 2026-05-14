---
name: agentos-artifact-impl-req
description: "Define and manage impl-req (implementation request) artifacts. Use when creating, reading, updating, or executing an impl-req live-note."
---

# Artifact: impl-req

Protocol for `impl-req` artifacts — structured live-notes that capture what should be implemented, what constraints matter, and how later work should be evaluated.

## Trigger Boundary

Use this skill when:

- The user asks to create, read, update, or execute an `impl-req`.
- Another skill needs to produce or consume an `impl-req` artifact.

## Purpose

- An `impl-req` is an implementation-request artifact for other-agent consumption.
- It captures converged design intent in a form that another agent (or future session) can act on without replaying the full discussion.
- It should shape implementation toward fast feedback, especially through vertical slices.
- Treat `impl-req` notes as durable coordination artifacts, not chat transcripts.

## Location And Naming

- Read `agentos-live-note-base` from the current available skills surface before writing.
- Use a filename ending in `-impl-req.md`.
- Store in `notes/live/`.

## Writing Guidance

- Write for another agent who did not see the full discussion.
- Be direct and clear.
- Prefer references to files, notes, commands, or surfaces over pasted code.
- Do not include large file fragments or long code excerpts.
- Prefer implementation-shaping context over implementation detail.
- Prefer vertical slices. This is one of the central purposes of an `impl-req`: convert broad intent into small end-to-end changes that can be checked quickly.
- Include ordered work when useful, but keep the artifact focused on the request and validation contract rather than a progress diary.
- Be flexible about exact headings when needed, but keep the same semantic coverage.
- Do not write an `impl-req` automatically. Only write one on explicit user request.

## Vertical Slices

A vertical slice is a small change that goes through the full useful path for one behavior, instead of completing one technical layer in isolation.

Avoid horizontal plans like:

```txt
1. Add all schema changes.
2. Add all service logic.
3. Add all UI.
4. Test later.
```

That shape delays feedback. The agent may spend a long time building layers before anyone can tell whether the behavior works end to end.

Prefer slices like:

```txt
When X happens, the user or system can observe Y, and check Z proves it.
```

The observable result does not have to be a UI. Depending on the project, it may be:

- a passing behavior test
- a command output
- a created or updated artifact
- a visible UI state
- an API response
- a reviewable file or data state
- a manual QA step with a clear expected result

Each vertical slice should state:

- what narrow behavior changes
- what path through the system or artifact surface it exercises
- what observable result should exist afterward
- how that result will be checked
- what design or task assumption the slice validates

Use horizontal work only when it is truly enabling infrastructure that cannot be made observable yet. If a horizontal step is necessary, name the reason and pair it with the earliest possible vertical slice.

## Minimal Structure

```md
# [Short Title] - impl-req

## Impl-Req State

One sentence describing the current state of the request.

## User Intent

## Why This Exists

## Current Situation

## Requested Change

## Constraints And Invariants

## Out Of Scope

## Acceptance Signals

## Implementation Shape

## Relevant Files Or Surfaces

## Open Questions

## Related Impl-Reqs

## End Log
```

## Section Guidance

- `Impl-Req State` is a plain-language one-sentence state note, not a fixed status enum.
- `Relevant Files Or Surfaces` may include code paths, notes, commands, or spec surfaces.
- `Implementation Shape` should capture vertical slices first when the work can be sliced. It may also include sequencing, validation loops, risks, review points, or deviation triggers when they materially help another agent implement the request.
- `Related Impl-Reqs` should call out predecessors, follow-ups, or superseded requests.
- `End Log` is append-only. Add concise dated notes at the end as work progresses.

## Updating Guidance

- Preserve the original request intent unless the user explicitly changes it.
- When refining, prefer focused updates over full rewrites.
- Do not silently replace accepted intent with your own reinterpretation.
- When implementation work occurs, update `Impl-Req State` and append a short note to `End Log` describing what changed, what remains, and any important drift or blockers.

## Post-Execution Update

After implementing an `impl-req`:

- Update the `Impl-Req State` sentence to reflect the current state plainly.
- Append a short dated note to `End Log`.
- The log note should say what was implemented, what remains if anything, and any drift or blockers discovered.
- Cite concrete files or surfaces when useful.

## For Realignment Notes

When an `impl-req` is written to correct drift from an accepted design:

- Explain the observed drift under `Current Situation`.
- Make the corrective request explicit under `Requested Change`.
- Reference the original design artifact or discussion.

## Example

See `references/example.md` for a concrete sample.
