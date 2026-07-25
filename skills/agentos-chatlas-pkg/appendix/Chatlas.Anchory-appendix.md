****

## Chatlas.Anchory/Record.Format

- the record is the JSON payload stored under a chat anchor
- `app` — record discriminator, fixed `"chatlas"`; lets records of different applications coexist in one namespace
- `schema` — fixed `"chatlas.support-set.v1"`; no earlier Chatlas record shape is supported
- `hint` — one sentence describing what the support set evidences
- `members` — a non-empty ordered list of support turns, stored in relevance order
- each member's `session` is the full Chatlas `identity_hash`
- each member's `event_id` is the exact event identifier within that session's normalized tape
- each member's `at` is copied from the identified event for readability and integrity checking; it is never a fallback selector
- every member resolves to a visible user message; duplicate members and unknown fields are invalid
- the project is not a field — it is derivable from the session inside Chatlas; duplicating it invites desync

****

## Chatlas.Anchory/Resolution

example record:

```json
{
  "app": "chatlas",
  "schema": "chatlas.support-set.v1",
  "hint": "Evidence supporting the Grounding.Head/Drift section split",
  "members": [
    {
      "session": "<full identity_hash>",
      "event_id": "event-6894",
      "at": "2026-07-07T18:38:08.127Z"
    }
  ]
}
```

- `session + event_id` is identity; if the event is absent or `at` differs, resolution fails as stale instead of selecting a nearby event
- one anchor may contain members from several sessions; resolution returns one independent `Chatlas.Session.Model` neighborhood per member and never merges sessions
