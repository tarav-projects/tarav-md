# Compaction Boundary Event — issue

## Session.Abstract

- **Type:** Issue / gap report — proposes a first-class compaction event on the `Session.Event.Tape`.
- **Intent:** The Chatlas standard model preserves all conversation content but discards the provider compaction *boundary*, the one structural fact needed to reason about a session's persisted-thread shape.
- **State:** Open — grounded, not yet designed.
- **Scope:** `Chatlas.Session.Model` content layer — a new event kind + its `Session.Lineage` linkage. NOT identity/index/views.
- **Related:** `509-session-model-design-session.md` already lists compaction as an open neutral concept ("compaction, sub-agent lineage, attachments, fork lineage, labels…"); this issue supplies concrete grounding evidence for it.
- **Affects blocks:** `Session.Event.Tape`, `Session.Lineage`, `Chatlas.Session.Model` (`tarav-chatlas-pkg/design/100-design.md`).

## Motivation

A user hit a Codex TUI backtrack error — `Failed to branch before the selected prompt: the selected prompt was not found in the persisted thread` — on a fork+compacted thread (session `019f9910-2823-7ad2-a89e-be08084e11cf`). Diagnosing it required the compaction boundaries, which the standard model does not carry. Chatlas is faithful to the *conversation* but cannot currently represent *what happened structurally* around compaction.

## Evidence

Grounded on session `019f9910-2823-7ad2-a89e-be08084e11cf` (Codex, `agentos-project`). Raw rollout vs. materialized `events` view (`agentos chatlas views inline --view events`):

- Raw rollout carries **4 `compacted` records** (2 inherited at fork time, 2 real: 12:30Z, 13:59Z) and **3 stacked `session_meta`** (a thread forked from two ancestors).
- In the standard model: all 3 forks survive as `session.start` events; all user/assistant turns survive verbatim; abandoned-branch duplicate prompts are preserved (`Session.Lineage` working as designed).
- **None of the 4 `compacted` raw records back any tape event** — verified by source-ref line tracing. There is no compaction event kind.
- Each `compacted` record carries a `replacement_history` array. Inspected: it is a **verbatim re-listing of prior user/developer messages, with no distinct summary text** — every prompt in it already exists as a real `message` event on the tape. So dropping the payload loses **no conversation content**; it loses only the boundary fact.

**Conclusion:** zero semantic conversation loss; one structural fact lost — *where* compaction happened and what the persisted thread retained at that point.

## Proposal

Introduce a first-class compaction event on the `Session.Event.Tape`:

- a new event kind (e.g. `context`-family `compaction`, or a dedicated `lineage.compaction`) recorded at each provider compaction boundary
- carries: boundary timestamp, `source_refs` back to the raw `compacted` record, and the identity of the turns the post-compaction persisted thread retained (the `replacement_history` roster as references, not copied bodies)
- linked through `Session.Lineage` so the boundary sits on the linear tape as preserved structural evidence, consistent with how abandoned branches are already kept
- **do not** canonicalize the redundant `replacement_history` message bodies — reference the existing tape events instead

## Non-goals

- Not fixing the Codex backtrack bug (that is provider-side).
- Not persisting compaction summary *text* as canonical (Codex's compaction here has none; other providers may — handle per-provider in the normalizer, route unmapped richness to `native`/`source_refs`).

## Open questions

- Event family: reuse `context` vs. a dedicated lineage kind?
- How to represent the retained-turn roster — event-id references vs. a positional cut marker on the tape?
- Do inherited (fork-time) compaction boundaries and in-session compactions get the same event, or a distinguishing subtype?
