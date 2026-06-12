# Chatlas Commands

Operational Chatlas command reference absorbed from the deprecated `chatlas-usage` skill.

## Default Command Mapping

- Refresh dataset: `agentos chatlas update`
- Inventory/query sessions: `agentos chatlas query`
- Aggregate dataset stats: `agentos chatlas stats`
- Export standard-model views: `agentos chatlas export`
- Export raw artifacts: `agentos chatlas raw path` / `agentos chatlas raw export`
- Consume or produce materialized views: `agentos chatlas views`

## Working Rules

- Prefer `agentos chatlas ...` for normal session workflows.
- Use `agentos chat debug ...` only for live provider diagnostics, raw artifact extraction, or connector troubleshooting.
- If freshness matters, run `agentos chatlas update` before querying.
- If already-materialized dataset contents are enough, query first and avoid unnecessary updates.
- Default Chatlas dataset root is `~/Documents/chatlas`.

## Query Workflow

```sh
agentos chatlas query
agentos chatlas query "<query>" --include-match
agentos chatlas query "<query>" --include-match --include-provider-stats
agentos chatlas query "<query>" --include-artifacts
agentos chatlas query --active-after <iso-timestamp> --sort newest
agentos chatlas query "<query>" --compact
agentos chatlas update
agentos chatlas update --scan-cache false
agentos chatlas update --session-index-cache false
agentos chatlas update --verbose-mode=quiet --output-mode=json
```

## Export Workflow

```sh
agentos chatlas export "<query>" --view full --format json
agentos chatlas export "<query>" --view transcript --format json
agentos chatlas export "<query>" --view user --format json
agentos chatlas export "<query>" --view replay --format json
agentos chatlas export "<query>" --view events --format json
agentos chatlas export "<query>" --view zip-transcript --format json
agentos chatlas raw path "<query>"
agentos chatlas raw export "<query>" --format json
```

## Views Workflow

```sh
agentos chatlas views list
agentos chatlas views status --view <view-name> <selector-options>
agentos chatlas views get --view <view-name> <selector-options>
agentos chatlas views path --view <view-name> <selector-options>
```

Producer references live in `agentos-chatlas-pkg/references/`.
