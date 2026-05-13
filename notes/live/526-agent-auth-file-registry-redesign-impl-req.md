# Agent Auth File Registry Redesign - impl-req

## Impl-Req State

Implemented in `agentos-py`: Codex account registration now uses an auth-file input and stores auth files in the flat provider registry with hash-addressed files, registry JSONL, account manifests, and active auth pointers.

## User Intent

Redesign the AgentOS account auth registration and linking system so registered provider auth files are stored in a flat, searchable, hash-addressed registry.

For Codex, the target storage shape is:

```text
~/.agentos/accounts/codex/
  registry.jsonl
  files/
    8d6df568d9f814782739cbe5a799af6df4e24922a22b45d3570d7d1e9fd781da.auth.json
    a13c....auth.json
  accounts/
    br/
      manifest.json
      auth.json -> ../../files/8d6df568d9f8....auth.json
```

The user explicitly likes the internal symlink/current-pointer shape above. Do not replace it with a per-account snapshots directory unless the design is reopened.

The registration command should point to an auth file, not a provider home:

```sh
agentos agent accounts register --provider codex --account br --auth-file <path>
```

Provider-specific register hooks should parse provider auth files and require any missing metadata via provider-specific CLI flags. If required metadata cannot be parsed or supplied, fail clearly.

## Why This Exists

The first implemented model under `525-agent-accounts-registry-impl-req.md` used per-account snapshot storage and a manifest list. After review, that is still too complex and not searchable enough.

The desired model is simpler:

- `files/` is the immutable auth-file store, addressed by hash.
- `registry.jsonl` is the append-only searchable index of all registered auth files.
- `accounts/<account>/manifest.json` stores the current account pointer and current normalized metadata.
- `accounts/<account>/auth.json` is the current materialized pointer for that account, pointing to the active file in `files/`.

This makes it easy to answer:

- Is this given `auth.json` already registered?
- Which provider/account owns this auth file hash?
- Does this auth file belong to a known account identity but have a new hash?
- What is the active auth file for account `codex.br`?

## Current Situation

The previous implementation introduced:

- `agentos agent accounts register --provider codex --home <home> --account <alias>`
- `agentos agent accounts link --provider codex --account <alias> --home <home>`
- `agentos agent accounts status --provider codex --home <home>`
- global activity logging under `~/.agentos/activity/YYYYMM.jsonl`
- account storage under `~/.agentos/accounts/codex/<alias>/snapshots/`
- per-account `manifest.json` with snapshot metadata

That implementation was useful as a first vertical slice, but this impl-req intentionally replaces the storage/registration model. Do not preserve the old snapshots model as a compatibility layer.

Relevant current code surfaces:

- `agentos-py/src/agentos/codex/account_registry.py`
- `agentos-py/src/agentos/agent/commands.py`
- `agentos-py/src/agentos/_core/project_command_log.py`
- `agentos-py/src/agentos/utils/commands.py`
- `agentos-py/tests/test_agent_account_registry_commands.py`
- `agentos-md/notes/live/525-agent-accounts-registry-impl-req.md`

## Requested Change

### 1. Change register input from home to auth file

Replace the register command shape:

```sh
agentos agent accounts register --provider codex --home <home> --account <alias>
```

with:

```sh
agentos agent accounts register --provider codex --account <alias> --auth-file <path>
```

For Codex, the source file may have any filename, but it is registered as a Codex auth file and stored under the provider registry as a `.auth.json` hash-addressed file.

### 2. Use provider-specific register hooks

Each provider owns its registration parser and required metadata rules.

For Codex:

- Parse the provided `--auth-file` as Codex `auth.json`.
- Extract `tokens.account_id`.
- Extract safe metadata such as `auth_mode`, `last_refresh`, JWT `iat`, and email when present.
- Surface provider-specific CLI options for required metadata that may be missing from the file.
- If required metadata is missing and cannot be supplied, error. Do not guess.

### 3. Replace per-account snapshots with provider-level hash files

Use this provider storage shape:

```text
~/.agentos/accounts/<provider>/
  registry.jsonl
  files/
    <sha256>.auth.json
  accounts/
    <account>/
      manifest.json
      auth.json -> ../../files/<sha256>.auth.json
```

For Codex:

```text
~/.agentos/accounts/codex/
  registry.jsonl
  files/
    <sha256>.auth.json
  accounts/
    br/
      manifest.json
      auth.json -> ../../files/<sha256>.auth.json
```

### 4. Define registry.jsonl as the searchable index

`registry.jsonl` is append-only. Each line is a normalized registration entry for one auth file hash and account association.

Example entry:

