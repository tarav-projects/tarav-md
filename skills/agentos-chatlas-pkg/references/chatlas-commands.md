# Chatlas Commands

Operational Chatlas command and workflow reference.

## Default Command Mapping

- Refresh dataset: `agentos chatlas update`
- Inventory/query sessions: `agentos chatlas query`
- Query relational turn patterns: `agentos chatlas events query`
- Find matching authoritative turns: `agentos chatlas turns query`
- Aggregate dataset stats: `agentos chatlas stats`
- Export attributed sessions into a project tree: `agentos chatlas local sync`
- Print inline standard-model views: `agentos chatlas views inline`
- Preview a support set without minting: `agentos chatlas anchory preview`
- Mint a validated support-set anchor: `agentos chatlas anchory register`
- Resolve an anchor to its ordered support set: `agentos chatlas anchory resolve`
- Export raw artifacts: `agentos chatlas raw path` / `agentos chatlas raw export`
- Consume or produce materialized views: `agentos chatlas views`

## Working Rules

- Prefer `agentos chatlas ...` for normal session workflows.
- Use `agentos chat debug ...` only for live provider diagnostics, raw artifact extraction, or connector troubleshooting.
- If freshness matters, run `agentos chatlas update` before querying.
- If already-materialized dataset contents are enough, query first and avoid unnecessary updates.
- Default Chatlas dataset root is `~/Documents/chatlas`.

## Local Chatlas Workflow

```sh
agentos chatlas local sync --project <project-root>
agentos chatlas local status --project <project-root>
```

`chatlas local` bootstraps a project-local `chatlas/` folder from the global
Chatlas dataset. v0 is export-only: reads, query resolution, linting, and
grounding still use the global Chatlas depot.

- relevance is path attribution only: the selected Agentos project path plus contiguous Agentos-project ancestors (`Projects.Chats`)
- content is the `turns` filter only: visible user/assistant message events as model JSON, with native/source plumbing stripped
- sync overwrites the sessions it computes and never deletes other local files
- status reports attributed-and-present, attributed-and-missing, and present-but-not-attributed buckets
- the local folder contains a small marker manifest plus one `<identity_hash>.json` session-model file per synced session

## Query Workflow

```sh
agentos chatlas query
agentos chatlas query "<query>" --include-match
agentos chatlas query "<query>" --include-match --include-provider-stats
agentos chatlas query "<query>" --include-artifacts
agentos chatlas query --active-after <iso-timestamp> --sort newest
agentos chatlas query "<query>" --compact
agentos chatlas update
agentos chatlas update --scan-cache false
agentos chatlas update --session-index-cache false
agentos chatlas update --verbose-mode=quiet --output-mode=json
```

## Event.Pattern Workflow

`Event.Pattern` queries relations between visible turns without exposing a SQL
contract. The normal scan is authoritative; SQLite is a disposable candidate
index whose coordinates are reloaded and re-evaluated against current
`Chatlas.Session.Model` events.

```sh
agentos chatlas events index
agentos chatlas events query \
  --backend sqlite \
  --pattern-json '{
    "steps": [
      {"role": "assistant", "text_contains": "candidate:"},
      {"role": "user", "text_exact": "::approve POI.Class"}
    ],
    "relation": "next_turn",
    "select": "all",
    "project": "match",
    "cardinality": "many"
  }'
```

- Predicates: `role`, `kind`, `event_id`, `text_exact`, `text_contains`.
- V1 relation: `next_turn`, where tool events do not interrupt adjacent visible message turns.
- Selection: `all`, `first`, `latest`.
- Projection: `match`, `first`, `last`.
- Cardinality: `many`, `one`, `zero-or-one`.
- Backends: `auto`, `scan`, `sqlite`. Missing, stale, or incomplete SQLite coverage falls back to `scan` and reports `backend_used`.
- Existing index selectors such as `--session-id`, `--identity-hash`, and `--provider` can constrain the queried sessions.

For one-step turn discovery, `turns query` is the compact ergonomic projection:

```sh
agentos chatlas turns query --identity-hash <H> --contains "<text>" --human
agentos chatlas turns query --identity-hash <H> --contains "<text>" --human --detail turn
```

- default `summary` detail returns `Normal.Turn.Ref`, Anchory-ready `member_ref`, and compact matched-event entries with exact `Event.Ref` values
- `--detail turn` adds the complete authoritative `Normal.Turn`
- `auto` scans directly when deterministic selectors already reduce the selection to at most 16 sessions; explicit `--backend sqlite` still forces candidate-index use

## Inline View Workflow

```sh
agentos chatlas views inline "<query>" --view full --format json
agentos chatlas views inline "<query>" --view transcript --format json
agentos chatlas views inline "<query>" --view user --format json
agentos chatlas views inline "<query>" --view replay --format json
agentos chatlas views inline "<query>" --view events --format json
agentos chatlas views inline "<query>" --view zip-transcript --format json
agentos chatlas views inline "<query>" --view zip-transcript --range 10: --format json
agentos chatlas raw path "<query>"
agentos chatlas raw export "<query>" --format json
```

