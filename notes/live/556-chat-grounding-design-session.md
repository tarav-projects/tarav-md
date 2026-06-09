# Chat.Grounding - design-session

## Session.Abstract

Design `Chat.Grounding`: a citation and context-injection mechanism that lets agents ground index and appendix blocks in prior user/agent chat interactions.

Chats are the SSOT for user/agent interaction. `Chat.Grounding` makes selected prior chat context traceable from index/appendix blocks, so later agents can inspect the interaction that established a requirement, preference, decision, concern, contradiction, or alignment resolution.

Current status: core design promoted to the Agentos package index. Retrieval and search are related but secondary: retrieval finds candidate evidence; grounding is the selected authoritative context cited by kernel block grounding sections and injected through those blocks into downstream work.

## Design.Index

### Chat.Grounding

- `Chat.Grounding` is a context-injection and citation responsibility over index/appendix blocks.
- It grounds a `Kernel.Block:Index` or `Kernel.Block:Appendix` in prior user/agent chat interactions.
- It improves downstream work quality by connecting cited concepts to actual recorded user/agent alignment evidence.
- It is an `Alignment.Mechanism`: it helps agents preserve user intent, recover prior decisions, and detect drift.
- It has sequential semantics: more recent grounded chat about a topic is treated as the current view.
- Lack of grounding is not by itself sufficient reason to stop a job.
- Lack of a `### grounding` section is the implicit sign that a block is not grounded.
- Grounding is strongest when recent, relevant chat evidence supports the current claim or decision.
- Grounding remains useful while the cited chat context is still current; stale or problematic current grounding becomes an alignment issue, not silent truth.

#### appendix

- The core user framing: "Chats are the SSOT of User/Agent interactions."
- Grounding is not merely "this was influenced by chat"; it is a traceable relationship from a kernel block back to the chat context that supports it.
- The mechanism should let future agents inspect the larger surrounding conversation, not just a quote-sized snippet.
- The responsibility is intentionally concentrated on the index/appendix system.
- Other surfaces benefit from grounding by citing grounded kernel blocks, not by carrying first-class chat grounding themselves.
- Surfacing grounding drift is productive because the resolution happens in chat and creates new `Chat.Surface` evidence for the topic.
- Grounding does not need a state taxonomy; only material grounding problems need an explicit marker.

#### meta

- status: promoted to package index
- promotion: core blocks promoted to `skills/agentos-pkg/index/100-index.md`, `102-index.md`, `103-index.md`, `105-index.md`, and `appendix/Index.Architecture-appendix.md`

### Chat.Surface

- `Chat.Surface` is the recorded surface of direct user/agent interaction.
- It is a `Stable.Surface`, but append-only.
- It is emit-driven and append-only: chat turns are produced by interaction and later superseded, not edited.
- It is the SSOT for user/agent alignment evidence: what was said, accepted, corrected, rejected, overwritten, and when.
- User turns are primary alignment signal; assistant turns provide context, reasoning trace, and forensic detail.
- Index and appendix blocks should cite chat when the chat materially supports a decision, preference, requirement, or concern.

#### appendix

- Chats are long, scattered, and numerous; this makes retrieval important, but does not change the grounding definition.
- Chat evidence can be richer than durable notes because it preserves the discussion around how the conclusion emerged.

### Chat.Ref

- `Chat.Ref` is the minimal addressable citation primitive for `Chat.Surface`.
- A `Chat.Ref` identifies a session, a time window, or a range of time windows on a chat tape.
- Current preferred shape: `@<hash>-<time>` for a point/window and `@<hash>-<time>..<time>` for a range.
- The address is separate from the readable annotation that explains what the ref establishes.
- Refs should be easy for agents to write, copy, resolve, and display in documents.

#### appendix

- Existing package index wording defines `@<hash>-<timetag>` where the hash is an `identity_hash` prefix and the timetag is ISO 8601, truncatable to any precision.
- Session-level refs may use `@<hash>` when the whole session is the intended citation target.
- Exact turn-level citation may require a stricter `Turn.Ref` or `Chat.Turn.Ref`; this is open.

#### meta

- open: whether MVP `Chat.Ref` is sufficient or a stricter exact-turn primitive is needed

### Kernel.Block:Grounding

- `Kernel.Block:Grounding` is the standard grounding section of a kernel block.
- It is the block-local expression of a `Chat.Grounding` relationship.
- It sits alongside fundamentals, `### appendix`, and `### meta` as a normal block section.
- Its canonical heading is lowercase `### grounding`.
- It groups `Grounding.Entry` rows by grounding role.
- The `*HEAD*` group marks the active current grounding for the block.
- Multiple rows may be marked as `*HEAD*` when several chat refs jointly define the current view.
- Historical grounding belongs in appendix depth where it can accumulate without compressing the index block.
- Grounding wording should describe the supported block claim, not summarize the whole chat.

#### appendix

Block-local form:

```md
## Concept.Name

...

### grounding

*HEAD*

- @<hash>-<time>..<time> - One sentence explaining what this current chat evidence establishes.
```

