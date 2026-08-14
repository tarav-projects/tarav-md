# 510 — Chatlas Tiered `--update` Flag — Impl.Req

## Impl.Abstract

- **Goal:** let a Chatlas read command refresh the data it is about to read, in one call, paying only for what the read actually needs.
- **Surface:** a reusable `--update` flag on the read commands (`query`, `recents`, `views inline`, `stats`), plus the scoped mtime-window update primitive it depends on.
- **Core model — escalation ladder.** `--update` runs the cheapest *applicable* update and escalates only when a cheaper tier left the read empty:
  1. **Direct** — an exact session selector (`--session-id`/`--uri`/`--identity-hash`) names the session: resolve straight to the id and targeted-update it. No index pre-query. Reuses the existing `session_ids` path.
  2. **Index-resolve → direct** — no exact id: query the index by *structural* selectors (provider, window) for candidate ids, then targeted-update those. Reuses the `session_ids` path; adds an index pre-query.
  3. **Recent** — scoped mtime-windowed instance scan to catch sessions whose index timestamp is stale, or that are new since last ingest. **New primitive.**
  4. **Full** — the current full delta sweep. Last resort.
- **Timestamp-trust boundary:** Tiers 1–2 trust the index (its session ids and `last_activity_at`); Tiers 3–4 trust the disk (source mtime). This boundary is *why* the ladder works: a time-window read whose index `last_activity_at` is stale precisely because new turns are un-ingested will under-resolve at Tier 2 and only be caught at Tier 3.
- **Start-tier rule:** enter at the cheapest applicable tier, not always Tier 1 — exact identity selector → Tier 1; only a time window → Tier 2; nothing → Tier 3. Freshness-sensitive time-window reads (`recents`, `my-session-id`) commonly settle at Tier 3.
- **Stop rule:** run a tier, re-run the read, stop as soon as the read is non-empty (or the ladder is exhausted). `--update=direct|index|recent|full` jumps straight to a tier.
- **Status:** implemented (Slices 1–4). Tests green; one pre-existing unrelated suite failure noted in `Impl.Log`. Changes uncommitted.
- **Source context:** design discussion in this session (no prior design-session artifact). Motivating consumer: the `tarav-chatlas-my-session-id` skill, whose `update → recents → match` pipeline this collapses into `recents --update`.

### Scope

- In: the three update tiers as callable primitives; a shared `--update` argument + escalation wrapper; wiring it into `query`, `recents`, `views inline`, `stats`; behavior tests per slice.
- In: exposing the new **scoped (mtime-window) update** as a standalone update option so it is independently testable.
- Out: the `my-session-id` skill rewrite is optional (last slice, doc-only) — not required for the feature.
- Out: changing the existing default `agentos chatlas update` behavior. Bare `update` stays the full sweep.
- Out: a richer per-read "satisfied" predicate beyond "non-empty result" at the CLI level. Callers needing "exactly one" (my-session-id) read the counts themselves.

## Impl.Index

### Block: existing targeted-update reuse (Tiers 1 & 2)
- `chatlas_update(session_ids=...)` (`agentos-chatlas-py/src/agentos_chatlas/core.py:16-53`) already routes to `chatlas_single_session_update` (`session_refresh.py:18`), which locates each id via the index first and falls back to a provider-instance walk on miss.
- **Implication:** neither Tier 1 nor Tier 2 needs a new refresh mechanic — both call this path. Tier 1 passes ids taken directly from exact selectors (`--session-id`/`--uri`/`--identity-hash`); Tier 2 first runs an index query over structural selectors to derive the candidate ids, then passes those.

### Block: timestamp-trust boundary
- The query selectors that name a session exactly (`--session-id`, `--uri`, `--identity-hash`, lines ~596-600/571-580 in `commands.py`) make Tier 1 exact and index-pre-query-free.
- `--active-after` (line ~611) filters on the index `last_activity_at`, which is stale exactly when un-ingested turns are the reason for the update — so a Tier-2 candidate resolve by time window can omit the very session that needs refreshing.
- **Implication:** Tiers 1–2 trust index identity/timestamps; Tier 3 (mtime scan) trusts disk. The escalation is the mechanism that bridges the gap — do not try to make Tier 2 "smart" about staleness; let it under-resolve and escalate.

