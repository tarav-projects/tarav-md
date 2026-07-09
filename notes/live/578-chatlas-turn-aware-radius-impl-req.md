# Chatlas Turn-Aware Radius — Impl.Req

## Impl.Abstract

- **Goal**: make `agentos chatlas views inline --anchor X --radius N --filter turns` show the N surrounding *turns* in chronological order — the anchor-resolution window a `--gr-review` reviewer actually needs (landing turn plus the preceding assistant proposal).
- **Problem today** (observed live during the 577 Gr.Req review, 2026-07-09):
  1. `around_filter` selects the `2r+1` events nearest by time-distance over ALL raw events — tool events consume the window, so `--radius 3` around a turn in a tool-heavy stretch returns only the landing turn; a reviewer needed `--radius 60` to see the preceding proposal.
  2. the selected events are returned in **distance order**, not chronological — the output reads shuffled.
  3. named filters (`turns`) apply after projection (`apply_chatlas_filters` is the last step), so message-pruning happens after the window is already spent.
- **Fix shape**: no new flags. (a) `around_filter` returns chronological output — plain bug fix. (b) when selection flags AND `--filter` names are both supplied, apply the named filters to the model *before* projection/selection, so radius counts post-filter events. The composition `--anchor X --radius 3 --filter turns` then IS the turn-radius.
- **Out of scope**: a `--radius-turns` flag (interface growth without demand); changing distance-based candidate picking to sequence-based; query-layer (`query.py`) selection.
- **Repos**: `agentos-chatlas-py` only. Reinstall after CLI-visible changes: `uv tool install --reinstall --editable .` from `agentos-cli/`.
- **Source**: live failure in session `99144906-781e-43cc-9d27-b40f166e2acf` (2026-07-09, second 577 review sitting); index concepts `Chatlas.View`, `Chatlas.Filter` (chatlas 100), `Chatlas.Anchory` (+ appendix reading rule: "the anchor lands in an evidence neighborhood — read the landing turn and around it").
- **Status**: designed; ready for execution

## Impl.Index

### Design.Decisions

- radius semantics become: "N nearest events each side *among the events your filters kept*" — one radius concept, composable, no new flag
- chronological output is unconditional (fix 1 applies even without named filters) — distance order was never useful to a reader
- pre-applying named filters happens ONLY when selection flags are present alongside `--filter`; the no-selection path keeps today's post-projection order (shape-preserving filters on a projected view)
- when filters are pre-applied, do not re-apply them post-projection (they are idempotent, but double work and double deepcopy are pointless); the returned payload must be identical either way for the no-selection path
- precedent: file-touch selection already prunes `chat.events` before projection (`inline.py`, `_FILE_TOOLS` block) — this change makes named filters consistent with that
- the `--anchor` default radius stays `4`; with `--filter turns` that now means up to 9 messages — the intended review neighborhood

### Current.State *(inspect before coding)*

- pipeline: `src/agentos_chatlas/inline.py` `chatlas_views_inline` — anchor resolve → session select → model load → file-touch pre-prune → `project_chatlas_session_model_view(...)` → `apply_chatlas_filters(projected, filters)` (last)
- windowing: `src/agentos_chatlas/normalization/session_model/filters.py` `around_filter` (lines ~104-127): builds `(distance, index, event)` tuples, sorts by distance, truncates to `2r+1`, returns in that order
- selection composition: `build_event_selection` — contains → role → around, applied in `_views.py` `_project_session_model_view` over `chat.events`
- named filters: `CHATLAS_FILTERS` registry (`slim`/`messages`/`turns`) — model→model, shape-preserving, idempotent
- existing test coverage on around/radius: ~none (4 grep hits total in tests/) — the RED tests below are the first real coverage

## Execution.Plan

*(test-first; reuse the e2e fixture machinery in `tests/test_e2e_chatlas.py` — the rollout writers can interleave tool events between messages)*

### S1 — chronological window output
- what: `around_filter` sorts its selected events by timestamp (ties: original index) before returning
- RED: unit test on `around_filter` — events at t0..t6, target t3, radius 2 → returns the 5 nearest **in chronological order**; today it returns them distance-ordered
- check: suite green
- status: pending

### S2 — filters before selection in the inline pipeline
- what: in `chatlas_views_inline`, when `has_selection` and `filters` are both truthy, apply `apply_chatlas_filters(session_model, filters)` to the loaded model before projection and skip the post-projection application; otherwise unchanged
- RED: pipeline test — session with messages `u1 a1 u2 a2` and 10 tool events packed between `a1` and `u2`; `chatlas_views_inline(anchor→u2, radius=1, filters=("turns",))` returns exactly `a1 u2 a2` (today: tool events eat the radius, `a1` missing); plus a no-selection regression assert: `filters=("turns",)` without selection returns byte-identical payload to today's path
- check: suite green
- status: pending

### S3 — live acceptance + docs
- what: reinstall; rerun the live failing case: `agentos chatlas views inline --anchor 20260707-3 --radius 3 --filter turns` must show the assistant proposal turn preceding the "apply" landing turn, chronologically; update `agentos-chatlas-md/skills/agentos-chatlas-pkg/references/chatlas-commands.md` anchor-resolution section (state the composed semantics: radius counts filter-surviving events, output chronological)
- check: live output correct; both index depots still lint clean; `uv run pytest` + `ruff check src tests` green
- status: pending

### Acceptance signals
- `--anchor X --radius 3 --filter turns` is sufficient for approval-turn review (proposal + landing + follow-up visible, in order)
- no behavior change for `--filter` without selection flags
- `No.Regression.Tests.Allowed` respected — the new tests are behavior tests at the pipeline boundary

### Risks / deviation triggers
- if pre-applied `turns` breaks a projection view that expects pruned tables (`replay` reads `model_runs`/`tool_invocations`), scope the pre-application to event-shape-only filters or to the `events` view — note the decision in `Impl.Log`
- if payload-identity for the no-selection path is impossible to keep exactly, preserve semantic equality and record the difference

## Impl.Log

- (empty — no execution yet)
