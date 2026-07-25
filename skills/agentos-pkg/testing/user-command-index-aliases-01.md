# Test: user-command-index-aliases-01

## Purpose

Evaluate whether an agent operating `agentos-index` resolves equivalent command triggers to one canonical transition while preserving approval and landing as separate acts.

## Entry Path

`AGENTS.md -> load agentos-pkg -> load agentos-index -> load agentos-batchy-skills`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `agentos-index` to reason about this hypothetical interactive capture state. Do not edit files.

There is one foreground approval-ready block named `Draft.A`, with a concrete landing target. Nothing is approved yet.

Explain the state transition for each user turn independently:

1. `I agree with the wording. ::approve`
2. `I agree with the wording. ::approved`

Then assume `Draft.A` is approved and unlanded. Explain the state transition for:

3. `::land`
4. `We can continue discussing afterward; ::write`

State whether any pair differs semantically and whether approval itself writes a file.

## Behavior Tiers

### Minimal Pass

- Resolves `::approve` and `::approved` to the same approval transition.
- Resolves `::land` and `::write` to the same landing transition.
- States that approval does not write.

### Expected Behavior

- Names `User.Command::Approve` and `User.Command::Land`.
- Treats the prose surrounding a command as normal conversation without losing the command.
- Lands only after the target is already approved.
- Distinguishes the in-workflow `::write` trigger from the `--write` skill argument.

### Above Expected

- Notes that the unique foreground target satisfies the contextual target argument.
- Mentions that a later change to wording or destination invalidates approval.

### Overwork

- Invents a command runtime, persistent registry, or parser implementation.
- Loads unrelated Hugentic implementation workflows.

### Failure Signs

- Treats aliases as different commands or gives them different semantics.
- Writes or proposes writing during approval.
- Treats `::write` as a Git commit or as the `--write` skill invocation.
- Requires the command to begin the user turn.

## Navigation Trace

Expected: `agentos-pkg -> agentos-index -> agentos-batchy-skills -> answer`.

## Evolution Notes

Add real multi-turn traces when Testground gains native scripted-turn support.
