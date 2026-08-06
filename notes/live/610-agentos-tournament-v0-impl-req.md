# Agentos Tournament v0 - Impl.Req

## Impl.Abstract

- **Goal:** implement the first runnable cut of `Agentos.Tournament` — a domain-blind comparative-evaluation engine that renders player pairs through consumer hooks, spawns one judge agent per match, and accumulates verdict records.
- **Status:** executed. All seven slices are implemented, `agentos tournament` is registered in `agentos-cli`, 66 tournament tests and the full `agentos-py` suite (705 tests) pass, and the engine was verified end to end against live `claude-code` judges. Changes are uncommitted for review.
- **Source design:** the `Agentos.Tournament` block family in `agentos-pkg/design/111-design.md` (landed; eight blocks, 66 grounded lines), grounded on `Accountable.Assertion` (`agentos-pkg/design/107-design.md` is the POI family; `design/106-design.md` owns `Accountable.Assertion`, `Producer.Aids.Checker`, `Program.Hardness`), `Agentos.Bloberia` (`design/109-design.md`), and `POI.System` (`design/107-design.md`).
- **Borrowed implementations:** `agentos-iterante-py` (`src/iterante/ctx.py`, `contract.py`, `locking.py`, `state.py`) for hook plumbing; `agentos-chatlas-py/src/agentos_chatlas/products.py:418` (`chatlas_products_run_produce`) for the agent fan-out shape; `agentos.agent.run_runtime` for the spawn.
- **In scope:** the record model and its Bloberia-backed store, consumer hook loading with per-tournament code snapshot, hook-purity enforcement, judge-output contract validation, single-match execution through `agentos.agent`, a `agentos tournament` CLI with concurrent fan-out, a default pair sampler with hook override, and raw accumulation reporting.
- **Out of scope:** any ranking or scoring model (`Standing` is parked by explicit user decision — see Deviation D1), cross-tournament aggregation, adaptive/uncertainty-driven sampling beyond a declared seam, POI classes for domain findings, a judge-consistency analysis surface, and any consumer of the engine (the index-line use case is a later `Impl.Req`).

## Impl.Index

### Placement And Boundary

- `agentos.tournament` is a subsystem of the `agentos-py` foundation library, placed beside `agentos.bloberia` and `agentos.wayfinder` — the existing precedent for general substrates that other packages consume.
- Module layout mirrors `agentos/wayfinder/`: `model.py`, `store.py`, `hooks.py`, `contract.py`, `runner.py`, `commands.py`, `poi.py`.
- `agentos-cli` registers `register_tournament_commands` alongside the existing registrars in `agentos-cli/src/*/cli.py`.
- The engine never imports a consumer and never interprets a player payload; domain meaning enters only through consumer hooks and leaves only through stored records.

### Record Model

- A `Tournament` is a definition reference plus its accumulated verdict records over one player pool.
- A `Tournament.Verdict` record has two zones, mirroring the `Bloberia.Record` split one level down: an engine-written envelope and an opaque consumer slot.
- Both zones live inside Bloberia's application-owned `value`. Bloberia's own reserved envelope is `id`/`created_at`/`updated_at`/`revision` and cannot hold engine fields, so the engine envelope is a named subobject of `value`, not Bloberia's envelope.
- Envelope fields: tournament id, consumer-supplied match id, judge identity (provider/model/account), outcome, presentation order actually run, `Match.Verbatim` hash, timing, run status.
- `BloberiaDepot.create` assigns a uuid4 record id; the consumer's match id is an envelope field reached by `query` subset match, never the Bloberia record id.
- The consumer slot is JSON the engine stores and never reads.
- Records are append-only; a later verdict never replaces an earlier one.
- Append-only is a Tournament-layer rule, not a Bloberia guarantee: `BloberiaDepot.edit` exists and mutates in place, so `store.py` enforces the rule by never calling it.
- The engine writes nothing into the consumer slot and reads nothing from it; envelope fields are never shadowed by slot content.

