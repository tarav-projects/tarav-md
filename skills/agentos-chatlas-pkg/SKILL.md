---
name: agentos-chatlas-pkg
description: Chatlas Package.Skill. Workflow-neutral package orientation for the Chatlas dataset system and its public skill surfaces.
---

# agentos-chatlas-pkg

`agentos-chatlas-pkg` is the `Package.Skill` for Chatlas.

It is the package-level public agentic surface for the Chatlas dataset system: session query and export workflows, view model, raw archive and retention concepts, session continuation and recovery surfaces.

This root skill is workflow neutral. It gives package identity and orientation only, so loading it does not change the caller's current task.

Package structure and routing live in `package.md`.

## Package Surfaces

| Surface | Use |
|---|---|
| `package.md` | package identity, boundaries, dependencies, and current routing |
| `references/chatlas-commands.md` | Chatlas CLI query, export, raw, and view workflows |
| `chatlas-grounding-agent` | Mine Chatlas sessions into `Grounding.Request` live notes for Agentos kernel blocks |
| `chatlas-session-continue` | continuation handoff workflow for prior sessions |
| `chatlas-session-zip-transcript` | compact transcript summary artifact workflow |
| `agentos-chatlas-retention-audit` | raw retention audit workflow |