Downstream surface form:

```md
Current claim or decision cites `Concept.Name`; `Concept.Name` carries the chat grounding.
```

### Grounding.Entry

- `Grounding.Entry` is one citation row inside `### grounding`.
- It resolves to one direct `Chat.Ref`.
- It includes a short evidence note explaining what the cited chat establishes for the block.
- Its grounding role comes from the group it appears under.
- `*HEAD*` entries identify active chat evidence still considered current for the block.
- Historical entries are placed in the block's appendix surface, not in compressed index grounding.

#### appendix

- A block may have multiple `*HEAD*` rows when the current view is assembled from several recent or complementary chat refs.
- A block may have no `*HEAD*` rows when it is intentionally ungrounded, not yet researched, or current grounding has not been found.
- Historical grounding is important because it shows evolution, rejected directions, and superseded alignment.
- Appendix placement lets grounding history accumulate freely without overloading the index block.
- The role grouping is visual and lightweight; it does not introduce markdown heading depth inside `### grounding`.

### Grounding.History

- `Grounding.History` is accumulated older chat evidence for a grounded topic.
- It belongs in the topic's appendix surface.
- It preserves alignment evolution, rejected directions, superseded views, and drift resolutions.
- It does not override `*HEAD*` grounding in the index block.
- It can grow freely under appendix constraints.

#### appendix

- `Grounding.History` may use the same `Grounding.Entry` row shape as `*HEAD*`.
- A future appendix convention may use a dedicated `### grounding` section with `*history*` grouping.
- History placement follows `Natural.Placement`: current compact signal in the index block, accumulated depth in appendix.

### Grounding.DRIFT

- `Grounding.DRIFT` is an explicit marker that a grounded block needs alignment discussion.
- It only marks `*HEAD*` grounding rows.
- It signals that alignment must be performed on this block/grounding.
- It does not encode the drift reason; the evidence note carries the reason.
- It does not resolve the issue; it marks the need for chat alignment.
- Its canonical form is a `DRIFT:` prefix on the affected `*HEAD*` row.
- The resolution happens on `Chat.Surface`.
- After discussion, the resulting chat can become the new `*HEAD*` grounding.

#### appendix

- `DRIFT` is intentionally a marker, not a full state taxonomy.
- Lack of grounding remains implicit through absence of `### grounding`.
- The marker should be used only when a material grounding issue has been noticed.
- `DRIFT:` can appear under `*HEAD*` because the latest known view may still be the problematic one.
- `DRIFT:` should not be used for history entries; history carries context in the note.
- Example shape:

```md
### grounding

*HEAD*

- DRIFT: @<hash>-<time>..<time> - Current view conflicts with implementation behavior.
```

### Grounding.Context.Injection

- `Grounding.Context.Injection` is the act of selecting authoritative prior context and making it available through grounded kernel blocks.
- The citation is the durable pointer; the injected context is what improves the current agent's reasoning.
- Injection may happen when an agent loads a grounded index/appendix block during drafting, review, implementation planning, implementation execution, or drift investigation.
- The injected context should be relevant enough to affect judgment, not merely adjacent.
- Grounded blocks should make prior work reusable without requiring the user to re-explain settled context.

#### appendix

- "Ask the user" remains the best source when the user is present and the issue is unsettled.
- "Check previous work" is the reusable path when the needed alignment evidence already exists in chats.
- The system should support both: use prior chat grounding when possible, and ask the user when evidence is missing, stale, or contradictory.

### Topic.Identity

- `Topic.Identity` is kernel block identity in the index/appendix system.
- A grounding topic is a `Kernel.Block:Index` or `Kernel.Block:Appendix` subject.
- If a subtopic inside a block needs independent grounding, it should become its own kernel block.
- `Topic.HEAD` is scoped to one grounded kernel block topic.
- Other surfaces cite grounded blocks instead of inventing separate grounding topics.

#### appendix

- This makes topic identity explicit through existing `Dotted.Notation`, routing, appendix discovery, and block maintenance properties.
- It prevents grounding from becoming scattered across arbitrary documents.
- It is not limiting: any surface can create or cite a block for the concern it needs grounded.
- Grounding concentration uses the existing index/appendix system as the natural home for curated conceptual claims.

#### meta

- status: user-settled direction

### Grounding.Retrieval.Boundary

- Retrieval is how an agent finds candidate chat evidence.
- Grounding is the selected evidence relationship that current work accepts and cites.
- Retrieval quality affects grounding quality, but retrieval mechanics are not the definition of grounding.
- Search engines, vector databases, keyword indexes, and session queries are candidate-discovery mechanisms.
- Grounding does not depend on a specific retrieval backend.

#### appendix

- Future retrieval work must account for long, scattered chats and many sessions.
- Machine constraints matter for retrieval design; the user's current machine has limited RAM, so vector storage and embedding choices must be modest.
- Retrieval should be designed as a separate concern so `Chat.Grounding` does not depend on one search backend.

### Topic.HEAD

