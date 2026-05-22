# Monitor Account Status Lane — impl-req

## Impl.Abstract

- **scope:** change monitor account header rows so the account line uses a full-width status lane for fetch status plus auto-prime status only
- **status:** implemented
- **source:** user requested replacing the narrow `fresh` slot in rows such as `⬢ codex/tk: | fresh` with a special account-level lane; user explicitly rejected adding usage percentages or broad account metadata
- **target project:** `agentos-py`
- **primary files:** `src/agentos/agent/monitor/models.py`, `src/agentos/agent/monitor/workflows.py`
- **test target:** existing monitor rendering tests if present, plus focused tests around `MonitorAccountRow` and `AutoPrimeZeroLimitsWorkflow` account note state
- **current context:** `agentos-py` has uncommitted cleanup work after checkpoint `63e84c9 chore: checkpoint before codebase-general-cleanup`; executor must inspect current worktree and build on it, not revert it

Accepted target shape:

```text
⬢ codex/tk:  fresh · prime pending
⬢ codex/tk:  fresh · primed
⬢ codex/tk:  fallback 12m ago · prime retry in 8m
⬢ codex/tk:  error · prime failed
```

Do not add usage percentages, limit summaries, reset times, identity metadata, or other account details to this header lane. The lane is intentionally scoped to:

- fetch/usage-record freshness status
- auto-prime status

## Impl.Index

### Current.Rendering.Path

- `src/agentos/agent/monitor/workflows.py::_target_rows(...)` creates `MonitorAccountRow(label=..., **_usage_refresh_columns(...))`.
- `src/agentos/agent/monitor/workflows.py::_usage_refresh_columns(...)` returns `{"value": ..., "suffix": ...}`.
- `src/agentos/agent/monitor/models.py::MonitorAccountRow` currently inherits `_MonitorColumnRowMixin`.
- `_MonitorColumnRowMixin` renders account rows through fixed columns:
  - label width
  - value width
  - suffix width
- That fixed-column shape makes the current account header behave like:
  - `⬢ codex/tk:            | fresh`
  - or `provider/account: | recorded_at | age`

### Desired.AccountStatusLane

- The account row should remain visually anchored by account identity on the left.
- Everything after the account identity should be a full-width status lane, not the generic narrow value/suffix columns.
- The lane should be composed from ordered short parts separated by ` · `.
- Initial parts:
  - fetch status part from the usage record state
  - auto-prime status part when available
- Long text may animate/truncate using the existing row animation behavior. Do not over-engineer wrapping.

### FetchStatusParts

- Preserve the current fetch information but adapt it into one compact status part.
- Required examples:
  - fresh usage record -> `fresh`
  - registry fallback/latest with age -> `fallback 12m ago` or equivalent existing freshness language
  - no usage metadata -> omit fetch part rather than inventing a misleading value
  - target error -> `error`
- Do not include limit usage percentages or summaries here.
- Existing detailed rows below the account header remain responsible for usage/time, reset, and fetch error detail.

### AutoPrimeStatusParts

- Auto-prime status should be derived from `auto-prime-zero-limits` state, not from usage percentages directly in the renderer.
- Use current state fields produced by `AutoPrimeZeroLimitsWorkflow`:
  - `primed_periods`
  - `last_error`
  - `retry_after_monotonic`
  - per-period `verification_status`
  - per-period `next_retry_after_monotonic`
  - attempt ticks/counts if useful for state classification, but not as display noise
- Required display semantics:
  - pending verification -> `prime pending`
  - verified effective -> `primed`
  - ineffective -> `prime ineffective`
  - blocked by retry cooldown -> `prime retry in <duration>`
  - last ping command failed -> `prime failed`
- If multiple limits have auto-prime state, choose the most severe/highest-action status rather than listing all of them.
- Suggested priority:
  - `prime failed`
  - `prime ineffective`
  - `prime retry in <duration>`
  - `prime pending`
  - `primed`

### WorkflowBoundary

- The limits-tracking renderer currently only receives the limits-tracking target state.
- Auto-prime state lives separately under `MonitorState.data["auto-prime-zero-limits"]["targets"]`.
- Required boundary:
  - do not make auto-prime mutate limits-tracking target state just for rendering
  - instead pass account status notes into the row-building/render path from the monitor state or a helper that joins target-keyed workflow state
- A clean approach:
  - update `LimitsTrackingWorkflow._write_frame_block(...)` to compute account-row status parts using both the limits-tracking target state and the matching auto-prime target state
  - pass the composed status lane into `_target_rows(...)`
  - keep auto-prime status classification in a small helper near monitor workflows, not in `MonitorAccountRow`

### RowModelChange

- `MonitorAccountRow` should support full-lane account status text.
- Preferred model:
  - add `status: str | None` or `status_parts: tuple[str, ...]`
  - render account rows as `row_indent + label + "  " + animated status lane`
  - keep summary data explicit so JSON output contains the lane parts/text
