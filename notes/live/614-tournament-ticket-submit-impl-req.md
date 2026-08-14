# Tournament Ticket And Submit - Impl.Req

## Impl.Abstract

- **Goal:** move the judge's answer off stdout and onto a validating CLI, authorized by a per-run ticket, and remove the refusal-attribution enum. Follows the capture of `^c20260806-60u`…`^c20260806-71u`.
- **Status:** executed. All six slices are implemented, the full `agentos-py` suite passes at 795 tests, and live `claude-code` judges answered by command on the first attempt. Changes are uncommitted for review.
- **Source design:** `tarav-pkg/design/111-design.md` — `Tournament.Judge`, `Tournament.Ticket` (new), `Tournament.Depot`, `Tournament.Verdict::No.Contest`.
- **Prior implementation:** `notes/live/613-*.md` shipped N-way matches with ordering outcomes; `notes/live/612-*.md` shipped the depot and hook surface. This request reverses one decision recorded in 610's `Impl.Log` — "judge output parsed from captured stdout" — which that note already flagged as provisional with a written-artifact fallback as the known escape hatch.
- **Motivation:** a malformed answer currently burns the whole spawn and surfaces to an orchestrator. 610 declared the goal that "a contract violation is agent-facing and actionable in the iterante style"; stdout parsing cannot deliver that, because nothing reaches the judge. A submit command puts the error in front of the agent that made it, in the context that can still fix it.
- **In scope:** the `tickets/` staging area and its lifecycle; `agentos tournament submit`; the runner minting a ticket and resolving by it instead of parsing stdout; the engine frame carrying the submit instruction; removal of `attribution` from the contract, the envelope, and the report; age-based GC at run start and `agentos tournament gc`.
- **Out of scope:** cross-run judge-failure analytics; any change to how verdicts are read or folded; the Index.Line tournament definition; `Issue.I0001`.

## Impl.Index

### Drift Inventory

Verified against source before this plan was written:

- `contract.py` declares `ATTRIBUTIONS` and requires `attribution` on every answer; `^c20260806-61u` rejects asking the judge to attribute at all. 29 references across five modules.
- `model.py:ENVELOPE_FIELDS` carries `no_contest_attribution`; `^c20260806-60u` leaves only a plain stated reason.
- `report.py` builds an `attributions` map and `reason_samples` keyed on it; the distribution read now comes from which players were in which refused match.
- `runner.py` parses `run_result.stdout`; `^c20260806-62u` makes submission a command.
- No ticket concept exists anywhere; `^c20260806-64u`…`-68u` and `^c20260806-69u`…`-71u` are entirely new.

### Ticket Lifecycle

- A ticket is one JSON file at `<depot>/tickets/<ticket-id>.json`. Plain filesystem, not Bloberia: it is mutable staging, and keeping it out of the record store is what leaves append-only untouched (`^c20260806-68u`).
- Minted **before** the spawn, carrying everything the verdict needs except the outcome: tournament id, match id, players in canonical order, presented order, verbatim hash, judge identity, created-at, attempt count, attempt cap.
- One file per ticket means one writer per file. No depot-wide lock is taken on the pending side; Bloberia's lock is still taken once, at submit.
- Redemption marks the ticket rather than deleting it. `^c20260806-70u` says tickets are swept by age *rather than on completion*, so the file survives its own redemption and the attempt history stays inspectable until GC.
- The ticket id is uuid4. It is a local capability: any process that can read `tickets/` can submit. That is the same trust boundary as the depot itself and is not tightened here.

### Submit Command

- `agentos tournament submit --ticket <id> --ranking A,C,B,D`
- `agentos tournament submit --ticket <id> --no-contest --refusal-reason "..."`
- Comma-separated labels rather than JSON: an agent typing a shell command should not have to survive nested quoting, and the labels are already a closed alphabet.
- The submission carries **only** the outcome. Players, order, arity, and hash all resolve from the ticket, so a confused judge cannot name a match it was not given (`^c20260806-66u`).
- Validation is the existing `validate_verdict_answer`, with arity taken from the ticket. A rejection exits nonzero with the actionable message and increments the ticket's attempt count.
- Past the cap, the command refuses without validating and says so. Default cap 3.
- A second submission against a redeemed ticket is refused. Repeat runs of one match get distinct tickets, so nothing legitimate needs it.

### Runner Changes

- Order becomes: present → identity → shuffle → compose → hash → **mint ticket** → spawn → **resolve by ticket**.
- The engine frame gains the submit instruction with the ticket id and the resolved depot pre-filled, so the judge copies a formed command rather than assembling one. Same argument as the position labels: instructions the consumer could get wrong stay engine-owned.
- `stdout` stops being read. The exit code stops being the primary signal — the question becomes whether the ticket was redeemed.
- The verdict envelope gains `ticket`, which is also how the runner finds the verdict its spawn produced. `match_id` cannot serve, because repeat runs share it.

