---
name: agentos-index-writer
description: "Complete writer's guide for the Agentos Index. Covers index structure, writing philosophy, block format, write gates, the write loop, and post-write maintenance. The canonical doc surface for index writing knowledge."
---

# agentos-index-writer

The complete writer's guide for the Agentos Index — everything an agent needs to know to write well into the index, in one place.

This is a `Workflow.Neutral.Skill` of `agentos-pkg` — it provides knowledge about index writing without steering the caller into a writing action. Loading this skill makes the agent literate about index writing; whether writing happens is up to the user and the caller's workflow. [`Package.Aux.Skill`, `Workflow.Neutral.Skill`, `Natural.Placement`]

## Index Structure For Writers

The index is a flat set of concept blocks organized across anonymous files. [`Index.Architecture`, `Flat.Index.Architecture`, `Index.Surface.Layout`]

- **Flat index files** (`100-index.md`, `101-index.md`, ...) — anonymous containers of `Kernel.Block:Index` blocks, ~20 blocks per file. New blocks append to the last file — zero placement decisions.
- **Routing table** (`000-index.md`) — maps every `Dotted.Name` to its flat file. Updated when blocks are added, moved, or renamed. Entries annotate appendix depth: `Concept.Name[+N]` when appendix pages exist.
- **Appendix** (`appendix/Concept.Name-appendix.md`) — on-demand depth for any concept. Concept-named files, discovered implicitly — no outlink required. Relaxed space constraints.
- **Block separators** — `****` between H2-level blocks in flat files. Required.
- **Local index** (`notes/index/`) — project-local concepts with their own router (`001-index.md`) and range (`300-499`). Same format, same rules.

## Writing Philosophy

`Kernel.Writing` is the philosophy; the surface determines the budget. [`Kernel.Writing`, `Kernel.Block`]

- each line describes a fundamental dimension of the concept — multi-faceted view
- lines aim to be orthogonal — avoid redundancy, prefer independent facts
- language is direct — concise, no superfluous words
- completeness over clarity — every fundamental dimension has at least evidence in the block
- coverage over compression — losing a dimension is more costly than an extra line
- the filter: capture material that changes future judgment
- useful material can enter before it has mature structure — capture first, polish later

## Block Format

### Kernel.Block:Index

The loadable unit of meaning in the index. [`Kernel.Block:Index`, `Kernel.Block`]

- anchored by an H2 heading naming the concept in `Dotted.Notation`
- structure: **fundamentals** (conceptual core) + optional `### grounding` (chat evidence) + optional `### appendix` (extended) + optional `### meta` (non-conceptual: aliases, outlinks, status)
- tight space constraints — conceptual completeness under compression
- must carry enough signal for an agent to reason correctly about the concept
- 25-line hard cap per block (enforced by linter)
- `Content.Verbatim.Gated` — user approves exact wording before commit
- should NOT become transcripts, changelogs, task lists, or implementation dumps
- `Inline.Relatedness` — related `Dotted.Name` concepts blend into the text naturally; `Concept.Cite` is for relations that matter but don't read naturally

### Kernel.Block:Appendix

Extended depth that hangs off a concept. [`Kernel.Block:Appendix`]

- relaxed space constraints — depth over compression, no line-count ceiling
- content is not limited to conceptual depth — specs, regex, raw ideas, parked material all belong
- the discipline is at the insertion point — find the right concept, then write freely under it
- can be cleaned and integrated later — low friction first, curation second
- `Write.Trigger.Gated` only — user initiates, but exact wording is not gated
- discovery is implicit — agents check if `appendix/Concept.Name-appendix.md` exists
- scoped blocks: `Concept.B/Concept.A` views a concept from another concept's lens [`Concept.Scoping`]

## Write Gates

The index is gated by default — writing does not happen without explicit user control. [`Agentos.Index.System`]

- **`Write.Trigger.Gated`** — the user explicitly initiates the write. The agent does not start writing on its own. Asking "should I add this to the index?" is fine; opening an editor without approval is not.
- **`Content.Verbatim.Gated`** — the user approves the exact wording before it is committed. The agent proposes; the user settles. Implies `Write.Trigger.Gated`.

These gates support `Hugentic.Alignment` — the review point is where human judgment shapes the index.

## Pre-Write Concerns

Before a block is proposed, the writer considers: [`Natural.Placement`, `Dotted.Notation`, `Explicit.Namespace`]

1. **Overlap** — the full index is in context; existing concepts that cover the same idea may already exist. When overlap is found, extending the existing block may be better than creating a new one.
2. **Placement** — is this an index concept? Design knowledge → index. Operational procedure → skill or reference. Implementation detail → code. Extended depth → appendix.
3. **Naming** — `Dotted.Notation` with at least two parts. Dots provide context but are not a strict hierarchy. The routing table shows whether the name is already taken.
4. **Scoping** — some concepts belong in an `Explicit.Namespace`. Existing namespace `### meta` membership lists show current groupings.

## Write Loop

The write process for index blocks follows a propose-review cycle: [`Write.Trigger.Gated`, `Content.Verbatim.Gated`]

1. **Propose** — a full block draft (new) or a diff (update), following `Kernel.Writing` and block format.
2. **Review** — the user reads, suggests changes, asks questions.
3. **Revise** — incorporate feedback, present the updated block.
4. **Repeat** until the user accepts.
5. **Commit** — write to file and update the routing table in `000-index.md`.

For appendix writing, the loop is lighter — `Write.Trigger.Gated` applies, but exact wording is not gated. The writer has more freedom under relaxed constraints.

## Post-Write Concerns

After a block is committed: [`Index.Writer.Maintenance.Pass`, `Cited.Duplication`, `Placement.Balance`]

- **Routing table** — `000-index.md` reflects the new or renamed concept. `[+N]` annotation added if appendix pages exist.
- **Namespace** — if the concept belongs in an `Explicit.Namespace`, the namespace's `### meta` membership list is updated.
- **Maintenance pass** — for edits to existing blocks: mentions and citations of the edited concept across stable markdown surfaces are checked. Clear cited duplicates can be updated in the same approved write pass. Ambiguous drift or disagreement is surfaced as an issue, not silently resolved.

## Concept Map

Key concepts a writer should know, grouped by concern. Depth available through `Appendix.Discovery`.

- **Structure**: `Index.Architecture`, `Flat.Index.Architecture`, `Index.Surface.Layout`, `Index.Router`, `Distributed.Index`
- **Writing**: `Kernel.Writing`, `Kernel.Block`, `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Block:Design`
- **Naming**: `Dotted.Notation`, `Dotted.Parameterized.Notation`, `Explicit.Namespace`, `Concept.Scoping`
- **Placement**: `Natural.Placement`, `Placement.Balance`, `Placement.Heuristic`, `Cited.Duplication`, `Index.Empirical.Placement`
- **Discovery**: `Appendix.Discovery`, `Appendix.Pages`, `Concept.Cite`, `Inline.Relatedness`
- **Maintenance**: `Index.Writer.Maintenance.Pass`, `Index.Linter`, `Maintenance.System`, `Index.Concept.Coverage`
- **Gating**: `Write.Trigger.Gated`, `Content.Verbatim.Gated`
