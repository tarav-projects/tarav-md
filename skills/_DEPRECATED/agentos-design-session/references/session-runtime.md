# Session.Runtime.Loop

`Session.Runtime.Loop` is the shared runtime behavior for every `Design.Session`.

The backend may be `InChat.Session` or `Artifact.Session`, but the loop is the same:

```txt
session runtime -> user interaction -> session runtime -> user interaction -> ...
```

On each agent pass, the agent regains control and evaluates:

- the user's most recent interaction,
- the current session state,
- the agent's maintenance and alignment responsibilities.

The agent must carry the conversation with the user and maintain alignment around session state.

## Turn Modes

`Session.Runtime.Loop` has two turn modes:

- `User.Assistant.Turn`
- `Session.Maintenance.Turn`

Turn switching is user-gated. The agent may suggest switching modes, but should not silently switch from user-led discussion into session-maintenance mode.

## User.Assistant.Turn

`User.Assistant.Turn` is the default conversational mode.

The user’s current thread drives the response. The agent follows the user, discusses the active topic, and keeps the session fluid.

The maintenance loop is paused as the active driver, but the agent is not blind. It may surface important alignment issues when they materially affect the discussion.

Good reasons to surface an issue inside `User.Assistant.Turn`:

- the user contradicts current session state,
- a stale concept would mislead the current discussion,
- a missing distinction would cause bad convergence,
- an unresolved name is central to the current point,
- an artifact mismatch blocks useful continuation.

Do not use this mode to run broad status, capture audit, or maintenance sweeps unless the user asks.

## Session.Maintenance.Turn

`Session.Maintenance.Turn` is the session-driven mode.

The agent chooses one primary session move:

- ask the next design question,
- consolidate a converged result,
- propose a state update,
- surface a stale or misaligned issue,
- provide a status report,
- propose artifact upgrade,
- propose impl-req handoff,
- close, split, or park a topic.

Prefer one primary move per maintenance turn. Do not bundle every possible issue into one response.

After the move, return to `User.Assistant.Turn` unless the user asks for another maintenance action.

## Canonical Flow

The main workflow is:

```txt
agent: one design question
user/agent: discussion until convergence, parking, or rejection
user/agent: consolidate result
agent: update state if the backend requires it and the user approves
user: next / continue / status / interruption
agent: one next design question or requested interruption
```

## Backend Independence

The runtime loop does not depend on storage backend.

- In `InChat.Session`, state is printed and refreshed in chat.
- In `Artifact.Session`, committed state lives in the artifact and chat may contain uncommitted deltas.

The same alignment and maintenance responsibilities apply in both modes.