### Identity

- Match identity is a consumer-supplied opaque string, required by the engine and never computed by it.
- The engine enforces presence, not meaning: a missing id is a hard error rather than a generated default, because a generated default silently produces the never-accumulates failure.
- The default identity hook supplies a hash of the rendering, so a zero-hook tournament is strict by default while an overriding consumer may declare looser identity.
- The `Match.Verbatim` hash is cheap evidence of what actually ran and is not an identity: it varies per run because presentation order is randomized.

### Hook Surface

- A tournament is defined by a Python file exposing named functions; every hook has a working default so a zero-hook tournament runs end to end.
- Hooks are pure: they compute and return values (a string, a prompt, a dict). They never spawn, store, or randomize.
- Declared hooks for v0: render a match prompt from a player pair, supply a match identity, contribute the consumer verdict slot, and select the next pairs.
- Hooks receive one data-only context object carrying read-only zones and returning through an explicit output value — the `iterante.ctx.Ctx` shape, minus the turn state it exists to carry.
- The engine validates every hook return before acting on it, mirroring the post-hook validation in `iterante/harness.py`.

### Hook Snapshot And Purity

- The tournament's hook file is snapshotted at tournament creation and every match executes the snapshot, never the live file — adapted from `iterante/state.py:create_run`.
- Provenance records the origin path so a tournament stays self-describing.
- Snapshotting is load-bearing here rather than convenient: a hook edited mid-tournament silently makes later verdicts incomparable with earlier ones.
- `File.Locking` (`iterante/locking.py`) verifies the snapshot and store files after each hook call, so hook purity is mechanically enforced rather than trusted.

### Judge Execution

- One match is one judge run in one fresh context, carrying no state from any other match.
- The spawn is `resolve_agent(provider, profile, start_path)` then `agent.run(AgentCommandConfig(prompt=match_verbatim, model=..., account=..., interaction_mode="non_interactive"), AgentRunConfig(cwd=..., process_mode="capture", timeout_sec=...))`.
- `process_mode` must be `"capture"`, not the `"terminal"` used by `chatlas products`: `_run_terminal` calls `_run_subprocess(capture=False)` and returns `ProcessResult(exit_code=...)` with `stdout=None`. Products only ever reads `exit_code` because its agent writes an artifact file; a tournament reads the judge's answer, so it needs the captured stream.
- Judge account is bound by the tournament definition; a tournament is many spawns and quota selection is a definition-level decision.
- Presentation order is randomized by the engine per run as default normalization, and the order run is recorded.
- A judge that completes but declines produces a `No.Contest` verdict with a stated reason; a spawn that fails, times out, or exits nonzero produces no verdict record at all.

### Verdict Contract

- Judge output is validated at the boundary against a declarative `expects` schema, adapted from `iterante/contract.py` (JSON-safe type markers, enum-as-list, nested objects, dependency-free).
- The v0 outcome schema is an enum over the two players plus `no_contest`, with a required reason field on `no_contest`.
- Validation is mandatory. Iterante's opt-in `if "expects" in call` leniency is deliberately not carried over: verdicts are the entire product of this system.
- A contract violation is agent-facing and actionable in the iterante style, so an orchestrator can re-run the match with a corrective message.

### Fan-Out And CLI

- `agentos tournament run` mirrors `chatlas_products_run_produce`: a `--concurrency` parameter over a `ThreadPoolExecutor`, degrading to a plain serial loop at 1.
- Failures are collected as data rather than raised: a failed match becomes a result row, and the command returns a structured envelope with `status`, `run_count`, `failed_count`, `failures[]`, `runs[]`.
- Results stay in input order regardless of completion order.
- `--dry-run` returns the rendered `Match.Verbatim` and the resolved agent argv without spawning.
- The failure envelope is the orchestration primitive: an agent re-invokes with the failed subset rather than the engine implementing retry policy.
- Products' skip-when-fresh default is deliberately inverted — repeat runs of one match are the feature, so `run` executes what it is asked for and does not skip on prior success.
- Per-match locking is not carried over from products: verdicts are append-only, so concurrent runs of the same match are not contention.
- Bloberia still serializes the writes: `create` takes an exclusive depot lock and `query` scans every record. Judge spawns dominate wall time at v0 volume, so this is acceptable; it is the first thing to revisit if a pool grows large.

