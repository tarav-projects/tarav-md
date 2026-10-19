---
name: tarav-pkg
description: "Tarav's constitutional and candidate big-picture design root. Use for constitutional audits of projects, when working on Tarav itself or when a surface must align with Archive.Attic, Tarav.Archive, Tarav.Diagram, Tarav.Bloberia, Chatlas-backed evidence, contextualization, or the legacy Tarav skill mine."
---

# tarav-pkg

<!-- tarav.sessions
4720b13e = codex:01a02f8b-8c36-7123-ba70-1a217b776e28 @4720b13eeb5dc61cad2d999b24f45a78d9dcd776c77e0be98b68822e30fdb604
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

Tarav is an external harness for enhancing collaboration between Users and
Agents. Its extensible Python library provides tools and workflows that can be
integrated into wider systems and composed into harnesses for particular Projects.
<!-- tarav.breadcrumb f4a6e0e1061e -->

A Project is a fundamental Tarav concept. Capture, contextualization, checks,
and workflow coordination are capabilities Projects can select and extend.
<!-- tarav.breadcrumb c458c653f431 -->

Use this skill to load Tarav's constitutional boundaries and find the design
guidance relevant to the current task. Material is active only when explicitly
promoted into this package; candidate designs remain distinguishable from the
Constitution and from implemented behavior.

## Start here

Read [CONSTITUTION.md](CONSTITUTION.md) completely before using any other
guidance in this package. Every surface claiming to be part of Tarav must
comply with it.

The Constitution is amendable. Surface conflicts for discussion and alignment
through a change to the design, the Constitution, or both.

## Reading and rereading

Load only the module relevant to the current task.

Do not reread a skill `references/` file that was already read completely and
remains available in context. Reread it only if it changed, its contents were
lost or materially reduced through compaction, or a specific uncertainty
requires it.

## Implementation principles

Use these principles when designing, implementing, or reviewing Tarav.
They describe the implementation approach, subordinate to the Constitution;
they are not a claim that every existing subsystem already realizes it.

1. **Code carries semantics.** Types, methods, usage, and storage behavior
   express meaning. Explicit metadata and interfaces expose some of that
   meaning, not all of it. Inspect surrounding code and evidence when needed.
2. **Classes participate in the Diagram.** `entity(SomeClass)` represents
   the class, not its instances. Class, object, and Workflow identities may
   be distinct; place Diagram metadata on their representing objects rather
   than duplicating it in parallel class attributes.
3. **The Diagram is emergent.** Types, Archive, Context, and other workflows
   define overlapping graphs. Do not force every relationship into one
   universal graph schema or confuse the Diagram with one Python package.
4. **Workflow containment is one organization path.** `.workflow` identifies
   the containing Workflow. That implementation hierarchy is not semantically
   superior to alternative views; other workflows can group the same subjects.
5. **Share minimal mechanics, not entire graph semantics.** Explorer contracts
   give independent graphs familiar operations. A shared interface does not
   imply cross-graph navigation; crossing graphs needs explicit jump points.
6. **Types can carry executable behavioral obligations.** Ship reusable tests
   with interfaces and let implementations supply fixtures and inherit checks.
   Use ordinary Python inheritance and testing tools; no separate conformance
   system is required. Tests check behavior within their stated coverage.
7. **Namespaces reinforce meaning.** Qualified paths such as
   `obj.records.to_record()` can clarify capabilities inherited by many Types
   or crowded APIs. This is an optional, evolutionary tool, not a mandatory
   Workflow mapping or dispatch rule. Direct methods remain valid; these
   illustrative paths do not claim an API is already implemented.
8. **Layers separate dependencies from ownership.** One namespace can span
   `l0`, `l1`, and higher levels. Higher levels may import lower levels;
   same-level imports have no additional directional restriction. Put
   integrations above the definitions they combine. Layers address avoidable
   packaging cycles, not genuinely circular definitions. They do not change
   Workflow parentage. Adopt the principle without requiring new tooling.
9. **Simple mechanics support agent judgment.** Mechanize reliable operations
   and expose evidence; leave interpretation and ambiguous repair to agents
   and users. Skills are primary workflow entry points alongside Python.
   Human participation is constitutive: review points can deliberately pace
   evolution to human understanding, not just detect incorrect agent work.
10. **Capture first, evolve afterward.** Favor low capture friction over
    premature integration. Workflows may evolve, stabilize, or be abandoned.
    Preserve evidence such as Git history and retained chats for later
    interpretation and migration; recovery is not guaranteed or always cheap.
11. **Validation informs rather than forbids.** Checks and scoring surface
    POIs with context. Consumers choose responses; imperfect consistency
    does not by itself prohibit mutation. Generated interpretation needs
    inspectable evidence and assessment, not an unexplained agent conclusion.
12. **Connectivity precedes optimized contextualization.** First preserve
    navigable connections to components and evidence. Specialized workflows
    can improve selection, ordering, summaries, and discovery afterward.
    Reachability is an objective, not proof that all data is already connected.

For current Python boundaries and APIs, consult the maintained product's
`ARCHITECTURE.md`, source, and tests. In the source workspace, detailed
rationale and conversational evidence live in `tarav-md/notes/wiki/`, notably
`diagram-workflows.md`, `context-graph.md`, and `tarav-harness.md`. Those
repository surfaces are navigation hints, not required deployed skill files.

## Current candidate design

Load only the design relevant to the work:

- For artifact preservation, records, identity, locators, and references,
  read [tarav-archive.md](tarav-archive.md).
