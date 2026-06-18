---
name: chatlas-grounding-agent
description: Grounding.Miner for the Chat.Surface. Mine Chatlas sessions into append-only Grounding.Request JSONL for Agentos kernel blocks. Two levels — L1 (chat→session reqs) and L2 (block→block reqs). USE WHEN a caller wants chat-to-block or block-to-chat grounding mining that proposes candidate Chat.Refs without writing the index. Called like a terminal command — a `--level` (L1/L2) and a `--target`.
---

# Chatlas Grounding Agent

Operational `Package.Aux.Skill` under `agentos-chatlas-pkg`.

`Grounding.Miner` for the `Chat.Surface`: mine chat sessions for `Grounding.Material` and append `Grounding.Request` records for later gated index review. The miner **neither creates nor destroys information** — it surfaces high-signal turns and converges toward exhausting the design signal in the chats. It never writes index or appendix files.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- supplied flags resolve to the `Skill.Arg` names below.

## Skill.Arg.Section

### Skill.Arg:Level
- the mining level: `L1` (chat→session requests) or `L2` (block→block requests)
- required: false
- default: L1
- help: "mining level: L1 or L2"
- examples: --level L2

### Skill.Arg:Target
- what to mine: the chat sessions, scope, or kernel block(s) to ground
- required: false
- help: "the sessions or blocks to mine"
- examples: --target "agentos-pkg index blocks"

For the concept model, read the owning index blocks:

- `agentos-chatlas-pkg` index — `Grounding.Miner`, `Grounding.Miner.Locality`, `Grounding.Material`, `Grounding.Material.Catalog`, `Grounding.Request`
- `agentos-pkg` index — `Chat.Surface`, `Chat.Ref`, `Chat.Grounding`, `Grounding.Latest.Wins`, `Topic.HEAD`

## Two Levels

- **L1 — chat→reqs.** Read one chat session, detect `Grounding.Material` turns, append session records. Reads only the `Chat.Surface`, never a project. Output lives in the `Chatlas.Depot`. See `references/l1-miner.md`.
- **L2 — block→reqs.** Target one kernel block, search the L1 session layer, confirm against the actual chat turn, append block records. Output lives in the target project. See `references/l2-miner.md`.

Both produce `Grounding.Request`s; neither writes the index.

## Routing

| Need | Load |
|---|---|
| record shape, file kinds, paths, dedup | `references/gr-req-format.md` |
| what counts as `Grounding.Material` | `references/grounding-material-catalog.md` |
| run L1 (mine a session) | `references/l1-miner.md` |
| run L2 (ground a block) | `references/l2-miner.md` |
| query / export chat evidence | `references/chatlas-surface.md` |

## Pick The Level

- caller gives a **session / `Chat.Ref` / transcript** and wants its design signal mined → **L1**.
- caller gives a **kernel block** and wants chat evidence for it → **L2** (which leans on existing L1 output).
- no target → ask which: a session to mine, or a block to ground.

## Boundaries

This skill does not:

- write index or appendix files, or decide stable index wording
- decide final grounding authority — `*HEAD*`, appendix history, or `DRIFT:` classification is reviewer work on the `Grounding.Request`, settled by `Grounding.Latest.Wins` at index-write time
- use or require vector search
- treat absence of search hits as absence of grounding
