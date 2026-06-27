---
name: agentos-index
description: "Workflow-neutral Package.Aux.Skill for the Agentos Index subsystem of agentos-pkg. USE WHEN you need index research, writing, diagnosis, testing, maintenance, or index design context."
---

# agentos-index

Workflow-neutral `Package.Aux.Skill` for the Agentos Index subsystem.

This skill is the public Batchy router for index work. It orients the caller to the subsystem by default and routes explicit operations such as `--search` and `--write` into named `Skill.Module`s.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and the public args without running.

## Skill.Arg.Section

### Skill.Arg:Search
- search the index through routing-first selective loading
- required: false
- help: "search the index and return cited context"
- examples: --search "Index.AGENTS.MD"

### Skill.Arg:Write
- work the approved write path for index or appendix edits
- required: false
- help: "use the index write path for approved edits"
- examples: --write "add Context.Hook"

## Boundary

- this skill is the canonical public entry surface for working with the Agentos Index system
- it remains a `Workflow.Neutral.Skill` when no explicit arg is selected
- it routes into named modules for concrete index operations instead of splitting those operations into separate public skills
- later modules such as diagnosis, testing, or grounding may be added without changing the public package entry surface

## What The Index Is

- the index is a `Soft.Programming.Language` for project knowledge
- it is an `Alignment.Surface` between humans and agents
- it contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized across flat index files and on-demand appendix depth
- agents operate it by collecting routing blocks, concept blocks, appendix material, and references relevant to the current task

## Router Table

| Situation | Module / Surface |
|---|---|
| Search for concepts, load cited context, or retrieve appendix depth | `references/search.md` |
| Work an approved index or appendix write | `references/write.md` |
| Understand the subsystem at package level | `agentos-pkg/index/`, `agentos-pkg/appendix/`, `agentos-pkg/references/` |
| Behavior examples for block writing quality | `agentos-pkg/references/index-block-catalog.md` |
| Behavioral testing of index entry paths or usage patterns | `agentos-testground` |

## Index Operating Behavior

An agent operating the index should:

- search routing surfaces first, then load only relevant concept blocks, appendix material, or references
- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- use writing/mutation only when the user has approved an index write

For delegated read-only research that protects the caller's context, use `Packages.Master.Agent` against the relevant package or packages.

## Skill Modules

- `references/search.md` — routing-first search, selective loading, appendix discovery, and citation behavior
- `references/write.md` — approved write path for index and appendix edits: gates, naming, placement, write loop, and maintenance

## When To Load This Skill

- when a session needs index-grounded context or a custom index research pass
- when writing, diagnosing, testing, or maintaining the index
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
