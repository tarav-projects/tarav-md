---
name: agentos-design-session
description: "Coordinate a composable Design.Session for non-linear human-agent design convergence. Use when design work needs an alignment exercise, one-question-at-a-time pacing, externalized state, TODO design, or implementation-request handoff."
---

# Design Session

Coordinate a composable `Design.Session`: a scoped human-agent convergence surface for moving from exploratory discussion into core design, TODO design, and implementation requests.

The durable model is `notes/index/111-Design.Session.md`. Read it when available and treat this skill as the operational workflow for that indexed concept.

This skill combines alignment-question pacing with design discussion behavior and adds artifact maintenance, facilitation, alignment/open-space tracking, component transitions, and user-gating of session state.

## Trigger Boundary

Use this skill when:

- The user explicitly starts a design session.
- Design work needs alignment through a guided one-question-at-a-time flow.
- A design discussion grows complex enough that multiple topics need tracking.
- The user wants externalized, user-gated state for a design conversation.
- The user wants to move from concept design into TODO design or implementation-request handoff.
- The user asks to discuss, interview, align, or converge on a design.

Do not use it for implementation work or generic status/reporting outside design work.

## Dependencies

- `agentos-live-note-base` — for file location and naming.
- `notes/index/111-Design.Session.md` — durable indexed model when present.

## References

Always load all `references/*.md` files. They contain detailed protocols for:

- `discussion.md` — design discussion behavior inside an active alignment question.
- `interview.md` — one-question-at-a-time alignment loop and `Alignment.Space` guidance.
- `core-design.md` — `*-core-design.md` artifact role, structure, and writing guidance.
- `todo-design.md` — `*-todo-design.md` artifact role, structure, and writing guidance.
- `impl-req.md` — how a session produces or feeds an implementation request.
- `session-status.md` — status report format, next-item selection criteria.
- `uncommitted-work.md` — tracking uncommitted discussion, continue semantics.
- `capture-audit.md` — chat-to-artifact sync verification.

## Core Model

Prefer this flow:

```txt
Core.Design -> TODO.Design -> Impl.Req
```

This is not a rigid waterfall. It is an authority and dependency direction: implementation should be downstream of explicit design/alignment material.

### Components

- `Design.Session.Core.Design` — conceptual design layer; stages a fragment of `Design.Target.Model`.
- `Design.Session.TODO.Design` — task-design layer; defines how to move `Current.Implementation` closer to the staged target fragment.
- `Impl.Req` — implementation-request artifact; carries execution-facing scope, constraints, vertical slices, ordered work when useful, validation, risks, review points, and deviation triggers.

A session may use one, two, or three surfaces depending on scope:

- `*-core-design.md`
- `*-todo-design.md`
- `*-impl-req.md`

Do not create a component just because it exists in the model. Create or update a component when the conversation needs that component.

The components can be used independently. A session may only produce `Core.Design`, start with `TODO.Design` when core alignment already exists, or produce an `Impl.Req` directly when enough design alignment is already available.

## Workflow Rhythm

A `Design.Session` is a discussion/interview/convergence workflow with artifact consolidation points:

```txt
explicit invocation
-> propose session frame
-> user approves artifact creation
-> agent asks one highest-leverage alignment question
-> discuss freely inside that question
-> converge enough for now or identify open space
-> propose capture/state change/action
-> user approves writes
-> user asks for next/continue
-> agent asks the next highest-leverage alignment question
-> close, transition, or spawn implementation artifact on user direction
```

Fundamental rule: the agent controls organization; the user controls advancement.

The agent is responsible for keeping the process organized. The user decides what is sufficient, what is settled, and where to go deeper.

Core design is the natural starting gravity because Agentos designs first in ontology/index space and then moves toward implementation. Still, the session may scale a topic across components in whatever order the work requires.

A `Design.Session` is an alignment exercise paced by one agent-selected question at a time. The agent chooses the highest-leverage unresolved question and must include a recommended answer or direction. The user controls advancement: the agent may suggest moving to another question, but must not present the next full question until the user explicitly asks for it.

## Items

Items are the selected focus set for a session component. They are not a registry of every relevant concept or task.

