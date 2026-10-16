# Index.Line.Anchor Dossier Migration — Impl.Req

## Impl.Abstract

Replace the line-bound `chatlas.support-set.v4`–`v6` model with the landed
`Index.Line.Anchor` design:

- the Index Markdown line owns the current `Line.Type + body + Anchor.Id` triplet;
- the Chatlas anchor resolves to a `Chatlas.Line.Anchor.Dossier` whose attachment
  assertion hashes that triplet;
- semantic support, gates, and provenance are independent relationship namespaces;
- relationship paths type each `Normal.Turn.Ref`; member-local generic `types` cargo
  disappears;
- runtime code has no compatibility reader or writer for the retired line-bound
  schemas.

The implementation updates the shared Index identity primitive, Chatlas record
model and linter, capture/registration consumers, runnable skill surfaces, and all
line-anchor records cited by `tarav-pkg`.

## Impl.Index

### Canonical identity

`agentos.index-line-anchor-triplet.v1` canonicalizes exactly:

1. the parsed `Line.Type` assertion, or the empty value when absent;
2. the normalized line body with trailing anchors excluded;
3. the normalized anchor id without the leading `^`.

The three values are length-safe encoded and hashed as lowercase `sha256:<hex>`.
The attachment API is named for the triplet rather than line content. A separate
body canonicalizer/hash excludes both `Line.Type` and trailing anchors for consumers
that compare statement wording before an anchor exists. Consumers that need the
whole typed statement use an explicit `(Line.Type, body)` pair; consumers that
validate attachment use the triplet primitive. The old helper whose name said
"content" while hashing type and body together is removed.

### Chatlas dossier schema

The only runtime line-bound schema is `chatlas.line-anchor-dossier.v1`:

```json
{
  "app": "chatlas",
  "schema": "chatlas.line-anchor-dossier.v1",
  "attachment": {
    "canonical_schema": "agentos.index-line-anchor-triplet.v1",
    "triplet_hash": "sha256:..."
  },
  "relationships": {
    "support": {"members": ["Normal.Turn.Ref", "..."]},
    "gates": {
      "semantic_approval": [],
      "tokenized_verbatim_approval": [
        {
          "token": "idx-edition:...",
          "proposal_turn": "Normal.Turn.Ref",
          "approval_turn": "Normal.Turn.Ref"
        }
      ]
    },
    "provenance": {
      "predecessor_anchors": ["cYYYYMMDD-Nu"],
      "issue_context": ["Issue.I####"]
    }
  }
}
```

The JSON example uses labels for the existing canonical `Normal.Turn.Ref` object
shape. `support.members` is nonempty, ordered, and duplicate-free. Gate lists and
provenance lists are ordered and duplicate-free. Empty mechanism lists and empty
provenance lists remain explicit so paths do not vary by incidental population.
The dossier stores no hint, copied line content, `Line.Type`, derived standing, or
generic member `types` map.

`chatlas.support-set.v3` may remain a distinct generic Chatlas support record, but
it is never accepted as an `Index.Line.Anchor` dossier. The retired v4–v6 schemas
are not accepted by runtime line resolution, creation, amendment, or linting.

### Relationship semantics

- `relationships.support.members[]` occurrences are semantic-support turns.
- `relationships.gates.semantic_approval[]` and
  `relationships.gates.tokenized_verbatim_approval[]` own their mechanism cargo.
- gate positions `proposal_turn` and `approval_turn` supply their finer
  `Turn.Type`; the approval turn need not derive its role from support membership.
- one exact `Normal.Turn.Ref` may repeat across namespaces or gate positions.
- support-member uniqueness is enforced only within the support relationship.
- `relationships.provenance.predecessor_anchors` retains anchor genealogy.
- `relationships.provenance.issue_context` retains issue coordinates without
  copying issue content or derived issue standing.

### Linter behavior

The line-drift check computes the current triplet hash from each parsed kernel line
and its cited anchor. A dossier whose attachment assertion differs reports drift.
Grounding reads only `relationships.support.members`. Approval and verbatim checks
read only their gate mechanisms. Review-content comparison excludes the Markdown
`Line.Type` assertion because type is not line body content; it still validates the
gate token, proposal/approval roles, order, and normalized body material.

An old line-bound schema cited by an Index line is invalid, not silently adapted.

### Corpus boundary and migration

The migration source is the complete parser-discovered `tarav-pkg` depot, not a
hand-maintained file list. The pre-implementation inventory is:

- 95 Index documents;
- 1,593 anchored kernel-line occurrences;
- 1,592 unique cited anchors;
- 1,284 v4 records, 307 v6 records, and one v3 record attached to a line;
- zero missing records;
- one anchor repeated on two identical `Line.Type + body` occurrences;
- 791 tokenized-approval relationships;
- zero populated issue-context lists in this corpus.

