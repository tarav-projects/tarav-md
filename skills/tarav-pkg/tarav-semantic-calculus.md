# Tarav Semantic Calculus

This document describes Tarav's current candidate design for constructing,
evolving, and evaluating semantic annotations. It is subordinate to the
[Tarav Constitution](CONSTITUTION.md), complements
[Tarav.Diagram](tarav-diagram.md), and remains amendable.

## Purpose

Tarav captures `User.Touched.Data` before requiring mature semantic structure.
Agents may then derive useful claims, relationships, and decompositions from
that evidence. Every derived semantic structure remains assessable rather than
becoming unquestioned fact.

The general system is `Semantic.Calculus`:

```text
Evidence and existing semantic objects
                ↓
       Semantic.Computation
                ↓
    semantic objects and relations
                ↓
        Semantic.Assertions
                ↓
         Assertion.Scoring
                ↓
scores, evidence, uncertainty, and POIs
```

Agents supply semantic interpretation. Deliberately small mechanics retain
identity, provenance, support, histories, scoring evidence, and navigation.
The calculus remains open to new semantic objects, relations, computations,
and Assertions rather than requiring a closed ontology or algebra.

## Semantic Claims

A semantic object or declared relation produced by the calculus is a claim.
Its representation does not become authoritative merely because an Agent or
mechanic produced it.

A `Semantic.Computation` derives semantic objects or relations from evidence
or existing semantic objects. Every computation must declare the
`Semantic.Assertions` by which its outputs can be evaluated and scored.

This permits progressive structure:

```text
capture a useful claim
        ↓
retain evidence and provenance
        ↓
derive finer semantic structure later
        ↓
score each derived claim and relationship
```

Tarav can therefore capture before it knows the final schema, decomposition,
or ontology. Later enrichment adds assessable structure without invalidating
the original capture.

## Index Lines

An `Index.Line` is a supported semantic claim selected as one orthogonal
indexing unit within a Block.

Its minimal interpretation context consists of:

```text
Line.Context
├── containing Block
└── Support.Set
```

Orthogonality is relative to peer Lines at the Block's current resolution. It
does not claim that a Line is permanently or universally indivisible.

The Line remains the supported Block-level indexing claim even when later
computations expose finer structure. It is not called an Atom: decomposability
does not make the capture defective, and capture-time selection does not claim
ultimate semantic irreducibility.

Although Chatlas provides Tarav's strongest current capture primitives, the
Line model applies generally to supported claims over immutable evidence.

## Line Key/Value Decomposition

`Line.KeyValue.Decompose` is a `Semantic.Computation` that derives two semantic
sublines implicit in an original Line:

```text
Original Line
├── Line.Key
└── Line.Value
```

The sublines are semantic statements, not textual substrings or primitive
database fields. Each must be independently supportable by the evidence.

The computation is evaluated by
`Line.KeyValue.Fidelity.Assertion`:

> Do `Line.Key` and `Line.Value` together preserve the original Line's
> meaning?

The original Line remains the provenance and interpretation surface for the
decomposition. Decompositions may remain implicit, admit competing candidates,
or recurse into finer sublines when further resolution is useful.

This lets Tarav extract supported facts first and discover their latent design
variables later.

## Theseus.Identity

Every Diagram semantic UUID is a `Semantic.Ship`. The UUID is a nonsemantic
address for one claimed existence. It says only that one addressable something
exists; descriptions and contracts supply the meaning of that something.

Reusing a Ship UUID across changing descriptions makes the continuity claim:

> These descriptions remain editions of the same something.

Allocating a new UUID claims a distinct existence. Rebinding an existing UUID
to an unrelated semantic lineage violates `Theseus.Identity`.

Annotation Ships retain one current Record in HEAD while Git preserves their
preceding editions. Other semantic Ships, including Lines, Blocks, and Models,
are projected from the Annotations carrying their UUIDs.

## Ship History

`Ship.History.Resolve` retrieves the raw editions of a Ship without
interpreting their historical schemas. Its stable responsibility is identity
and retrieval, not semantic migration:

```text
Ship.History.Resolve(namespace_uuid, ship_uuid)
    → raw editions with Git revision and available history topology
```

