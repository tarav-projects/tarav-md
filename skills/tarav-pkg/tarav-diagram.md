# Tarav.Diagram

This document describes the current candidate design of `Tarav.Diagram`.
It is subordinate to the Tarav Constitution and remains amendable.

## Data Train

Tarav progressively interprets captured user-agent collaboration through
one integrated data train:

```text
Chat.Raw.Artifact
      ──normalize──▶ Chatlas.Normal.Model
      ──annotate───▶ Diagram.Annotations
      ──select─────▶ Context.Model
      ──supply─────▶ user-agent collaboration
```

Evidence inspection and audit travel in the opposite direction:

```text
Context.Model
      ──expand─────▶ Diagram.Annotations
      ──resolve────▶ Chatlas.Normal.Model
      ──verify─────▶ Chat.Raw.Artifact
```

Meaning accumulates toward the `Context.Model`; evidentiary authority
accumulates toward the `Chat.Raw.Artifact`.

## Progressive Interpretation

`Chat.Raw.Artifact` preserves provider-native evidence. It retains the
greatest source detail while making the fewest Tarav interpretations.

`Chatlas.Normal.Model` turns provider-specific chats into a shared causal
tape of sessions, events, turns, content, and context horizons.

`Diagram.Annotations` retain typed claims from which consumers project semantic
structure. The Namespace containing an Annotation defines its base meaning,
required assertions, and any evidence or support policy. Annotation types may
add narrower structure and assertions.

`Context.Model` selects and organizes relevant Diagram material for a
particular collaboration. It is a contextual projection, not a new
authority surface.

The supplied context enriches further user-agent collaboration, which
captures more touched chat data and continues the loop.

## Responsibility Boundaries

The data train is layered so no component must carry all of Tarav's
complexity:

- `Tarav.Archive` preserves Artifacts without understanding chats.
- Chatlas understands chats without constructing Diagram ontology.
- `Tarav.Diagram` retains typed, assessable structure without parsing
  provider-native artifacts.
- Contextualization selects useful structure without becoming its
  authority.

Capture therefore precedes interpretation. Higher layers remain
inspectable through lower layers, derived layers can evolve without
rewriting their evidence, and faults in normalization, annotation, or
selection can be surfaced independently.

## Diagram Namespaces

The main `Tarav.Diagram` is composed from `Diagram.Namespace`s. A Namespace is
an independent Git repository, a flat Annotation tape, and the semantic policy
used to interpret that tape. Namespaces let the same Diagram mechanics serve
different semantic systems without mixing their authority or repository
history.

Conceptually:

```text
Tarav.Diagram
  ├── Namespace A repository → flat Annotation tape
  ├── Namespace B repository → flat Annotation tape
  └── Namespace N repository → flat Annotation tape
```

Each Annotation belongs to exactly one Namespace. A Namespace may reference
Annotations or projected objects from other Namespaces, but those references
do not move or duplicate the target's authority.

A Namespace owns:

- a stable Namespace identity and human-facing name;
- one independent Git repository and Annotation tape;
- its accepted Annotation types and their runtime specializations;
- the base Assertions applied to every Annotation it contains;
- its support, evidence, addressing, and other semantic policies.

Namespace type allowlists and policies guide normal writers and produce
validation findings. They do not make the Diagram unwritable: a disallowed,
incomplete, or unassessable Annotation may still be retained while its state is
surfaced as a POI.

Creating a Namespace is analogous to `git init`. It initializes a
self-describing repository with a Namespace definition and an empty Annotation
tape. Mounting that repository into a Diagram load path is a separate,
machine-local operation; creation may perform both operations as a convenience.
The default physical depot for Namespace repositories is
`~/Documents/tarav/diagram/`; each Namespace remains its own Git repository.

The Diagram resolves bare Annotation identities by searching mounted
Namespaces in load-path order. A stable, exact reference includes both the
Namespace identity and Annotation identity. Search order is a convenience for
discovery and does not redefine Annotation identity.

### Flat Annotation Tape

A Namespace repository stores no separate Model, Block, or Line collections.
Its only semantic records are Annotations:

