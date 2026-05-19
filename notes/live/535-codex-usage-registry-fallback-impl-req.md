# Codex Usage Registry Fallback — impl-req

## Impl.Abstract

- **scope:** extract provider account-usage registry fallback into a common helper and wire Codex account status through the same fallback behavior already used by Claude and Copilot
- **status:** ready for execution
- **source:** current discussion after inspecting `limits-tracking`, Codex recording, and Claude account-status fallback behavior
- **target project:** `agentos-py`

Observed state:

- `limits-tracking` setup already primes configured Codex targets from the last recorded usage registry record and renders them as `registry_latest`.
- Codex usage recording is working: successful `account_status()` app-server reads append `app_server` usage records under `~/.agentos/agent/usage-registry`.
- Codex does not fall back to the last recorded usage record on live provider refresh failure. `fallback_to_usage_registry` is currently discarded in `src/agentos/codex/account_status.py`.
- Claude and Copilot already implement the desired failure path: live usage fetch first, registry fallback second, `usage_status="ok"` if fallback succeeds, and the live failure preserved in `raw.usage_record.live_error`.

## Impl.Index

### Current.Codex.Gap

- `src/agentos/codex/account_status.py::_codex_account_status_impl` accepts `fallback_to_usage_registry` but immediately deletes it.
- Codex live usage reads flow through `_account_usage_app_server(agent)`.
- On `_account_usage_app_server` failure, Codex currently sets `usage_status="error"`, leaves `usage_record_metadata=None`, and does not attempt `latest_usage_record`.
- Codex already exposes `codex_usage_record_limits(payload)`, which can parse the usage registry payload shape used by both monitor setup and future fallback.
- Codex usage records use `CODEX_APP_SERVER_USAGE_SOURCE = "app_server"`.

### Claude.Path.To.Mirror

- `src/agentos/claude/account_status.py::_claude_account_status_impl` calls `_account_usage_statusline(...)`.
- If `usage_errors` exists, it calls `_account_usage_registry_fallback(...)` with:
  - `source=CLAUDE_STATUSLINE_USAGE_SOURCE`
  - `parser=_parse_claude_statusline_rate_limits`
  - `live_error=usage_errors[0]`
  - `fallback_to_usage_registry=fallback_to_usage_registry`
- The helper reads `latest_usage_record(...)`, parses the cached payload, and returns:
  - cached `limits`
  - empty `usage_errors`
  - cached payload as `usage_payload`
  - `usage_record_payload=None` so fallback data is not re-recorded
  - `registry_fallback_usage_record_metadata(...)` with the original live error
- The final `usage_status = "error" if usage_errors else "ok"` makes a successful fallback visible as usable status while preserving the live failure in raw metadata.

### Shared.Helper.Shape

Extract the duplicated fallback logic out of provider files into a provider-neutral helper. Prefer a new module:

- `src/agentos/agent/account_usage_fallback.py`

The helper should accept primitives rather than an `Agent` object:

- `provider: str`
- `account: str`
- `home: Path`
- `source: str`
- `parser: Callable[[Mapping[str, Any]], tuple[AccountLimit, ...]]`
- `live_error: AccountStatusError`
- `fallback_to_usage_registry: bool`

This keeps the helper independent of provider `Agent` types and avoids broadening `agent.account_status` model dependencies.

Return the same five-part tuple used by Claude and Copilot:

- `limits`
- `usage_errors`
- `usage_payload`
- `usage_record_payload`
- `usage_record_metadata`

### Common.Semantics

- If fallback is disabled, no record exists, no valid payload exists, or `home` is absent, return the original live error.
- If the registry payload parser fails, return the original live error plus an `invalid_registry_payload` error.
- If fallback succeeds, return cached limits, no usage errors, cached payload as `usage_payload`, `usage_record_payload=None`, and `registry_fallback_usage_record_metadata(...)`.
- Provider account-status implementations remain responsible for computing `usage_status`, `usage_summary`, `auth_summary`, and deciding whether to append a fresh usage record.

