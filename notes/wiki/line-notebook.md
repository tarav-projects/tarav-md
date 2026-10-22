# Line Notebook

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## Workflow and Project integration

The agreed design separates the [Lines primitives](lines-workflow.md) from
Line Notebook, a workflow providing the central persistent home for Blocks
and Lines. Notebook owns storage, capture, retrieval, and organization; Lines
supplies the recursive typed contexts. Notebook is intended to play a role
analogous to Chatlas's home for chats.
<!-- tarav.breadcrumb 0114b579847d -->
<!-- tarav.breadcrumb 538cfa114882 -->

A participating Project gets a notebook partition rooted in a Project Block.
Its Project Type can provide a default layout of typed Blocks and extend that
layout for its own work. The Project integrates checks, POIs, and actions;
it is an integration surface for the notebook's behavior. Exact class and
accessor names remain implementation choices.
<!-- tarav.breadcrumb 8f5d0282be58 -->
<!-- tarav.breadcrumb 5faef8e3fddb -->

## Default discussion and current model

The default layout has a Project root with three typed sibling branches:
Discussion, Model, and Archive. Discussion stores conversation and reasoning;
its content carries no obligation to implement it or align another surface
with it. Model aims to represent the Project's current design and can carry
alignment and maintenance obligations. Model here is a typed Block within
the notebook.
<!-- tarav.breadcrumb 18a9929cf7d1 -->
<!-- tarav.breadcrumb 215d0f2ea689 -->

Lines explain a Block's intended reading; its Type supplies code for assertions,
checks, and other operational behavior. Possible protections include a
read-only root or an explicit acceptance step for edits. These are capabilities
to design for particular Types, not a universal approval requirement for
capture.
<!-- tarav.breadcrumb 2048adc9463e -->
<!-- tarav.breadcrumb 7fed2ad6797e -->

## First use: recover a design archive

The first intended use is an Archive Block containing recovered legacy
design discussions. Its Lines establish the historical context inherited by
the recovered Blocks; inclusion does not claim that the material is current
design. The first implementation places Archive beside Discussion and Model;
the arrangement can evolve through later design and use. Candidate sources
include the old Diagram stores, Archive.Attic
repositories, and historical Markdown indexes and their Git histories.
<!-- tarav.breadcrumb c954c91f710c -->
<!-- tarav.breadcrumb b484181f85e1 -->

Start by selecting the most recent suitable recovered state. “Current archive”
means the selected archive snapshot, not a claim of present applicability.
Git can record changes after import. General historical reconstruction belongs
to the separate [Lineage design](lineage.md); the first notebook/import should
not require a Block-specific version system.
<!-- tarav.breadcrumb 74db021699d7 -->
<!-- tarav.breadcrumb 3bf8feada293 -->

## Implemented first use — request 931

[Request 931](../../../tarav-py/notes/live/931-line-notebook-impl-req.md) implements
the bounded storage, Project layout, and first import. The Python
[Notebook](../../../tarav-py/src/tarav/l1/notebook/__init__.py) uses the
Notebook Workflow partition of the existing Record Registry. Each Line or
Block is one JSON Record keyed by Ship. The
[Project binding](../../../tarav-py/src/tarav/l2/project/notebook.py) selects a
ProjectBlock; explicit create() seeds its explanatory Lines and three typed
sibling Blocks once. Existing layouts and edits are loaded without regeneration.
<!-- tarav.breadcrumb 0a93a5eb1c22 -->
<!-- tarav.breadcrumb 89bee5b1a16a -->

Run Python through Tarav and initialize the current runtime before using the
default store. A minimal example from the umbrella Project is:

```python
from pathlib import Path
from tarav.l3.runtime import get_runtime
from tarav.l2.project import Project

get_runtime()
project = Project.from_path(Path("/Users/pereiro/projects/taravangian-project"))
book = project.notebook()
archive = book.archive
for item in archive.contents:
    print(type(item).__name__, item.id)
```

Notebook.save(obj) writes one Record. Notebook.save_tree(block) writes its
contained tree. Notebook.load(ship) resolves the connected context with shared
object identity. Notebook.commit(message) explicitly records changes in Git.
The [storage and layout tests](../../../tarav-py/tests/test_project_notebook.py)
and [storage tests](../../../tarav-py/tests/test_notebook.py) verify reload,
identity continuity, mixed contents, and preservation of edits. This first
implementation adds no alignment engine, editing protections, move operations,
or general Lineage API.
<!-- tarav.breadcrumb a158c6f2a488 -->
<!-- tarav.breadcrumb c1476bc6d5e0 -->

