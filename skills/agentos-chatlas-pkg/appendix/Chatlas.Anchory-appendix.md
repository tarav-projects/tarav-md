****

## Chatlas.Anchory/Record.Format

- the record is the JSON payload stored under a chat anchor
- `app` — record discriminator, fixed `"chatlas"`; lets records of different applications coexist in one namespace
- `schema` — `"chatlas.support-set.v3"` for generic/historical support or `"chatlas.support-set.v4"` for a line-bound Index relationship
- `hint` — one sentence describing what the support set evidences
- `members` — a non-empty ordered list of support turns, stored in relevance order
- each member's `session` is the full Chatlas `identity_hash`
- each member carries exact `turn_id`, `turn_hash`, and `at` coordinates from its `Normal.Turn.Ref`; optional `types` annotate roles such as approval without changing base support
- every member resolves to a visible user message; duplicate members and unknown fields are invalid
- v4 adds immutable `subject` identity for the versioned hash of `Line.Type + body` without trailing anchors
- v4 `predecessors` records the duplicate-free former anchors whose support contributed to the relationship; it may be empty for newly authored lines
- v3 remains readable for historical and non-line support, but new Index grounding supplies explicit line content and writes v4
- the project is not a field — it is derivable from the session inside Chatlas; duplicating it invites desync

****

## Chatlas.Anchory/Resolution

example record:

```json
{
  "app": "chatlas",
  "schema": "chatlas.support-set.v4",
  "hint": "Evidence supporting the Grounding.Head/Drift section split",
  "subject": {"kind": "index.line", "canonical_schema": "agentos.index-line-content.v1", "content_hash": "sha256:<hex>"},
  "predecessors": ["c20260707-0u"],
  "members": [{
      "session": "<full identity_hash>",
      "turn_id": "turn-r6894",
      "turn_hash": "<sha256>",
      "at": "2026-07-07T18:38:08.127Z"
  }]
}
```

- `session + turn_id` locates the grouping while `turn_hash` verifies it; absent or changed turns fail stale instead of selecting nearby evidence
- one anchor may contain members from several sessions; resolution returns one independent `Chatlas.Session.Model` neighborhood per member and never merges sessions
- a v4 subject mismatch is `Index.Linter/Anchor.LineDrift`; different line contents sharing one anchor are `Index.Linter/Anchor.Collision`
