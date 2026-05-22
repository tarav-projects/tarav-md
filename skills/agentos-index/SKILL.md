---
name: agentos-index
description: "Auxiliary skill for the Agentos Index — a Soft.Programming.Language for project knowledge. Load when an index auxiliary skill needs full design context or when discussing the index design itself."
---

# agentos-index

Auxiliary skill for the Agentos Index — a `Soft.Programming.Language` for project knowledge.

This is a `Package.Aux.Skill` for `agentos-pkg`. The Agentos Index design reference now lives in `agentos-pkg/index/`, `agentos-pkg/appendix/`, and `agentos-pkg/references/`.

## What The Index Is

- the index is a `Soft.Programming.Language` — soft syntax (natural language), programming semantics (execution behavior)
- it is the `Alignment.Surface` between humans and agents — the shared ground where both sides align on what things mean
- it contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized in flat index files
- agents operate the index through the `Index.Runtime` — the full index is loaded at activation, concepts are always in context

## References

| Reference | Covers |
|---|---|
| `agentos-pkg/references/launch-runtime.md` | bootstrap script — load index data, ground key concepts, load appendix, always-on behavior |
| `agentos-pkg/references/maintenance.md` | maintenance checklist (linting, dedup, promotion, placement audit) + Index.CLI commands |
| `agentos-pkg/references/test-system.md` | index testing mechanism — master/subagent pattern, test file format |

## Auxiliary Skills

The following `Package.Aux.Skill` surfaces point into the Agentos Index subsystem:

- `agentos-index-activate` — bootstrap the index runtime for a session
- `agentos-index-writer` — user-gated write path to the index
- `agentos-index-doctor` — index health review and diagnosis
- `agentos-index-test` — run index activation and runtime tests

All auxiliary skills point back to the relevant surface in `agentos-pkg`.

## When To Load This Skill

- when another index auxiliary skill needs full design context
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
- not needed for routine index operations — auxiliary skills handle those
