****

## Chatlas.Anchory/Record.Format

- the record is the JSON payload stored under a chat anchor
- `app` — record discriminator, fixed `"chatlas"`; lets records of different applications coexist in one namespace
- `session` — the full session `identity_hash`; no prefixes — the token stays small, the record carries the fat
- `at` — one ISO 8601 timestamp marking the landing turn, truncatable precision; no ranges — the reading rule is land and read around
- `hint` — one sentence describing what is at the location; the desync tripwire — resolved turns that do not match the hint expose a stale record
- the project is not a field — it is derivable from the session inside Chatlas; duplicating it invites desync

example record:

```json
{
  "app": "chatlas",
  "session": "<full identity_hash>",
  "at": "2026-06-30T14:22:05",
  "hint": "user proposes the Grounding.Head/Drift section split"
}
```
