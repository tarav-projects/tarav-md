# Hugentics Capture

This module runs the conversational workflow that develops and lands typed
Ships, Ship editions, and Annotations into a Project's configured main
`Diagram.Model` in `User.Touched.Chatlas.Index`.

Read [`../../tarav-pkg/tarav-diagram.md`](../../tarav-pkg/tarav-diagram.md)
before operating. Use its current Ship and Annotation schemas, Capture.Manifest rules,
named Renderers, Gates, and Assertion.Engine semantics.

## Shared Loop

Every mode uses the same conceptual loop:

```text
Contextualize → Map → Focus → Discuss/Propose → Land → Reconcile
```

1. Resolve the current native session with `tarav-chatlas-my-session-id` when
   available, then refresh it with `tarav chatlas update --session-id <id>`.
2. In a writing mode, run `tarav diagram capture context --project
   --session-id <id> --json`. This resolves or mechanically bootstraps the
   Project's main Model. Report a new Model association when bootstrap occurs.
   In audit mode, inspect the Project association first and stop with a
   missing-Model finding instead of allowing read-only audit to bootstrap one.
3. Render the Model with `Kernel.Writing.Model` and inspect narrower Blocks or
   Lines when needed. Read the Model context's Object.Type registry and use
   full Type names; compact Type codes are rendering-only. Build an internal
   candidate map covering overlap, suitable existing lineages, new Blocks or
   Lines, and visible POIs.
4. Present a compact `Capture.Roadmap`: small coherent clusters in a useful
   order, with one recommended first focus. It is orientation, not an
   approval-ready proposal.

Keep context assembly internal unless missing or contradictory evidence
changes a user decision. The conversation should remain a collaboration, not
an evidence inventory.

### Design-family Block Line.Type vocabulary

Use this compact vocabulary during ordinary design capture. Retain the full
Type name in records; the short code is only a rendering aid.

`Design.Block` and the initial `Impl.Req.Block` implementation accept this
same vocabulary. Their distinct Block.Types preserve separate mechanics and
contextual projections without duplicating the Line.Type definitions.

| Line.Type | Code | Use when the Line... |
| --- | --- | --- |
| `Design.Line.Definition` | `DF` | fixes what a name means. |
| `Design.Line.Decision` | `DC` | pins a `Design.Variable` to a value. |
| `Design.Line.Constraint` | `CT` | bounds a `Design.Variable` without selecting a value. |
| `Design.Line.Rejection` | `RJ` | excludes a considered alternative. |
| `Design.Line.Principle` | `PR` | gives generative orientation across multiple variables. |
| `Design.Line.Freedom` | `FR` | explicitly leaves a `Design.Variable` Agent-owned. |
| `Design.Line.Example` | `EX` | illustrates another Line through a concrete case. |

These summaries are low-friction capture guidance. The Object.Type registry
links every Type to its addressable Definition.Block; inspect that Block when
the compact wording is insufficient. Definition resolution findings are POIs,
not capture blockers.

## Interactive Reviewed Capture

`--capture` starts in `Capture.Stance::Review`.

Work on one Block or small coherent Line cluster at a time. Reuse an existing
Model, Block, or Line ship when the proposed material continues that semantic
lineage; otherwise propose a new ship. Render the exact proposed Line wording
and mint one fresh opaque token for that proposal.

Render every approval-ready proposal as a `Capture.Review.Turn`: an assistant
turn that presents one targeted Ship edition for efficient User review.
Use a compact `Kernel.Writing` Block rendering rather than a separate heading
for every Line.Type. Before the exact wording, identify:

- `Landing`: the destination Namespace;
- `Model`: the target Model label and ship UUID;
- `Target`: the existing or proposed Block label and ship UUID when one
  already exists;
- `Block.Type` and `Line.Type`: their full retained Object.Type names;
- `Operation`: the concrete structural change, such as introducing a Block and
  its Line ships or adding a new Line edition to an existing ship; and
- `Edition.Approval.Token`: the proposal's opaque token.

The destination must not remain implicit merely because the Agent previously
rendered the Model. For a new Block or Line ship whose UUID is allocated only
during landing, say that the target is new instead of inventing an identity.
Render each Line as `- [<short-code>] <exact wording>`. The short code is a
presentation aid resolved through the selected Block.Type's vocabulary; it is
not part of the retained wording. Capture.Manifest retains the full Line.Type
ID. The exact retained wording must follow the marker verbatim so the Gate can
assess it without interpreting the overall presentation layout.

### Capture.Review.Turn renderings

The shape is stable while headings, spacing, and other presentation details
may evolve:

```md
## Context.Provider

Landing: User.Touched.Chatlas.Index → Tarav / <model-ship>
Target: new Block
Block.Type: Design.Block
Operation: introduce Block and three Line ships

- [DF] The central contextualization problem is bridging `Current.Chat.Context` to relevant `Diagram.Data` through Agent-driven discovery.
- [PR] Tarav provides `Context.Provider` mechanics that Agents operate to navigate, select, expand, render, and compile Diagram context.
- [CT] Tarav does not decide which context an Agent wants; direct block-by-block Model navigation remains the fallback instead of requiring a semantic recommendation algorithm.

Edition.Approval.Token: <opaque-token>

`::approve <opaque-token>`
```

