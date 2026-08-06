# Chatlas Commands

Operational Chatlas command and workflow reference.

## Default Command Mapping

- Refresh dataset: `agentos chatlas update`
- Inventory/query sessions: `agentos chatlas query`
- Query relational turn patterns: `agentos chatlas events query`
- Find matching authoritative turns: `agentos chatlas turns query`
- Aggregate dataset stats: `agentos chatlas stats`
- Export attributed sessions into a project tree: `agentos chatlas local sync`
- Print a named standard-model view: `agentos chatlas views get`
- Preview a support set without minting: `agentos chatlas anchory preview`
- Mint a validated support-set anchor: `agentos chatlas anchory register`
- Resolve an anchor to its ordered support set: `agentos chatlas anchory resolve`
- Export raw artifacts: `agentos chatlas raw path` / `agentos chatlas raw export`
- Inspect chronological Chat.Index surfaces: `agentos chatlas chat-index`
- Consume or produce retained agent products: `agentos chatlas products`

## Output Contract

Every Chatlas command computes a JSON-like payload internally, renders it as
human-readable text by default, and prints the raw payload under `--json`.

- `--json` — the exact machine payload; what every script and agent should ask for
- `--text` — the default; writable when the intent matters
- the default never changes with TTY or pipe state, so a command's shape does not depend on how it was invoked
- `stats` and `index doctor` render markdown as their text output
- `raw path`, `chat-index path`, and `products path` render bare paths, so they stay pipe-friendly
- `--field` on `query` and `products run-produce` extracts one value per row and wins over both flags
- the mutating commands (`update`, `index update|reset|redo`, `gc`) add `--quiet` to print nothing at all; progress still follows `--verbose-mode`

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
agentos chatlas update --verbose-mode=quiet --json
```

## Chat.Index Workflow

Chat.Index v2 is a descriptor-free Markdown surface: tape-ordered `deltas/`
plus `HEAD.md`. Reads derive structure from those files and the authoritative
chat; they never repair, migrate, or recapture a surface.

```sh
agentos chatlas chat-index source --identity-hash <H> --json
agentos chatlas chat-index status --identity-hash <H> --json
agentos chatlas chat-index show --identity-hash <H> --json
agentos chatlas chat-index path --identity-hash <H>
agentos chatlas chat-index files --identity-hash <H> --json
agentos chatlas chat-index deltas --identity-hash <H> --json
agentos chatlas chat-index head --identity-hash <H> --json
agentos chatlas chat-index tail --identity-hash <H> --detail chat --json
agentos chatlas chat-index home --identity-hash <H> \
  --line-content '- [DC] exact line content' --json
