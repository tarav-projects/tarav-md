# L2 Miner — block → block reqs

L2 is the block-to-reqs `Grounding.Miner`. `Cited.Duplication` of `[Grounding.Miner, Grounding.Request, Topic.Identity, Grounding.Latest.Wins]` from the package indexes.

Input: one kernel block. Output: `<project>/notes/live/grounding/<block-name>-gr-req.jsonl` (see `gr-req-format.md`). L2 is keyed by project blocks and writes into the target project.

## L1 as a searchable layer

L2 does not re-read every chat. It treats the L1 session files in the `Chatlas.Depot` as a hand-built retrieval index over chats — how MVP mining avoids a vector backend:

```sh
rg -n "Block.Name|token|neighbor-term" ~/Documents/chatlas/grounding/*-gr-req.jsonl
```

Match on the `blocks` field and on `grounding-why` text.

## Procedure

1. **Read the target block.** Concept name (`Topic.Identity`), fundamentals, existing `### grounding`, aliases, user-language phrases. If the evidence is really a subtopic, propose a separate block instead of forcing grounding onto the parent.

2. **Load existing block records.** Read `<block-name>-gr-req.jsonl`; dedup context.

3. **Search the L1 layer.** Probe the depot session files for the block name, split tokens, user phrasing, and named neighbors. Prefer a few high-signal probes. Failed search is not proof of absence — widen probes once, then report.

4. **Confirm against the chat.** For each L1 hit, return to the actual chat turn (`chatlas-surface.md`, `--ref`) and verify it establishes something for this block. Never append from an L1 record's summary alone.

5. **Append confirmed records.** Build `{ref, blocks:[Block.Name], grounding-why}`; dedup per `ref`; append only.

6. **Report.** Block, count of new records, file path.

## Discipline

- L2 confirms before appending; L1 is the lead, the chat turn is the evidence.
- L2 records evidence; it does not decide `*HEAD*` vs history vs `DRIFT`. `Grounding.Latest.Wins` and the reviewer settle the current view at index-write time.
- when the L1 layer is thin for a block, run L1 over the relevant sessions first, then L2.
