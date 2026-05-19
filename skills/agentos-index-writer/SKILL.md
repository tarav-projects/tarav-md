---
name: agentos-index-writer
description: "User-gated write path to the Agentos Index. Reinforces writing quality: overlap checks, placement, block standards, and write gates."
---

# agentos-index-writer

User-gated write path to the Agentos Index.

This is an `Alias.Skill` of the `agentos-index` `Skill.Package`.
Write gates and quality guidance are defined in the index blocks: `Kernel.Block:Index`, `Kernel.Writing`, `Kernel.Block:Appendix`.

## When To Use

- the user explicitly asks to write, register, or update something in the index
- never auto-triggered by the agent — the user controls when writing happens

## Before Writing

Ground on these before proposing a block:

- **Overlap check** — the full index is in context, scan it for existing concepts that cover the same idea
- **`Natural.Placement`** — is this an index concept? Or does it belong in a skill, appendix, code, or live note?
- **`Kernel.Writing`** — how blocks are written: capture material that changes future judgment, capture first polish later
- **`Kernel.Block:Index`** — the block format: compact, loadable, grounding

## Write Gates

- `Write.Trigger.Gated` — the user must explicitly initiate the write
- `Content.Verbatim.Gated` — the user must approve the exact wording before commit

## Write Loop

For each block:

1. Propose block (git diff style for updates, full block for new)
2. User reviews, suggests changes
3. Revise and show again
4. Repeat until user accepts
5. Write to file and update `000-index.md` routing table

## After Writing

- Update the routing table in `000-index.md` with the new concept
- Check if the concept needs an `Explicit.Namespace` or belongs in an existing one
