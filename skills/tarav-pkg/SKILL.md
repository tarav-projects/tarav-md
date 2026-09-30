---
name: tarav-pkg
description: "Tarav's constitutional and candidate big-picture design root. Use when working on Tarav itself or when a surface must align with Archive.Attic, Tarav.Archive, Tarav.Diagram, Tarav.Bloberia, Chatlas-backed evidence, contextualization, or the legacy Tarav skill mine."
---

# tarav-pkg

Tarav is an `Agents.Harness` for strengthening user-agent collaboration by
capturing `User.Touched.Data`, structuring it through supported annotations,
and making that structure available for contextualization.

This is Tarav's fresh package root. Its small size is deliberate. Material is
active only when it has been explicitly promoted here; older Tarav skills are
legacy evidence, not inherited design truth.

## Constitution

Read [CONSTITUTION.md](CONSTITUTION.md) completely before using any other
guidance in this package. Every surface claiming to be part of Tarav must
comply with it.

The Constitution is amendable. A conflict requires discussion and alignment
through a change to the design, the Constitution, or both.

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

The public contextualization, conversational capture, and implementation
workflows are `tarav-hugentics --ground`, `tarav-hugentics --capture`, and
`tarav-hugentics --impl`. Their grounding, reviewed, automatic, audit,
implementation-design, execution, and stance behavior uses the Diagram
mechanics documented by this package.

- `tarav-pkg --constitution` — load the Constitution.
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
- `tarav-pkg --attic` — read [references/attic.md](references/attic.md) for
  Archive.Attic semantics, Deposit workflow, and its boundaries with
  `Tarav.Archive` and `Diagram.Attic`. Load the linked legacy-skill-mine
  module only when deliberately mining the displaced skill implementation.

Without an explicit module, use this file as orientation, read the
Constitution, and route to the smallest relevant current design surface.
