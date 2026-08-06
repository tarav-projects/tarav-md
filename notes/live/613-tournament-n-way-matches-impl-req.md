# Tournament N-Way Matches - Impl.Req

## Impl.Abstract

- **Goal:** generalize `Agentos.Tournament` from pairwise matches with a single winner to matches over N players with a strict total ordering, following the capture of `^c20260806-47u`…`^c20260806-57u`.
- **Status:** executed. All six slices are implemented, the full `agentos-py` suite passes at 772 tests, and a 4-way tournament was verified end to end against live `claude-code` judges. Changes are uncommitted for review.
- **Source design:** `agentos-pkg/design/111-design.md` — `Agentos.Tournament`, `Tournament.Hook`, `Tournament.Match`, `Tournament.Judge`, `Tournament.Verdict`.
- **Prior implementation:** `notes/live/612-tournament-index-drift-impl-req.md` shipped the current pairwise engine. Nothing there was wrong; the design moved again.
- **Motivation:** cost. Grading 1,033 index lines at ten comparisons each is 5,165 pairwise spawns; a 4-way match fills twelve comparison-slots per spawn, cutting it to ~861, and a 10-way match to ~115. Arity becomes the knob that trades inference budget against judge discrimination.
- **In scope:** N-ary `match_players`; N-position engine framing; an ordering-valued judge contract validated against the actual arity; an envelope that records the ordering; pairwise extraction as a read-side fold in the report.
- **Out of scope:** every reading concern — how a fold should weight extracted comparisons, and any retuning of POI thresholds. Interpretation emerges from usage; the engine runs matches and stores records. Also out: adaptive tail sampling, the Index.Line tournament definition itself, and `Issue.I0001`.

## Impl.Index

### Drift Inventory

Verified against source before this plan was written:

- `hooks.py:_validated_pair` requires exactly two players; `^c20260806-48u` and `^c20260806-50u` make arity the definition's per-match choice.
- `runner.py:_POSITIONS = ("A", "B")` and `compose_verbatim` frame exactly two candidates; `^c20260806-49u` makes a match a set.
- `contract.py:VERDICT_EXPECTS` declares `outcome` as the enum `["A", "B", "no_contest"]`; `^c20260806-54u` makes it an ordering or a no-contest.
- `model.py:ENVELOPE_FIELDS` carries `preferred`, a single winner; `^c20260806-53u` records the ordering the judge returned.
- `report.py` counts wins and losses from `verdict.preferred`; `^c20260806-56u` extracts pairwise comparisons from the stored ordering at read time.

No durable records exist to migrate — `~/.agentos/tournament` is absent and every existing verdict lives in a test `tmp_path`. `No.Legacy.Allowed` applies cleanly: the `preferred` field is removed, not deprecated.

### Answer Shape

- The judge returns `outcome` as either the string `no_contest` or a **JSON array of position labels**, best first: `{"outcome": ["C", "A", "D", "B"], "attribution": "none", "reason": "..."}`.
- Positions, not players. The judge already answers by position (`^c20260806-9u`) and the engine decodes through the order it ran; an array of positions is the same contract widened.
- Validation is arity-aware: the array must be a permutation of exactly the labels presented — every label once, none missing, none invented. A repeated label is the judge placing two players at equal rank, which `^c20260806-55u` forbids, so it is a contract violation with an actionable message rather than a silently dropped comparison.
- `validate_verdict_answer` gains an arity argument. The existing cross-field no-contest rule is unchanged.
- Labels are `A`…`Z`, so arity above 26 is rejected at the hook boundary. Twenty-six candidates in one prompt is far past where judge discrimination collapses; the cap is a guard rail, not a design position.

### Record Shape

- The envelope's `preferred` becomes `ordering`: the match's players in judged order, best first, decoded from positions back to players.
- `players` keeps canonical order and `presented` keeps the order actually run, so the decode stays auditable.
- Arity is not stored: it is `len(players)`, and a second copy could only ever disagree with the first.
- A `no_contest` verdict carries `ordering: null`, exactly as it carried `preferred: null`.
- `Verdict.preferred` is replaced by `Verdict.ordering`; nothing keeps a single-winner accessor, because at N>2 "the winner" is the least interesting thing the record knows.

### Framing

- `compose_verbatim` takes N presentations and labels them `A:`…`N:` in presented order.
- The answer-contract block states the arity explicitly and names the labels the judge must order.
- Position randomization is unchanged in kind — `_presented_order` already shuffles players zipped to presentations and generalizes to N as written.
- `^c20260805-61u` still holds and gets harder: N positions offer more bias surface than two, and the defense is still statistical. Nothing to implement, but it belongs in the docs.

