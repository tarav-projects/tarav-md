---
name: tarav-hugentics
description: "Run Tarav's conversational capture workflow over a Project Diagram.Model. USE WHEN the user wants reviewed capture, automatic/unreviewed capture, a capture audit, or invokes `tarav-hugentics --capture`."
---

# Tarav Hugentics

`tarav-hugentics` is Tarav's public conversational capture surface. It
preserves the Hugentics alignment workflow while using Chatlas and the Tarav2
Diagram as its backend.

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
```

`--auto` and `--unreviewed` are aliases only within `--capture`. They omit both
per-Line review and a separate landing checkpoint: the initial User trigger
covers the bounded pass. They do not weaken support, producer, validation, or
POI requirements. `--audit` conflicts with either unreviewed-capture flag
because audit is read-only.

## Routing

Every non-help route above loads and follows
[`references/capture.md`](references/capture.md). Without an explicit flag,
route conversationally only when the user is clearly asking to capture or
review material into a Tarav Model.

The runtime commands `::discuss`, `::review`, `::approve <token>`, `::land`,
and `::land-all-approved` belong to the running Capture workflow, not to the
initial Batchy.Skill call.

## Boundary

This fresh skill does not use the legacy Markdown Index, Anchory, Agendix, or
Chat.Index backpropagation mechanics. Those are Attic evidence. Current
durable output is the flat Annotation tape of the target Diagram Namespace.
