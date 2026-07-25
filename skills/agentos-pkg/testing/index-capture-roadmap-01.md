# Test: index-capture-roadmap-01

## Purpose

Evaluate whether interactive `agentos-index --capture` performs broad internal preparation while presenting a lightweight, context-aware roadmap before detailed drafting.

## Entry Path

`AGENTS.md -> load agentos-pkg -> load agentos-index -> references/capture.md -> references/index-capture-context-assembly.md`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `agentos-index --capture` to describe the opening response for this hypothetical interactive capture.

The visible conversation has already established four possible changes:

- clarify `User.Command` target resolution
- introduce a capture-time index academy
- add a lightweight capture roadmap
- make writing approved material continue the review loop

Assume relevant ontology, appendix, agendix, code, and adjacent surfaces exist. Do not edit files. Show the user-facing opening response, then explain briefly what preparation remains internal.

## Behavior Tiers

### Minimal Pass

- Loads the complete `Index.Capture.Context.Assembly` before candidate discovery.
- Grounds the chat and relevant external surfaces.
- Shows a `Capture.Roadmap` before detailed approval-ready drafts.
- Keeps the roadmap to short block or edit-cluster entries with one sentence each.

### Expected Behavior

- Maintains a broader internal candidate map than the roadmap.
- Avoids showing an evidence inventory, source matrix, or context-assembly transcript.
- Uses the user's existing context instead of re-explaining every concept.
- Recommends one first focus while allowing natural conversational redirection.
- Does not expose `::approve` for the roadmap itself.

### Above Expected

- Distinguishes exhaustive preparation from selective presentation.
- Notes that roadmap entries are provisional rather than an exhaustive backlog.

### Overwork

- Presents full drafts for every candidate.
- Dumps ontology, appendix, agendix, code, and chat evidence into the opening response.
- Loads a separate design workflow as a required runtime dependency.

### Failure Signs

- Treats the visible roadmap as the full candidate map.
- Asks the user to supply evidence that the agent can inspect.
- Treats a roadmap entry as approval-ready material.
- Prints command menus after the ordinary orientation turn.

## Navigation Trace

Expected: `agentos-pkg -> agentos-index -> capture -> index-capture-context-assembly -> answer`.

## Run Log

### Run 1 — 2026-07-25

- **Session**: `019f9955-691f-76e1-8de5-28d3e43c148a`
- **Model**: `gpt-5.4`
- **Tier**: expected
- **Trace**: `AGENTS.md -> agentos-pkg -> agentos-index -> capture -> index-capture-context-assembly -> answer`
- **Tool calls**: 7
- **Tokens**: 60,707 input; 1,305 output
- **Notes**: produced a four-entry roadmap, recommended one focus, kept grounding internal, and exposed no approval command
