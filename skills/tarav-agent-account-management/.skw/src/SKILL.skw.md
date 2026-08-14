> $kw: ^agentos-root-reachability --reachable-from @<tarav-pkg>/SKILL.md

---
name: tarav-agent-account-management
description: "Operational incident runbook for Agentos provider-account problems: inspecting account state, capturing auth artifacts, activating active credentials, materializing provider homes, diagnosing account monitor fallback, resolving aligned-vs-drifted homes, and troubleshooting Codex auth.json, Claude Code Keychain/browser auth, or Copilot CLI account state. USE WHEN the user asks to inspect, capture, activate, materialize, repair, or diagnose Agentos-managed provider accounts or provider homes."
---

# Agentos Agent Account Management

Use this skill when the user asks to inspect, capture, activate, materialize, repair, or diagnose Agentos-managed provider accounts or provider homes.

This is a `Batchy.Skill`. Load `tarav-batchy-skills` for the full convention.

- `-h` / `--help` prints this skill's help into the chat instead of running; it takes no arguments — describe the account problem in natural language and the skill routes it.

## Core Rule

Treat provider credentials as state spread across separate layers. Most account incidents are layer confusion.

- **Home.State** is what the provider runtime will actually use.
- **captured / registered** means Agentos archived the credential payload as immutable `Auth.Data`.
- **active** means Agentos designated one captured artifact in `registry/active.json`.
- **aligned** means a home's current `Auth.Data` hashes to the active artifact. This is read-only and not a live-provider proof.
- **drift** means a home's current `Auth.Data` is not the active artifact.
- **freshest** means newest observed credential metadata, often by provider expiry/refresh-token fields, not by capture timestamp alone.
- **valid** means a live provider operation currently accepts the credential.

Do not assume these states agree. Verify the specific state relevant to the user's problem.

## First Checks

Start read-only unless the user explicitly asks to mutate:

```bash
agentos agent accounts status --json
agentos agent accounts capture --global --dry-run --json
jq . ~/.agentos/accounts/<provider>/registry/active.json
```

For a specific provider home:

```bash
agentos agent accounts status --provider <provider> --home "$HOME_PATH" --json
agentos agent accounts materialize --provider <provider> --account <account>/<method> --home "$HOME_PATH" --check --json
```

Interpret `materialize --check`:

- `active_artifact_id` is what would be written.
- `captured_artifact_id` is what the home currently contains.
- if they differ, the home is drifted from the active pointer.

## State-Changing Commands

Know which layer each command writes:

- `status`: read-only, compares home state with active pointer; no provider call.
- `capture --dry-run`: read-only preview of what capture would archive.
- `capture`: reads homes and writes only registry artifacts/capture log.
- `activate`: writes only the active registry pointer. Homes remain drifted until materialized.
- `materialize --check`: read-only preview; capture-first result only.
- `materialize`: captures current home first, then writes the active artifact into exactly one home.
- `monitor` and `agent ping`: may perform live provider calls; use only when live validation is intended.

## Current Storage Shape

Current new-model state lives under:

```text
~/.agentos/accounts/<provider>/accounts.json
~/.agentos/accounts/<provider>/registry/active.json
~/.agentos/accounts/<provider>/registry/captures.jsonl
~/.agentos/accounts/<provider>/registry/artifacts/<artifact-id>
```

Do not assume old `register`, `link`, or `reconcile` commands exist. Check `agentos agent accounts --help` when in doubt.

## Route By Symptom

- Fresh or duplicate Codex `auth.json` files, backup auth files, or ChatGPT token claims: read `references/codex-auth-json.md`.
- Claude Code browser login, macOS Keychain, path-scoped ambient auth, artifact expiry/refresh-token questions, or "logged in but failing": read `references/claude-ambient-auth.md`.
- `agentos agent accounts monitor` shows fallback, stale usage, `fetch error`, or provider usage failures: read `references/account-monitor.md`.
- Active artifact is not freshest, homes are drifted/aligned unexpectedly, `activate` did not affect a home, or registry state looks contradictory: read `references/registry-consistency.md`.

## Mutating Discipline

When changing state:

1. Identify provider, account/method, provider account id, home path, current active artifact, current home artifact, and whether the user wants read-only or mutation.
2. Capture current homes before overwriting them. `materialize` already does capture-first, but inspect `captured_artifact_id` when debugging.
3. Choose the desired artifact explicitly. For Claude, compare `expiresAt` and refresh-token presence without printing tokens.
4. Activate the chosen captured artifact if it is not active.
5. Materialize each target home explicitly. Activating does not rewrite homes.
6. Re-run passive `status`. Run a live provider check only when the user asks for validation or it is operationally necessary.

Do not use alignment as proof of credential validity. Alignment is desired-state matching; only a live provider call proves current validity.

> $kw: --from Auth.Data
> $kw: --from Batchy.Skill
