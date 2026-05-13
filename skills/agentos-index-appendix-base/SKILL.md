---
name: agentos-index-appendix-base
description: Define and operate the Agentos Index appendix protocol for `notes/appendix/`. Use when creating, updating, routing, promoting, or reviewing `Index.Appendix` notes or appendix blocks.
---

# Agentos Index Appendix Base

Operational baseline for `Index.Appendix`.

This skill derives from `skills/agentos-index/references/appendix.md` and the durable index model in `notes/index/`. If this skill conflicts with the index or the `agentos-index` reference package, report the drift and follow the durable source.

## Scope

- This skill defines only the `notes/appendix/` surface protocol.
- It does not define concepts independently from `notes/index/`.
- It does not replace `agentos-index`, `agentos-index-writer`, or `agentos-index-doctor`.
- It keeps appendix work anchored to paired `Index.Blocks`.

## Surface Identity

- `Index.Appendix` is stable design truth for durable depth.
- It is part of the Agentos Index system.
- It is not part of `Context.Minimal.Surface`.
- Agents load appendix material only when extended reasoning, examples, tradeoffs, rationale, or provenance are useful.

## Placement Rules

- Fundamentals belong in `notes/index/` as `Index.Blocks`.
- Appendix depth belongs in `notes/appendix/` as `Index.Appendix.Blocks`.
- Operational workflow belongs in skills.
- Exact mechanical behavior belongs in code and CLI help.
- Temporary session state belongs in live notes.

Appendix material should not duplicate fundamentals. It should extend them.

## Appendix Material

Good appendix material includes:

- rationale and design reasoning
- examples and use cases
- pressure tests and edge cases
- tradeoffs, pros/cons, and rejected alternatives
- longer explanations that would make default grounding too heavy

Do not use appendix notes for transcripts, changelogs, task lists, dashboards, or implementation dumps.

## File Protocol

- Appendix notes live in `notes/appendix/`.
- Canonical filename shape is `NNN-short-topic.md`.
- `NNN` is a zero-padded 3-digit stable prefix.
- Appendix notes use the rolling `100-499` note range.
- Appendix notes receive their own prefix; do not mirror the paired index note number.
- The filename slug may mirror the paired index note or owning concept.
- Gaps are allowed. Do not renumber existing notes.

## Prefix Allocation

Expected command:

```sh
agentos stdlib prefix next --project-base <project-root-basename> --target notes/appendix --json
```

Rules:

- Use `--project /path/to/project --project-base <project-root-basename> --target notes/appendix --json` when outside the intended project tree.
- Do not assign ordinary appendix prefixes by manual inspection.
- Accept allocator output only when the reported range is `[100, 499]`.
- If the allocator reports another range, stop and report prefix-policy drift instead of creating the file.

## Routing

- Each appendix note should correspond to an owning index note or tight concept cluster when possible.
- Related appendix blocks should cluster in the same appendix note when they extend the same index note.
- The paired index note or block should link to appendix material through outlinks or an equivalent explicit pointer.
- `000-index.md` remains a minimal router; do not turn it into a full appendix table of contents by default.

## Promotion

When promoting from `Design.Index.Block`:

- fundamentals compress into the paired `Index.Block`
- `#### appendix` material promotes to `Index.Appendix.Block`
- `#### meta` does not promote unless it contains separate durable design truth

Preserve user wording when the wording carries design judgment.

## Write Gates

- Appendix notes inherit `User.Gated.Index` behavior.
- Agents may read and propose freely.
- Writing requires explicit user initiation.
- Committing content requires user approval of the exact wording.
- Use the `agentos-index-writer` loop for gated writes until a dedicated appendix writer exists.

## Review Checklist

- Is this material durable design depth rather than fundamentals or workflow?
- Is there a paired index concept or note?
- Is the appendix reachable from the paired index block or note?
- Was the prefix allocated through the CLI and confirmed in the `100-499` range?
- Does the block avoid becoming a transcript, progress log, or duplicate definition?