### Attribution Removal

- `ATTRIBUTIONS` and the `attribution` field leave `contract.py`. A decided answer is the ranking alone; a refusal carries `refusal_reason`.
- `no_contest_attribution` leaves the envelope and `store.append_verdict`; `no_contest_reason` stays and stays required on a refusal.
- `report.py` drops `attributions` and re-keys `reason_samples` off the refused match rather than off an axis the judge supplied.
- The engine frame loses the attribution sentence, which is the largest single reduction in the prompt.

### Garbage Collection

- `run` sweeps once before minting: one `listdir`, remove tickets older than the horizon.
- Horizon is one week. `^c20260806-71u` requires only that it be far longer than any match can run; a week makes the race structurally impossible and removes any need for per-ticket deadlines.
- `agentos tournament gc [--depot]` exposes the same sweep explicitly, following the `agentos chatlas gc` precedent.

## Impl.Agendix

- **Ordering gate `^c20260806-72u`** — the `--impl --dev` turn ordering this artifact.
- **Readiness approval `^c20260806-73u`** — the turn delegating both open checkpoint decisions to the implementer and switching the run to `Alignment.Mode::Autonomous`. It authorizes execution.
- **Touched — `tarav-pkg/design/111-design.md`**: `Tournament.Judge` (`^c20260806-62u`, `-63u`), `Tournament.Ticket` (`^c20260806-64u`…`-68u`), `Tournament.Depot` (`^c20260806-69u`…`-71u`), `Tournament.Verdict::No.Contest` (`^c20260806-60u`, `-61u`, and `^c20260805-83u` for the distribution read).
- **Structural** — `notes/live/613-*.md` and `notes/live/612-*.md` are the implementations this extends.
- **Open.Space** — cross-run judge-failure analytics has no index home and stays unanchored.

## Execution.Plan

### Slice 1 - Ticket store

- Add `tickets.py`: mint, load, record attempt, mark redeemed, sweep by age.
- RED: prove a minted ticket round-trips its match context; prove attempts increment and the cap is enforced; prove a redeemed ticket refuses a second submission; prove sweep removes tickets past the horizon and leaves fresher ones; prove sweep on an absent directory is a no-op.
- GREEN: implement over plain JSON files.
- Check: `uv run pytest tests/test_tournament_tickets.py -q`.
- Observable: a ticket file appears under `<depot>/tickets/` and survives redemption.
- **Done** — `tickets.py`: `mint`, `load`, `set_verbatim_hash`, `set_slot`, `record_attempt`, `redeem`, `sweep`. Two setters beyond plan (see Deviation D1). 12 tests.

### Slice 2 - Attribution removal

- Strip `attribution` from `contract.py`, `model.py`, `store.py`, `report.py`, and the frame.
- RED: prove a decided answer needs only its ranking; prove a refusal requires `refusal_reason`; prove the report no longer emits `attributions` and still counts refusals per player and pool-wide.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_contract.py tests/test_tournament_report.py -q`.
- Observable: the rendered frame drops the attribution sentence.
- **Done** — `ATTRIBUTIONS` gone; `VERDICT_EXPECTS` replaced by `REFUSAL_REASON_FIELD`; envelope swaps `no_contest_attribution` for `refusal_reason` and `ticket`; `report.py` keys `reason_samples` by match.
- Depends on nothing.

### Slice 3 - Submit command

- Add `agentos tournament submit`, validating against its ticket and appending the verdict.
- RED: prove a valid ranking appends exactly one verdict carrying the ticket; prove an invalid ranking exits nonzero, appends nothing, and increments attempts; prove the cap refuses; prove a redeemed ticket refuses; prove a no-contest submission requires a reason; prove the submission cannot name players.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_submit.py -q`.
- Observable: `agentos tournament submit --ticket ... --ranking B,A` records a verdict by hand.
- **Done** — `_cmd_submit` plus `_submitted_answer` and `_append_submitted`. 11 tests in `tests/test_tournament_submit.py`, including that the parser exposes no way to name players.
- Depends on Slices 1-2.

### Slice 4 - Runner resolves by ticket

