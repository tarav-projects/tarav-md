# Auto-Prime Closed-Loop Reliability — impl-req

## Impl.Abstract

- **scope:** harden `auto-prime-zero-limits` from a best-effort one-shot helper into an observable, retryable, closed-loop workflow that can prove whether pings are effective
- **status:** implemented
- **source:** audit of `agentos-py` auto-prime workflow after registry evidence showed Codex accounts continuing in sliding near-zero/full-window ranges
- **target project:** `agentos-py`
- **primary files:** `src/agentos/agent/monitor/config.py`, `src/agentos/agent/monitor/loop.py`, `src/agentos/agent/monitor/workflows.py`, `src/agentos/agent/monitor/models.py`
- **test target:** `tests/test_agent_monitor_auto_prime.py` plus focused monitor-loop/config tests as needed

Observed evidence:

- Usage recording works: Codex records continue to land in `~/.agentos/agent/usage-registry/202605-usage.jsonl`.
- `auto-prime-zero-limits` is configured and visible in monitor setup JSON.
- A long-running monitor process was observed as:
  - `agentos agent accounts monitor`
  - started `Tue May 19 19:41:59 2026`
  - still running on `2026-05-22`
- Registry evidence on `2026-05-22` showed ongoing uninitialized/sliding shapes, especially `codex/tk`:
  - repeated `usedPercent = 1`
  - reset remaining around `300.0m`
  - reset moving forward with each sample
- No recent Codex session files were found for `jp/mm/tk/br` after `2026-05-19`, while usage registry records continued through `2026-05-22`.

Audit findings to address:

- `uninitialized` primes are remembered forever for the lifetime of a monitor process.
- The workflow treats a successful ping command as a successful prime, without checking whether usage state actually stabilized afterward.
- Already-running monitor processes do not reload config/code, so activation changes can be invisible while recording continues.
- Auto-prime attempt/skip/success/failure data is memory-only and not durable.
- Trigger timing uses monitor scan time instead of the usage sample timestamp when registry-backed status is used.
- Partial `triggers` or `target_limits` config can silently disable a configured target provider.
- Tests cover eligibility helpers but not enough workflow lifecycle behavior.

## Impl.Index

### Current.Workflow.Path

- Config is loaded by `src/agentos/agent/monitor/config.py::load_monitor_workflow_configs(...)`.
- Workflow instances are built by `src/agentos/agent/monitor/workflows.py::build_monitor_workflows(...)`.
- `AutoPrimeZeroLimitsWorkflow` consumes `limits-tracking` state from `MonitorState.data`.
- Eligibility is computed through `AutoPrimeZeroLimitsWorkflow._eligible_periods(...)` and `_eligible_limit_period(...)`.
- A prime attempt runs through `_prime_target(...)` and `_run_account_prime_ping(...)`.
- Successful pings are recorded in `target_state["primed_periods"]`.
- Auto-prime state is memory-only inside the active monitor process.

### Defect.OneShotUninitializedKey

- Uninitialized ranges intentionally use a stable key:
  - `provider/account/home/limit/uninitialized`
- This prevents a moving reset timestamp from creating a ping loop.
- Current behavior has no expiration or revalidation:
  - once the key is present in `primed_periods`, future eligible uninitialized periods are skipped
  - the skip can last for days if the monitor process is long-lived
- Required behavior:
  - uninitialized keys must have retry semantics
  - the workflow must avoid tight ping loops while still retrying after a bounded cooldown
  - recovery should clear or supersede the uninitialized memory so later regressions can be primed again

### Defect.NoEffectVerification

- Current success means only that provider command exited successfully and returned the expected numeric answer.
- It does not mean the provider usage range changed.
- Required behavior:
  - after a successful ping, mark the target/limit as pending verification
  - inspect subsequent `limits-tracking` observations
  - classify the prime as `effective`, `ineffective`, or still `pending_verification`
  - only suppress future retries indefinitely when evidence shows the range stabilized

### Defect.ProcessAndConfigDrift

- Monitor config is loaded once at startup.
- Long-running monitor processes can keep using stale workflow composition after local config changes.
- Required behavior:
  - expose enough process/config identity in monitor state to identify stale monitors
  - include monitor setup metadata such as config loaded time, workflow names, source config fingerprint, and code/build fingerprint if already available cheaply
  - provide a low-risk config reload or stale-config warning path
- Minimum acceptable implementation:
  - monitor JSON state must make it obvious whether the running process includes `auto-prime-zero-limits`, which targets/triggers it loaded, and when it loaded them
  - if config fingerprint changes, the monitor should surface a warning that restart/reload is required
