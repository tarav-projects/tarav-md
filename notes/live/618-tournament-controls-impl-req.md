# Tournament Controls - Impl.Req

## Impl.Abstract

- **Goal:** implement `Tournament.Control` — consumer-supplied players carrying a declared expected standing, substituted into matches by the engine at a consumer-set rate, recorded on the verdict, and held apart in the read.
- **Status:** executed. All five slices are implemented and the full `agentos-py` suite passes at 835 tests, up from 810. Changes are uncommitted for review.
- **Source design:** `tarav-pkg/design/111-design.md` — `Tournament.Control` (`^c20260806-129u`, `-130u`, `^c20260807-0u`, `^c20260807-1u`, `^c20260806-131u`…`-135u`), plus the amended `Tournament.Hook` lines `^c20260806-127u` and `^c20260806-128u`.
- **Starting state:** the engine has no control hook, no substitution, no rate, no band on the record, and `report.py` folds every player into one list. The design landed complete; the implementation is behind on all of it.
- **Why it exists:** a null result today has three indistinguishable causes — the pool genuinely has no signal, the question is ineffective, or the judge cannot discriminate. Controls separate them. If a control declared `low` does not sink and one declared `high` does not rise, the instrument is reporting on itself, and the pool's flatness says nothing about the pool.
- **In scope:** a defaulted `controls` hook returning the control pool; a `control_rate` definition attribute; engine-side substitution before identity; `controls` on the ticket and on the verdict envelope; a separate `controls` section in the report; docs.
- **Out of scope:** any met/failed judgment on a control. `^c20260806-135u` is a reading principle, and the report already emits no ranking, score, or standing — computing "this control converged" here would be the engine diagnosing, which `^c20260806-137u` denies it. Also out: more than one control per match, a middle band, and consumer-chosen substitution — all three are settled `[DC]`/`[RJ]` lines, not open questions.

## Impl.Index

### The Control Pool Is A Hook, The Rate Is An Attribute

- `^c20260807-1u` settles the hook's return: the **pool**, not one control per call. One-per-call would put "which control appears in this match" back in the consumer, and that choice is engine work.
- The hook is **defaulted**, not required. A definition with no controls is a valid definition; `REQUIRED_HOOKS` stays `(match_players, match_identity)`.
- Return shape: a mapping of player to band, or `None`/`{}`. A dict is the natural shape for "these players, each with a declared expectation", and it makes a duplicated player impossible to express.
- The **rate** is a module-level attribute (`control_rate`), not a hook return and not a hook parameter. It follows the existing `question`/`criteria` precedent: a scalar the definition declares once. Default `0.0` — controls present but unrated substitute nothing, so turning them on is explicit.
- Bands are `high` and `low` only (`^c20260806-130u`, `^c20260807-0u`). A returned band outside that set is a hook return error, not a silently ignored one.

### Substitution Is Engine Work, And It Precedes Identity

- Order inside a match becomes: `match_players` → **substitute** → present → identity → shuffle → mint → compose → hash → spawn.
- `^c20260806-132u` is what fixes that position: identity is derived from the substituted roster, so a match carrying a control is a *different* match from the one without. Substituting after identity would silently merge two different comparisons under one id and corrupt accumulation.
- One control at most (`^c20260806-131u`). The engine draws one control and replaces one pool player, both uniformly.
- A control already among the match's players is not drawn — substituting it would produce a duplicate, which `_validated_players` already rejects, and dropping the substitution is the honest outcome rather than an error.
- Randomization is engine-side by `^c20260806-128u`: the engine randomizes presentation order **and** control substitution, and nothing else. One seeded `random.Random` drives both, so a seeded preview renders the same match every time.
- Preview substitutes too. `preview_match` exists to render *a valid match*; a preview that could never carry a control would show a frame the judge does not always get.

### Recording And Reading