### Codex.Expected.Behavior

- On successful app-server read, Codex behavior remains unchanged:
  - `usage_status="ok"`
  - `auth_summary="Codex rate limits read"`
  - `raw.usage_record.status="fresh"`
  - append fresh `app_server` usage record when `record_usage=True`
- On app-server failure with a usable cached record:
  - `usage_status="ok"`
  - `auth_summary="Codex usage registry fallback"`
  - limits and `usage_summary` come from the cached payload
  - `raw.usage_record.status="registry_fallback"`
  - `raw.usage_record.live_error` contains the original app-server failure
  - no new usage record is appended
- On app-server failure without usable cached data:
  - behavior remains an error, with the original usage error still visible

### Monitor.Impact

- `limits-tracking` already renders `registry_fallback` metadata through the shared monitor row helpers.
- Once Codex uses fallback metadata, failed live refreshes should keep the last known Codex limits visible and add the existing `fetch error` row, matching Claude/Copilot monitor behavior.
- Do not change `limits-tracking` setup priming semantics; it should continue to load `registry_latest` from the registry before any refresh.

## Execution.Plan

### Slice 1 — Extract common registry fallback helper

- Add `src/agentos/agent/account_usage_fallback.py`.
- Move the provider-neutral body of Claude/Copilot `_account_usage_registry_fallback` into `account_usage_registry_fallback(...)`.
- Import `latest_usage_record`, `AccountLimit`, `AccountStatusError`, and `registry_fallback_usage_record_metadata`.
- Keep the `invalid_registry_payload` behavior and the five-part return tuple exactly compatible with current provider code.
- **changes:** `agentos-py/src/agentos/agent/account_usage_fallback.py`
- **validation:** targeted unit tests or import smoke verifies the helper can return fallback limits from a fake registry record and returns the original live error when disabled.

### Slice 2 — Refactor Claude and Copilot to use the helper

- Replace duplicated `_account_usage_registry_fallback` implementations in:
  - `src/agentos/claude/account_status.py`
  - `src/agentos/copilot/account_status.py`
- Call `account_usage_registry_fallback(...)` with explicit `provider=agent.provider`, `account=agent.account.account` or existing `_account_name(agent)`, `home=agent.home`, source, parser, live error, and fallback flag.
- Remove now-unused imports from provider files.
- Keep existing user-facing behavior unchanged.
- **validation:** existing Claude/Copilot account-status tests pass; no behavior drift in monitor rendering.

### Slice 3 — Wire Codex fallback through the shared helper

- Stop deleting `fallback_to_usage_registry` in `src/agentos/codex/account_status.py`.
- Adjust Codex usage-fetch code to track both `usage_payload` and `usage_record_metadata` like Claude/Copilot.
- If `_account_usage_app_server(agent)` returns `usage_errors`, call `account_usage_registry_fallback(...)` with:
  - `source=CODEX_APP_SERVER_USAGE_SOURCE`
  - `parser=codex_usage_record_limits`
  - `live_error=usage_errors[0]`
  - `fallback_to_usage_registry=fallback_to_usage_registry`
- Set `auth_summary` to:
  - `"Codex usage registry fallback"` when metadata status is `registry_fallback`
  - `"Codex rate limits read"` for fresh success
  - `None` for error
- Ensure Codex append behavior only records fresh provider reads, not fallback payloads.
- **changes:** `agentos-py/src/agentos/codex/account_status.py`
- **validation:** Codex account-status tests cover both fresh success recording and failed app-server fallback.

### Slice 4 — Add focused tests

