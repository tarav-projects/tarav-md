# Codex Auth JSON

Use this when working with Codex `auth.json` files, backup auth files, or Codex homes such as `~/.codex`, `~/.codex-jp`, and `~/.agentos/agent/homes/codex/<account>`.

## Read Identity Without Printing Tokens

Do not paste raw tokens in chat. Extract only stable metadata:

```bash
python3 - "$AUTH_FILE" <<'PY'
import base64, json, sys
p = sys.argv[1]
o = json.load(open(p))
t = o.get("tokens", {}).get("id_token")
claims = json.loads(base64.urlsafe_b64decode(t.split(".")[1] + "==")) if t else {}
auth = claims.get("https://api.openai.com/auth", {})
profile = claims.get("https://api.openai.com/profile", {})
print(json.dumps({
  "account_id": auth.get("chatgpt_account_id") or o.get("tokens", {}).get("account_id"),
  "email": profile.get("email") or claims.get("email"),
  "iat": claims.get("iat"),
  "auth_time": claims.get("auth_time"),
  "last_refresh": o.get("last_refresh"),
}, sort_keys=True))
PY
```

Compare files by hash:

```bash
shasum -a 256 "$HOME"/.codex*/auth*.json
```

## Current Workflow

Read-only triage:

```bash
agentos agent accounts status --provider codex --json
agentos agent accounts capture --provider codex --global --dry-run --json
jq . ~/.agentos/accounts/codex/registry/active.json
agentos agent accounts materialize --provider codex --account <account>/file --home "$HOME_PATH" --check --json
```

Archive what a home currently holds:

```bash
agentos agent accounts capture --provider codex --home "$HOME_PATH" --json
```

Activate a captured artifact:

```bash
agentos agent accounts activate --provider codex --account <account>/file --artifact <artifact-id> --json
```

Write the active artifact into one home:

```bash
agentos agent accounts materialize --provider codex --account <account>/file --home "$HOME_PATH" --json
```

Activation does not rewrite homes. Materialize each desired home explicitly.

## Live Usage Validation

Codex `aligned` only proves the home matches Agentos registry intent. It does not prove ChatGPT accepts the token.

Validate a Codex home with the app-server rate-limit request:

```bash
CODEX_HOME="$HOME_PATH" codex app-server
```

Send JSONL:

```json
{"id":1,"method":"initialize","params":{"capabilities":{"optOutNotificationMethods":["account/updated","account/rateLimits/updated"]},"clientInfo":{"name":"agentos-debug","version":"1"}}}
{"id":2,"method":"account/rateLimits/read"}
```

Read until response id `2`; notification messages may arrive first.

Common failures:

- `401 token_expired`: access token expired; re-login or use a fresher artifact.
- `401 token_invalidated`: auth payload was invalidated; re-login or use a different valid artifact.
- `401 Unauthorized`: inspect the same home's `auth.json` identity and active pointer before materializing over it.

After a successful live validation, make sure the desired artifact is active and materialized into the target homes.
