---
name: hugentics-designer
description: "Main.Designer.Agent workflow master — run What.Design.Session workflows for scoped human-agent design convergence. Covers in-chat and artifact-backed sessions, session interruptions, and impl-req handoffs."
---

# Hugentics Designer

Workflow master for the `Main.Designer.Agent` — the first phase of the Hugentic Harness.

Coordinate a `What.Design.Session`: a scoped human-agent convergence surface for design work. The agent serves as moderator, tracking progress and driving the user toward alignment through cycles of `Alignment.Question:What` → `Alignment.Discussion:What` → `Alignment.Consolidation:What`.

For the general alignment model, see `agentos-hugentics` and its `references/alignment-session.md`.

This skill is a router. Load only the references needed for the current backend, interruption, or section update.

## Activation

Activate this skill when the user wants to start or continue a design session.

Typical activation phrases include "let's start a design session", "let's design X", "start a design-session", "continue the design-session", or an explicit `hugentics-designer` invocation.

Do not activate for ordinary design discussion, implementation work, generic status reporting, or code review.

## Execution Workflow

1. Activate the minimal runtime.
2. Choose the backend.
3. Detect the current move or interruption.
4. Load only the references needed for that move.
5. Execute one `Alignment.Loop:What` move.
6. Respect user gates.

## Minimal Runtime

Always load:

- `references/alignment-loop.md`
- `references/interview.md`
- `references/discussion.md`

## Backend Routing

Use `Alignment.Backend:InChat:What` by default:

- load `references/backend-inchat.md`
- do not create a file

Use `Alignment.Backend:Artifact:What` when the user explicitly asks to upgrade, persist, capture to file, or create a design-session artifact:

- load `references/backend-artifact.md`
- load `references/artifact.md`
- use `agentos-live-note-base` for live-note location and numbering

Suggest `Alignment.Backend:Artifact:What` when:

- the session state is too large or important to keep only in chat
- the work needs durable handoff to later agents or future sessions

Do not upgrade automatically. The user controls backend changes.

## Impl.Req Handoff

When the user wants implementation-ready handoff:

- load `references/impl-req.md`
- load `hugentics-impl-designer` to hand off to the implementation-request workflow

## Move Routing

For normal design flow:

- use `Alignment.Loop:What`
- ask or continue one design question at a time
- follow `references/interview.md` and `references/discussion.md`

For session interruptions:

- load `references/session-interruptions.md`
- then load the specific interruption reference:
  - status request -> `hugentics-workflow-status`
  - capture audit -> `hugentics-capture-audit`
  - consolidation request -> `references/discussion.md` and `references/consolidation-plan-example.md`
  - artifact upgrade -> `references/backend-artifact.md` and `references/artifact.md`
  - implementation handoff -> `references/impl-req.md`
  - split / close / park -> `references/session-interruptions.md` plus backend reference as needed

For uncommitted or stale session state:

- load `references/uncommitted-work.md`
- surface only issues that matter to the current move

## Section Routing

Load section references only when printing, updating, auditing, or capturing that section:

- `Session.Abstract` -> `references/session-abstract.md`
- `Design.Index` -> `references/design-index.md`
- `Session.Notes` -> `references/session-notes.md` in `Alignment.Backend:Artifact:What`
- `Session.Log` -> `references/session-log.md` in `Alignment.Backend:Artifact:What`

## Alignment.Backend:Artifact:What Format

A `*-design-session.md` `Live.Note` used as file-backed session backend.

Sections: `Session.Abstract`, `Design.Index`, `Session.Notes`, `Session.Log`

Artifact writes are user-gated.

## Runtime Rule

The shared runtime is:

```txt
Alignment.Loop:What:

Alignment.User.Turn
  -> agent follows the user's current thread
  -> user/agent discuss one design question until convergence, parking, or rejection
  -> agent may surface important alignment issues when they materially affect the discussion
  -> agent may suggest a user-gated Alignment.Maintenance.Turn

Alignment.Maintenance.Turn
  -> agent chooses one primary session move
  -> ask next question, consolidate, report status, surface stale state, upgrade, close, split, or hand off
  -> return to Alignment.User.Turn
```

Turn switching is user-gated. The agent may recommend a maintenance turn, but should not silently switch from user-led discussion into session-maintenance mode.

The happy path is:

```txt
agent asks one design question
-> user/agent discuss until convergence
-> user/agent consolidate the result
-> update state if needed
-> user asks for next/continue
-> agent asks one next design question
```

## User Gates

In chat:

- the agent may print updated session sections without file-write approval
- the agent should make clear what changed when refreshing state
- the user controls whether printed state is accepted, corrected, parked, or upgraded

In artifacts:

- the agent may not create or update a session artifact without user approval
- the agent must present the intended write, exact proposed text, or a concise diff summary before writing
- artifact creation, section updates, splitting, and impl-req production are user-gated

Actual Agentos Index writes remain governed by the Agentos Index write workflow.

## Evidence Priority

1. The user's current explicit directions.
2. Accepted decisions from the current session.
3. Current in-chat session state or active artifact state.
4. Current codebase state and diffs.
5. Stable project surfaces such as index notes, project `AGENTS.md`, active skills, CLI help, documented spec surfaces, or other source-of-truth project artifacts.

## Exit Condition

Exit this skill when the session ends, or when the user switches to implementation, a different skill, or a different task.
