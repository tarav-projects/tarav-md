# Product Review Tracker

<!-- tarav.sessions
ec6cf584 = codex:01a1563b-2992-7c62-8a38-05c1cc75b1fe @ec6cf5849bb6c4e66f011b015415da94eeb1a17634872aa4fb9e25d8e065ab53
-->

## Batches are the review objects

Product Mapping supplies product-agnostic chunk identities and exact committed
coordinates. Product Review Tracker groups them into meaningful batches. The
Agent uses product understanding to choose useful subjects; a chunk may belong
to several batches representing different views. Chunks have no independent
review token. A batch keeps its identity while its membership evolves.
<!-- tarav.breadcrumb 86b23eabe674 -->
<!-- tarav.breadcrumb 5c3a07f47861 -->

There are two separate checks. Completeness asks whether every chunk in the
selected map belongs to at least one batch. Currency asks whether each batch's
current revision has been reviewed. An overlapping batch cannot discharge
another batch's review obligation. Changes make the batch stale; maintaining
membership and reviewing the material can be covered by one completion token.
<!-- tarav.breadcrumb e05fc85ec6c7 -->
<!-- tarav.breadcrumb 86ad33eb82a9 -->
<!-- tarav.breadcrumb 9003bf3223c3 -->

## A committed review horizon

Reviews use an existing map pinned to a specific commit. By convention the
routine horizon uses a somewhat older map, roughly five to ten days old, so
recent material has time to settle. At that map, maintainers reconcile which
chunk IDs belong to each persistent batch before completing its next review.
The mapping and review workflows keep distinct responsibilities.
<!-- tarav.breadcrumb 29e8342d47b1 -->
<!-- tarav.breadcrumb 88da590c788a -->

## Completion records attention, not endorsement

Review happens with the User present in chat. Its result may be a design
change, new Actions, a decision to reconsider something later, or no further
work. Outputs can live elsewhere and reference the exact batch revision.
The User's token means the review happened and its outcomes are in place;
it does not approve the product content or require follow-up work to finish.
The User can then move to the next batch.
<!-- tarav.breadcrumb 9db218ec9441 -->
<!-- tarav.breadcrumb 6cb5f70a898f -->
<!-- tarav.breadcrumb b7c9ab4f09ed -->

## Implementation

The User requested an implementation request and execution together.
<!-- tarav.breadcrumb 361695dab82c -->

[Request 949](../../../tarav-py/notes/live/949-product-review-tracker-impl-req.md)
implements separate [Batch, BatchRevision and ReviewCompletion Records](../../../tarav-py/src/tarav/l1/product_review/model.py).
The [tracker](../../../tarav-py/src/tarav/l2/product_review/tracker.py) reuses
confirmed Product Maps, retains exact selected states and history, and validates
an Agent presentation followed by the User's exact `::reviewed review:<revision>`
token. Chatlas snapshots preserve the cited Turns. Existing mappings are reused.

Implementation policy selects the newest HEAD-ancestor map whose commit is at
least five days old; explicit map selection overrides that convention. A newer
mapping confirmation time does not make an old commit recent. No eligible map
leaves the scan incomplete. Unchanged selected bytes and coordinates retain
currency across unrelated map updates; changed locations or selected content
request renewed review. Maintaining membership creates a fresh revision and
does not transfer completion from earlier revisions.

The [Project manager](../../../tarav-py/src/tarav/l2/project/product_review.py)
uses the `product_review` section of `.tarav/config.json`; the installed
`product-review` CLI calls the same workflow. [Situation Chains](../../../tarav-py/src/tarav/l2/product_review/checks.py)
produce one aggregate completeness signal and one stable signal per batch.
Scan checkpoints preserve pending Actions when the integration is disabled or
the horizon is unavailable. The [guide](../../../tarav-py/src/tarav/l1/product_review/README.md)
and [behavioral tests](../../../tarav-py/tests/test_product_review.py) provide the
operating path and verification. Implementing the workflow does not itself
review any real product batch.

## Existing subjects and bounded batches

The User refined the organization boundary: every batch attaches under an
existing UUID, while the base batch stays product agnostic. For Tarav, that
attachment is to a class's Type identity. Selected classes can have batches;
there is no requirement to create one for every class. This reuses the codebase's
semantic structure rather than building another class or subject hierarchy.
<!-- tarav.breadcrumb a271ec766f36 -->
<!-- tarav.breadcrumb 9bd1c1956c26 -->

The User also requested a maximum number of chunks per batch and delegated the
choice of a sensible default. Implementation policy selects eight chunks,
configurable through Project `product_review.max_chunks`. This is a count bound,
not a promise about bytes: Product Mapping permits chunks to grow.
<!-- tarav.breadcrumb b4b6d4835f4c -->

[Request 954](../../../tarav-py/notes/live/954-review-batch-class-subjects-impl-req.md)
adds a required generic `Batch.subject` UUID and pins it into each revision's
review presentation. The [ClassBatch specialization](../../../tarav-py/src/tarav/l2/product_review/subjects.py)
resolves its TypeShip to the existing TaravClass, whose bases, Workflow and
Context remain the source of organization. Workflow class identity is distinct
from the Workflow entity's own UUID. Several small batches can share a class.
Subjects stay fixed for a batch; retirement and replacement preserve earlier
reviews when a subject grouping changes.

Creation, revision and completion enforce the current size limit. Reducing
configuration can make an existing batch oversized; its normal review Action
then requests regrouping, preserving identity and historical completion evidence.
No automatic splitting, map regeneration or mandatory Notebook creation is
introduced. The [Python/CLI tests](../../../tarav-py/tests/test_product_review.py)
exercise generic subjects, class attachment, exact limits and Action reopening.
