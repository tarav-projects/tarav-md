# Account Monitor

Use this when `agentos agent accounts monitor` shows fallback, stale usage, fetch errors, or surprising quota rows.

## Key Distinction

Monitor can show usage bars from the usage registry even when live usage fetch fails.

For Codex:

- Live fetch uses `codex app-server` method `account/rateLimits/read`.
- Usage registry fallback reads `~/.agentos/agent/usage-registry/*-usage.jsonl`.
- Fallback usage does not verify the auth artifact.

## Commands

Current monitor frame:

```bash
agentos agent accounts monitor --once --json
```

Extract provider rows:

```bash
agentos agent accounts monitor --once --json \
  | jq '.frame.blocks[] | select(.data.targets? != null) | .data.targets[] | {provider, account, status, usage_status: .account_status.usage_status, usage_errors: .account_status.usage_errors, usage_record: .account_status.raw.usage_record}'
```

Latest usage records:

```bash
python3 - <<'PY'
import json
from collections import defaultdict
p = "~/.agentos/agent/usage-registry/202606-usage.jsonl"
rows = defaultdict(list)
for line in open(p.replace("~", __import__("os").path.expanduser("~"))):
    o = json.loads(line)
    if o.get("source") == "app_server":
        rows[(o.get("provider"), o.get("account"))].append(o)
for key, values in sorted(rows.items()):
    last = values[-1]
    print(key, last.get("recorded_at"), last.get("home"))
PY
```

## Interpret Rows

- `usage_status: ok` with `raw.usage_record.status: registry_latest` means setup loaded cached usage.
- `registry_fallback` means a live fetch failed and Agentos kept usable cached limits.
- A visible `fetch error` row means the live provider call failed; inspect the provider-specific reference.
- Stale reset times usually mean the cached usage record is old, not that the provider has current reset data.

## Codex Live Failure Check

If monitor shows Codex `api/wham/usage failed`, test the home directly with `references/codex-auth-json.md`.

Common backend messages:

- `token_expired`
- `token_invalidated`
- `401 Unauthorized`

Those require a fresher valid auth artifact, not just relinking the same artifact.
