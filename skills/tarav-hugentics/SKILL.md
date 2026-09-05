---
name: tarav-hugentics
description: "Run Tarav's grounding, conversational capture, Issue, and implementation workflows over Project Diagram.Models. USE WHEN the user wants Diagram-backed context, reviewed or automatic capture, Issue work, implementation design or execution, or invokes `tarav-hugentics --ground`, `--capture`, `--issues`, or `--impl`."
---

# Tarav Hugentics

`tarav-hugentics` is Tarav's public grounding, conversational capture, and
implementation surface. It preserves the Hugentics alignment workflows while
using Chatlas and the Tarav.Diagram as its User-Touched indexing backend.

Before operating, read the Tarav Constitution at
[`../tarav-pkg/CONSTITUTION.md`](../tarav-pkg/CONSTITUTION.md). Capture must
remain writable, evidence-linked, and nonblocking in the presence of POIs.

## Batchy.Skill Contract

Treat the skill call like a command line:

- explicit flags win over conversational inference;
- a trailing value is the selected workflow's focus or input;
- `-h` or `--help` prints the command surface and stops;
- ask rather than guess when the requested route remains materially ambiguous;
- flags select workflow behavior; they are not forwarded to the Tarav CLI.

## Command Surface

```text
tarav-hugentics --ground [FOCUS]
    Build or resume the current session's Diagram.View and use it to
    contextualize the collaboration through Agent-operated navigation.

tarav-hugentics --capture [PROMPT]
    Interactive reviewed capture. Initial stance: Review.

tarav-hugentics --capture --auto [PROMPT]
tarav-hugentics --capture --unreviewed [PROMPT]
    Equivalent one-trigger unreviewed routes; the invocation authorizes one
    bounded capture pass and its landing.

tarav-hugentics --capture --audit [PROMPT]
    Read-only contextualization and Capture.Roadmap.

tarav-hugentics --capture --inline <SURFACE>
    Leave lightweight, resolvable Chatlas Turn references in one Product.Surface.
    The first surface specialization is Markdown.

tarav-hugentics --capture --inline --audit <SURFACE>
    Audit the embedded references in one Product.Surface without mutation.
    Generic audit semantics are applied through surface-native inspection.

tarav-hugentics --issues [INPUT]
tarav-hugentics --issue [INPUT]
    Work with Issue.Blocks. New material defaults to the short Parking
    workflow; an existing Issue defaults to maintenance.

tarav-hugentics --issues --park [INPUT]
    Explicitly select the Parking workflow.

tarav-hugentics --issues --audit [QUERY]
    Inspect relevant Issue.Blocks and their POIs without mutation.

tarav-hugentics --impl [INPUT]
tarav-hugentics --impl --design [INPUT]
tarav-hugentics --impl-design [INPUT]
    Design an implementation and produce its live-note Impl.Req. Bare --impl
    defaults here for actionable input that is not already an Impl.Req.

tarav-hugentics --impl --review <IMPL_REQ>
tarav-hugentics --review <IMPL_REQ>
    Cold, read-only readiness and evidence review.

tarav-hugentics --impl --execute <IMPL_REQ|INPUT>
tarav-hugentics --execute <IMPL_REQ|INPUT>
tarav-hugentics --exec <IMPL_REQ|INPUT>
    Execute an existing Impl.Req. Explicit Execute with direct input first
    bootstraps its Impl.Req surfaces through ordinary capture.

tarav-hugentics --impl --develop [INPUT]
tarav-hugentics --develop [INPUT]
tarav-hugentics --dev [INPUT]
    Design the durable Impl.Req, cold-reload it, then execute it.

tarav-hugentics --impl --harvest [PROMPT]
tarav-hugentics --impl-harvest [PROMPT]
    Select one ready implementation unit from mixed discussion and Develop it.

tarav-hugentics --impl --capture
tarav-hugentics --impl-capture
    Compose implementation capture behavior with the selected mutating
    implementation workflow; this is not an independent implementation phase.
```

`--auto` and `--unreviewed` are aliases only within `--capture`. They omit both
per-Line review and a separate landing checkpoint: the initial User trigger
covers the bounded pass. They do not weaken support, producer, validation, or
POI requirements. `--audit` conflicts with either unreviewed-capture flag
because audit is read-only.

Within `--capture --inline`, `--audit` selects the read-only audit route instead
of the ordinary reference-writing route. It takes exactly one surface and does
not compose with `--auto` or `--unreviewed`.

Within `--impl`, `--auto` or `--autonomous` selects autonomous alignment at
declared checkpoints. It does not change Diagram support requirements or turn
Agent-generated coordination material into User-Touched data.

## Routing

Grounding routes load and follow [`references/ground.md`](references/ground.md).
Ordinary Capture routes load and follow [`references/capture.md`](references/capture.md).
`--capture --inline`, including its composed `--audit` route, instead loads and follows
[`references/inline-capture.md`](references/inline-capture.md); it edits the
selected Product.Surface only in the ordinary non-audit route and never enters
Diagram capture.
Issue routes first load [`references/issues.md`](references/issues.md), which
selects one Issue workflow without creating a separate Parking.Note object.
Implementation routes first load
[`references/impl.md`](references/impl.md), which selects exactly one
implementation workflow module. Without an explicit route, infer capture or
grounding, Issue, or implementation only when the conversational request is
clear.

Grounding is ungated and read-only toward the Diagram semantic database. It may
create and maintain a `Diagram.View`; that View is a separate contextual WIP
surface and never supplies approval, capture, or Diagram mutation.

The runtime commands `::discuss`, `::review`, `::approve <token>`, `::land`,
and `::land-all-approved` belong to the running Capture workflow, not to the
initial Batchy.Skill call.

## Boundary

This fresh skill does not use the legacy Markdown Index, Anchory, Agendix, or
Chat.Index backpropagation mechanics. Those are Attic evidence. Current
User-Touched index output is the target Diagram Namespace's typed Ship database
and separate Annotation claims; implementation live notes remain separate
Product.Surfaces.

Implementation retains two deliberately different surfaces:

- the live-note `Impl.Req` is the Agent's main coordination artifact and phase
  boundary;
- its `Impl.Req.Diagram` points to one `Impl.Req.Collection` and the durable
  `Diagram.Draft` that accumulates supported User-Touched material relevant to
  that implementation request.

An implementation Line remains semantically attached to the most suitable
existing Model Block when possible, while its edition is hosted by the
`Impl.Req.Collection`. This preserves Model encapsulation without adding
automatic implementation material to the Model's primary load surface.

Implementation capture uses ordinary Capture semantics inside one writable
Draft. It must resolve the same Namespace, Project.Model, current context,
Object.Types, support, checks, and landing mechanics as `--capture`. The Draft
is reconciled across slices and applied once at completion. A live note never
substitutes for a missing Diagram target or Draft.

The workflow's explicit User invocation is retained as one
`Capture.Authorization.Gate`; affected editions reference that Gate. This
records permission to write, not review of wording.
