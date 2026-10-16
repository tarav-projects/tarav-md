# AGENTS.md

## Purpose

`tarav-chatlas-md` owns Chatlas design notes and markdown coordination — the design surface for Chatlas concepts and the provider-neutral Normal Model used by current Tarav workflows.

Chatlas Python mechanics live at `tarav-py/src/tarav/chatlas/`.

## Orientation

- Load `tarav-pkg` and read its `CONSTITUTION.md`. Any surface claiming to be part of Tarav must comply with it.
- Load `tarav-chatlas-pkg` for the Chatlas package index and concept blocks.
- Design sessions live in `notes/live/*-design-session.md`.

## Harness Reference

Local source copies of agent-coding harnesses are kept for studying how each provider natively represents a session. They are **reference-only**: outside the Tarav repositories, never committed here, used as `Hard.Evidence` when designing the Chatlas Normal Model and when understanding each provider's own raw format that the Chatlas normalizers read.

Location: `~/Documents/workspaces/main-workspace/harnesses/`

- `pi-mono/` — PI agentic harness (TypeScript monorepo). Session model is an append-only JSONL entry **tree**: typed entries (message / model-change / thinking-change / compaction / branch-summary / label / custom), branching via `parentId`, forks via session lineage. Anatomy in `packages/coding-agent/src/core/session-manager.ts` and `packages/coding-agent/docs/session.md`.
- `codex-repo/` — OpenAI Codex harness (shallow clone of `openai/codex`). Rust core in `codex-rs/`, CLI in `codex-cli/`, SDK in `sdk/`. Rollout-based session format — the ground truth for the Chatlas `codex.raw_rollout` normalizer's field semantics.
- `claude-leaked/` — Claude Code source recovered from a published npm sourcemap (Mar 2026). JS/TS under `src/` (tools, coordinator, context, tasks, etc.). Use for understanding Claude Code's native session/transcript shape.

Use these to verify provider-native field semantics against real source instead of inferring from notes. Take structural ideas as *inspiration*; providers never conform to `Chatlas.Session.Model` — Chatlas normalizes their formats inward.
