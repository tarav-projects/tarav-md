# Test: index-token-approval-multiple-drafts-01

## Purpose

Evaluate whether distinct approval tokens disambiguate simultaneous approval-ready index drafts.

## Entry Path

`AGENTS.md -> load tarav-pkg -> load tarav-hugentics -> references/capture.md`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `tarav-hugentics` to reason about this hypothetical interactive capture state. Do not edit files.

Two exact proposals are approval-ready:

- `Draft.A` carries `idx-edition:aaaa1111`.
- `Draft.B` carries `idx-edition:bbbb2222`.

First show the available approval commands. Then explain what happens when the user says `::approve idx-edition:bbbb2222`.

## Behavior Tiers

### Minimal Pass

- Shows one resolved tokenized command per draft.
- Approves only `Draft.B`.
- Leaves `Draft.A` approval-ready.
- Does not write either draft.

### Expected Behavior

- Renders `::approve idx-edition:aaaa1111` and `::approve idx-edition:bbbb2222`.
- Uses the token itself to resolve the exact proposal without asking for a target.
- Adds `Draft.B` to the approved, unlanded cluster and continues the review loop.

### Above Expected

- Explains that tokens are proposal-specific and cannot be exchanged between drafts.

### Overwork

- Prints the full roadmap or unrelated command menus.
- Invents a persistent workflow registry.

### Failure Signs

- Approves both drafts.
- Asks which draft `bbbb2222` means.
- Offers bare `::approve Draft.A` as the normal workflow command.

## Navigation Trace

Expected: `tarav-pkg -> tarav-hugentics -> capture -> answer`.
