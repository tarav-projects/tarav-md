# Chatlas Surface

How the miner reads the `Chat.Surface`. `Cited.Duplication` of `[Chat.Surface, Chat.Ref]` (agentos-pkg) and `[Chatlas.Query.Surface]` (agentos-chatlas-pkg).

Agents access chat content through `agentos chatlas`. The `Chat.Surface` is append-only, so a `Chat.Ref` is a stable, never-dangling pointer.

## Refresh (only when freshness matters)

```sh
agentos chatlas update --verbose-mode=quiet --output-mode=json
```

## Discover sessions

```sh
agentos chatlas recents --limit 20 --json
agentos chatlas query --message-contains "<term>" --sort newest --limit 20
agentos chatlas query --user-contains "<term>" --sort newest --limit 20
agentos chatlas query --project-base <name> --message-contains "<term>" --sort newest --limit 20
agentos chatlas query --ref "@<hash>-<time>"
```

Useful filters: `--project` / `--project-base` (project-local grounding), `--provider`, `--active-after`, `--min-user-turns`, `--field session_id|identity_hash` for compact follow-up.

Prefer a few high-signal probes over broad noisy recall. Do not use vector search. Do not treat a failed search as proof no grounding exists.

## Read an inline session view

```sh
agentos chatlas views inline --identity-hash <hash> --view transcript --format json
agentos chatlas views inline --session-id <id> --view user --format json
agentos chatlas views inline --ref "@<hash>-<time>..<time>" --view transcript --format json
```

- `--view user` when user turns alone settle it; `--view transcript` for user+assistant; `--view full` only when tool calls or metadata are materially needed.

## Chat.Ref construction

```txt
@<identity-hash-prefix>-<timetag>                point/window
@<identity-hash-prefix>-<timetag1>..<timetag2>   range
@<identity-hash-prefix>                           whole session
```

- `<hash>` is an `identity_hash` prefix; `<timetag>` is ISO 8601, truncatable to any precision.
- prefer a range when evidence spans turns; prefer the smallest range that preserves the decision.
- session-level ref only when the whole session is the evidence.

Note: the session **file key** for L1 (`<identity_hash>-gr-req.jsonl`) uses the full `identity_hash`; the `ref` inside records may use a shorter prefix.