```text
<namespace-repository>/
├── .git/
├── namespace.json
└── annotations/
    ├── <annotation-uuid>.json
    └── ...
```

Models, Blocks, Lines, relationships, and other semantic objects are
projections obtained by interpreting and folding the flat Annotation tape.
They are not parallel storage authorities.

The canonical implementation path is a full projection of that tape. A later
incremental index may accelerate the same computation, but it must remain
equivalent to the full projector and cannot become a second authority.

### Diagram Object Types

The retained Annotation `type` selects the Python class that owns how the
record contributes to projection. Parametric Annotation types additionally
retain full Diagram Object.Type names:

```json
{"type": "Diagram.Block.Annotation", "block_type": "Design.Block"}
{"type": "Diagram.Line.Annotation", "line_type": "Design.Line.Principle"}
```

Full Type names are record data. Compact codes such as `PR` are rendering
conventions only. Existing records with no Object.Type remain readable through
the generic `Diagram.Block` and `Diagram.Line` classes while surfacing a
missing-Type POI. Unknown, conflicting, or Namespace-disallowed Types likewise
remain writable and recoverable through generic objects while surfacing POIs.

Every Object.Type has two complementary semantic surfaces: an addressable
Definition.Block for Agents and users, and a Python class for executable
mechanics. A class exists only when code must parse or operate on the Type; a
Definition.Block explains intention and meaning. Parametric Record types define
where their Type parameters occur and which values they accept.

The runtime Object.Type registry retains the Definition.Block ship UUID rather
than one Block edition, allowing the definition to evolve through its lineage.
Definition.Blocks resolve through the mounted Diagram, so they need not live in
the consuming project's Model or Namespace. Missing or ambiguous resolution
surfaces a POI without blocking capture.

A Block.Type owns the Line.Type vocabulary valid inside that Block. The normal
design vocabulary belongs to `Design.Block`:

- `Design.Line.Definition` (`DF`)
- `Design.Line.Decision` (`DC`)
- `Design.Line.Constraint` (`CT`)
- `Design.Line.Rejection` (`RJ`)
- `Design.Line.Principle` (`PR`)
- `Design.Line.Freedom` (`FR`)
- `Design.Line.Example` (`EX`)

`Design.Block` does not make its heading a semantic commitment and does not
require a privileged Definition Line. Content gives a Block its semantics;
Type contributes explicit mechanics and assessable conformance claims.

`Impl.Req.Block` is the User-Touched Diagram surface for one implementation
request. It groups supported User-Touched material relevant to that request
across its design and execution chats. A numerical label such as
`502.Impl.Req` is a human-facing address; the Block ship UUID remains its
identity. This work grouping does not claim that the request is a project
ontology concept.

The Block is not the implementation's main coordination artifact. The Agent
maintains a separate live-note `Impl.Req` containing `Impl.Abstract`, an
`Impl.Req.Diagram` reference to the Block, `Execution.Plan`, and `Impl.Log`.
Agent-only plans, status, logs, summaries, and incidental observations may live
there without becoming User-Touched Diagram Lines. During design and execution,
the workflow enriches the Block only with relevant material grounded in the
corresponding User-Touched chat data.

Initially, `Impl.Req.Block` accepts the same Line.Type vocabulary as
`Design.Block`. It retains a distinct Block.Type so implementations can select,
render, validate, and contextualize implementation work independently and add
specialized mechanics later without changing its identity.

`Issue.Block` is the addressable Diagram surface for a temporary concern such
as an idea, reminder, question, opportunity, defect, migration, or
contradiction. Parking is a workflow that creates an `Issue.Block`; it does not
introduce a `Parking.Note` Object.Type or separate storage surface.

Initially, `Issue.Block` accepts the Design-family Line.Type vocabulary and the
specialized `Issue.Line.Resolve` Type. An Issue projects as open until a Resolve
Line has a passing reviewed `Verbatim.Gate`. A missing, failed, or unassessable
review leaves the Issue open and surfaces an `issue-open` POI without blocking
mutation. A later ordinary Line does not stale a passing resolution.