- For the Chatlas-backed data train, grounded annotations, semantic lineages,
  capture manifests, and Models, read [tarav-diagram.md](tarav-diagram.md).
- For the general semantic annotation system governing Semantic.Computations,
  Ships, continuity, Assertion carry, scoring, and controls, read
  [tarav-semantic-calculus.md](tarav-semantic-calculus.md).
- For the global Agent-managed JSON registry and its Agent.Hint workflow, read
  [tarav-bloberia.md](tarav-bloberia.md).
- For behavioral situations used to develop and test candidate Tarav designs,
  read [USAGE-HISTORIES.md](USAGE-HISTORIES.md).
- For the general theory governing the constitutional document, read
  [references/constitutional-theory.md](references/constitutional-theory.md).

These design documents are subordinate to the Constitution and remain WIP.
They are candidate design truth, not constitutional amendments.

## Data root

Durable Tarav data defaults to the physical depot `~/Documents/tarav/`.
Its child surfaces retain independent semantics and Git histories:

```text
~/Documents/tarav/
├── archive/
├── attic/
├── chatlas/
├── diagram/
├── reading-club/
└── bloberia/
```

The data root is not itself one repository or authority. Machine-local
configuration, caches, indexes, and operational logs remain under `~/.tarav/`.
External repositories registered by the Archive remain free to live elsewhere.

## Unapproved design digests

The following surface preserves ongoing discussion for later review and
capture. It is not approved or landed design truth:

- [Context, POIs, and Product-Surface Impact](references/context-poi-and-impact-map-design-digest.md)
  — discussion digest from Chatlas session
  `01a02f8b-8c36-7123-ba70-1a217b776e28`.
- [Gates and Deferred Review](references/gates-and-deferred-review-design-digest.md)
  — discussion digest from Chatlas session
  `01a02f8b-8c36-7123-ba70-1a217b776e28` covering reusable Gate Assertions,
  deferred review, and Line-ship review standing.

## Modules

The public conversational capture and implementation workflows are
`tarav-hugentics --capture` and `tarav-hugentics --impl`. Their reviewed,
automatic, audit, implementation-design, execution, and stance behavior
uses the Diagram mechanics documented by this package.

- `tarav-pkg --constitution` — load the Constitution.
- `tarav-pkg --constitution --audit --project <path>` — scan that Project
  for significant constitutional misalignments and report them in chat
  using the audit instructions below.
- `tarav-pkg --archive` — load the Constitution and Archive design.
- `tarav-pkg --diagram` — load the Constitution and Diagram design.
- `tarav-pkg --semantic-calculus` — load the Constitution and
  [tarav-semantic-calculus.md](tarav-semantic-calculus.md).
- `tarav-pkg --bloberia` — load the Constitution and Tarav.Bloberia design.
- `tarav-pkg --usage-histories` — read
  [USAGE-HISTORIES.md](USAGE-HISTORIES.md) and use its behavioral histories
  to develop or test candidate designs.
- `tarav-pkg --review` — read [references/review.md](references/review.md) and
  review existing Diagram Block Lines through mechanically auditable
  `Verbatim.Gate`s.
- `tarav-pkg --constitutional-theory` — load the Constitution and the general
  constitutional-theory module.
- `tarav-pkg --step-actions` — read
  [references/step-actions.md](references/step-actions.md) for how to work a
  Step action: place the input, start, work, close.
- `tarav-pkg --attic` — read [references/attic.md](references/attic.md) for
  Archive.Attic semantics, Deposit workflow, and its boundaries with
  `Tarav.Archive` and `Diagram.Attic`. Load the linked legacy-skill-mine
  module only when deliberately mining the displaced skill implementation.
- `tarav-pkg --github` — read [references/github.md](references/github.md) for
  the `tarav-projects` GitHub organization: source repositories on `main`,
  `tarav-releases`, licensing and the scan before publishing.
  <!-- tarav.breadcrumb ee604b3b60e3 -->
- `tarav-pkg --monologs --process` — read
  [references/monologs.md](references/monologs.md) and bring new voice
  recordings from the phone through xtt-readings on the Studio to a curated
  `transcript.md` under `~/Documents/tarav/monologs/`.

Without an explicit module, use this file as orientation, read the
Constitution, and route to the smallest relevant current design surface.

### Constitutional audit

`--project <path>` selects the Project to inspect; if omitted, use the current
directory. Resolve relative paths from the current directory.

Read the Constitution and the selected Project's guidance. Scan its code,
documentation, and tests for significant misalignments with constitutional
statements. Follow relevant evidence far enough to explain each finding;
distinguish current behavior from proposals and unresolved review notes.

Present a concise report in chat. State which Project and areas you inspected.
For each finding, cite the constitutional statement and the conflicting project
evidence (file and location), explain the mismatch, and state any uncertainty.
Prioritize consequential findings. If none are found, say so within the inspected
coverage; do not claim exhaustive alignment.

The audit only surfaces misalignments. Do not repair the Project, amend or
question the Constitution, or decide which side should change. Do not create
report files or persistent actions unless separately requested.

## Review notes

The following User notes are retained verbatim from before this revision.
Section splitting and a separate rereading policy are addressed here; specialized
SKW document Types remain a design question.

[NOTE/TODOS
  - Its skw i also a single block
    - terrible
  - I think we should also Type the skw files
    - for instance, this one should be a SKILLSkwSrcFile (or whatever name)
    - this way for instance, we can force the description to be its own special block
  - In general this file is not a good SKILL.md
    - What would be a good SKILL.md?
]

[NOTE
  - I think this should be its own section
  - I mean, the reread policy
]
