# Test: index-capture-write-continues-01

## Purpose

Evaluate whether landing approved material during capture preserves the active review loop and re-grounds the remaining roadmap.

## Entry Path

`AGENTS.md -> load agentos-pkg -> load agentos-hugentics -> references/capture.md`

## How To Run

Run from `agentos-pkg-testground/` in a fresh session. Give the tested agent only the `Subagent Prompt` plus normal project context. Do not provide the behavior tiers.

## Subagent Prompt

Use `agentos-hugentics` to reason about this hypothetical interactive capture state. Do not edit files.

`Draft.A` and `Draft.B` are approved and unlanded. `Draft.C` is the next roadmap cluster and has not been drafted. The user says:

`::write Draft.A`

Explain the transition and the next user-facing capture move.

## Behavior Tiers

### Minimal Pass

- Lands only approved `Draft.A`.
- Leaves `Draft.B` approved and unlanded.
- Keeps the capture workflow active.
- Re-grounds after the write because the touched index changed.

### Expected Behavior

- Updates the internal candidate map against the changed surface.
- Refreshes only roadmap entries affected by the write.
- Continues toward one small foreground cluster rather than replaying the whole roadmap.
- Does not treat `::write` as approval, workflow completion, or a Git commit.

### Above Expected

- Shows a compact roadmap delta only if the write changed the visible session arc.
- Preserves natural conversation as a way to redirect the next focus.

### Overwork

- Reprints the context assembly or complete evidence inventory after landing.
- Restarts the entire capture session ceremonially.

### Failure Signs

- Lands `Draft.B` without it being targeted.
- Ends capture after writing `Draft.A`.
- Continues from a stale candidate map without re-grounding.

## Navigation Trace

Expected: `agentos-pkg -> agentos-hugentics -> capture -> edit landing procedure -> capture`.

## Run Log

### Run 1 — 2026-07-25

- **Session**: `019f9956-b1bf-78b1-a7e0-8b4c08e6be70`
- **Model**: `gpt-5.4`
- **Tier**: expected
- **Trace**: `AGENTS.md -> agentos-pkg -> agentos-hugentics -> capture -> edit -> answer`
- **Tool calls**: 5
- **Tokens**: 61,002 input; 1,118 output
- **Notes**: landed only `Draft.A`, preserved `Draft.B`, left `Draft.C` undrafted, re-grounded, and continued the capture loop
