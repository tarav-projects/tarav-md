# Index Curation Session - tail summary

Summary of the last ~5h of Codex session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`
(`2026-08-17T16:36Z` → `21:39Z`, project `taravangian-project`).

Continuous design discussion on the semantics and mechanics of the Hugentics `Index`.
Nothing was implemented except one capture: `629-index-curation-model-design-session.md`.

## Arc

1. **Naming the grouping** — started from `Index.Narrative` (grouping several line
   expressions of the same atomic assertion). Rejected as over-suggestive: it sounded like
   a graph relating lines. Passed through `Index.Proposition` and `Line.Trace`, landed on
   **`Line.History`** — the git analogy is the right semantics: the full history of a line,
   with a `HEAD.Line` as current expression.
2. **Decoupling skin from support** — a history separates the line *wording* from its
   *support*. Condensing or rewording `HEAD` does not require relinking support, and does
   not discard prior editions.
3. **The Index is mutable** — the git analogy breaks here: histories are *not* immutable.
   Lines can be added, removed, regrouped. `Chat.Surfaces` are the immutable append-only
   SSOT; the `Index` is a `WIP.Surface` — a current interpretation that converges over past
   chats, and git records the Index's own edit history *outside* the semantic model.
4. **Identity envelope** — because the Index is WIP, Index entities are *not* content
   addressed. Agreed envelope: `id` (random, from an identity provider), `hash` (content
   descriptor, for drift detection / POI surfacing), `label` (public). Mechanical records
   and references carry a hash purely to surface drift.
5. **Amendment vs. evolution** (stress test 1) — fixing a badly extracted `LineA` is *not*
   part of the line's semantic history. Same `Line.id` may appear in several `Chat.Index`
   surfaces; a mechanical correction is just an edit, and git records it. No
   `produced_in` / `correction_support` / "correction line" machinery. Contrast with a
   genuine rename supported by the user at both times — that *is* history (`LineA` → `LineB`
   as `HEAD`).
6. **Where does a line land?** (the recursion) — indexing happens *in chats*, so an index of
   an old `ChatA` is produced in a new `ChatB`. Explored making `Chat.Index` a pure
   append-only production ledger of the lines produced in that chat; rejected forcing a chat
   to write its own ledger as too heavy a workflow inheritance. Settled: the line lands on
   the indexing chat's `Chat.Index` (`ChatB.Index`), and `ChatA` is reachable through the
   support set — plus lines may also be located against any `User.Turn` that supports them.
7. **Landing vs. verbatim** — a verbatim line in a chat is only a *candidate*; a line is
   "landed" when it has a record. This is what makes `Chat.Index` mechanically auditable.
8. **Curation** (the key turn) — the Index must contain only semantically correct, correctly
   attached, correctly typed lines. Three dispositions:
   - incorrect extraction → **remove** (git preserves the mistake),
   - valid earlier expression → keep as **`Tail`**,
   - current valid expression → **`HEAD`**.
   `HEAD`/`Tail` is *current vs. earlier validity*, never correct vs. incorrect.
9. **Capture** — `$tarav-hugentics --capture --design-session` landed
   `629-index-curation-model-design-session.md`: 14 typed user-grounded lines in four
   blocks, all Chatlas2 anchors `MATCHED`, Chat.Index backpropagation clean.
10. **Back to mechanics** — how to satisfy those principles with a convenient workflow.

## Settled model

```text
Chat.Support     immutable User.Turn authority
Index            mutable WIP interpretation
Line.Type        defines qualifying touched data
Line.History     HEAD.Line (current valid) + Tail.Lines (earlier valid user states)
Bad.Indexing     curation finding — excluded from the semantic model
Git              external history of Index construction and mistakes
```

Index goals: **completeness** (all qualifying touched data), **fidelity** (every retained
line faithful to its support), **contextual usefulness** (`HEAD` for fast Design.Model
discovery, `Tail` + support for depth).

Curation operations: add missing lines, correct wording or support, remove incorrect
interpretations, group genuine editions into histories, promote current edition to `HEAD`,
preserve earlier editions in `Tail`, split histories that describe different facts.

## Mechanics — where the session ended

First proposal: make `Line.History.Record` the single canonical content-bearing WIP object,
with everything else a rebuildable projection.

```text
Chat.Support                      immutable authority
        ↓
Line.History.Record               canonical curated Index
  id / hash / label
  HEAD.Line + support
  Tail.Lines[] + support
        ↓
Project.Index.HEAD / Chat.Index   convenient agent views
```

Final refinement (accepted, last two turns): **no single absolute owner**. The Index is an
*eventually coherent family of WIP surfaces*, each with a distinct role:

- `Native.Index.Surfaces` / `Skw.Annotated.Surfaces` — selected `HEAD` lines in their useful
  product scope.
- `Chat.Index` — the complete curated materialization: `HEAD` and `Tail` content, no
  `Bad.Indexing`.
- `Touched.Index.Record` — the coordination layer: identities, hashes/drift, history
  membership, `HEAD` selection, support sets, surface occurrences.
- `Project.Index` — self-documenting surface *and* the registry of `Index.Block` scopes.

`Index.Block` stays essential: the line is the atom of touched-data indexing, the block
supplies the scope in which the atom means something.

"Sync" does not mean identical content everywhere. Temporary incoherence is *normal* for a
WIP surface — untyped/ungrounded project lines, grounded lines without a `HEAD` placement,
wording drifted from record hash, stale materializations — and reconciliation discovers and
repairs these as POIs. Multiple entry paths are supported rather than one strict workflow:

```text
Project line → type/ground → record → Chat.Index
Old chat     → extract → Chat.Index → record → optional Project HEAD
Product annotation → record → Chat.Index
Record audit → repair whichever surface drifted
```

Shared invariant (not workflow order):

> Every retained semantic line is correctly typed, scoped by an `Index.Block`, supported by
> qualifying `User.Turn`s, represented in its `Touched.Index.Record`, and materialized in
> `Chat.Index`; selected current lines may additionally appear on Native or Skw HEAD
> surfaces.

## Open / next

- ~~The last exchange was accepted with "capture on the design-sessions" — a second capture
  covering the multi-surface mechanics was requested.~~ Done: landed as
  `Index.Surface.Family`, `Index.Block.Scope`, and `Index.Surface.Coherence` in `629`.
- Line identity mechanics vs. anchor records (anchor `label` etc.) discussed but not closed.
- How a line is recognized as *landed* when reading a chat (candidate detection, no regex
  extraction) remains partly open.
- `626-index-narrative-identity-design-req.md` is superseded prior provenance; left
  unchanged on purpose.
