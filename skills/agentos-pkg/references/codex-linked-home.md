# Codex Linked Home

Reference for the intended `Linked.Home` pattern used by Codex homes.

## Model

Codex homes may operate as a `Linked.Home` set:

- one base home owns selected shared subcomponents
- other Codex homes link those subcomponents back to the base home or to a common shared depot
- each linked home keeps its own local state for the parts that should remain separate

Codex splits its session storage across two layers:

- `codex_home` stores rollout files and home-local surfaces such as `sessions/`, `history.jsonl`, `skills`, `hooks`, and `hooks.json`
- `sqlite_home` stores the SQLite-backed runtime state used for thread metadata, logs, goals, and memories

## Intended Shared Set

The intended shared set for each Codex linked home is:

- `AGENTS.md`
- `skills`
- `hooks`
- `hooks.json`
- `sessions/`
- `history.jsonl`
- `sqlite_home`

## Why Each One

- `AGENTS.md` is shared so the homes inherit the same durable agent instructions
- `skills` is shared so the same imported skill surface is available from every Codex home
- `hooks` is shared so hook scripts stay aligned across homes
- `hooks.json` is shared so hook configuration stays aligned across homes
- `sessions/` is shared so rollout JSONL session artifacts accumulate into one common depot
- `history.jsonl` is shared so prompt history accumulates into one common append-only log
- `sqlite_home` is shared so thread metadata, logs, goals, and memories accumulate into one common SQLite-backed runtime store

## SQLite Home

The shared `sqlite_home` should be treated as one coherent runtime store, not as isolated database files.

It owns:

- `state_5.sqlite`
- `logs_2.sqlite`
- `goals_1.sqlite`
- `memories_1.sqlite`

The intended mechanism is a shared `sqlite_home` configuration that points to the base home or other chosen shared runtime store, rather than hand-linking individual SQLite files.

## Construction Guidance

When constructing a Codex `Linked.Home` set:

- prepare the base home first, so every intended shared surface actually exists there before other homes link to it
- link shared `codex_home` surfaces to the base home or to a common depot
- configure linked homes to use the shared `sqlite_home` instead of keeping independent SQLite runtime stores
- keep home-local configuration local unless there is a separate reason to normalize it
- validate shared session behavior by creating and resuming sessions across homes, not only by inspecting files

## Operational Notes

- interactive Codex/TUI turns append to shared `history.jsonl`; non-interactive `codex exec` runs should not be used as the only validation path for `history.jsonl`
- a linked home that switches to shared `sqlite_home` may still have stale local SQLite artifacts from before the switch
- those stale local SQLite artifacts should be moved to a backup folder or removed after validation, so the home shape matches the intended model
- after migration, linked variant homes should have no active local SQLite runtime files outside explicit backup locations
- the shared state DB may contain rollout paths with different home-shaped prefixes such as `~/.codex/...` and `~/.codex-mm/...`
- that mixed-path state is acceptable as long as each linked home's `sessions/` path resolves to the same shared rollout depot
- file-shape validation is a useful first check, but it is insufficient on its own
- cross-home resume is the practical validation target for the linked session model: a session created in one home should be continuable from another home

## Local Set

Codex linked homes should normally keep these local:

- `config.toml`
- `auth.json`
- caches
- temporary files
- shell snapshots
- other home-specific runtime state not explicitly listed in the shared set

## Boundary

- this reference defines the intended shared Codex subcomponents, not all home contents
- linked Codex homes still keep local state outside this shared set
- the base home may need one-time preparation so shared surfaces such as `AGENTS.md`, `hooks`, or `hooks.json` actually exist there before other homes link to them
- this is Codex-specific operational guidance, not the full definition of `Linked.Home`
