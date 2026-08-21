---
name: chatlas-session-continue
description: Resolve one prior Codex or Claude session through Chatlas2 and return a continuation handoff derived from bounded chronological Chat.Message pages, preserving every user message verbatim. USE WHEN the goal is to continue work from another supported chat. Called like a terminal command — `--session <id|uri|query>`.
---

# Chatlas Session Continue

Operational `Package.Aux.Skill` under `tarav-chatlas-pkg`.

Return a continuation handoff for one prior supported session so its discussion can resume in the current chat. Chatlas2 provides the session identity and complete bounded message traversal; the agent derives continuation state and compresses agent messages.

This is a `Batchy.Skill` — called like a terminal command. Load `tarav-batchy-skills` for the full convention.

- `-h` / `--help` prints help instead of running.
- a bare session id, URI, identity hash, or query resolves to `--session`.

## Skill.Arg.Section

### Skill.Arg::Session
- one prior session: native id, `agentos://chat-session/...` URI, identity hash, or provider-agnostic message query
- required: true
- flags: --session

## Execution Mode

Run transcript traversal and synthesis in a separate agent by default so prior-session content does not consume the caller's working context. Inline execution is an explicit fallback. The worker returns the handoff artifact, not a report about producing it.

## Boundary

- supports Codex and Claude Code sessions recognized by Chatlas2
- never invokes Chatlas1 query, Views, Products, or zip-transcript machinery
- never produces or commits a retained summary artifact
- preserves every user `Chat.Message.text` in full and verbatim; Chatlas2 makes no broader `User.Turn` promise
- preserves chronological order; agent messages may be compressed but not used to rewrite user text

## Quality Bar

1. Zero user-message loss.
2. Continuation-first state: current goal, accepted decisions, constraints, artifacts, open threads, and best next move.
3. Minimal agent-message redundancy.
4. Explicit provenance and an explicit warning that agent wording is compressed.

## Workflow

### 1. Resolve exactly one session and refresh once

Classify the selector, then make the first read the workflow's only update:

```bash
tarav chatlas --update sessions query --session-id <id> --limit 10 --json
tarav chatlas --update sessions query --uri <uri> --limit 10 --json
tarav chatlas --update sessions query --identity-hash <hash> --limit 10 --json
```

For free text, search verified user and agent messages, then deduplicate by neutral identity:

```bash
tarav chatlas --update chat query --contains '<text>' \
  --sort newest --session-limit 50 --limit 100 --json
```

- exact selectors may still be ambiguous across provider instances; never guess
- zero candidates means not found or unsupported
- several identities produce a compact candidate list (`provider`, `session_id`, `uri`, last activity) and stop
- after one identity is selected, do not update again during traversal

### 2. Traverse the transcript in bounded pages

Read all `Chat.Message` records oldest-first. Redirect each page to a temporary file and process it before requesting the next:

```bash
tarav chatlas chat query --identity-hash <hash> \
  --sort oldest --offset <offset> --limit 100 --json
```

Start at offset `0`. Continue with the returned `next_offset`; stop when it is `null`. Fail rather than synthesize when the selected session reports a normalization failure. Do not update between pages: paging is deterministic only over one stable archive snapshot.

For every page:

- append each user message to the handoff transcript exactly as returned
- retain only new state from agent messages: decisions, results, failures, constraints, material paths/commands/ids, and unresolved work
- discard progress chatter, repeated framing, and filler
- keep page order; never regroup by side

### 3. Derive continuation state

From the complete traversal, include only supported values:

- `current-goal`
- `accepted-decisions`
- `active-constraints`
- `important-artifacts`
- `open-threads`
- `recommended-next-step`

Prefer end-of-session evidence for current state and earlier messages for the original objective. Omit unknown fields rather than inventing them.

### 4. Return the handoff artifact

Use this stable shape:

```text
[session continuation handoff]
User messages are preserved verbatim.
Agent messages are compressed and may not match original wording.
Do not treat this artifact as the original transcript.

source-session-id: <id>
source-session-uri: <uri>
source-identity-hash: <hash>
resolved-via: tarav chatlas ...
sourced-via: bounded Chat.Query pages

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

Omit empty continuation-state lists. Return the artifact itself. On ambiguity, missing support, paging failure, or partial normalization, return a brief failure and no fabricated handoff.

## Sensitivity

Treat prior-session content as sensitive. Read and return only the selected session, and do not mix in unrelated repository or web context.
