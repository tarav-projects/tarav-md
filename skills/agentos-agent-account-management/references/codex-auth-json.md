# Codex Auth JSON

Use this when working with Codex `auth.json` files, backup auth files, or Codex homes such as `~/.codex`, `~/.codex-jp`, and `~/.agentos/agent/homes/codex/<account>`.

## Read Identity Without Printing Tokens

Do not paste raw tokens in chat. Extract only stable metadata:

```bash
python3 - <<'PY' "$AUTH_FILE"
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

Compare bytes with:

```bash
sha256sum "$HOME"/.codex*/auth*.json
```

## Register And Materialize

Register a fresh Codex auth artifact:

```bash
agentos agent accounts register --provider codex \
  --auth-file "$AUTH_FILE" \
  --account "$ACCOUNT" \
  --email "$EMAIL"
```

Materialize the active artifact into a home for manual repair:

```bash
agentos agent accounts materialize --provider codex --home "$HOME_PATH" --account "$ACCOUNT" --force
```

Use `--register-only` only when staging an artifact before deciding whether to activate it.

## Live Usage Validation

Codex `matching-active` only proves the home matches Agentos registry metadata. It does not prove ChatGPT accepts the token.

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

- `401 token_expired`: the access token is expired; re-login or use a fresher artifact.
- `401 token_invalidated`: the auth payload has been invalidated; re-login or use a different valid artifact.

After a successful live validation, make sure the artifact is verified, active, and materialized. Passive reconcile may otherwise revert homes to the latest verified artifact.
