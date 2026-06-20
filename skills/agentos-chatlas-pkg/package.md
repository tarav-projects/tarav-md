# agentos-chatlas-pkg Package

## Package.Identity

- `agentos-chatlas-pkg` is the `Package.Skill` for Chatlas.
- It is a package-level public agentic surface, not the `agentos-chatlas-md` repository or the `agentos-chatlas-py` implementation.
- It currently lives in `agentos-chatlas-md/skills/agentos-chatlas-pkg/` as an implementation detail.
- The first migration is structural: Chatlas index content has moved from `agentos-pkg` into this package, while skills are routed by reference.

## Package.Router

### Orientation

- `agentos-chatlas-pkg` — workflow-neutral Chatlas package orientation.
- `references/chatlas-commands.md` — Chatlas command and workflow reference.

### Index

- `agentos-chatlas-pkg/index/` — Chatlas public index flat files and routing table.
- `agentos-chatlas-pkg/appendix/` — Chatlas public index appendix files.
- `agentos-chatlas-pkg/references/` — Chatlas operational references and view producer protocols.

### Workflows

- `agentos-chatlas-retention-audit` — raw retention policy audit workflow.
- `chatlas-grounding-agent` — mine Chatlas sessions into `Chat.Grounding.Request` records or run git-guided grounding review for Agentos kernel blocks.
- `chatlas-session-continue` — session continuation handoff workflow.
- `chatlas-session-zip-transcript` — compact transcript recovery workflow.
- `agentos-chatlas-my-session-id` — discover the running agent's own native session id.

## Package.Boundary

- `agentos-chatlas-pkg` owns Chatlas public agentic knowledge: dataset usage, session query/export/view workflows, raw archive/retention concepts, view model concepts, and session continuation surfaces.
- Does not own: `agentos-chatlas-md` local design notes, `agentos-chatlas-py` internal mechanics, general Agentos index/project/skill concepts (those stay in `agentos-pkg`).
- Chatlas operational skills live under `agentos-chatlas-md/skills/` when they are package-owned Chatlas surfaces.

## Package.Dependency

- Depends on `agentos-pkg` for project model, index framework, skill model, `Kernel.Block`, `Kernel.Writing`, and shared Agentos operating surfaces.

## Package.Install

- Install behavior is not implemented in this structural pass.

## Package.Agents

- No dedicated `Package.Agent` is defined in this structural pass.

## Local.Boundary

- `agentos-chatlas-md` is the markdown design project for Chatlas surfaces.
- `agentos-chatlas-pkg` is not the same thing as `agentos-chatlas-md`.
- Local design sessions and impl-req notes stay in `agentos-chatlas-md/notes/live/`, not in the package.