agentos chatlas chat-index audit --identity-hash <H> --json
```

- `source` emits the v2 source hash and `Normal.Turn.Ref` values in event-sequence tape order; it reports non-linear lineage instead of guessing branch semantics.
- `deltas` resolves each file's horizon against the authoritative tape and returns that derived order; filenames and timestamps do not establish ordering.
- `tail` compares the evidence horizon declared by HEAD with the live chat. It detects ordinary growth past that horizon; revision of an uncited turn inside the reconstructed prefix is deliberately outside Chat.Index freshness. `--detail chat` returns the transcript-visible user and assistant messages of each pending turn, while `--detail turn` returns complete `Normal.Turn` groupings. Neither rewrites the surface.
- `home` compares canonical line content without trailing support anchors and selects the oldest matching Delta in authoritative tape order.
- `audit` replaces the per-line inspection loop: one read-only pass over derived surface structure, identity placement, source-prefix compatibility, Delta and HEAD horizons against the chat, one trailing anchor per line, anchor resolution and exact subject hashes, anchor/content collisions, Delta support horizons and attachments, and `Line.Home` selection. It exits nonzero on blocking findings, accepts `--surface <path>` to audit a staged directory against the same session, and never repairs what it reads.
- HEAD-only ordinary content is advisory reconciliation work (`head-line-without-delta-home`), not a failed surface; inspection does not write backward automatically.

### Capture.Plan

Capture is a semantic handoff: the agent authors meaning, while Chatlas owns
Delta filenames and headings, timestamps, tape order, the resulting Delta/HEAD
file set, and support anchors.

```sh
agentos chatlas chat-index scaffold --identity-hash <H> --stage <dir> --json
agentos chatlas chat-index validate --plan <dir>/plan.json --json
agentos chatlas chat-index apply --plan <dir>/plan.json --json
```

- `scaffold` writes `plan.json` (a CPU-owned `agentos.chat-index.capture-plan.v1` envelope plus an empty semantic region) and `evidence.json` (chat-only messages for the turns this capture must read) into an empty stage. It detects `create` or `maintain-v2`.
- The agent fills only `delta_edits`, `head`, and `status`; `status` is `draft` until the semantic plan is ready to apply. Line content must be typed and must never carry a trailing anchor. Each Delta line names support once — ordered `members` plus a `hint`, or `{"anchor": "<key>"}` for an existing line-bound record. A HEAD line that occurs in the resulting Delta set inherits that occurrence's anchor; a HEAD-first `POI.Line` must supply its own.
- `validate` is read-only. It reloads the authoritative source, requires the inspected prefix to be `current` or `append-only`, verifies the base-surface fingerprint, previews the whole support batch, builds the complete resulting model, and returns planned anchor actions plus the rendered-file inventory. It mints nothing and touches no surface.
- `apply` takes a visible lock at `<chatlas-root>/locks/chat-index/<H>.lock`, revalidates under it, batch-ensures the anchors, renders the complete Delta/HEAD surface, audits the stage, and installs through a recoverable rename. Unedited Deltas survive byte-for-byte; files outside the resulting surface set are reported in `removed_paths` and dropped.
- Anchors are written before the directory swap. They are append-only and idempotent, so a retry after a failed install reuses them rather than duplicating them — this is not cross-depot atomicity.
- Append-only growth after scaffold is not a failure: `apply` installs exactly the inspected prefix, leaves HEAD at that evidence horizon, and returns the remaining tail. A `revised`, `expanded`, `diverged`, or `blocked` prefix fails closed and requires a fresh scaffold.

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
agentos chatlas turns query --identity-hash <H> --contains "<text>" --producer-type human
agentos chatlas turns query --identity-hash <H> --contains "<text>" --producer-type human --detail turn
```

- default `summary` detail returns `Normal.Turn.Ref`, Anchory-ready `member_ref`, and compact matched-event entries with exact `Event.Ref` values
- `--detail turn` adds the complete authoritative `Normal.Turn`
- `auto` scans directly when deterministic selectors already reduce the selection to at most 16 sessions; explicit `--backend sqlite` still forces candidate-index use

## View Workflow

A `Chatlas.View` is a fixed, named projection of one session's Normal Model. It
is cheap, pure, and recomputed on demand — views are never materialized, never
cached, and never stale. `agentos chatlas views list` prints the fixed registry.

```sh
agentos chatlas views get "<query>" --view full
agentos chatlas views get "<query>" --view transcript
agentos chatlas views get "<query>" --view user
agentos chatlas views get "<query>" --view replay
agentos chatlas views get "<query>" --view events
agentos chatlas views get "<query>" --view zip-transcript
agentos chatlas views get "<query>" --view zip-transcript --range 10:
agentos chatlas raw path "<query>"
agentos chatlas raw export "<query>"
```

`views get --range <range>` is a view-specific slicing surface. Range
syntax is Python-style and half-open, with forms such as `N`, `A:B`, `A:`,
`:B`, and `-N:`. The first rangeable view is `zip-transcript`, where
the range applies to the top-level `turns` sequence and the output includes a
`range` metadata object. Other views reject `--range` unless they define
their own range target.

## Event Selection And Filters

`views get` selects at event granularity and cleans fragments with named filters. Selection flags imply `--view events` when no view is named; every output stays a `Chatlas.Session.Model` fragment.

```sh
agentos chatlas views get --identity-hash <H> --contains "<distinctive text>" --role user
agentos chatlas views get --identity-hash <H> --around <iso-timestamp> --radius 3
agentos chatlas views get --identity-hash <H> --contains "<text>" --filter turns
```

