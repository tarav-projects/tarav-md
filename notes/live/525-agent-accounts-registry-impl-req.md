# Agent Accounts Registry And Activity Logger - impl-req

## Impl-Req State

Implemented in `agentos-py`: the new Codex account register/link/status workflow, flat account registry, copy-based auth snapshots, and generalized activity logging are built and verified.

## User Intent

Build a new `agentos agent accounts` workflow for managing provider account auth files, starting with Codex.

The immediate user-facing commands should be:

```sh
agentos agent accounts register --provider codex --home ~/.codex-br --account br
agentos agent accounts link --provider codex --account br --home ~/.codex
agentos agent accounts status --provider codex --home ~/.codex
```

The system should treat Codex `auth.json` files as provider-owned local auth caches that can drift when Codex refreshes tokens. AgentOS should register those refreshed files into managed account storage, select the right stored snapshot for linking, and report enough status/debug information to explain what happened.

## Why This Exists

The current Codex linker assumes a single managed `auth.json` per account and links homes with a symlink. That makes drift handling weak and lets Codex refreshes mutate managed storage implicitly when the home auth path is linked.

The desired model is clearer:

- Codex owns `<home>/auth.json`.
- AgentOS owns stored account snapshots under `~/.agentos/accounts`.
- Linking copies a stored auth snapshot into the target home.
- Registering imports a home auth file into managed storage.
- Status compares the home auth, registered accounts, stored snapshots, and latest link events.

There is also a related logging gap. The existing `cmd-logger` surface is presented like a generic command logger, but its implementation is project-specific. Account linking is global AgentOS state, so the command/activity logger needs to support non-project commands and command-specific payloads.

## Current Situation

Relevant current code surfaces:

- `agentos-py/src/agentos/agent/commands.py` has `agentos agent accounts stats` and a separate legacy `agentos agent link`.
- `agentos-py/src/agentos/codex/linking.py` hardcodes `accounts/codex/<account>/auth.json` and links target homes by symlink.
- `agentos-py/src/agentos/agent/link_runtime.py` models the current legacy link request/result.
- `agentos-py/src/agentos/_core/project_command_log.py` records project command events only, with `project_id` and `project_root`.
- `agentos-py/src/agentos/utils/commands.py` exposes `agentos stdlib utils cmd-logger ...` for the project command log.
- `agentos-py/src/agentos/agent/accounts.py` already uses Tara tapes for account stats history; that is separate from command/activity logging.

The prior discussion established that Codex `auth.json` contains `tokens.account_id`, which should be the primary identity key for deciding whether two auth files belong to the same Codex account. Local aliases such as `br` are human/AgentOS labels, not identity.

## Requested Change

### 1. Generalize command/activity logging

Replace or evolve the project-only command log into a generic AgentOS activity log that can record any command or system event with command-specific payloads.

Preferred log path:

```text
~/.agentos/activity/YYYYMM.jsonl
```

Preferred event envelope:

```json
{
  "schema_version": 2,
  "timetag": "2026-05-13T00:00:00Z",
  "event_type": "agent.accounts.link",
  "command": "agent accounts link",
  "argv": ["agent", "accounts", "link", "--provider", "codex", "--account", "br", "--home", "/Users/pereiro/.codex"],
  "status": "ok",
  "payload": {}
}
```

Project command fields should move into `payload` instead of being required top-level fields. Account commands should store account/link-specific fields in `payload`.

Keep the command logger query/tail surface useful for both old project-style diagnostics and new global activity events.

### 2. Add flat global account registry

Store configured accounts in `~/.agentos/config.json` using a flat registry keyed by provider plus local alias.

Preferred shape:

```json
{
  "agent": {
    "account_registry": {
      "codex.br": {
        "provider": "codex",
        "account": "br",
        "account_id": "acc_...",
        "email": "person@example.com",
        "storage": "~/.agentos/accounts/codex/br"
      }
    }
  }
}
```

Fields may grow as needed, but identity matching must remain based on `tokens.account_id`, not email. Email is useful metadata for humans and diagnostics.

### 3. Add Codex auth registration

Implement:

```sh
agentos agent accounts register --provider codex --home <home> --account <alias>
```

Behavior:

