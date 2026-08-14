# Chatlas Turn-Aware Radius — Impl.Req

## Impl.Abstract

- **Goal**: make `agentos chatlas views inline --anchor X --radius N --filter turns` show the N surrounding *turns* in chronological order — the anchor-resolution window a `--gr-review` reviewer actually needs (landing turn plus the preceding assistant proposal).
- **Problem today** (observed live during the 577 Gr.Req review, 2026-07-09):
  1. `around_filter` selects the `2r+1` events nearest by time-distance over ALL raw events — tool events consume the window, so `--radius 3` around a turn in a tool-heavy stretch returns only the landing turn; a reviewer needed `--radius 60` to see the preceding proposal.
  2. the selected events are returned in **distance order**, not chronological — the output reads shuffled.
  3. named filters (`turns`) apply after projection (`apply_chatlas_filters` is the last step), so message-pruning happens after the window is already spent.
- **Fix shape**: no new flags. (a) `around_filter` returns chronological output — plain bug fix. (b) when event-window selection flags AND `--filter` names are both supplied, apply the named filters to the model *before* projection/selection, so radius counts post-filter events. The composition `--anchor X --radius 3 --filter turns` then IS the turn-radius.
- **Out of scope**: a `--radius-turns` flag (interface growth without demand); changing distance-based candidate picking to sequence-based; query-layer (`query.py`) selection; changing `chatlas anchory register` neighborhood echo unless execution deliberately widens scope.
- **Repos**: `agentos-chatlas-py` for behavior and CLI help; `agentos-chatlas-md` for command-reference docs. Reinstall after CLI-visible changes: `uv tool install --reinstall --editable .` from `agentos-cli/`.
- **Source**: live failure in session `99144906-781e-43cc-9d27-b40f166e2acf` (2026-07-09, second 577 review sitting); index concepts `Chatlas.View`, `Chatlas.Filter` (chatlas 100), `Chatlas.Anchory` (+ appendix reading rule: "the anchor lands in an evidence neighborhood — read the landing turn and around it").
- **Status**: implemented; suite green; live acceptance verified

## Impl.Index

### Design.Decisions

- radius semantics become: "N nearest events each side *among the events your filters kept*" for event-window selection — one radius concept, composable, no new flag
- chronological output is unconditional (fix 1 applies even without named filters) — distance order was never useful to a reader
- pre-applying named filters happens ONLY when event-window selection flags are present alongside `--filter`; the no-selection path keeps today's post-projection order (shape-preserving filters on a projected view)
- event-window selection flags are `--contains`, `--role`, `--around`, and anchor-resolved `--around`; file/tool selectors (`--file-read`, `--file-write`, `--file-touched`, `--tool-contains`, `--tool-name`) are pre-prune selectors and must still run against the unfiltered model so `tool_invocations` are available
- when filters are pre-applied, do not re-apply them post-projection (they are idempotent, but double work and double deepcopy are pointless); the returned payload must be identical either way for the no-selection path
- precedent: file-touch selection already prunes `chat.events` before projection (`inline.py`, `_FILE_TOOLS` block) — this change makes named filters consistent with that
- the `--anchor` default radius stays `4`; with `--filter turns` that now means up to 9 messages — the intended review neighborhood

### Current.State *(inspect before coding)*

- pipeline: `src/agentos_chatlas/inline.py` `chatlas_views_inline` — anchor resolve → session select → model load → file-touch pre-prune → `project_chatlas_session_model_view(...)` → `apply_chatlas_filters(projected, filters)` (last)
- windowing: `src/agentos_chatlas/normalization/session_model/filters.py` `around_filter` (lines ~104-127): builds `(distance, index, event)` tuples, sorts by distance, truncates to `2r+1`, returns in that order
- selection composition: `build_event_selection` — contains → role → around, applied in `_views.py` `_project_session_model_view` over `chat.events`
- named filters: `CHATLAS_FILTERS` registry (`slim`/`messages`/`turns`) — model→model, shape-preserving, idempotent
- existing test coverage: `test_chatlas_views_inline_around_orders_nearest_first` currently locks the wrong nearest-first behavior; execution should replace that expectation, not merely add a parallel test
- CLI help currently says `--around` orders nearest-first; execution must update `commands.py` help text alongside docs
- `chatlas_anchory_register` echoes a `turns`-filtered neighborhood after projection; this impl-req is scoped to `views inline`, so treat register echo as unchanged unless execution widens scope and records the deviation

### Implementation.Notes