The [bounded recovery script](../../../tarav-py/scripts/import_legacy_notebook.py)
imported 1,581 legacy Lines, 269 legacy Blocks, and nine former Model groupings
as ordinary Blocks. It selected the latest explicit editions in the two
retained Diagram stores and preserved text and Ships. Former labels became
ordinary Lines. The live Tarav root Project's notebook now has 2,149 Records
including explanatory and label Lines. Original namespace, ship, annotation,
and richer edition data were copied alongside the conversion; the 38 former
Collection records remain there as raw source.
<!-- tarav.breadcrumb 5f3ab7cb0427 -->
<!-- tarav.breadcrumb b246defca8b1 -->

The local partition is
`~/Documents/tarav/records/92338514-6f87-4dad-8a41-3148020f90d4`.
Its import report is
`imports/ee7c5865-2209-516f-8be2-361eea2d8f18/report.json`.
The data commit is `a14e4955`. Reopening the Project root verified all 1,581
legacy texts and Block links, all 1,859 selected source hashes, and reachability
of all 2,149 Records. The
[recovery tests](../../../tarav-py/tests/test_notebook_recovery.py) cover
latest-edition selection, source retention, fresh-process execution, and
refusal to overwrite a later notebook edit. Older Markdown indexes, Git
histories, and unfinished Drafts were not part of this selected first import.
<!-- tarav.breadcrumb 49908ac5c359 -->
<!-- tarav.breadcrumb 6d8bb0536f55 -->

## Context-based grounding

Grounding finds Blocks that speak to the current conversation. An optional
hint focuses that task; it need not be a Block name. The default source is the
inferred Project's complete Model subtree, which aims to contain the current
model of the system. Discussion and Archive can be selected explicitly while
retaining their respective conversational and historical meaning.
<!-- tarav.breadcrumb 40eee331eedf -->
<!-- tarav.breadcrumb 3aa182b94d8f -->

Lines contribute typed and structural triplets through Context hooks. Query
execution belongs to Context, using its existing SPARQL SELECT/ASK engine;
Notebook remains the persisted home for objects. Agent judgment determines
relevance and how much to read. Collecting the Model makes its contents
available to query; it does not mean the agent has read or endorsed each Line.
<!-- tarav.breadcrumb faf571d4d914 -->
<!-- tarav.breadcrumb 5d4f4f5bb5a8 -->

[Request 933](../../../tarav-py/notes/live/933-notebook-context-grounding-impl-req.md)
implements [Lines hooks and collection](../../../tarav-py/src/tarav/l1/lines/context.py),
[Project selection](../../../tarav-py/src/tarav/l2/notebook.py), and the
[Notebook CLI](../../../tarav-py/src/tarav/l3/notebook/commands.py).
The collected graph includes every Block and Line in the selected subtree,
plus ancestors and their direct Lines. Ancestor sibling targets may appear
as edges, but their contexts and text are not collected. Lines use the IRI
prefix `urn:tarav:lines:` with `text`, `scope`, `parent` and `contains`;
RDF ordinal membership predicates preserve mixed content order.
<!-- tarav.breadcrumb af6cb83e28f2 -->
<!-- tarav.breadcrumb af4e86d1b3fd -->

The installed commands run through the selected Project's declared harness:

```sh
tarav notebook ls --project /absolute/project/path --json
tarav notebook read --project /absolute/project/path --id BLOCK_OR_LINE_SHIP --json
tarav notebook query --project /absolute/project/path --sparql 'ASK { ?s ?p ?o }' --json
```

Each command defaults to Model. `--branch discussion`, `archive` or `project`
selects another branch; `--block SHIP` selects a particular subtree. Reads
return ordered direct contents and ancestor Lines. Known stored Ships also
resolve through `tarav context --id`. Missing storage or coverage is reported
without creating a Notebook or broadening the search. The
[integration tests](../../../tarav-py/tests/test_notebook_context.py) cover
scope, read-only storage, CLI queries, identity lookup and custom Project Types
available only through their declared environment.
<!-- tarav.breadcrumb fd44d7c9728b -->

[Request 868](../live/868-notebook-grounding-skill-impl-req.md) restores
[`tarav-hugentics --ground --notebook [HINT]`](../../skills/tarav-hugentics/references/ground.md)
and the equivalent bare `--ground` route. Its module guides Project inference,
map inspection, Context queries, scoped reads and explicit branch expansion.
This new ModelBlock route leaves the retired Model-backed capture and
implementation backend parked. The read-only live rehearsal found only the
umbrella Project Model's seed explanatory Line; substantive grounding remains
to be exercised after there is useful Model content.
<!-- tarav.breadcrumb c86272c43710 -->