### Block: scoped mtime-window scan is missing
- `chatlas_index_update` → `chatlas_delta_scan` (`delta_scan.py:156`) has no "only sessions touched in the last N seconds" parameter; it walks configured instances and relies on the per-session derivation cache + an internal `cold_session_cutoff_seconds` to skip cold work.
- **Implication:** Tier 2 is new. Add an mtime-window cutoff that filters discovered sessions to `source_mtime > now − window` *before* derivation, short-circuiting the per-instance enumeration cost where possible. Reuse the existing per-session timestamp already computed in the scan.

### Block: read commands and their selectors
- Query selectors live in `_add_chatlas_query_selector_arguments` / `_chatlas_query_selector_kwargs` (`commands.py` ~570-710); `recents` has `--days`/`--provider`/`--limit` (`recents.py:16`); both already carry the *structural* selectors (`providers`, `active_after`/window) the update should scope by.
- `chatlas_query` returns `query_matched_row_count` and `returned_row_count` (`query.py:144-146`) — the escalation stop-signal.
- **Implication:** the wrapper derives the update scope from the command's already-parsed structural selectors; content predicates (`--user-contains`, etc.) are **excluded** from update scoping and applied only to the final read.

### Block: critical correctness constraint — scope vs. content
- Tier 1 must resolve candidates using only structural selectors (provider, active window). Filtering candidates by content (`--user-contains`) against the stale index would drop the very session whose matching turn is not yet ingested — defeating the purpose.
- **Decision:** structural selectors scope the update; content predicates filter only the post-update read.

### Block: escalation predicate
- CLI-level "satisfied" = `returned_row_count > 0`. Simple, command-agnostic.
- Per-command richer predicates (e.g. "exactly one" for self-location) stay caller-side: the caller reads the counts and decides; the CLI does not encode them.

## Execution.Plan

Ordered vertical slices. Each reaches an observable CLI result and is checked by a behavior test under `agentos-chatlas-py/tests/`. RED before the change, GREEN after.

### Slice 1 — Scoped mtime-window update primitive (Tier 3)
- **Changes:** add an mtime-window cutoff to the delta-scan path (`chatlas_delta_scan` / `chatlas_index_update`); discovered sessions older than the window are skipped before derivation. Thread it through `chatlas_update`.
- **Path exercised:** `update` → `chatlas_index_update` → `chatlas_delta_scan` with a window cutoff.
- **Observable:** `agentos chatlas update --since <seconds>` (name TBD: `--since` / `--recent-window`) re-ingests only recently-touched sessions.
- **Check (RED→GREEN behavior test):** given two on-disk sessions, one with a fresh source mtime and one older than the window, a windowed update ingests the fresh one and skips the old one; a bare full update ingests both.

### Slice 2 — Shared `--update` flag + escalation ladder, on `query`
- **Changes:** add a reusable `_add_update_flag(parser)` (value form `direct|index|recent|full`, bare `--update` = ladder entered via the start-tier rule) and a `run_read_with_update(args, read_fn, scope_fn, satisfied_fn)` helper applied to `_cmd_chatlas_query`. `read_fn` is the existing one-liner; `satisfied_fn` defaults to `returned_row_count > 0`. The helper: pick the start tier from the selectors → run that tier → re-run the read → escalate to the next tier while unsatisfied and tiers remain.
- **Start-tier selection:** exact id selector present → Tier 1; else a structural window → Tier 2; else → Tier 3.
- **Path exercised:** `query --provider X --user-contains Y --update` → (no exact id) start Tier 2 → index-resolve ids by provider → targeted update → re-query → escalate to Tier 3 if still empty.
- **Observable:** a query that returns 0 against a stale index returns the fresh match with `--update`, without the caller running `update` first.
- **Check (RED→GREEN):** (a) `query --session-id <id> --update` enters Tier 1 with no index pre-query and refreshes that id; (b) seed an un-ingested turn on disk, `query --user-contains <turn>` → 0, same query `--update` → 1, escalating Tier 2→3; assert the update scope used provider/window, never `--user-contains`.

