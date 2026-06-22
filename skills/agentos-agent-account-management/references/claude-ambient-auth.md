# Claude Ambient Auth Reconcile

Operational reference for Agentos account credential artifact reconciliation.

Use this when a provider account home reports logged in, asks for login unexpectedly, rotates credentials, or reconcile behavior looks wrong.

## Mental Model

Provider credential storage is an implementation detail. Agentos should expose the same account semantics for providers even when their credential shapes differ.

Codex uses `auth.json` files. Claude Code browser login uses home identity plus secure storage.

Claude Code browser login auth is path-scoped.

On macOS, Claude stores OAuth secure storage in Keychain entries whose service name includes a hash of the Claude home path. Copying files between homes is not enough; the target home needs matching secure storage under its own path-derived Keychain service.

Agentos handles provider auth by treating credentials as an artifact system:

- **observed** means Agentos read identity plus secure storage from a home.
- **archived** means Agentos stored that credential payload as an immutable artifact.
- **verified** means a real provider interaction succeeded with that artifact.
- **active** means the latest verified successful artifact for an account.

Do not treat `claude auth status` alone as proof that credentials work. A home can report logged in and still fail real API use.

## Keychain Is The Credential Source Of Truth (macOS)

Home files (`.claude.json`, `.credentials.json`) are NOT where the live OAuth token lives. On macOS the real secret is in the **login Keychain**, and that is what you must inspect — checking home files alone will mislead you.

Service name per home (see `claude_keychain_service_names` in `claude/account_registry.py`):

```text
Claude Code-credentials-<sha256(resolved_home_path)[:8]>      # path-scoped
Claude Code-credentials                                       # legacy fallback
```

Derive the service and read the actual token:

```bash
# service for a home
python3 -c 'import hashlib,os,sys; p=os.path.realpath(sys.argv[1]); print("Claude Code-credentials-"+hashlib.sha256(p.encode()).hexdigest()[:8])' "$HOME/.agentos/agent/homes/claude-code/<account>"

# read the secret and inspect expiry + refresh token
security find-generic-password -s "Claude Code-credentials-<hash>" -w \
  | python3 -c 'import sys,json,datetime; o=json.load(sys.stdin).get("claudeAiOauth",{}); print("expiresAt", datetime.datetime.fromtimestamp(o["expiresAt"]/1000, tz=datetime.timezone.utc).isoformat()); print("refreshToken_len", len(o.get("refreshToken","")))'
```

The two diagnostic fields: `expiresAt` (is the access token still valid?) and `refreshToken` length (can the home self-heal?). List all Claude entries with `security dump-keychain | grep -i 'svce.*Claude Code-credentials'`.

## Symptom: Logged In But Dead (Refresh Token Rotation)