Items may be completely new or may revisit existing concepts, notes, tasks, or decisions. In `Core.Design`, an item represents the design work this session has done around that selected concept or topic. In `TODO.Design`, an item represents task/action design work derived from the design.

`Impl.Req` is not item-focused by default. It uses the implementation-request format and guidance from `agentos-artifact-impl-req`.

The item set grows naturally as the session reveals what needs focused design work. Each item should contain only the amount of design the user thinks is sufficient for the current session pass.

## Agent Roles

The agent operates in two simultaneous roles:

### Alignment Questioner

- Control organization, not advancement: keep the alignment path coherent, but wait for the user to advance to the next full question.
- Bootstrap the session when needed with one useful opener, such as "What are we designing?" or "What references should anchor this session?"
- Select the highest-leverage unresolved question from `Alignment.Space`.
- Ask one question at a time.
- Include the agent's recommended answer or direction with every question.
- Explore codebase, notes, artifacts, transcripts, or other references instead of asking the user when the question can be answered from evidence.
- Do not present the next full question until the user explicitly asks for it.

### Discussant

- Propose concrete ideas, critique constructively, and surface tradeoffs.
- Update only the impacted design section or active question.
- Add only the most useful 1-2 high-leverage points per round.
- Surface open risks and lightweight pressure tests.
- Avoid repeating the same framing.
- Stay in discussion around the active question until the user resolves it, parks it, or asks for the next question.

### Facilitator

Additionally:

- Track which items are being discussed and notice when the conversation moves between topics.
- Track which component is active: `Core.Design`, `TODO.Design`, or `Impl.Req`.
- Distinguish settled design material from `Design.Open.Space`.
- Notice when user-settled material should be captured in `Design.Alignment.Core`.
- Notice when discussion has moved from core design into TODO design, or from TODO design into implementation-request handoff.
- Use `Alignment.Sufficiency` to provide well-timed recommendations, warnings, or status notes without treating the agent's judgment as a user gate.
- Notice when new topics emerge that should be added to the plan. After 2-3 exchanges on an unlisted topic, proactively suggest adding it.
- Notice when a topic has converged enough to move to `converging`, or suggest closing.
- Notice when the conversation drifts to an orthogonal concept for 2+ turns — flag it.
- Surface these observations naturally in chat — do not wait for the user to notice.

## User-Gating Protocol

Session work has separate gates:

- The agent may freely discuss, propose, and suggest in chat.
- `Design.Alignment.Core` is user-gated: the agent can propose candidate material, but only the user can settle it into the core.
- `User.Gated.Trigger` means the write path begins only after an explicit user trigger.
- `User.Gated.Writing` means the agent must present exact proposed text or diff before writing.
- The agent can update observational states (`fresh → in-progress`, `in-progress → converging`) without asking when a write is already authorized by the active workflow.
- User gates include closing items, reopening items, adding new items, updating item content, reverting states, and settling material into `Design.Alignment.Core`.
- Before gated changes, state what you want to change and wait for approval.
- Keep proposals concise: "I'd like to add [item] to the plan and close [other item]. OK?"

## Lifecycle

### Starting A Session

1. Confirm with the user that a design session is appropriate.
2. Identify the initial component. Default to `Core.Design` unless the user is explicitly designing work to do or requesting implementation.
3. Propose the session frame in chat: motivation, active component, likely references, and initial focus set if known. Do not create the file yet.
4. On user approval, create the appropriate component artifact.
5. Ask the first alignment question. If context is vague, bootstrap with one opener before narrowing.

### During The Session

1. Ask one alignment question, including a recommended answer or direction.
2. Discuss that question using the behavior in `references/discussion.md`.
3. Track settled material, rejected options, assumptions, references, implications, and open space in `Alignment.Space`.
4. Periodically surface facilitation observations:
   - "This feels like a new topic — should I add it to the plan?"
   - "I think [item] is converging — close it or keep going?"
   - "This sounds like TODO design now — should I capture it in the TODO component?"
   - "This looks ready for an impl-req — should I draft one from the current design?"
   - "We can proceed, but alignment is still thin on [axis]; I can keep decisions conservative unless you want to settle that first."
   - "We've been on this adjacent topic for a while — worth its own item, or part of [existing item]?"
