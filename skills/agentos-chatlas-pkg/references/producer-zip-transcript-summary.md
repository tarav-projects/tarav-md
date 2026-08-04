# Producer: zip-transcript-summary

Use this reference when an agent must produce or retrieve the Chatlas product:

```text
zip-transcript-summary
```

`zip-transcript-summary` is a `Chatlas.Product`: a retained agent production over
the `zip-transcript` `Chatlas.View`. The caller wants a lower-token version of
another chat session and should receive only the path to a fresh artifact.

## Contract

Return only the artifact path unless diagnostics were explicitly requested.

The product depot is the durable artifact surface. A missing or stale product is
an invitation to contribute one; reads never regenerate it automatically.

## Inputs

Required:

- one Chatlas index selector that resolves exactly one session, usually:
  - `--session-id <session-id>`
  - `--uri <agentos://chat-session/...>`
  - `--identity-hash <hash>`

Use option-based selectors only. Do not use positional session arguments.

## Check The Product

Run:

```bash
agentos chatlas products status --product zip-transcript-summary <selector-options> --json
```

Chatlas renders human-readable text by default, so every step whose output you
parse passes `--json`. `products path` is deliberately left bare: its text output
is exactly the artifact path, which is what this producer returns.

If `state` is `fresh`, return:

```bash
agentos chatlas products path --product zip-transcript-summary <selector-options>
```

There is no separate dependency to materialize. The `zip-transcript` input view
is a disposable projection recomputed on every product read.

## Produce Missing Or Stale Product

If `state` is `production_required`, stage the production:

```bash
agentos chatlas products produce --product zip-transcript-summary <selector-options> --json
```

This returns `stage.stage_id`, `stage.input_path`, and `stage.output_path`.

Read `stage.input_path`. It is the current `zip-transcript` view payload and
contains:

- `class`, `schema_version`, `view`
- `session`
- ordered `turns`, each with `role` and `text`

Write the compressed artifact to `stage.output_path`. Write compact JSON. Do not
pretty-print or add indentation. Do not write any other file, and do not write
outside the stage directory.

Then commit:

```bash
agentos chatlas products commit --stage-id <stage-id> --json
```

Finally return:

```bash
agentos chatlas products path --product zip-transcript-summary <selector-options>
```

## Artifact Shape

The artifact is a lower-token, turn-aligned replacement for `zip-transcript`,
and it keeps the `zip-transcript` shape exactly. Copy `class`, `schema_version`,
`view`, and `session` from the staged input unchanged:

```json
{
  "class": "agentos_chatlas.zip_transcript",
  "schema_version": 1,
  "view": "zip-transcript",
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

Commit validates the staged artifact against the staged input view. The linter
requires:

- `class`, `schema_version`, and `view` exactly match the input view
- `session` exactly matches the input `session`
- `turns` count exactly matches the input `turns`
- every turn is a JSON object
- every turn `role` exactly matches the input turn role at the same index
- every turn has string `text`
- every user turn `text` exactly matches the input turn text
- every assistant turn `text` is non-blank

Because the artifact carries the `zip-transcript` shape, its provenance lives in
the product manifest, not in the payload. Reach it through
`products path --product zip-transcript-summary`, never by reading a bare file
and assuming it is an original transcript.

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

## Freshness

Product freshness compares two fingerprints recorded at commit time:

- the input fingerprint: a hash of the current `zip-transcript` view payload
- the definition fingerprint: a hash of the fixed product definition, including
  the content of this reference

A new session turn changes the input fingerprint. An edit to this reference
changes the definition fingerprint. Either makes existing products stale, and a
stale product only reports `production_required`.

## Failure Handling

If the selector resolves zero sessions, stop with the Chatlas selector error.

If the selector resolves multiple sessions, do not guess. Ask for a narrower selector.

If staging or commit fails, report the failing command and stderr. Do not write outside the stage directory.
