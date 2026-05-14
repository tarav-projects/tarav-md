# Agent Account Model - impl-req

## Impl.Abstract

Status: implemented.

Scope: extend `agentos agent accounts` from a Codex-only auth-file registry into a provider-neutral account model, while keeping Codex file-backed account behavior intact.

Primary implementation target: `agentos-py`.

Source context:

- Existing Codex account registry implementation: `agentos-py/src/agentos/codex/account_registry.py`
- Existing command surface: `agentos-py/src/agentos/agent/commands.py`
- Existing registry tests: `agentos-py/tests/test_agent_account_registry_commands.py`
- Deprecated account stats reference only: `agentos-py/_DEPRECATED/agent-accounts-stats/`

This impl-req prepares the model needed for a future `agentos agent accounts monitor` command. Do not implement monitor, monitor config, history migration, or TUI in this pass.

## Impl.Index

### Provider.Neutral.Account

Intent: every user-facing account reference should use the same shape:

```json
{"provider": "codex", "account": "br"}
{"provider": "claude-code", "account": "main"}
```

Do not introduce an `instance`-based account path for Claude or other non-Codex providers. The asymmetry belongs inside provider implementation details, not in user-facing config or CLI.

Evidence:

- User rejected `{"provider":"claude-code","instance":"claude-main"}` as asymmetric.
- User wants an account model for Claude even though Claude does not expose a portable `auth.json`.

### Account.Manifest.Common.Fields

All account providers should have account manifests at:

```text
~/.agentos/accounts/<provider>/accounts/<account>/manifest.json
```

Common manifest fields should include:

```json
{
  "schema_version": 1,
  "provider": "claude-code",
  "account": "main",
  "label": "Claude main",
  "email": "person@example.com",
  "auth_kind": "ambient-browser-login",
  "capabilities": {
    "register": true,
    "link": false,
    "status": true,
    "monitor": true
  },
  "created_at": "...",
  "updated_at": "..."
}
```

Exact optional fields can remain provider-owned, but common fields should be stable enough for `status` and future `monitor` to read without provider-specific hacks.

### Codex.FileBacked.Account

Codex remains the existing file-backed implementation:

```text
~/.agentos/accounts/codex/
  registry.jsonl
  files/<sha256>.auth.json
  accounts/<account>/
    manifest.json
    auth.json -> ../../files/<sha256>.auth.json
```

The implementation may normalize the Codex manifest to include the common account fields, but must not break:

- `register --provider codex --account <name> --auth-file <path>`
- `link --provider codex --account <name> --home <home>`
- `status --provider codex --home <home>`
- existing flat file registry invariants

### Claude.AmbientLogin.Account

Claude account registration is metadata-only.

Command shape:

```sh
agentos agent accounts register \
  --provider claude-code \
  --account main \
  --home ~/.claude \
  --email person@example.com \
  --label "Claude main"
```

Rules:

- Do not copy credentials.
- Do not create fake auth files.
- Store a manifest only.
- `auth_kind` should represent the reality of the provider login model, for example `ambient-browser-login`.
- The registered `home` is the provider context the monitor will later use to run Claude status/usage checks.
- Require enough metadata to make the account meaningful. If email cannot be discovered, require `--email`.

### Link.Capability.Gated

`link` remains supported for Codex.

For Claude, `link` should fail clearly because there is no file-backed auth pointer to copy:

```text
agent accounts link is not supported for provider claude-code
```

This is not a legacy placeholder. It is capability enforcement for a real registered account provider.

Claude accounts must still appear in `status`.

### Status.ProviderAware

`agentos agent accounts status` should show all registered provider accounts, including metadata-only accounts.

Expected Claude fields in human and JSON status:

- provider
- account
- label
- email
- auth kind
- home, if registered
- capabilities
- link support shown as unsupported

Existing Codex home status remains home-specific:

```sh
agentos agent accounts status --provider codex --home ~/.codex
```

If a provider has registered accounts but does not support home inspection, status should still present the registered account manifests.

## Execution.Plan

### Slice 1 - Provider-neutral registry helpers

Add a small shared account-registry layer for provider account manifests.

Observable result:

- Code can read/write `~/.agentos/accounts/<provider>/accounts/<account>/manifest.json`.
- Codex can either use this helper directly or continue provider-local writes while producing compatible common fields.

Validation:

- Unit tests write and read a metadata-only manifest.
- Existing Codex registry tests remain green.

### Slice 2 - Extend `register` for Claude metadata accounts

Update the CLI so `--provider claude-code` is accepted by `agentos agent accounts register`.

Observable result:

```sh
agentos agent accounts register --provider claude-code --account main --home ~/.claude --email person@example.com
```

creates:

```text
~/.agentos/accounts/claude-code/accounts/main/manifest.json
```

Validation:

- Test metadata-only registration.
- Test registration does not create `auth.json`, `files/`, or credential copies for Claude.
- Test missing required metadata errors clearly.

### Slice 3 - Capability-gate `link`

Make provider account capabilities explicit enough for command handlers.

Observable result:

- Codex link behavior is unchanged.
- Claude link exits with a clear unsupported-provider message.

Validation:

- Existing Codex link tests remain green.
- New Claude link unsupported test.

### Slice 4 - Provider-aware account status

Update status overview to include provider-neutral account manifests.

Observable result:

```sh
agentos agent accounts status
```

shows Codex and Claude registered accounts.

Validation:

- Test Claude registered account appears in human status.
- Test Claude registered account appears in `--json`.
- Test Codex home status remains scoped to the requested home.

### Slice 5 - CLI and docs cleanup

Update help text and minimal docs so the account model is discoverable.

Observable result:

- `agentos agent accounts register --help` shows provider-appropriate options without implying every provider uses `--auth-file`.
- README or local notes do not imply accounts are Codex-only.

Validation:

- CLI help smoke test.
- Focused ruff and pytest for touched modules.

## Constraints

- No monitor implementation in this pass.
- No resurrecting `agentos agent accounts stats`.
- No `instance`-based user-facing account config for Claude.
- No fake Claude auth files.
- No copying or deleting Claude credentials.
- No regression to Codex file-backed registry behavior.
- No backward-compatibility aliases unless explicitly requested.

## Impl.Log

Implemented 2026-05-14.

- Added provider-neutral account manifest helpers in `agentos-py/src/agentos/agent/account_registry.py`.
- Normalized Codex manifests with common account fields while preserving file-backed `registry.jsonl`, `files/<sha>.auth.json`, and `accounts/<account>/auth.json` behavior.
- Added metadata-only Claude account registration in `agentos-py/src/agentos/claude/account_registry.py`.
- Extended `agentos agent accounts register/status/link` to accept `claude-code`, require Claude `--home` and `--email`, and report Claude link as unsupported.
- Updated general `agentos agent accounts status` to read provider-neutral manifests and show registered Codex and Claude accounts.
- Updated account registry command tests and README account examples.
- Verification:
  - `uv run pytest tests/test_agent_account_registry_commands.py tests/test_agent_commands.py -q` passed: 52 tests.
  - `uv run pytest -q` passed: 266 tests.
  - Focused `uv run ruff check` for touched modules passed.
  - Isolated CLI smoke confirmed Claude creates only `accounts/claude-code/accounts/main/manifest.json` and status shows `link=unsupported`.
  - Full `uv run ruff check .` still fails on unrelated pre-existing lint in deprecated Chatlas and other modules.
  - Refreshed installed CLI with `uv tool install --reinstall --editable .`.
