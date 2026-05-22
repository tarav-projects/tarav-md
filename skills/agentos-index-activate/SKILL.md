---
name: agentos-index-activate
description: "Bootstrap the Agentos Index runtime for a session. Executes the load-runtime sequence from agentos-pkg/references/launch-runtime.md."
---

# agentos-index-activate

Bootstrap the Agentos Index runtime for this session.

This is a `Package.Aux.Skill` for the Agentos Index subsystem of `agentos-pkg`.

## Activation

Execute the load-runtime sequence: `agentos-pkg/references/launch-runtime.md`

That file is the step-by-step bootstrap — follow it in order.

## After Bootstrap

- for full design context, load `agentos-index`
- for writing to the index, the user invokes `agentos-index-writer`