- do not reuse the current broad `has_selection` boolean for filter pre-application; it includes file/tool selectors that need the unfiltered model
- compute a narrower predicate after anchor resolution, roughly: `has_event_window_selection = any(value is not None for value in (contains, role, around))`
- after file/tool pre-pruning, if `has_event_window_selection and filters`, replace `session_model` with `apply_chatlas_filters(session_model, filters)` before `project_chatlas_session_model_view(...)` and return `projected` directly
- otherwise keep the current post-projection `apply_chatlas_filters(projected, filters)` path

## Execution.Plan

*(test-first; reuse the e2e fixture machinery in `tests/test_e2e_chatlas.py`; the existing rollout writer appends tool events after all messages, so the packed-between-messages RED needs either a helper extension or a one-off custom JSONL writer)*

### S1 — chronological window output
- what: `around_filter` sorts its selected events by timestamp (ties: original index) before returning
- RED: replace/update `test_chatlas_views_inline_around_orders_nearest_first` and/or add a unit test on `around_filter` — events at t0..t6, target t3, radius 2 → returns the 5 nearest **in chronological order**; today it returns them distance-ordered
- check: suite green
- status: done

### S2 — filters before selection in the inline pipeline
- what: in `chatlas_views_inline`, when event-window selection and `filters` are both truthy, apply `apply_chatlas_filters(session_model, filters)` to the loaded model before projection and skip the post-projection application; otherwise unchanged
- RED: pipeline test — session with messages `u1 a1 u2 a2` and 10 tool events packed between `a1` and `u2`; `chatlas_views_inline(anchor→u2, radius=1, filters=("turns",))` returns exactly `a1 u2 a2` (today: tool events eat the radius, `a1` missing); plus a no-selection regression assert: `filters=("turns",)` without selection returns byte-identical payload to today's path
- RED: regression that file/tool selectors still run against the unfiltered model — e.g. existing `--file-write ... --filter slim` and `--tool-contains ... --filter slim` behaviors remain green
- check: suite green
- status: done

### S3 — live acceptance + docs
- what: reinstall; rerun the live failing case: `agentos chatlas views inline --anchor 20260707-3 --radius 3 --filter turns` must show the assistant proposal turn preceding the "apply" landing turn, chronologically; update `agentos-chatlas-md/skills/tarav-chatlas-pkg/references/chatlas-commands.md` anchor-resolution section and `commands.py` help text (state the composed semantics: radius counts filter-surviving events for event-window selection, output chronological)
- check: live output correct; both index depots still lint clean; `uv run pytest` + `ruff check src tests` green
- status: done

### Acceptance signals
- `--anchor X --radius 3 --filter turns` is sufficient for approval-turn review (proposal + landing + follow-up visible, in order)
- no behavior change for `--filter` without selection flags
- `No.Regression.Tests.Allowed` respected — the new tests are behavior tests at the pipeline boundary

### Risks / deviation triggers
- if pre-applied `turns` breaks a projection view that expects pruned tables (`replay` reads `model_runs`/`tool_invocations`), scope the pre-application to event-shape-only filters or to the `events` view — note the decision in `Impl.Log`
- if pre-applied filters break file/tool selectors, the implementation is applying too broadly; narrow the condition to event-window selectors and keep file/tool pre-pruning before event projection
- if fixing `chatlas_anchory_register` echo is needed for live review, record the scope expansion; otherwise leave it untouched and note that `views inline` is the supported review command
- if payload-identity for the no-selection path is impossible to keep exactly, preserve semantic equality and record the difference

## Impl.Log

- 2026-07-09: executed all three slices; test-first throughout (S1 and S2 REDs failed for the planned reasons)
- 2026-07-09: deviation: beyond the one test the plan named, two more tests locked nearest-first ordering (`test_chatlas_views_inline_anchor_returns_neighborhood`, `test_chatlas_anchory_register_mints_and_echoes_neighborhood`); both updated to chronological expectations — same category, not regressions
- 2026-07-09: open-space decision: added `_write_codex_rollout_script` test helper for interleaved message/tool fixtures (the existing writer appends tools after messages, as the plan predicted)
- 2026-07-09: open-space decision: the pre-filter condition tests `(contains, role, around)` after anchor resolution — `--anchor` implies `--around`, so no separate anchor term needed
- 2026-07-09: the replay-view risk trigger did not fire — no test exercises selection+`--filter` on `replay`; pre-application stays unconditional on event-window selection
- 2026-07-09: register echo unchanged (in scope boundary respected); its test only needed the ordering-expectation update
- 2026-07-09: live acceptance: `--anchor 20260707-3 --radius 3 --filter turns` shows 7 chronological turns with the proposal (18:43:49) directly before the "apply" landing turn
- 2026-07-09: verification: `uv run pytest` 143 passed; `ruff check src tests` clean; both index depots lint 0/0 at 17 checks; CLI reinstalled