5. Update session artifacts only on user approval.
6. Items don't need to be discussed in order — follow the conversation's natural flow.
7. Keep implementation-request handoff downstream of `Core.Design` and `TODO.Design` unless the user explicitly chooses to proceed from open space.
8. When the session rejects a path or defines scope boundaries, preserve the negative decision in the relevant component. Negative decisions are not noise; they prevent stale ideas from being reintroduced as open options.
9. After a meaningful capture, closure, or action, return to the big picture and help the user choose the next focus.
10. If the next highest-leverage question is clear, say so briefly, but wait for the user to ask for `next`, `continue`, or equivalent before presenting it.

### Closing Items

When the agent thinks an item is ready to close:

- Suggest in chat: "I think [item] is sufficient for this session. Here's what I'd write: [brief summary]. Close it?"
- Wait for user confirmation.
- On approval, update the item status to `closed` and finalize the section content.
- "Closed" means sufficient for this session, not that the design is finished.

Closed items can still receive minor updates without reopening. Closed does not mean frozen.

Reopening is an explicit user action that signals: "I want to directly work on this item again — significant work remains." It is not needed for small tweaks.

### Scope Drift

When the conversation consistently moves away from the plan:

- Gently flag it: "We've been exploring [topic] which isn't in the plan. Should I add it, or should we refocus?"
- Do not enforce — the user decides.
- If the drift is substantial enough to warrant a separate session, suggest it but don't insist.

### Ending A Session

A session ends when:

- All items are closed.
- The user explicitly ends it.
- The user asks to produce a different artifact (e.g., `design-summary`, `impl-req`).
- The user asks to execute an `Impl.Req` or otherwise switches to implementation.

On ending:
- Suggest an End Log entry summarizing: items closed, items still open, any deferred work.
- Brief "what's next" nudge: suggest the most natural follow-up (e.g. "promote these concepts into index notes", "draft TODO design", "produce an impl-req", "start implementation", or simply "this can rest as reference").

## Upgrade From Lightweight Discussion

When a lightweight design discussion grows complex:

- The agent may suggest: "This is getting multi-threaded — want to upgrade to a design session so we can track the topics?"
- If the user agrees, create the appropriate session artifact capturing the current state of the discussion (topics identified so far, any decisions already made).
- Continue from there.

## Compatibility

`agentos-design-session` is the preferred skill for new Agentos design work. Standalone design discussion and design interview behavior should be treated as internal behavior of this skill unless the user explicitly asks for a legacy/simple mode.

## Interaction Rules

- All discussion happens in chat — the artifacts are the externalized state, not the conversation medium.
- Use artifacts as the durable state. Do not rely on fragile chat memory when a session decision, TODO design, or implementation request should be reusable.
- Keep facilitation observations brief and natural. Don't interrupt flow for minor state updates.
- When proposing document changes, be specific but concise.
- Don't force linear progression through items — follow the conversation.
- Don't force linear progression through questions — choose the highest-leverage unresolved question, then wait for the user to explicitly advance.
- The plan is a tool for the human, not a constraint on the discussion.

## Evidence Priority

1. The user's current explicit directions.
2. Accepted design decisions from the current session (closed items).
3. The active session artifacts' current state.
4. Current codebase state and diffs.
5. Stable project surfaces such as index notes, project `AGENTS.md`, active skills, CLI help, documented spec surfaces, or other source-of-truth project artifacts.

## Evidence-Backed Judgment

The agent should try to ground its recommendations, warnings, sufficiency judgments, and capture proposals in evidence.

Valid evidence includes:

- direct user instructions or approvals
- accepted decisions from the current session
- active session artifacts
- current codebase state and diffs
- stable project surfaces such as index notes, project `AGENTS.md`, active skills, CLI help, documented spec surfaces, or other source-of-truth project artifacts

Evidence does not replace judgment. The agent should still recommend an answer or direction, but should make clear what the recommendation is based on when the decision materially affects the design, task shape, or implementation handoff.

## Example Prompts That Should Trigger This Skill

- "let's start a design session"
- "this needs a session" (in context of design work)
- "upgrade to a session"
- "let's track these topics"
- "let's discuss" (when the subject is design work)
- "interview me" (when the subject is design work)
- "align on this design"

## Exit Condition

Exit this skill when the session ends, or when the user switches to implementation, a different skill, or a different task.