Each Annotation class owns how its record contributes to a projected object.
Projected Line and Block assertion surfaces recursively expose the Assertions
of their contributing Annotations and contained objects. Assertion identities
are preserved so a linter can evaluate by level without evaluating one
Assertion twice.

### User-Touched Chatlas Index

`User.Touched.Chatlas.Index` is the first, default, and fundamental Namespace.
It uses Chatlas as its evidence model and projects the Model/Block/Line
knowledge structure grounded in `User.Touched.Data`.

Other Namespaces may use unrelated semantics, Annotation types, and support
policies while reusing Diagram identity, storage, specialization, assertion,
scoring, querying, and POI mechanics. This allows speculative or Agent-authored
material to remain available without polluting the User-Touched index.

## Chatlas Foundation

Chatlas is an integral part of Tarav and the native evidence model of the
`User.Touched.Chatlas.Index` Namespace.

Chatlas captures selected provider-native material into a Git-tracked raw
repository suitable for registration by `Tarav.Archive`. It then derives
the normalized causal tape used by the Diagram.

Annotations in this Namespace use Chatlas references for support and producer
coordinates rather than direct references into provider-native Artifacts. A
Chatlas reference
must remain able to resolve its normalized subject and expose the Archive
references supporting it.

Conceptually:

```text
Diagram.Annotation
      ↓ Support.Set / Producer
Chatlas.Reference
      ↓ normalized subject and provenance
Chatlas.Normal.Model
      ↓ source evidence
Archive.Reference
      ↓
Chat.Raw.Artifact
```

For every member of an Annotation's `Support.Set`, the referenced content
must have been present in the Annotation's producing chat context before
the producing turn. This is assessed by resolving the support content and
inspecting the producer's preceding chat horizon; it does not require a
separate materialization record.

### Rooted Support Sets

In `User.Touched.Chatlas.Index`, an Annotation's `Support.Set` is a set of
rooted support members. Every member designates one `User.Turn` as its root and
may select a bounded neighborhood of companion User or Agent turns needed to
interpret that touch.

```text
Support.Set
└── Support.Member
    ├── root: User.Turn
    └── neighborhood: selected companion User or Agent turns
```

The root establishes the qualifying `User.Touch`. Neighborhood turns preserve
interpretive context but do not replace that root. When several User turns
independently support an Annotation, they may be represented by several rooted
members rather than one unstructured collection of messages.

Support references must identify both the Chatlas session and exact Turn
edition they address. This permits the Diagram to resolve cross-chat support,
render each selected neighborhood in causal order, and let consumers expand
beyond that selection when necessary.

A later User touch does not retroactively enter an older Annotation's producing
context. It is recorded through a new Annotation on the same semantic lineage,
including a support-only Annotation when no new wording is needed.

## Monolithic Library

Tarav is one monolithic library. Archive, Chatlas, Diagram, and
Contextualization are responsibility and data boundaries rather than
separate packages or services.

Diagram Annotations are retained as typed data and instantiated by the Tarav
library as runtime objects. The retained data stores irreducible
instance-specific facts. Namespace- and type-level rules and reliably
recoverable values may be supplied or derived by code. Data is duplicated only
when a material robustness benefit justifies it.

The only universally required retained Annotation field is `type`:

```json
{
  "type": "<Annotation.Type>"
}
```

This is the minimum common field, not a prohibition against additional fields.
Producer, support, location, payload shape, and other facts belong to the
containing Namespace or specialized Annotation type. An Annotation's identity
comes from its record address, and its Namespace comes from the repository
containing it; neither needs to be duplicated inside the retained data.

The constitutional requirement that Diagram Annotations link to archived data
does not require one universal retained field. A Namespace may retain or
reliably derive that linkage according to its own model. Missing or
unresolvable archival grounding must surface through its Assertions and POIs;
it does not prevent the writable Diagram from retaining the Annotation.

The generic runtime object therefore exposes only its identity, Namespace,
declared type, and opaque retained record. Its Namespace supplies base
Assertions and specialization behavior. A specialized type may add Assertions
but cannot remove the Namespace's base Assertions.