### Reading

- `report.py` extracts pairwise comparisons from each ordering: for positions `i < j`, `ordering[i]` beat `ordering[j]`. One 4-way match yields six comparisons; one 10-way yields forty-five.
- `matches` keeps its current meaning without change: one verdict, one increment per participating player. It already counts matches rather than comparisons, so arity does not disturb it.
- `wins` and `losses` become extracted pairwise counts and therefore grow with arity. Their sum is the player's comparison count, so nothing separate is stored.
- No weighting, discounting, or rank-distance treatment is applied, and no threshold is retuned. Reading is the consumer's concern; the record keeps the match whole (`^c20260806-57u`) so a later fold stays free. `poi.py` is untouched by this request.

## Impl.Agendix

- **Ordering gate `^c20260806-58u`** — the `/agentos-hugentics --impl --dev on the N-way change` turn orders this artifact. `Alignment.Mode::Interactive`, so the readiness checkpoint paused for the user.
- **Touched — `agentos-pkg/design/111-design.md`**: `Agentos.Tournament` (`^c20260806-47u`), `Tournament.Hook` (`^c20260806-48u`), `Tournament.Match` (`^c20260806-49u`, `-50u`, `-51u`), `Tournament.Judge` (`^c20260806-52u`, and `^c20260806-9u` for the position decode), `Tournament.Verdict` (`^c20260806-53u`, `-54u`, `-55u`, `-56u`, `-57u`, plus `^c20260805-77u` on the absence of draws).
- **Readiness approval `^c20260806-59u`** — the turn that ruled POI thresholds a reader concern and left the answer shape to implementer judgment. It authorizes execution.
- **Structural** — `notes/live/612-tournament-index-drift-impl-req.md` shipped the pairwise engine this generalizes; the derivation is the evidence.
- **Open.Space** — how a fold should weight extracted comparisons has no index home and stays unanchored by explicit user decision.

## Execution.Plan

### Slice 1 - Ordering contract

- Rewrite `contract.py`'s outcome handling: `outcome` is `no_contest` or a permutation of the presented labels, validated against arity.
- RED: prove a valid permutation passes; prove a missing label, a repeated label, an invented label, and a wrong-length array each fail with an actionable message; prove `no_contest` still validates and still requires attribution; prove a two-player match still accepts `["A", "B"]`.
- GREEN: implement `POSITION_LABELS`, arity-aware validation, and the widened `VERDICT_EXPECTS`.
- Check: `uv run pytest tests/test_tournament_contract.py -q`.
- Observable: a judge payload for any arity is accepted or rejected deterministically.
- **Done** — `contract.py` gains `POSITION_LABELS`, `MIN_ARITY`/`MAX_ARITY`, `position_labels()`, and `_validate_ordering`. `outcome` left `VERDICT_EXPECTS` entirely (see Deviation D1). 25 tests.

### Slice 2 - Ordering record

- Replace `preferred` with `ordering` in `model.py`, `store.py`, and `Verdict`.
- RED: prove an ordering round-trips; prove an ordering that is not a permutation of the match's players is rejected at the store boundary; prove `no_contest` still stores null ordering with reason and attribution; prove the slot still cannot shadow `ordering`.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_store.py -q`.
- Observable: a 4-player verdict reads back with its ordering intact.
- **Done** — `VerdictOutcome.PREFERRED` became `ORDERED`; `_require_ordering` enforces the permutation at the store boundary; `Verdict.preferred` became `Verdict.ordering`. 9 tests.
- Depends on nothing.

### Slice 3 - N-ary hook

- `_validated_pair` becomes `_validated_players`: at least two, at most twenty-six, distinct, non-empty.
- RED: prove a 4-tuple is accepted; prove a single player, a duplicate, an empty payload, and 27 players are each rejected; prove `None` still signals exhaustion; prove a definition may return different arities on successive calls.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_hooks.py -q`.
- Observable: a definition alternating 2-way and 6-way matches loads and resolves.
- **Done** — `_validated_pair` became `_validated_players`, bounded by `MIN_ARITY`/`MAX_ARITY`. A test proves arity may differ between successive calls. 18 tests.

### Slice 4 - N-position framing and decode

- Generalize `compose_verbatim` and the decode in `runner._append`.
- RED: prove a 4-way verbatim labels A–D in presented order and states the arity; prove the decode maps a returned position ordering back to players through the presented order; prove a shuffled 4-way match records an ordering over the right players; prove identity still ignores presentation order at N>2.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_runner.py -q`.
- Observable: one 4-way match runs end to end against a stub judge.
- **Done** — `compose_verbatim` labels N candidates and states the arity; `_presented_order` generalized to N; the decode maps the returned label ordering back through `presented`. 17 tests.
- Depends on Slices 1–3.

