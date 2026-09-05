---
name: tarav-chatlas-my-session-id
description: Discover the running agent's own provider-native session ID and neutral Chatlas identity through the current Tarav Chatlas Normal Model. USE WHEN an agent must identify the session it is running inside. Called with no required arguments; optional `--provider` narrows provider routing.
---

# Chatlas My Session ID

Resolve the caller's own session inline. Do not delegate this workflow: a
different agent has a different harness session.

Use only the current `tarav chatlas` surface. In particular, do not invent
session-query or chat-query subcommands that are absent from
`tarav chatlas --help`.

## Arguments

- `--provider <codex|claude-code>` selects the provider explicitly.
- `--since <duration>` bounds fallback discovery; default `1d`.
- `-h` or `--help` prints this contract and stops.

## Direct Resolution

Use Chatlas's verified provider-native reader through its public command:

```bash
tarav chatlas current-session --provider <codex|claude-code> --json
```

The command is read-only and supports both Codex and Claude Code. Read its
`provider` and `session_id`; do not inspect harness environment variables
directly or substitute recency-based inference when this exact command succeeds.

After resolving a native ID, refresh exactly that session and ask the Normal
Model for its neutral identity:

```bash
tarav chatlas update \
  --provider <provider> \
  --session-id <native-session-id>

tarav chatlas normal-model \
  --provider <provider> \
  --session-id <native-session-id>
```

Read `session.session_id`, `session.identity_hash`, and `session.provider` from
the Normal Model envelope. The update is the workflow's single freshness
boundary; callers should not refresh the same session again.

## Fallback Discovery

When the running harness exposes no verified native ID, use a bounded
Agent-driven fallback over current Chatlas data:

1. Select distinctive verbatim fragments from the caller's own recent User
   turns. Prefer late, rare fragments that distinguish forks.
2. Run one `tarav chatlas update --provider <provider>`.
3. Read recent candidate rows from the maintained session index under
   `~/Documents/tarav/chatlas/index/sessions/<provider>/`, bounded by
   `--since` and newest activity.
4. Materialize candidates with
   `tarav chatlas normal-model --identity-hash <identity> --messages` and match
   all selected User fragments locally.
5. Keep candidate rows and Normal Models out of model context. Perform the
   intersection in a subprocess and surface only the final row.

Never infer identity from the newest file, cwd alone, process recency, a
parent session, or one weak fragment. Exactly one candidate must survive. If
none or several survive after one bounded escalation, report the unresolved
state instead of guessing.

## Result

Return one compact object:

```text
session_id:       <provider-native id>
identity_hash:    <neutral Chatlas identity>
provider:         <provider family>
last_activity_at: <when available from the session-index row>
```

If the native ID resolves but the Normal Model is not yet available, return
the native ID and provider while marking the neutral identity unavailable.