### Reporting

- v0 reporting exposes raw accumulation only: per-player win/loss counts, per-player match counts, and the `No.Contest` distribution across the pool and per player.
- No ranking, score, or ordering is computed — `Standing` is parked, and committing a fold now would prejudge it.
- Match count is surfaced beside every count so a consumer can filter by confidence rather than reading an under-played player as a finding.
- `No.Contest` concentration is reported both ways, since scattered refusals indict the definition and clustered refusals indict a player.

### POI Boundary

- The engine emits `POI.Instance`s about tournament dynamics only, never about domain semantics.
- Its `POI.Class` identities are engine-owned: low standing, unjudgeable player, incoherent definition.
- Consumers read accumulated records and mint their own domain POIs; the engine never learns what a player represents.
- v0 registers the class identities and emits instances; authoring the `POI.Catalog` documentation blocks is out of scope.

## Execution.Plan

Every slice below is **done**. Execution order deviated from written order once (see Deviation D4). Landed files: `agentos-py/src/agentos/tournament/{__init__,model,store,hooks,locking,contract,runner,sampling,report,poi,commands}.py`, `agentos-py/tests/test_tournament_{store,hooks,contract,runner,commands,sampling,report}.py`, and the registrar line in `agentos-cli/src/agentos_cli/cli.py`.

### Slice 1 - Record model and store

- Add `model.py` (envelope/slot record types, tournament and verdict shapes) and `store.py` over `agentos.bloberia`.
- RED: prove envelope/slot separation, append-only behavior, required match id rejection on absence, and that slot content cannot shadow an envelope field.
- GREEN: minimal importable model and Bloberia-backed store.
- Check: `uv run pytest tests/test_tournament_store.py -q`.
- Observable: a tournament can be created and verdicts appended and read back, with no agent involved.
- **Done** — `model.py` + `store.py`, 7 tests. `store.py` exposes only `create_tournament`, `tournament`, `tournaments`, `append_verdict`, `verdicts`; the absence of any edit path is asserted by test. Verdict timestamps keep microseconds (`iso_z(..., drop_micros=False)`) because repeat matches within one second would otherwise order by random uuid4.

### Slice 2 - Hook loading, snapshot, and purity

- Add `hooks.py`: load a tournament definition file, snapshot it at creation, execute the snapshot, validate hook returns, and verify `File.Locking` after each call.
- Port `locking.py` from iterante as a generic dependency-free module.
- RED: prove the snapshot is executed rather than the live file after the origin is edited; prove a hook writing to a store file raises a lock violation; prove an invalid hook return is rejected at the boundary.
- GREEN: implement loader, snapshot, and post-hook verification.
- Check: `uv run pytest tests/test_tournament_hooks.py -q`.
- Observable: hooks run and are constrained, still with no agent involved.
- **Done** — `hooks.py` + `locking.py`, 11 tests. Four hooks land: `render_match`, `match_identity`, `verdict_slot`, `select_pairs`. `open_definition` was added beyond plan (see Deviation D6).

### Slice 3 - Verdict contract

- Add `contract.py` adapted from `iterante/contract.py`, plus the v0 outcome schema.
- RED: prove enum outcomes validate, an unknown outcome is rejected, `no_contest` without a reason is rejected, and the error message is actionable.
- GREEN: implement the validator and schema.
- Check: `uv run pytest tests/test_tournament_contract.py -q`.
- Observable: a judge payload can be accepted or rejected deterministically.
- **Done** — `contract.py`, 15 tests. The schema carries an `attribution` enum beyond the written plan (see Deviation D5) and a cross-field rule in `validate_verdict_answer`.