- Preferred implementation:
  - reload monitor workflow config safely on config change, preserving compatible state when possible
  - if safe reload is too invasive, stop at warning and document the operational signal in JSON/text output

### Defect.NoDurableAudit

- Current auto-prime decisions are only in memory.
- The usage registry cannot tell whether a ping was attempted, skipped, failed, or considered effective.
- Required behavior:
  - add a durable auto-prime event registry or reuse an existing registry surface if one already fits
  - record attempt, success, failure, skip, verification-effective, and verification-ineffective events
  - include provider, account, home, limit id, period key, trigger reasons, tick, timestamp, and error detail when applicable
  - avoid storing provider raw payloads or sensitive command output
- Suggested path:
  - add `src/agentos/agent/monitor/auto_prime_registry.py` or equivalent module-local helper
  - write JSONL records under `~/.agentos/agent/monitor/auto-prime-events.jsonl` or a month-partitioned path under an existing Agentos registry convention

### Defect.TimestampSource

- Trigger evaluation currently uses monitor scan time.
- For registry-backed or fallback account status, the actual usage sample may have a `recorded_at` timestamp.
- Required behavior:
  - derive observation time from `account_status.raw.usage_record.recorded_at` when present and parseable
  - fall back to scan time only for fresh/no-metadata status
  - store both `observed_at` and `scan_at` in workflow state/event records
- This is necessary for correct `remaining_ratio`, `sliding_reset`, and period-churn decisions.

### Defect.PartialConfigSilence

- If `triggers` is configured for only one provider, providers missing from the trigger map are silently skipped.
- Similar risk exists for `target_limits`.
- Required behavior:
  - for every auto-prime target provider, resolve target limits and triggers explicitly
  - either apply provider defaults for omitted providers or fail config loading with a clear `CliError`
  - do not silently skip a configured target provider because a provider key is missing in `target_limits` or `triggers`
- Preferred behavior:
  - omitted top-level `triggers` or `target_limits` means defaults for all supported providers
  - present-but-partial maps are merged with defaults for configured target providers unless the implementation chooses stricter validation
  - whichever behavior is chosen must be tested and visible in config state

### Defect.TestCoverageGaps

- Current tests directly exercise `_eligible_periods(...)`.
- They do not sufficiently cover:
  - monitor loop lifecycle
  - `limits-tracking` to auto-prime handoff
  - uninitialized retry expiration
  - post-ping verification
  - stale config warning/reload
  - durable event records
  - sample timestamp versus scan timestamp
  - partial config behavior
- Required behavior:
  - add focused tests at workflow boundaries, not only private helper tests
  - mock provider pings; do not spend live provider calls in tests
  - keep tests deterministic with explicit timestamps

## Execution.Plan

### Slice 1 — Durable Auto-Prime Events

- Add a small auto-prime event writer/reader helper.
- Emit events for:
  - `eligible`
  - `skipped_already_primed`
  - `attempt_started`
  - `attempt_succeeded`
  - `attempt_failed`
- Include provider/account/home/limit/period key/trigger reasons/timestamp/tick.
- Avoid command output and raw provider usage payloads.
- **Paths:** new helper under `src/agentos/agent/monitor/`, `src/agentos/agent/monitor/workflows.py`.
- **Validation:** test writes events to a fake `AGENTOS_HOME`; assert schema and no sensitive fields.

### Slice 2 — Observation Timestamp Correctness

- Extract observation timestamp resolution from account status:
  - prefer `account_status.raw.usage_record.recorded_at`
  - fall back to scan time
- Store `observed_at` and `scan_at` in target observations and auto-prime events.
- Recompute `remaining_ratio` and sliding-reset comparisons against observed time.
- **Paths:** `src/agentos/agent/monitor/workflows.py`.
- **Validation:** test stale sample where scan time would fail near-full-window detection but recorded_at succeeds; test fallback to scan time.

### Slice 3 — Retryable Uninitialized Keys

- Replace permanent skip semantics for uninitialized keys with bounded retry state.
- Add state fields such as:
  - `last_attempt_tick`
  - `last_attempt_at`
  - `next_retry_after_monotonic`
  - `verification_status`
  - `attempt_count`
- Keep normal fixed-period keys unchanged.
- For uninitialized keys:
  - allow retry after configured cooldown if verification did not become effective
  - clear or rotate the key after the limit leaves uninitialized shape
  - avoid more than one ping per target per scan
- **Paths:** `src/agentos/agent/monitor/workflows.py`, config if a separate retry interval is needed.
- **Validation:** tests cover first ping, immediate skip, retry after cooldown, and clearing after stable non-uninitialized observation.

### Slice 4 — Post-Ping Effect Verification