- Do not break non-account rows.
- Keep existing animation behavior for long status lane text.
- Avoid preserving legacy account `value/suffix` behavior unless it is still used by existing code after the change.

### TestingExpectations

- Tests should verify text output, not just internal helpers.
- Required coverage:
  - account row with only fetch status renders as full-lane `label  fresh`, not `label | fresh`
  - account row with fetch plus auto-prime status renders `fresh · prime pending`
  - auto-prime pending/effective/ineffective/failed/retry states map to the expected note
  - detailed usage/time rows still render below account row and do not leak into account status lane
  - JSON summary exposes account status text or parts
- Tests must not invoke live provider commands.

## Execution.Plan

### Slice 1 — Account Row Full-Lane Rendering

- Change `MonitorAccountRow` in `src/agentos/agent/monitor/models.py` to render account rows with a full-width status lane.
- Keep label anchoring and animation behavior.
- Update `summary()` to include the status lane.
- Add/adjust focused tests for account-row rendering and JSON summary.
- **Acceptance signal:** `MonitorAccountRow(label="  ⬢ codex/tk:", status="fresh").render_frame(...)` produces a full-lane row without `| fresh`.

### Slice 2 — Fetch Status Part Extraction

- Replace `_usage_refresh_columns(...)` with a status-part helper or adapt it so `_target_rows(...)` receives a fetch status part.
- Preserve existing fresh/fallback/latest/error semantics, but express them as compact lane parts.
- Keep detailed usage and fetch-error rows unchanged.
- **Acceptance signal:** monitor output still shows fetch freshness, now as the account lane first part.

### Slice 3 — Auto-Prime Status Classification

- Add a helper that maps matching auto-prime target state to one optional status part.
- Use priority ordering:
  - failed
  - ineffective
  - retry cooldown
  - pending
  - primed
- Compute retry remaining from monotonic timestamps when possible; if not available, prefer `prime retry` over a misleading duration.
- **Acceptance signal:** synthetic auto-prime states produce `prime pending`, `primed`, `prime ineffective`, `prime retry in <duration>`, and `prime failed`.

### Slice 4 — Join Limits Tracking With Auto-Prime State

- Update the workflow rendering path so limits-tracking account rows can include auto-prime notes from `MonitorState.data`.
- Join by the same target key used by both workflows.
- Do not mutate limits-tracking target state with auto-prime display data.
- **Acceptance signal:** synthetic monitor state with both workflow states renders an account row like `⬢ codex/tk:  fresh · prime pending`.

### Slice 5 — Boundary Verification And Smoke

- Run focused tests for monitor models/workflows.
- Run:
  - `uv run pytest tests/test_agent_monitor_auto_prime.py -q`
  - any new monitor render/model test file
  - `uv run ruff check src/agentos/agent/monitor/models.py src/agentos/agent/monitor/workflows.py tests/test_agent_monitor_auto_prime.py`
- If CLI/runtime code changed, refresh the installed CLI correctly. Note: `agentos` executable is provided by `agentos-cli`; installing `agentos-py` directly may remove the wrapper.
- Run `agentos agent accounts monitor --once --json` and inspect frame rows to confirm account rows carry only fetch plus prime info.

## Impl.Log

### 2026-05-22 — implemented

- Implemented `MonitorAccountRow.status` as a full account-lane renderer in `agentos-py/src/agentos/agent/monitor/models.py`; account rows no longer use the generic `value/suffix` column shape.
- Replaced the limits-tracking account-header fetch columns with ordered status parts in `agentos-py/src/agentos/agent/monitor/workflows.py`.
- Added auto-prime account-note classification from `MonitorState.data["auto-prime-zero-limits"]["targets"]`, joined by the existing target key without mutating limits-tracking state.
- Kept the lane scoped to fetch freshness/error plus one auto-prime note. Usage percentages, reset information, and fetch error details remain in their existing detailed rows.
- Added focused tests in `agentos-py/tests/test_agent_monitor_auto_prime.py` covering full-lane rendering, JSON summary status, fetch-plus-prime joined rendering, usage rows below the account row, and auto-prime failed/ineffective/retry/pending/effective priority.
- Verification:
  - `uv run pytest tests/test_agent_monitor_auto_prime.py -q` -> 12 passed
  - `uv run pytest -q` -> 12 passed
  - `uv run ruff check src/agentos/agent/monitor/models.py src/agentos/agent/monitor/workflows.py tests/test_agent_monitor_auto_prime.py` -> passed
  - `uv tool install --reinstall --editable ../agentos-cli` -> refreshed installed `agentos`
  - `agentos agent accounts monitor --once --json` -> returned status ok; limits-tracking account rows expose `status` lane values such as `latest 1m ago`
  - `agentos agent accounts monitor --once` -> account rows render as lane text, e.g. `⬢ codex/tk:  latest 1m ago`, with usage rows below
