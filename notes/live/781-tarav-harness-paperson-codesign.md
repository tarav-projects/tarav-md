# 781 — Tarav.Harness and PaperSON co-design — live note

Status: Working design

## Session

- Provider: `codex`
- Native session: `01a07228-313a-7ab3-b6e0-aedcb5216b3c`
- Chatlas identity: `33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd`
- Chatlas model commit at note creation: `ff20d87e151bd4b9552ab0d068c4bc0cb45f52d6`

This note records the rationale and working plan developed in the linked
conversation. It is a live design surface, not an approved constitutional
amendment or a substitute for later durable Tarav and PaperSON design.

## Motivation

PaperSON's primary goal remains straightforward:

> Turn a scientific paper's scattered native evidence into one canonical,
> machine-usable `Normal.Model`.

The difficult part is making that extraction process scale without requiring
every result to be reviewed manually forever. Up-front prompts, tools, schemas,
and agent instructions help, but they cannot prevent every poor extraction.
PaperSON therefore needs two complementary quality fronts:

- **A priori:** give agents precise types, tools, context, and bounded actions
  so they can produce the best extraction available initially.
- **Posterior:** continuously apply deterministic checks, agent evaluations,
  and selected user review to surface suspicious states as POIs.

The central quality promise is not that PaperSON proves an extraction correct:

> PaperSON progressively reduces the probability that a poor extraction
> remains unnoticed.

Each detected problem should be an opportunity to improve the extraction and,
when useful, the tooling that checks the entire maintained package surface.
New evaluators must be replayable over existing packages, not only applied to
future work. This creates a quality ratchet across both one package and the
whole PaperSON Studio.

## POI-driven maintenance

A POI is a signal for attention, not a verdict that an error exists. A clean
run means only that the current evaluators detected nothing suspicious.
PaperSON packages remain `WIP.Surface`s whose standing may change when new
checks, evidence, or interpretations become available.

Two resolution policies are fundamental:

- A **non-blessable POI** expresses a condition that code can determine must
  change. It resolves only when reevaluation no longer emits that POI. Effort,
  commentary, or acknowledgment is not resolution; the observable state must
  change so the POI predicate no longer holds.
- A **blessable POI** expresses suspicion requiring judgment. It resolves when
  the state changes enough that the evaluator stops emitting it, or when an
  Agent or User retains an auditable blessing for the current situation.

This permits checks to favor recall where rational. A check that catches only
part of an error class can still be valuable, and false positives can be
blessed by Agents. Review cost still matters: grouping, prioritization,
deduplication, and evaluator quality must keep the attention burden useful.
Fixes are never automatic consequences of POIs; Agents or Users perform them.

Blessings are themselves auditable records. They must identify the reviewed
situation, relevant context, authority, and the system state under which the
judgment was made. Changed evidence or evaluation may make an earlier blessing
stale and cause the POI to surface again.

## The common architecture

Tarav.Diagram and PaperSON already converge on the same pattern:

```text
record.type
    → registered Python class
    → declared Assertions and available actions
    → code, Agent, or User evaluation
    → scores, evidence, and POIs
    → fix or bless
    → reevaluate
```

Records retain explicit state. Code supplies the precise behavior, contracts,
navigation, actions, and evaluation associated with each record type. Agents
must be able to inspect both the record and the code-defined description of
its behavior. Code is therefore a primary executable documentation surface.

A system version is the combination of its current records and the code that
interprets them. Records and code evolve together. Type names may change when
useful; they are not permanent merely because they once appeared in retained
data. Migrations must nevertheless be explicit and auditable.

## Tarav.Harness

`Tarav.Harness` is the proposed ownership boundary for reusable primitives used
to build Agent harnesses. The name identifies where developers look for those
primitives; it does not claim that the namespace is one concrete harness or a
factory object.

Its central aim is:

> Make arbitrary systems legible, operable, and self-evaluating for Agents.

The maintained Python distribution remains a modular monolith. The public
namespace is `tarav.harness`, importable by Tarav applications and external
projects such as PaperSON.

### Candidate responsibilities

`tarav.harness` should own only mechanics demonstrated as common across real
consumers:

