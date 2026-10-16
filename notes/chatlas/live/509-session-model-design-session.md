# Session.Model - design-session

## Session.Abstract

- **Intent:** Revisit and redesign `Chatlas.Session.Model` — the standard with which Chatlas represents any session's information.
- **State:** Active — spine settled and promoted to the Chatlas index (`Chatlas.Session.Model`, `Session.Event.Tape`, `Session.Lineage`, `Session.Model.Map`); now working the neutral-concept queue.
- **Scope:** The content-representation layer: events, messages, tool/model/usage/reasoning, normalization contract. NOT identity/index/views (already live).
- **Settled:** Chatlas-local, one-way normalization. Providers know nothing about the model; Chatlas normalizes their formats inward. Provider formats are inspiration, not an input contract.
- **Inspiration:** PI session model (typed JSONL tree: messages, compaction, branching, forks, labels, extension slots).
- **Source material:** archived `006-Session.Model`, `007-Chatlas.Standard.Model.Contract`, `102-Agentos.Agent.Model`.
- **Target surface:** `tarav-chatlas-pkg` index (promotion is follow-on, not this session).
- **Next:** Decide which provider-native concepts survive normalization into the model.

## Design.Index

### Chatlas.Session.Model

- `Chatlas.Session.Model` is the standard with which Chatlas represents any session's information
- provider-neutral: one model normalized inward from many provider-native session formats
- directionality: Chatlas knows provider formats and normalizes them into one; providers know nothing about this model
- producer: `Chatlas.Normalizer.<Provider>` is the only writer — there is no provider-side conformance
- provider-native formats are *inspiration* for the model's expressiveness, not an input contract it must accept
- not overfitted to any single provider — the model carries no provider-named canonical fields
- expressive enough to represent most of what a provider provides — each provider's real content maps into a neutral concept the model defines
- provider-specific richness with no neutral concept lives in `native` / `source_refs` — recoverable, never canonical
- consumers are read-side: search, summary, replay, UI, `Chatlas.View.Model`

#### meta

- renamed `Session.Model` → `Chatlas.Session.Model` (Chatlas-owned concept)
- settled: scope is Chatlas-local normalization output, not a general provider-writable standard
- settled (rule for survival): a provider concept survives canonically iff it maps to a neutral concept; otherwise it goes to `native`/`source_refs`
- open: the concrete neutral concept set (compaction, sub-agent lineage, attachments, fork lineage, labels…) — designed per concept in later questions

****

### Session.Event.Tape

- `Session.Event.Tape` is the canonical structure of a `Chatlas.Session.Model` — an append-only, ordered ledger of typed events
- the tape is the single source of truth; every higher-level view of the session is a projection derived from it
- one event captures one thing that happened in the session
- an event carries its identity, its order, its kind, who produced it, its content, and a link back to raw evidence
- projections are derived and disposable — rebuildable from the tape, never authoritative on their own

#### meta

- settled: the canonical spine is an event tape, not a message-centric model (evidence: archived `007` chose `events[]` as canonical ledger; PI stores an append-only entry log)
- open: linear tape vs tree — PI's log branches (`parentId`); a normalization output may only need linear visible history
- open: exact event-kind vocabulary (deferred to a later question)

****

### Session.Lineage

- the canonical tape is linear-chronological — the order events were recorded, not a branching tree
- branching and forking are represented as event-level lineage references on the linear tape
- an event may reference a prior event as its origin; the tree is a projection derived from those references, never the spine
- the active/visible path is the default read; abandoned branches stay on the tape as preserved evidence

#### meta

- settled: linear-chronological spine; lineage as event metadata; tree is a derived projection (evidence: `007` linear `events[]`; PI stores append-only chronological and derives its tree from `parentId`)
- open: compaction and cross-session forks handled separately (later questions) — this block is only the linear-vs-tree spine decision

****

### Session.Model.Map

