---
name: chatlas-session-continue
description: Resolve one exact prior Codex or Claude Code session through the current Tarav Chatlas Normal Model and return a continuation handoff while preserving every user Chat.Message verbatim. USE WHEN continuing work from a known native session id or Chatlas identity hash. Called like a terminal command with `--session`.
---

# Chatlas Session Continue

Operational `Package.Aux.Skill` under `tarav-chatlas-pkg`.

Return a continuation handoff for one exact prior supported session. Chatlas
provides the provider-neutral Normal Model; the agent derives continuation state
and compresses agent messages.

This is a `Batchy.Skill` — called like a CLI and run in a separate agent by
default so transcript content does not consume the caller's working context.
Inline execution is an explicit fallback.

- `-h` / `--help` prints help instead of running.
- a bare selector resolves to `--session`.

## Skill.Arg.Section

### Skill.Arg::Session

One exact native session id or Chatlas identity hash. A 64-character SHA-256
value is an identity hash; other values are native session ids.

- required: true
- flags: `--session`

### Skill.Arg::Provider and Skill.Arg::Instance

Optional `--provider` and `--instance` disambiguate a native session id. Session
URIs and free-text queries are not supported by the current CLI; report that
briefly instead of searching or guessing.

- required: false
- flags: `--provider`, `--instance`

## Boundary

- supports Codex and Claude Code sessions recognized by Chatlas
- uses only the current `tarav chatlas update` and `tarav chatlas normal-model`
  surfaces
- never invokes retired Query, Views, Products, or zip-transcript machinery
- never produces or commits a retained summary artifact
- preserves every user `Chat.Message.text` in full, verbatim, and chronological
  order; agent messages may be compressed but never used to rewrite user text

## Workflow

### 1. Refresh capture when the selector is a native session id

Perform one exact capture/index update and redirect its JSON result to a
temporary file:

```bash
tarav chatlas update --session-id <id> \
  [--provider <provider>] [--instance <instance>] > <tmp>/update.json
```

Do not update again during the run. An identity hash cannot select an update;
for that selector, use the retained archive as-is and disclose that capture was
not refreshed.

If resolution is missing or ambiguous, stop. Ask for `--provider` or
`--instance` when that can disambiguate; do not inspect unrelated sessions.

### 2. Materialize the exact Normal Model

Redirect the full result so it does not enter the caller's context:

```bash
tarav chatlas normal-model --session-id <id> \
  [--provider <provider>] [--instance <instance>] \
  --refresh --messages > <tmp>/model.json
```

For an identity hash, replace `--session-id <id>` with
`--identity-hash <hash>`.

Validate before synthesis:

- class is `tarav.chatlas.normal_model`
- `session` contains one provider, session id, and identity hash
- `messages` is an array of `Chat.Message` objects with `side` equal to `user`
  or `agent` and string `text`
- transcript sources are recognized

Treat command failure or an invalid/partial model as failure; do not fabricate a
handoff.

### 3. Traverse messages in bounded slices

The CLI emits one JSON document rather than query pages. Read its chronological
`messages` array from the temporary file in slices of at most 100; process and
discard each slice before reading the next. For example:

```bash
jq --argjson offset <offset> --argjson limit 100 \
  '.messages[$offset:($offset + $limit)]' <tmp>/model.json > <tmp>/page.json
```

For every slice:

- append each user message to the handoff transcript exactly as returned
- retain only new state from agent messages: decisions, results, failures,
  constraints, material paths/commands/ids, and unresolved work
- discard progress chatter, repeated framing, and filler
- preserve message order; never regroup by side

Count source user messages and ensure the handoff contains the same count before
returning it. Remove the temporary directory after successful synthesis or
failure.

### 4. Derive continuation state

Include only supported values:

- `current-goal`
- `accepted-decisions`
- `active-constraints`
- `important-artifacts`
- `open-threads`
- `recommended-next-step`

Prefer end-of-session evidence for current state and earlier messages for the
original objective. Omit unknown fields rather than inventing them.

### 5. Return the handoff artifact

```text
[session continuation handoff]
User messages are preserved verbatim.
Agent messages are compressed and may not match original wording.
Do not treat this artifact as the original transcript.

source-provider: <provider>
source-session-id: <id>
source-identity-hash: <hash>
capture-refresh: <command, or not available for identity-hash selector>
sourced-via: tarav chatlas normal-model --refresh --messages; bounded local slices

[continuation-state]
current-goal: ...
accepted-decisions:
- ...
active-constraints:
- ...
important-artifacts:
- ...
open-threads:
- ...
recommended-next-step:
- ...

[transcript]
[user]
<verbatim text>

[agent]
<compressed state-bearing content>
```

Omit empty continuation-state lists. Return the artifact itself, not a report
about producing it.

## Sensitivity

Treat prior-session content as sensitive. Read and return only the selected
session, and do not mix in unrelated repository or web context.