- typed records and strict `type`-to-class specialization;
- Type registration and Agent-readable type/record introspection;
- `Ship` identity, editions, histories, and continuity primitives;
- Assertions and evaluator contracts;
- scoring evidence and score-vector primitives;
- POI classes, instances, identity, blessability, and blessings;
- generic actions and optional transition descriptions; and
- evaluation and reevaluation of current state.

A `Ship` UUID is semantically void: it is a pure address. Reusing that UUID is
the semantic act claiming that several descriptions or editions remain the
same something. Ships are therefore core Harness primitives rather than
Diagram-only objects. A Type itself may be a Ship whose UUID is embedded in
its class definition; renaming or moving that class need not break the Type's
identity.

Not every UUID-bearing record must be a Ship. Ship semantics apply when a
system deliberately tracks sameness across change.

### Hard dependency boundary

`tarav.harness` must never import Diagram, Archive, Chatlas, Skillware, or the
Tarav CLI. It may depend only on lower-level, domain-neutral foundations.

```text
tarav._core
    ↑
tarav.harness
    ↑
├── tarav.diagram
├── tarav.skillware
└── other Tarav applications

papersonlib ──imports──▶ tarav.harness
```

Harness does not own:

- LLM execution or internal Agent reasoning;
- one prescribed workflow;
- domain schemas, meanings, or transition policies;
- a mandatory storage layout, repository, or Git policy;
- Diagram graphs, Blocks, Lines, support, or contextualization;
- PaperSON extraction and normalization concepts; or
- automatic fixing of POIs.

The framework may describe actions and evaluate their observable results while
leaving Agents and Users as the primary mutators. A domain may decline to
consider a transition complete while non-blessable POIs remain without making
Harness validation itself a global mutation gate.

## Applications

### Tarav.Diagram

Diagram becomes one consumer of Harness. It contributes its Namespace,
Model/Block/Line, Ship and Annotation specializations, Archive-grounded
support policy, projections, contextualization, and Diagram-specific
Assertions. It should no longer be the accidental owner of generally reusable
typed-record, Ship, Assertion, scoring, or POI behavior.

### PaperSON

PaperSON becomes another consumer of Harness. Its records describe native
paper artifacts, transformations, intermediate fragments, canonical Normal
Models, and review evidence. Its classes define what agents can do with those
records and which Assertions evaluate the resulting state.

The PaperSON processing loop is:

```text
inspect current typed state
    → choose an available action
    → Agent performs semantic work
    → evaluate observable result
    → emit POIs
    → fix or bless
    → repeat
```

Agents are flexible processors, but they normally advance the package through
code-defined actions and state transitions. The objective is not to perform
arbitrary work or merely hide POIs. It is to improve the extraction while
resolving each POI through an observable correction or an allowed, auditable
blessing.

## Existing implementation seeds

This is an extraction and convergence effort, not a greenfield rewrite.

Tarav already contains:

- Diagram generic-record loading plus strict runtime specializations;
- typed Ships, editions, Assertions, projections, and POI-producing checks;
- a workflow-neutral `tarav.poi` check runtime; and
- Assertion scoring records, ranking evidence, and score derivation.

PaperSON already contains:

- `papersonlib.graph`, its package records, lineage, builds, and freshness;
- the unified `papersonlib.lint` mechanical checking surface; and
- `papersonlib.poi`, including stable situations, POI classes, dispositions,
  blessing policy, and stale-context detection.

The first task is to identify semantics actually shared by Diagram and
PaperSON. Code should move into Harness only after these independent consumers
demonstrate the same meaning. Domain policy remains with its consumer.

## Known PaperSON type collision

Current PaperSON graph registries use their containing folder as the record
kind discriminator. An object record's `type` field names its domain object
type rather than the Python record class. This conflicts with the proposed
Harness invariant that every retained record has a `type` resolving to exactly
one class.

The migration must separate those roles. One candidate shape is:

```json
{
  "type": "PaperSON.Object.Record",
  "object_type": "<domain object type>",
  "file": {},
  "provenance": {}
}
```

