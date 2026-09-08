# Diagram workflows

<!-- tarav.sessions
33afe59c = codex:01a07228-313a-7ab3-b6e0-aedcb5216b3c @33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd
-->

## Framework shape

Tarav.Diagram is a framework for capture and contextualization. It contains
built-in capture workflows, reading and navigation workflows, and primitives
from which those workflows are assembled. It should not define the product as
one universal capture procedure or around a domain object called `Ship`:
Ship is a general identity primitive, not the name of Diagram's center.
<!-- tarav.context 33afe59c:b2b6cbbf0510f90d -->

One workflow cannot satisfy every capture situation. Each capture workflow may
produce Records suited to its own operational demand. Integration is valuable,
but it must not constrain capture prematurely. New built-in workflows should be
designed with the same primitives that future custom workflows could use.
<!-- tarav.context 33afe59c:b2b6cbbf0510f90d -->

## Capture and reading hourglass

```text
capture workflows
      \ | /
 Tarav.Harness + Tarav.Diagram
      / | \
reading and contextualization workflows
```
<!-- tarav.context 33afe59c:b2b6cbbf0510f90d -->

Capture can remain relatively independent and optimized for its natural user
situation. Reading should become more universal across heterogeneous captures,
but semantic richness still comes through capabilities implemented by the
Records' authoritative classes—not by inspecting private JSON conventions.
<!-- tarav.context 33afe59c:b2b6cbbf0510f90d -->

Capture performance and discovery performance are distinct objectives.
Capturers prioritize low interruption, high retention recall, sufficient
support, and session-bounded completion. Readers prioritize relevance, low
context cost, useful summaries, navigability, and broad recall. Shared schemas
and interfaces should emerge from demonstrated convergence rather than being
forced before the workflows mature.
<!-- tarav.context 33afe59c:fa586401e0fe790b -->
<!-- tarav.context 33afe59c:8ee915b60fc175f0 -->

## Joint implementation

A Diagram workflow is implemented jointly by deterministic Python code and an
Agent skill:

```text
Diagram workflow
├── Python
│   ├── registered Records and classes
│   ├── deterministic validation
│   ├── storage and transitions
│   └── CLI operations
└── Agent skill
    ├── interpretive procedure
    ├── evidence-reading instructions
    ├── judgment and escalation rules
    ├── human authorization protocol
    └── ALI interaction
```
<!-- tarav.context 33afe59c:eef072fe5456cee5 -->

The CLI is the human-facing command surface; the ALI is its Agent-facing
counterpart. The skill is workflow source code, not documentation external to
Diagram semantics.
<!-- tarav.context 33afe59c:eef072fe5456cee5 -->

## Initial capture family

```text
Capture
├── Note
└── Model
    ├── Agent
    └── User
```
<!-- tarav.context 33afe59c:864b0f87dd82fb92 -->

The User selects the capture workflow explicitly. `Capture.Model.User` keeps a
closely User-reviewed Model. `Capture.Model.Agent` may use similar primitives
without requiring User approval, but its effective Model extends the User
Model and should avoid duplicating it. `Capture.Note` is the fast,
User-Turn-grounded Note workflow.
<!-- tarav.context 33afe59c:864b0f87dd82fb92 -->
