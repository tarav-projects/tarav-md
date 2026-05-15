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
- it contains `Named.Concepts` written in `Kernel.Block:Index` blocks, organized in flat index files, registered in the `Ontology.Registry`
- agents execute the index at runtime through the `Index.Eval.Loop` — resolving names, loading blocks, detecting gaps

## References

| Reference | Covers |
|---|---|
| `references/core-model.md` | what the index IS — Soft.Programming.Language, Alignment.Surface, SSOT rule, Stable.Surfaces |
| `references/eval-loop.md` | Index.Call, triggers, Index.Eval.Loop pipeline, activation, runtime semantics |
| `references/block-syntax.md` | Kernel.Block:Index, Index.Block.Syntax, Bullet.Point.Sentence, Index.Note, size constraints |
| `references/appendix.md` | Index.Appendix, Kernel.Block:Appendix, placement, promotion, file convention |
| `references/naming.md` | Dotted.Notation, detection rules, parameterized and variable notation |
| `references/ontology.md` | Ontology.Registry, namespaces, workflows (emergence → registration → promotion) |
| `references/maintenance.md` | maintenance model, promotion, low-friction capture, Stub.Convention |
| `references/gating.md` | User.Gated.Index, write gates, write loop, agentos-index-writer behavior |
| `references/install.md` | instructions for creating Alias.Skills from this Skill.Package |

## Alias.Skills

This skill package exports the following `Alias.Skills`:

- `agentos-index-activate` — bootstrap the index runtime for a session
- `agentos-index-trigger` — lightweight always-on detection of Dotted.Names
- `agentos-index-resolution` — resolve approximate names against the index
- `agentos-index-writer` — user-gated write path to the index
- `agentos-index-doctor` — index health review and diagnosis
- `agentos-index-appendix-base` — appendix surface protocol for `notes/appendix/`

All alias skills point back to the relevant reference file in this skill.

## When To Load This Skill

- when another index skill needs full design context
- when discussing or modifying the index design itself
- when debugging index behavior or resolving design questions
- not needed for routine index operations — alias skills handle those
