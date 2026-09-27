# Diagram workflows

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
33afe59c = codex:01a07228-313a-7ab3-b6e0-aedcb5216b3c @33afe59c2f13ac5d4b59e56f7a3761d3d91c1206a1b6287b0872036739b370fd
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
