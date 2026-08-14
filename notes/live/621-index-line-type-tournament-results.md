# 621 — Index.Line Type Tournament: First Results

Tournament `bd549216-fad7-4dcb-83d8-ad8a23ba7cb6` in the global depot.
Definition: `dev/live/620-index-line-type-tournament.py`. Fold:
`dev/live/620-index-line-type-fold.py`.

## What Was Run

30 index lines sampled stratified across the `Line.Type.Vocabulary` from
`tarav-pkg/design/*.md` (5 each DF/DC/CT/RJ/PR, 3 FR, 2 EX; no GR line in the
depot matched the length filter). Each match shows **one line under five type
codes** — its registered one plus four drawn from the rest of the vocabulary,
seeded on the line id so repeat runs accumulate against one match identity. Each
candidate carries the code's meaning inline, so the judge needs no external
lookup.

Judges: `claude-haiku-4-5-20251001` via profiles `claude-br` / `claude-jp`.
**112 verdicts, 105 ordered, 7 no-contest, all 30 lines covered.**

## The Headline

| | rate | chance |
|---|---|---|
| registered type ranked 1st | **0.581** | 0.200 |
| registered type in top 2 | **0.724** | 0.400 |

Mean rank 1.87 of 5. The index's typing carries real signal — roughly 2.9× chance
at top-1. That is the tournament's first useful output: whatever else is wrong
below, the `Line.Type` assignments are not noise.

## Per Type

| type | lines | verdicts | top-1 | mean rank |
|---|---|---|---|---|
| DF | 5 | 23 | 0.913 | 1.09 |
| RJ | 5 | 15 | 0.733 | 1.33 |
| FR | 3 | 11 | 0.636 | 1.73 |
| DC | 4 | 15 | 0.600 | 1.67 |
| CT | 5 | 17 | 0.412 | 2.24 |
| PR | 4 | 17 | 0.353 | 2.24 |
| EX | 2 | 7 | 0.000 | 4.43 |

`DF` is almost perfectly recoverable: a line that fixes what a name means reads
as one. `CT` and `PR` sit near half of `DF` — both are about *how much* a line
constrains, which is the subtler judgement, and `PR` loses to `RJ` seven times.
`GR` won 7 matches while being no line's registered type: its definition
("accounts for what an anchored evidence neighborhood grounds") appears to act as
an attractor for lines the judge cannot otherwise place.

## Two Findings Worth Acting On

**L12 is mistyped.** Registered `[EX]`, beaten by `[DF]` in 5 of 5 matches:

> a `POI.Catalog` is a `Skw.Kernel.Index` application whose `poi` chapter
> registers `POI.Class` blocks

That is a definition, not an illustration of another line's claim. This is the
type-finder working exactly as intended — one line losing consistently while its
own code wins elsewhere.

**L08 breaks the frame.** Six of the seven no-contests are one line, all with the
same complaint — *"the index line to be classified was not provided in the
prompt"*:

> standing test: the assertion rides next to the content forever; every later
> pass has a small, local, closed-set claim to check against

It opens with `standing test:`, which reads as a section header rather than line
content, so the judge concluded the line was missing. Refusals clustered on one
player indict that player, and here they do — though what they indict is the
interaction between that line's shape and the presentation, not its typing.

## What This Does Not Show

- **`[EX]`'s 0.000 is not evidence against `[EX]`.** Two lines is far too few,
  *and* the match design cannot test it: `[EX]` is defined **relationally** — it
  illustrates *another line's* claim — while the match shows the line alone. An
  `EX` line has no way to demonstrate its act in this frame. That is a defect in
  the definition, confounded with any genuine mistyping. Testing `[EX]` needs a
  presentation that carries the illustrated claim alongside the line.
- **The sample survived a filter.** Haiku complies with submit-by-command roughly
  a third of the time; the rest read the prompt and answer in prose, which the
  engine correctly records as a failed run with no verdict. ~180 spawns produced
  112 verdicts. If compliance correlates with how hard a line is to judge, the
  surviving sample is biased in a direction this run cannot measure.
- **There are no controls, so judge discrimination is unverified.** Nothing here
  separates "the judge reads the act" from "the judge pattern-matches surface
  cues" — a line beginning *"we chose X over Y"* announces `[DC]` without any
  reading. The spread between `DF` at 0.913 and `PR` at 0.353 shows the judge is
  at least not answering uniformly, but that is weaker than a control would give.

## Blocked: Controls Do Not Fit This Match Shape

`Tournament.Control` substitutes a control for one pool player before identity.
Every player here is a variant of **one line**, so a control drawn from a pool
would land among four variants of a *different* line and destroy the match's
premise. Calibration for variant-shaped matches has to come from inside
`match_players` — a deliberately absurd variant included by the definition — not
from the engine's control pool.

This is a real limit of the mechanism against a legitimate match shape, not an
oversight in this definition. It is the first candidate index line out of this
run.

## Operational Notes

- **`--provider` / `--home` cannot be used for judges.** The agent runtime rejects
  them (`provider command runtime requires --profile`) while `tournament run`
  accepts them and fails only at spawn time, recording every match as
  `judge submitted nothing (judge exit 1)`. `agentos-py/AGENTS.md` describes
  `--home` as required when running without `--profile`, which is backwards.
- **Account limits masquerade as judge failure.** A drained account produces the
  same `judge submitted nothing` row as a non-compliant judge. `agentos agent run
  --profile X --prompt ping` distinguishes them in one call and is worth running
  before diagnosing anything else.
- **`--agent-arg=--allowedTools --agent-arg=Bash` was investigated and cleared.**
  An apparent effect was an artifact of account capacity draining underneath the
  comparison; re-tested on a healthy account it changed nothing that survives the
  noise. The `AGENTS.md` guidance stands.

## Next

- raise `--budget` for depth on `CT` / `PR`, where the rates are least settled
- redesign the `[EX]` presentation to carry the illustrated claim, or drop `[EX]`
  from the pool and say so
- add an in-definition absurd variant as a `low` calibrator, since the engine's
  controls cannot serve this shape
- fix L12's type and re-run it
