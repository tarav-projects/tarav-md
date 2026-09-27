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
<!-- tarav.breadcrumb 768a7d5c870eb9b476ceabf24bb0841b81389259aa0d18b74ad79f0b47981cd7 -->

One workflow cannot satisfy every capture situation. Each capture workflow may
produce Records suited to its own operational demand. Integration is valuable,
but it must not constrain capture prematurely. New built-in workflows should be
designed with the same primitives that future custom workflows could use.
<!-- tarav.breadcrumb 86ff334cfdec84d6da052852ddd913a324b1621ae3f63a1874b40a940df9fb6c -->

## Capture and reading hourglass

```text
capture workflows
      \ | /
 Tarav.Harness + Tarav.Diagram
      / | \
reading and contextualization workflows
```
<!-- tarav.breadcrumb fdab61093de380d2e9b4cd0b46c8dffd722407afec177b36920a605f6d787001 -->

Capture can remain relatively independent and optimized for its natural user
situation. Reading should become more universal across heterogeneous captures,
but semantic richness still comes through capabilities implemented by the
Records' authoritative classes—not by inspecting private JSON conventions.
<!-- tarav.breadcrumb d713c045dd91a87f15b140aa18db9314e5da3c772962e937fc04bff5a19eea9d -->

Capture performance and discovery performance are distinct objectives.
Capturers prioritize low interruption, high retention recall, sufficient
support, and session-bounded completion. Readers prioritize relevance, low
context cost, useful summaries, navigability, and broad recall. Shared schemas
and interfaces should emerge from demonstrated convergence rather than being
forced before the workflows mature.
<!-- tarav.breadcrumb 9561b69d250106f65449fcc4a439f5bf02a85ac809cbc966859d6cbcac4ffa86 -->
<!-- tarav.breadcrumb 12197c63ac8cab93f54e9078995f8293acbee750beea1a6b23cbcd8645e79f6b -->

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
<!-- tarav.breadcrumb 6d757948ed41b579290f6aebd7a9006b32d9b30eaaf0f24232a4682aec7897b7 -->

The CLI is the human-facing command surface; the ALI is its Agent-facing
counterpart. The skill is workflow source code, not documentation external to
Diagram semantics.
<!-- tarav.breadcrumb 8057cc381b1ad651a7c19c62fed293fc77a75299fb57718cb31581fb48c8377a -->

## Initial capture family

Skills and their instructions are primary workflow entrypoints. Combining
agent instructions with Python mechanics is expected for most workflows.
<!-- tarav.breadcrumb 56825cd31c37094b2f462280f20704456ba9d8a96cb543b7a57d8611bfc1848d -->

```text
Capture
├── Wiki
└── Model
    ├── Agent
    └── User
```
<!-- tarav.breadcrumb 7f8ad9c3c725674086af17da0552a8aaab9dba3bd70b5b50a3469f69416079ed -->

The User selects the capture workflow explicitly. `Capture.Model.User` keeps a
closely User-reviewed Model. `Capture.Model.Agent` may use similar primitives
without requiring User approval, but its effective Model extends the User
Model and should avoid duplicating it. `Capture.Wiki` is the
User-Turn-grounded Project.Wiki workflow, combining mandatory daily narration
with opportunistic topical integration.
<!-- tarav.breadcrumb 8619ea9deb4764764ab0e9e4ca8b253de43416c8cbab18e20c35c124563e13c3 -->
<!-- tarav.breadcrumb 2f8c574c0ccde4476c33651945b7399b628b29a321355399eca782e708c9dcd7 -->
<!-- tarav.breadcrumb b04275f7a36a30a4218871333ac78632c8f850d697634d37351dc8d6cdbc3935 -->

## One implementation path among several organizations

The `.workflow` relationship and Tarav's code organization provide one chosen
path for organizing an object or concept. Choose that path for implementation
needs and embrace the hierarchy's limitations. It is neither privileged nor
semantically superior to other ways of organizing the same subjects.
<!-- tarav.breadcrumb a96b62b622718cc144122c0d9a4ac645dcb6726786a366772b8931aa4c8c6474 -->

Other workflows may group the same entities differently. A workflow may model
a view on a problem even when no object's `.workflow` points to it. Modeling
those alternative organizations at the Diagram level remains later work;
the immediate focus is a first implementation path.
<!-- tarav.breadcrumb 6d56bebdea5f6a546d624de3844e9d0c48874a07c905a052381b833307f2a2c6 -->

