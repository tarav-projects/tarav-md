---
name: agentos-design-session
description: "Route and coordinate Design.Session workflows for in-chat design convergence, artifact-backed sessions, and optional impl-req handoffs. USE WHEN the user explicitly requests starting or continuing a design-session"
---

# Design Session

Coordinate a `Design.Session`: a scoped human-agent convergence workflow for design work.

This skill is a router. Load only the references needed for the current backend, interruption, or section update.

## Activation Gate

Use this skill only when the user explicitly requests starting or continuing a `design-session`, or explicitly invokes `agentos-design-session`.

Do not use it for ordinary design discussion, implementation work, generic status reporting, or code review.

## Execution Workflow

1. Activate the minimal runtime.
2. Choose the backend.
3. Detect the current move or interruption.
4. Load only the references needed for that move.
5. Execute one `Session.Runtime.Loop` move.
6. Respect user gates.

## Minimal Runtime

Always load:

- `references/session-runtime.md`
- `references/interview.md`
- `references/discussion.md`

Load `notes/index/111-Design.Session.md` when available and useful. Do not block if it is absent.

## Backend Routing

Use `InChat.Session` by default:

- load `references/inchat-session.md`
- do not create a file

Use `Artifact.Session` when the user explicitly asks to upgrade, persist, capture to file, or create a design-session artifact:

- load `references/artifact-session.md`
- load `references/artifact.md`
- use `agentos-live-note-base` for live-note location and numbering

Suggest `Artifact.Session` when:

- the session state is too large or important to keep only in chat
- the work needs durable handoff to later agents or future sessions

Do not upgrade automatically. The user controls backend changes.

Use `Impl.Req` only on demand when the user wants implementation-ready handoff:

- load `references/impl-req.md`
- use `agentos-artifact-impl-req`

## Move Routing

For normal design flow:

- use `Session.Runtime.Loop`
- ask or continue one design question at a time
- follow `references/interview.md` and `references/discussion.md`

For session interruptions:

- load `references/session-interruptions.md`
- then load the specific interruption reference:
  - status request -> `references/status-report.md`
  - capture audit -> `references/capture-audit.md`
  - consolidation request -> `references/discussion.md` and `references/consolidation-plan-example.md`
  - artifact upgrade -> `references/artifact-session.md` and `references/artifact.md`
  - implementation handoff -> `references/impl-req.md`
  - split / close / park -> `references/session-interruptions.md` plus backend reference as needed

For uncommitted or stale session state:

- load `references/uncommitted-work.md`
- surface only issues that matter to the current move

## Section Routing

Load section references only when printing, updating, auditing, or capturing that section:

- `Session.Abstract` -> `references/session-abstract.md`
- `Design.Index` -> `references/design-index.md`
- `Session.Notes` -> `references/session-notes.md` in `Artifact.Session`
- `Session.Log` -> `references/session-log.md` in `Artifact.Session`

## Runtime Rule

The shared runtime is:

```txt
Session.Runtime.Loop:

User.Assistant.Turn
  -> agent follows the user's current thread
  -> user/agent discuss one design question until convergence, parking, or rejection
  -> agent may surface important alignment issues when they materially affect the discussion
  -> agent may suggest a user-gated Session.Maintenance.Turn

Session.Maintenance.Turn
  -> agent chooses one primary session move
  -> ask next question, consolidate, report status, surface stale state, upgrade, close, split, or hand off
  -> return to User.Assistant.Turn
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

## Example Prompts That Should Trigger This Skill

- "let's start a design session"
- "let's start a design-session"
- "continue the design-session"
- "upgrade this to a design-session"
- "create a design-session artifact"
- "use agentos-design-session"

## Exit Condition

Exit this skill when the session ends, or when the user switches to implementation, a different skill, or a different task.