- Read `<home>/auth.json`.
- Parse JSON and extract `tokens.account_id`.
- Extract human metadata when available, such as email from decoded JWT claims.
- Create or update the flat account registry entry.
- Store the auth file as a snapshot under `~/.agentos/accounts/codex/<alias>/snapshots/`.
- Keep every successful registration as its own immutable auth snapshot. Use freshness/registration time and SHA-256 in the filename; do not collapse repeated hashes.
- Maintain account-local manifest metadata for snapshots, selected/current snapshot, freshness, and identity.
- Emit a structured activity event.

### 4. Add copy-based Codex account linking

Implement:

```sh
agentos agent accounts link --provider codex --account <alias> --home <home>
```

Behavior:

- Resolve `codex.<alias>` from the flat registry.
- Before overwriting `<home>/auth.json`, inspect any existing home auth.
- If existing home auth has the same `tokens.account_id`, register it first so refreshed tokens are not lost.
- If existing home auth has a different `tokens.account_id`, stop with a clear error unless an explicit force path is added.
- Select the best stored snapshot for the account.
- Copy that snapshot to `<home>/auth.json`.
- Do not symlink.
- Emit a structured activity event on success and on failure.

Snapshot selection should prefer auth freshness metadata:

1. `last_refresh`
2. JWT `iat`
3. file mtime

Do not use "most recently added" as the primary selector when better freshness data exists.

### 5. Add Codex account/home status

Implement:

```sh
agentos agent accounts status --provider codex --home <home>
```

Behavior:

- Report whether `<home>/auth.json` exists.
- Report whether it is a regular file or symlink.
- Parse and report known auth identity fields.
- Report SHA-256 and freshness metadata.
- Report whether the current home auth is registered in managed storage.
- Report whether its `tokens.account_id` matches a configured account.
- Report latest relevant `agent.accounts.link` activity event for the home.
- Classify the home state.

Useful classifications:

- `missing`: no home auth file.
- `registered`: home auth matches a stored snapshot.
- `unregistered-known-account`: home auth belongs to a configured account but the snapshot is not stored.
- `unregistered-unknown-account`: home auth has an account id not present in the registry.
- `different-account`: home auth conflicts with the requested or last linked account.
- `broken`: auth file exists but cannot be parsed.
- `legacy-symlink`: auth path is a symlink from the older linker model.

## Constraints And Invariants

- Start with Codex only, but keep `--provider codex` explicit.
- Do not add broad provider abstractions until another provider needs them.
- `tokens.account_id` is the primary identity key.
- Local account aliases such as `br` are not identity keys.
- Email is metadata only; do not use it for identity matching.
- Linking copies auth files into target homes; it must not symlink.
- Register before overwrite when a target home already has a same-account auth file.
- Preserve and report drift instead of silently destroying it.
- Log both successful and failed link attempts when enough context exists.
- Avoid backward-compatibility aliases unless the user explicitly asks for them.
- Keep sensitive token values out of logs, command output, manifests, and config. Store full auth files only in the managed snapshot store and target home auth path.

## Out Of Scope

- Implementing non-Codex providers.
- Reworking `agentos agent accounts stats` semantics beyond namespace coexistence.
- Designing encryption or secret storage beyond current file storage behavior.
- Migrating all historical command logs.
- Removing old project command log files from disk.
- Building an interactive account picker.

## Acceptance Signals

- `agentos agent accounts --help` lists `stats`, `register`, `link`, and `status`.
- `agentos agent accounts register --provider codex --home ~/.codex-br --account br` creates or updates `agent.account_registry["codex.br"]`.
- The registry entry is flat and includes provider, alias/account, account id, storage path, and available human metadata such as email.
- Registration writes an immutable auth snapshot under `~/.agentos/accounts/codex/br/snapshots/`, even when the same auth content was registered before.
- Registration never writes raw token values into config, manifests, logs, or command output.
- `agentos agent accounts link --provider codex --account br --home ~/.codex` copies a selected snapshot to `~/.codex/auth.json`.
- Link does not create a symlink.
- Link registers an existing same-account home auth before replacing it.
- Link refuses a different-account home auth with a clear diagnostic.
- Link writes structured `agent.accounts.link` activity events for success and failure.
- `agentos agent accounts status --provider codex --home ~/.codex` reports parsed identity, registration match, snapshot match, freshness, hash, and latest link event.
- The generalized logger can tail/query account activity events.
- Existing project command logging tests are updated or preserved through the new generic event envelope.

