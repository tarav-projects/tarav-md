---
name: tarav-hugentics
description: "Run Tarav's conversational capture, Issue, and implementation workflows over a Project Diagram.Model. USE WHEN the user wants reviewed or automatic capture, wants to park or maintain an Issue, requests a capture audit, implementation design, Impl.Req review or execution, end-to-end development, or invokes `tarav-hugentics --capture`, `tarav-hugentics --issues`, or `tarav-hugentics --impl`."
---

# Tarav Hugentics

`tarav-hugentics` is Tarav's public conversational capture and implementation
surface. It preserves the Hugentics alignment workflows while using Chatlas and
the Tarav2 Diagram as its User-Touched indexing backend.

Before operating, read the Tarav Constitution at
[`../tarav-pkg/CONSTITUTION.md`](../tarav-pkg/CONSTITUTION.md). Capture must
remain writable, evidence-linked, and nonblocking in the presence of POIs.

## Batchy.Skill Contract

Treat the skill call like a command line:

- explicit flags win over conversational inference;
- a trailing value is the capture focus or prompt;
- `-h` or `--help` prints the command surface and stops;
- ask rather than guess when the requested route remains materially ambiguous;
- flags select workflow behavior; they are not forwarded to the Tarav CLI.

## Command Surface

```text
tarav-hugentics --capture [PROMPT]
    Interactive reviewed capture. Initial stance: Review.

tarav-hugentics --capture --auto [PROMPT]
tarav-hugentics --capture --unreviewed [PROMPT]
    Equivalent one-trigger unreviewed routes; the invocation authorizes one
    bounded capture pass and its landing.

tarav-hugentics --capture --audit [PROMPT]
    Read-only contextualization and Capture.Roadmap.

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

Within `--impl`, `--auto` or `--autonomous` selects autonomous alignment at
declared checkpoints. It does not change Diagram support requirements or turn
Agent-generated coordination material into User-Touched data.

## Routing

Capture routes load and follow [`references/capture.md`](references/capture.md).
Issue routes first load [`references/issues.md`](references/issues.md), which
selects one Issue workflow without creating a separate Parking.Note object.
Implementation routes first load
[`references/impl.md`](references/impl.md), which selects exactly one
implementation workflow module. Without an explicit route, infer capture or
Issue, or implementation only when the conversational request is clear.

The runtime commands `::discuss`, `::review`, `::approve <token>`, `::land`,
and `::land-all-approved` belong to the running Capture workflow, not to the
initial Batchy.Skill call.

## Boundary

This fresh skill does not use the legacy Markdown Index, Anchory, Agendix, or
Chat.Index backpropagation mechanics. Those are Attic evidence. Current
User-Touched index output is the flat Annotation tape of the target Diagram
Namespace; implementation live notes remain separate Product.Surfaces.

Implementation retains two deliberately different surfaces:

- the live-note `Impl.Req` is the Agent's main coordination artifact and phase
  boundary;
- its `Impl.Req.Diagram` points to one `Impl.Req.Block` containing only
  supported User-Touched material relevant to that implementation request.

Do not copy Agent-only plans, logs, summaries, or incidental implementation
observations into the Block merely because they appear in the live note.

Implementation capture is the ordinary Capture workflow constrained to one
`Impl.Req.Block` target. It must resolve the same Namespace, Project.Model,
current context, Object.Types, support, Manifest checks, and landing mechanics
as `--capture`. A live note never substitutes for a missing Diagram target.
