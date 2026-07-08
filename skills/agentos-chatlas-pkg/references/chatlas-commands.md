# Chatlas Commands

Operational Chatlas command and workflow reference.

## Default Command Mapping

- Refresh dataset: `agentos chatlas update`
- Inventory/query sessions: `agentos chatlas query`
- Aggregate dataset stats: `agentos chatlas stats`
- Print inline standard-model views: `agentos chatlas views inline`
- Mint a chat anchor (validated, echoing the landing turns): `agentos chatlas anchory register`
- Resolve a chat anchor to its turn neighborhood: `agentos chatlas views inline --anchor <key>`
- Export raw artifacts: `agentos chatlas raw path` / `agentos chatlas raw export`
- Consume or produce materialized views: `agentos chatlas views`

## Working Rules

- Prefer `agentos chatlas ...` for normal session workflows.
- Use `agentos chat debug ...` only for live provider diagnostics, raw artifact extraction, or connector troubleshooting.
- If freshness matters, run `agentos chatlas update` before querying.
- If already-materialized dataset contents are enough, query first and avoid unnecessary updates.
- Default Chatlas dataset root is `~/Documents/chatlas`.

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
- `--around` + `--radius` — nearest events to a time; radius keeps the closest `2r+1`
- `--filter` — named `Chatlas.Filter`, repeatable and ordered: `slim` (strip provenance plumbing), `messages` (message events only, synced), `turns` (`messages` then `slim` — the grounding reader's preset)

## Anchor Workflow

Chat anchors (`@YYYYMMDD-N`) are the chat application of the Anchory subsystem — see `Chatlas.Anchory` in the index.

```sh
agentos chatlas anchory register --identity-hash <H> --at "<iso-time>" --hint "<one sentence>"
agentos chatlas views inline --anchor <key> --radius 4 --filter turns
```

- registration validates the session and time bounds, allocates the date-prefixed key atomically, and echoes the landing neighborhood for double-checking
- resolution returns the landing-turn neighborhood as a model fragment — read the landing turn and around it

## Views Workflow

```sh
agentos chatlas views list
agentos chatlas views inline --view <inline-view-name> <selector-options>
agentos chatlas views status --view <view-name> <selector-options>
agentos chatlas views get --view <view-name> <selector-options>
agentos chatlas views path --view <view-name> <selector-options>
```

Producer references live in `agentos-chatlas-pkg/references/`.