## Implementation Shape

Vertical slice 1: introduce generic activity logging.

- Add a generic activity logger API that writes to `~/.agentos/activity/YYYYMM.jsonl`.
- Make event payloads command-specific.
- Keep or adapt `agentos stdlib utils cmd-logger path/tail/query` so it can inspect the new events.
- Check by emitting a small test event and querying it without a project.

Vertical slice 2: add Codex auth parsing and snapshot registration.

- Add a Codex auth parser that extracts `tokens.account_id`, `auth_mode`, `last_refresh`, SHA-256, and safe JWT-derived metadata such as email.
- Add account registry read/update helpers for `agent.account_registry`.
- Add snapshot storage that preserves every successful registration as a separate file.
- Implement `agent accounts register`.
- Check with a home containing `auth.json` and verify config plus snapshot output.

Vertical slice 3: implement copy-based link.

- Add `agent accounts link`.
- Resolve account registry entry and selected snapshot.
- Inspect current home auth before overwrite.
- Register same-account drift first.
- Refuse different-account auth.
- Copy selected snapshot into the target home.
- Emit activity events.
- Check that the target auth path is a regular file and matches the selected snapshot SHA.

Vertical slice 4: implement status diagnostics.

- Add `agent accounts status`.
- Combine home auth inspection, registry lookup, snapshot lookup, and latest activity lookup.
- Emit JSON by default if consistent with local command style, or add `--output json|markdown` if the implementation needs both machine and human output.
- Check each classifier case with focused fixtures.

Vertical slice 5: cleanup legacy surface.

- Decide whether the old `agentos agent link` command should be removed or converted to the new implementation.
- Follow `agentos-py/AGENTS.md`: do not keep backward-compatibility aliases unless explicitly requested.
- Refresh the installed CLI with `uv tool install --reinstall --editable .`.
- Run targeted tests, then the relevant full test suite if feasible.

## Relevant Files Or Surfaces

- `agentos-py/AGENTS.md`
- `agentos-py/src/agentos/agent/commands.py`
- `agentos-py/src/agentos/agent/accounts.py`
- `agentos-py/src/agentos/agent/link_runtime.py`
- `agentos-py/src/agentos/codex/linking.py`
- `agentos-py/src/agentos/codex/accounts.py`
- `agentos-py/src/agentos/_core/project.py`
- `agentos-py/src/agentos/_core/project_command_log.py`
- `agentos-py/src/agentos/utils/commands.py`
- `agentos-py/tests/test_project_command_log.py`
- `agentos-py/tests/test_utils_commands.py`
- Existing account/linking tests if present; add focused tests if absent.
- Runtime config: `~/.agentos/config.json`
- Runtime account storage: `~/.agentos/accounts/codex/<alias>/`
- Runtime activity log: `~/.agentos/activity/YYYYMM.jsonl`

## Open Questions

- Should `agentos agent link` be removed immediately once `agentos agent accounts link` exists, or should this impl-req leave that as a follow-up? The current compatibility policy prefers clean namespace changes and no aliases unless explicitly requested.
- Should `status` default to JSON, markdown, or support both from the beginning?
- Should `register` require `--account` always, or allow a generated alias only behind an explicit flag?
- Should failed `register` attempts be logged when the auth file cannot be parsed, or only after an account identity is known?

## Related Impl-Reqs

- None known.

## End Log

- 2026-05-13: Created from discussion converging on `agentos agent accounts register/link/status`, flat `agent.account_registry`, copy-based Codex auth linking, and a generalized global activity logger for command-specific events.
- 2026-05-13: Implemented in `agentos-py`: generalized activity logging to `~/.agentos/activity/YYYYMM.jsonl`, added `agentos agent accounts register/link/status` for Codex, stored flat `agent.account_registry` entries, preserved registered auth snapshots under `~/.agentos/accounts/codex/<alias>/snapshots/`, copied snapshots instead of symlinking on account link, added status diagnostics and latest link-event lookup, removed the legacy top-level `agentos agent link` command, refreshed the installed CLI, and verified with the full `agentos-py` test suite plus an isolated installed-CLI smoke test.
- 2026-05-13: Refined after user correction: registration must keep all `auth.json` snapshots, including repeated hashes, rather than deduping by SHA-256.