Support is not a universal Diagram field or status. A Namespace may define
direct User support, support derived through referenced Diagram objects,
mechanical support, or another policy. Support status remains distinct from
Assertion scoring: `UnAsserted` means that required Assertion scores are
missing or unresolvable, not merely that direct User support is absent.

### Runtime Type Specialization

One retained Annotation Record is loaded first as one generic
`DiagramAnnotation`. Generic loading exposes the common identity, Namespace,
type, opaque record, and universal Annotation behavior without requiring the
runtime to understand its declared type.

When a consumer needs type-specific behavior, it explicitly specializes that
object:

```python
annotation = diagram.annotation(annotation_id)
typed = annotation.specialize()
```

`specialize()` asks the Annotation's Namespace to select a registered class
from the retained `type`. The specialized class is the code-owned home for that
type's parsing, navigation, assertions, and other behavior. In
`User.Touched.Chatlas.Index`, the first specialized types include Line and
Line-support Annotations.

Specialization is strict. An unknown type or data that does not satisfy its
registered class raises an ordinary error. Generic access remains available,
but Tarav does not prescribe whether the caller should retain it, report the
error, skip the Record, or stop its operation.

## Gates and Review

A Gate is a reusable set of mechanically evaluated Assertions over retained
collaboration evidence. Gate evaluation never blocks Diagram mutation. Failed,
missing, and unassessable Gate Assertions surface POIs.

`Verbatim.Gate` is a proxy for explicit User review of one exact Line wording.
Its retained instance data is:

```json
{
  "type": "Verbatim.Gate",
  "token": "<opaque-token>",
  "proposal_turn": "<Agent Chatlas.Turn.Reference>",
  "approval_turn": "<User Chatlas.Turn.Reference>"
}
```

The token is an opaque nonce, not a content hash. The Gate passes only when
the proposal resolves to an Agent turn containing both the token and
materially equivalent Line wording, and a later User turn in the same chat
explicitly approves that token.

A newly captured `Diagram.Line.Annotation` may retain its Gates directly.
Reviewing an immutable existing Line wording creates a separate record:

```json
{
  "type": "Diagram.Line.Gate.Annotation",
  "target_annotation": "<existing Diagram.Line.Annotation UUID>",
  "gates": [{"type": "Verbatim.Gate", "...": "..."}]
}
```

The target supplies the wording, Model, Block, and Line lineage. The gate-only
Annotation does not rebind or duplicate that target. One review exchange may
cover several Lines; each exact target receives its own independently
assessable gate-only Annotation.

Gate records retain no authoritative passed flag. Tarav recomputes Gate
standing from the target record and Chatlas evidence. A Line ship is
`Reviewed` when at least one exact Line Annotation in that lineage has a
passing `Verbatim.Gate`. Later ungated lineage members do not erase that
standing; their continuity remains a separate Assertion.

Capture has no Gate-specific contract. A `Capture.Manifest` transports typed
Annotation records without interpreting their semantics. The Namespace
specializes each record from its `type`; the resulting Tarav class owns its
schema, model location, Assertions, mechanical checks, and findings. Gate
Annotations therefore travel through the ordinary Capture path without adding
Gate commands or Gate branches to Capture.

## Assertion Evaluation

`Assertion.Engine` is the central read service for current Assertion state.
Annotation types declare Assertions, registered evaluators implement their
mechanical assessment, and the Engine resolves available evidence and produces
the Annotation's current `Annotation.Score.Vector`.

Renderers, linters, contextualizers, and other consumers request Assertion
state from the Engine. They do not evaluate Gates or other Assertion types
independently.

The Engine combines retained scores with mechanically recomputed scores without
writing derived truth into the immutable Annotation Record. A mechanically
derived result may be cached as disposable data, but it is never authoritative
Annotation content.

Assertion state distinguishes `NotEvaluated`, when no score or applicable
evaluation result exists; `Unassessable`, when evaluation lacks resolvable
evidence; `Passed` and `Failed` Boolean scores; and other `Scored` values.

An Annotation remains `UnAsserted` while any required Assertion is
`NotEvaluated` or `Unassessable`. A falsy score is still an asserted result and
surfaces a POI without making Diagram mutation invalid.

