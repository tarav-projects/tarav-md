# Claude Ambient Auth

Use this for Claude Code browser login, macOS Keychain, path-scoped ambient auth, expired/no-refresh-token failures, or "logged in but failing" incidents.

## Mental Model

Claude browser auth spans two places:

- identity: `<home>/.claude.json` `oauthAccount`
- secret: macOS Keychain service scoped to the resolved home path

On macOS, the secret service is:

```text
Claude Code-credentials-<sha256(resolved_home_path)[:8]>
```

The legacy `Claude Code-credentials` service may exist but should not be trusted as the target-home credential.

## Safe Keychain Inspection

Do not print tokens. Print only expiry, token lengths/presence, and identity.

```bash
python3 - "$HOME_PATH" <<'PY'
import hashlib, os, sys
p = os.path.realpath(sys.argv[1])
print("Claude Code-credentials-" + hashlib.sha256(p.encode()).hexdigest()[:8])
PY
```

```bash
security find-generic-password -s "Claude Code-credentials-<hash>" -w \
  | python3 -c 'import sys,json,datetime; o=json.load(sys.stdin); a=o.get("claudeAiOauth",{}); exp=a.get("expiresAt"); print("expiresAt", datetime.datetime.fromtimestamp(exp/1000, tz=datetime.timezone.utc).isoformat() if exp else None); print("refreshToken_len", len(a.get("refreshToken") or "")); print("accessToken_len", len(a.get("accessToken") or "")); print("top_keys", sorted(o.keys()))'
```

Dead-home signature:

- access token expired, and
- `refreshToken_len == 0`

A home can report logged in yet be dead. Real provider use may fail with 401 if the Keychain entry is expired and cannot refresh.

## Inspect Registered Claude Artifacts

Artifact payload files contain secrets. Use sanitized inspection only.

```bash
python3 - <<'PY'
import json, datetime
from pathlib import Path
root = Path.home() / ".agentos/accounts/claude-code"
for line in (root / "registry/captures.jsonl").read_text().splitlines()[-40:]:
    r = json.loads(line)
    if r.get("method") != "browser":
        continue
    aid = r["artifact_id"]
    p = root / "registry/artifacts" / aid
    if not p.exists():
        continue
    payload = json.loads(p.read_text())
    oauth = payload.get("claudeAiOauth", {})
    exp = oauth.get("expiresAt")
    print(json.dumps({
        "captured_at": r.get("ts"),
        "account": r.get("account"),
        "artifact_id": aid,
        "expires_at_utc": datetime.datetime.fromtimestamp(exp/1000, tz=datetime.timezone.utc).isoformat() if exp else None,
        "refresh_token_present": bool(oauth.get("refreshToken")),
        "email": (payload.get("oauthAccount") or {}).get("emailAddress"),
        "display_name": (payload.get("oauthAccount") or {}).get("displayName"),
    }, sort_keys=True))
PY
```

For Claude, "freshest" usually means later `expiresAt` plus a present refresh token, not simply latest capture timestamp.

## Current Workflow

Read-only triage:

```bash
agentos agent accounts status --provider claude-code --json
agentos agent accounts capture --provider claude-code --global --dry-run --json
jq . ~/.agentos/accounts/claude-code/registry/active.json
agentos agent accounts materialize --provider claude-code --account <account>/browser --home "$HOME_PATH" --check --json
```

If the user asks to activate a selected artifact:

```bash
agentos agent accounts activate --provider claude-code --account <account>/browser --artifact <artifact-id> --json
```

If the user asks to update homes:

```bash
agentos agent accounts materialize --provider claude-code --account <account>/browser --home "$HOME_PATH" --json
```

Run materialize once per desired Claude home. Activation does not write Keychain.

## Why Materialization Matters

`ClaudeAuthMethod.materialize` writes:

- Keychain secret for the target home's path-scoped service
- `<home>/.claude.json` `oauthAccount`

`agentos agent accounts materialize` captures the target home's current credential first, then writes the active artifact. In `--check` mode it reports the same `captured_artifact_id` without writing.

## Rotation Hazard

Claude OAuth refresh tokens can rotate. Multiple live homes for one Claude account may race:

- the winner refreshes and receives a new token pair
- the loser may become expired with an empty refresh token

When diagnosing, compare Keychain entries by home. A working artifact in the registry does not mean every home has been materialized to it.

## Live Validation

Only use live provider checks when the user asks for validation or it is necessary:

```bash
agentos agent ping --profile claude-om
CLAUDE_CONFIG_DIR="$HOME_PATH" /opt/homebrew/bin/claude
```

Live calls may trigger refresh behavior, so inspect `expiresAt` first when rotation safety matters.

## Code Entry Points

Current implementation:

```text
agentos-py/src/agentos/agent/commands.py
agentos-py/src/agentos/agent/capture.py
agentos-py/src/agentos/agent/auth_registry.py
agentos-py/src/agentos/agent/account_status_report.py
agentos-py/src/agentos/claude/auth_method.py
agentos-py/src/agentos/claude/keychain.py
```

Known code-doc mismatch: `claude/auth_method.py` has an old module docstring saying materialization is unimplemented; the method now writes Keychain and `.claude.json`.