### Slice 4 - Single match run

- Add `runner.py`: render through hooks, randomize order, hash the verbatim, spawn one judge, validate, append the verdict.
- RED: prove a completed run appends exactly one verdict with the recorded order and verbatim hash; prove a nonzero exit or timeout appends no record; prove a declining judge appends a `No.Contest` with its reason.
- GREEN: implement single-match execution against a stubbed agent boundary.
- Check: `uv run pytest tests/test_tournament_runner.py -q`.
- Observable: one real match runs end to end against a live provider by hand.
- **Done** — `runner.py`, 9 tests. `process_mode="capture"` as planned; the pre-execution reading of `_run_terminal` was correct and saved the slice.

### Slice 5 - CLI and fan-out

- Add `commands.py` (`create`, `run`, `list`, `show`) and register in `agentos-cli`.
- Implement `run` with `--concurrency`, `--dry-run`, and the failure envelope.
- RED: prove input-order results under concurrency, a failed row landing in `failures[]` without aborting siblings, and `--dry-run` producing prompt and argv with no spawn.
- GREEN: implement the command surface.
- Check: `uv run pytest tests/test_tournament_commands.py -q` and `agentos tournament run --dry-run ...`.
- Observable: a pool of matches runs concurrently from the terminal.
- **Done** — `commands.py` + the `agentos-cli` registrar, 6 tests. Ran after Slices 6 and 7 (Deviation D4). `run` carries `--budget --concurrency --provider --profile --home --model --account --timeout --dry-run`; `--home` was added after smoke testing (Deviation D6). Verified live: 3 concurrent `claude-code` matches, 0 failures.

### Slice 6 - Pair sampling

- Add the default sampler and its hook override seam.
- RED: prove the default sampler covers the pool without repeating a pair before all pairs are seen, and that a consumer override is honored.
- GREEN: implement the default and the override.
- Check: `uv run pytest tests/test_tournament_sampling.py -q`.
- Observable: `run` accepts a match budget and selects pairs itself.
- Note: uncertainty-driven sampling is explicitly deferred; this slice only establishes the seam it will land on.
- **Done** — `sampling.py`, 7 tests. The default is least-played-first; the `select_pairs` hook overrides it wholesale.

### Slice 7 - Reporting and engine POIs

- Add raw accumulation reporting and `poi.py` with the three engine-owned class identities.
- RED: prove counts include match counts, that `No.Contest` distribution is reported per-pool and per-player, and that no ordering is emitted.
- GREEN: implement the report and POI emission.
- Check: `uv run pytest tests/test_tournament_report.py -q`.
- Observable: `agentos tournament show` prints accumulation a consumer can filter.
- **Done** — `report.py` + `poi.py`, 11 tests. Two match floors instead of one: `MIN_MATCHES_FOR_STANDING = 6` and `MIN_MATCHES_FOR_UNJUDGEABLE = 3`, honoring the landed `[PR]` line that clustered refusals are a sharper finding than a low score.

## Impl.Log

### Execution

- **Authorization gate ^c20260805-86u.** Execution was authorized by the `/agentos-hugentics --exec --ATO 610` turn, anchored as `^c20260805-86u`. Everything below this line was produced under that gate.
- **Result.** All seven slices landed. 66 tournament tests pass; the full `agentos-py` suite passes at 705 tests. `agentos tournament create|list|run|show` is registered and was exercised live against `claude-code` / `claude-sonnet-4-5-20250929`: 3 concurrent matches, 0 failures, and the deliberately weak player (`- [CT] stuff should probably be handled well`) lost both its matches (w0 l2 m2) — the tail behavior the system exists to surface.
- **Uncommitted.** Implementation changes are left uncommitted for user review, per the execute workflow.

### Blockers

