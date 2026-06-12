# Producer: zip-transcript-agent-summary

Use this reference when an agent must produce or retrieve the Chatlas view:

```text
zip-transcript-agent-summary
```

The caller wants a lower-token version of another chat session and should receive only the path to a fresh `summary.json` artifact.

## Contract

Return only the artifact path unless diagnostics were explicitly requested.

Chatlas view storage is the durable artifact surface.

## Inputs

Required:

- one Chatlas index selector that resolves exactly one session, usually:
  - `--session-id <session-id>`
  - `--uri <agentos://chat-session/...>`
  - `--identity-hash <hash>`

Use option-based selectors only. Do not use positional session arguments.

## Ensure Dependency

The summary depends on the materialized `zip-transcript` view.

Run:

```bash
agentos chatlas views get --view zip-transcript <selector-options>
```

This auto-produces or refreshes the internal transcript view when needed.

## Check Target View

Run:

```bash
agentos chatlas views status --view zip-transcript-agent-summary <selector-options>
```

If the state is `fresh`, return:

```bash
agentos chatlas views path --view zip-transcript-agent-summary <selector-options>
```

## Produce Missing Or Stale Summary

If the target view reports `production_required`, get the source transcript path:

```bash
agentos chatlas views path --view zip-transcript <selector-options>
```

Read the `zip-transcript.json` artifact. It contains:

- `session`
- ordered `turns`
- each turn has `role` and `text`

Stage the external view:

```bash
agentos chatlas views stage --view zip-transcript-agent-summary <selector-options>
```

Write this file inside the returned stage directory:

```text
summary.json
```

Write compact JSON. Do not pretty-print or add indentation.

Then commit:

```bash
agentos chatlas views commit --stage-id <stage-id>
```

Finally return:

```bash
agentos chatlas views path --view zip-transcript-agent-summary <selector-options>
```

## Artifact Shape

`summary.json` is a lower-token, turn-aligned replacement for `zip-transcript`.

Required shape:

```json
{
  "class": "agentos.chatlas.zip_transcript_agent_summary",
  "schema_version": 1,
  "view": "zip-transcript-agent-summary",
  "source_view": "zip-transcript",
  "session": {},
  "turns": [
    {
      "role": "user",
      "text": "verbatim user turn"
    },
    {
      "role": "assistant",
      "text": "compressed assistant turn"
    }
  ]
}
```

Copy `session` from the source `zip-transcript.json`.

Commit validates the staged artifact against the source `zip-transcript` view. The linter requires:

- `session` exactly matches the source `zip-transcript.session`
- `turns` count exactly matches source `zip-transcript.turns`
- every turn is a JSON object
- every turn `role` exactly matches the source turn role at the same index
- every turn has string `text`
- every user turn `text` exactly matches the source turn text
- every assistant turn `text` is non-blank

## Compression Rules

Always preserve turn order and turn alignment.

Hard requirements:

- Preserve every user turn verbatim, in full, and in chronological order.
- Keep every assistant turn in place, but summarize it aggressively.
- Preserve enough assistant context for later user references such as "nice", "this", quoted text, corrections, or "the previous idea" to remain intelligible.
- Preserve decisions, accepted plans, constraints, commands, paths, identifiers, test results, failures, warnings, and unresolved issues.
- Remove progress chatter, repeated framing, obvious restatement, speculative narration, apology/filler, and verbose output that does not change state.
- If a later user turn corrects or supersedes earlier assistant content, keep the corrected relationship clear enough for the transcript to make sense.
- Do not pretend the summary is the original transcript.

Preferred assistant rewrite shape:

```text
result; evidence; decision; unresolved issue only if one remains
```

## Failure Handling

If the selector resolves zero sessions, stop with the Chatlas selector error.

If the selector resolves multiple sessions, do not guess. Ask for a narrower selector.

If staging or commit fails, report the failing command and stderr. Do not write outside the stage directory.