The common history is a simple ordered lineage, but histories may branch. The
resolver preserves ordering and topology available from the authoritative
data while remaining schema-blind.

Git and Diagram data remain the source of truth. A separate authoritative
Ship registry is rejected because it duplicates identity and risks
synchronization drift. Disposable, rebuildable indexes remain permitted.

Historical storage adapters are retained only when immutable layouts cannot
be migrated. Otherwise authoritative data and current mechanics move forward.
All unavoidable compatibility burden is concentrated in this smallest
identity-and-retrieval kernel.

## Ship Key and Value

A `Semantic.Ship` can be understood through three roles:

```text
UUID        stable mechanical address
Ship.Key    evolving description of the semantic something being tracked
Ship.Value  edition-specific descriptions or states of that something
```

The Key also has editions. A later Key edition may restate, enrich, or
generalize the Key while every prior `Ship.Key.Assertion` continues to carry.
The effective identity is therefore not merely the latest Key wording; it is
the carried Key history.

Values need not change at every edition:

```text
Key     “the color of boat X”
v0      red
v1      red
v2      green
```

The repeated value is still an edition. The transition to green breaks a claim
of value sameness without necessarily breaking Ship continuity.

A Line may initially contain its Key/Value pair implicitly. Later semantic
computation can expose the stable Key and changing Values. Across sufficiently
varied, well-indexed histories, stable Keys emerge as design variables and
Value transitions expose decisions, states, revisions, or rejections.
Repetitive history provides no guarantee of improved resolution.

## Ship Continuity and Assertion Carry

`Ship.Continuity.Assertion` evaluates whether Key carry preserves one semantic
something across editions.

`Assertion.Carry` is the more general question:

> Does a particular Assertion's standing remain applicable across this Ship
> transition?

Continuity and carry are related but distinct. Identity continuity does not
require every asserted property to remain unchanged. Value Assertions may
carry across unchanged values or break when a Value changes while the Ship
continues.

A Ship contract may strengthen this boundary by requiring particular
Assertions, or all applicable Assertions, to carry. Carry semantics belong to
current mechanics and do not introduce an independent legacy-compatibility
system.

A Ship history may branch. Failed or diverging Key carry may produce
descendant Ships retaining shared ancestry. One UUID must not permanently bind
several distinct somethings.

Cross-support Key carry supplies merge evidence:

- one-directional carry may indicate identity, generalization, or containment;
- reciprocal carry is stronger evidence that two Ships may be merged;
- carry is a scored merge signal, not an automatic merge command.

## Assertion Scoring

`Assertion.Scoring` is Tarav's general system for accumulating evaluation
evidence and deriving scores for declared `Semantic.Assertions`.

`Assertion.Ranking` is its main current primitive. It retains an Agent's
relative ordering of candidate presentations under one Assertion. Repeated
rankings let strong examples provide an empirical definition-by-examples
without requiring one absolute mechanical definition.

Assertion.Scoring may add other primitives without changing its fundamental
boundary:

> Assertion.Scoring publishes inspectable evidence and derived scores; it does
> not convert scores into truth.

A published score exposes the evidence needed to judge its standing, including
its method, rankings, opponents, judges, controls, presentation order,
uncertainty, and underlying verdicts.

Accumulated scoring evidence is analogous to proof of work: it demonstrates
that substantial, inspectable evaluation occurred. It does not prove the
conclusion true, but robust work across varied comparisons and controls makes
catastrophic pathological failure less likely.

Relative ranking alone cannot establish that the strongest candidate is good.
Controls and inspectable provenance provide calibration.

## Continuity Controls

`Continuity.Control.Ladder` produces matched corruptions from real Ship
histories:

```text
real
  > mildly reordered
  > partly intermixed
  > strongly intermixed
  > fully randomized
```

Matched controls reuse real history material so format, vocabulary, length,
schema versions, and complexity remain comparable. Control-generation
protocols and difficulty bands must be versioned and visible so improvement
cannot be simulated merely by making controls easier.

`Continuity.Separation.Profile` measures the distribution of real-history
scores against their matched corrupted histories. A robust evaluator should
produce a roughly monotonic decline along the corruption ladder.