- Add or extend account-status tests with fake `AGENTOS_HOME` usage registry records.
- Codex fallback test:
  - register/link or construct a Codex agent context consistent with existing tests
  - seed a valid `app_server` usage record for that provider/account/home
  - force `_account_usage_app_server` or app-server process path to fail
  - assert `usage_status == "ok"`
  - assert limits match cached record
  - assert `raw["usage_record"]["status"] == "registry_fallback"`
  - assert `raw["usage_record"]["live_error"]` contains the forced failure
  - assert no new usage record is appended during fallback
- Shared helper test:
  - parser success returns cached limits and empty errors
  - parser failure returns live error plus `invalid_registry_payload`
  - disabled fallback returns live error only
- **changes:** likely `agentos-py/tests/test_agent_account_registry_commands.py` or a new focused test file if cleaner
- **validation:** `uv run pytest <targeted tests> -q`

### Slice 5 — Validate monitor-facing behavior

- Run targeted tests for account registry/account status/monitor paths.
- Run a local smoke if safe:
  - `agentos agent accounts monitor --once --json`
- Inspect one Codex target in the JSON frame to ensure unchanged `registry_latest` setup behavior.
- If a failure-path test constructs monitor state directly, assert a Codex fallback account status produces the existing `fetch error` row.
- **validation commands:**
  - `uv run pytest tests/test_agent_account_registry_commands.py -q`
  - `uv run pytest tests/test_e2e_agent_accounts.py -q`
  - `uv run ruff check src/agentos/agent/account_usage_fallback.py src/agentos/codex/account_status.py src/agentos/claude/account_status.py src/agentos/copilot/account_status.py`

## Impl.Log

- 2026-05-19: Implemented Slice 1. Added `agentos-py/src/agentos/agent/account_usage_fallback.py` with the shared provider-neutral usage registry fallback helper. The helper preserves the five-part return shape, returns the original live error when fallback is disabled or unavailable, adds `invalid_registry_payload` on parser failure, and emits `registry_fallback` metadata on success.
- 2026-05-19: Implemented Slice 2. Refactored Claude and Copilot account-status code to call `account_usage_registry_fallback(...)` and removed their duplicated local fallback helpers and registry imports.
- 2026-05-19: Implemented Slice 3. Wired Codex account status to use `fallback_to_usage_registry`, parse cached `app_server` payloads with `codex_usage_record_limits`, report `Codex usage registry fallback`, preserve the live app-server error in raw metadata, and avoid recording fallback payloads.
- 2026-05-19: Implemented Slice 4. Added `agentos-py/tests/test_account_usage_fallback.py` covering shared helper success, parser failure, disabled fallback, Codex fresh app-server success recording, Codex failed app-server fallback with no extra usage record append, and Codex failed app-server behavior when no cached usage exists.
- 2026-05-19: Implemented Slice 5. Validation passed:
  - `uv run pytest tests/test_account_usage_fallback.py -q`
  - `uv run pytest tests/test_account_usage_fallback.py tests/test_e2e_agent_accounts.py -q`
  - `uv run pytest tests/test_e2e_agent_accounts.py -q`
  - `uv run ruff check src/agentos/agent/account_usage_fallback.py src/agentos/codex/account_status.py src/agentos/claude/account_status.py src/agentos/copilot/account_status.py`
  - `uv run ruff check src/agentos/agent/account_usage_fallback.py src/agentos/codex/account_status.py src/agentos/claude/account_status.py src/agentos/copilot/account_status.py tests/test_account_usage_fallback.py`
  - `uv run agentos agent accounts monitor --once --json`
  - `uv run agentos agent accounts monitor --once --json >/tmp/agentos-monitor-smoke.json && uv run python ...` reported `ok` and a Codex target with `registry_latest` / `ok`.
- 2026-05-19: Validation note: the planned command `uv run pytest tests/test_agent_account_registry_commands.py -q` could not be run because `tests/test_agent_account_registry_commands.py` does not exist in `agentos-py`; the new focused fallback tests and existing `tests/test_e2e_agent_accounts.py` cover the requested account registry/account status/monitor-facing behavior.
