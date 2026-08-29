# Hugentics Capture

This module runs the conversational workflow that develops and lands
`User.Touched.Chatlas.Index` Annotations into a Project's configured main
`Diagram.Model`.

Read [`../../tarav-pkg/tarav-diagram.md`](../../tarav-pkg/tarav-diagram.md)
before operating. Use its current Annotation schemas, Capture.Manifest rules,
named Renderers, Gates, and Assertion.Engine semantics.

## Shared Loop

Every mode uses the same conceptual loop:

```text
Contextualize → Map → Focus → Discuss/Propose → Land → Reconcile
```

1. Resolve the current native session with `tarav-chatlas-my-session-id` when
   available, then refresh it with `tarav chatlas update --session-id <id>`.
2. In a writing mode, run `tarav tarav2 diagram capture context --project
   --session-id <id> --json`. This resolves or mechanically bootstraps the
   Project's main Model. Report a new Model association when bootstrap occurs.
   In audit mode, inspect the Project association first and stop with a
   missing-Model finding instead of allowing read-only audit to bootstrap one.
3. Render the Model with `Kernel.Writing.Model` and inspect narrower Blocks or
   Lines when needed. Build an internal candidate map covering overlap,
   suitable existing lineages, new Blocks or Lines, and visible POIs.
4. Present a compact `Capture.Roadmap`: small coherent clusters in a useful
   order, with one recommended first focus. It is orientation, not an
   approval-ready proposal.

Keep context assembly internal unless missing or contradictory evidence
changes a user decision. The conversation should remain a collaboration, not
an evidence inventory.

## Interactive Reviewed Capture

`--capture` starts in `Capture.Stance::Review`.

Work on one Block or small coherent Line cluster at a time. Reuse an existing
Model, Block, or Line ship when the proposed material continues that semantic
lineage; otherwise propose a new ship. Render the exact proposed Line wording
and mint one fresh opaque token for that proposal.

Render every approval-ready proposal as a targeted Diagram edition. Before
the exact wording, identify:

- `Landing`: the destination Namespace;
- `Model`: the target Model label and ship UUID;
- `Target`: the existing or proposed Block label and ship UUID when one
  already exists;
- `Operation`: the concrete structural change, such as introducing a Block and
  its Line ships or adding a new Line edition to an existing ship; and
- `Edition.Approval.Token`: the proposal's opaque token.

The destination must not remain implicit merely because the Agent previously
rendered the Model. For a new Block or Line ship whose UUID is allocated only
during landing, say that the target is new instead of inventing an identity.
Place every proposed Line wording undecorated in the turn so the User can
review the exact retained content.

Pause with:

```text
::approve <token>
```

Approval accepts the exact presented wording but does not write it. A changed
wording, Model, Block target, or semantic operation requires a new token.
Presentation-only changes may retain the token. Approved material accumulates
while the workflow advances through the roadmap.

At a coherent landing pause, do not repeat the approved wording or render a
settled batch. Ask for landing with only the resolved command needed by the
foreground approved cluster, for example:

```text
::land-all-approved
```

Use `::land` instead when one clearly targeted approved item is foreground.
Both commands land only already-approved material and supply no missing
approval. The compact Agent landing-pause turn becomes the producer coordinate
for the landed Annotations; its context already contains the approved proposal
turns and supporting User turns.

## Capture Stances

`::discuss` enters a sticky Discuss stance. Continue ordinary conversation,
present no approval-ready proposal, and preserve the roadmap, current draft,
and approved cluster. At a pause, advertise only `::review`.

`::review` enters Review stance and resumes proposal work from the current
foreground without repeating the full roadmap.

These are conversational dispositions. They do not mutate the Diagram or
change the evidentiary status of already captured Annotations.

## Automatic Unreviewed Capture

`--capture --auto` and `--capture --unreviewed` are the same route. The Agent
contextualizes, maps, forms one bounded settled capture, lands it, and reports
the result without per-Line approval or a separate landing checkpoint. The
initial User invocation is the trigger authorizing that complete pass.

Do not present a roadmap or final batch and then wait. Doing so spends the same
`User.Attention` as a review checkpoint while withholding reviewed standing.
The autonomous loop is internal:

```text
User trigger → contextualize → map → settle → land → report
```

Before materialization, ensure Chatlas has a stable Agent producer turn for the
capture. This is an evidence mechanic, not a User checkpoint and does not
require exposing the settled batch for approval.

Do not manufacture approval evidence. Automatic Line Annotations retain their
producer and rooted User support but contain no `Verbatim.Gate`; they remain
unreviewed and may surface review POIs. They are still usable Model material.

If the User explicitly redirects a still-running pass into discussion or
review, stop autonomous landing and enter the corresponding interactive
workflow. This is an interruption, not a normal automatic-mode pause. Material
landed through the unreviewed route remains unreviewed until a later review
adds a passing Gate.

## Read-Only Audit

`--capture --audit` performs Contextualize and Map, presents the compact
Capture.Roadmap and relevant POIs, then stops. It must not present approval
commands, create a Manifest, mutate Project configuration, or write Diagram
Annotations.

## Landing Through Tarav2

Create no `Capture.Manifest` during ordinary discussion. In reviewed mode,
compile it only after `::land` or `::land-all-approved`. In automatic mode,
compile and apply it once the internally developed bounded batch is settled;
the initial invocation already authorizes landing.

The Manifest is a faithful mechanical compilation:

- each semantic Line retains its exact wording, Model/Block/Line ships,
  producer Chatlas Turn, and rooted User support;
- reviewed Lines retain `Verbatim.Gate` data containing the shared opaque
  token and exact proposal and approval Turn references;
- automatic Lines omit Gates;
- one approval exchange may cover several exact Lines when the proposal turn
  contains every wording, but each Line retains its own Gate instance;
- Block and Model organization uses ordinary typed Annotations; do not invent
  semantic content during landing.

Use a temporary Manifest path and run:

```bash
tarav tarav2 diagram capture template --project --manifest <path> --json
tarav tarav2 diagram capture check --manifest <path> --json
tarav tarav2 diagram capture apply --manifest <path> --json
```

Correct mechanical errors before applying. A semantic correction returns to
discussion or reviewed proposal work. POIs never block capture.

After applying, report created and existing Annotation identities, the Git
commit, and all POIs. Re-render the affected Model or Lines so the centralized
Assertion.Engine recomputes Gate standing from Chatlas evidence. Report the
result without writing derived `passed` flags into Annotation records.
