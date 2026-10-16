# Chatlas Annotations - design-session

## Session.Abstract

Design a minimal v1 of a Chatlas-owned annotations subsystem: free-form JSON metadata per session, stored alongside Chatlas data, queryable like the rest of session data. v1 ships only the built-in `tags` annotation with dedicated CLI verbs; general annotations exist in storage but have no user-facing surface yet.

A broader, related system — `chivo` (agent-workflow registry, secondary-market reuse, prompt+args caching) — was discussed and is deferred to its own design session. Chatlas may eventually become one consumer/producer of chivo, but annotations is built standalone.

## Design.Index

### Annotations.Storage

- Location: `chatlas/annotations/<XX>.jsonl`
- Sharding: 2-char hex prefix of Chatlas's existing normalized session hash → 256 shards
- Line schema: `{session_id, annotations: {...}}` — free-form JSON
- Mutability: mutable state, not event log. Update = read shard → mutate → atomic write (tmp + rename)
- Concurrency: no internal locks. Callers coordinate.
- Sharding rationale: bounds shard size for high session volume; query "all sessions with tag X" is O(shards) of small files, acceptable

### Annotations.Tags

- `tags` is a built-in, system-recognized annotation key
- Storage representation: `annotations.tags = ["tag-a", "tag-b", ...]`
- Storage stays uniform (not a separate primitive); tags is a convention with first-class CLI surface
- `user-touched` is just a particular tag value, no special handling at the storage or CLI layer

### Annotations.CLI.v1

- Subcommand group: `agentos chatlas annotations ...` for annotation management
- All args via options/flags (no positionals)
- `--tag` is exposed as a special, first-class flag in v1; no generic `--key`/`--value` surface yet
- Write: `agentos chatlas annotations add --session-id <id> --tag <tag>`
- Write: `agentos chatlas annotations remove --session-id <id> --tag <tag>`
- Query: extend existing `agentos chatlas query` with `--tag <tag>` (repeatable, AND semantics, matching existing `--*-contains` pattern)
- Non-tag annotations live in storage but have no CLI surface in v1
- Write path = CLI only. No programmatic/skill writes through approval gates in v1 — gating is human-side ("agent suggests, human runs the verb")

### Annotations.Read.Surface.v1

- v1: annotations surface only as a `--tag` filter on the existing `agentos chatlas query`
- `agentos chatlas annotations` subcommand is write-only in v1 (add/remove); no `list`/`show` verb
- Existing per-session views (e.g., `chatlas export`, `chatlas raw`) do not include annotations by default in v1
- Discoverability is intentionally limited; broader read surface is a v2 concern

### Chivo.Relationship.Parked

- Chivo = separate system (agent-workflow registry + reuse). Not built in chatlas.
- Chatlas may later be a chivo source (transcripts) and/or consumer (in-session agents querying chivo)
- `collections` (named, prompt-curated session sets) — discussed, looks chivo-shaped, deferred
- Annotations does not depend on chivo and vice versa

## Session.Notes

- v2 candidates (not in v1 scope): generic annotation CLI (`agentos chatlas annotations add --key ... --value ...` or similar), annotations in default per-session reads (`export`, `raw`), skill-driven write-with-approval gate, freshness/audit signals
- The "user-touched" use case: gated in chat by the agent/user interaction, CLI is just the verb. Skill design for this is out of v1 scope.
- Open: exact CLI flag shapes within the agreed conventions (e.g., singular vs plural `--tag` repeats) — implementation detail, not design-blocking

## Session.Log

- 2026-05-31: session opened. Decisions captured: storage layout (sharded jsonl under `chatlas/annotations/<XX>.jsonl`), schema (general annotations with built-in `tags`), mutability model (rewrite shard, callers coordinate concurrency), v1 CLI scope (tags-only verbs under `agentos chatlas annotations`, no generic key/value surface), query integration (`--tag` flag added to existing `agentos chatlas query`, AND semantics), read surface (queries only). Chivo deferred to its own future design session.