### Slice 3 — Apply `--update` to remaining reads
- **Changes:** apply the shared flag + wrapper to `recents`, `views inline`, `stats`. Each derives its own structural scope (`recents` from `--days`/`--provider`; `views`/`stats` from their selectors).
- **Observable:** each command accepts `--update` and freshens before reading.
- **Check:** per-command behavior test that `--update` triggers a scoped update with the command's structural selectors and the read runs against the freshened index. `stats` (no row predicate) runs a single targeted update without escalation.

### Slice 4 — (Optional, doc-only) Adopt in `my-session-id` skill
- **Changes:** update `agentos-chatlas-md/skills/tarav-chatlas-my-session-id/SKILL.md` to use `recents --provider <p> --days <d> --update` in place of the manual `update` + `recents` two-step.
- **Observable:** the skill workflow drops a step; the token-discipline / file-pipe guidance is unchanged.
- **Check:** skill reads correctly end-to-end (manual run); no code test.

### Risks & deviation triggers
- **Scope-vs-content leakage** — if the wrapper ever scopes the update by content predicates, self-locating/just-ingested reads break. Guard with an explicit test (Slice 2 check). If the structural/content split is unclear for a given command, stop and raise.
- **Escalation reaches Tier 4 by design** — bare `--update` escalates all the way to the full sweep if cheaper tiers leave the read empty. Decision: the user wants an up-to-date Chatlas, so a guaranteed-fresh result outranks worst-case cost. No max-tier cap. `--update=<tier>` still pins a single tier for callers who want to bound cost explicitly.
- **mtime-window primitive (Slice 1 / Tier 3) is the dependency** — if the windowed scan can't reuse the existing per-session timestamps cheaply and needs a full enumeration anyway, surface it: Tier 3's value depends on skipping enumeration, not just derivation.

### Acceptance signals
- `query`/`recents` with `--update` return freshly-ingested results a bare read misses.
- Known-identity reads settle at Tier 1; time-window reads (`recents`, `my-session-id`) commonly settle at Tier 3; Tier 4 fires only when cheaper tiers leave the read empty.
- All new behavior tests GREEN; existing Chatlas tests unaffected.
- Update scope is provably structural-only (asserted in test).

## Impl.Log

- **Tier-3 recency signal:** realized the "source mtime" window via `ChatlasDiscoveredSession.session_ref.sort_timestamp()` (codex: content `updated_at` coalesced with rollout file mtime). It is the per-session, disk-derived, index-independent timestamp the cold logic already uses — faithful to the design's disk-trust intent without a new mtime probe.
- **Window skips derivation, not enumeration:** the filter drops out-of-window sessions before `sources()`/derivation/raw-copy/index, but per-instance discovery still enumerates refs (same shape as the existing cold-skip). Matches the Slice-1 risk note; acceptable since derivation/copy dominate cost.
- **Flag name resolved:** `--recent-window <duration>` (Impl.Req left `--since`/`--recent-window` open). Parses via the existing `parse_duration_seconds` (`60s`, `30m`, `1h`, `2d`).
- **stats/views satisfied predicate:** both run a single start-tier update with `satisfied_fn=lambda _: True` (no escalation), per scope note "`stats` runs a single targeted update." `recents` uses `entry_count > 0`; `query` uses `returned_row_count > 0`.
- **Test-fixture decision (open space):** codex `read_codex_index_session_refs` coalesces each entry's `updated_at` with the `session_index.jsonl` file mtime, so a session listed in a freshly-written index always looks fresh. The Slice-1 fixture therefore models an old session as rollout-only (old rollout mtime, not in the recent index) — a realistic "old session not in the recently-written index" shape.
- **Pre-existing failure (not mine):** `tests/test_chatlas_gc.py::test_chatlas_gc_dry_run_and_apply_moves_old_archived_sources` fails identically on the pre-change checkpoint (`no configured instances match providers=['codex'] instances=['codex-work']`). Left untouched — out of scope.
- **Minor process deviation:** Slice 2's helper was written before its test; RED was still established (the `--update` flag did not exist, so the pre-impl call errored at argparse). Subsequent slices kept test-then-verify.