## Notebook capture: support and review

The Notebook Model is the concrete use case for rebuilding capture. Small base
Types define reusable support and review capabilities; Notebook Line and Block
Types compose them. Every newly captured Notebook Line should trace to
User-touched evidence, normally specific Chatlas User turns, or another
explicitly authorized surface. Its content summarizes material already in
that discussion. The evidence relationship is explicit and remains a claim
whose semantic adequacy can later be assessed.
<!-- tarav.breadcrumb d66a41457150 -->

Support and review are independent. Agent-maintained parts require support
without requiring review of their verbatim wording. A User-reviewed core
additionally records explicit approval of the presented Block or change,
using proposal/approval chat references and the token protocol. This allows
the core to evolve through direct User interaction while other supported
material can be maintained faster. Approval evidence does not automatically
constitute substantive support.
<!-- tarav.breadcrumb b1e41a455654 -->
<!-- tarav.breadcrumb 3f9d570fcaa1 -->

A simple Line still has a stable Ship and mutable content, with previous states
in Git. Its Type can invalidate assessments or require renewed review after
an edit. A LineTrace is an optional more sophisticated evolution mechanism;
it is not necessary for every Line. Evidence for an older state must remain
distinguishable from evidence about the current wording and context.
<!-- tarav.breadcrumb 95789849fe31 -->

[Implementation request 934](../../../tarav-py/notes/live/934-notebook-support-review-impl-req.md)
specifies the next Python implementation: support sets, exact evidence links,
review records, state-sensitive attachment, capture/inspection operations and
a few mechanical checks. Semantic Assertion evaluation and scoring integration
are explicitly deferred. This is a design handoff; those capabilities have
not been implemented by this capture pass.
<!-- tarav.breadcrumb bb0f9e4b889d -->

## Implemented support and review capture — request 934

The User authorized execution of
[request 934](../../../tarav-py/notes/live/934-notebook-support-review-impl-req.md).
The Python implementation now provides independent
[support records](../../../tarav-py/src/tarav/l1/grounding/__init__.py) and
[verbatim review records](../../../tarav-py/src/tarav/l1/review/__init__.py),
composed into NotebookLine, ReviewedLine, SupportedBlock and ReviewedBlock
Types. Base Lines remain unchanged. Existing imported records are not retyped
or given invented evidence.
<!-- tarav.breadcrumb e938c0e93df6 -->

[NotebookCapture](../../../tarav-py/src/tarav/l2/notebook_capture.py) is the
Python-first capture interface. Selecting it does not create storage;
its explicit create initializes the Grounding and Review Record Registry
partitions. It can capture a Notebook Line, attach a SupportSet, render a
proposal, record a review, inspect evidence, and check review completion.
Evidence records are inserted separately and retain the subject state they
concern. Approval is not substituted for substantive support.
<!-- tarav.breadcrumb 36d84282dbba -->
<!-- tarav.breadcrumb ba443f1b05ef -->

From a Tarav-started Python script, with an existing Project notebook and
already resolved ChatlasTurnReference objects:

```python
book = project.notebook().create()
model = book.model
line = model.capture(
    "The supported design statement.",
    root=user_turn_ref, producer=producer_turn_ref, reviewed=True,
)
proposal_text = model.propose_review([line], token=unique_review_token)
# Present proposal_text; obtain the real proposal and User approval references.
review = model.record_review(
    [line], token=unique_review_token,
    proposal=proposal_turn_ref, approval=approval_turn_ref,
)
model.complete_review(review)
report = model.inspect(line)
```
<!-- tarav.breadcrumb 31da614fc262 -->

The references and token in that example are inputs obtained from the actual
conversation. Proposal rendering needs no fabricated future approval reference.
Capture persists incomplete content; completion checks cannot report success
for a failed review. Agent-maintained capture uses reviewed=False in a scope
without an inherited review requirement, and still requires support.
The returned report describes mechanical support/review
problems, not semantic scores.
<!-- tarav.breadcrumb adadd47cf70d -->
<!-- tarav.breadcrumb 1c08242ad734 -->