- `^c20260806-133u`: the verdict records which of its players were controls and each declared band. That is a `controls` map on the engine envelope — empty when the match carried none — added to `ENVELOPE_FIELDS` so a consumer slot cannot shadow it.
- The ticket carries it forward. `submit` builds the verdict entirely from the ticket and never loads a definition, so a band that lived only in the definition would be lost between spawn and submission.
- `^c20260806-134u` is the read requirement: `report.py` gains a `controls` list and **excludes** those players from `players`. Folded in, a low control sits in the weak tail looking exactly like a finding.
- Ordinary players keep every comparison they made, including comparisons against a control. Holding controls apart is about whose *row* is read as a pool finding; discarding the comparisons would throw away the only matches that calibrate anything.
- `poi.py` needs no change and gets the right behaviour for free: it reads `report["players"]`, so a control can no longer raise `Player.LowStanding` — which is exactly right, since a `low` control losing is the instrument working.

## Impl.Agendix

- **Gate** — the `--impl --dev --AUTO Implement controls` invocation turn.
- **Touched — `tarav-pkg/design/111-design.md`**: `Tournament.Control` (`^c20260806-129u`, `-130u`, `^c20260807-0u`, `^c20260807-1u`, `^c20260806-131u`…`-135u`); `Tournament.Hook` (`^c20260806-127u`, `-128u`); `Agentos.Tournament` (`^c20260806-136u`, `-137u`).
- **Structural** — `notes/live/613-tournament-n-way-matches-impl-req.md` (arity and ordering), `614-tournament-ticket-submit-impl-req.md` (the ticket lifecycle this extends), `617-tournament-preview-system-impl-req.md` (preview).
- **Open.Space** — how a reader decides a control converged has no index home and stays out of the code.

## Execution.Plan

### Slice 1 - Bands and the control hook

- `contract.py`: `BAND_HIGH`, `BAND_LOW`, `CONTROL_BANDS`.
- `hooks.py`: `CONTROLS = "controls"` joins `DEFAULTED_HOOKS`; `TournamentDefinition.controls(...)` returns a validated `dict[str, str]`; `TournamentDefinition.control_rate` reads the module attribute and bounds it to `[0.0, 1.0]`.
- RED: prove a definition with no `controls` hook yields `{}` and rate `0.0`; prove a returned band outside `{high, low}` raises `HookReturnError`; prove an empty or non-string player raises; prove a non-mapping return raises; prove a rate outside `[0,1]` raises.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_hooks.py -q`.
- Observable: a definition can declare controls and a rate, and a malformed declaration fails at the hook boundary rather than mid-match.
- **Done** — `BAND_HIGH`/`BAND_LOW`/`CONTROL_BANDS` in `contract.py`; `CONTROLS` joins `DEFAULTED_HOOKS`; `TournamentDefinition.controls()` and `.control_rate`. 6 new tests.

### Slice 2 - Substitution before identity

- `runner.py`: one `random.Random(rng_seed)` per match drives substitution then the shuffle; `_presented_order` takes the rng instead of the seed. `_substituted(players, controls, rate, rng)` returns the roster and the controls it placed. Applied in both `run_match` and `preview_match`, before `present_player`. `MatchResult` gains `controls`.
- RED: prove rate `1.0` substitutes exactly one control; prove rate `0.0` substitutes none; prove the roster length is unchanged; prove a control already among the players is not drawn; prove `match_identity` sees the substituted roster — the same seed with and without substitution must produce different ids; prove the same seed reproduces the same match.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_runner.py -q`.
- Observable: a seeded run produces a match carrying one control, and its match id differs from the uncontrolled one.
- **Done** — `_substituted` runs first in both `run_match` and `preview_match`; one `random.Random` per match drives substitution then the shuffle; `MatchResult.controls`. 6 new tests.
- Depends on Slice 1.

### Slice 3 - Controls on the ticket and the verdict

- `tickets.py`: `Ticket.controls: dict[str, str]`, defaulted `{}` so an existing ticket file loads; threaded through `mint`, `as_dict`, `_replace`, and the payload reader.
- `model.py`: `controls` joins `ENVELOPE_FIELDS`.
- `store.py`: `append_verdict(..., controls=None)` writes it onto the envelope.
- `commands.py`: `_append_submitted` passes `ticket.controls` through, on both the ordered and the no-contest path.
- `runner.py`: `_run_row` and the preview JSON payload report `controls`.
- RED: prove a minted ticket round-trips its controls; prove a ticket file without the field loads as `{}`; prove a submitted verdict's envelope carries the band; prove a consumer slot restating `controls` raises `EnvelopeShadowedError`; prove a no-contest verdict carries them too.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_tickets.py tests/test_tournament_submit.py tests/test_tournament_store.py -q`.
- Observable: `tournament submit` records which players were controls and what each was expected to do.
- **Done** — `Ticket.controls`, `controls` in `ENVELOPE_FIELDS` and the envelope, `_append_submitted` on both paths, `controls` on run rows and the preview payload. 8 new tests.
- Depends on Slice 2.

