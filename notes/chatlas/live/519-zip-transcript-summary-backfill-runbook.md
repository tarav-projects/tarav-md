# 519 — zip-transcript-summary Backfill Runbook

A supervisor/worker procedure for growing and refreshing the
`zip-transcript-summary` product pool.

Point an agent at this note and it can run a backfill batch without rediscovering
the selection queries, the worker prompt, or the hazards below.

**Two jobs, one procedure.**

- **Refresh** — an existing product went stale. Its `input_fingerprint` changed
  (the session gained turns) or its `definition_fingerprint` changed (the
  producer reference was edited).
- **Backfill** — a session has no product at all.

Both report `state: production_required` and both run the identical producer
loop. The only difference is how the supervisor selects targets.

## Roles

**Supervisor** — selects targets, spawns workers, verifies results, reports.
Never produces a product itself; it must not spend its context on transcripts.

**Worker** — one subagent, one or more sessions, produced strictly one at a
time. Reads the producer reference and follows it.

Use a small-to-mid model for workers. The work is bulk summarization, not
reasoning. Sonnet has run this successfully across ~1900 turns.

## Supervisor: select targets

Existing products, and which are stale:

```bash
ls "$(agentos chatlas products list --json | python3 -c 'import json,sys; print(json.load(sys.stdin)["products_root"])')/zip-transcript-summary"
agentos chatlas products status --product zip-transcript-summary --identity-hash <hash> --json
```

Candidate sessions with no product yet:

```bash
agentos chatlas query --extractable --min-user-turns 12 --idle-for 2h \
  --sort newest --limit 80 --field identity_hash --text
```

`--idle-for` matters. A session still being worked in gains turns immediately
after production and the fresh artifact goes stale for nothing. Two hours is a
reasonable floor.

Subtract the sessions that already have a product, then confirm each target
before spawning — never trust the subtraction alone:

```bash
agentos chatlas products status --product zip-transcript-summary --identity-hash <hash> --json
```

Expect `state: production_required`. Anything already `fresh` is a selection bug.

Order matters less than honesty about size. Measure before spawning, because
size decides how many sessions one worker can carry:

```bash
agentos chatlas views get --identity-hash <hash> --view zip-transcript --json
```

Sum `text` length over assistant-role turns.

Measured capacity per worker: **one large session, and only one.** A 569-turn
session with 256KB of assistant text consumed ~280K tokens and ~19 minutes, and
the worker stopped there. Plan one worker per large session. A worker can carry
several small sessions (under ~50KB assistant text) in sequence.

## Supervisor: spawn workers

**Parallel workers, one session each** — for a batch of independent sessions.
Five at once has run cleanly. This is the default.

**One sequential worker, several sessions** — when the batch is a queue and you
want a single consistent hand across it, or when you want the worker's feedback
on the reference to come from one accumulating perspective.

Never split a *single* session across workers. Compressing a turn range in
isolation is how a detail gets dropped that a much later user turn depends on,
and the staged artifact is one file that concurrent writers corrupt. This has
already happened once: a worker fanned out five subagents by index range and
lost the turn on a batch boundary.

### Worker prompt template

```text
Produce the Chatlas `zip-transcript-summary` product for exactly one session.

Read and follow this producer reference in full:
<repo>/agentos-chatlas-md/skills/tarav-chatlas-pkg/references/producer-zip-transcript-summary.md

Session selector: --identity-hash <hash>

If you use any working file in the scratchpad, prefix its name with the stage
id — several agents share one scratchpad directory.

Report back: the committed artifact path, the turn count, how many assistant
turns you filled, and every `check` refusal you hit before it passed — quote the
POI class, the message, and what you changed in response. If anything about the
reference or the tooling was confusing, missing, or made you want to write your
own helper, say so plainly.
```

For a sequential worker, list the sessions in order and add:

