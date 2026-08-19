# Index Curation Model - design-session

## Session.Abstract

- **topic** — redefine the Index as a mutable curated interpretation of immutable `Chat.Support`, with semantic history separated from the Index's own edit history
- **settled frame** — the Index targets complete, faithful, typed coverage of user-touched data; `HEAD` exposes the current model, `Tail` preserves valid user evolution, and `Bad.Indexing` is removed rather than memorialized semantically
- **settled mechanics** — the Index is a family of `WIP.Surface`s with distinct roles; `Touched.Index.Record` coordinates identity, history, support, and occurrences while readable line wording stays on the surfaces; `Index.Block` supplies line scope and `Project.Index` registers the scopes
- **active concern** — define `Line` and `Line.History` identity, and reconcile the current `Chat.Index.HEAD`/Delta implementation with the curated-materialization role assigned to `Chat.Index`
- **next useful move** — specify the `Touched.Index.Record` shape and the reconciliation POIs that detect surface/record incoherence

## Design.Index

### Index.Curated.Model

- [DF] The `Index` is the actively maintained, increasingly complete interpretation of all qualifying touched data in `Chat.Support`. ^c20260817-21u
- [DC] `Chat.Support` supplies immutable user authority while the `Index` remains a mutable `WIP.Surface` that agents actively curate. ^c20260817-22u
- [CT] `Line.Type` defines which touched data qualifies for indexing; completeness does not mean indexing every sentence or paraphrase. ^c20260817-23u

### Index.Quality

- [DF] `Index.Quality` is the joint pursuit of completeness, fidelity, and contextual usefulness over qualifying touched data. ^c20260817-24u
- [DC] Completeness aims to index all qualifying touched data expressed through `User.Turn`s. ^c20260817-25u
- [CT] Fidelity requires every retained line to be correctly typed, supported by `User.Turn`s, and representative of its underlying touched data. ^c20260817-26u
- [PR] Contextual usefulness gives agents a fast `HEAD` view of the current `Design.Model` and a deeper path through `Tail`, support, and semantic evolution. ^c20260817-27u

### Line.History

- [DF] `Line.History` groups the semantically correct `Index.Line` expressions that index one atomic assertion across genuine user evolution. ^c20260817-28u
- [DC] `HEAD.Line` is the history's semantically correct and currently applicable expression. ^c20260817-29u
- [DC] `Tail.Lines` are semantically correct expressions for earlier chat horizons where the user held a different state. ^c20260817-30u
- [CT] The `HEAD`/`Tail` distinction expresses current versus earlier validity, never correct versus incorrect indexing. ^c20260817-31u

### Bad.Indexing

- [DF] `Bad.Indexing` is a maintenance finding that an indexed line is incorrectly extracted, attached, typed, duplicated, or grouped. ^c20260817-32u
- [DC] Correcting `Bad.Indexing` repairs, regroups, or removes the affected line instead of preserving it inside the semantic Index. ^c20260817-33u
- [CT] Git remains outside the semantic model: it records construction history and mistakes that no longer deserve Index membership. ^c20260817-34u

### Index.Surface.Family

- [DF] The `Index` is a family of `WIP.Surface`s that maintain each other rather than one surface owning semantic truth. ^c20260817-35u
- [DC] `Native.Index.Surface`s and `Skw.Annotated.Surface`s carry the selected `HEAD` lines inside their useful product scope. ^c20260817-36u
- [DC] `Chat.Index` carries the complete curated materialization: both `HEAD` and `Tail` line content, and no `Bad.Indexing`. ^c20260817-37u
- [DC] `Touched.Index.Record` carries the relationship network: stable identity, hashes and drift, history membership, `HEAD` selection, support sets, and surface occurrences. ^c20260817-38u
- [CT] `Touched.Index.Record`s are central to the Index mechanics without imposing a strict production flow on the agents that write them. ^c20260817-39u

### Index.Block.Scope

- [DF] `Index.Block` is the scope that makes an `Index.Line` mean something; the line is the atom of touched-data indexing and always needs a scope. ^c20260817-40u
- [DC] `Project.Index` defines the scopes agents index into, which keeps that registry on a self-documenting surface. ^c20260817-41u

### Index.Surface.Coherence