Subject state includes the Line's wording and concrete Type, plus direct Lines
in its Block and ancestor contexts. Attachments do not affect this fingerprint.
This first policy is conservative: a context Line edit, including a sibling
addition, can stale existing evidence. For a batch, establish the final Block
contents before attaching support. Proposals include target-state digests;
unchanged wording under a different context cannot acquire approval through
an older proposal. New evidence can satisfy the current-state requirement
while older records remain inspectable. Git history remains the simple Line's
history mechanism; no LineTrace or semantic carry engine was introduced.
<!-- tarav.breadcrumb afc888b0a772 -->
<!-- tarav.breadcrumb a2b7aa681cee -->

[NotebookEvidenceSuite](../../../tarav-py/src/tarav/l2/notebook_checks.py) is
composed into the featured Project's checks. Atomic Situation Chains report
missing, stale, invalid or unavailable support/review, and inaccessible existing
notebooks. Block and Line Types combine requirements; descendants cannot
silently weaken them. Unavailable evidence makes checks incomplete and cannot
settle earlier unresolved findings. Valid new review evidence closes the
corresponding MissingReview action through the normal gone path.
<!-- tarav.breadcrumb 68deb7b32511 -->
<!-- tarav.breadcrumb 164dadc08eea -->

The [capture tests](../../../tarav-py/tests/test_notebook_evidence.py) exercise
actual Chatlas reference resolution over fixed Normal Model fixtures, retained
evidence, invalid review protocols, bounded multi-Line changes and changed
context. The [Project tests](../../../tarav-py/tests/test_notebook_evidence_checks.py)
exercise action closure, unavailable evidence, explicit source authorization,
inherited requirements and read-only behavior. Semantic Assertions, scoring,
alignment with code, a new capture skill route and extension UI remain deferred.
<!-- tarav.breadcrumb db91a40c82c4 -->
<!-- tarav.breadcrumb 8d1ca9c52f24 -->


## Typed Notebook integration — request 937

The discussion identifies Notebook as the object responsible for coordinating
the workflows around Lines. A Notebook is itself a typed recursive Block;
global, Project and nested notebooks can organize the same primitives. Its
Types can specialize checks and evidence behavior. Lines remain small, while
support, exact review and Project status retain their distinct responsibilities.
<!-- tarav.breadcrumb 41f0114793f7 -->

[Request 937](../../../tarav-py/notes/live/937-typed-notebook-integrator-impl-req.md)
implements this through [l2 Notebook](../../../tarav-py/src/tarav/l2/notebook.py).
Project.notebook() now returns the actual ProjectBlock, whose Discussion,
Model and Archive children are also Notebooks. The l1 Notebook remains the
storage transport, exposed as book.storage. The examples above use this new
API. Context collection moved to l2.notebook_context; its CLI and graph
contracts remain intact. Existing record Ships, concrete Type names and parent
links are preserved. Newly created Project notebooks share a deterministic
TaravNotebook root; opening an existing notebook never reparents it.
<!-- tarav.breadcrumb d9d7e4d1eff6 -->

The standard capture/support entry point accepts one User-turn root plus
optional conversational neighborhood per SupportSet. Additional calls can
attach further sets to the same Line. This composes the existing general
Grounding records, rather than limiting that general schema. Capture remains
nonblocking: missing or wrong-role roots can be retained and then reported.
Support and verbatim review remain independent; review completion requires
real proposal/approval evidence. Notebook operations stay within their subtree.
<!-- tarav.breadcrumb 3f8ea4d30568 -->
<!-- tarav.breadcrumb 428238b3167c -->

Each Notebook checks its local Lines and composes its nearest child notebooks'
suites, including subtype extensions. Ancestor requirements still apply, and
each Line is evaluated once. Project access checks load existing storage and
compose this suite; the Project continues to own actions/status. Existing seed
and archive Lines acquire no invented support or new retrospective policy.
The [integration tests](../../../tarav-py/tests/test_notebook_integrator.py)
and existing evidence/action tests verify these boundaries. The focused run
passed 94 tests, plus 3 recovery tests. A live read preserved all 5,126 files
in the existing store. Scoring and general Ship lineage remain deferred.
<!-- tarav.breadcrumb 238a29ac8161 -->


## Reviewed Notebook capture skill — requests 869 and 939

The User requested a capture path targeting Notebook, with the inferred
Project's ModelBlock as its default. Preparation reads that target's existing
Blocks and ancestor context before proposing additions or amendments. Explicit
Project, branch or Block selection can target another part of the notebook.
This route is separate from Wiki/inline capture and the retired Diagram Model
backend. The implemented invocation is `tarav-hugentics --capture --notebook`.
<!-- tarav.breadcrumb f8d021a17494 -->
<!-- tarav.breadcrumb 86c87c46ecca -->