```json
{"registered_at":"2026-05-13T00:00:00Z","provider":"codex","account":"br","account_id":"acc_...","sha256":"8d6df...","file":"files/8d6df....auth.json","source_auth_file":"/some/source/file.json","auth_mode":"chatgpt","email":"person@example.com","last_refresh":"2026-05-12T17:00:07Z","jwt_iat":1776000000}
```

Rules:

- Do not include raw tokens.
- Do include enough normalized metadata to search and diagnose.
- If the same account/hash entry already exists, registration is a noop.
- If the same hash exists for the provider, do not copy the file again.
- If the hash exists but not for this account association, append the association entry after validating identity rules.

### 5. Define account manifest.json as the current pointer

Each account has:

```text
~/.agentos/accounts/<provider>/accounts/<account>/manifest.json
```

Example:

```json
{
  "schema_version": 1,
  "provider": "codex",
  "account": "br",
  "account_id": "acc_...",
  "active_sha256": "8d6df...",
  "active_file": "../../files/8d6df....auth.json",
  "email": "person@example.com",
  "updated_at": "2026-05-13T00:00:00Z"
}
```

The account `auth.json` is the current pointer:

```text
~/.agentos/accounts/codex/accounts/br/auth.json -> ../../files/<sha256>.auth.json
```

### 6. Keep and protect all auth files

The system must never delete a current `auth.json` while registering or linking.

Important invariants:

- Never delete a user's current home auth file.
- Never destructively overwrite a provider account current auth pointer without first ensuring the previous target remains in `files/`.
- Registered auth file contents are immutable once stored under `files/<sha>.auth.json`.
- If replacing a symlink/pointer, replace the pointer atomically. Do not delete the target file.
- If encountering an existing regular file where a pointer is expected, copy/rename it into `files/` appropriately before replacing it, or fail without touching it.
- If a link operation sees an existing target-home `auth.json`, register it through the same provider hook before replacing it when it belongs to the same account.
- If the existing target-home `auth.json` belongs to a different account or cannot be parsed, fail and leave it untouched.

### 7. Link should use the active account pointer

`link` remains home-oriented:

```sh
agentos agent accounts link --provider codex --account br --home <home>
```

Behavior:

- Resolve the account manifest.
- Read `active_file`.
- Before touching `<home>/auth.json`, inspect the current home auth.
- If current home auth belongs to the same account, register it by auth file path first.
- If current home auth belongs to a different account, fail.
- If current home auth is broken/unparseable, fail.
- Copy active auth file to `<home>/auth.json`.
- The home file should remain a regular file unless a future design explicitly changes linking semantics.

## Constraints And Invariants

- No legacy slop. Do not preserve the old per-account `snapshots/` model as an active compatibility layer.
- No backward-compatibility aliases unless explicitly requested by the user.
- Do not keep `--home` for registration. Registration is file-oriented through `--auth-file`.
- Do not invent migration logic for old local data unless explicitly requested. This impl-req defines the new model.
- Do not delete current auth files. Copy, rename, or atomically replace pointers only after the previous file remains recoverable.
- Do not log raw token values or write them into config, manifests, registry entries, command output, or activity events.
- Provider hooks decide provider-specific required metadata and parsing rules.
- `tokens.account_id` remains the Codex identity key.
- Local aliases such as `br` are not identity keys.
- `registry.jsonl` is append-only.
- `files/<sha>.auth.json` entries are immutable.
- `accounts/<account>/manifest.json` is the current account state.
- `accounts/<account>/auth.json` is the current account auth pointer to the active file.

## Out Of Scope

- Supporting non-Codex providers beyond preserving the provider-hook boundary.
- Migrating existing `snapshots/` data from the previous implementation.
- Adding encryption or secret-store integration.
- Designing an interactive account picker.
- Keeping old command aliases.
- Redesigning activity logging beyond any needed account event payload updates.

## Acceptance Signals

- `agentos agent accounts register --provider codex --account br --auth-file <path>` works.
- `agentos agent accounts register --provider codex --home <home> --account br` fails at parser level or is removed.
- Registering a new Codex auth creates:
  - `~/.agentos/accounts/codex/files/<sha>.auth.json`
  - `~/.agentos/accounts/codex/registry.jsonl`
  - `~/.agentos/accounts/codex/accounts/br/manifest.json`
  - `~/.agentos/accounts/codex/accounts/br/auth.json` pointing to the active file.
