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

If `state` is `production_required`, run the four-step producer loop below. Do
not write your own structural or verification script — every mechanical step
has a command, and those commands are the same code the commit gate runs.

### 1. Stage

```bash
agentos chatlas products produce --product zip-transcript-summary <selector-options> --json
```

This returns `stage.stage_id`, `stage.input_path`, and `stage.output_path`.

It also returns a `prompt` field. That is a handoff prompt for delegating the
production to a separate agent; ignore it when you are producing the artifact
yourself. It restates this reference and is not a second entry point.

### 2. Scaffold

```bash
agentos chatlas products scaffold --stage-id <stage-id> --json
```

This writes `stage.output_path` for you, already carrying everything you must
not invent: `class`, `schema_version`, `view`, the `session` object, the exact
turn count and order, every `role`, and every user turn copied verbatim. Only
assistant `text` is left empty, and `assistant_turns_to_fill` reports how many.

Never rebuild this skeleton by hand. Copying user turns yourself is the single
largest source of production failures.

### 3. Fill

Read `stage.input_path` for the source assistant text, then edit only the
assistant `text` fields in `stage.output_path`. Keep it compact JSON. Do not
reorder, add, or remove turns. Do not touch user turns.

Compress by content, not to a number: remove everything that does not change
state, and keep everything a later turn depends on. See `Compression Rules` for
what that means and for how far to expect the text to fall.

You may write a script to apply the fill. Authoring summary text programmatically
is not the same as building structure by hand. The rule is narrow:

- the script **mutates** `stage.output_path` in place, setting only `text` on
  assistant-role turns
- it never regenerates the artifact from `stage.input_path`, and never writes
  `class`, `schema_version`, `view`, `session`, roles, turn order, or user text —
  the scaffold owns all of that
- it addresses turns by their index in the scaffolded file, so a dropped or
  shifted index is impossible

Keep working files out of the stage directory. Several producers may share one
scratchpad, so prefix any working filename with the stage id.

### 4. Check, then commit

```bash
agentos chatlas products check --stage-id <stage-id> --json
```

`check` runs the full commit linter without committing. It exits `0` with
`check.ok: true` when the artifact is publishable. Otherwise it exits `1` and
returns `check.finding` — a POI naming the exact invariant and, where relevant,
the offending `turn_index`. Fix and re-run `check` until it passes.

Then commit:

```bash
agentos chatlas products commit --stage-id <stage-id> --json
```

## Large Sessions

Sessions above roughly 300 turns cannot be filled in one pass. Work them in
chunks, and let the tooling track coverage instead of trusting your own bookkeeping.

**First, consider reading the user turns alone.**

```bash
agentos chatlas views get --identity-hash <hash> --view user --json
```

They are verbatim and they are what later turns refer back to, so reading them
first can tell you which assistant content must survive before you start cutting.

The value of this step is workload-dependent, so judge it rather than doing it
by default. It pays in support, debugging, and question-and-answer sessions,
where user turns carry the substance. It pays much less in iterative design or
approval sessions, where the user turns are mostly short acknowledgements and
approval tokens carrying no context on their own — there it can be a large read
for very little signal. Sample it before committing to the whole thing.

**Then fill in chunks of about 40–60 turns.** Size chunks by turn count, not by
byte budget: a chunk sized to ~50KB of assistant text can be well over 100KB of
raw JSON view payload, which will silently truncate mid-read and force a
paginated recovery. Fewer turns per chunk is the cheaper mistake.

Slice the input by turn range rather than re-reading the whole payload:

```bash
agentos chatlas views get --identity-hash <hash> --view zip-transcript --range=120:180 --json
```

The response echoes `range.start` and `range.total`, so mapping a chunk back to
global turn indices needs no bookkeeping of your own.

`--range` is supported only on the `zip-transcript` view, and a negative spec
needs the `=` form or it parses as a flag.

**Between chunks, let `check` tell you what is left.**

