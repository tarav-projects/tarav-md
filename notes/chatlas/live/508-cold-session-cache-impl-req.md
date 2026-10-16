# Cold Session Cache - impl-req

## Impl.Abstract

- **scope:** implement `Cold.Session.Cache` in `agentos-chatlas-py` session-index derivation cache.
- **status:** implemented and verified.
- **source:** Chatlas package index block `Cold.Session.Cache` and current design discussion.
- **intent:** reduce `agentos chatlas update` cache-comparison cost by ignoring already-known cold sessions during normal update.
- **observed pressure:** after `Provider.GC`, `copilot-cli` provider discovery is fast, but update still spends most time comparing cache entries.
- **non-goal:** do not skip provider discovery; cold behavior applies only to the derivation cache path after sessions are discovered.

## Impl.Index

### Cold.Session.Cache.Contract

- `Cold.Session.Cache` is a cache optimization for old known sessions.
- provider discovery still runs and discovers current sessions.
- absence of `scan_state` means hot; existing cache entries without the field keep normal behavior.
- `scan_state: "cold"` means the session cache entry is ignored completely during normal update.
- ignored completely means no expensive source-signature comparison, no raw copy, and no index derivation for that session in the normal path.
- the force flag disables cold skipping and performs the full existing comparison path.
- recommended force CLI: `--full-scan`.

### Cache.Entry.Shape

- extend each session-index derivation cache entry with cold-state metadata.
- target shape:
  - `last_activity_at`: provider activity timestamp already available from `session_ref.sort_timestamp()`.
  - `scan_state`: optional string; only `"cold"` has special meaning.
  - `cold_since`: timestamp recording when the entry first became cold.
- do not require migration for old cache entries.
- missing `scan_state` is hot by definition.
- cold metadata lives in the derivation cache entry, not in the session index row or raw archive.

### Cold.Transition.Rule

- a session becomes cold when its provider activity timestamp is older than the cold cutoff.
- initial cutoff: `30d`.
- when a session is first marked cold, set `cold_since`.
- if a discovered session has provider activity inside the cutoff, it is hot and should be compared normally.
- if a previously cold session becomes hot again, remove or omit cold fields in the next cache entry.
- normal update should keep cold entries present in the next cache so they remain known and skipped.

### Full.Scan.Flag

- add a force flag that bypasses cold skipping.
- recommended CLI: `agentos chatlas update --provider copilot-cli --full-scan`.
- `--full-scan` should also apply to `agentos chatlas index update`.
- full scan recomputes source signatures and updates cache entries for cold sessions.
- existing cache-disable flags keep their current meaning; `--full-scan` is a different concern from disabling cache entirely.

### Update.Report.Visibility

- expose cold behavior in update reports.
- add counters under `cache`, such as `cold_skip_count`, `cold_marked_count`, and `full_scan_count`.
- keep existing `hit_count`, `miss_count`, and `removed_entry_count` semantics understandable.
- report `full_scan_enabled` or equivalent in the update payload.
- progress output may remain compact; JSON output should carry enough detail for performance diagnosis.

### Implementation.Boundary

- primary implementation target: `agentos_chatlas.delta_scan`.
- likely command wiring target: `agentos_chatlas.commands` and `agentos_chatlas.core`.
- likely tests: existing `tests/test_e2e_chatlas.py` or a dedicated cache test.
- do not change provider discovery, raw archive layout, query/export behavior, or view materialization.
- work with current uncommitted `Provider.GC` changes if present; do not revert or rewrite them.

## Execution.Plan

### Slice 1 - Add full-scan plumbing

- add a `full_scan` boolean through `commands.py`, `core.py`, and `delta_scan.chatlas_delta_scan`.
- add `--full-scan` to `agentos chatlas update` and `agentos chatlas index update`.
- path: CLI args -> update kwargs -> delta scan.
- observable: JSON update payload includes full-scan state.
- check: targeted command/update test verifies `--full-scan` reaches the update payload.
- status: completed.

### Slice 2 - Persist cold cache metadata

