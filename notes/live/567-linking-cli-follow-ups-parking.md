# Linking CLI Follow-Ups — Parking.Note

Items surfaced while designing the `agentos-index --link` module (first end-to-end anchor run, session `9d194db7…`). Companion stream: 564/565/566 anchory impl-reqs — allocation and chatlas integration are out of their scope.

## Anchory: atomic prefix allocation — DONE (568, executed 2026-07-08)

- status: implemented by `568-anchory-prefix-allocation-impl-req.md`
- `agentos anchory register --prefix <YYYYMMDD> --record-json '…'` — allocates the next free `-N` under the depot lock, registers, and returns the full anchor
- closes the query-then-register race; the returned anchor is what the agent tags the line with
- an advisory `next` peek may exist later if workflows demand it, documented as non-reserving
- user-confirmed direction (this session)

## Chatlas: anchors digestible natively — DONE (569, executed 2026-07-08)

- `agentos chatlas query --anchor <anchor>` (and sibling read surfaces) — resolve a chat anchor through the chatlas anchory depot and land on the session/turn neighborhood
- anchors are the successor of `Chat.Ref`; the `--ref` query surfaces were tuned for the old `Chat.Ref` grammar and need review — keep, retarget to anchors, or retire
- user-confirmed direction (this session)

## Chatlas: turn-level search ergonomics — DONE (569, executed 2026-07-08)

- locating an evidence turn currently means pulling the full `views inline` payload and scanning client-side (551 events for one turn in the test run)
- wanted: a turn/event search returning matching events with timestamps — input to `--link` step 2
- optimization, not a blocker: the inline-view path works today