`Impl.Req.Block` uses the same compact design-family vocabulary while making
its implementation target explicit:

```md
## 781.Impl.Req

Landing: User.Touched.Chatlas.Index → Tarav / <model-ship>
Target: new Block
Block.Type: Impl.Req.Block
Operation: introduce implementation request and two Line ships

- [DC] Implement the first `Context.Provider` vertical slice over Diagram Blocks.
- [CT] Keep semantic relevance selection Agent-operated.
```

`Issue.Block` uses the design-family vocabulary plus its own registered Line
Types. Include projected state when the target already exists or state is
mechanically significant:

```md
## Context.Provider.Missing

Landing: User.Touched.Chatlas.Index → Tarav / <model-ship>
Target: existing Block / <block-ship>
Block.Type: Issue.Block
State: Open
Operation: add a resolution Line

- [RESOLVE] The Project now provides a working block-by-block Context.Provider path.
```

For another Block.Type, query its registered vocabulary and apply the same
shape. Use its short codes only when their mapping is unambiguous; otherwise
render the full Line.Type ID in brackets.

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
for the landed supported records; its context already contains the approved proposal
turns and supporting User turns.

## Capture Stances

`::discuss` enters a sticky Discuss stance. Continue ordinary conversation,
present no approval-ready proposal, and preserve the roadmap, current draft,
and approved cluster. At a pause, advertise only `::review`.

`::review` enters Review stance and resumes proposal work from the current
foreground without repeating the full roadmap.

These are conversational dispositions. They do not mutate the Diagram or
change the evidentiary status of already captured records.

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

Do not manufacture approval evidence. Automatic Line editions retain their
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
records.

## Landing Through Tarav.Diagram

Create no `Capture.Manifest` during ordinary discussion. In reviewed mode,
compile it only after `::land` or `::land-all-approved`. In automatic mode,
compile and apply it once the internally developed bounded batch is settled;
the initial invocation already authorizes landing.

The Manifest is a faithful mechanical compilation. Entity creation and
semantic evolution go in `ships`; claims about existing entities or editions
go in `annotations`:

- each semantic Line is a `Diagram.Line.Ship` draft whose edition retains its
  exact wording, full `line_type`, producer Chatlas Turn, and rooted User
  support; the Ship record retains its Model and Block references;
- reviewed Lines retain `Verbatim.Gate` data containing the shared opaque
  token and exact proposal and approval Turn references;
- automatic Lines omit Gates;
- one approval exchange may cover several exact Lines when the proposal turn
  contains every wording, but each Line retains its own Gate instance;
- each new Block is a `Diagram.Block.Ship` whose first edition retains its full
  `block_type`; its Block.Type determines the allowed Line.Type vocabulary;
- append a fresh edition UUID to an existing Ship when the approved material
  continues that entity; allocate a new Ship UUID when it creates a new one;
- Annotations may add review, type, tag, rename-transition, or other claims,
  but they never create the Ship they discuss;
- missing, unknown, conflicting, or disallowed Object.Types are writable POIs,
  not permission to silently substitute another Type.

A new Block and Line compile to this shape; append-only updates may include
only the new editions of an existing Ship:

```json
{
  "class": "Tarav.Diagram.Capture.Manifest",
  "schema_version": 2,
  "model_ship": "<model-ship-uuid>",
  "ships": [
    {
      "id": "<block-ship-uuid>",
      "type": "Diagram.Block.Ship",
      "model_ship": "<model-ship-uuid>",
      "editions": [
        {
          "id": "<block-edition-uuid>",
          "block_type": "Design.Block",
          "data": {"label": "<block-label>"}
        }
      ]
    },
    {
      "id": "<line-ship-uuid>",
      "type": "Diagram.Line.Ship",
      "model_ship": "<model-ship-uuid>",
      "block_ship": "<block-ship-uuid>",
      "editions": [
        {
          "id": "<line-edition-uuid>",
          "line_type": "Design.Line.Principle",
          "producer": {"session_identity": "...", "turn_address": "...", "turn_hash": "..."},
          "support": [{"root": {"session_identity": "...", "turn_address": "...", "turn_hash": "..."}, "neighborhood": []}],
          "data": {"text": "<exact approved wording>"}
        }
      ]
    }
  ],
  "annotations": []
}
```

Use a temporary Manifest path and run:

```bash
tarav diagram capture template --project --manifest <path> --json
tarav diagram capture check --manifest <path> --json
tarav diagram capture apply --manifest <path> --json
```

Correct mechanical errors before applying. A semantic correction returns to
discussion or reviewed proposal work. POIs never block capture.

After applying, report created or updated Ship identities, edition and
Annotation identities, the Git commit, and all POIs. Re-render the affected
Model or Lines so the centralized
Assertion.Engine recomputes Gate standing from Chatlas evidence. Report the
result without writing derived `passed` flags into Annotation records.