This is a design direction, not yet a settled schema. It must preserve the
current graph's useful principle that source-ness is derived from lineage; the
redesign must not revive the retired source/entity-class model accidentally.

## Co-design plan

### Phase 1 — Set the constitutional and architectural frame

- Define `Tarav.Harness` in active Tarav design.
- Reconcile the Constitution's contextualization-centered Purpose with
  Harness as a reusable foundation and Diagram as one principal application.
- Establish `tarav.harness` as a public, lower-level namespace with the hard
  dependency boundary above.
- Record that Tarav remains one modular-monolith distribution.

### Phase 2 — Inventory the shared semantics

- Compare Diagram specialization, Assertions, POIs, and scoring with
  PaperSON graph, lint, POIs, and dispositions.
- Classify each candidate primitive as truly shared, Tarav-specific,
  Diagram-specific, or PaperSON-specific.
- Refuse speculative abstractions supported by only one consumer.

### Phase 3 — Implement one complete Harness vertical slice

Build the smallest end-to-end path that can:

1. load a retained record;
2. resolve its `type` to one registered class and Type Ship;
3. render its contract and available actions for an Agent;
4. declare and evaluate Assertions;
5. emit one blessable and one non-blessable POI;
6. retain an auditable blessing when permitted; and
7. reevaluate after correction or blessing.

The slice should use real existing behaviors rather than a synthetic demo.
PaperSON's `DataType.ClassificationRequired` is a useful non-blessable case;
`Source.AdmissionRequired` or `Source.Drift` is a useful blessable case.

### Phase 4 — Make Diagram the first in-tree consumer

- Move or adapt only the primitives exercised by the vertical slice.
- Change Diagram to consume them through `tarav.harness`.
- Preserve Diagram's current records, rendered behavior, validations, and
  writable-in-the-presence-of-POIs property.
- Keep Archive, Chatlas, projection, and contextualization policy in Diagram.

### Phase 5 — Make PaperSON the second consumer

- Add the Tarav distribution as a `paperson-py` dependency while importing
  only the public `tarav.harness` boundary.
- Define PaperSON-owned typed record classes, Assertions, actions, and state
  interpretations in `papersonlib`.
- Resolve and migrate the current `type` collision explicitly.
- Keep `paperson-cli` a thin adapter over `papersonlib`.
- Exercise the complete loop on one real PaperSON package and one narrow path
  from source evidence toward its Normal Model.

### Phase 6 — Replay and grow

- Run the new evaluations across every maintained PaperSON package.
- Treat surfaced POIs as expected migration and quality signals.
- Add further deterministic checks, controlled Agent evaluations, and review
  surfaces according to expected value versus review cost.
- Replay each useful evaluator improvement across the whole package surface.
- Promote additional primitives into Harness only after repeated use proves
  their shared semantics.

## Initial acceptance signals

- `tarav.harness` imports no Tarav application domain or CLI.
- Diagram uses the public Harness primitives without behavioral regression.
- PaperSON imports `tarav.harness` without importing Diagram or Chatlas.
- One real PaperSON record resolves strictly to its registered class and Type
  Ship.
- The Agent can inspect that record's contract, actions, Assertions, and POIs.
- One real non-blessable POI disappears only after its state predicate changes.
- One real blessable POI can retain a context-complete auditable blessing.
- Reevaluation invalidates stale blessings when their relevant situation
  changes.
- Existing packages can be reevaluated with improved tooling.

## Open design questions

- What is the smallest retained shape shared by all typed records beyond
  `type`, if anything?
- How are Type Ship UUIDs declared in code and inspected without importing
  arbitrary untrusted product modules?
- Which parts of current `tarav.poi` and `tarav.scoring` become canonical
  Harness ownership, and which remain adapters or domain policy?
- How should Agent-readable action and transition descriptions be expressed
  without prescribing one workflow engine?
- What evidence identifies the exact records-plus-code `System.Version` used
  for an evaluation or blessing across separate repositories?
- Which PaperSON record and package provide the safest representative pilot?

## Next move

Produce a joint Harness–PaperSON vertical-slice design that settles the
minimum public contracts, the PaperSON record-type migration, and the two
representative POI paths before moving code.
