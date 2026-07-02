# Chat.Grounding.Request Format

The miner's output artifact. `Cited.Duplication` of `[Chat.Grounding.Request, Chat.Grounding.Miner.Locality]` from `agentos-chatlas-pkg/design`; the index owns authority.

A `Chat.Grounding.Request` is append-only JSONL — one record per line. It queues candidate grounding for later gated index writing. It is not index truth and never mutates index/appendix blocks by itself.

## Record

```json
{"ref": "@<hash>-<time>..<time>", "blocks": ["Concept.Name"], "grounding-why": "why this turn is Chat.Grounding.Material and what to weigh before pulling it"}
```

- `ref` — a `Chat.Ref` into the `Chat.Surface` (see `chatlas-surface.md`). Prefer the smallest range that preserves the decision.
- `blocks` — kernel blocks named explicitly in the turn. May be empty (`[]`) for block-agnostic material. The miner never invents block names; it records only what the turn names.
- `grounding-why` — describes the request, not the turn: why it is `Chat.Grounding.Material` and what an agent should consider before pulling it. Same function as a Skill description. One line, block-shaped, not a transcript summary.

The record carries evidence only. Classification into `*HEAD*`, appendix history, or `DRIFT:` is the reviewer's job, not the miner's.

## Two File Kinds (`Chat.Grounding.Miner.Locality`)

- **session request (L1)** — `<identity_hash>-gr-req.jsonl`, one chat session, in the `Chatlas.Depot`:

  ```txt
  ~/Documents/chatlas/grounding/<identity_hash>-gr-req.jsonl
  ```

- **block request (L2)** — `<block-name>-gr-req.jsonl`, one kernel block, in the target project under its grounding base path (skill arg; default `notes/live/grounding/`):

  ```txt
  <project>/notes/live/grounding/<block-name>-gr-req.jsonl
  ```

L1 reads only the `Chat.Surface` and serves every project, so its output is depot-resident and project-agnostic. L2 is keyed by a project's blocks and writes back into that project.

## Block-Name Sanitization

`<block-name>` is the block's `Dotted.Name` made filesystem-safe: keep dots, replace unsafe characters such as `:` with `-`.

- `Kernel.Block:Grounding` → `Kernel.Block-Grounding-gr-req.jsonl`
- `Chat.Surface.Closure` → `Chat.Surface.Closure-gr-req.jsonl`

## Append-Only + Per-Turn Dedup

- files are append-only; never rewrite or delete records.
- before appending for a turn, read existing records for that `ref` and skip or merge duplicates.
- a re-run adds only new material; re-mining an already-mined session should mostly no-op.
