# Interview

A `Design.Session` is an alignment exercise paced by one agent-selected question at a time.

Fundamental rule: the agent controls organization; the user controls advancement.

The agent chooses the highest-leverage unresolved question and keeps the alignment path organized. The agent may suggest that the next question is ready, but must not present the next full question until the user explicitly asks for `next`, `continue`, `next question`, `go on`, or equivalent.

## Alignment.Space

`Alignment.Space` is the working map of the session's alignment state.

Track:

- settled answers
- unresolved questions
- active assumptions
- rejected or superseded options
- relevant references
- user taste and judgment
- implications for `Core.Design`, `TODO.Design`, or `Impl.Req`
- material that belongs in `Design.Open.Space`

`Alignment.Space` is not automatically written verbatim. Consolidate it into the active artifacts when it becomes useful durable state and the user approves the write.

## Question Selection

Ask the highest-leverage unresolved question first.

Prefer questions that:

- unlock multiple downstream choices
- clarify user taste, authority, or scope
- separate settled material from open space
- determine whether work belongs in `Core.Design`, `TODO.Design`, or `Impl.Req`
- identify relevant references or evidence
- prevent likely implementation drift

If context is insufficient, bootstrap with one opener:

- "What are we designing or deciding?"
- "What references should anchor this session?"
- "What is the current artifact or code surface we should inspect first?"

If a question can be answered by inspecting code, notes, artifacts, transcripts, or other available evidence, inspect that evidence instead of asking the user.

## Question Format

Use plain chat text. Do not use UI forms.

Default format:

```txt
Question: [one highest-leverage question]
Why now: [why this is the right next alignment point]
Recommended answer: [the agent's recommended answer or direction]
Evidence: [only when useful: user instruction, code/artifact evidence, or stable project surface]
```

The agent must recommend an answer or direction. The recommendation may be provisional when evidence is thin, but it should still give the user something concrete to accept, reject, or refine.

Use evidence to support the recommendation when the decision materially affects design direction, task shape, or implementation handoff. Evidence may come from direct user instruction, inspected codebase state, active session artifacts, or stable project surfaces such as index notes, project `AGENTS.md`, active skills, CLI help, or documented spec surfaces.

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