A home can show `claude auth status` → `loggedIn: true` while its Keychain holds an **expired `accessToken` AND an empty `refreshToken`**. That home is dead — it cannot refresh and every live call (including the monitor's statusline harvest) will fail or hang to timeout, even though status looks fine.

Root cause when multiple homes share one account: Claude OAuth refresh tokens are **single-use / rotating**. Two live homes off the same account each start with the same refresh token; whichever refreshes first gets a new pair and the server **invalidates the other's** refresh token. The loser's next refresh fails and Claude clears its refresh token → permanent expiry. The winning home stays healthy and self-refreshing.

Diagnose by comparing the two homes' Keychain entries (not their files):

- working home: `accessToken` valid OR a present `refreshToken` (can self-heal)
- dead home: expired `accessToken` + **empty `refreshToken`**

Note the registered agentos artifact may still contain a refresh token (it is the immutable snapshot from capture time); the *home* is what lost it. So the active artifact can itself be an expired snapshot — passive reconcile cannot fix this; you need a fresh capture from a working home (see Common Repair Pattern).

## Important Paths

Managed Claude homes:

```text
~/.agentos/agent/homes/claude-code/<account>
```

Managed Codex homes:

```text
~/.agentos/agent/homes/codex/<account>
```

Claude account registry:

```text
~/.agentos/accounts/claude-code/accounts.json
```

Claude artifact index:

```text
~/.agentos/accounts/claude-code/artifacts.jsonl
```

Claude artifact payloads:

```text
~/.agentos/accounts/claude-code/artifacts/<artifact-id>.ambient-auth.json
```

Verification ledger:

```text
~/.agentos/accounts/<provider>/verifications.jsonl
```

Artifact payload files can contain credentials. The JSONL indexes and verification ledger must not contain tokens or raw secure storage.

## Core Semantics

Passive reconcile:

```bash
agentos agent accounts reconcile --provider claude-code
agentos agent accounts reconcile --provider codex
```

It should:

- scan known configured and managed Claude homes
- read Claude home identity and secure storage
- archive any new observed artifact
- use existing verification evidence to choose active artifacts
- sync stale homes only from verified active artifacts
- avoid live Claude provider calls

Explicit ping reconcile:

```bash
agentos agent accounts reconcile --provider claude-code --ping
agentos agent accounts reconcile --provider codex --ping
```

It should:

- do the passive reconcile work
- run live ping checks for candidate homes
- write verification evidence for successful pings
- promote successful artifacts to active
- sync homes from the newly verified active artifact

Check mode:

```bash
agentos agent accounts reconcile --provider claude-code --check --json
agentos agent accounts reconcile --provider claude-code --check --ping --json
agentos agent accounts reconcile --provider codex --check --json
agentos agent accounts reconcile --provider codex --check --ping --json
```

`--check --ping` must not run live provider calls. It reports `would_ping`.

## Success Evidence Sources

The verification ledger can be refreshed by successful provider operations:

- `agent.run`
- `agent.ping`
- `account.status`
- `monitor.auto_prime`
- `accounts.reconcile.ping`

Registry fallback usage does not verify credentials.

## First Checks

Inspect passive reconcile:

```bash
agentos agent accounts reconcile --provider claude-code --check --json
agentos agent accounts reconcile --provider codex --check --json
```

Inspect explicit ping plan without live calls:

```bash
agentos agent accounts reconcile --provider claude-code --check --ping --json
agentos agent accounts reconcile --provider codex --check --ping --json
```

Inspect one home through Claude directly:

```bash
CLAUDE_CONFIG_DIR="$HOME/.agentos/agent/homes/claude-code/<account>" claude auth status
```

Inspect one Codex home directly:

```bash
CODEX_HOME="$HOME/.agentos/agent/homes/codex/<account>" codex auth status
```

Then test a real provider call only when live calls are acceptable.

## Common Repair Pattern

If one home works and another home is broken (e.g. the managed home died via rotation while a personal home like `~/.claude-<x>` stays healthy):

First confirm agentos does not already hold the working credential. The Keychain (SSOT) is often *ahead of* agentos — a home self-refreshed and agentos never captured the new token. Check by matching the working home's current Keychain `accessToken`/`refreshToken` against the registered artifact payloads in `accounts/claude-code/artifacts/*.ambient-auth.json`. If there is no match, the live credential is unregistered and a plain reconcile (which only syncs from existing artifacts) will not help — and could even sync a stale artifact back over the working home.

Capture from the working home, verify, and sync only the broken home:

```bash
# observes the working home's Keychain -> archives a fresh artifact ->
# live-ping verifies it -> promotes it active -> syncs the managed home
agentos agent accounts reconcile --provider claude-code --account <account> --ping --json
```

Scoping with `--account` keeps the sync targeted: it updates the broken managed home and leaves the healthy personal home untouched. Confirm the action trail shows `verified_artifact` for the working home and `synced_home` for the broken one.

**Timing matters (rotation safety):** run this while the working home's `accessToken` still has time left (check `expiresAt`). A ping on a still-valid token will not trigger a refresh, so it cannot rotate the token out from under the working home. If the working token is about to expire, the ping may refresh+rotate and a subsequent sync could clobber the good home.

Then verify the repair on the **Keychain**, not just the registry:

```bash
# the managed home's Keychain should now show a valid expiresAt + non-empty refreshToken
# and a live check should pass:
agentos agent accounts status --provider claude-code --json   # active_artifact + last_verified
# plus a live account.status on the managed home (check=ok, usage=ok, identity=verified)
```

Do not run a mutating passive reconcile expecting it to decide validity from observation alone. Passive reconcile collects and uses existing evidence; it does not prove credentials.

**Standing hazard:** as long as two homes run live off one account, they will keep racing over refresh-token rotation and re-breaking the loser. Either avoid concurrent live use, or treat the personal home as the single source and re-capture into the managed home on demand.

## Code Entry Points

Provider-neutral ledger:

```text
agentos-py/src/agentos/agent/account_registry.py
```

Claude artifact and verified promotion helpers:

```text
agentos-py/src/agentos/claude/account_registry.py
```

Codex artifact and verified promotion helpers:

```text
agentos-py/src/agentos/codex/account_registry.py
```

Claude reconcile core:

```text
agentos-py/src/agentos/claude/account_reconcile.py
```

Codex reconcile core:

```text
agentos-py/src/agentos/codex/account_reconcile.py
```

CLI wrapper:

```text
agentos-py/src/agentos/agent/commands.py
```

Success hooks:

```text
agentos-py/src/agentos/claude/agent.py
agentos-py/src/agentos/claude/account_status.py
agentos-py/src/agentos/codex/agent.py
agentos-py/src/agentos/codex/account_status.py
agentos-py/src/agentos/agent/monitor/workflows.py
```

## Tests To Start With

```bash
cd /Users/pereiro/projects/agentos-project/agentos-py
uv run pytest tests/test_agent_account_registry.py tests/test_claude_account_registry.py tests/test_claude_account_reconcile.py -q
uv run pytest tests/test_codex_account_reconcile.py -q
uv run pytest tests/test_claude_account_status.py tests/test_agent_run_account_preflight.py tests/test_agent_monitor_auto_prime.py -q
```

## Known Bootstrap Note

Artifacts and active pointers that existed before the verification ledger may show:

```text
active_verified: false
```

That does not necessarily mean the credential is broken. It means the new ledger has not yet seen a fresh successful Claude operation for that artifact.
