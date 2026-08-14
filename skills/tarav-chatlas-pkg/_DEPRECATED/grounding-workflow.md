# DEPRECATED — grounding miner workflow (L1/L2)

> parked 2026-07-05 during the grounding-system redesign (`Index.Linking` / grounding levels).
> these blocks are out of the routed index; kept for reference only.

****

## Chat.Grounding.Miner

- `Chat.Grounding.Miner` is an agent that produces `Chat.Grounding.Request`s from chat evidence — candidate evidence, not authority.
- it has two levels that mine in opposite directions.
- L1 mines chat-to-reqs: it reads one chat session and emits a session `Chat.Grounding.Request` of `Chat.Grounding.Material` records, detected by heuristic with or without named blocks.
- L2 mines block-to-reqs: it targets one kernel block, searches the L1 session layer, confirms against the actual chat turn, then appends a block `Chat.Grounding.Request`.
- the L1 session layer acts as a hand-built retrieval index over chats — how MVP mining avoids a vector backend on constrained hardware.
- output is append-only and per-turn deduped; mining is shared across chats via a re-mine cooldown.
- it neither creates nor destroys information — it surfaces high-signal turns/sessions, converging toward exhausting the design signal in the chats.
- both levels produce `Chat.Grounding.Request`s; neither writes the index.

****

## Chat.Grounding.Miner.Locality

- `Chat.Grounding.Miner.Locality` is the placement rule for chat miner output — `Natural.Placement` applied to the pipeline: the two levels derive from different scopes, so they live on different surfaces.
- L1 → `Chatlas.Depot`: L1 reads only the `Chat.Surface`, never a project, and serves every project; its output is derived chat data stored in the depot at `~/Documents/chatlas/grounding/`.
- L2 → target project: L2 is keyed by a project's `Index.Block`s and writes into that project's `### grounding`, so `<block-name>-gr-req.jsonl` lives in the target project (skill arg).
- L1's recorded `blocks` strings may name project concepts, but L1 only stores the strings — never resolving them — so L1 stays project-agnostic.
- relation: L1 is the shared retrieval index in the depot; L2 is a per-project consumer of it — many L2s, one L1.

****

## Chat.Grounding.Material

- `Chat.Grounding.Material` is a chat turn (or turn span) carrying durable design signal worth grounding — the fundamental core of L1 detection.
- membership is governed by `Chat.Grounding.Material.Catalog`.
- the miner neither creates nor destroys information: it surfaces high-signal turns/sessions; chats stay the SSOT.
- system goal: converge toward exhausting all design signal in the chats — coverage grows over passes, not one-shot.
- detection is heuristic, not exhaustive: a miss is a recoverable gap, never corruption.
- requires no named block; block-agnostic material is still recorded, and one turn can yield multiple records.

****

## Chat.Grounding.Material.Catalog

- `Chat.Grounding.Material.Catalog` is the maintained, ever-growing list of positive and negative criteria defining `Chat.Grounding.Material`.
- it is never assumed complete.
- it refines from a high-signal feedback sample: turns approved into a `### grounding` section, fed back into the catalog.

****

## Chat.Grounding.Request

- `Chat.Grounding.Request` is a miner output artifact: queued candidate chat grounding entries (`### grounding`, appendix history, or `DRIFT:`) proposed for later gated index writing.
- produced by `Chat.Grounding.Miner`, digested later by a hugentic user/agent reviewer; it is not stable index truth and never mutates index/appendix blocks by itself.
- it lets low-cost miners collect evidence broadly — preserving ambiguity, search notes, and weak/rejected candidates — without crossing the index write gate.
- carrier: append-only JSONL, one record per line — `{"ref": "@<hash>-<time>..<time>", "blocks": ["Concept.Name"], "grounding-why": "..."}`.
- `grounding-why` describes the request, not the turn — why it is `Chat.Grounding.Material` and what to weigh before pulling it; same function as a Skill description.
- `blocks` lists only blocks named explicitly in the turn, and may be empty for block-agnostic material.
- two kinds — session (L1) and block (L2) — whose file locations are governed by `Chat.Grounding.Miner.Locality`.
- append-only with per-turn dedup: before appending, the miner reads existing records for that turn `ref` and skips or merges.

