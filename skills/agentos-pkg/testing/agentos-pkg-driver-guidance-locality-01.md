# Test: agentos-pkg-driver-guidance-locality-01

## Purpose

Evaluate whether `Package.Driver:Agentos.Pkg` helps a fresh agent handle realistic index-block work from an external project context.

This test intentionally proposes a concept that overlaps with existing Agentos index concepts. It evaluates both output quality and navigation behavior — what the agent did matters as much as what it produced.

## Entry Path

`AGENTS.md -> load agentos-pkg -> Package.SKILL:Agentos.Pkg`

## How To Run

Run with a small/cheap model by default:

- Codex: `gpt-5.4-mini` or another mini model
- Claude: a Haiku-class model

Spawn a fresh CLI session from `agentos-pkg-testground/`. Give it the `Subagent Prompt` only, plus normal project context such as `AGENTS.md`. Do not tell the subagent it is being tested, and do not provide the `Behavior Tiers`.

## Subagent Prompt

I'm thinking about a concept called Guidance.Locality.

It means that a piece of guidance should live where agents naturally need it, even if that creates some repeated explanation across surfaces. For example, project guidance might belong in AGENTS.md because agents see it early, while detailed package guidance belongs in the package skill or references.

Please propose an index block for this concept.

## Behavior Tiers

Semantic match, not exact wording. Evaluate what the agent did, not just what it produced.

### Minimal Pass

- Recognizes the request as index/block work.
- Uses `Agentos.Pkg` / index guidance to find index block conventions.
- Proposes a plausible candidate index block.
- Does not write to files unless explicitly approved.

### Expected Behavior

- Checks the routing table (`000-index.md`) for nearby concepts before proposing a new independent block.
- If overlap is visible from the routing table (e.g., `Natural.Placement`), flags it and suggests the concept may be better handled as an update, cited duplicate, or related placement under existing concepts.
- Identifies or asks for the target index before mutation.
- Navigation cost is proportional: one routing-table scan is cheap and the driver points there.

### Above Expected

- Loads a specific index page (e.g., `100-index.md`) to confirm overlap with `Natural.Placement`.
- May also mention `Entry.Path.Placement` and/or `Cited.Duplication` as related concepts.
- Useful but not required — shows deeper index navigation ability.

### Overwork

- Loads multiple index pages, spawns broad subagent searches, or does exhaustive index scans.
- May produce good output, but the cost is disproportionate to the prompt.
- Diagnostic signal: the driver or routing table may not be giving enough orientation for the agent to narrow its search cheaply.

### Failure Signs

- Cannot produce a recognizable index block shape.
- Writes to files without explicit approval.
- Assumes the target index is `Agentos.Pkg` only because Agentos index tools are involved.
- Creates `Guidance.Locality` as an obviously independent concept without checking nearby existing concepts.

## Navigation Trace

When evaluating, note which surfaces the agent loaded and in what order. This makes the test diagnostic for entry-path quality, not just pass/fail.

Example trace: `SKILL.md -> agentos-index -> 000-index.md -> proposed block` (expected), vs. `SKILL.md -> agentos-index -> 000-index.md -> 100-index.md -> 101-index.md -> ...` (overwork).

## Evolution Notes

This test will be enriched as we run it and discover new failure modes or unexpected agent strategies.
