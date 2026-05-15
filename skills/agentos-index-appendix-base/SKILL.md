---
name: agentos-index-appendix-base
description: Define and operate the Agentos Index appendix protocol for `notes/appendix/`. Use when creating, updating, routing, promoting, or reviewing appendix notes or `Kernel.Block:Appendix` blocks.
---

# Agentos Index Appendix Base

Operational baseline for `Index.Appendix`.

This skill derives from `skills/agentos-index/references/appendix.md` and the durable index model in `notes/index/`. If this skill conflicts with the index or the `agentos-index` reference package, report the drift and follow the durable source.

## Scope

- This skill defines only the `notes/appendix/` surface protocol.
- It does not define concepts independently from `notes/index/`.
- It does not replace `agentos-index`, `agentos-index-writer`, or `agentos-index-doctor`.
- It keeps appendix work anchored to paired `Kernel.Block:Index` blocks.

## Surface Identity

- `Index.Appendix` is stable design truth for durable depth.
- It is part of the Agentos Index system — the `Extended.Index.Scope`.
- It is not part of `Context.Minimal.Surface`.
- Agents load appendix material only when extended reasoning, examples, tradeoffs, rationale, or provenance are useful.

## Placement Rules

- Fundamentals belong in `notes/index/` as `Kernel.Block:Index`.
- Appendix depth belongs in `notes/appendix/` as `Kernel.Block:Appendix`.
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
- Canonical filename shape is `Concept.Name-appendix.md`.
- The concept name in the filename is the `Dotted.Name` of the owning concept or concept cluster.
- No numeric prefix — the `Dotted.Name` is the stable handle.
- Discovery is implicit — agents check if `notes/appendix/Concept.Name-appendix.md` exists by convention.
- No outlink from the index block is required for discovery.
- Created on demand — no empty files, no pre-planning.

## Routing

- Each appendix note corresponds to an owning concept or tight concept cluster.
- Related appendix blocks should cluster in the same appendix note when they extend related concepts.
- Discovery is implicit through the naming convention — no explicit routing table needed.
- `000-index.md` remains a minimal router; do not turn it into a full appendix table of contents.

## Promotion

When promoting from `Kernel.Block:Design.Session`:

- fundamentals compress into the paired `Kernel.Block:Index`
- `### appendix` material promotes to `Kernel.Block:Appendix`
- `### meta` does not promote unless it contains separate durable design truth

Preserve user wording when the wording carries design judgment.

## Write Gates

- Appendix notes inherit `User.Gated.Index` behavior.
- Agents may read and propose freely.
- Writing requires explicit user initiation.
- Committing content requires user approval of the exact wording.
- Use the `agentos-index-writer` loop for gated writes until a dedicated appendix writer exists.

## Review Checklist

- Is this material durable design depth rather than fundamentals or workflow?
- Is there a paired index concept?
- Does the filename follow `Concept.Name-appendix.md` convention?
- Does the block avoid becoming a transcript, progress log, or duplicate definition?
