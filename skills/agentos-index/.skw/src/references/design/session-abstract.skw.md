# Session.Abstract

This detailed product-design module is owned by `agentos-index --design`.

> $kw: --dev-from references/index-context-assembly.skw.md

`Session.Abstract` is the agent-maintained summary of what the design session is for.

It should let someone reopen the artifact and understand the session's intent without reading the whole file.

## Role

Use `Session.Abstract` for:

- session intent and goal
- current active focus
- relevant references
- current state of the artifact
- natural next move when known

## Shape

Prefer a short bullet block:

```md
## Session.Abstract

- intent: [what this session is trying to converge]
- active focus: [current question, concept, or section]
- references: [important notes, files, prior sessions, or none]
- state: [fresh / active / converging / parked / closed]
- next: [recommended next move, if known]
```

## Writing Guidance

- Keep it short.
- Update it after meaningful shifts in intent, focus, or state.
- Do not duplicate the full docs or log.
- Use plain language even when the rest of the artifact uses Dotted.Names.

## User Gate

`Session.Abstract` may be updated with other approved artifact updates.

If updating only the abstract, ask briefly unless the user has already authorized a status refresh or capture pass.
