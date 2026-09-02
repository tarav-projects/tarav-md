---
name: tarav-chatlas-pkg
description: Chatlas Package.Skill for Tarav's maintained chat artifacts, session index, and provider-neutral Normal Model. USE WHEN orienting to Chatlas, resolving sessions, reading normalized chats, or auditing raw retention.
---

# tarav-chatlas-pkg

Chatlas captures selected provider-native chat artifacts and derives a small
provider-neutral Normal Model while preserving navigation back to raw data.

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
- `tarav chatlas normal-model` resolves one exact session by native session ID
  or neutral identity hash. Its default output is metadata plus Events;
  `--messages`, `--turns`, `--loaded-contexts`, and `--all` add projections.
- `tarav chatlas raw sources` returns retained raw Artifact locations for one
  exact session.
- `tarav chatlas index redo` rebuilds the derived Session.Index from retained
  raw artifacts.
- `tarav chatlas index reset` removes disposable index/cache state and is an
  explicit maintenance operation, not an ordinary read step.

There is currently no public `sessions query`, `chat query`, or `turns get`
command. Agentic workflows may perform bounded discovery over the retained
Session.Index and then use `normal-model` for authoritative reads; they must
not document imaginary CLI compatibility surfaces.

## Package Workflows

- `tarav-chatlas-my-session-id` resolves the running agent's own session.
- `chatlas-session-continue` produces a continuation handoff from one exact
  maintained session.
- `tarav-chatlas-retention-audit` checks provider-native raw retention.

Historical command compendia and displaced implementations remain evidence,
not current operational guidance.