For Wiki capture, the preferred first path is `Capture → Wiki`: capture means
extracting valuable information into a more organized format or surface, and
Wiki supplies a destination and surface model. `Wiki → Capture` remains another
useful route to the same workflow. The choice of implementation containment
does not restrict discovery to that route.
<!-- tarav.breadcrumb 6b080926aa3d0e62275ba13e642a96502a471dbf9df2b524b57df335688d038a -->
<!-- tarav.breadcrumb 94514db2fc6b3e03acc2c441f193e2c4570cea3af7a074cd2998cf61f07d3069 -->

## Namespaces as semantic qualification

Tarav may qualify Python operations with namespaces such as
`SomeType.loadings.from_path(...)`, `obj.context.explorer().ls()`, or
`obj.records.to_record()`. These are proposed API shapes, not claims that the
paths are implemented. The plural `loadings` names the workflow namespace.
Such paths make Tarav's organization more visible in code and help readers
interpret which capability a method belongs to.
<!-- tarav.breadcrumb 9caaa09976128f906a4eb51f2642e31cf71f41a7e9acde935606e3badb27c688 -->
<!-- tarav.breadcrumb 76bf0589e1655fba76216d6adcc9a5408c9c5d4f9efdaa27bdfad7a48e3e4449 -->
<!-- tarav.breadcrumb 0b654d22bae4b827aacc9230eebc7dada937f6a25def86adbdaa4736f69a93d6 -->

This is an optional semantic reinforcement, not a new dispatch rule or a
requirement for every workflow. A workflow may expose methods directly. When
many Types inherit a base-class API and bare method names become crowded or
ambiguous, a qualified namespace can clarify them. Tarav can apply this tool
progressively as the library grows; mechanics need not rely on the path.
<!-- tarav.breadcrumb 87c47e276d68aaa55aef9d061d27fc63a41dc119f77abc23deae13fcba96264d -->
<!-- tarav.breadcrumb 16bd3a29b74b8099642bef65f8376203297916ad33ffa86099166effa4057909 -->
<!-- tarav.breadcrumb d3e8504deac4f6701f8f419adf29704173026d4ff43462d2ee51bb8011d3c618 -->

## Dependency layers across namespaces

Dependency layers are a proposed additional dimension of code organization.
A namespace such as Kernel can span several layers rather than placing all
its definitions and integrations in one dependency unit. Higher layers may
depend on lower layers; imports within a layer have no additional directional
restriction from this principle. This provides more room to model concepts
without making their namespace alone determine their dependency position.
<!-- tarav.breadcrumb 318b5c3bed0edb5be4b764bc8ee9276c3f7c5c4fa968a2fb7d65cfaadf824e5c -->
<!-- tarav.breadcrumb 6699b265fa560134e4720d84b8848422ee3358793739df506574433b02309f8c -->

Start with layering as a design principle; enforcement tooling can come later.
The purpose is to eliminate avoidable import cycles caused by grouping
foundational definitions and integrations together. It does not eliminate
genuinely circular definition dependencies or Python's initialization constraints
within a layer. Those harder cases remain distinct from the packaging cycles
that layering can remove. No package migration or final layer spelling was
selected in this discussion.
<!-- tarav.breadcrumb 55c17ba0daa1c25d619a74090b4f98c956a4d9b4fa905940aaa4ad11ba601691 -->

## First dependency-layer implementation

The user authorized moving Tarav toward the layer design, emphasizing that the
first organization need not be perfect. The first bounded slice moved private
utilities and Kernel into `tarav.l0`, made the root `ARCHIVE` convenience lazy,
and updated maintained Python imports and architecture checks. It creates a
working foundation while leaving other domain placements for later slices.
The [821 implementation note](../../../tarav-py/notes/live/821-dependency-layer-migration.md)
records the exact scope and validation. The layer path expresses dependency
position; it does not change Workflow identity or semantic parentage.
<!-- tarav.breadcrumb d1b9b41fd726576a7d030e3b5cfd8b6709fcbf90ed1aa4520f0594c6f7050191 -->

## Placing four workflows in l1

The user directed the next placement: Context, Loading, Project, and Archive
move to `tarav.l1`. Their Python packages now live there, with maintained
imports and architecture checks updated. The placement creates organization
without claiming every operation is dependency-clean: Context storage, the
Loading facade, and Record Archive reads still use runtime composition. The
[821 implementation note](../../../tarav-py/notes/live/821-dependency-layer-migration.md)
records the verified scope and remaining split.
<!-- tarav.breadcrumb 70f947a8bde288a044897b1062753fadc9c10aea0db371316d0adc1002327c5b -->
