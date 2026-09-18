# 792 — Diagram workflow catalog — live note

Status: Working design and usage inventory

## Purpose

This note is the brainstorming and history surface for workflows implemented
with `tarav.harness` and `tarav.diagram`.

It should answer:

- which workflows exist or are being considered;
- what user or agent need motivates each workflow;
- which parts are deterministic code and which parts are Agent-operated;
- which Records the workflow writes or reads;
- what happened when the workflow was exercised; and
- which design changes actual usage suggests.

The catalog is deliberately provisional. A command, skill route, or current
class tree does not establish the final workflow taxonomy.

## Architecture frame

Diagram is a framework for capture and contextualization workflows. It also
implements several built-in workflows using the same primitives intended for
future workflows.

```text
many capture workflows
          ↓
  tarav.harness + tarav.diagram
          ↓
many reading and contextualization workflows
```

Capture workflows may remain relatively independent. Reading workflows seek
broader interoperability through generic Harness capabilities or explicit
interfaces implemented by authoritative Record classes. A reader must not
infer domain semantics from a Record's private serialized representation.

A complete Diagram workflow may span two executable surfaces:

```text
Diagram workflow
├── Python code
│   ├── Records and registered classes
│   ├── deterministic validation
│   ├── storage and transitions
│   └── CLI operations
│
└── Agent skill
    ├── interpretive procedure
    ├── evidence-reading instructions
    ├── judgment and escalation rules
    ├── human authorization protocol
    └── ALI interaction
```

The skill is Agent-executed source code. The CLI is part of the deterministic
interface; the ALI is part of the Agent-facing interface.

Diagram grounding: `Diagram.Workflow` Block
`0c970e18-f2f6-41d3-bb6d-fb338fcc21d5`.

## Workflow entry

Each workflow entry should grow only as usage supplies useful evidence.

```text
Name
Direction: Capture | Read | Mixed
Standing: Candidate | Exercised | Implemented | Parked

Motivation
Natural trigger
Inputs and authority
Records written
Capabilities read
Python responsibilities
Agent-skill responsibilities
CLI surface
ALI surface
Known consumers and integrations
Open design questions
Usage history
```

`Standing` describes implementation evidence, not importance or correctness.

## Initial workflow inventory

The entries below are seeds for discussion. Some current routes may later
split into several workflows or collapse into one shared workflow.

### Model.Capture

- **Direction:** Capture
- **Standing:** Implemented and repeatedly exercised
- **Motivation:** retain conversational design as supported Model, Block, and
  Line material without requiring the conversation itself to become a design
  database.
- **Current ALI:** `tarav-hugentics --capture`, including reviewed and
  unreviewed modes.
- **Current code surface:** Diagram Draft, validation, application, support,
  Gates, projections, and Assertion evaluation.
- **Open question:** whether `Model.Capture` is the right durable name and
  where its Record family begins and ends.

### Implementation.Work

- **Direction:** Mixed
- **Standing:** Implemented and repeatedly exercised
- **Motivation:** turn actionable design into a durable implementation request,
  execute it with explicit authorization, and reconcile product and Diagram
  results.
- **Current ALI:** `tarav-hugentics --impl` routes.
- **Current Records:** `Impl.Req.Collection` plus supported design Lines and
  authorization Gates; the live note remains a separate Product.Surface.
- **Open question:** which parts are one workflow and which are compositions of
  Model.Capture, implementation coordination, execution, and landing capture.

### Issue.Parking.And.Maintenance

- **Direction:** Mixed
- **Standing:** Implemented
- **Motivation:** retain a concern cheaply, inspect it later, and record
  resolution without forcing immediate product work.
- **Current ALI:** `tarav-hugentics --issues` and `--issues --audit`.
- **Open question:** define the durable boundary between capture, maintenance,
  audit, and resolution workflows.

### Reading.Project

- **Direction:** Mixed
- **Standing:** First implementation slice
- **Motivation:** coordinate long-running document reading while retaining
  progress, discussion, and selected captures.
- **Current ALI:** `tarav-hugentics --reading-club`.
- **Open question:** identify which Records belong specifically to reading and
  which captures should delegate to other Diagram workflows.

### Session.Grounding

- **Direction:** Read
- **Standing:** Implemented and repeatedly exercised
- **Motivation:** recover relevant Diagram context for the current
  user–agent collaboration without treating a static context dump as complete.
- **Current ALI:** `tarav-hugentics --ground`.
- **Current code surface:** `Diagram.View`, navigation, rendering, and
  Context.Provider mechanics.
- **Open question:** clarify the boundary between the maintained View, generic
  navigation, discovery, and final context compilation.

### Capture.Audit

- **Direction:** Read
- **Standing:** Implemented
- **Motivation:** inspect likely capture opportunities, overlap, and POIs
  without writing Diagram data.
- **Current ALI:** `tarav-hugentics --capture --audit`.
- **Open question:** determine which audit mechanics are generic readers and
  which belong specifically to Model.Capture.

### Record.Evaluation.And.Curation

- **Direction:** Mixed
- **Standing:** Partially implemented across Assertion, POI, review, and
  maintenance mechanics
- **Motivation:** surface suspicious Diagram state and let Agents or Users
  amend, enrich, prune, or bless it over time.
- **Open question:** whether evaluation, POI navigation, review, and curation
  are separate composable workflows.

### Product.Surface.Context

- **Direction:** Mixed
- **Standing:** Partial and experimental
- **Motivation:** preserve which archived or Diagram material was supplied
  while producing an external Product.Surface and detect later contextual
  drift.
- **Related current routes:** inline capture and inline audit.
- **Open question:** separate the Product.Surface-native reference mechanic
  from the Diagram workflow that captures and reads generation context.

## Candidate workflow questions

- What is the smallest shared contract for all Diagram workflows?
- Is a workflow itself a typed, Ship-identified object with editions?
- How does a skill declare the CLI operations and Record capabilities it uses?
- How are workflow state and available Agent actions exposed without encoding
  a rigid universal state machine?
- Which reading capabilities belong in Harness, Diagram, or one Record family?
- How does a universal reader discover capabilities without importing every
  capture workflow?
- How should workflow versions cover Python code, skills, and retained Records
  together?
- Which POIs describe a workflow's own execution rather than the Records it
  reads or produces?

## Usage history

Append concise entries. Link the session, issue, implementation note, Diagram
Collection, or other evidence instead of reproducing it.

| Date | Workflow | Scenario | Outcome / friction | Design consequence |
| --- | --- | --- | --- | --- |
| 2026-09-07 | Model.Capture | Captured the general Diagram workflow architecture through the unreviewed route. | One new `Diagram.Workflow` Block and eight unreviewed Lines landed; evidence-coordinate mistakes were caught before landing. | Confirmed that the workflow combines Agent interpretation with deterministic Draft validation and that POIs do not block capture. |

## Working method

When a workflow is proposed or exercised:

1. add or update its inventory entry;
2. record the motivating natural workflow;
3. append the concrete usage outcome and friction;
4. promote only the general lessons supported by that history; and
5. leave unresolved taxonomy and interface choices visibly open.

This note is a design workshop and evidence index. Settled general design may
later be promoted into `skills/tarav-pkg/`; implementation requests should use
their own live notes and Diagram Collections.
