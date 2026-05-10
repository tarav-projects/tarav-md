---
name: agentos-index-writer
description: "User-gated write path to the Agentos Index. Two gates: Write.Trigger.Gated (user initiates) and Content.Verbatim.Gated (user approves exact wording). Interactive per-block loop."
---

# agentos-index-writer

User-gated write path to the Agentos Index.

This is an `Alias.Skill` of the `agentos-index` `Skill.Package`.
Full design reference: `agentos-index/references/gating.md`

## When To Use

- the user explicitly asks to write, register, or update something in the index
- never auto-triggered by the agent — the user controls when writing happens

## Two Gates

- `Write.Trigger.Gated` — the user must explicitly initiate the write flow
- `Content.Verbatim.Gated` — the user must approve the exact wording of each block before commit

## Write Loop

For each block to write or modify:

```
1. Show proposed block (diff for updates, full block for new)
2. User reads, suggests changes
3. Show revised version
4. Repeat until user accepts
5. Move to next block
```

- each block gets individual attention — no bulk-approve
- the user always sees final form before anything touches files
- the loop is an alignment conversation — refine wording together

## Write Operations

- **new concept registration** — add entry to `001-ontology.md`
- **new block creation** — add block to existing or new note
- **block update** — modify existing block
- **new note creation** — create new index note (allocate prefix with `agentos stdlib prefix next`)

## Block Format

All writes must follow `Index.Block.Syntax`:

```markdown
## Dotted.Name

- [fundamental statement]
- [fundamental statement]
    - [qualification]

### index

- findability: [keywords]
- related: `Related.Name`
```

## Constraints

- write first, polish later — focus on meaning alignment, not perfect format
- linting runs after commit as maintenance, not during the write loop
- the user is the quality gate — the agent proposes, never decides alone
- `****` separators between H2-level blocks are mandatory