- Mint before the spawn, render the submit instruction into the frame, stop reading stdout, resolve the verdict by ticket.
- RED: prove the frame carries the ticket id and a runnable command; prove a spawn that submits produces a verdict; prove a spawn that exits without submitting produces none and lands in `failures[]`; prove `--dry-run` mints no ticket.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_runner.py -q`.
- Observable: one match completes end to end against a stub judge that shells out.
- **Done** — `run_match` mints, renders the command, spawns, and resolves via `_verdict_for_ticket`. `_append` deleted from the runner; the stub judge now submits through the real CLI handler. `JudgeSpawn.agent_argv` added (Deviation D2).
- Depends on Slice 3.

### Slice 5 - Garbage collection

- Sweep at run start; add `agentos tournament gc`.
- RED: prove a run sweeps before minting; prove `gc` reports what it removed; prove a fresh ticket survives both.
- GREEN: implement.
- Check: `uv run pytest tests/test_tournament_commands.py -q`.
- Observable: `agentos tournament gc` prints a count.
- **Done** — `run` sweeps before minting; `agentos tournament gc` added.
- Depends on Slice 1.

### Slice 6 - Docs and full-suite green

- Refresh `agentos-py/AGENTS.md`; run the full suite; one live run.
- Check: `uv run pytest -q` and a live `agentos tournament run` with a real judge submitting through the CLI.
- Observable: a real judge answers by command, and a deliberately malformed first attempt is corrected in-context.
- **Done** — `AGENTS.md` refreshed. Live: 2 concurrent 3-way matches, both judges submitted successfully on their first attempt (0 recorded attempts, both tickets redeemed). The in-context correction path was exercised by the unit suite rather than live, since no live judge produced a malformed ranking.
- Depends on every prior slice.

## Impl.Log

### Blockers

- None. Every line is reviewed with a verifying tokenized approval and `design/111-design.md` linted at 0 errors after the capture.

### Decisions in open space

- **Comma-separated labels over JSON on the command line.** Fewer quoting failure modes for an agent composing a shell command.
- **The engine renders the whole submit command, depot included.** A judge assembling its own invocation is a consumer-shaped error the frame can simply prevent.
- **Redemption marks rather than deletes.** Required by `^c20260806-70u`, and it keeps the attempt history readable until GC.
- **The envelope gains `ticket`.** `match_id` cannot identify which run produced a verdict, because repeat runs of one match share it deliberately.
- **A validated verdict outranks a nonzero exit** (resolved at readiness, `^c20260806-73u`). Once the answer travels out of band the exit code stops being evidence that anything failed; it is recorded on the ticket rather than used as a gate. The cost is that `failures[]` no longer catches a judge misbehaving *after* it answered — acceptable, because the thing that run existed to produce is durable and valid.
- **Only contract rejections count against the cap** (same gate). Those are the ones a retry can fix. A submission against a redeemed ticket, or one past the cap, is refused without incrementing, so a confused judge cannot exhaust a counter that no longer protects anything.

### Execution

- **Gates `^c20260806-72u`** (ordering) and **`^c20260806-73u`** (readiness approval, which also switched the run to `Autonomous`). Git checkpoints taken in `agentos-py` and `agentos-md` before the first edit.
- **Result.** 795 tests pass, up from 772.
- **Live verification.** Two concurrent 3-way matches against `claude-code` / `claude-sonnet-4-5-20250929`. Both judges ran the submitted command and were redeemed on the first attempt; the depot shows `definitions/`, `records/`, and `tickets/` side by side. Six comparisons from two spawns, and the vague line took 0-2.
- **Uncommitted.** Implementation changes are left uncommitted for user review.

### Deviations

- **D1 — a ticket needs two post-mint setters the plan did not anticipate.** The frame embeds the ticket id, so the verbatim cannot exist before the ticket does, and therefore neither can its hash — `set_verbatim_hash` fills it in afterwards. Separately, `submit` runs in a process with no `TournamentDefinition`, so it cannot call `verdict_slot`; the runner computes the slot before the spawn and `set_slot` carries it on the ticket. Both are ordinary mutable staging, so neither strains the design, but the plan described the ticket as written once.
- **D2 — the live run failed, and the cause was not in the design.** Both judges exited 0 having submitted nothing, with zero recorded attempts: they never ran the command at all. `claude-code` in non-interactive mode declines tool use without an explicit grant, and cannot prompt for one. Confirmed by hand — the same command succeeded immediately with `--allowedTools Bash`. `JudgeSpawn.agent_argv` and `tournament run --agent-arg` now pass provider flags through, keeping the engine provider-neutral rather than teaching it claude-code's permission model. **Nothing in the index anticipates this**: `^c20260806-62u` says a judge submits through a command and says nothing about the judge being *able* to. Worth a line if it recurs on another provider.
- **D3 — `--agent-arg --allowedTools` does not work; `--agent-arg=--allowedTools` does.** argparse's `append` action swallows a following token that begins with `--`. Documented in the flag's help text and in `AGENTS.md` rather than worked around, since the `=` form is standard.
- **D4 — `MatchResult` lost and regained its `match_id` field mid-edit.** A field-reordering edit dropped it; the runner tests caught it immediately. Recorded only because it briefly made every runner test fail for a reason unrelated to the slice.