`views inline --range <range>` is a view-specific slicing surface. Range
syntax is Python-style and half-open, with forms such as `N`, `A:B`, `A:`,
`:B`, and `-N:`. The first rangeable inline view is `zip-transcript`, where
the range applies to the top-level `turns` sequence and the output includes a
`range` metadata object. Other inline views reject `--range` unless they define
their own range target.

## Event Selection And Filters

`views inline` selects at event granularity and cleans fragments with named filters. Selection flags imply `--view events` when no view is named; every output stays a `Chatlas.Session.Model` fragment.

```sh
agentos chatlas views inline --identity-hash <H> --contains "<distinctive text>" --role user
agentos chatlas views inline --identity-hash <H> --around <iso-timestamp> --radius 3
agentos chatlas views inline --identity-hash <H> --contains "<text>" --filter turns
```

- `--contains` — case-insensitive text match over event payloads
- `--role` — message events with this role (`user`, `assistant`)
- `--around` + `--radius` — nearest events to a time; radius keeps the closest `2r+1`, output stays chronological
- `--filter` — named `Chatlas.Filter`, repeatable and ordered: `slim` (strip provenance plumbing), `messages` (message events only, synced), `turns` (`messages` then `slim` — the grounding reader's preset)
- composition: with `--contains`/`--role`/`--around` selection, named filters apply **before** the window, so radius counts filter-surviving events — `--around <t> --radius 3 --filter turns` means 3 turns each side, tool events don't eat the window

## Anchor Workflow

Chat anchors (`^c<YYYYMMDD>-<N>u` — `c` namespace prefix, primary-member date, counter, user-evidence tag) are the chat application of the Anchory subsystem — see `Chatlas.Anchory` in the index.

```sh
agentos chatlas anchory register \
  --member <identity-hash>:<turn-id> \
  --member <identity-hash>:<turn-id> \
  --hint "<one sentence>"
agentos chatlas anchory preview \
  --member <identity-hash>:<turn-id> \
  --hint "<one sentence>"
agentos chatlas anchory preview \
  --member <identity-hash>:<turn-id> \
  --hint "<one sentence>" \
  --detail context --radius 2
agentos chatlas anchory resolve <key> --detail context --radius 4
```

- repeat `--member` in relevance order; each session identity may be a unique prefix on input and is stored as the full identity
- preview validates and assembles the exact v3 record without allocating an anchor; it also reports equivalent existing anchors
- preview, registration, and resolution default to compact member summaries; `--detail turn` adds exact turns and `--detail context` adds neighborhoods
- registration allocates from the first member's date only after the support set has been reviewed
- radius counts visible turns around each exact member turn only under `--detail context`

## File Touch Workflow

Which sessions read/wrote a file, and where — answered from the normal model's `tool_invocations` (explicit-path tools: `Read`, `Write`, `Edit`, `NotebookEdit`). Substring path matching. Blind spot by design: paths inside Bash command strings are invisible to these filters.

```sh
agentos chatlas query --file-touched "<path-fragment>"
agentos chatlas query --file-write "<path-fragment>" --field identity_hash
agentos chatlas views inline --identity-hash <H> --file-write "<path-fragment>" --filter slim
```

- `query` flags answer *which sessions* (mentions in prose never match — touch means a tool invocation carried the path)
- `views inline` flags answer *where in the session*: the touching invocations' events as a model fragment
- blind-spot escape hatch: `--tool-contains "<text>"` (optionally `--tool-name Bash`) matches over the whole invocation — full recall, no verb claim; the reader judges read/write from the matched invocations

## Ping Workflow

Transcript round-trip probe: emit unique marker lines to stdout (they land in the calling session's transcript when the tool call completes), then update and search Chatlas for them. Unresolved markers persist in `<chatlas-root>/ping/state.json`, so the *next* ping run resolves them and reports cross-call latency plus the caller's session id.

```sh
agentos chatlas ping --provider claude-code
agentos chatlas ping --provider claude-code --lines 1 --rounds 1
```

- a run never sees its own markers (`self_visible` is false until providers stream tool output); the value is in `previous_resolved` — each entry carries `session_id`, `identity_hash`, and `latency_seconds`
- markers must actually reach the transcript: piping ping's stdout through `tail`/parsers hides them from the provider log and the probe silently loses them — run it unpiped
- output is markers + update progress + one JSON payload on stdout; parse from the first `{`

## Views Workflow

```sh
agentos chatlas views list
agentos chatlas views inline --view <inline-view-name> <selector-options>
agentos chatlas views status --view <view-name> <selector-options>
agentos chatlas views get --view <view-name> <selector-options>
agentos chatlas views path --view <view-name> <selector-options>
```

Producer references live in `agentos-chatlas-pkg/references/`.