```text
One session at a time, fully committed, before starting the next. Do not fan out
subagents per chunk or per session. Work as far down the list as you can; when
you are running low on context, stop cleanly — do not leave a half-filled stage
— and report which you did not reach.
```

**Do not restate the producer loop in the prompt.** The reference owns it.
Restating it hides whether the reference actually works, which is the one thing
each batch is also measuring.

**Do ask for critical feedback.** Every substantive improvement to this system
came from worker reports, not from inspection.

## Supervisor: verify

Never accept a worker's self-report as the measurement. Check freshness:

```bash
agentos chatlas products status --product zip-transcript-summary --identity-hash <hash> --json
```

Then measure retention independently, comparing assistant text in the committed
artifact against the source view. The committed manifest also records it:

```bash
python3 -c "import json,pathlib,sys; print(json.loads(pathlib.Path(sys.argv[1]).read_text()).get('compression'))" \
  "$(dirname "$(agentos chatlas products path --product zip-transcript-summary --identity-hash <hash>)")/manifest.json"
```

`compression.retained_ratio` is the number that matters, but read it against the
source's average assistant turn length, not against other sessions. A very low
ratio is not automatically a win. `allow_low_compression: true` means a worker
waived the compression ceiling and `allow_aggressive_compression: true` means it
waived the collapse gates — both legitimate, both requiring a stated reason. Products committed before the compression gates existed have no
`compression` block at all; measure those against the source view directly.

## What the gates do and do not catch

`products check` and `products commit` run one linter. It guarantees structure:
turn count, order, roles, every user turn verbatim, no blank assistant turn, a
compression ceiling, no large uncompressed region, no assistant turn collapsed
to a stub, and no large crushed region.

It cannot see meaning. A summary that drops a blocker a later user turn refers
back to passes every gate. That is why the reference tells workers to read the
`user` view before compressing, and why worker feedback is part of the loop
rather than a courtesy.

The collapse gates narrow that hole from the other side but do not close it. A
replay across the 326 committed products refused 47 of them, and the sampled
refusals were unambiguous loss inside artifacts whose overall ratios looked
good — one 1742-byte status-and-open-questions block had become `"Batchy."` in a
product retaining 24% overall. Aggregate retention does not tell you whether a
specific turn survived.

Both gates skip sessions under 50 KB of source assistant text, so a small
session crushed to nothing still passes. Spot-check small products by hand.

## Known hazards

- **Shared scratchpad.** Subagents of one session share one scratchpad
  directory. Generic filenames collide across workers and one has already read
  another's file. Require a stage-id prefix.
- **A stale pool after a reference edit.** `definition_fingerprint` hashes the
  producer reference's content, so editing it invalidates every product at once.
  Expected, not a defect. Batch the reference edits, then backfill.
- **Threshold as target.** Workers land just under the compression ceiling
  rather than well below it, and stating the ceiling anchors harder than stating
  the goal beside it. One session measured 54.2% before the ceiling was written
  into the reference and 63.1% after. Watch the ratios; a ceiling is not a
  standard.
- **Compression is density-bound.** Terse, telegraphic source text cannot reach
  the ratios verbose prose reaches, and forcing it there is deletion. Judge a
  ratio against the source's average assistant turn length, not against other
  sessions.
- **`--limit` is a query-row cap, not a production cap.** Rows that are already
  fresh still consume it.
- **`run-produce` output is contaminated.** The CLI batch runner does not capture
  the spawned agent's stdout, so child output prepends to the parent `--json`
  payload. Use subagents until that is fixed.

## Related

- producer reference:
  `skills/tarav-chatlas-pkg/references/producer-zip-transcript-summary.md`
- command surface:
  `skills/tarav-chatlas-pkg/references/chatlas-commands.md`
- refusal classes: `skills/tarav-chatlas-pkg/poi/102-poi.md`
- tooling design and decisions: `agentos-chatlas-py/notes/live/552-chatlas-product-tooling-impl-req.md`