## Named Renderers

Diagram Renderers are named, read-only code projections over Diagram objects.
They create no Annotations and hold no Diagram authority. Several Renderers may
present the same object differently without requiring their surfaces to agree.

Each Renderer declares a stable name, accepted target kind, output media type,
and implementation. Renderer selection is explicit:

```bash
tarav diagram render \
  --line-ship <uuid> \
  --renderer Kernel.Writing.Line.WithSupport
```

Renderer discovery is mechanical through `diagram renderer list` and
`diagram renderer show`. Native output is written to stdout; `--json` returns
an envelope containing the Renderer name, target, media type, content, and
findings.

A Line Renderer projects the Line ship rather than treating one Annotation as
the Line. When exactly one wording Annotation exists, it may render that
wording directly. When several wording Annotations exist without an explicit
selection, a mechanical Renderer must not silently choose the latest: it must
render the variants and surface the unresolved selection as a POI.

Support-aware Renderers preserve exact rooted Chatlas verbatims and navigation
references. Contextualizing Renderers include available Assertion scores and
surface `UnAsserted` state rather than hiding it.

## User-Touched Semantic Lineages

`User.Touched.Chatlas.Index` is intended to support a knowledge graph grounded
in `User.Touched.Data`. A chronological chat tape alone is not sufficiently
structured for contextualization, while a current graph without its reasoning
history loses how the user's ideas developed.

The candidate semantic hierarchy is:

```text
Model
  └── Block
        └── Line
              └── Annotation
                    └── Chatlas support
```

These are projected objects, not stored collections. Typed Annotations create,
address, and change Model, Block, and Line lineages. An addressable `Line`
groups its Annotations into one atomic semantic history. A `Block` groups Lines
into a larger addressable semantic unit. A `Model` groups Blocks into a
consumable interpretation for a project, question, or other purpose.

Each retained Annotation has its own Annotation identity. Model, Block, and
Line identities are separate semantic ship UUIDs carried by the Annotation
types that participate in those lineages. A root Model Annotation establishes
a Model ship in one Namespace; folding the relevant tape material produces the
current Model projection.

A `Diagram.Block.Annotation` establishes a Block ship within a Model and may
retain its human-facing label. The label is a schema-shaped rendering and
lookup aid, not the Block's identity or semantic definition. Line Annotations
locate their Line ships within one Model and Block context.

Object.Types may be assigned after content capture through support-free
curation Annotations:

```json
{
  "type": "Diagram.Block.Type.Annotation",
  "location": {"model_ship": "<uuid>", "block_ship": "<uuid>"},
  "block_type": "Design.Block"
}
```

```json
{
  "type": "Diagram.Line.Type.Annotation",
  "location": {
    "model_ship": "<uuid>",
    "block_ship": "<uuid>",
    "line_ship": "<uuid>"
  },
  "line_type": "Design.Line.Constraint"
}
```

These Annotations add no wording and require neither a `Support.Set` nor a
producer chat. They reference existing projected objects whose content retains
its own support, contribute only to Object.Type projection, and expose a
Type-conformance Assertion. Missing or poor conformance scores surface POIs
without blocking the assignment.

Like the root Model Annotation, a Block declaration is structural bookkeeping:
it does not require a producer or direct `Support.Set`. The support of the
projected Block comes from the supported Annotations attached to it. A later
semantic operation on the Block, such as a supported rename, may be represented
by its own Annotation rather than retroactively adding support to the original
declaration.

`Line`, `Block`, and `Model` identities are semantic lineages rather than
fixed wordings or fixed collections. Their identities persist through
editions. An edition may rephrase an idea, add or remove material, or reflect
the evolution of the user's position without requiring a new identity.

This is the Ship-of-Theseus problem applied at every grouping level. The
fundamental lineage claim is:

> Despite these changes, treating these editions as the continuing history
> of one addressable thing remains semantically coherent.

Continuity is not semantic equivalence. Two expressions may differ or even
record a changed user position while remaining useful parts of one semantic
history. Conversely, superficially similar material may require separate
lineages when grouping it as one continuing thing would be incoherent.