- Re-registering the same account/hash is a noop and does not append a duplicate registry entry.
- Registering a new hash for the same account appends a registry entry and updates the account manifest/current pointer.
- Registering an auth file whose `account_id` conflicts with an existing account alias fails without touching current account files.
- Given any auth file, status/search logic can compute SHA and determine whether it is registered by reading `registry.jsonl`.
- Link registers same-account target-home auth before replacing it.
- Link fails and leaves the current target-home `auth.json` untouched when that file is different-account or broken.
- No raw token values appear in config, manifest, registry, activity log, or command output.
- Tests cover idempotent noop, new-hash registration, account-id mismatch, same-account link preservation, broken-home-auth link refusal, and registry lookup by SHA.
- Full `agentos-py` tests pass.
- Installed CLI is refreshed with `uv tool install --reinstall --editable .`.

## Implementation Shape

Vertical slice 1: switch register command to auth-file input.

- Update argparse for `agent accounts register`.
- Remove `--home` from registration.
- Add `--auth-file`.
- Adjust Codex registration entry point to accept a file path.
- Check parser behavior and a simple Codex registration fixture.

Vertical slice 2: add provider-level file registry layout.

- Store auth bytes under `~/.agentos/accounts/codex/files/<sha>.auth.json`.
- Append normalized entries to `~/.agentos/accounts/codex/registry.jsonl`.
- Avoid duplicate registry lines for the same provider/account/hash.
- Check by registering the same auth twice and asserting noop.

Vertical slice 3: add current account manifest and pointer.

- Write `accounts/<account>/manifest.json`.
- Point `accounts/<account>/auth.json` at the active hash file.
- Replace active pointer atomically.
- Check by registering a new hash and verifying the manifest and pointer update.

Vertical slice 4: preserve current/home auth during link.

- Before link overwrite, inspect `<home>/auth.json`.
- Register same-account existing home auth by auth file path.
- Fail on broken/different-account auth without changing it.
- Copy active auth to the home only after preservation checks pass.
- Check with fixtures that compare file bytes before and after failure.

Vertical slice 5: status/search diagnostics.

- Make status use `registry.jsonl` as the searchable source for registered hashes.
- Report whether home auth hash is registered, known-account-new-hash, unknown, broken, or matching active.
- Include latest activity link event when available.

Vertical slice 6: remove old active storage model.

- Remove active references to `snapshots/`.
- Remove tests that assert the old snapshots model.
- Do not keep compatibility shims.
- Run focused tests, full tests, refresh installed CLI, and update this impl-req end log.

## Relevant Files Or Surfaces

- `agentos-py/AGENTS.md`
- `agentos-py/src/agentos/agent/commands.py`
- `agentos-py/src/agentos/codex/account_registry.py`
- `agentos-py/src/agentos/_core/project_command_log.py`
- `agentos-py/src/agentos/utils/commands.py`
- `agentos-py/tests/test_agent_account_registry_commands.py`
- `agentos-py/tests/test_project_command_log.py`
- `agentos-py/tests/test_utils_commands.py`
- Prior implementation request: `agentos-md/notes/live/525-agent-accounts-registry-impl-req.md`
- New provider registry root: `~/.agentos/accounts/codex/`
- Activity log: `~/.agentos/activity/YYYYMM.jsonl`

## Open Questions

- What Codex metadata, if any, should be required via CLI when it cannot be parsed from `auth.json`? The implementation should surface provider-specific options and error if a required value is missing.
- Should `accounts/<account>/auth.json` be an internal symlink only, or should there be a mode to materialize it as a copy? The accepted direction for now is the symlink pointer shown by the user.

## Related Impl-Reqs

- Supersedes the storage/registration model in `notes/live/525-agent-accounts-registry-impl-req.md`.

## End Log

- 2026-05-13: Created after redesign discussion. The user accepted the flat provider registry shape with `registry.jsonl`, `files/<sha>.auth.json`, and `accounts/<account>/manifest.json` plus an internal `auth.json` pointer. The request explicitly rejects legacy compatibility slop and emphasizes that current auth files must not be deleted.
- 2026-05-13: Implemented in `agentos-py`. Registration now uses `--auth-file` plus Codex-specific `--email` metadata override; the Codex registry writes `~/.agentos/accounts/codex/registry.jsonl`, immutable `files/<sha>.auth.json`, `accounts/<account>/manifest.json`, and an internal `accounts/<account>/auth.json` symlink pointer. Link preserves same-account home auth by registering it before copy, refuses broken or different-account home auth without replacing it, and status reads registry JSONL for hash/account classification. Added tests for flat layout, old `--home` parser rejection, manual email metadata, idempotent registration, new-hash active updates, account-id conflicts, regular pointer preservation, link preservation/refusal, and known-account-new-hash status.
