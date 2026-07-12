# Interview

A `What.Design.Session` is an alignment exercise paced by one agent-selected question at a time.

Fundamental rule: the agent controls organization; the user controls advancement.

The agent chooses the highest-leverage unresolved question and keeps the alignment path organized. The agent may suggest that the next question is ready, but must not present the next full question until the user explicitly asks for `next`, `continue`, `next question`, `go on`, or equivalent.

In `Alignment.Loop::What`, asking the next full design question is an `Alignment.Maintenance.Turn`. Turn switching is user-gated.

## Canonical Flow

```txt
agent asks one design question
-> user/agent discuss until convergence, parking, or rejection
-> user/agent consolidate the result
-> update state if useful and approved
-> user asks for next/continue
-> agent asks one next design question
```

During discussion, the agent remains in `Alignment.User.Turn`: follow the user's thread, respond directly, and surface important alignment issues only when they materially affect the discussion.

## Design.Space

`Design.Space` is the working map of the session's alignment state.

Track:

- settled answers
- unresolved questions
- active assumptions
- rejected or superseded options
- relevant references
- user taste and judgment
- implications for `Design.Index`, `Session.Notes`, or `Impl.Req`
- material that belongs in open space

`Design.Space` is not automatically written verbatim. Consolidate it into the session artifact when it becomes useful working state and the user approves the write.

## Question Selection

Ask the highest-leverage unresolved question first.

Prefer questions that:

- unlock multiple downstream choices
- clarify user taste, authority, or scope
- separate settled material from open space
- determine whether work belongs in `Design.Index`, `Session.Notes`, or `Impl.Req`
- identify relevant references or evidence
- prevent likely implementation drift

If context is insufficient, bootstrap with one opener:

- "What are we designing or deciding?"
- "What is the current artifact or code surface we should inspect first?"

Anchors come from `Design.Session.Setup`, not from the user. `Concept.Discovery` has already surfaced the existing and neighbor blocks, so the agent **proposes** them as anchors for the user to confirm, redirect, or extend.

If a question can be answered by inspecting code, notes, artifacts, transcripts, or other available evidence, inspect that evidence instead of asking the user — `Hard.Evidence` beats agent assumption, and a premature question burns a slot (see `design-anti-patterns.md` / premature questions).

## Question Format

Use plain chat text. Do not use UI forms. Communicate in `Kernel.Writing` — orthogonal bullet lines, direct language (see `writing-craft.md`).

A question turn on a defined subject pairs a `Design.Block` with the question: the block first as actionable context, then the question. This turn shape is `Designer.Turn.Kernel.Form`.

```txt
### Subject.Name
- orthogonal fundamental
- orthogonal fundamental
#### meta
- open: [unresolved point]

Question: [one highest-leverage question]
Why now: [why this is the right next alignment point]
Recommended answer: [the agent's recommended answer or direction]
Evidence: [only when useful: user instruction, code/artifact evidence, or stable project surface]
```

Every new question on a defined subject is accompanied by its block. Pure openers are exempt — they create the first subject, so no block exists yet.

The agent must recommend an answer or direction. The recommendation may be provisional when evidence is thin, but it should still give the user something concrete to accept, reject, or refine.

Use `Hard.Evidence` to support the recommendation when the decision materially affects design direction, task shape, or implementation handoff. Evidence may come from direct user instruction, inspected codebase state, active session artifacts, or stable project surfaces such as `Index.Block`s, project `AGENTS.md`, active skills, CLI help, or documented spec surfaces. See `writing-craft.md` for the full evidence discipline.

## Discussion Fork

After asking a question, stay on that question.

The user may:

- answer directly
- critique the recommendation
- ask for more context
- discuss alternatives
- delegate the decision to the agent
- park the question
- ask for the next question

Do not advance to a new full question until the user explicitly asks. While discussing the active question, use `discussion.md`.

## Capture

When useful convergence appears, propose a capture:

```txt
I think this is ready to capture under [surface/item].
Proposed capture: [brief exact text or summary]
Write it?
```

Only write after user approval. Keep the capture proportional to what the user considers sufficient for the current pass.

After capture, do not automatically ask the next full question. State that the next question is ready when useful, then wait for the user to ask for it.
