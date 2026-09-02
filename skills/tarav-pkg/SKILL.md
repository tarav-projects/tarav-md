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
- `tarav-pkg --capture` — read [references/capture.md](references/capture.md)
  for the lower-level reviewed Tarav.Diagram capture mechanics. Prefer
  `tarav-hugentics --capture` for the public conversational workflow.
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
