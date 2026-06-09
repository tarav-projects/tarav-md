# Account Auth Reconcile

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

If one home works and another home is broken:

1. Identify the working home artifact.
2. Promote only the working artifact after real success or known evidence.
3. Materialize/sync that verified active artifact into stale homes.

Do not run a mutating passive reconcile expecting it to decide validity from observation alone. Passive reconcile collects and uses existing evidence; it does not prove credentials.

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
