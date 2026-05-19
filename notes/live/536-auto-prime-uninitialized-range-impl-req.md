# Auto-Prime Uninitialized Range Detection — impl-req

## Impl.Abstract

- **scope:** improve `auto-prime-zero-limits` so it can detect uninitialized/sliding provider limit ranges, not only exact zero-usage ranges, and activate the workflow in the local account monitor config
- **status:** ready for execution
- **source:** current discussion after inspecting `limits-tracking`, `auto-prime-zero-limits`, and `codex/jp` usage registry behavior
- **target project:** `agentos-py`
- **local activation target:** `~/.agentos/config.json`

Observed state:

- The monitor workflow users call "auto-ping" is implemented as `auto-prime-zero-limits`.
- The current local `~/.agentos/config.json` has `limits-tracking` entries but no `auto-prime-zero-limits` entry, so auto-prime is not active.
- `agentos agent accounts monitor --max-ticks 2 --interval-sec 0.1 --json` showed only `limits-tracking` in `workflow_run_counts`.
- `codex/jp` usage registry shows a recent uninitialized range pattern:
  - before `2026-05-19T22:39:56Z`, burst reset was fixed at `2026-05-19T23:54:32Z` and remaining time counted down
  - from `2026-05-19T22:39:56Z` onward, burst used stayed near zero while reset moved to approximately `recorded_at + 300m`
  - this produces a sliding full-window shape: `used_percent` around `1`, remaining time around `300m`
- Current eligibility in `src/agentos/agent/monitor/workflows.py::_eligible_limit_period(...)` only primes when `used_percent == 0`, so it misses Codex ranges that report `1%` while still behaving uninitialized.

## Impl.Index

### Current.AutoPrime.Path

- Config is loaded in `src/agentos/agent/monitor/config.py`.
- Workflow name constant is `AUTO_PRIME_ZERO_LIMITS_WORKFLOW = "auto-prime-zero-limits"`.
- Default target limits are:
  - `codex: ("burst",)`
  - `claude-code: ("burst",)`
- Supported target limits are:
  - `codex: ("burst", "weekly")`
  - `claude-code: ("burst", "weekly")`
- Runtime logic is in `src/agentos/agent/monitor/workflows.py::AutoPrimeZeroLimitsWorkflow`.
- `_scan_and_prime(...)` reads current target state from `limits-tracking`; auto-prime depends on `limits-tracking` state being available.
- `_eligible_periods(...)` evaluates each tracked limit, skips previously primed period keys, and calls `_prime_target(...)`.
- `_prime_target(...)` runs `_run_account_prime_ping(...)`, records success/failure, and stores primed periods in memory for the running monitor session.

### Current.Trigger.Gap

- `_eligible_limit_period(...)` currently has one trigger: `used_percent == 0`.
- That is useful but too narrow for Codex app-server behavior.
- Codex can present an apparently empty/full fresh range with `used_percent == 1`, not `0`.
- Codex can also report `resets_at`/`period_ends_at` as a moving value near `recorded_at + windowDurationMins`, which means the range has not been stabilized by an actual model call.
- The generated period key currently includes period start/end. For sliding uninitialized ranges, that can churn on every refresh and would cause repeated primes unless the uninitialized key is stabilized.

### Accepted.Trigger.Set

Keep all triggers and fire if any configured trigger matches.

- `zero_usage`
  - Existing behavior.
  - Match when `used_percent == 0`.
- `near_zero_full_window`
  - Match when usage is near zero and remaining time is nearly a full provider window.
  - Initial threshold: `used_percent <= 1` and `remaining_ratio >= 0.98`.
  - Requires a known duration from `period_duration_mins` or `windowDurationMins`.
- `sliding_reset`
  - Match when repeated refreshes show reset/end time moving with the recording time instead of counting down.
  - For each target/limit, store the last observed end time and observation time in workflow state.
  - If both observation delta and end-time delta are positive and approximately equal, the reset is sliding.
  - Initial tolerance: absolute difference between deltas no more than `max(60s, 0.20 * observation_delta)`.
- `period_key_churn`
  - Match when a near-zero/full-window range produces a new period key across successive observations for the same target/limit.
  - This is a secondary symptom of the sliding reset behavior.
  - Use it as an additional trigger reason, not a separate ping loop.

### Trigger.Configuration.Shape

Add explicit trigger configuration for `auto-prime-zero-limits`.

- Field name: `triggers`
- Shape:
  - object keyed by provider
  - each provider maps to a non-empty list of trigger names
- Defaults:
  - `codex: ["zero_usage", "near_zero_full_window", "sliding_reset", "period_key_churn"]`
  - `claude-code: ["zero_usage"]`
- Supported trigger names:
  - `zero_usage`
  - `near_zero_full_window`
  - `sliding_reset`
  - `period_key_churn`
- Invalid providers or trigger names should fail config loading with clear `CliError` messages.

This keeps current Claude behavior conservative while making Codex robust by default.

### Stable.Prime.Keys

- Fixed/normal periods should keep the existing period-key shape:
  - provider/account/home/limit/period start/period end
- Uninitialized trigger matches should use a stable logical key:
  - provider/account/home/limit/uninitialized
