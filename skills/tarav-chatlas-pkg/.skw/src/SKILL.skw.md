> $kw: ^agentos-root-reachability --reachable-from @<tarav-pkg>/SKILL.md

---
name: tarav-chatlas-pkg
description: "Chatlas Package.Skill for the maintained chat-session dataset and its Chatlas2-first read workflows. USE WHEN orienting to Chatlas, selecting or querying sessions, recovering prior work, discovering the current session, or auditing raw retention."
---

# tarav-chatlas-pkg

> $kw: --from Batchy.Router --from Batchy.Skill --from Batchy.Skill.Banner --from Package.Skill --from Skill.Arg --from Skill.Module --from User.Command

`tarav-chatlas-pkg` is the `Package.Skill` for Chatlas.

Chatlas retains provider-native artifacts and presents a small provider-neutral Normal Model through Chatlas2. Its central read contract is chronological `Chat.Message` and `Chat.Turn` content over a loss-preserving event tape; deeper provider details remain available in the raw archive.

Use this root for package orientation. Use the Chatlas2 CLI for deterministic reads and the companion skills for agentic session discovery, dashboards, continuation, and raw-retention audits. Chatlas1 normalization, views, query, and Product routes are not dependencies of these public workflows.

> $kw: ^chatlas-pkg-batchy-runtime-contract --copy
> --from @<tarav-batchy-skills>/references/batchy-skill-run.skw.md^batchy-skill-runtime-contract

This is a `Batchy.Skill`, called like a CLI and resolved by one `Batchy.Router`. This compact contract is materialized from `tarav-batchy-skills`; load that skill when the full convention is needed.

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

> $kw. end

The Chatlas index lives in `000-INDEX.md` over its `design/` and `poi/` chapters, with depth in `appendix/`.

## Core Read Model

```text
Session.Query  → which supported chats?
Chat.Query     → which Chat.Messages inside them?
Chat.Turn      → what provider material belongs to a selected message's turn?
Raw.Archive    → what native detail was retained beyond the Normal Model?
```

- `tarav chatlas2 --update <command>` performs one archive/index delta refresh before a read when freshness matters.
- `tarav chatlas2 sessions query` selects Codex and Claude sessions from Session.Index metadata.
- `tarav chatlas2 chat query` reads verified `Chat.Message` content, stable refs, and optional containing-turn refs.
- `chat query --offset N --limit M` returns bounded chronological pages and a `next_offset`; update once before a multi-page traversal, not once per page.
- `tarav chatlas2 turns get --message-address ... --hydrate` expands a selected message to its containing opaque turn material.

## Package.Driver.Router

The root owns no full-session capture or retained-summary production route. Agentic operations are separate companion skills selected semantically by the caller:

- `tarav-chatlas-my-session-id` — discover the running agent's own session.
- `chatlas-work-dashboard` — inspect recent work and bounded session recaps.
- `chatlas-session-continue` — derive a continuation handoff while preserving every user message verbatim.
- `tarav-chatlas-retention-audit` — audit provider-native artifact retention.

## Package Surfaces

| Surface | Use |
|---|---|
| `000-INDEX.md` → `design/`, `poi/` | Chatlas concepts and package-owned POI classes, with depth in `appendix/` |
| `tarav chatlas2 sessions query` | Select supported sessions by provider-neutral metadata |
| `tarav chatlas2 chat query` | Search or traverse authoritative `Chat.Message` records |
| `tarav chatlas2 views get` | Read disposable transcript, user-message, event, or full-model projections |
| `tarav chatlas2 turns get` | Resolve and optionally hydrate a containing `Chat.Turn` |
| `tarav chatlas2 anchory` | Ground consumer records in stable `Chat.Message.Ref` evidence |

## Parked Work

The former root `--capture --session` workflow, Chatlas1 command compendium, `zip-transcript-summary` Product producer, and public zip-transcript skill are intentionally parked. Their useful requirements are retained in `issues/100-issues.md`; they are not compatibility routes. Hugentic Real.Time.Capture remains the active Chat.Index path for newly landed semantic lines.