- Add pending verification after successful ping command.
- On later observations for the same target/limit:
  - mark `effective` when reset stops sliding or usage state leaves uninitialized range
  - mark `ineffective` when uninitialized shape persists after enough fresh observations or after a verification timeout
  - record durable verification events
- Keep command success separate from prime effectiveness in state and events.
- **Paths:** `src/agentos/agent/monitor/workflows.py`, event helper.
- **Validation:** tests simulate post-ping observations that stabilize and remain sliding; assert event/state classification.

### Slice 5 — Config Completeness And Drift Visibility

- Resolve provider defaults for auto-prime target providers or fail partial maps clearly.
- Add loaded config metadata to monitor state:
  - loaded timestamp
  - workflow names
  - target summary
  - target limits
  - triggers
  - config fingerprint/source fingerprint
- Add stale-config detection:
  - if config fingerprint changes while monitor runs, emit warning/state field
  - if safe reload is implemented, record reload event and preserve compatible state
- **Paths:** `src/agentos/agent/monitor/config.py`, `src/agentos/agent/monitor/loop.py`, `src/agentos/agent/monitor/workflows.py`.
- **Validation:** tests cover partial trigger/limit config and config fingerprint warning/reload behavior.

### Slice 6 — Boundary Tests And CLI Smoke

- Add monitor-loop-level tests with synthetic `limits-tracking` state and monkeypatched ping runner.
- Cover:
  - `limits-tracking` state handoff into auto-prime
  - one target eligible among many
  - durable event records for attempts/skips/verification
  - stale config warning signal
  - no live provider command execution
- Run focused commands:
  - `uv run pytest tests/test_agent_monitor_auto_prime.py -q`
  - any new monitor-loop/config test file
  - `uv run ruff check src/agentos/agent/monitor/config.py src/agentos/agent/monitor/loop.py src/agentos/agent/monitor/models.py src/agentos/agent/monitor/workflows.py`
- Refresh installed CLI after code changes:
  - `uv tool install --reinstall --editable .`
- Run a smoke that does not spend provider calls:
  - `agentos agent accounts monitor --once --json`
  - parse JSON to verify config metadata and auto-prime block/state

## Impl.Log

### 2026-05-22 — implemented

- Added durable auto-prime JSONL events through `src/agentos/agent/monitor/auto_prime_registry.py`.
- Wired auto-prime events for `eligible`, `skipped_already_primed`, `attempt_started`, `attempt_succeeded`, `attempt_failed`, `verification_effective`, and `verification_ineffective`.
- Changed auto-prime observation time resolution to prefer `account_status.raw.usage_record.recorded_at`, while retaining scan time as `scan_at`.
- Replaced process-lifetime permanent uninitialized suppression with retryable state:
  - successful ping marks uninitialized periods as `pending_verification`
  - retries are allowed after `retry_cooldown_sec` when verification remains ineffective
  - stable observations emit `verification_effective` and clear the uninitialized memory so future regressions can retry
- Added post-ping verification that classifies later observations as effective or ineffective separately from command success.
- Changed partial `target_limits` and `triggers` config maps to merge with defaults, preventing silent provider disablement.
- Added monitor setup/config metadata:
  - loaded timestamp
  - workflow names
  - config fingerprint
  - auto-prime target summary, target limits, triggers, and config fingerprint
  - stale-config warning state when the live fingerprint changes
- Added focused tests in `tests/test_agent_monitor_auto_prime.py` for:
  - durable events and sanitized schema
  - recorded-at versus scan-at detection
  - uninitialized retry after cooldown
  - stable-observation clearing
  - persistent-uninitialized ineffective classification
  - no live provider calls in tests
  - partial config map default merging
  - monitor config drift signal

Validation:

- `uv run pytest tests/test_agent_monitor_auto_prime.py -q` -> `9 passed`
- `uv run pytest -q` -> `9 passed`
- `uv run ruff check src/agentos/agent/monitor/config.py src/agentos/agent/monitor/loop.py src/agentos/agent/monitor/models.py src/agentos/agent/monitor/workflows.py src/agentos/agent/monitor/auto_prime_registry.py tests/test_agent_monitor_auto_prime.py` -> passed
- `uv tool install --reinstall --editable .` from `agentos-py` failed because package `agentos` exposes no executable and removed the previous tool wrapper.
- Recovered the CLI with `uv tool install --reinstall --editable ../agentos-cli`; this installed the `agentos` executable and the editable `agentos-py` dependency.
- `agentos agent accounts monitor --once --json` smoke parsed successfully and showed:
  - `monitor_setup.workflow_names = ["limits-tracking", "auto-prime-zero-limits"]`
  - `monitor_setup.config_stale = false`
  - config fingerprint present
  - auto-prime loaded timestamp, target summary, target limits, and triggers present