- **B1 — cleared.** The `Agentos.Tournament` block family landed to `agentos-pkg/design/111-design.md` with a `000-INDEX.md` router entry: eight blocks (`Agentos.Tournament`, `Tournament.Definition`, `Tournament.Player`, `Tournament.Hook`, `Tournament.Match`, `Tournament.Judge`, `Tournament.Verdict`, `Tournament.Verdict::No.Contest`), 66 typed lines, all line-linked and block-grounded, linter clean at 0 errors with the opt-in `line-approval` and `line-verbatim-gate` checks passing. `Tournament.Hook` was added after this artifact was first written; the hook design in `Impl.Index` is now index-backed rather than chat-only.

### Decisions in open space

- **Placement in `agentos-py` rather than a new `agentos-tournament-py`.** Bloberia and Wayfinder — the two closest analogues, both general substrates with no domain — live inside the foundation library. A separate package would invert nothing and add a dependency edge for no gain. Revisit if the engine grows provider or storage backends of its own.
- **Bloberia as the record store.** The verdict record shape converged independently on Bloberia's exact contract: reserved envelope, application-owned JSON value, opaque identity, structural queries. Implementing separate persistence would duplicate it. Bloberia already lives in `agentos-py`, so no dependency direction is violated.
- **Judge output parsed from captured stdout.** `AgentRunResult` exposes `stdout`, but only under `process_mode="capture"`; v0 validates that against the contract. If provider stdout proves unreliable, the fallback is a written artifact path in the prompt, as `chatlas products` does with its staged output file — noted as the known escape hatch rather than built now.
- **Readiness verification.** The `resolve_agent` / `agent.run` / `AgentRunConfig` signatures, the flat `agentos-py/tests/test_*.py` layout the slice checks assume, and the `agentos-cli/src/*/cli.py` registrar pattern were each confirmed against current source before this plan was marked ready.

### Deviations

- **D1 — no fold, by user decision.** `Standing` was explicitly parked during design, so v0 stores and reports raw records without computing any ranking. The consequence is that the system's stated product — the weak tail — is not directly produced by v0; a consumer must derive it. This is a conscious waiver of the readiness expectation that every slice produce user-visible value, taken because committing a fold now would prejudge the parked concept.
- **D2 — no adaptive sampling.** Concentrating matches on the uncertain or low tail is what makes the system affordable at scale, and Slice 6 ships only a naive default. Recorded as known debt with its seam declared, not as an oversight.
- **D3 — chivo relationship undecided.** `notes/live/552-chivo-design-session.md` designs a general registry of reusable agent work with contestable, accumulated, ranked answers. A content-addressed match cache is close enough to overlap. v0 deliberately implements no cache, which keeps the question open rather than answering it by accident.
- **D4 — slice reorder (5 after 6 and 7).** `commands.py` imports `report.py` and `sampling.py`, so writing the CLI first would have meant stubbing both. Slices 6 and 7 ran ahead of Slice 5. No slice content changed; only the order did. The written plan's dependency direction was simply wrong.
- **D5 — attribution axis added to the verdict contract.** The design's `No.Contest` reason is free prose, and the first live run showed why that is not enough: the report grouped refusals by full sentence, producing one bucket per refusal and no countable signal. The landed `[DC]` line already says a refusal "carries a reason attributing the refusal to the question, to a player, or to the prompt it was given" — that three-way axis was implemented as a required `attribution` enum (`question`/`player`/`prompt`/`none`) alongside the free-text reason, threaded through `contract`/`model`/`store`/`runner`/`report` and the default rendering. This closes design intent rather than extending it, but it was found by running, not by reading.
- **D6 — two CLI gaps found only by smoke testing.** (a) Reopening a tournament called `load_definition` on its own snapshot and raised `shutil.SameFileError`; fixed with a separate `open_definition` that **verifies** the existing snapshot instead of re-recording it — re-recording would re-authorize a tampered snapshot rather than catch it. (b) `resolve_agent` accepts `home`, but `run` never exposed it, so running without `--profile` was impossible. Both are covered by regression tests now. Neither was reachable from the unit suite; both needed a real invocation.