### Slice 4 - Controls held apart in the read

- `report.py`: a player declared a control in any verdict moves to `report["controls"]` with its band beside its counts, and out of `report["players"]`. Comparisons stay as they are.
- RED: prove a control appears in `controls` and not in `players`; prove its band is reported; prove ordinary players keep the wins they earned against a control; prove a control that lost consistently raises no `Player.LowStanding`; prove a tournament with no controls reports an empty list rather than omitting the key.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_report.py -q`.
- Observable: `tournament show` reports the pool and the instrument separately.
- **Done** — `report["controls"]` carries the band beside the counts and those players leave `players`. 5 new tests.
- Depends on Slice 3.

### Slice 5 - Docs and full-suite green

- Refresh the `Tournament System` section of `agentos-py/AGENTS.md`.
- Check: `uv run pytest -q`.
- Observable: the control mechanism is documented where an implementer will find it.
- **Done** — `AGENTS.md` `Tournament System` gains four control lines and its randomization line is corrected; the `hooks.py` and `runner.py` module docstrings follow.
- Depends on Slices 1-4.

## Impl.Log

### Blockers

- None.

### Decisions in open space

- **The rate is an attribute, the pool is a hook.** The pool may need to be computed; a rate is a constant a definition declares. Making the rate a second hook return would have coupled two things that change on different schedules.
- **Rate `0.0` by default.** Declaring controls without a rate is a plausible half-finished state, and substituting nothing is the safe reading of it.
- **A control already in the match is skipped, not swapped for another.** Retrying the draw would make the substitution rate silently depend on pool overlap; skipping keeps the rate meaning what it says.
- **Comparisons against controls are kept.** `^c20260806-134u` is about the control's row being misread, not about the comparisons being invalid.

### Execution

- **Gate** — the `--impl --dev --AUTO Implement controls` turn. Git checkpoints taken in both repos before the first edit (`agentos-py` `1a79556`, `agentos-md` `f1108c3`), the `agentos-py` one capturing the still-uncommitted Impl.Req 617 work so the checkpoint records the repository exactly as found.
- **Live verification.** A throwaway depot with two pool players and two controls at `control_rate = 1.0`: `tournament preview --seed 3` substituted `c-high` for `p2`, rendered it under label `B` indistinguishably from a pool line, and the match id became `c-high VS p1`. Answering that ticket by hand put `c-high` in `report["controls"]` with `band: high, wins: 1` and left `p1` alone in `players`. No spawns were needed — the whole mechanism is reachable through preview and submit.
- **Result.** 835 tests pass, up from 810. `ruff` reports the same three pre-existing unused imports as the baseline and no new ones.
- **Uncommitted.** Implementation changes are left uncommitted for user review.

### Deviations

- **D1 — Slice 3's implementation landed inside Slice 2, ahead of its tests.** `preview_match` mints its ticket in the same breath as substituting, so `Ticket.controls` had to exist for Slice 2 to be writable at all. Slice 3's tests were then written against working code rather than red. The boundary they cover — an old ticket file loading as uncontrolled, the slot not shadowing the map — is still tested; only the ordering slipped.
- **D2 — the control pool is read per match rather than once per run.** `_substituted` calls the hook inside each match. A definition whose pool is expensive to compute pays for it every match, but the hook already sees `verdicts`, and caching it at run start would silently deny a definition the right to vary its pool as evidence accumulates. Revisit only if a real definition makes it hurt.
- **D3 — the report classifies a player as a control from any verdict that declared it.** The alternative, per-verdict classification, would put the same player in both sections of one report. The declaration is definition-level, so one verdict is enough to prove it, and a definition that reclassifies a player mid-tournament has already broken comparability in worse ways.