- Trigger matches should record reason metadata in `primed_periods`:
  - `trigger_reasons`
  - `limit_id`
  - attempt/success ticks
- The stable uninitialized key prevents auto-prime from pinging on every monitor scan while Codex keeps returning a moving reset time.

### Activation.Requirement

Activation must be included in execution:

```txt
Add an auto-prime-zero-limits workflow entry to agent.accounts.monitor in
  ~/.agentos/config.json.
```

Recommended local activation entry:

```json
{
  "workflow": "auto-prime-zero-limits",
  "interval_sec": 60,
  "retry_cooldown_sec": 600,
  "target_limits": {
    "codex": ["burst"]
  },
  "triggers": {
    "codex": [
      "zero_usage",
      "near_zero_full_window",
      "sliding_reset",
      "period_key_churn"
    ]
  },
  "targets": [
    { "provider": "codex", "account": "jp" },
    { "provider": "codex", "account": "mm" },
    { "provider": "codex", "account": "tk" },
    { "provider": "codex", "account": "br" }
  ]
}
```

The implementer may include `claude-code` targets later only if they can preserve conservative default behavior and avoid unnecessary pings.

### Monitor.Output

- Keep the existing `auto-prime` rows.
- Add trigger reason details in JSON state, not necessarily in the compact text UI.
- When a scan pings a target, `last_scan.pinged` should increment as today.
- When a scan skips because an uninitialized logical key was already primed, state should make that inspectable through `primed_periods`.

## Execution.Plan

### Slice 1 — Add Trigger Config Model

- Extend monitor config parsing in `src/agentos/agent/monitor/config.py`.
- Add supported/default trigger constants for `auto-prime-zero-limits`.
- Add `triggers` to `MonitorWorkflowConfig` or an equivalent typed field.
- Validate provider keys and trigger names with clear errors.
- Preserve existing behavior for configs that omit `triggers`.
- **changes:** `src/agentos/agent/monitor/config.py`, `src/agentos/agent/monitor/models.py`
- **validation:** focused config tests cover defaults, explicit Codex triggers, invalid trigger name, and invalid provider.

### Slice 2 — Track Limit Observations

- Extend `AutoPrimeZeroLimitsWorkflow` state with per-target/per-limit observation history.
- Store last observed:
  - period key
  - period end/reset timestamp
  - observation timestamp
  - used percent
  - remaining/window ratio if available
- Keep state memory-only for the running monitor loop.
- Avoid using usage registry history for this slice; current `limits-tracking` state is enough.
- **changes:** `src/agentos/agent/monitor/workflows.py`
- **validation:** unit tests can call the workflow helper path with synthetic target state across repeated scans.

### Slice 3 — Implement Trigger Reasons

- Replace `_eligible_limit_period(...)` single-condition behavior with trigger evaluation.
- Return an eligible period only when any configured trigger matches.
- Attach `trigger_reasons`.
- Implement:
  - `zero_usage`
  - `near_zero_full_window`
  - `sliding_reset`
  - `period_key_churn`
- Use stable uninitialized prime keys for uninitialized triggers.
- Preserve normal fixed-period keys for plain `zero_usage` matches that are not otherwise uninitialized.
- **changes:** `src/agentos/agent/monitor/workflows.py`
- **validation:** tests cover:
  - `used_percent == 0` still primes
  - Codex `used_percent == 1`, remaining ~= full window primes via `near_zero_full_window`
  - two observations with reset sliding by observation delta prime via `sliding_reset`
  - near-zero changing period key primes via `period_key_churn`
  - repeated uninitialized scans do not ping repeatedly after stable uninitialized key is primed

### Slice 4 — Activate Local Auto-Prime

- Edit `~/.agentos/config.json`.
- Add an `auto-prime-zero-limits` workflow entry to `agent.accounts.monitor`.
- Include Codex accounts `jp`, `mm`, `tk`, `br`.
- Use `target_limits.codex = ["burst"]`.
- Use Codex triggers:
  - `zero_usage`
  - `near_zero_full_window`
  - `sliding_reset`
  - `period_key_churn`
- Preserve existing `limits-tracking` entries.
- **changes:** `~/.agentos/config.json`
- **validation:** `agentos agent accounts monitor --max-ticks 2 --interval-sec 0.1 --json` includes `auto-prime-zero-limits` in blocks or `workflow_run_counts`.

### Slice 5 — End-To-End Monitor Validation

- Run focused tests for monitor config/workflow behavior.
- Run local smoke:
  - `agentos agent accounts monitor --once --json`
  - `agentos agent accounts monitor --max-ticks 2 --interval-sec 0.1 --json`
- Inspect JSON state for:
  - `limits-tracking` still present
  - `auto-prime-zero-limits` present after activation
  - Codex targets included
  - trigger config visible in raw workflow state/config
- If current live Codex state is still near-zero/full-window, verify one auto-prime attempt is recorded or skipped because its stable uninitialized key is already primed.
- **validation commands:**
  - `uv run pytest tests/test_e2e_agent_accounts.py -q`
  - `uv run pytest <new monitor auto-prime test file> -q`
  - `uv run ruff check src/agentos/agent/monitor/config.py src/agentos/agent/monitor/models.py src/agentos/agent/monitor/workflows.py`

## Impl.Log

(empty — not yet started)
