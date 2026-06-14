---
name: agentos-agent-account-management
description: "Operational router for Agentos provider-account management problems: registering fresh auth artifacts, linking provider homes, diagnosing account monitor failures, checking usage fallback, resolving active-vs-verified registry drift, and troubleshooting Codex auth.json, Claude Code ambient browser auth, and Copilot CLI account state."
---

# Agentos Agent Account Management

Use this skill when the user asks to inspect, register, repair, reconcile, link, or diagnose Agentos-managed provider accounts or provider homes.

## Core Rule

Treat account credentials as artifacts with separate states:

- **registered** means Agentos archived the credential payload.
- **active** means Agentos intends to materialize that artifact into homes.
- **verified** means a live provider operation succeeded with that artifact.
- **freshest** means newest observed credential metadata, not necessarily valid.

Do not assume these states agree. Verify the specific state relevant to the user request.

## First Checks

Start read-only unless the user explicitly asks to mutate:

```bash
agentos agent accounts status --json
agentos agent accounts status --provider codex --json
agentos agent accounts reconcile --provider codex --check --json
agentos agent accounts reconcile --provider claude-code --check --json
```

For a specific provider home:

```bash
agentos agent accounts status --provider codex --home "$HOME/.codex-jp" --json
agentos agent accounts status --provider claude-code --home "$HOME/.agentos/agent/homes/claude-code/browser-jp" --json
```

## Route By Symptom

- Fresh or duplicate Codex `auth.json` files, backup auth files, or ChatGPT token claims: read `references/codex-auth-json.md`.
- Claude Code browser login, macOS Keychain, path-scoped ambient auth, or "logged in but failing": read `references/claude-ambient-auth.md`.
- `agentos agent accounts monitor` shows fallback, stale usage, `fetch error`, or provider usage failures: read `references/account-monitor.md`.
- Active artifact is not newest, reconcile reverts homes, homes are `matching-active` but live calls fail, or registry state looks contradictory: read `references/registry-consistency.md`.

## Mutating Discipline

When changing state:

1. Identify the provider, account alias, provider account id, home path, auth artifact id, and live validation result.
2. Register fresh auth artifacts before linking homes.
3. Verify artifacts with a live provider operation before relying on passive reconcile.
4. Link only from the verified active artifact.
5. Re-run status and one live provider check after mutation.

Do not use passive reconcile as proof of credential validity. Passive reconcile archives observations and syncs from existing verification evidence; it does not prove a credential works.
