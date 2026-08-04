---
name: agentos-chatlas-pkg
description: "Chatlas Package.Skill for the maintained chat-session dataset and its public agentic workflows. USE WHEN orienting to Chatlas, querying or recovering sessions, working with Chatlas Anchory, or capturing one session as a chronological Chat.Index. Capture is called like a terminal command with `--capture --session SESSION_SELECTOR`."
---

# agentos-chatlas-pkg

`agentos-chatlas-pkg` is the `Package.Skill` for Chatlas.

Use it as the package-level public agentic surface for the Chatlas dataset system: session query and export workflows, session continuation and recovery, the chat-anchor system (`Chatlas.Anchory`), raw archive and retention concepts, and per-session `Chat.Index` capture.

Keep the root driver workflow-neutral until a route such as `--capture` selects an operation module.

Its `Package.Driver.Router` is one `Routing.Table`; `Batchy.Skill.Help` handles help calls, and declared `User.Command`s remain the only explicit workflow gates.

This is a `Batchy.Skill`, called like a CLI and resolved by one `Batchy.Router`. This compact contract is materialized from `agentos-batchy-skills`; load that skill when the full convention is needed.

- `-h` / `--help` prints callable help into the chat and stops without running
- a written `--<flag>` is intentional run configuration and must be resolved as such
- explicit configuration wins over compatible inferred or default configuration for the same route
- conversational discovery and declared defaults apply only where the applicable router row permits them
- every non-help run with custom configuration first prints its resolved `Batchy.Skill.Banner`
- only external data consumed by the selected behavior is a `Skill.Arg`; operation and module selection remain router effects
- compatible routes may compose, but aliases and composed flags do not create new module identities
- load only selected `Skill.Module`s and the additional context they explicitly require
- declared `User.Command`s are the only way to cross their explicit workflow gates
- when a configured run, command target, or required argument remains materially ambiguous, ask rather than guess

The Chatlas index lives in `000-INDEX.md` over its `design/` and `poi/` chapters, with depth in `appendix/`.

## Skill.Arg.Section

### Skill.Arg::Session

- the exact Chatlas session to capture: a provider-native session id, an `agentos://chat-session/...` URI, or a full Chatlas identity hash
- required: true with `--capture`
- help: "the exact session to capture (session id, URI, or identity hash)"
- examples: --session "019fbfbd-6fa3-74c0-a6dc-206aa3b3cb25"

## Package.Driver.Router

Selection cardinality: `many`.

### `^route-chat-index-capture`

- match: `explicit-or-semantic`
- flags: `--capture`
- destinations: `Chat.Index.Capture.Operation.Module`
- loads: `references/capture.md`
- when: the caller wants to construct, refresh, or resume the chronological Chat.Index projection of one Chatlas session
- then: load the capture module and materialize the target session under the Chatlas depot

### `^route-session-arg`

- match: `explicit`
- flags: `--session`
- destinations: `Skill.Arg::Session`
- then: bind Skill.Arg::Session to the exact target session selector

## Package Surfaces

| Surface | Use |
|---|---|
| `000-INDEX.md` → `design/`, `poi/` | Chatlas concepts and package-owned POI classes, with depth in `appendix/` |
| `--capture --session <selector>` | Build or refresh `<chatlas-root>/session-index/<identity-hash>/` from that chat alone |
| `references/chatlas-commands.md` | Chatlas CLI query, export, event, turn, and anchor workflows |
| `chatlas-session-continue` | Continue work from a prior session |
| `chatlas-session-zip-transcript` | Recover a compact transcript artifact |
| `agentos-chatlas-my-session-id` | Discover the running agent's own native session id |
| `agentos-chatlas-retention-audit` | Audit raw retention policy for one provider |
