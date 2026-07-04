# Session.Model.Map — codex

Native→neutral mapping decisions for the codex provider. Same conventions as
`session-model-maps.md`: append-only, one section per native concept, only non-obvious
mappings recorded, each row carries its rationale and survival decision.

## Sources
Session-file anchors for the `seen:` lines; reference form is `<path>` in `~/Documents/chatlas`.
- `C1` = `raw/codex/46626a3c3c87c26a0f98210757f09592b8c516e3877777e33e37653cb9706ded/home/sessions/2026/07/02/rollout-2026-07-02T13-14-56-019f23d3-95f8-71d1-b832-8bb63adcf269.jsonl`

# Mappings

## event_msg / thread_rolled_back
- seen: `C1:47` → `{"timestamp": "2026-07-02T17:16:09.325Z", "type": "event_msg", "payload": {"type": "thread_rolled_back", "num_turns": 1}}` — recorded when the user rolls the conversation back to a previous turn; abandoned turns stay inline in the rollout before the sentinel
- native: rollback sentinel on the linear rollout; `num_turns` counts the rolled-back turns
- neutral: `lineage.rollback` event (payload keeps `num_turns`) plus `lineage: {on_active_path: false}` on the events of the last `num_turns` turn_ids preceding the sentinel
- rationale: same meaning as a claude `parentUuid` conversation fork — one neutral `Session.Lineage` representation, two native encodings (codex linearizes and marks; claude branches the DAG). The sentinel position is the rebranch point. Implemented by 528 Slice 3; validated on the `knights-knaves-restore` corpus.
