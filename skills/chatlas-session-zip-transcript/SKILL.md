---
name: chatlas-session-zip-transcript
description: Resolve a prior chat session and return the Chatlas `zip-transcript-agent-summary` artifact path, producing the view through Chatlas when needed. USE WHEN the user wants prior session context recovered compactly while preserving every user turn. Called like a terminal command — `--session <id|uri|query>`.
---

# Chatlas Session Zip Transcript

Operational `Package.Aux.Skill` under `agentos-chatlas-pkg`.

Delegate prior-session transcript summary recovery to a subagent.

The default output is the path to a fresh Chatlas `zip-transcript-agent-summary` `summary.json` artifact. The artifact body should not be pasted into the parent chat unless the user explicitly asks for inline output.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-skills-base` for the full convention.

- `-h` / `--help` prints the help into the chat instead of running (`Batchy.Skill.Help`).
- a bare session id, URI, or query resolves to `--session`.

## Skill.Arg.Section

### Skill.Arg:Session
- the prior session to recover: a session id, a session URI, or a provider-agnostic query
- required: true
- help: "the session to recover (id, URI, or query)"
- examples: --session "agentos://chat-session/..."

## Caller Contract

Run this skill in a separate agent by default.

Use a small model by default for the producer subagent.

Recommended candidate models:

- Codex: `gpt-5.4-mini`
- Claude: Haiku

Escalate only when the transcript is unusually long or complex, the user explicitly asks for higher-fidelity summarization, a cheaper model failed validation, or the output will drive a high-stakes decision.

The caller should provide the subagent:

- the session id, `agentos://chat-session/...` URI, identity hash, or other selector that resolves exactly one Chatlas session
- an instruction to load `agentos-chatlas-pkg/references/producer-zip-transcript-agent-summary.md`
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
Load `agentos-chatlas-pkg/references/producer-zip-transcript-agent-summary.md` and follow it.

Session selector: <option-based-chatlas-selector>

Ensure `zip-transcript`, then ensure `zip-transcript-agent-summary`.
Return only the path to the fresh `summary.json` artifact. Do not paste the artifact body.
```

## Expected Output

The subagent should return:

```text
<path-to-chatlas-summary.json>
```

## Notes

- This skill is for continuation and context recovery, not quote-accurate archival use.
- The Chatlas view artifact is sensitive prior-session content.
- Producer details, artifact format, compression rules, and failure handling live in `agentos-chatlas-pkg/references/producer-zip-transcript-agent-summary.md`.