The system must preserve these continuity claims as assessable Assertions.
The expected assertion is strongest and most local at the Line layer and may
become broader as Lines are grouped into Blocks and Blocks into Models.

### Project Model

A Tarav project may name one default Model ship in `.tarav/project.json`:

```json
{
  "diagram": {
    "main_model": "<model-ship-uuid>"
  }
}
```

The project configuration retains only the Model ship UUID. It is an
association, not an ownership claim: several Projects may point to the same
main Model. For example, implementation and documentation Projects belonging
to one system may share one system Model while retaining independent Project
identities and repositories.

The root Model Annotation determines the Namespace that owns the Model, so
Capture does not need a second Namespace target. Associating a Project with an
existing Model does not create, copy, or modify that Model.

If `main_model` is missing, the Project may be associated with an existing
Model or a Capture bootstrap may allocate a Model ship, write a root Model
Annotation to the default `User.Touched.Chatlas.Index` Namespace, and retain
the UUID in the project configuration. Model creation and Project association
remain distinct operations even when one command performs both as a
convenience. A Model with no Line material is an existing empty Model, not a
reason to allocate another identity. A configured Model that cannot be
resolved must surface an error or POI and must not be silently rebound.

Root Model and Block declaration Annotations may lack direct `User.Touch`
support. Their Namespace still supplies assessable base Assertions, and their
projected support is derived from the User-supported material attached within
them. This structural exception does not permit ordinary semantic Line
Annotations to bypass the Namespace's direct-support policy.

## Bad Indexing and Semantic Evolution

Legitimate semantic evolution and incorrect annotation are different
conditions.

Within `User.Touched.Chatlas.Index`, an Annotation that does not honestly
follow from its producing context and declared support is `Bad.Indexing`. It
should be surfaced as a POI and may be amended, replaced, marked, or pruned.
Git history may preserve the former data, but the Namespace must not present an
unsupported Annotation as a valid edition of the user's evolving idea.

A correctly grounded earlier position followed by a correctly grounded
later position is legitimate semantic evolution. The earlier Annotation may
remain in the lineage even when the later position differs from it.

For every member of an Annotation's `Support.Set`, the referenced content
must have been available in the producing Agent's chat context before the
producer turn. Cross-chat support is valid only when the referenced content
was brought into that producing context. This makes it possible to audit
that an Agent derived an Annotation from material it actually received
rather than merely copying support references.

## Context-Local Capture

The current Capture design concerns `User.Touched.Chatlas.Index` and only the
Model or Models being worked on in the producing chat context. It does not
predict how unengaged or future Models may reuse the captured material.

The `NOW` of one capture is the complete bounded context available to the
annotating Agent at its producer turn. A NOW may contain earlier chats,
Models, files, tool results, and other addressed material loaded into the
current chat. The Annotation's `Support.Set` selects the high-signal
`User.Turn`s supporting its claim from within that context.

Every semantic Annotation produced by this Capture workflow is therefore an
interpretation made in one auditable NOW. The Namespace accumulates
Annotations from successive NOWs rather than constructing one timeless
interpretation of the user.

Capture performs only the minimum ontology work needed to locate the
Annotation in the context being developed. A captured Line Annotation is
assigned to a Line ship, a Block ship that contextualizes it, and a Model in
the active capture scope. Capture may work on several Models in one session,
but it concerns only those explicitly engaged Models.

Cross-model reuse, derivation, dependency, mixture, and forking are not
prospective Capture responsibilities. When a later user-agent collaboration
uses one Model to construct or interpret another, that relationship belongs
to the future NOW. It may then be represented through ordinary grounded
Annotations, including relationship Blocks whose Lines reference the related
Diagram objects.

Tarav must provide stable references and navigation primitives that let
Agents describe such relationships. It need not hard-code their semantic
vocabulary into Capture.

## Capture Manifest

User-Touched Capture is an approval-gated collaboration performed in chat, not
a sequence of improvised direct mutations. The chat is the WIP capture surface:
the User and Agent discuss, revise, and approve each Block and Line there.

