---
name: tarav-pkg
description: "Tarav's constitutional and candidate big-picture design root. Use when working on Tarav itself or when a surface must align with Tarav.Archive, Tarav.Diagram, Chatlas-backed evidence, contextualization, or the legacy Tarav skill mine."
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
- For the general theory governing the constitutional document, read
  [references/constitutional-theory.md](references/constitutional-theory.md).

These design documents are subordinate to the Constitution and remain WIP.
They are candidate design truth, not constitutional amendments.

## Modules

- `tarav-pkg --constitution` — load the Constitution.
- `tarav-pkg --archive` — load the Constitution and Archive design.
- `tarav-pkg --diagram` — load the Constitution and Diagram design.
- `tarav-pkg --constitutional-theory` — load the Constitution and the general
  constitutional-theory module.
- `tarav-pkg --attic` — read [references/attic.md](references/attic.md), then
  inspect only the selected legacy material needed for the current question.

Without an explicit module, use this file as orientation, read the
Constitution, and route to the smallest relevant current design surface.
