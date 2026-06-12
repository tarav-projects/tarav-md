---
name: chatlas-grounding-agent
description: Mine Chatlas sessions into Grounding.Request live notes for Agentos kernel blocks. Use when a caller wants block-to-chat or chat-to-block mining that proposes `### grounding`, `*HEAD*` refs, appendix history refs, or `DRIFT:` candidates without writing the index.
---

# Chatlas Grounding Agent

Operational `Package.Aux.Skill` under `agentos-chatlas-pkg`.

Mine Chatlas sessions for grounding evidence and produce a `Grounding.Request` live note for human/index-workflow review. Do not mutate stable index or appendix files directly.

## Inputs

The caller should provide one mining direction and its target:

- **block-to-chat**: one target kernel block or a set of target blocks
- **chat-to-block**: one Chatlas session, `Chat.Ref`, transcript, or chat window
- optional scope filters: project path/base, provider, active-after date, search hints, known session ids, or known `Chat.Ref`s

For block-to-chat, the caller should provide enough block text to understand the topic: heading, fundamentals, existing `### grounding`, and appendix if relevant.

For chat-to-block, the caller should provide the session selector or transcript plus the relevant index surface when block matching is expected.

If the target is missing, ask for it. If scope is missing, search broadly but keep the candidate set small.

## Output Contract

Primary output is a `Grounding.Request` live note.

Use `notes/live/NNN-<topic>-grounding-request.md` in the project that owns the target index/appendix blocks. Allocate the prefix with:

```sh
agentos stdlib prefix next --project <project-root> --project-base <project-basename> --target notes/live
```

If the caller explicitly asks for no file write, return the request body inline.

Use this live-note shape:

```md
# <topic> - grounding-request

## Request.Abstract

- source: chatlas-grounding-agent
- direction: block-to-chat | chat-to-block
- status: proposed
- target-blocks:
  - `Concept.Name`
- source-chat:
  - @<hash>-<time>..<time>

## Target.Blocks

### Concept.Name

<block locator or copied current block text>

## Proposed.Grounding

### Concept.Name

### grounding

*HEAD*

- @<hash>-<time>..<time> - What this chat evidence establishes for the block.

## Appendix.History.Candidates

### Concept.Name

- @<hash>-<time>..<time> - Older useful context, superseded direction, rejection, or drift resolution.

## DRIFT.Candidates

### Concept.Name

- DRIFT: @<hash>-<time>..<time> - Why this current grounding needs alignment.

## Search.Notes

- queries tried:
- sessions inspected:
- weak or ambiguous evidence:

## Review.Notes

- accepted:
- rejected:
- needs user alignment:
```

Omit empty sections. Keep the request compact and reviewable.

## Grounding Semantics

Use the Agentos grounding model:

- `Chat.Grounding` only happens on index/appendix kernel blocks.
- `### grounding` is the standard block section.
- `*HEAD*` marks current grounding for the block.
- Multiple `*HEAD*` rows are allowed.
- Historical grounding belongs in appendix depth.
- `DRIFT:` only prefixes affected `*HEAD*` rows.
- Absence of `### grounding` is the implicit sign that a block is not grounded.
- Downstream surfaces cite grounded blocks instead of carrying first-class chat grounding.

The skill writes requests; the active index workflow or user accepts, revises, rejects, and eventually writes accepted entries.

## Workflow

1. Identify mining direction.
2. Load existing grounding requests.
3. Gather target context.
4. Query or export Chatlas evidence.
5. Inspect evidence.
6. Write a `Grounding.Request`.

### 1. Identify Mining Direction

Use **block-to-chat** when the user gives one or more blocks and wants evidence for them.

Use **chat-to-block** when the user gives a chat/session and wants design decisions mined out of it.

Chat-to-block may run in two levels:

- **L1**: identify chat places where the user added design info, made a decision, corrected direction, rejected an idea, or created drift
- **L2**: attempt to match those places to existing index/appendix blocks

Both levels produce `Grounding.Request`s.

### 2. Load Existing Grounding Requests

Before mining, search existing live notes so the agent does not repeat already-proposed grounding:

```sh
rg -n "Grounding.Request|grounding-request|@<hash>|Concept.Name|<session-id>" <project>/notes/live
```

Check especially:

- requests for the same target block
- requests for the same source chat/session
- prior rejected or weak candidates
- prior `DRIFT:` candidates still awaiting review

Do not suppress a duplicate silently; mention it in `Search.Notes` if it affects the proposal.

### 3A. Block-To-Chat: Read The Target Block

Extract:

- concept name
- fundamentals
- existing `### grounding`
- aliases or related `Dotted.Name`s
- appendix material if supplied
- likely user-language phrases from the block

