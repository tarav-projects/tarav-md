# Chatlas View Materialization Lock - impl-req

## Impl.Abstract

- **scope:** Add visible, cross-platform, per-depot locking to Chatlas view materialization and commit paths so concurrent operations targeting the same `View.Identity` serialize safely.
- **status:** implemented
- **target project:** `agentos-chatlas-py`
- **source context:** confirmed concurrent depot-replacement race in `agentos_chatlas/views/framework.py`; user alignment on `filelock`, one central lock-file folder, and `Chatlas.Lock.Visibility`
- **durable design:** `tarav-chatlas-pkg/index/100-index.md` — `Chatlas.Lock.Visibility`, `Chatlas.View.Model`, `View.Identity`
- **out of scope:** global scheduling, locking fresh reads, automatic stale-lock recovery, silent lock deletion, lock-breaking behavior, lock sidecar metadata, and a lock-inspection CLI

## Impl.Index

### Materialization.Race

- `View.Identity` deterministically resolves to one `View.Depot`; concurrent operations for the same identity therefore target the same directory
- `_ensure_available(...)` currently lets multiple callers observe `missing` or `stale` and produce the same programmatic view concurrently
- `_replace_directory(...)` checks whether the target exists and then renames it without synchronization, creating a time-of-check/time-of-use race
- concurrent replacements can fail with `FileNotFoundError` or `Directory not empty`, leave `.old-*` directories, and expose a temporarily missing depot to readers
- both programmatic production and staged agentic-view commits use the same replacement helper
- transcript and full exports converge on the shared `chatlas-session/<cache-key>` depot before projecting their requested output

### View.Materialization.Lock

- one materialized view depot may have only one active materializer or committer
- lock identity is `(View.Name, Cache.Key)`, matching the depot identity rather than globally locking all Chatlas views
- lock files live together under `<chatlas-root>/locks/views/`
- use a flat, deterministic lock filename such as `<view-name>--<cache-key>.lock`
- use the `filelock` package so the coordination primitive is cross-platform from the beginning
- different view identities retain independent locks and may continue concurrently

### Lock.Scope

- fresh reads do not acquire locks
- when `_ensure_available(...)` observes a missing or stale programmatic view, it acquires the target view lock, rechecks status under the lock, and produces only if the view remains missing or stale
- the recheck allows a waiting caller to reuse the materialization completed by the previous lock holder
- staged agentic-view commit acquires the target view lock before observing final dependencies and replacing the target depot
- lock ownership must cover the complete mutation-critical section, not only `_replace_directory(...)`
- dependency materialization may acquire locks for dependency view identities; declared view dependencies are expected to remain acyclic

### Chatlas.Lock.Visibility

- every actual lock lifecycle is visible; no lock acquisition, wait, or release happens silently
- shared lock functions print lifecycle messages directly to `stderr`, preserving structured command output on `stdout`
- immediate acquisition prints `acquiring`, `acquired`, and `released`
- contention additionally prints `waiting for active materialization lock`
- every lifecycle message includes the exact lock-file path
- required message shapes are `[chatlas] acquiring materialization lock: <lock-path>`, `[chatlas] waiting for active materialization lock: <lock-path>`, `[chatlas] acquired materialization lock: <lock-path>`, and `[chatlas] released materialization lock: <lock-path>`
- lock messages are not suppressed by unrelated quiet/progress modes
- operations that do not acquire a lock, including fresh reads, print no lock lifecycle messages

### Lock.Recovery

- Chatlas performs no automatic stale-lock recovery, lock breaking, or lock-file deletion
- visible lock actions and the exact lock-file path are the recovery mechanism
- agents may inspect a reported lock and surrounding depot state when a command appears stuck or fails
- implementation must not infer that a persistent lock file means an active lock; `filelock` ownership is authoritative
- after printing that an active lock is being awaited, acquisition blocks until the lock is acquired or the caller interrupts the command
- the initial implementation adds no periodic wait messages, automated lock timeout, or timeout-driven recovery action

### Replacement.Boundary

- locking should prevent concurrent writers from entering `_replace_directory(...)` for the same depot
- existing temporary-depot construction and replacement behavior may remain unless implementation discovers a correctness issue outside concurrent same-depot writes
- replacement failures must still clean the current caller's temporary directory
- implementation should not add compatibility paths or retain an unlocked mutation route

## Execution.Plan

### Slice 1 — Add visible per-depot lock primitive

