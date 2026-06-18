---
name: agentos-index
description: "Workflow-neutral Package.Aux.Skill for the Agentos Index subsystem of agentos-pkg. USE WHEN you need index research, writing, diagnosis, testing, maintenance, or index design context."
---

# agentos-index

Workflow-neutral `Package.Aux.Skill` for the Agentos Index — a `Soft.Programming.Language` for project knowledge.

This skill orients the caller to the index subsystem without forcing an operation. The Agentos Index design reference lives in `agentos-pkg/index/`, `agentos-pkg/appendix/`, and `agentos-pkg/references/`.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments.



## What The Index Is

- the index is a `Soft.Programming.Language` — soft syntax (natural language), programming semantics (execution behavior)
- it is the `Alignment.Surface` between humans and agents — the shared ground where both sides align on what things mean
- it contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized in flat index files
- agents operate the index by collecting the relevant routing blocks, concept blocks, appendix material, and references for the current task

## References

| Reference | Covers |
|---|---|
| `agentos-pkg/references/launch-runtime.md` | bootstrap script — load index data, ground key concepts, load appendix, always-on behavior |

## Index Functions

| Function | Use |
|---|---|
| Research / navigation | Search the index, collect relevant blocks or appendix sections, and return cited context for the current task. |
| Writing / mutation | User-gated index edits. Full writer's guide: `agentos-index-writer`. |
| Diagnosis | Report on structure, routing, staleness, coherence, coverage gaps, or placement drift. Do not mutate unless separately approved. |
| Testing | Use `agentos-testground` for behavioral testing of index entry paths and usage patterns. Legacy activation-recall tests remain in `agentos-pkg/testing/`. |

## Index Operating Behavior

An agent operating the index should:

- search routing surfaces first, then load only relevant concept blocks, appendix material, or references
- return context with source block citations so the caller can verify and maintain the summary
- distinguish discovered context from inference
- use writing/mutation only when the user has approved an index write

For delegated read-only research that protects the caller's context, use `Packages.Master.Agent` against the relevant package or packages.

## When To Load This Skill

- when a session needs index-grounded context or a custom index research pass
- when writing, diagnosing, testing, or maintaining the index
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
