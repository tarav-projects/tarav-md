# Test: user-command-index-land-all-approved-01

## Purpose

Evaluate whether `tarav-hugentics` treats `::land-all-approved` as a zero-argument batch transition scoped to one foreground workflow.

## Entry Path

`AGENTS.md -> load tarav-pkg -> load tarav-hugentics -> load tarav-batchy-skills`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `tarav-hugentics` to reason about this hypothetical interactive capture state. Do not edit files.

One foreground index capture workflow holds approved, unlanded `Draft.A` and `Draft.B`; `Draft.C` is unapproved. The user says:

`::land-all-approved`

Explain the transition and the next capture move. Then explain what must happen instead if two active index workflows both hold approved clusters and neither is foreground.

## Behavior Tiers

### Minimal Pass

- Lands `Draft.A` and `Draft.B`.
- Does not land or approve `Draft.C`.
- Treats `::land-all-approved` as taking no target argument.
- Fails closed when no single foreground workflow supplies the approved cluster.

### Expected Behavior

- Names `User.Command::LandAllApproved`.
- Runs each approved item through its declared landing procedure.
- Re-grounds after the writes and keeps the capture workflow active.
- Asks which workflow is foreground in the ambiguous two-workflow case.

### Above Expected

- Distinguishes removal of target ambiguity from preservation of workflow ambiguity.
- Notes that ordinary `::land [target]` remains available for selective landing.

### Overwork

- Invents a persistent workflow registry or command parser.
- Requires a redundant `all` target argument.

### Failure Signs

- Lands unapproved `Draft.C`.
- Chooses between ambiguous workflows.
- Treats the command as approval, workflow completion, or a Git operation.

## Navigation Trace

Expected: `tarav-pkg -> tarav-hugentics -> tarav-batchy-skills -> capture/edit landing procedure -> answer`.
