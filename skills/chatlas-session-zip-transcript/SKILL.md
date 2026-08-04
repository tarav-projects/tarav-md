---
name: chatlas-session-zip-transcript
description: Resolve a prior chat session and return the Chatlas `zip-transcript-summary` product artifact path, producing it through Chatlas when needed. USE WHEN the user wants prior session context recovered compactly while preserving every user turn. Called like a terminal command — `--session <id|uri|query>`.
---

# Chatlas Session Zip Transcript

Operational `Package.Aux.Skill` under `agentos-chatlas-pkg`.

Delegate prior-session transcript summary recovery to a subagent.

The default output is the path to a fresh Chatlas `zip-transcript-summary` product artifact. The artifact body should not be pasted into the parent chat unless the user explicitly asks for inline output.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- a bare session id, URI, or query resolves to `--session`.

## Skill.Arg.Section

### Skill.Arg::Session
- the prior session to recover: a session id, a session URI, or a provider-agnostic query
- required: true
- help: "the session to recover (id, URI, or query)"
- examples: --session "agentos://chat-session/..."

## Caller Contract

Run this skill in a separate agent by default.

Use a small model by default for the producer subagent.

Recommended candidate models:

- Codex: `gpt-5.6-luna`
- Claude: Haiku

Escalate only when the transcript is unusually long or complex, the user explicitly asks for higher-fidelity summarization, a cheaper model failed validation, or the output will drive a high-stakes decision.

The caller should provide the subagent:

- the session id, `agentos://chat-session/...` URI, identity hash, or other selector that resolves exactly one Chatlas session
- an instruction to load `agentos-chatlas-pkg/references/producer-zip-transcript-summary.md`
- an instruction to return only the artifact path unless diagnostics were explicitly requested

If no session identifier or query is provided, stop with:

```text
Could not resolve a prior session because no session identifier or query was provided.
Provide one of:
- a session id
- an agentos://chat-session/... URI
- an identity hash
- another Chatlas index selector that resolves exactly one session
```

## Subagent Prompt Shape

Use this shape when spawning the subagent:

```text
Use the chatlas-session-zip-transcript skill.
Load `agentos-chatlas-pkg/references/producer-zip-transcript-summary.md` and follow it.

Session selector: <option-based-chatlas-selector>

Check the `zip-transcript-summary` product; produce and commit it when it is not fresh.
Return only the path to the fresh artifact. Do not paste the artifact body.
```

## Expected Output

The subagent should return:

```text
<path-to-zip-transcript-summary.json>
```

## Notes

- This skill is for continuation and context recovery, not quote-accurate archival use.
- The Chatlas product artifact is sensitive prior-session content.
- Producer details, artifact format, compression rules, freshness, and failure handling live in `agentos-chatlas-pkg/references/producer-zip-transcript-summary.md`.
