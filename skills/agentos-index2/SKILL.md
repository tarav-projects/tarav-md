---
name: agentos-index2
description: "POC do-over of agentos-index built with Skillware — its reference modules compile from .skillware/src/*.skw.md sources via agentos skillware build. USE only as a Skillware demonstration; agentos-index remains the canonical index skill."
---

# agentos-index2 (Skillware POC)

**This is a proof-of-concept**, the first skill developed on the Skillware pipeline (`584-skillware-v1-impl-req.md`). `agentos-index` remains the canonical index skill.

- `references/search.md` and `references/ground.md` are **compiled surfaces** — do not hand-edit them; develop in `.skillware/src/` and run `agentos skillware build --skill <this folder>`.
- `references/ground.md` imports from `references/search.skw.md` (one `copy`, one `derived` also depending on the `Context.Grounding` index block) — the demonstration dependency.
- `references/gr-survey.md` is hand-owned (no src) — the absence case.
- `agentos skillware check --skill <this folder>` reports drift; `status` inventories the pipeline.

## Modules

- `references/search.md` — cited index retrieval (compiled)
- `references/ground.md` — conversation-to-index grounding (compiled; imports from search + index)
- `references/gr-survey.md` — grounding survey (hand-owned)