Treat `Topic.Identity` as the kernel block identity. If the evidence is really for a subtopic, propose a separate block instead of forcing grounding onto the parent block.

### 3B. Chat-To-Block: Read The Chat

Export the chat/session or use the supplied transcript.

Look for user turns where the user:

- adds durable design information
- makes or accepts a decision
- corrects an agent's framing
- rejects an approach
- says something should be reused later
- marks current behavior as drift
- names or renames a concept
- explains why a block should exist or split

L1 output may stop at marked chat refs without block matches.

L2 additionally searches the index for matching blocks by concept name, phrase, and nearby terminology.

### 4A. Build Search Probes For Block-To-Chat

Start simple. Use:

- exact concept name, e.g. `Chat.Grounding`
- split name tokens, e.g. `grounding`, `Chat.Ref`, `Topic.HEAD`
- user-facing phrases from fundamentals
- likely synonyms from the current project vocabulary
- known nearby concepts

Prefer a few high-signal probes over broad noisy recall.

### 4B. Query Chatlas

Refresh only when freshness matters:

```sh
agentos chatlas update --verbose-mode=quiet --output-mode=json
```

Use basic query filters:

```sh
agentos chatlas query --message-contains "<term>" --sort newest --limit 20
agentos chatlas query --user-contains "<term>" --sort newest --limit 20
agentos chatlas query --project <path> --message-contains "<term>" --sort newest --limit 20
agentos chatlas query --project-base <name> --message-contains "<term>" --sort newest --limit 20
agentos chatlas query --ref "@<hash>-<time>"
```

Useful filters:

- `--project` or `--project-base` when grounding is project-local
- `--provider` when the caller knows the provider family
- `--active-after` when recency matters
- `--min-user-turns` to avoid tiny sessions
- `--field session_id` or `--field identity_hash` for compact follow-up

Do not use vector search in this first workflow. Do not treat failed search as proof that no grounding exists.

### 5. Export Candidates

Export only a small candidate set.

```sh
agentos chatlas export --session-id <id> --view transcript --format json
agentos chatlas export --identity-hash <hash> --view transcript --format json
agentos chatlas export --ref "@<hash>-<time>..<time>" --view transcript --format json
```

Use `--view user` when user turns alone are enough. Use `--view full` only when tool calls, metadata, or assistant context are materially needed.

### 6. Inspect Evidence

Prioritize evidence in this order:

1. user turns that explicitly settle, correct, reject, or refine the block
2. user turns that imply a stable preference or requirement
3. assistant turns accepted by the user or needed to understand the user decision
4. assistant-only material as weak context, not authority

Select a ref only when it changes future judgment about the block.

Classify candidates:

- `HEAD`: current user/agent view for the block
- `history`: older useful evidence for appendix depth
- `DRIFT`: current `HEAD` evidence needs alignment discussion
- `weak`: related but insufficient evidence; report in notes, do not propose as grounding

### 7. Write The Grounding Request

For each proposed row, include:

- direct `Chat.Ref`
- one short evidence note
- whether it belongs in block `### grounding` or appendix history
- any ambiguity that affects acceptance

Use direct, block-shaped language. Do not summarize whole transcripts.

Write one request file by default. If mining one chat session with many decisions, one request per chat session is acceptable. If mining a large block batch, one request per block is acceptable when it improves review.

Return the request path and a short summary. Do not paste the whole request unless asked.

## Ref Construction

Use Chatlas `Chat.Ref` form:

```txt
@<identity-hash-prefix>-<timetag>
@<identity-hash-prefix>-<timetag1>..<timetag2>
@<identity-hash-prefix>
```

Prefer a range when the evidence spans several turns. Prefer the smallest range that preserves context. Use session-level refs only when the whole session is the meaningful evidence.

## Boundaries

This skill does not:

- write index or appendix files
- decide stable index wording
- decide final grounding authority
- define what every workflow must do when it sees grounded blocks
- add a grounding state taxonomy
- require or design vector search
- claim absence of search hits means absence of user intent

## Failure Shapes

No target:

```text
Cannot mine grounding: no target block or source chat was provided.
Provide either:
- a kernel block for block-to-chat mining
- a session selector, Chat.Ref, or transcript for chat-to-block mining
```

No candidates:

```text
No grounding candidates found with the searched Chatlas probes.
This does not prove the block has no grounding; it only means this pass found none.
Queries tried: ...
```

Ambiguous candidates:

```text
Found related chat evidence, but not enough to propose `*HEAD*`.
Candidate refs:
- @... - why it is related but insufficient
```