- `--contains` — case-insensitive text match over event payloads
- `--role` — message events with this role (`user`, `assistant`)
- `--producer-type` (on `turns query`) — who produced the turn. `--role user` is **not** the same as a turn you typed: tool output, system reminders, and injected command stdout all arrive on the user channel, so `--producer-type human` is the filter that isolates real typed turns
- `--around` + `--radius` — nearest events to a time; radius keeps the closest `2r+1`, output stays chronological
- `--filter` — named `Chatlas.Filter`, repeatable and ordered: `slim` (strip provenance plumbing), `messages` (message events only, synced), `turns` (`messages` then `slim` — the grounding reader's preset)
- composition: with `--contains`/`--role`/`--around` selection, named filters apply **before** the window, so radius counts filter-surviving events — `--around <t> --radius 3 --filter turns` means 3 turns each side, tool events don't eat the window

## Maintenance Passes

Batch production over many sessions. `run-produce` skips fresh products, so a
pass is idempotent and safely resumable — rerun it and only the outstanding work
repeats.

```sh
agentos chatlas products run-produce --product zip-transcript-summary \
  --min-user-turns 10 --idle-for 2d --concurrency 4 --limit 50
```

- `--idle-for <duration>` keeps only sessions untouched for at least that long (`30s`, `10m`, `4h`, `3d`, `2w`). Summarizing a session you are still working in wastes the run: it goes stale on the next turn. It is a general `query` selector, so `chatlas query --idle-for 30d` also answers "what have I abandoned"
- `--concurrency N` produces N sessions in parallel. Sessions are independent — each owns its own stage directory and a depot lock keyed by `(product, identity_hash)` — and results stay in input order. Default is 1
- `--limit N` caps the batch; combine with `--sort oldest` to work through a backlog deterministically
- `--dry-run` prints each prompt and agent command without staging anything
- failures are collected in `failures` as `{identity_hash, error}` alongside the full `runs` array

**Beware `--scan-limit` when counting.** Content filters like `--min-user-turns` are applied only to the rows that survive the scan limit, so a narrower index-level filter can return *more* rows than a broader one. Raise `--scan-limit` before comparing counts.

## Product Workflow

A `Chatlas.Product` is a retained agent production over one session and one named
input view. Unlike a view it is expensive, non-deterministic, materialized, and
subject to freshness. Reads never regenerate a product: a missing or stale
product reports `production_required` and is an invitation to contribute one.

```sh
agentos chatlas products list
agentos chatlas products status --product zip-transcript-summary --identity-hash <H>
agentos chatlas products path --product zip-transcript-summary --identity-hash <H>
agentos chatlas products produce --product zip-transcript-summary --identity-hash <H>
agentos chatlas products scaffold --stage-id <stage-id>
agentos chatlas products check --stage-id <stage-id>
agentos chatlas products commit --stage-id <stage-id>
agentos chatlas products run-produce --product zip-transcript-summary --identity-hash <H>
```

- product identity is `(product name, session identity hash)`; there is no caller-supplied prompt
- `status --explain` reports the observed and current input/definition fingerprints
- `produce` stages `input.json` (the input view payload) plus the production prompt
- the producer loop is **produce → scaffold → fill → check → commit**
- `scaffold` writes the artifact skeleton: envelope fields, session, turn count, order, roles, and every user turn already copied verbatim, with assistant text left empty; `--force` overwrites an existing staged artifact
- `check` runs the full commit linter without committing — exit `0` with `check.ok: true`, or exit `1` with `check.finding` naming the POI class and the offending `turn_index`
- a blank-assistant refusal lists **every** remaining index in `evidence.blank_turn_indices`, so a partial fill can resume from the refusal instead of discovering one turn at a time
- the linter also enforces a compression floor: above 50 KB of source assistant text, an artifact retaining more than 70% of it is refused as `Compression.Insufficient`, with the longest assistant turns named in the evidence. Resummarize those turns — never truncate to reach the ratio
- a second guard windows the transcript by source assistant bytes and refuses `Compression.RegionUntouched` when a material share of those windows was left essentially uncompressed — the global ratio alone can be satisfied by crushing one region. One dense window is tolerated; the evidence names every offending turn range
- `--allow-low-compression` on `check` and `commit` waives both of the above for a session that genuinely cannot compress further, and records the exemption in the product manifest
- the gates cut both ways. `Compression.TurnCollapsed` refuses an artifact where a substantial assistant turn was reduced to a stub, naming each one with its source and summary byte sizes; `Compression.RegionCrushed` refuses when a material share of the transcript retains almost nothing. Over-retention leaves a fat but faithful artifact — collapse leaves a wrong one no reader can detect
- repair a collapse refusal by re-reading those turns in the staged input and restoring what later turns depend on. Never pad to clear the gate: the fix is restoration, and invented filler is unfalsifiable against the source
- `--allow-aggressive-compression` waives the two collapse gates. It is a separate flag on purpose — it asserts the opposite of `--allow-low-compression`, so the two are not interchangeable
- `commit` runs the same linter and refuses with the same canonical Chatlas POI on any invariant violation
- a producing agent should never hand-build the skeleton or write its own verification script; `scaffold` and `check` are the same code the commit gate runs
- `run-produce` drives the whole loop through a configured agent; `--dry-run` prints the prompt and agent command without staging
- registered products: `zip-transcript-summary` over the `zip-transcript` view — see `producer-zip-transcript-summary.md`

## Anchor Workflow

Chat anchors (`^c<YYYYMMDD>-<N>u` — `c` namespace prefix, primary-member date, counter, user-evidence tag) are the chat application of the Anchory subsystem — see `Chatlas.Anchory` in the index.

```sh
agentos chatlas anchory register \
  --line-content '- [CT] <Index line body>' \
  --member <identity-hash>:<turn-id> \
  --member <identity-hash>:<turn-id> \
  --hint "<one sentence>"
agentos chatlas anchory preview \
  --line-content '- [CT] <Index line body>' \
  --member <identity-hash>:<turn-id> \
  --hint "<one sentence>"
agentos chatlas anchory preview \
  --member <identity-hash>:<turn-id> \
  --hint "<one sentence>" \
  --detail context --radius 2
agentos chatlas anchory resolve <key> --detail context --radius 4
```

- repeat `--member` in relevance order; each session identity may be a unique prefix on input and is stored as the full identity
- `--line-content` binds Index grounding to canonical `Line.Type + body` and previews/registers a v4 record; omit it only for generic non-line support, which remains v3
- preview validates and assembles the exact record without allocating an anchor; it also reports equivalent existing anchors
- preview, registration, and resolution default to compact member summaries; `--detail turn` adds exact turns and `--detail context` adds neighborhoods
- registration allocates from the first member's date only after the support set has been reviewed
- radius counts visible turns around each exact member turn only under `--detail context`

## File Touch Workflow

Which sessions read/wrote a file, and where — answered from the normal model's `tool_invocations` (explicit-path tools: `Read`, `Write`, `Edit`, `NotebookEdit`). Substring path matching. Blind spot by design: paths inside Bash command strings are invisible to these filters.

```sh
agentos chatlas query --file-touched "<path-fragment>"
agentos chatlas query --file-write "<path-fragment>" --field identity_hash
agentos chatlas views get --identity-hash <H> --file-write "<path-fragment>" --filter slim
```

- `query` flags answer *which sessions* (mentions in prose never match — touch means a tool invocation carried the path)
- `views get` flags answer *where in the session*: the touching invocations' events as a model fragment
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

## Views And Products Surface

```sh
agentos chatlas views list
agentos chatlas views get --view <view-name> <selector-options>
agentos chatlas products list
agentos chatlas products status --product <product-name> <selector-options>
agentos chatlas products path --product <product-name> <selector-options>
```

Views are disposable projections of the Normal Model; products are retained
agent productions over one named input view. Producer references live in
`agentos-chatlas-pkg/references/`.
