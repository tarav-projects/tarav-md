---
name: agentos-chatlas-pkg
description: Chatlas Package.Skill. Workflow-neutral package orientation for the Chatlas dataset system and its public skill surfaces. USE WHEN you need orientation to the Chatlas dataset system or its skill surfaces.
---

# agentos-chatlas-pkg

`agentos-chatlas-pkg` is the `Package.Skill` for Chatlas.

It is the package-level public agentic surface for the Chatlas dataset system: session query and export workflows, inline views with event selection and named filters, the chat-anchor system (`Chatlas.Anchory`), raw archive and retention concepts, session continuation and recovery surfaces.

This root skill is workflow neutral. It gives package identity and orientation only, so loading it does not change the caller's current task.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments.

The Chatlas index lives in `000-INDEX.md` (the lookup table) over its chapters — `design/` by default — with depth in `appendix/`.

## Package Surfaces

| Surface | Use |
|---|---|
| `000-INDEX.md` → `design/` | Chatlas index: chapter routing and concept definitions (depth in `appendix/`) |
| `references/chatlas-commands.md` | Chatlas CLI query, export, raw, view, selection/filter, and anchor workflows |
| `chatlas-session-continue` | continuation handoff workflow for prior sessions |
| `chatlas-session-zip-transcript` | compact transcript summary artifact workflow |
| `agentos-chatlas-my-session-id` | discover the running agent's own native session id |
| `agentos-chatlas-retention-audit` | raw retention audit workflow |
