# Test: index-capture-approval-continues-01

## Purpose

Evaluate whether approving one draft during interactive capture accumulates it and advances review instead of immediately suggesting landing.

## Entry Path

`AGENTS.md -> load tarav-pkg -> load tarav-hugentics -> references/capture.md`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `tarav-hugentics` to reason about this hypothetical interactive capture state. Do not edit files.

`Draft.A` is the foreground approval-ready block with token `idx-edition:a1b2c3d4`. `Draft.B` is the next unresolved roadmap cluster. Nothing is approved yet. The user says:

`::approve idx-edition:a1b2c3d4`

Explain the transition and show the next user-facing capture move.

## Behavior Tiers

### Minimal Pass

- Adds `Draft.A` to the approved, unlanded cluster.
- Keeps the capture workflow active.
- Advances to `Draft.B` instead of pausing to suggest landing.
- Does not write either draft.

### Expected Behavior

- Codesigns or presents only the next small approval-ready draft for `Draft.B`.
- Mints and shows a fresh `::approve <token>` command when the exact `Draft.B` wording and landing target are ready.
- Does not show a landing-only command pause merely because `Draft.A` is approved.
- Retains `Draft.A` as available for a later explicit or suggested landing.

### Above Expected

- Distinguishes the approved cluster from the foreground review item.
- Notes that an explicit, clearly targeted `::land Draft.A` would still be valid.
- Treats the echoed token as tokenized verbatim approval rather than only semantic approval.

### Overwork

- Reprints the full roadmap or all approved wording.
- Lands `Draft.A` without a separate landing command.

### Failure Signs

- Responds to approval only with `::land Draft.A`.
- Treats approval as a write.
- Loses `Draft.A` when moving to `Draft.B`.
- Requires landing before the review loop may continue.

## Navigation Trace

Expected: `tarav-pkg -> tarav-hugentics -> capture -> next foreground cluster`.