Focus and interaction mode remain independent. The Agent can discuss a Block,
present exact wording for token review, return to discussion, or move to the
next Block after approval. `::discuss` holds until `::review`. `::approve TOKEN`
accepts the presented proposal without writing it; approved items can wait for
`::land` or `::land-all-approved`. A changed semantic proposal needs a fresh
token. Substantive User-turn support remains distinct from verbatim approval.
<!-- tarav.breadcrumb 56271e477598 -->
<!-- tarav.breadcrumb 8af5606291ae -->

The User also requested explicit writing guidance for the capture Agent.
The recovered Kernel Writing craft emphasizes focused contributions, sibling
orthogonality at the chosen resolution, direct wording, meaningful
qualifications, coverage over compression and useful future signal. The
[writing guide](../../skills/tarav-hugentics/references/kernel-writing.md)
includes worked examples and a short proposal checklist. It allows meaning to
depend on Block ancestry and order to matter for logs/arguments; it adds no
topic field, compulsory sections or concept-only Block restriction.
<!-- tarav.breadcrumb 30529b4eecbd -->

Implementation: [NotebookDraft](../../../tarav-py/src/tarav/l2/notebook_draft.py)
stages new recursive Blocks, Lines and amendments through Notebook.draft().
Its temporary plan preserves actual Ships, operations, source/context
baselines and exact presentation across tool calls. Staging writes no live
candidate records. Landing checks the actual proposal/approval and fresh
source/context before applying the change through current support/review
mechanics. Amendments preserve Ship and concrete Type; plain historical Lines
are not migrated. Independent new child Blocks can land sequentially, while
changed local meaning requires a fresh proposal. This supplies bounded
preflight rather than transactional batches or general lineage.
<!-- tarav.breadcrumb 4f41a74a98d1 -->

The [capture guide](../../skills/tarav-hugentics/references/notebook-capture.md)
documents targeting, interaction, real Python staging/landing, support,
read-only audit and the existing supported/unreviewed route. Its two compiled
Python examples were executed against isolated Project and Normal Model
fixtures. Nine draft tests and 79 focused combined tests passed; full Project
status completed 1,298 checks and all 58 test-file runs with zero test POIs.
No live Model capture was performed. The deployed skill copy matches the
compiled products and the active depot links them. Package generation still
reports freshness findings, including two neighboring Issue contexts made
stale by the changed capture guidance; no scoring, LineTrace or legacy Index
runtime was restored. See [skill request 869](../live/869-notebook-capture-skill-impl-req.md)
and [Python request 939](../../../tarav-py/notes/live/939-notebook-reviewed-capture-impl-req.md)
for the measured checks and remaining findings.
<!-- tarav.breadcrumb 51d7d69c7438 -->

## Repository DOI context recording — request 945

The User requested Notebook adoption of the repository DOI and Change-ID
infrastructure. Context remains reconstructed from Git; each state reference now
names the repository DOI, exact commit/tree, optional Change-ID and Line-record
path. A maintained locator can change without rewriting the evidence reference.
<!-- tarav.breadcrumb 72e3ec1b37ee -->

`l2.notebook_references.NotebookStateReference` is the explicit Git consumer.
It asks the repository resolver for the original commit or one unambiguous
matching-tree Change-ID candidate, then reads the Line and its authoring ancestry
from that verified state. The old path-based reader was removed. Support,
review roles, tokens and current-state comparison keep their existing semantics.

Explicit capture checkpoints bind/install tarav-change on Notebook, Grounding
and Review stores, with System Project ownership by default and an explicit
owner override. Support/review writes commit their evidence and the Notebook
links. Read-only inspection never installs hooks, provisions storage or commits.
Commits select only records and repository metadata, preserving unrelated paths.

The live migration translated 30 references in 15 SupportSets and two
ReviewFrames. All prior SubjectState digests and review presentations remained
identical. Original current records were hash-verified into Attic; all three
repositories committed their migration and their witnesses matched. Historical
commits without Change-IDs retain exact commit/tree coordinates.
See [request 945](../../../tarav-py/notes/live/945-notebook-repository-references-impl-req.md)
for verification and [repository references](archive-doi-registry.md#repository-references-and-change-id--2026-10-22)
for the underlying resolution contract.

Final verification: all 65 pytest suites passed, with 84 checks completed and
none incomplete. A test-fixture isolation defect found during the first full
run was corrected and its action closed on recheck. Existing Gitleaks and
synthetic marker findings remain separate. New implementation evidence audits
cleanly; twelve older unavailable chat links in this Note are preserved as found.