- [DF] Index maintenance is the work of moving material across Index surfaces: removing `Bad.Indexing` lines, grounding ungrounded lines, and making ordinary evolution edits such as renames and better wording. ^c20260817-42u
- [DC] Index surfaces may be temporarily unsynchronized because the Index is a `WIP.Surface`; that state is normal rather than a defect. ^c20260817-43u
- [CT] Synchronization between Index surfaces does not mean identical content everywhere; each surface carries what its own role requires. ^c20260817-44u
- [DC] Incoherence between surfaces and records is discovered and repaired as `POI`s rather than prevented by a stricter production flow. ^c20260817-45u
- [FR] Material may enter the Index through several valid paths; the order of production is agent-owned rather than fixed by the model. ^c20260817-46u
- [CT] Every retained semantic line is correctly typed, scoped by an `Index.Block`, supported by qualifying `User.Turn`s, represented in its `Touched.Index.Record`, and materialized in `Chat.Index`. ^c20260817-47u

## Session.Notes

### Curation operations

- Add missing qualifying lines.
- Correct wording or support.
- Remove incorrect interpretations.
- Group genuine semantic editions into histories.
- Promote the current edition to `HEAD`.
- Preserve valid earlier editions in `Tail`.
- Split histories when lines turn out to describe different atomic assertions.

### Superseded working assumptions

- `Index.Narrative` suggested more semantic structure than the current `Line.History` model requires.
- Incorrect extraction is not semantic evolution and must not remain in a history merely for auditability.
- An immutable Chat.Index landing ledger would confuse production history with the curated semantic Index; Git already owns the former.
- Support is necessary but not sufficient: a line may be attached to relevant turns and still misrepresent them.
- Making `Line.History.Record` the single canonical content-bearing object was proposed and not adopted: no surface is the absolute owner, and readable wording stays on the Index surfaces while the record coordinates.

### Surface roles

- `Native.Index.Surface` / `Skw.Annotated.Surface` — selected current lines in their useful product scope.
- `Chat.Index` — all curated valid editions, `HEAD` and `Tail`.
- `Touched.Index.Record` — identities, hashes and drift, history membership, `HEAD` selection, support sets, occurrences.
- Git — discarded mistakes and surface edit history, outside the semantic model.

### Reconciliation POIs

- A Project line may exist before typing or grounding.
- A grounded `Chat.Index` line may not yet have a useful `HEAD` placement.
- A surface wording may drift from its record hash.
- A record may identify missing or stale materializations.

### Entry paths

- `Project.Index` line → type/ground → record → `Chat.Index`
- Old chat → extract → `Chat.Index` → record → optional `Project.Index` HEAD
- Product annotation → record → `Chat.Index`
- Record audit → repair whichever surface drifted

### Open mechanics

- Define stable `Line` and `Line.History` identity without making mutable Index entities content-addressed, and reconcile that with `Index.Line.Anchor`, which explicitly is not line identity and takes a successor anchor on a new support edge.
- Define how one correctly supported line appears across several chat scopes without creating competing authorities or uncontrolled duplication.
- Reconcile the current `Chat.Index.HEAD`/Delta receipt implementation with the curated-materialization role this model assigns to `Chat.Index`; the current workflow mechanics predate these decisions.
- Decide how a reader recognizes a landed line while reading a chat: a verbatim line is only a candidate, and no regex extraction is intended.
- Reconcile `Demoted.Index.Line` in the stable Index with `Tail.Lines`: demotion is currently overruled history, while `Tail` is correct-for-an-earlier-horizon.
- Decide whether `Bad.Indexing` removal conflicts with `Index.Presumption`, where missing grounding is debt rather than a deletion trigger.

### Capture mechanics POI

- This second capture pass grounded its lines in another chat (`01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8`) while running from a different session, so `Index.HEAD.Backpropagation` has no current-chat projection to write. This is exactly the placement question the session itself is modeling; the anchors are registered and the backpropagation is left as an explicit reconciliation gap rather than being written into an unsupported chat scope.

### Prior design

- `626-index-narrative-identity-design-req.md` remains prior design provenance. Its shared-support `Index.Narrative`, immutable edition-history, and anchor-record identity assumptions are not adopted here.

## Session.Log

- **2026-08-17** — opened from the Line.History and Index-curation discussion; captured fourteen typed lines grounded in two qualifying current-session user messages through one Chatlas2 anchor batch.
- The capture deliberately stops at the semantic model. Canonical line storage, physical Chat.Index behavior, and identity mechanics remain open rather than being inferred from the current implementation.
- **2026-08-17** — second capture pass over the Index mechanics discussion: thirteen typed lines in three new blocks (`Index.Surface.Family`, `Index.Block.Scope`, `Index.Surface.Coherence`), grounded in three qualifying user messages of session `01a001c2-8fb1-72e0-8aa1-0bbc52c4b5e8` through one Chatlas2 anchor batch.
- The pass ran from a separate session, so the material is historical rather than current-chat. Anchors resolve `MATCHED`; `Index.HEAD.Backpropagation` is left as a reported reconciliation gap.
