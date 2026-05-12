---
name: agentos-session-zip-transcript
description: Resolve a prior chat session from a session id, session URI, or provider-agnostic query by delegating to a subagent that writes a compressed transcript live note and returns a short manifest. Use when the user wants prior session context recovered compactly while preserving every user turn.
---

# Session Zip Transcript

Delegate prior-session transcript recovery to a subagent.

The default output is a short manifest pointing to a `notes/live/` compressed transcript artifact. The transcript body should not be pasted into the parent chat unless the user explicitly asks for inline output.

## Caller Contract

Run this skill in a separate agent by default.

The caller should provide the subagent:

- the session id, `agentos://chat-session/...` URI, or provider-agnostic session query
- the owning `Agentos.Project` root for the live-note artifact, when known
- an instruction to load `references/subagent-workflow.md`
- an instruction to return only the manifest unless inline output was explicitly requested

If no session identifier or query is provided, stop with:

```text
Could not resolve a prior session because no session identifier or query was provided.
Provide one of:
- a session id
- an agentos://chat-session/... URI
- a query that can be resolved with `agentos chatlas query --include-match`
```

If the owning `Agentos.Project` is not clear to the subagent, it must complain and stop before writing.

## Subagent Prompt Shape

Use this shape when spawning the subagent:

```text
Use the agentos-session-zip-transcript skill.
Load `references/subagent-workflow.md` from the skill directory and follow it.

Session input: <session-id-or-uri-or-query>
Owning Agentos.Project for live note: <absolute-project-root-or-unclear>

Write the compressed transcript to `notes/live/` in the owning project.
Return only the short manifest. Do not paste the transcript body.
```

## Expected Manifest

The subagent should return:

```text
[compressed transcript manifest]
path: <project-relative-notes-live-path>
source-session-id: <session-id>
source-session-uri: <resolved-uri>
resolved-via: agentos chatlas query --include-match
extracted-via: agentos chatlas export --view zip-transcript --format json
turn-count: <number>
artifact-size-bytes: <number>
```

## Notes

- This skill is for continuation and context recovery, not quote-accurate archival use.
- The live-note artifact is sensitive prior-session content.
- Detailed resolution, compression, live-note allocation, artifact format, and failure handling live in `references/subagent-workflow.md`.