Migration amends records in place and preserves every parser-discovered anchor id
(1,597 at apply time). It derives
the attachment assertion from the authoritative current Index triplet, copies every
old support member into `relationships.support.members`, projects typed approval
cargo into the matching gate mechanism, moves predecessors and issue coordinates
under provenance, and drops hints. It must refuse missing anchors, divergent
multi-occurrence triplets, malformed legacy records, unresolvable turn refs, or
lossy relationship projection.

The migration implementation is a bounded development utility, not a runtime
compatibility reader. It supports a read-only plan and explicit apply. The Chatlas
depot is Git-backed, so the required workflow checkpoint supplies recovery before
application.

## Execution.Plan

1. Add body and triplet canonicalization/hash primitives in `agentos-py`, move Index
   collision checks and tests to the explicit identity they need, and update the
   documented identity contract.
2. Replace the Chatlas line-bound record model with the v1 dossier parser, builder,
   resolver, equivalence, amendment, and gate projections; update batch/capture,
   audit, render, reconciliation, CLI, and tests as required by those semantics.
3. Update Chatlas-powered Index checks to validate attachment triplets and typed
   relationship namespaces, including body-only review equivalence.
4. Add and test the bounded `tarav-pkg` dossier migration utility; verify its
   read-only plan accounts for every source anchor before apply.
5. Update Skillware sources and other maintained Chatlas package guidance, build the
   runnable skill surfaces, and check generated-surface drift.
6. Apply the migration to every parser-discovered `tarav-pkg` anchor, then rerun corpus
   inventory to prove every cited record uses the dossier schema and every current
   triplet hash matches.
7. Run focused unit/e2e tests, full affected-package tests, Anchory structural check,
   Skillware check, and the complete `tarav-pkg` Index linter including approval
   and verbatim gates.

## Impl.Log

- Execution authorized by the explicit autonomous implementation turn
  ^c20260809-170u. Design is cold-read and ready for the mandatory pre-edit
  checkpoint.
- Mandatory checkpoints were created in every affected repository before the
  first implementation edit. No implementation commit was created afterward.
- Runtime implementation now has one line-bound schema,
  `chatlas.line-anchor-dossier.v1`; allocation-dependent attachment records use
  `AnchoryDepot.register_derived` so the allocated anchor participates in its
  record atomically.
- Migration apply discovered 95 documents, 1,598 anchored occurrences, and
  1,597 unique anchors. The five-anchor increase over the initial inventory came
  from approved design lines landed before apply. All 1,597 records were amended
  in place; verification reports 1,597 current dossiers and zero remaining
  changes.
- The migrated path inventory is uniform: one schema and only `app`, `schema`,
  `attachment.{canonical_schema,triplet_hash}`, and the explicit
  `relationships.{support,gates,provenance}` subpaths. It contains 2,199 support
  members and 796 tokenized-verbatim gate relationships.
- A separate text-citation audit found no parser-discovered kernel anchor outside
  the dossier corpus. The three other unique `^` citations are deliberately not
  `Index.Line.Anchor` records: one nested-list support record, one backticked
  example literal, and one Skillware annotation support record.
- Chatlas tests pass (472) and the full Agentos foundation suite passes (870);
  affected Ruff checks, compilation, diff checks, and the generic Anchory
  depot structural check pass.
- The complete `tarav-pkg` linter resolves the migrated support and attachment
  model: `Grounding.Provenance`, `Anchor.Collision`, and `Anchor.LineDrift` all
  pass with zero findings. Its six errors are genuine older verbatim-gate wording
  drift on six `design/107-design.md` lines, not schema, attachment, or
  support-resolution failures. Existing warning debt remains outside this migration.
- The shared Chatlas depot still contains 384 v4, 199 v5, and 266 v6 records not
  cited by `tarav-pkg`; they remain explicit migration debt outside this
  bounded corpus and are intentionally rejected by the new runtime.
- Hugentics and Chatlas Skillware sources were updated and rebuilt. Their checks
  have no diagnostics or newly unhonored dependencies; seven Hugentics and one
  Chatlas derived-stale advisories remain intentionally untouched.

## Impl.Agendix

### Completion assertions

- No retired v4–v6 line-bound schema is emitted or accepted by runtime code.
- No `tarav-pkg` anchored kernel line resolves to v3–v6 after migration.
- Anchor count and anchor ids are unchanged by migration.
- Every dossier attachment hash matches its current authoritative Index triplet.
- Every old support member, gate relationship, predecessor, and issue coordinate is
  accounted for in the migrated dossier; hints are intentionally discarded.
- Runnable skill files are generated from `.skw/src`; Skillware reports no
  diagnostics or new dependency POIs, while the explicitly retained stale-derived
  advisories remain visible.
- Implementation changes remain uncommitted after the mandatory pre-edit checkpoint.