```bash
agentos chatlas products check --stage-id <stage-id> --json
```

While any assistant turn is still empty it refuses with
`Turn.AssistantTextBlank` and returns **every** remaining index in
`evidence.blank_turn_indices`. That is your coverage diff — it is authoritative,
and it is cheaper and more reliable than reconciling chunk boundaries yourself.
Chunk boundaries are where turns get dropped; do not verify them by hand.

Do not fan out one agent per chunk. Compressing a range in isolation is exactly
how cross-references between distant turns get lost, and the artifact is a single
staged file that concurrent writers will corrupt.

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

`products check` and `products commit` run the same linter against the staged
artifact and the staged input view. The linter requires:

- `class`, `schema_version`, and `view` exactly match the input view
- `session` exactly matches the input `session`
- `turns` count exactly matches the input `turns`
- every turn is a JSON object
- every turn `role` exactly matches the input turn role at the same index
- every turn has string `text`
- every user turn `text` exactly matches the input turn text
- every assistant turn `text` is non-blank — the refusal lists every remaining
  blank index at once, so a partial fill can resume from it
- assistant text retains at most 70% of the source, once the source is large
  enough for compression to be meaningful
- no material share of the transcript is left essentially uncompressed while
  other regions carry the reduction
- no substantial assistant turn is reduced to a stub — the refusal names each
  collapsed turn with its source and summary sizes
- no material share of the transcript is reduced to almost nothing

Because the artifact carries the `zip-transcript` shape, its provenance lives in
the product manifest, not in the payload. Reach it through
`products path --product zip-transcript-summary`, never by reading a bare file
and assuming it is an original transcript.

## Compression Rules

Always preserve turn order and turn alignment.

**Compress by content, not to a ratio.** The test for each assistant turn is
whether what you removed changed the transcript's state or is referenced later.
If it did not, remove it; if it did, keep it. A ratio falls out of that work —
it is not the work.

How far the text falls depends on how dense the source already is. Measure the
average assistant turn length before you start, and calibrate:

- **verbose sources** (averaging over ~1500 characters per assistant turn):
  prose with restated context, narrated plans, and repeated framing. Expect to
  land near 25–40%.
- **mid-density sources** (~600–1500 characters): expect 40–60%.
- **terse sources** (under ~600 characters, or telegraphic output-style turns):
  already close to signal. Expect 55–70%, and do not force it lower — cutting
  dense text past its content is deletion, not compression.

Compress every region. A summary that crushes a few huge turns and leaves whole
stretches untouched is refused even when the overall ratio passes.

**Summarize; do not stub.** The gates cut both ways, because over-retention
leaves a fat but faithful artifact while over-compression leaves a wrong one
that no reader can detect. A substantial assistant turn reduced to `"Yes."` or
`"Batchy."` is refused however good the overall ratio looks — and both of those
are real examples pulled from committed artifacts. If a turn resolved a
question, name what it resolved.

Never truncate text to reach a ratio. If a session genuinely cannot compress
further, commit with `--allow-low-compression` and say why.

Never pad text to escape a collapse refusal. The repair is to re-read that turn
in the staged input and restore what a later turn depends on — writing filler to
clear the gate is worse than the loss it was meant to prevent. If the turn
genuinely carried nothing, commit with `--allow-aggressive-compression` and say
why. The two waivers assert opposite things and are not interchangeable.

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

If `check` keeps refusing the same invariant, re-run `scaffold --force` to reset
the artifact to a known-good skeleton and fill it again. Never hand-repair
structure the scaffold owns.

If `check` refuses on compression, it names the longest assistant turns or the
offending turn ranges. Resummarize those and re-run `check`; work down the list
across passes rather than trying to clear it in one edit.

If `check` refuses on collapse, it names each turn with its source and summary
byte sizes. Re-read those turns in `stage.input_path` and rewrite them from the
source. Do not write toward a byte count.
