# Test: index-token-approval-landing-01

## Purpose

Evaluate whether landing token-approved index lines records independent Chatlas support and gate relationships and verifies the new lines.

## Entry Path

`AGENTS.md -> load tarav-pkg -> load tarav-hugentics -> references/edit.md -> references/link.md -> references/check.md`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `tarav-hugentics` to describe, without executing, the landing procedure for this hypothetical approved line:

- session identity: `sessionhash`
- substantive user turn: `turn-38`
- proposal assistant turn: `turn-40`
- approval user turn: `turn-42`
- token: `idx-edition:a1b2c3d4`
- user approval text: `::approve idx-edition:a1b2c3d4`

Show the relevant `agentos chatlas anchory register` shape and the post-edit linter command. Explain which turns become support members and which are referenced only by the gate.

## Behavior Tiers

### Minimal Pass

- Registers `sessionhash:turn-38` as the semantic support member.
- Records a `tokenized_verbatim_approval` gate with the token plus proposal and approval `Normal.Turn.Ref`s.
- Does not add the assistant proposal as a support member.
- Runs both approval checks after landing.

### Expected Behavior

- Uses `--member sessionhash:turn-38`, never timestamp registration.
- Uses `--gates` with both explicit gate namespaces.
- Sets `proposal_turn` to the exact `turn-40` ref and `approval_turn` to the exact `turn-42` ref.
- Shows `agentos index linter ... --check line-approval --check line-verbatim-gate --scope <edited-path>`.

### Above Expected

- Explains that the assistant proposal and user approval are gate references, while support membership remains an independent semantic judgment.
- Notes that legacy review-debt warnings outside the edited scope are not regressions.

### Overwork

- Executes commands or edits a real index.
- Uses raw provider transcripts or SQL.

### Failure Signs

- Registers by timestamp.
- Adds the assistant proposal as a support member merely because it participates in the gate.
- Omits the gate relationship or either opt-in check.

## Navigation Trace

Expected: `tarav-pkg -> tarav-hugentics -> edit -> link -> check -> answer`.
