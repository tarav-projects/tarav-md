# Subagent Workflow

Follow this workflow when running `agentos-session-zip-transcript` as the delegated worker.

## Goal

Resolve a prior chat session, export the compact Chatlas `zip-transcript` view, compress the transcript, write it to a live note in the owning `Agentos.Project`, and return only a short manifest.

## Inputs

Required:

- a session id, `agentos://chat-session/...` URI, or provider-agnostic session query
- the owning `Agentos.Project` root for the `notes/live/` artifact

If the session input is missing, stop:

```text
Could not resolve a prior session because no session identifier or query was provided.
Provide one of:
- a session id
- an agentos://chat-session/... URI
- a query that can be resolved with `agentos chatlas query --include-match`
```

If the owning project is unclear, stop:

```text
Could not write the compressed transcript because the owning Agentos.Project is unclear.
Retry from inside the intended project or provide the exact Agentos.Project root.
```

Do not guess between sibling projects. Do not write to the umbrella repository root unless it is explicitly the intended project.

## Resolve The Session

If the input is already an `agentos://chat-session/...` URI, use it directly.

Otherwise resolve with:

```bash
agentos chatlas query "<query>" --include-match
```

Rules:

- If `session_count` is `1`, use `sessions[0].uri`.
- If `session_count` is `0`, fail clearly.
- If `session_count` is greater than `1`, do not guess. Return a short ambiguity report listing provider, session id, and URI for each candidate.

## Export The Transcript

Export:

```bash
agentos chatlas export "<resolved-uri>" --view zip-transcript --format json
```

Interpret the output as:

- top-level `turns` is the ordered turn source
- each turn has `role` and `text`
- the view contains visible user/assistant text only
- do not expect raw event tape, message ids, source refs, images, encrypted content, opaque reasoning, tool payloads, or normalization metadata

## Compression Rules

Always compress the transcript.

Hard requirements:

- Preserve every user turn in full, exactly, and in chronological order.
- Compress assistant turns to the shortest direct form that preserves new state.
- Keep decisions, accepted plans, constraints, concrete results, failures, warnings, unresolved issues, command names, paths, flags, identifiers, and test counts when they matter.
- Drop progress chatter, repeated framing, speculative narration, repeated summaries, apology/filler text, and status updates that did not change the outcome.
- Compress long structured outputs into short factual summaries instead of copying them wholesale.
- Do not pretend the output is the original transcript.

Preferred assistant rewrite shape:

```text
result; evidence; decision; unresolved issue only if one remains
```

## Live Note Target

Allocate a live-note prefix in the owning project:

```bash
agentos stdlib prefix next --project <project-root> --project-base <project-root-basename> --target notes/live
```

If prefix allocation fails, stop and report the failure. Do not assign a prefix manually.

Write to:

```text
notes/live/NNN-session-zip-transcript-<short-session-id>.md
```

Use the first 8 characters of the source session id for `<short-session-id>` when available. Never overwrite an existing path; stop and report a collision instead.

## Artifact Format

The live-note artifact must be self-describing:

```text
[compressed transcript]
User turns are preserved in full.
Assistant turns are compressed for brevity and may not match the original wording.
Do not treat this artifact as the original transcript.

source-session-id: <session-id>
source-session-uri: <resolved-uri>
resolved-via: agentos chatlas query --include-match
extracted-via: agentos chatlas export --view zip-transcript --format json

[user]
<full user content>

[assistant]
<compressed assistant content>
```

Include both session id and URI when available.

## Manifest Output

Return only this manifest unless the caller explicitly requested inline output:

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

Do not paste the transcript body in the final response.
