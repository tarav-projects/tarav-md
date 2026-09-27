---
name: tarav-chatlas-pkg
description: Chatlas Package.Skill for Tarav's maintained chat artifacts, session index, and provider-neutral Normal Model. USE WHEN orienting to Chatlas, resolving sessions, reading normalized chats, or auditing raw retention.
---

# tarav-chatlas-pkg

Chatlas captures selected provider-native chat artifacts and derives a small
provider-neutral Normal Model while preserving navigation back to raw data.

This package is maintained directly in its Markdown product files until a new
`skw.skills` package source is deliberately adopted. Do not recreate or run
the retired legacy Skillware build surface.

The maintained dataset defaults to `~/Documents/tarav/chatlas/`. It owns its
own data authority inside the shared physical Tarav depot.

## Current Data Path

```text
Provider-native session artifacts
          ↓ tarav chatlas update
Chatlas raw depot + Session.Index
          ↓ normalize
Chatlas Normal Model
          ↓ consumed by
Diagram support, grounding, and Agent workflows
```

The Normal Model is regular Chatlas. Do not route current work through retired
parallel implementations or command surfaces.

## Current CLI

Discover exact options from `tarav chatlas <command> --help`.

- `tarav chatlas update` captures provider deltas and updates Session.Index.
- `tarav chatlas current-session` resolves the running Codex or Claude Code
  harness's verified provider-native session without writing.
- `tarav chatlas normal-model` resolves one exact session by native session ID
  or neutral identity hash. Its default output is metadata plus Events;
  `--messages`, `--turns`, `--loaded-contexts`, and `--all` add projections.
- `tarav chatlas query` selects Turns from one exact session, assembles their
  referenced Messages and Event time, and uses the default named Renderer.
- `tarav chatlas render` accepts the same Query selectors and optionally uses
  another fully qualified registered Renderer plus Renderer-owned options.
- `tarav chatlas raw sources` returns retained raw Artifact locations for one
  exact session.
- `tarav chatlas index redo` rebuilds the derived Session.Index from retained
  raw artifacts.
- `tarav chatlas index reset` removes disposable index/cache state and is an
  explicit maintenance operation, not an ordinary read step.

Query owns selection and Turn-to-Message assembly. Renderers consume the
resulting structured Findings and own only what and how they present. Default
`query` and default `render` output are equivalent.

`current-session` works only when invoked inside a supported harness process
tree carrying verified provider context. Query and Render may use that target
through `--current-session`; their explicit `--update` performs one exact
provider-session capture before the read, while `--refresh` rebuilds only the
retained Normal Model cache.

`Chatlas.Turn.Ledger.Renderer` provides compact timestamped Turn discovery.
Query supports literal text discovery inside one exact session. There is no
public cross-session inventory or full-text query command; Agentic workflows
may select bounded candidates from the retained Session Index and then use
exact-session Query or Normal Model reads. Do not document imaginary CLI
compatibility surfaces.

## Package Workflows

- `tarav-chatlas-my-session-id` resolves the running agent's own session.
- `chatlas-session-continue` produces a continuation handoff from one exact
  maintained session.
- `tarav-chatlas-retention-audit` checks provider-native raw retention.

Historical command compendia and displaced implementations remain evidence,
not current operational guidance.
