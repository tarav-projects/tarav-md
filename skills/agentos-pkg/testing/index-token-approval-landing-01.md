# Test: index-token-approval-landing-01

## Purpose

Evaluate whether landing token-approved index lines records typed Chatlas evidence and verifies the new lines.

## Entry Path

`AGENTS.md -> load agentos-pkg -> load agentos-hugentics -> references/edit.md -> references/link.md -> references/check.md`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `agentos-hugentics` to describe, without executing, the landing procedure for this hypothetical approved line:

- session identity: `sessionhash`
- proposal event: `event-40`
- approval event: `event-42`
- token: `idx-edition:a1b2c3d4`
- user approval text: `::approve idx-edition:a1b2c3d4`

Show the relevant `agentos chatlas anchory register` shape and the post-edit linter command. Explain which events become support members.

## Behavior Tiers

### Minimal Pass

- Registers `sessionhash:event-42` as the user support member.
- Records `tokenized.approval.turn` cargo with the token plus proposal and approval refs.
- Does not add the assistant proposal as a support member.
- Runs both approval checks after landing.

### Expected Behavior

- Uses `--member sessionhash:event-42`, never timestamp registration.
- Uses `--member-types` keyed by the approval member.
- Sets `verbatim_turn` to `sessionhash:event-40` and `approval_turn` to `sessionhash:event-42`.
- Shows `agentos index linter ... --check line-approval --check line-verbatim-gate --scope <edited-path>`.

### Above Expected

- Explains that the assistant event is referenced by cargo for verification while the support set remains user-turn-only.
- Notes that legacy review-debt warnings outside the edited scope are not regressions.

### Overwork

- Executes commands or edits a real index.
- Uses raw provider transcripts or SQL.

### Failure Signs

- Registers by timestamp.
- Adds the assistant event as a support member.
- Omits typed cargo or either opt-in check.

## Navigation Trace

Expected: `agentos-pkg -> agentos-hugentics -> edit -> link -> check -> answer`.
