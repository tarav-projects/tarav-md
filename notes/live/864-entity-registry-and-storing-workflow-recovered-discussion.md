# Entity Registry and Storing Workflow — recovered discussion

Status: provisional dialogue recovery, not an approved architecture or implementation request.

## Why this note exists

The discussion moved from the storage cost of Ranking records to reusable Tarav storage primitives. This note preserves the user's design direction and the questions still open, so the conversation can resume without reconstructing it from a long session.

Source: Codex Chatlas session `01a0d86c-9538-7be1-af96-014cd4203d61`. The turn hashes below are exact Chatlas `Chat.Turn` identifiers; the timestamps are UTC. To retrieve a turn, run `tarav chatlas query --session-id 01a0d86c-9538-7be1-af96-014cd4203d61 --turn-hash-prefix <prefix>`.

## Conversation recovered

1. **Storage pressure.** The user asked how much Ranking's Case, Pair, and Judgment records duplicate, and where their storage footprint lands (`a5ca6acd92480f49`, 2026-10-07 15:18:57). They then proposed retaining what cannot be derived, avoiding copies of complete Cases in Pair records, and identifying relevant code through hashes or Git commits where useful. Git behavior should come from shared Git primitives (`6178e3163610f0bd`, 16:06:43).
2. **Entity records and references.** An Assertion may currently be transient, yet another workflow may want to retain it. The user proposed a general `EntityRegistry` capability: store Entity Records once, let workflows reference them, and make it possible to detect changes or refer to a particular Git edition. Starting with `TaravEntity` identities was offered as a possible first scope, not a permanent limit (`acf235c2a23069c8`, 16:18:04).
3. **Registry is a repository, not merely a reference index.** The user corrected an interpretation of `EntityRegistry`: an implementation is itself a Git repository containing the Entity Records. References point into it—to a current object or a particular edition. The records are stored as records, not replaced by references (`3692edc41054d2a2`, 16:24:21).
4. **Shared Storing foundation.** The user asked whether `EntityRegistry` might specialize the Record Archive, but the larger aim was to unify older storage facilities under a `StoringWorkflow`. It could supply record-based, data-structure-like primitives (map/dictionary-like and vector/list-like), with Git and References integration. Archive, Registry, and other workflows could use the primitives while choosing central Tarav storage or their own repositories (`31877c8b70798bc3`, 16:36:21).
5. **Typed reference precision.** The user rejected treating committed `HEAD` as the only way to read a registry. An ordinary file/path reference, a Git `HEAD` reference, and a reference to a particular edition can express different relationships. The design should find clear Types, names, and Workflow ownership for those semantics; the exact `HEAD` contract still needs definition (`b9d08c02ed3cb153`, 16:39:45).

## Working direction, not yet a decision

Use a common storage vocabulary so workflows can share mechanisms without surrendering their own storage semantics. `EntityRegistry` is a candidate Git-backed store of Entity Records; consumers pass typed references to records instead of each duplicating identity snapshots. References must say whether they follow a mutable file, a repository's current state, or an immutable edition. A registry's physical location and ownership need not be global.

Open design questions: what is truly common beneath Archive and Registry; whether the present Record Archive can be specialized directly or needs extracted primitives first; how Entity IDs map to record paths and editions; the exact behavior of `HEAD` versus working-tree reads; and which information must remain frozen in a Ranking trial even when other data is derivable. These are questions to investigate, not contracts established by this note.
