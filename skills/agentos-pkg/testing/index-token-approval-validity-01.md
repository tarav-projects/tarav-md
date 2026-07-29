# Test: index-token-approval-validity-01

## Purpose

Evaluate whether `agentos-hugentics` treats approval tokens as exact proposal capabilities and fails closed for unknown or stale tokens.

## Entry Path

`AGENTS.md -> load agentos-pkg -> load agentos-hugentics -> references/capture.md -> references/edit.md`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `agentos-hugentics` to reason about this hypothetical interactive capture state. Do not edit files.

`Draft.A` was shown with token `idx-edition:old11111`. Its wording was then revised, invalidating that token. The complete revised proposal is now shown with token `idx-edition:new22222`.

Explain the transition for each user turn independently:

1. `::approve idx-edition:unknown0`
2. `::approve idx-edition:old11111`
3. `::approve idx-edition:new22222`
4. bare `::approve`

Show the command the workflow should expose after each rejected attempt.

## Behavior Tiers

### Minimal Pass

- Rejects the unknown token.
- Rejects the stale token.
- Accepts only `idx-edition:new22222` for the revised proposal.
- Does not write when approval succeeds.

### Expected Behavior

- Leaves the draft approval-ready after rejected attempts.
- Reprints exactly `::approve idx-edition:new22222` after unknown, stale, or bare approval.
- Explains that wording or destination changes require a fresh token and complete proposal.
- Treats the accepted token as tokenized verbatim approval.

### Above Expected

- Distinguishes general semantic approval support from the stricter `agentos-hugentics` workflow policy.
- Notes that the accepted draft enters the approved, unlanded cluster.

### Overwork

- Invents token hashes, persistent registries, or cryptographic verification.
- Edits files or mints a real anchor.

### Failure Signs

- Accepts the old or unknown token.
- Treats bare approval as satisfying the index verbatim gate.
- Lands the draft during approval.

## Navigation Trace

Expected: `agentos-pkg -> agentos-hugentics -> capture -> edit -> answer`.
