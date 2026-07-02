# L1 Miner — chat → session reqs

L1 is the chat-to-reqs `Chat.Grounding.Miner`. `Cited.Duplication` of `[Chat.Grounding.Miner, Chat.Grounding.Material, Chat.Grounding.Miner.Locality]` from `agentos-chatlas-pkg/design`.

Input: one chat session. Output: `~/Documents/chatlas/grounding/<identity_hash>-gr-req.jsonl` (see `gr-req-format.md`). L1 reads only the `Chat.Surface` — no project, no index.

## Procedure

1. **Resolve the session.** Take the caller's session id, `identity_hash`, `Chat.Ref`, or selector. Get the `identity_hash` (the session file key) and read the transcript with `chatlas-surface.md`. Use `--view user` when user turns suffice; `--view transcript` when assistant context is needed to read a decision.

2. **Load existing records.** Read `<identity_hash>-gr-req.jsonl` if it exists. These are dedup context — do not re-propose what is already recorded for a `ref`.

3. **Walk turns, apply the catalog.** For each turn (or span), test it against `grounding-material-catalog.md`. Detect `Chat.Grounding.Material` with or without named blocks.

4. **Build each record.**
   - `ref` — smallest `Chat.Ref` range that preserves the decision.
   - `blocks` — only blocks the turn names explicitly; else `[]`.
   - `grounding-why` — one block-shaped line: why it is material, what to weigh.

5. **Dedup + append.** For each candidate `ref`, skip or merge against existing records. Append new records only; never rewrite the file. Create `~/Documents/chatlas/grounding/` if missing.

6. **Report.** Print the session, the count of new records, and the file path. Do not paste the file.

## Discipline

- append-only; one turn may yield several records, a noisy turn may yield none.
- L1 surfaces signal; it does not classify `*HEAD*` / history / `DRIFT`.
- `blocks` records what the turn names — never resolve or validate names against any project, so L1 stays project-agnostic.

## Cooldown

Mining capacity is shared across many chats. Re-mine a session only after a cooldown, not back-to-back — a fresh re-run over an already-mined session should mostly no-op via dedup. Prefer un-mined or recently-active sessions first (`agentos chatlas recents`).
