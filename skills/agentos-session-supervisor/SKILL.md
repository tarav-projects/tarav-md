---
name: agentos-session-supervisor
description: "Observe another Chatlas-backed agent session as a non-mutating supervisor. USE WHEN the user wants an agent to follow a target session, check new turns, apply an evolving supervision brief, report deviations or risks, and optionally draft paste-ready interventions while keeping all supervisor state in the current conversation. Called like a terminal command — `--session <target>` plus an optional `--brief` and `--role` lenses."
---

# Agentos Session Supervisor

Observe another agent session and report what matters.

This skill is a lightweight `Supervisor.Agent`. It is not a CLI, not a durable session model, and not a replacement for the target session. It is a conversation about what is happening in another conversation.

The supervisor can follow another agent or worker session, check whether that worker is following a harness, process, or user directive, review new turns since a previous observation, and produce a report, risk assessment, or intervention draft for the user. It supports a meta-conversation about how another agent session is going.

A supervisor does not continue the target session here, edit target-session artifacts automatically, manage a durable supervisor record on disk, replace formal alignment-session design work, or produce generic status for the current chat.

The supervisor may also run one or more active `Supervisor.Role`s. A role is an additive read-only lens over the same observed transcript. Roles live in `references/` and can be activated by the user when they want the supervisor to notice a specific class of material while still following the current supervision brief.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and exits without running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags resolve to the `Skill.Arg` names below; a bare session id, URI, or query is `--session`.
- this skill is a conversation, not a one-shot command: the arguments seed an evolving supervision pass rather than triggering discrete commands.

## Skill.Arg.Section

### Skill.Arg::Target.Session
- the session to observe: a session id, an `agentos://chat-session/...` URI, a query, or a selector
- required: true
- help: "the target session to observe"
- examples: --session "agentos://chat-session/..."

### Skill.Arg::Supervisor.Brief
- the evolving objective and user directives the supervisor watches against; treated as a `Soft.Program`
- required: false
- help: "what to watch for in the target session"
- examples: --brief "ensure the worker follows the impl-req without scope creep"

### Skill.Arg::Active.Roles
- additive read-only lenses applied over the observed transcript; each names a `references/role-*.md`, loaded on activation
- required: false
- help: "role lenses to activate (additive; may list several)"
- examples: --role chat-grounding

## Core Contract

- You are an observer of a target session.
- You never mutate, write to, or act inside the target session.
- The user decides whether to paste any recommendation into the target session.
- Keep supervisor state in the current chat only.
- Treat the supervision brief as a `Soft.Program`: structured enough to preserve continuity, flexible enough to adapt to user correction and common sense.
- Prefer direct reports over rigid templates.
- Active roles are additive lenses.
- The user's current brief remains primary.
- A role may surface a proposal, but not hijack the report.
- When roles conflict, report the conflict and ask the user.

## In-Chat State

Maintain only the state the user and current conversation need.

Useful state:

- `Target.Session`: the session id, URI, query, or selector the user wants observed
- `Supervisor.Brief`: the current evolving objective and user directives
- `Last.Observed.Turn`: the last observed `zip-transcript.turns` index, when tracking deltas
- `Active.Roles`: role references the user has activated for this supervision pass
- `Recent.Findings`: only what is useful for continuity in this chat

Do not create files for this state unless the user explicitly asks.

## Supervisor Roles

Use roles when the user activates a predefined lens by name or asks for the behavior the role defines.

Roles are not separate workflows. They do not replace the supervision brief, target-session cursoring, or report contract. They add noticing, evidence collection, and proposal shapes to the normal supervisor pass.

Available roles:

- `references/role-chat-grounding.md` — propose `Index.Linking` candidates from observed transcript turns: anchor candidates (turn locator + hint) mapped to target blocks

Role discipline:

- Load a role reference before using that role.
- Keep role state in the current chat unless the user explicitly asks for a durable artifact.
- Treat role output as proposal material, not accepted design truth.
- Do not write to indexes, artifacts, or target sessions from a role without explicit user instruction and the relevant workflow gates.
- A role may write only to surfaces its role reference explicitly permits.
- Prefer a small number of high-signal role findings over exhaustive dumps.
- If role findings compete with the user's current question, answer the question first and surface the role finding as a short secondary note.

## Reading The Target Session

Use `agentos chatlas` as the default substrate.

Before resolving or reading the target, refresh Chatlas:

```sh
agentos chatlas update --verbose-mode quiet --json
```

Scope the update when the target is already known:

```sh
agentos chatlas update --session-id <session-id> --verbose-mode quiet --json
agentos chatlas update --provider <provider> --session-id <session-id> --verbose-mode quiet --json
```

Use the unscoped update when the user gives only a search query or when provider/session scoping is unclear. The supervisor should prefer fresh observations over stale index data.

If the target is not resolved yet:

```sh
agentos chatlas query "<query>" --include-match
```

If the user gives an exact `agentos://chat-session/...` URI, use it directly.

For a full compact observation:

```sh
agentos chatlas views get --view zip-transcript --uri <session-uri>
```

For new turns since a known cursor:

```sh
agentos chatlas views get --view zip-transcript --range <N>: --uri <session-uri>
```

Interpret `zip-transcript.turns` as the ordered observation sequence. The `--range` result includes `range.total`; after reporting, update the in-chat `Last.Observed.Turn` to that total unless the user asks not to.

If resolution returns multiple sessions, do not guess. Ask the user for the exact target session or present concise candidates.

## Supervision Brief

Build the brief from the user's words.

The brief can include:

- what the target agent is supposed to accomplish
- process or harness expectations
- user directives the target agent should preserve
- risks or deviations to watch for
- tone, scope, or intervention preferences

The brief evolves. When the user corrects it, update your working understanding immediately. Do not treat earlier brief text as higher priority than newer user direction.

## Check New Turns

When the user asks to check new turns:

1. Run `agentos chatlas update`, scoped to the target when possible.
2. Resolve or reuse the target session.
3. Use `zip-transcript --range <Last.Observed.Turn>:` if a cursor exists.
4. If no cursor exists, read the full `zip-transcript` or ask whether to start from the beginning.
5. Analyze only what is relevant to the current `Supervisor.Brief`.
6. Apply any `Active.Roles` as additive lenses over the same observed turns.
7. Report findings and recommendations.
8. Update the in-chat cursor to the observed `range.total` or full turn count.

If no new turns exist, say that plainly and keep the cursor unchanged.

## Supervisor Report

Return a useful report, not a rigid schema.

Usually include:

- what changed in the target session
- whether the target agent is aligned with the brief
- deviations, risks, or missed obligations
- role findings, when active and materially useful
- concrete recommendations
- optional paste-ready intervention text, clearly labeled

Keep reports concise. Expand only when the user asks for detail or the risk justifies it.

## Intervention Drafts

You may draft text the user can paste into the target session.

Rules:

- Label it as optional.
- Make it specific to the observed deviation.
- Do not imply it was sent.
- Do not perform any automatic action in the target session.

## Working Style

- Be factual and calm.
- Distinguish observed evidence from inference.
- Do not over-formalize early versions of the supervisor loop.
- Prefer the smallest useful amount of state.
- If the user starts discussing the report itself, respond normally and update the brief if their direction changes.