### Slice 5 - Pairwise extraction

- `report.py` extracts comparisons from orderings. `poi.py` is not touched.
- RED: prove a 4-way ordering yields six comparisons with the right winners; prove `matches` counts one per match regardless of arity; prove the no-contest distribution is unchanged; prove no ordering is emitted by the report itself.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_report.py -q`.
- Observable: `tournament show` reports a 4-way tournament's win/loss counts beside its match counts.
- **Done** — `report.py` extracts comparisons from each ordering. A test proves a 10-way match counts as one match while yielding 45 comparisons. `poi.py` untouched, as scoped. 15 tests.
- Depends on Slice 2.

### Slice 6 - Library, docs, and full-suite green

- Add an N-ary selector to `pairing.py`; refresh the `Tournament System` section of `agentos-py/AGENTS.md`.
- RED: prove a random N-subset selector returns N distinct players and is reproducible from a seed.
- GREEN: implement, then run the full `agentos-py` suite.
- Check: `uv run pytest -q` and one live `agentos tournament run` with a 4-way definition.
- Observable: a 4-way tournament runs from the terminal against a real judge.
- **Done** — `pairing.random_players` added; `AGENTS.md` `Tournament System` refreshed. Live: 3 concurrent 4-way `claude-code` matches, 0 failures, 18 comparisons from 3 spawns.
- Depends on every prior slice.

## Impl.Log

### Blockers

- None. Every line this plan implements is reviewed with a verifying tokenized approval, and `design/111-design.md` linted at 0 errors after the capture.

### Decisions in open space

- **Positions, not players, in the answer.** Keeps the existing engine-owned decode and the `^c20260806-8u` guarantee that a consumer cannot invert verdicts.
- **Arity derived, never stored.** A stored copy can only disagree with `len(players)`.
- **No migration path.** No durable records exist, and `No.Legacy.Allowed` governs.
- **Answer shape is an ordered array of labels** rather than a rank-per-label map, chosen at the readiness checkpoint: it is compact, and both shapes surface a dropped or duplicated label as a validation failure.
- **Reading stays out.** The readiness checkpoint raised POI thresholds as a fork; the user ruled it a reader concern. `matches` already counts matches by construction, so the question dissolved into no work rather than into a decision.

### Execution

- **Gates `^c20260806-58u`** (ordering) and **`^c20260806-59u`** (readiness approval). Git checkpoints were taken in `agentos-py` and `agentos-md` before the first edit.
- **Result.** 772 tests pass across the whole `agentos-py` suite, up from 750.
- **Live verification.** A definition importing `pairing.random_players` ran 3 concurrent 4-way matches against `claude-code` / `claude-sonnet-4-5-20250929`. 0 failures. Three spawns produced **18 comparisons**, and the accumulation separated cleanly: the sharpest line took 9-0, the vaguest 0-9, and the two middle lines split 5-4 — equivalence emerging from orderings that disagree across repeats, which is exactly what `^c20260806-55u` predicts.
- **Uncommitted.** Implementation changes are left uncommitted for user review.

### Deviations

- **D1 — `outcome` left the declarative schema entirely.** The plan said `VERDICT_EXPECTS` would be "widened". It could not be: the declarative markers express enums and types, not "a permutation of exactly these labels", and the label set is only known once a match is composed. `outcome` is now validated by hand in `validate_verdict_answer` and `VERDICT_EXPECTS` covers only `attribution` and `reason`. The contract is stricter than before, not looser, but the mechanism is no longer uniform across fields.
- **D2 — a docstring default was silently wrong.** `DEFAULT_QUESTION` still read "Which of the two candidates below is better?" — harmless in tests, but it would have shipped a pairwise question to any definition that declared none. Now "Rank the candidates below from best to worst."
- **D3 — one runner test asserted on a removed envelope key.** `test_a_declining_judge_records_a_no_contest_with_its_attribution` checked `envelope["preferred"] is None`; it now checks `verdict.ordering is None`. Same guarantee through the accessor rather than the raw key.