- extend `_native_derivation_signature` or adjacent cache-entry construction to include `last_activity_at`.
- mark entries cold when `last_activity_at` is older than the 30-day cutoff.
- set `scan_state: "cold"` and `cold_since` for newly cold entries.
- preserve `cold_since` from an existing cold entry when the session remains cold.
- omit `scan_state` for hot entries so absent means hot.
- path: discovered session -> cache entry -> cache partition JSON.
- observable: update writes cold metadata for old sessions and no scan state for hot sessions.
- check: cache-entry unit test or e2e fixture inspection.
- status: completed.

### Slice 3 - Skip cold cache entries in normal update

- when `full_scan` is false and an existing cache entry has `scan_state: "cold"`, skip expensive source-signature comparison for that session.
- carry the existing cold cache entry into the next cache partition.
- count the session as unchanged/cached in report semantics.
- do not copy raw sources or derive index rows for cold-skipped sessions.
- path: provider discovery -> old cache lookup -> cold shortcut -> next cache.
- observable: update report shows cold skips and avoids source artifact comparison work for cold sessions.
- check: test where a cold cache entry exists and source files would otherwise be expensive or changed; normal update skips, full scan does not.
- status: completed.

### Slice 4 - Full-scan bypass and hot reactivation

- when `--full-scan` is passed, ignore the cold shortcut.
- recompute source signatures for cold sessions.
- if provider activity is now inside the cutoff, write a hot cache entry without `scan_state`.
- if still cold, keep or update cold metadata.
- path: cold cache entry -> full scan -> recomputed signature -> next cache.
- observable: full scan processes cold entries and can reclassify them.
- check: tests for `--full-scan` bypass and hot reactivation.
- status: completed.

### Slice 5 - Performance and regression validation

- run targeted cold-cache tests.
- run existing Chatlas e2e tests.
- run the full package test suite.
- optionally compare `copilot-cli` update JSON timing before/after on the live dataset.
- status: completed.

## Validation

- targeted tests:
  - `uv run pytest tests/test_e2e_chatlas.py -q`
  - a new or focused cold-cache test file if added.
- broad tests:
  - `uv run pytest`
- scoped lint for touched files:
  - `uv run ruff check <touched files>`

## Risks

- old cache entries do not have cold metadata; this is intentional and means hot.
- if cold entries are removed from the next cache instead of carried forward, the optimization will not persist.
- if cold skipping happens before provider discovery, new sessions can be missed; this must not happen.
- if `--full-scan` is confused with disabling cache, existing cache-control semantics may become unclear.
- if `last_activity_at` is missing or unparsable, treat the session as hot.

## Deviation.Triggers

- stop and realign if the cache entry cannot preserve cold state without changing the cache schema behavior too broadly.
- stop and realign before changing provider discovery or session index row semantics.
- stop and realign before adding automatic/random cold audits.
- stop and realign if implementing cold skipping would make normal update miss newly discovered sessions.

## Acceptance.Signals

- normal update still performs provider discovery.
- cache entries can include `last_activity_at`, `scan_state: "cold"`, and `cold_since`.
- entries without `scan_state` are treated as hot.
- normal update ignores explicit cold entries completely after discovery.
- `--full-scan` forces cold entries through normal comparison and cache refresh.
- update JSON reports cold skip behavior.
- existing Chatlas update/query/raw behavior remains green under tests.

## Impl.Log

- 2026-06-09: Impl.Req created from `Cold.Session.Cache` design discussion; execution not started.
- 2026-06-09: Implemented in `agentos-chatlas-py`. No provider discovery, raw archive layout, query/export behavior, or view materialization changes were needed.
- 2026-06-09: Validation passed: `uv run pytest tests/test_cold_session_cache.py -q`; `uv run pytest tests/test_e2e_chatlas.py tests/test_chatlas_gc.py tests/test_cold_session_cache.py -q`; `uv run pytest`; scoped `uv run ruff check src/agentos_chatlas/delta_scan.py src/agentos_chatlas/core.py src/agentos_chatlas/commands.py tests/test_cold_session_cache.py`.