This profile measures how visibly semantic continuity separates from
corruption across a population. It does not prove any individual Ship correct.
Better capture should make real histories separate more clearly from their
matched controls over time.

Weakly separated or low-scoring real histories surface POIs for Agent or User
investigation, repair, splitting, or reattachment.

## Deferred Audit and Migration

Semantic capture and Assertion.Scoring are independent workflows. A captured
claim may remain `UnAsserted` until a later audit, possibly after several
schema migrations.

A delayed audit uses current mechanics to present:

1. the current claim;
2. its immutable support;
3. progressively disclosed raw Ship history when representation drift creates
   uncertainty.

The audit mechanic need not parse every historical schema. Raw editions let an
Agent interpret relevant changes, and progressive disclosure avoids paying
that cost when the current claim and support are already clear.

Migration continuity and every other `Semantic.Assertion` are orthogonal.
Strong continuity does not establish grounding, fidelity, type conformance, or
another property. Scoring provenance must expose whether standing was assessed
directly against the current edition or carried from an earlier edition.

Internal representation changes need not become target User-semantic events.
Git and raw Ship history retain their mechanical evolution without polluting
the semantic history being indexed.

Migrations advance data and mechanics into the current system. Problems found
by current scoring become POIs repaired within that system rather than reasons
to permanently retain every legacy semantic parser or migration mapping.

## Bad Indexing

Semantic continuity does not repair `Bad.Indexing`. A consistently carried
claim may remain consistently unsupported or wrong.

Grounding, computation fidelity, continuity, carry, and other Assertions remain
independent scoring axes. A migration may preserve the meaning of a badly
indexed claim perfectly. Conversely, a well-grounded edition may be attached
to an incoherent Ship history.

Tarav surfaces these distinctions as evidence and POIs rather than collapsing
them into one Boolean notion of validity.

## System Loop

The complete semantic-annotation loop is:

```text
Theseus.Identity
    → UUID reuse claims continuity

Ship.History.Resolve
    → retrieves history without interpreting old schemas

Semantic.Computation
    → proposes semantic objects, relations, and decompositions

Semantic.Assertions
    → make every derived claim assessable

Ship.Continuity.Assertion + Assertion.Carry
    → evaluate identity and standing across change

Assertion.Scoring
    → accumulates inspectable evaluation evidence

Continuity.Control.Ladder + Continuity.Separation.Profile
    → calibrate continuity against matched corruption

Weak tail
    → POIs for Agent/User repair, splitting, merging, or reattachment
```

Tarav does not need one absolute mechanical definition of semantic continuity.
It needs stable identities, inspectable histories, declared computations and
Assertions, controlled corruptions, comparative judgments, and transparent
evidence.

## Open Design Boundaries

This design deliberately does not yet fix:

- the retained schemas for explicit Ship Keys and Values;
- the representation of branching histories and ancestry;
- the API through which a Ship contract strengthens carry requirements;
- the exact record types for Semantic.Computations and their output relations;
- the scoring and aggregation methods derived from Assertion.Rankings;
- the control-generation protocols and hard-negative families;
- the curation workflows for Ship splits, merges, and reattachments.

These mechanics may evolve while preserving the core boundary: semantic
structure is Agent-derived, evidence-backed, independently assertable, scored,
and repairable.

## Diagram Provenance

This candidate document consolidates reviewed Lines landed in the `Tarav`
Model (`b7b78eab-e5c2-4610-9bf5-1b704a106f34`) at Namespace commit
`5f65898651dd5e4421482321a0d794339c814d21`:

- `Theseus.Identity` — `d0751ea1-d4ef-493c-a4c3-ad747bfef12d`
- `Semantic.Calculus` — `ee87efdb-cde1-4809-9915-da4d708f907f`
- `Index.Line.Semantic.Decomposition` —
  `c5522b1f-a769-43b5-afcb-f9ad9a41d416`
- `Ship.Key.Value.And.Continuity` —
  `2310f354-ffed-46b6-88fd-3a11963d52b7`
- `Assertion.Scoring.And.Continuity.Controls` —
  `e22e51cc-bf92-4369-9b2c-36a6c990ffd2`
- `Deferred.Assertion.Audit.And.Migration` —
  `6f2f010d-ecc9-4832-aeb1-993bfb760425`
