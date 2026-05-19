---
name: agentos-index
description: "Full design reference for the Agentos Index — a Soft.Programming.Language for project knowledge. Load when another index skill needs full design context or when discussing the index design itself."
---

# agentos-index

The master skill for the Agentos Index — a `Soft.Programming.Language` for project knowledge.

This is the `Main.Skill` of the index `Skill.Package`. It contains the full design reference for how the index works, how agents operate it, and how humans interact with it.

## What The Index Is

- the index is a `Soft.Programming.Language` — soft syntax (natural language), programming semantics (execution behavior)
- it is the `Alignment.Surface` between humans and agents — the shared ground where both sides align on what things mean
- it contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized in flat index files
- agents operate the index through the `Index.Runtime` — the full index is loaded at activation, concepts are always in context

## References

| Reference | Covers |
|---|---|
| `references/launch-runtime.md` | Index.Runtime — architecture, reading, writing, research, gaps, detection, footer |
| `references/maintenance.md` | maintenance model, promotion, low-friction capture, Stub.Convention |
| `references/test-system.md` | index testing mechanism — master/subagent pattern, test file format |

## Alias.Skills

This skill package exports the following `Alias.Skills`:

- `agentos-index-activate` — bootstrap the index runtime for a session
- `agentos-index-writer` — user-gated write path to the index
- `agentos-index-doctor` — index health review and diagnosis
- `agentos-index-test` — run index activation and runtime tests

All alias skills point back to the relevant reference file in this skill.

## When To Load This Skill

- when another index skill needs full design context
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
- not needed for routine index operations — alias skills handle those