- `Topic.HEAD` is the most recent grounded chat view for a topic.
- The topic is the identity of a grounded index/appendix kernel block.
- It is the grounding anchor for the block's current user/agent alignment state.
- Drift is measured against `Topic.HEAD`, not against every older grounded chat.
- Older grounded chats remain useful history, but do not override the current view.
- When a current view is problematic, the topic has an alignment problem even if it is the latest view.
- `Topic.HEAD` can be updated by finding a more recent grounded chat or by discussing the topic again in chat.

#### appendix

- Sequential semantics makes grounding closer to a maintained branch head than a timeless citation set.
- A contradiction with old chat may simply show legitimate design evolution.
- A contradiction with `Topic.HEAD` means the grounded block or a downstream surface citing it is out of alignment with the topic's latest known user/agent state.
- If the latest known state is itself bad, ambiguous, or incomplete, the drift is between the system's needs and the current topic head.
- Surfacing this produces the next alignment chat, which can become the new `Topic.HEAD`.

### Grounding.Alignment.Drift

- `Grounding.Alignment.Drift` occurs when current work contradicts `Topic.HEAD`.
- It also occurs when `Topic.HEAD` itself is problematic for the current concern.
- Drift is surfaced to the user or routed into an alignment workflow; it is not silently resolved by the agent.
- `DRIFT` marks the need for that discussion in the grounded block.
- If alignment produces a new resolution in chat, the new chat can become the updated grounding source.
- Stale or contradictory grounding is an inter-surface alignment problem.
- Grounding makes drift easier to detect because claims have traceable evidence.

#### appendix

- Example class: implementation behavior contradicts the most recent grounded user decision.
- The correct response is not "stop all work"; it is to surface the contradiction and align the issue with the user when material.
- Drift always has two first-class resolution paths: find a more recent `Topic.HEAD`, or create a new one through chat alignment.

### Grounding.MVP

- MVP concept surface: `Chat.Grounding`, `Chat.Ref`, `Topic.Identity`, `Topic.HEAD`, `Kernel.Block:Grounding`, `Grounding.Entry`, `Grounding.DRIFT`, `Grounding.History`, and `Grounding.Context.Injection`.
- MVP block convention: grounded index/appendix blocks carry a standard grounding section with direct `Chat.Ref`s and one-sentence evidence notes.
- MVP behavior: agents ground kernel blocks when relevant chat evidence is available and proceed responsibly when it is not.
- MVP retrieval path can use existing `agentos chatlas` query/export surfaces before adding vector search.
- MVP success means future agents can trace a kernel block back to the chat context that established it, then cite that block from downstream work.

#### appendix

- Implementation should first make the reference convention usable in index/appendix blocks.
- Search sophistication is useful but should not block the grounding convention.
- A later implementation pass can add tooling for resolving refs, exporting cited windows, validating refs, and assisting citation insertion.

## Session.Notes

Open / unresolved:

- Exact ref granularity: whether `Chat.Ref` ranges are enough, or whether exact turn IDs are required.
- Appendix history shape: exact convention for historical grounding entries in appendix depth.
- Authority language: how strongly a grounding citation should constrain implementation when evidence is old, partial, or ambiguous.
- Tooling path: whether initial support should live in Chatlas CLI, Agentos markdown workflows, editor helpers, or all three.
- Retrieval path: keyword/session query first, then modest vector search if it fits local resource constraints.
- Index promotion: revise the existing `Chat.Grounding` block only after the design session settles exact wording.

## Session.Log

- 2026-06-08 12:39 CDT: session opened as artifact-backed `What.Design.Session`. Seeded initial `Design.Index` blocks from current chat discussion and existing Agentos package concepts.
- 2026-06-08: revised blocks from user review. Added sequential semantics, `Topic.HEAD`, stable append-only `Chat.Surface`, and drift resolution paths.
- 2026-06-08: user settled topic identity and scope. `Chat.Grounding` only happens on index/appendix kernel blocks; other surfaces cite grounded blocks.
- 2026-06-08: user settled block shape. Grounding is a standard kernel block section, alongside fundamentals, appendix, and meta.
- 2026-06-08: user settled canonical grounding section heading as lowercase `### grounding`.
- 2026-06-08: user settled grounding entry grouping. `### grounding` uses emphasized groups such as `*HEAD*`; multiple `*HEAD*` rows are allowed.
- 2026-06-08: user moved historical grounding to appendix depth so history can accumulate without overloading compressed index blocks.
- 2026-06-08: user rejected grounding state taxonomy. Lack of grounding is implicit by absence of `### grounding`; only `DRIFT` is explicit.
- 2026-06-09: core design promoted into the Agentos package index. Linter passed for `skills/agentos-pkg/index` and `skills/agentos-pkg/appendix`.
- 2026-06-08: user settled `DRIFT:` as a row prefix, not a role group.
- 2026-06-08: user constrained `DRIFT:` to `*HEAD*` rows only. Reason lives in the evidence note; marker only signals that alignment must be performed.