- `Session.Model.Map` is a per-provider document mapping a provider's native session concepts/fields to `Chatlas.Session.Model` neutral concepts
- one file per provider: `tarav-chatlas-pkg/references/session-model-map-<provider>.md`
- the neutral side is a controlled vocabulary — only `Chatlas.Session.Model` concept names defined in the index
- one-directional: the index defines the neutral concept (SSOT); the map records the native→neutral path and never redefines it
- records only non-obvious mappings — an obvious native↔neutral correspondence needs no line
- each mapped line carries its rationale and the survival decision: the native concept resolves to a neutral concept or to `native`/`source_refs`
- decision-and-rationale-centric, not a field-by-field restatement of the normalizer code — that is redundant placement and drifts
- a native concept with no neutral mapping (`TBD`) is an open gap — the live question queue for `Chatlas.Session.Model` design
- the shared neutral vocabulary makes the cross-provider slice pivotable: one neutral concept, every provider's source for it
- a current-truth document — kept honest by re-checking against provider source and the raw archive; git holds history, no version metadata

#### meta

- settled and promoted to the Chatlas index; the per-provider map files are the durable form of the neutral-concept question queue

## Session.Notes

- Neighbor blocks to cite: `Session.Identity`, `Session.Set`, `Chatlas.Session.Index`, `Chatlas.View.Model`, `Chat.Surface`/`Chat.Ref`.
- The live Chatlas index holds the identity, indexing, and view layers; the content-representation layer was never promoted — this session fills that gap.

### Neutral-concept question queue

Candidate neutral concepts surfaced by cross-provider clustering of the Codex/Claude normalization audits (chatlas-py notes 517/518). Each is one design question under the survival rule: design a neutral concept, or send to `native`. Worked one at a time.

- **Compaction** — Codex `compacted`/`compaction` items; Claude `compact_boundary` / `isCompactSummary`. Is there a neutral compaction event, and what does it carry (summary, replaced span)?
- **Sub-agent lineage / provenance** — Codex `agent_nickname`/`agent_role`/`agent_path`, `parent_thread_id`; Claude `isSidechain`/`agentId`/`teamName`. Neutral concept for sub-agent / sidechain turns?
- **Fork lineage** — Codex `forked_from_id`; PI session forks. Neutral cross-session fork reference? (relates to `Session.Lineage`)
- **Attachments / non-message content** — Claude `attachment` records; Codex `input_image` in messages. Neutral attachment/non-message-content concept?
- **Tool-call taxonomy** — Codex `local_shell_call`/`web_search_call`/`image_generation_call`/`custom_tool_call`. Neutral tool-kind taxonomy vs one generic tool-call?
- **Reasoning visibility** — Claude `redacted_thinking`; Codex `encrypted_content`. Neutral reasoning-visibility states?
- **Usage** — both providers carry structured per-turn token usage. Neutral usage concept and its scoping honesty.
- **Session metadata** — `cwd` / git branch / harness version / entrypoint. Neutral session-metadata slot?

## Session.Log

- 2026-06-15: Session opened. Scope: `Session.Model` content-representation redesign, PI as inspiration.
- 2026-06-15: Renamed subject to `Chatlas.Session.Model`. Settled scope: Chatlas-local one-way normalization; providers know nothing about the model. Captured foundational block.
- 2026-06-15: Settled canonical spine — `Session.Event.Tape` (event ledger + derived projections), not message-centric. Captured block.
- 2026-06-16: Settled `Session.Lineage` — linear-chronological tape; branching/forking as event-level lineage metadata; tree is a derived projection. Captured block.
- 2026-06-16: Captured neutral-but-expressive rule into `Chatlas.Session.Model` (no provider-named canonical fields; provider content maps to neutral concepts or goes to native). Resolved the "which concepts survive" open into a survival rule. Surfaced from the Codex/Claude normalization audits (notes 517/518 in chatlas-py).
- 2026-06-16: Added neutral-concept question queue to `Session.Notes` — 8 cross-provider candidates (compaction, sub-agent lineage, fork lineage, attachments, tool taxonomy, reasoning visibility, usage, session metadata) derived from the audit GAPs. To be worked one at a time.
- 2026-06-16: Designed `Session.Model.Map` (per-provider native→neutral mapping surface, one-directional, controlled vocabulary, current-truth). Promoted the spine (`Chatlas.Session.Model`, `Session.Event.Tape`, `Session.Lineage`, `Session.Model.Map`) to `tarav-chatlas-pkg/index/100-index.md` + routing.
