---
name: agentos-index-activate
description: "Bootstrap the Agentos Index runtime for a session. Executes the load-runtime sequence from references/runtime.md."
---

# agentos-index-activate

Bootstrap the Agentos Index runtime for this session.

This is an `Alias.Skill` of the `agentos-index` `Skill.Package`.

## Activation

Execute the load-runtime sequence: `agentos-index/references/runtime.md`

That file is the step-by-step bootstrap — follow it in order.

## After Bootstrap

- load `agentos-index-trigger` skill for ongoing detection
- for full design context, load `agentos-index`
- for name resolution, load `agentos-index-resolution`
- for writing to the index, the user invokes `agentos-index-writer`
