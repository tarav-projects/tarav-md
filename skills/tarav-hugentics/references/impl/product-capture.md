# Implementation Product and Diagram Capture

This internal module composes Tarav capture with mutating implementation
workflows. It is not an independent implementation phase.

Read [`../capture.md`](../capture.md) for current Chatlas references,
Capture.Manifest mechanics, Object.Types, Gates, and Assertion.Engine
behavior. Implementation capture runs that ordinary Capture workflow while
fixing the semantic destination to the request's one `Impl.Req.Block`. The
Block may be introduced by the same Manifest when bootstrapping a direct
implementation request.

The explicit mutating implementation invocation authorizes bounded automatic,
unreviewed capture of qualifying material into that Block. Do not add a
separate Capture approval or landing checkpoint to each slice. This workflow
authorization does not weaken producer, support, typing, Assertion, or POI
requirements and never creates a `Verbatim.Gate` without an actual proposal and
User approval exchange.

## Surface Boundary

Implementation has three different surfaces:

- the **live-note Impl.Req** is Agent coordination data;
- the **Impl.Req.Diagram** is the `Impl.Req.Block` containing only supported
  User-Touched material relevant to the request;
- **Product.Surfaces** are the exact code, tests, configuration, and
  documentation editions produced by execution.

Do not collapse them. In particular, do not copy an Agent-authored plan or log
into the Block merely because it appears in the live note.

The live note does not own or recreate Diagram resolution. Every mutating
implementation run must use the shared capture path to resolve:

```text
Project
  → Diagram configuration and Namespace
  → Project.Model
  → current Model context and Object.Types
  → existing or new Impl.Req.Block target
  → ordinary Capture.Manifest check and apply
```

The implementation specialization begins only at target selection. It must not
bypass shared contextualization, lineage lookup, evidence construction,
Manifest linting, or landing.

## Capture Bar

Capture into the `Impl.Req.Block` only when material:

- is meaningfully touched by the User;
- directly constrains, changes, authorizes, rejects, or contextualizes the
  implementation request;
- can be stated as one typed Line; and
- has a resolvable rooted Support.Set from the producing chat context.

Zero new Lines in a slice is valid. Use the existing Line ship when the new
Annotation continues its semantic history; otherwise introduce a new one.
Reviewed Gates require actual proposal and approval turns. Automatic workflow
capture remains unreviewed rather than manufacturing approval.

## Slice Transaction

### Slice.Open.Capture

Before product edits, run the ordinary capture Contextualize path and inspect
User turns accumulated since the prior capture. Resolve the target Block from
the Diagram rather than trusting a live-note UUID alone. Land only supported
material that currently governs the slice into that same Block. This records
why the work is being attempted; it does not claim the product already
implements it.

### Product.Landing.Capture

After implementation, annotate exact Product.Surface editions with their
available Production.Context when current Diagram and Archive primitives can
represent the claim. Never describe intended work as landed product state.

When those mechanics are unavailable, do not reconstruct legacy SKW, Anchory,
or Chat.Index pipelines. Preserve the verified product, retain precise
references in the live note, and surface the missing Product.Surface context as
a POI for later reconciliation.

### Slice.Close.Capture

After checks pass and the diff is reviewed:

1. rescan the slice's chat for newly relevant User-Touched material;
2. update the live note's coordination state separately;
3. compile one ordinary Tarav2 Capture.Manifest targeting the existing Model
   and Block for any selected Lines;
4. check and apply it through the normal capture path;
5. re-render the affected Block so Assertion state and POIs are current; and
6. report capture omissions or failures without pretending they invalidate
   verified product work.

## Final Audit

Before closing the request, check that:

- the Block contains the important User-Touched constraints and resolutions
  encountered across Design and Execute;
- every Line remains typed, supported, and relevant to this Impl.Req;
- no Agent-only coordination material was mislabeled as User-Touched;
- Product.Surface context was captured where supported, with gaps surfaced as
  POIs; and
- the live note points to the exact Namespace, Model ship, and Block ship.

The audit exists to prevent meaningful loss and misgrounding, not to maximize
annotation volume.