- **changes:** add `filelock` as an `agentos-chatlas-py` runtime dependency; add a shared lock-path resolver and context manager for `(View.Name, Cache.Key)`
- **path:** `pyproject.toml` → Chatlas view framework lock helper → lock lifecycle messages on `stderr`
- **observable:** acquiring and releasing a view lock creates visible messages containing `<chatlas-root>/locks/views/<view-name>--<cache-key>.lock`
- **check:** focused tests cover immediate acquisition, active-lock waiting, acquisition after waiting, release on success, and release on exception
- **status:** completed

### Slice 2 — Serialize programmatic materialization

- **changes:** update `_ensure_available(...)` so missing/stale programmatic views acquire the per-depot lock, recheck freshness under lock, and produce only when still required
- **path:** export or view request → initial status check → visible lock lifecycle → under-lock status recheck → programmatic production or reuse → artifact read
- **observable:** concurrent transcript/full exports for one missing or stale session model all succeed while only one caller performs the required materialization
- **check:** concurrent same-session export test; assert lifecycle output is on `stderr`, JSON remains valid on `stdout`, final depot is fresh, and no `.tmp-*` or `.old-*` directories remain
- **status:** completed

### Slice 3 — Serialize staged agentic-view commits

- **changes:** acquire the same per-depot lock during `chatlas_views_commit(...)` before final dependency observation and target depot replacement
- **path:** staged artifact validation → visible target lock lifecycle → final dependency observation → committed manifest construction → depot replacement
- **observable:** concurrent commits targeting the same agentic `View.Identity` serialize instead of racing in `_replace_directory(...)`
- **check:** focused concurrent commit test verifies successful serialization, a valid final depot, and no temporary or backup leftovers
- **status:** completed

### Slice 4 — Prove lock granularity and operational contract

- **changes:** add boundary tests and update active Chatlas operational documentation where lock visibility affects command behavior
- **path:** same identity contention versus different identity independence → CLI diagnostics → documented behavior
- **observable:** same-depot operations serialize; different depots can acquire their locks independently; fresh reads emit no lock messages
- **check:** tests cover independent lock paths, fresh-read silence, exact lock-path presence in every lifecycle message, no automatic lock deletion/recovery, and full targeted view/export suite
- **status:** completed

## Risks And Deviation Triggers

- if `filelock` cannot distinguish an immediate acquisition from a contended acquisition without polling or private APIs, stop and align before weakening the required `waiting` message
- if protecting staged commits requires locking before long-running agent production, stop and realign; the accepted scope locks commit/materialization, not the external agent run
- if an existing mutation path cannot be routed through the shared visible lock primitive, record it explicitly and stop before leaving a silent unlocked writer
- if concurrent dependency locking reveals a possible dependency cycle, stop and surface the cycle rather than adding timeout-based recovery

## Acceptance Signals

- concurrent same-session exports against a missing or stale `chatlas-session` depot all succeed
- concurrent same-identity programmatic materialization and agentic commit paths serialize through one deterministic lock file
- different view identities remain independently lockable
- fresh reads remain lock-free
- every actual acquire, wait, acquired, and release action is printed to `stderr` with the exact lock-file path
- Chatlas performs no automatic lock recovery or silent lock deletion
- final depots validate and no `.tmp-*` or `.old-*` directories remain after concurrency tests

## Impl.Log

- 2026-06-06: Impl.Req created after reproducing the same-depot replacement race and aligning on a simple visible-lock model using `filelock`.
- 2026-06-06: `Chatlas.Lock.Visibility` promoted into the public Chatlas index; fresh reads remain lock-free, while every actual lock action must be visible.
- 2026-06-06: Added pinned `filelock` runtime dependency and shared visible per-`View.Identity` lock primitive under `<chatlas-root>/locks/views/`.
- 2026-06-06: Programmatic materialization now locks missing/stale production, rechecks status under lock, and reuses work completed by a preceding materializer.
- 2026-06-06: Staged agentic commits now hold the target view lock from final dependency observation through depot replacement.
- 2026-06-06: Added focused tests for immediate and contended lifecycle visibility, exception release, persistent diagnostic lock files, independent identities, fresh-read silence, single programmatic production, and serialized staged commits.
- 2026-06-06: Verification passed for focused tests and changed-file lint. Full suite result was 98 passed and 2 pre-existing failures caused by external Chatlas configuration referencing unknown agent instance `codex-work`.
