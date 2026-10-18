# Diagram workflows

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
33afe59c = codex:01a07228-313a-7ab3-b6e0-aedcb5216b3c @33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

## Framework shape

Tarav.Diagram is a framework for capture and contextualization. It contains
built-in capture workflows, reading and navigation workflows, and primitives
from which those workflows are assembled. It should not define the product as
one universal capture procedure or around a domain object called `Ship`:
Ship is a general identity primitive, not the name of Diagram's center.
<!-- tarav.breadcrumb 768a7d5c870e -->

One workflow cannot satisfy every capture situation. Each capture workflow may
produce Records suited to its own operational demand. Integration is valuable,
but it must not constrain capture prematurely. New built-in workflows should be
designed with the same primitives that future custom workflows could use.
<!-- tarav.breadcrumb 86ff334cfdec -->

## Capture and reading hourglass

```text
capture workflows
      \ | /
 Tarav.Harness + Tarav.Diagram
      / | \
reading and contextualization workflows
```
<!-- tarav.breadcrumb fdab61093de3 -->

Capture can remain relatively independent and optimized for its natural user
situation. Reading should become more universal across heterogeneous captures,
but semantic richness still comes through capabilities implemented by the
Records' authoritative classes—not by inspecting private JSON conventions.
<!-- tarav.breadcrumb d713c045dd91 -->

Capture performance and discovery performance are distinct objectives.
Capturers prioritize low interruption, high retention recall, sufficient
support, and session-bounded completion. Readers prioritize relevance, low
context cost, useful summaries, navigability, and broad recall. Shared schemas
and interfaces should emerge from demonstrated convergence rather than being
forced before the workflows mature.
<!-- tarav.breadcrumb 9561b69d2501 -->
<!-- tarav.breadcrumb 12197c63ac8c -->

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
<!-- tarav.breadcrumb 6d757948ed41 -->

The CLI is the human-facing command surface; the ALI is its Agent-facing
counterpart. The skill is workflow source code, not documentation external to
Diagram semantics.
<!-- tarav.breadcrumb 8057cc381b1a -->

## Initial capture family

Skills and their instructions are primary workflow entrypoints. Combining
agent instructions with Python mechanics is expected for most workflows.
<!-- tarav.breadcrumb 56825cd31c37 -->

```text
Capture
├── Wiki
└── Model
    ├── Agent
    └── User
```
<!-- tarav.breadcrumb 7f8ad9c3c725 -->

The User selects the capture workflow explicitly. `Capture.Model.User` keeps a
closely User-reviewed Model. `Capture.Model.Agent` may use similar primitives
without requiring User approval, but its effective Model extends the User
Model and should avoid duplicating it. `Capture.Wiki` is the
User-Turn-grounded Project.Wiki workflow, combining mandatory daily narration
with opportunistic topical integration.
<!-- tarav.breadcrumb 8619ea9deb47 -->
<!-- tarav.breadcrumb 2f8c574c0ccd -->
<!-- tarav.breadcrumb b04275f7a36a -->

## One implementation path among several organizations

The `.workflow` relationship and Tarav's code organization provide one chosen
path for organizing an object or concept. Choose that path for implementation
needs and embrace the hierarchy's limitations. It is neither privileged nor
semantically superior to other ways of organizing the same subjects.
<!-- tarav.breadcrumb a96b62b62271 -->

Other workflows may group the same entities differently. A workflow may model
a view on a problem even when no object's `.workflow` points to it. Modeling
those alternative organizations at the Diagram level remains later work;
the immediate focus is a first implementation path.
<!-- tarav.breadcrumb 6d56bebdea5f -->

For Wiki capture, the preferred first path is `Capture → Wiki`: capture means
extracting valuable information into a more organized format or surface, and
Wiki supplies a destination and surface model. `Wiki → Capture` remains another
useful route to the same workflow. The choice of implementation containment
does not restrict discovery to that route.
<!-- tarav.breadcrumb 6b080926aa3d -->
<!-- tarav.breadcrumb 94514db2fc6b -->

## Namespaces as semantic qualification

Tarav may qualify Python operations with namespaces such as
`SomeType.loadings.from_path(...)`, `obj.context.explorer().ls()`, or
`obj.records.to_record()`. These are proposed API shapes, not claims that the
paths are implemented. The plural `loadings` names the workflow namespace.
Such paths make Tarav's organization more visible in code and help readers
interpret which capability a method belongs to.
<!-- tarav.breadcrumb 9caaa0997612 -->
<!-- tarav.breadcrumb 76bf0589e165 -->
<!-- tarav.breadcrumb 0b654d22bae4 -->

This is an optional semantic reinforcement, not a new dispatch rule or a
requirement for every workflow. A workflow may expose methods directly. When
many Types inherit a base-class API and bare method names become crowded or
ambiguous, a qualified namespace can clarify them. Tarav can apply this tool
progressively as the library grows; mechanics need not rely on the path.
<!-- tarav.breadcrumb 87c47e276d68 -->
<!-- tarav.breadcrumb 16bd3a29b74b -->
<!-- tarav.breadcrumb d3e8504deac4 -->

## Dependency layers across namespaces

Dependency layers are a proposed additional dimension of code organization.
A namespace such as Kernel can span several layers rather than placing all
its definitions and integrations in one dependency unit. Higher layers may
depend on lower layers; imports within a layer have no additional directional
restriction from this principle. This provides more room to model concepts
without making their namespace alone determine their dependency position.
<!-- tarav.breadcrumb 318b5c3bed0e -->
<!-- tarav.breadcrumb 6699b265fa56 -->

Start with layering as a design principle; enforcement tooling can come later.
The purpose is to eliminate avoidable import cycles caused by grouping
foundational definitions and integrations together. It does not eliminate
genuinely circular definition dependencies or Python's initialization constraints
within a layer. Those harder cases remain distinct from the packaging cycles
that layering can remove. No package migration or final layer spelling was
selected in this discussion.
<!-- tarav.breadcrumb 55c17ba0daa1 -->

## First dependency-layer implementation

The user authorized moving Tarav toward the layer design, emphasizing that the
first organization need not be perfect. The first bounded slice moved private
utilities and Kernel into `tarav.l0`, made the root `ARCHIVE` convenience lazy,
and updated maintained Python imports and architecture checks. It creates a
working foundation while leaving other domain placements for later slices.
The [821 implementation note](../../../tarav-py/notes/live/821-dependency-layer-migration-impl-req.md)
records the exact scope and validation. The layer path expresses dependency
position; it does not change Workflow identity or semantic parentage.
<!-- tarav.breadcrumb d1b9b41fd726 -->

## Placing four workflows in l1

The user directed the next placement: Context, Loading, Project, and Archive
move to `tarav.l1`. Their Python packages now live there, with maintained
imports and architecture checks updated. The placement creates organization
without claiming every operation is dependency-clean: Context storage, the
Loading facade, and Record Archive reads still use runtime composition. The
[821 implementation note](../../../tarav-py/notes/live/821-dependency-layer-migration-impl-req.md)
records the verified scope and remaining split.
<!-- tarav.breadcrumb 70f947a8bde2 -->
