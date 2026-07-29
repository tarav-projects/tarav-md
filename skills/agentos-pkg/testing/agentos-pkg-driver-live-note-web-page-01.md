# Test: agentos-pkg-driver-live-note-web-page-01

## Purpose

Evaluate whether `Package.Driver::Agentos.Pkg` helps a fresh agent route a natural `live-note` request to the live-note surface instead of confusing it with index block authoring or formal design artifacts.

## Entry Path

`AGENTS.md -> load agentos-pkg -> Package.SKILL::Agentos.Pkg`

## How To Run

Run with a small/cheap model by default:

- Codex: `gpt-5.4-mini` or another mini model
- Claude: a Haiku-class model

Spawn a fresh CLI session from `agentos-pkg-testground/`. Give it the `Subagent Prompt` only, plus normal project context such as `AGENTS.md`. Do not tell the subagent it is being tested, and do not provide the `Behavior Tiers`.

## Subagent Prompt

I have an idea for a web page and want to keep it as a live-note.

The page is a compact personal dashboard for a solo researcher. It should show today's priorities, active reading notes, open questions, and a small area for quick captured thoughts. The feeling should be calm and focused, not like a productivity app with too many widgets.

Please help me make the live-note.

## Behavior Tiers

Semantic match, not exact wording. Evaluate what the agent did, not just what it produced.

### Minimal Pass

- Recognizes this as `Agentos.Live.Note` work because the prompt says `live-note`.
- Uses `agentos-live-surfaces` or live-note guidance surfaced by `agentos-pkg`.
- Does not route to index block authoring.
- Produces a reasonable live-note draft or explains the live-note creation path.
- Does not write files unless explicitly approved.

### Expected Behavior

- Identifies or asks for the target project for the live-note path.
- Uses or mentions the live-note numbering/location protocol.
- Keeps the note lightweight and editable.
- Does not convert the request into a formal design-session artifact unless the user asks.
- Captures the web page idea clearly enough that a later agent can continue from it.
- Navigation cost is proportional: loads `agentos-live-surfaces` or equivalent, does not load index surfaces.

### Above Expected

- Proposes a concrete live-note draft with the web page content sketched out.
- Mentions the `agentos` CLI for prefix allocation.
- Asks about placement (which `notes/live/` folder).

### Overwork

- Loads index pages, design-session guidance, or hugentics workflows for a simple live-note request.
- Diagnostic signal: the decision router may not be discriminating well enough between subsystems.

### Failure Signs

- Treats the request as an index concept/block task.
- Starts a design-session artifact without user intent.
- Writes files without explicit approval.
- Ignores the word `live-note` and gives only generic web page design advice.

## Navigation Trace

When evaluating, note which surfaces the agent loaded. Key signal: did the agent go to live-note surfaces directly, or did it detour through index/hugentics?

Expected trace: `SKILL.md -> agentos-live-surfaces -> draft`
Overwork trace: `SKILL.md -> agentos-hugentics -> ... -> live-note`

## Evolution Notes

This test will be enriched as we run it and discover new failure modes or unexpected agent strategies.
