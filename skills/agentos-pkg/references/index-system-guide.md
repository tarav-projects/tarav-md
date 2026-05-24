# Index System Guide

Compact tutorial for agents using the Agentos Index through `agentos-pkg`.

This is a cited duplicate of durable index concepts. If this reference disagrees with the index blocks, surface the drift and prefer updating the aligned surfaces rather than inventing a local rule.

Paths in this guide are relative to the `agentos-pkg` skill root unless explicitly absolute. For example, `index/000-index.md` means `skills/agentos-pkg/index/000-index.md`.

## What The Index Is

The Agentos Index is the package's conceptual working memory. It stores named concepts as `Kernel.Block:Index` blocks, routes them through `Index.Router`, and provides appendix depth through `Appendix.Discovery`. It is designed as a `Soft.Programming.Language`: natural-language syntax with operational semantics for agents. [`Agentos.Index.Notes`, `Kernel.Block:Index`, `Index.Router`, `Appendix.Discovery`, `Soft.Programming.Language`]

## Where To Start

- Start concept lookup at `index/000-index.md`.
- Use the routing table to find the flat index file that contains the concept.
- Load only the blocks, appendix pages, or references needed for the current task.
- For depth on `Concept.Name`, check `appendix/Concept.Name-appendix.md`.
- For local project context, also check `notes/index/001-index.md` when it exists. [`Index.Surface.Layout`, `Index.Router`, `Appendix.Discovery`, `Distributed.Index`]

## Main Surfaces

| Surface | Purpose |
|---|---|
| `index/000-index.md` | public routing table |
| `index/100-299*.md` | public compressed concept blocks |
| `appendix/Concept.Name-appendix.md` | public concept depth |
| `references/` | operational procedures and examples |
| `notes/index/001-index.md` | local project routing table when present |
| `notes/appendix/` | local project appendix when present |

## How Agents Should Use It

For research or grounding:

1. Read `index/000-index.md`.
2. Find the relevant concepts.
3. Load the relevant blocks and appendix pages.
4. Return a concise answer with concept citations.

For context collection:

1. Collect only the context needed for the caller's task.
2. Prefer a focused set of blocks over loading unrelated files.
3. If context may live in another package or local index, follow `Multi.Index.Operation`.
4. Qualify concepts from non-default indexes when needed, such as `<package>-pkg/Concept.Name`. [`Index.Agent`, `Multi.Index.Operation`, `Index.Depot`]

For writing:

1. Writes are user-gated.
2. Check overlap and natural placement before editing.
3. Update routing when adding, moving, or renaming blocks.
4. Run the maintenance pass: find mentions and cited duplicates of edited concepts.
5. Surface drift or disagreement as an issue unless the approved edit clearly updates the duplicate too. [`Natural.Placement`, `Cited.Duplication`, `Index.Writer.Maintenance.Pass`, `Placement.Balance`]

For diagnosis and testing:

- Use `references/maintenance.md` for linting, deduplication, promotion, and placement checks.
- Use `references/test-system.md` for index runtime tests.
- Use `agentos index linter` for deterministic surface checks.
- Semantic diagnosis belongs to the `agentos-index` function, not the linter alone. [`Index.Linter`, `Maintenance.System`]

## When To Load `agentos-index`

Load `agentos-index` when the task explicitly needs index research, writing, diagnosis, testing, maintenance, or index design context.

The caller may also perform the `Index.Agent` role directly when the index work is small enough to keep in the current context. Spawn or delegate when full-index work would pollute the caller's working context. [`Project.Index.Skill`, `Index.Agent`]

## Quick Concept Map

- Architecture: `Index.Architecture`, `Flat.Index.Architecture`, `Index.Surface.Layout`, `Distributed.Index`
- Runtime: `Index.Runtime`, `Index.Activation`, `Index.Agent`, `Multi.Index.Operation`
- Blocks: `Kernel.Block:Index`, `Kernel.Block:Appendix`, `Kernel.Writing`
- Discovery: `Index.Router`, `Appendix.Discovery`, `Appendix.Pages`, `Concept.Cite`
- Maintenance: `Natural.Placement`, `Placement.Balance`, `Cited.Duplication`, `Index.Writer.Maintenance.Pass`, `Index.Linter`
