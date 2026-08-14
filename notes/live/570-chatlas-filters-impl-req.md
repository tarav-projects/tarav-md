# Chatlas Named Filters — Impl.Req

## Impl.Abstract

- **Goal**: implement `Chatlas.Filter` — shape-preserving, composable, named operations on normal model objects — so consumers (the index/linking system first) can strip fragment noise with preset pipelines instead of bespoke surfaces.
- **Scope**: filter registry + repeatable `--filter` flag on `views inline`; starter presets `slim`, `messages`, `turns`; selection flags (`--contains`/`--role`/`--around`/`--radius`) re-expressed on the same filter pipeline internally; mint echo switched to the `turns` preset.
- **Out of scope**: the legacy named-view (`Chatlas.View.Model`) rework to model-object products (future design session, declared in `Chatlas.View`); a `--filter` mini-grammar for parameterized filters (the ergonomic flags stay the parametric surface); filters on other commands than `views inline` (extend when workflows demand).
- **Repos**: `agentos-chatlas-py` only (`normalization/session_model/_views.py`, new `normalization/session_model/filters.py`, `inline.py`, `anchory.py`, `commands.py`, `tests/test_e2e_chatlas.py`).
- **Source**: this design session — `Chatlas.View`/`Chatlas.Filter` index blocks (tarav-chatlas-pkg `design/100-design.md`, committed `f6f0e58`); builds on 569 (executed, uncommitted in the worktree — this work stacks on it).
- **Status**: implemented (2026-07-08); all three slices, suite 125 green, live-verified (`--anchor 20260708-0 --filter turns`)

## Impl.Index

### Design.Authority
- `Chatlas.View`: closed operation on the model space — output never leaves it
- `Chatlas.Filter`: shape-preserving view — same shape out, content reduced; named filters are registered presets; parameterized selection runs on the same pipeline behind ergonomic flags
- both blocks live in the chatlas index; this impl realizes them read-side

### Current.State *(inspected, cited)*
- selection today: `_select_events` (`_views.py:244`) applies `contains`/`role`/`around`/`radius` inside `_project_session_model_view` (`_views.py:46`) — parametric filtering exists but is not expressed as filters
- real event envelope (verified live): `event_id, interaction_ref, kind, model_run_ref, native, payload, producer, sequence, source_refs, surfaces, timestamp`; top-level model keys: `agent_instance, chat, class, normalization, schema_version, session, sources, view`; `chat`: `events, messages, model_runs, tool_invocations, usage`
- mint echo (`anchory.py`, `chatlas_anchory_register`) projects `view="events"`, `radius=4` — full envelopes, noisy
- 569 changes are uncommitted in the worktree; this effort stacks on them (single review unit or sequential commits — user's call at review)

### Filter.Contract
- a filter is `(model_object) -> model_object`: same `class`/shape, content reduced; never adds or renames fields
- registry: name → filter callable, in new `normalization/session_model/filters.py` (model-space code owns model-space operations)
- filters apply in caller order; unknown name → `CliError` listing registered names
- deep-copy discipline: filters never mutate their input (match projection behavior)

### Starter.Presets
- `slim` — reader preset, strips provenance plumbing: per-event drop `native`, `source_refs`, `lineage`, `producer`, `surfaces`, `model_run_ref`; top-level drop `normalization`, `sources`; keep `event_id`, `sequence`, `timestamp`, `kind`, `payload`, `interaction_ref`
- `messages` — keep only `kind == "message"` events; resync `chat.messages` from surviving events; drop `chat.usage` entries and `model_runs`/`tool_invocations` rows no longer referenced
- `turns` — the grounding reader's preset: `messages` then `slim` (a named composition, demonstrating preset-as-composition)

### Pipeline.Order
- `views inline` pipeline: load model → parametric selection filters (`contains`/`role`/`around`/`radius`, as today's `_select_events` re-expressed as filters) → view projection → named `--filter` chain in caller order
- rationale: parametric selection picks the evidence; projection picks the shape; named presets clean the envelope — each stage stays model-closed so order changes remain legal refactors later

### CLI.Surface
- `--filter <name>` on `views inline`, repeatable (`action="append"`), applied in order
- help text lists the registered presets
- selection flags unchanged externally — internal rework only

### Echo.Integration
- `chatlas_anchory_register` neighborhood echo applies the `turns` preset — the double-check surface becomes human-readable
- `--anchor` resolution keeps `events` as its default view; callers add `--filter turns` (or the echo shows the precedent)

## Execution.Plan

### S1 — Registry + named filters on `views inline` (test-first)
- what changes: `filters.py` with registry + `slim`/`messages`/`turns`; `--filter` flag; application after projection
- RED: `--filter slim` strips the named keys (event + top level) and nothing else; `--filter messages` leaves only message events with `messages` resynced; `--filter turns` equals `--filter messages --filter slim`; unknown filter errors listing names; filters compose in order; output `class`/`view` fields intact
- check: suite green; live: `--anchor 20260708-0 --radius 2 --filter turns` returns a clean turns-only neighborhood
- observable: fragment noise removable by name

### S2 — Selection flags re-expressed as filters
- what changes: `_select_events` logic moves into `filters.py` as parameterized filter constructors (`contains(text)`, `role(name)`, `around(at, radius)`); `_project_session_model_view` consumes them through the same apply-chain used by `--filter`
- RED: none new — this is an internal refactor; the existing selection tests are the behavior lock (`No.Regression.Tests.Allowed`: no new tests for unchanged behavior)
- check: full suite green, selection tests untouched and passing
- observable: one pipeline, two entry surfaces (flags and names)

### S3 — Mint echo on `turns`
- what changes: `chatlas_anchory_register` applies `turns` to its neighborhood payload
- RED: existing echo test updated — echo events carry no `native`/`source_refs`; landing turn text/timestamp still present
- check: suite green; live re-check of the echo shape via a scratch-depot mint
- observable: mint double-check readable at a glance

### Acceptance signals
- `agentos chatlas views inline --anchor <a> --filter turns` → neighborhood of clean `{timestamp, kind, payload…}` message events, no plumbing keys
- unknown `--filter` errors helpfully; full `agentos-chatlas-py` suite green
- `link.md` step-4 re-verify example gains `--filter turns` (agentos-md, same pass)

### Risks / deviation triggers
- `messages` resync semantics: reuse the existing `_messages_from_events`/projection helpers — if resync rules turn ambiguous for non-transcript views, stop and surface (design decision, not open space)
- preset key lists are the contract: if the model schema adds envelope keys, `slim` must be revisited — note the coupling in `filters.py`
- if stacking on the uncommitted 569 diff complicates review, pause for the user to review/commit 569 first

## Impl.Log

- 2026-07-08: executed in `Alignment.Mode::Autonomous`; 4 new behavior tests (S1), echo test tightened (S3), S2 pure refactor locked by existing selection tests.
- open-space decision (S1): `messages` keeps `model_runs`/`usage` rows referenced by surviving events (via `model_run_ref`) and empties `tool_invocations`; resync reuses `_messages_from_events`.
- open-space decision (S1): filter registry lives in `normalization/session_model/filters.py` — model-space code owns model-space operations; `slim` key lists documented there as a schema-coupled contract.
- note (S2): the event-selection constructors (`contains_filter`, `role_filter`, `around_filter`) operate on event lists (fragment components), while named filters operate on whole model objects — two arities, one module; unify only if a workflow demands whole-object parametric filters.
