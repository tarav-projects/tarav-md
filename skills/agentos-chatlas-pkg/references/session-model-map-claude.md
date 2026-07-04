# Session.Model.Map — Claude Code

Per-provider `Session.Model.Map` (see index `Session.Model.Map`). Maps Claude Code
native session concepts to `Chatlas.Session.Model` neutral concepts.

- provider / normalizer: `claude-code` → `claude-code.raw_session.experimental.v1` (`_claude.py`)
- evidence priority: **raw artifacts > source code**. The `seen:` line is the hard
  evidence — a real artifact you open and check yourself. The `native:` line is the
  leaked source (`harnesses/claude-leaked/src/`), interpretive only. When they
  disagree, artifacts win.
- this file is an index into evidence, not a claim. No passive states ("ok", "pending");
  a mapping exists only when grounded in a real artifact, and an absent concept is
  recorded with its verifiable zero-count.
- archive root: `~/Documents/chatlas/raw/claude-code/` (counts over 4638 session files
  unless noted; structural checks over a 1201-file / 10,987-record sample).

# Index

Reusable definitions referenced by the mapping records below.

## Legend
- neutral target: `Concept` = settled index concept; *proposed* = neutral concept not
  yet designed; `→ native` = stays provider-specific in `native`/`source_refs`;
  `TBD: <candidate>` = open gap naming a candidate neutral concept to be designed and
  promoted to the index.
- a record exists only for a non-obvious / decision-bearing mapping. Obvious 1:1s are
  omitted: message `role` user/assistant, `text` content, `tool_use`→tool-call,
  `tool_result`→tool-result, visible `thinking`→reasoning.

## Sources
Session-file anchors for the `seen:` lines. All references pinned at archive git commit
`6696ded47`; reference form is `<anchor>:<line>` = `<commit>/<path>/<line>` in `~/Documents/chatlas`.
- `S1` = `6696ded47/raw/claude-code/86acc51cd232dc0130baedad0ac45c8d0623f692e31f5fe95ea45f04ba2f55e8/home/projects/-Users-pereiro-projects-agentos-project/8d821501-f66e-4d27-9ec3-8f98ae6aa45a.jsonl`
- `S2` = `6696ded47/raw/claude-code/86acc51cd232dc0130baedad0ac45c8d0623f692e31f5fe95ea45f04ba2f55e8/home/projects/-Users-pereiro-projects-agentos-project/5d73ef54-30c7-4da2-a417-269366558b6f.jsonl`
- `S3` = `6696ded47/raw/claude-code/86acc51cd232dc0130baedad0ac45c8d0623f692e31f5fe95ea45f04ba2f55e8/home/projects/-Users-pereiro--agentos-agent-homes-claude-code-browser-br-agentos-workspaces-statusline-refresh/34c74fae-9c2a-4591-a814-5237993eb774.jsonl`

## Claude.TranscriptMessage
The common record envelope — confirmed present on every sampled record.
- seen: `S1:9` carries `{uuid, parentUuid, isSidechain, sessionId, cwd, version, userType, entrypoint, gitBranch}` (uuid `04381c50…`, `version:"2.1.168"`, `entrypoint:"cli"`, `gitBranch:"HEAD"`, `cwd:"/Users/pereiro/projects/agentos-project"`)
- native: `TranscriptMessage` common fields (`logs.ts:8-17,221-231`)
- referenced by the lineage and session-metadata records

## Claude.SystemRecord
- seen: `S1:9` → `{"type":"system","subtype":"turn_duration",…}`; `S2:467` → `{"type":"system","subtype":"compact_boundary",…}`
- native: `{type:'system', subtype, content, isMeta, level?, …}` (`messages.ts:4335-4419`); `subtype` selects the mapping

# Mappings

Append-only. One section per native concept.

## attachment
- seen: `S1:6` → `{"type":"attachment","attachment":{"type":"deferred_tools_delta","addedNames":["CronCreate",…]},"uuid":"000633c8…","timestamp":…}`. Present in 2353/4638 sessions. `attachment.type` taxonomy (sample 900 files): `task_reminder` 37, `deferred_tools_delta` 12, `skill_listing` 10, `command_permissions` 6, `compact_file_reference` 3, `date_change` 2, `file` 2, `invoked_skills` 1
- native: first-class transcript record, no `role` (`sessionStorage.ts:143`, `attachments.ts:3201`)
- neutral: `TBD: injected-context`
- rationale: artifacts show attachments are overwhelmingly **injected context** (tool/skill availability, reminders, permission state), NOT user attachments/screenshots as the source name suggests — only `file` (2) is user-content-like. The neutral concept is closer to injected/system context than to user attachments. chatlas drops it to opaque `session.update` (`_claude.py:328-349`), losing the injected content and its `attachment.type`.