A `Capture.Manifest` does not exist during that semantic discussion. After the
User sends `::land` for one settled proposal, the Agent creates a Manifest as a
faithful mechanical compilation of the approved material. The Manifest is
neither a collaboration surface nor a Diagram authority surface.

Conceptually:

```text
User/Agent discussion in chat
          ↕ propose / group / revise / approve
Settled capture proposal
          ↓ explicit ::land
Agent creates Capture.Manifest
          ↓
Mechanical check
          ↓
Capture applies
          ↓
Annotations initially remain UnAsserted
          ↓ later
Semantic Assertion scoring
          ↓
Scores + POIs + curation
```

Before landing, Tarav tooling should provide read-only Model projections and
manifest-ready context fragments: Chatlas references, resolved hashes, Diagram
identities, and existing Model, Block, and Line objects. After `::land`, it
should provide an empty Manifest template and freshly minted UUIDs. The Agent
should not reconstruct mechanical bureaucracy by hand.

The Manifest identifies its target Model ship. Resolving that Model identifies
the Namespace repository that owns it and therefore the sole write destination
for the batch. The Manifest does not need a redundant Namespace target.

Semantic capture remains Agentic work, but it occurs in the approved chat
discussion. Post-land Manifest construction may choose mechanical identities
and serialize the result, but it must not introduce new semantic content. If a
mechanical correction requires semantic reinterpretation, landing stops and
the work returns to discussion and approval.

The compact Agent landing-pause turn before `::land` serves as the producer
coordinate for its Annotations. It need not repeat the approved proposal: its
context must already contain the exact approved proposal turns and supporting
User turns. `::land` authorizes materialization; it does not retroactively
supply semantic support or approval.

Manifest checking covers `Mechanical.Semantics`: schema shape, resolvable
references, hashes, reference sides, producer-context inclusion, target
existence, batch-local references, unique identities, and executable
ordering. It may help the Agent revise the Manifest, but it cannot certify
semantic quality.

> Mechanical code may verify that a semantic act is well-formed, traceable,
> and executable; it cannot certify that the semantic act is good.

Applying a Manifest revalidates its mechanical interpretation and
materializes the mechanically executable batch. Formal semantic assessment
is always later work performed through the Semantic Assertion system. Newly
captured Annotations ordinarily remain `UnAsserted` until their Assertions
receive an `Annotation.Score.Vector`; that ordinary state may surface POIs
but does not make capture a semantic-scoring workflow.

Git commit policy is an apply-time option, not Manifest data. Normal Capture
application writes and commits the batch in its Namespace repository. A
development caller may explicitly request an uncommitted application; this
changes only materialization behavior and leaves the Manifest unchanged.
Uncommitted Annotations are outside a stable Diagram version until the
developer commits them through Git.

## Models and HEADs

There is no single mechanically derived `Tarav.Diagram.HEAD`.

Different projects, questions, and consumers may construct different Models
from the same normalized tape and Diagram material. These Models may make
different compatible or incompatible selections while remaining grounded in
the same evidence.

A Model may maintain its own `HEAD`: its currently selected edition for a
particular contextualization purpose. Producing or updating that HEAD is
interpretive work for an Agent. Tarav should provide simple mechanics,
support, scoring, references, and POIs without hard-coding a general semantic
fold.

Capture updates only the Models in its active scope. Model composition and
cross-model relationships are interpreted when a user-agent collaboration
works on them; Capture does not maintain or propagate speculative future
dependencies.

## Open Design Boundaries

The following mechanics remain deliberately unresolved:

- selection semantics for evolving Line, Block, and Model editions;
- how an Annotation identifies the exact Block edition that contextualized
  its wording;
- whether and how one Annotation or Line may participate in several Blocks;
- how forks and later reunification of semantic lineages are represented;
- how continuity Assertions are evaluated and scored at each layer;
- how Agents construct, update, and compare Model HEADs;
- the exact primitives through which future NOWs express Model composition
  and cross-model relationships without expanding Capture's responsibility.

These are implementation and further-design questions. They must preserve
the grounded reasoning tape, plural agent-constructed Models, assessable
continuity, and the distinction between semantic evolution and Bad Indexing.
