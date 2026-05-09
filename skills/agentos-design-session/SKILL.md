---
name: agentos-design-session
description: "Coordinate a layered Design.Session for non-linear human-agent design convergence. Use when design work needs externalized state, explicit alignment/open-space tracking, TODO design, or execution planning. Layers on top of agentos-design-discussion."
---

# Design Session

Coordinate a layered `Design.Session`: a scoped human-agent convergence surface for moving from exploratory discussion into core design, TODO design, and execution plans.

The durable model is `notes/index/111-Design.Session.md`. Read it when available and treat this skill as the operational workflow for that indexed concept.

This skill layers on `agentos-design-discussion` for conversational behavior and adds artifact maintenance, facilitation, alignment/open-space tracking, layer transitions, and user-gating of session state.

## Trigger Boundary

Use this skill when:

- The user explicitly starts a design session.
- A design discussion grows complex enough that multiple topics need tracking.
- The user wants externalized, user-gated state for a design conversation.
- The user wants to move from concept design into TODO design or execution planning.
- Upgrading from `agentos-design-discussion` when scope expands.

Do not use it for quick, focused design discussions (use `agentos-design-discussion`), implementation work, or structured interviews.

## Dependencies

- `agentos-design-discussion` — for conversational behavior and discussion principles.
- `agentos-live-note-base` — for file location and naming.
- `notes/index/111-Design.Session.md` — durable indexed model when present.

## References

Always load all `references/*.md` files. They contain detailed protocols for:

- `core-design.md` — `*-core-design.md` artifact role, structure, and writing guidance.
- `todo-design.md` — `*-todo-design.md` artifact role, structure, and writing guidance.
- `exec-plan.md` — `*-exec-plan.md` artifact role, structure, and writing guidance.
- `session-status.md` — status report format, next-item selection criteria.
- `uncommitted-work.md` — tracking uncommitted discussion, continue semantics.
- `capture-audit.md` — chat-to-artifact sync verification.

## Core Model

Prefer this flow:

```txt
Core.Design -> TODO.Design -> Exec.Plan
```

This is not a rigid waterfall. It is an authority and dependency direction: execution should be downstream of explicit design/alignment material.

### Layers

- `Design.Session.Core.Design` — conceptual design layer; stages a fragment of `Design.Target.Model`.
- `Design.Session.TODO.Design` — task-design layer; defines how to move `Current.Implementation` closer to the staged target fragment.
- `Design.Session.Exec.Plan` — concrete execution layer; plans the actual work derived from TODO design.

A session may use one, two, or three files depending on scope:

- `*-core-design.md`
- `*-todo-design.md`
- `*-exec-plan.md`

Do not create a layer just because it exists in the model. Create or update a layer when the conversation needs that layer.

## Agent Roles

The agent operates in two simultaneous roles:

### Discussant

Same as `agentos-design-discussion`:

- Propose concrete ideas, critique constructively, surface tradeoffs.
- Maintain delta updates, don't repeat the same framing.
- Balance exploration and convergence.
- Pressure-test proposals lightly.

### Facilitator

Additionally:

- Track which items are being discussed and notice when the conversation moves between topics.
- Track which layer is active: `Core.Design`, `TODO.Design`, or `Exec.Plan`.
- Distinguish settled design material from `Design.Open.Space`.
- Notice when user-settled material should be captured in `Design.Alignment.Core`.
- Notice when discussion has moved from core design into TODO design, or from TODO design into execution planning.
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
2. Identify the initial layer. Default to `Core.Design` unless the user is explicitly designing work to do or an execution plan.
3. Propose the initial Motivation and Items Index in chat. Do not create the file yet.
4. On user approval, create the appropriate layer file.
5. Begin discussion on the first open item or let the user choose.

### During The Session

1. Discuss items following `agentos-design-discussion` principles.
2. Periodically surface facilitation observations:
   - "This feels like a new topic — should I add it to the plan?"
   - "I think [item] is converging — close it or keep going?"
   - "This sounds like TODO design now — should I capture it in the TODO layer?"
   - "We can proceed, but alignment is still thin on [axis]; I can keep decisions conservative unless you want to settle that first."
   - "We've been on this adjacent topic for a while — worth its own item, or part of [existing item]?"
3. Update session artifacts only on user approval.
4. Items don't need to be discussed in order — follow the conversation's natural flow.
5. Keep execution planning downstream of `Core.Design` and `TODO.Design` unless the user explicitly chooses to proceed from open space.

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
- The user asks to execute an `Exec.Plan` or otherwise switches to implementation.

On ending:
- Suggest an End Log entry summarizing: items closed, items still open, any deferred work.
- Brief "what's next" nudge: suggest the most natural follow-up (e.g. "promote these concepts into index notes", "draft TODO design", "produce an exec plan", "start implementation", or simply "this can rest as reference").

## Upgrade From Design Discussion

When a `design-discussion` grows complex:

- The agent may suggest: "This is getting multi-threaded — want to upgrade to a design session so we can track the topics?"
- If the user agrees, create the appropriate session artifact capturing the current state of the discussion (topics identified so far, any decisions already made).
- Continue from there.

## Interaction Rules

- All discussion happens in chat — the artifacts are the externalized state, not the conversation medium.
- Use artifacts as the durable state. Do not rely on fragile chat memory when a session decision, TODO design, or execution plan should be reusable.
- Keep facilitation observations brief and natural. Don't interrupt flow for minor state updates.
- When proposing document changes, be specific but concise.
- Don't force linear progression through items — follow the conversation.
- The plan is a tool for the human, not a constraint on the discussion.

## Evidence Priority

Same as `agentos-design-discussion`:

1. The user's current explicit directions.
2. Accepted design decisions from the current session (closed items).
3. The active session artifacts' current state.
4. Current codebase state and diffs.
5. Relevant index notes, especially `111-Design.Session.md`.

## Example Prompts That Should Trigger This Skill

- "let's start a design session"
- "this needs a session" (in context of design work)
- "upgrade to a session"
- "let's track these topics"

## Exit Condition

Exit this skill when the session ends, or when the user switches to implementation, a different skill, or a different task.
