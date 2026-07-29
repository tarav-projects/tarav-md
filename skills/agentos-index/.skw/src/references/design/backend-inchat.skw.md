# Alignment.Backend::InChat::What

This detailed product-design module is owned by `agentos-index --design`.

> $kw: --dev-from references/index-context-assembly.skw.md

`Alignment.Backend::InChat::What` is the default `What.Design.Session` workflow.

It runs the session in chat without creating a file. The agent maintains visible session state by printing compact sections in the conversation.

## Role

Use `Alignment.Backend::InChat::What` when:

- the user starts a design session without asking for an artifact,
- the design is still exploratory,
- state is small enough to keep visible in chat,
- the user wants alignment before durable capture.

## Printed Sections

Use these sections when refreshing session state:

```md
## Session.Abstract

## Design.Index
```

Print only what is useful. Do not dump all sections every turn.

## Section Use

- `Session.Abstract` — intent, current goal, active focus, state, and next recommendation.
- `Design.Index` — concept blocks with fundamentals, appendix material, and session meta.

## Workflow

1. Start in chat by proposing a session frame.
2. Ask one highest-leverage alignment question.
3. Discuss the answer using `discussion.md`.
4. Refresh the relevant printed section when useful.
5. Wait for the user to ask for `next`, `continue`, or equivalent before presenting the next full question.
6. Offer upgrade when state becomes too large, important, or handoff-ready.

## Printing Guidance

- Keep updates compact.
- Prefer delta updates over full restatements.
- Use headings only when session state needs to be visible.
- Make clear which material is settled, open, or agent-assumed.
- Do not imply that printed state is a durable project surface.

## Upgrade

Upgrade to `Alignment.Backend::Artifact::What` when:

- the user asks,
- the state needs durable capture,
- the session is becoming multi-threaded,
- future agents need to resume from the state,
- implementation handoff is approaching.

On upgrade, seed the artifact from the latest printed `Session.Abstract` and `Design.Index`.

> $kw: --from What.Design.Session