## parentUuid / logicalParentUuid
- seen: `parentUuid` on every `Claude.TranscriptMessage` (`S1:6`, `S1:9`). `logicalParentUuid` is rare — 1/10,987 records — and appears on the compaction boundary: `S2:467` has `logicalParentUuid:"c31ba9a0…"` pointing across the compacted span
- native: transcript chain link; `logicalParentUuid` re-threads across compaction (`logs.ts:9`)
- neutral: `Session.Lineage` — a conversation fork (a parent with ≥2 conversation-bearing child subtrees) normalizes to a derived `lineage.rollback` event at the rebranch point plus `lineage: {on_active_path: false}` on the abandoned subtree's events; the active path is the ancestor chain of the last record (claude's replay rule). `logicalParentUuid` → compaction re-thread (see compaction)
- rationale: under the linear tape these are event-level origin refs, not the spine. Raw children counting is NOT a fork signal: `attachment` records are dead-end leaves sharing a parent with the `tool_result`, so every tool use forks the raw DAG benignly — only conversation-bearing children mark a rewind. Implemented by 528 (`_claude_mark_fork_lineage`); validated on the `knights-knaves-restore` corpus.

## system / turn_duration
- seen: `S1:9` → `{"type":"system","subtype":"turn_duration","durationMs":4179,"messageCount":4,"isMeta":false,…}` (uuid `04381c50…`). Present in 1382/4638 sessions
- native: `messages.ts:4433-4444`
- neutral: *metric: turn-timing* (proposed)
- rationale: chatlas maps to `metric` with `duration_ms` — **validated** against the artifact (corrects note 518's false positive). `budgetTokens`/`messageCount` also present and currently unmapped. `isMeta:false` here.

## system / compact_boundary
- seen: `S2:467` → `{"type":"system","subtype":"compact_boundary","content":"Conversation compacted","compactMetadata":{"trigger":"auto","preTokens":167845,"durationMs":141093,"preservedSegment":{"headUuid":…,"anchorUuid":…,"tailUuid":…}},"logicalParentUuid":"c31ba9a0…"}` (uuid `6a6c3d55…`). Present in 64/4638 sessions
- native: compaction event (`messages.ts:4539`); `microcompact_boundary` (`:4569`) NOT seen in dataset (0/4638)
- neutral: `TBD: compaction`
- rationale: primary, rich compaction evidence — `trigger` (auto), `preTokens`, `durationMs`, and a `preservedSegment` (head/anchor/tail uuids) marking what survived. A neutral compaction event should carry trigger, pre-size, and the preserved span.

## user / isCompactSummary
- seen: `S2:468` → `{"type":"user","isCompactSummary":true,"isVisibleInTranscriptOnly":true,"parentUuid":"6a6c3d55…","message":{"role":"user","content":"This session is being continued from a previous co…"}}` (uuid `452ecbe8…`). Present in 64/4638 sessions (pairs with compact_boundary)
- native: post-compaction summary user turn (`messages.ts:465`)
- neutral: `TBD: compaction`
- rationale: the summary turn that follows a `compact_boundary` (its `parentUuid` is the boundary uuid). chatlas treats it as an ordinary human turn; it is a compaction facet, not human input. `isVisibleInTranscriptOnly:true` here (see below).

## isVisibleInTranscriptOnly
- seen: `S2:468` → `"isVisibleInTranscriptOnly":true` (uuid `452ecbe8…`). Present in 64/4638 sessions (co-occurs with isCompactSummary)
- native: content shown in transcript but not sent to the model (`messages.ts:480`)
- neutral: *surface: transcript-only* (proposed)
- rationale: a neutral surface/visibility flag (transcript vs model-input). Currently ignored.

## assistant / usage
- seen: `S1:8` assistant msg → `usage:{"input_tokens":5480,"cache_creation_input_tokens":3263,"cache_read_input_tokens":8605,"output_tokens":63,"server_tool_use":{"web_search_requests":0,"web_fetch_requests":0},"service_tier":"standard","cache_creation":{"ephemeral_1h_input_tokens":3263,"ephemeral_5m_input_tokens":0},"inference_geo":"not_available","iterations":[…],"speed":"standard"}`. `server_tool_use` present in 2784/4638 sessions
- native: `Usage` object (`messages.ts:362-376`)
- neutral: 4 token counts → usage (mapped today, `_claude.py:876-881`); richer fields `TBD: usage`
- rationale: usage is per-assistant-message = per model request → model-run-scoped, not session. Rich fields (`server_tool_use`, `service_tier`, `cache_creation.{1h,5m}`, `inference_geo`, `iterations`, `speed`) are real and abundant; decide per field neutral-vs-native. A `diagnostics` sibling also appears alongside `usage`.

## assistant / isApiErrorMessage
- seen: `S3:5` → `{"type":"assistant","isApiErrorMessage":…,"message":{"model":"<synthetic>","stop_reason":"stop_sequence","stop_details":null,…}}`. Present in 1409/4638 sessions
- native: assistant API-error turn (`messages.ts:379,402-406`)
- neutral: `TBD: run-outcome`
- rationale: API-error turns carry `model:"<synthetic>"`; common in the dataset. chatlas treats them as normal assistant text — model-run outcome should reflect the failure.

## tool_use / tool_result (correlation)
- seen: `S2:10` → `tool_use` `{"type":"tool_use","id":"toolu_01U6…","name":"Bash","input":{…},"caller":{"type":"direct"}}` and its paired `tool_result` `{"tool_use_id":"toolu_01U6…","type":"tool_result","content":…,"is_error":false}`
- native: API content blocks
- neutral: tool-call / tool-result (mapped today); `caller` `→ native`
- rationale: the block mapping is obvious; recorded only for the non-obvious `caller` field (`{type:'direct'}`) which has no neutral home → native. `tool_use_id` is the lifecycle correlation key.

## session metadata (envelope)
- seen: every record carries the envelope — `S1:6` has `cwd`, `version` (`"2.1.168"`), `gitBranch` (`"HEAD"`), `entrypoint` (`"cli"`), `userType` (`"external"`), `sessionId`; `S2:468` also `slug` (`"compiled-mixing-riddle"`)
- native: `SerializedMessage` envelope (`logs.ts:8-17`)
- neutral: `sessionId` → `Session.Identity`; `cwd`/`gitBranch`/`version`/`entrypoint` → `TBD: session-metadata`; `slug`/`userType`/`promptId` → `→ native`
- rationale: working dir, git branch, harness version, and entrypoint are real on every record and currently dropped (chatlas keeps only `uuid`/`parent_uuid`). Candidate neutral session-metadata slot.

## thinking (empty marker)
- seen: `thinking` content items with `thinking: ""` and only a `signature` — every thinking item in the `knights-knaves` corpus sessions (6/6, 6/6, 7/7); claude-code does not persist thinking text in the session artifact
- native: assistant content block `{type:'thinking', thinking, signature}`
- neutral: `reasoning` event with `{visibility: "redacted", content: null, signature}` — an explicit reasoning-occurrence marker, no fabricated content
- rationale: the artifact proves reasoning occurred without carrying its text; per `Chat.Semantic.From.File.Content` the tape emits the absence explicitly rather than dropping the occurrence. Content-bearing thinking (if a future version persists it) stays `visibility: "visible"`. Implemented by 528 Slice 2.

# Absent in dataset (verifiable zero-grounding)

Concepts the leaked source describes but the archive does not contain. Recorded as
evidence, not omitted. Re-check with the noted probe; do not write mappings for these
without artifact grounding.

- `summary` record (`type:'summary'`) — 0/4638 sessions (`grep -rl '"type":"summary"'`). The source's standalone summary Entry does not occur here.
- `redacted_thinking` content block — 0/4638 sessions. The note-518 "handle redacted_thinking" improvement is ungrounded in this dataset.
- `microcompact_boundary` system subtype — 0/4638. Only `compact_boundary` occurs.
- sub-agent provenance — top-level `agentId` key 0/10,987 records; `isSidechain:true` 0/10,987 (every record has `isSidechain:false`); top-level `teamName`/`agentName` not seen. The source's sidechain/sub-agent fields are not carried as record fields here. The candidate `sub-agent-lineage` neutral concept has no Claude grounding — justify cross-provider (Codex) before making it neutral.
- inline `image` content block — 0 in the 900-file sample. Weakly grounded; do not assume.
