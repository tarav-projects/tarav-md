---
name: agentos-index
description: "Workflow-neutral Package.Aux.Skill for the Agentos Index subsystem of agentos-pkg. Load for index research, writing, diagnosis, testing, maintenance, or index design context."
---

# agentos-index

Workflow-neutral `Package.Aux.Skill` for the Agentos Index — a `Soft.Programming.Language` for project knowledge.

This skill orients the caller to the index subsystem without forcing an operation. The Agentos Index design reference lives in `agentos-pkg/index/`, `agentos-pkg/appendix/`, and `agentos-pkg/references/`.

Always load `agentos-pkg/references/index-system-guide.md` with this skill. It is the compact tutorial for the index architecture and workflows.

## What The Index Is

- the index is a `Soft.Programming.Language` — soft syntax (natural language), programming semantics (execution behavior)
- it is the `Alignment.Surface` between humans and agents — the shared ground where both sides align on what things mean
- it contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized in flat index files
- agents operate the index by collecting the relevant routing blocks, concept blocks, appendix material, and references for the current task

## References

| Reference | Covers |
|---|---|
| `agentos-pkg/references/index-system-guide.md` | compact tutorial — index architecture, surfaces, common workflows, citations |
| `agentos-pkg/references/launch-runtime.md` | bootstrap script — load index data, ground key concepts, load appendix, always-on behavior |
| `agentos-pkg/references/maintenance.md` | maintenance checklist (linting, dedup, promotion, placement audit) + Index.CLI commands |
| `agentos-pkg/references/test-system.md` | deprecated — index testing is now covered by `agentos-testground` |

## Index Functions

| Function | Use |
|---|---|
| Research / navigation | Search the index, collect relevant blocks or appendix sections, and return cited context for the current task. |
| Writing / mutation | User-gated index edits: placement, overlap checks, wording approval, routing updates, and maintenance pass. |
| Diagnosis | Report on structure, routing, staleness, coherence, coverage gaps, or placement drift. Do not mutate unless separately approved. |
| Testing | Use `agentos-testground` for behavioral testing of index entry paths and usage patterns. Legacy activation-recall tests remain in `agentos-pkg/testing/`. |
| Maintenance | Use `agentos-pkg/references/maintenance.md` for linting, deduplication, promotion, and placement audits. |

## Index.Agent Behavior

Any capable caller can act as an `Index.Agent`, or spawn a subagent to do so when context pollution matters.

An `Index.Agent` should:

- search routing surfaces first, then load only relevant concept blocks, appendix material, or references
- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- use writing/mutation only when the user has approved an index write

## When To Load This Skill

- when a session needs index-grounded context or a custom index research pass
- when writing, diagnosing, testing, or maintaining the index
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions

## Compatibility

`agentos-index-activate`, `agentos-index-writer`, `agentos-index-doctor`, and `agentos-index-test` are deprecated standalone public aux skills for now. Their roles are represented as functions in this skill.
