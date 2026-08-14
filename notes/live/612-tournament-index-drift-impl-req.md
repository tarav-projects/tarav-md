# Tournament / Bloberia Index Drift - Impl.Req

## Impl.Abstract

- **Goal:** bring `agentos.tournament` and `agentos.bloberia` back into agreement with the index after the capture pass of `^c20260806-5u`…`^c20260806-45u`. The engine must stop holding a pool, stop authoring match prompts, and stop computing identity; Bloberia must gain record namespaces; the tournament must gain a real depot.
- **Status:** executed. All seven slices are implemented, the full `agentos-py` suite passes at 750 tests, and the engine was verified end to end against live `claude-code` judges on a namespaced global depot. Changes are uncommitted for review.
- **Source design:** `tarav-pkg/design/111-design.md` (`Agentos.Tournament`, `Tournament.Definition`, `Tournament.Hook`, `Tournament.Match`, `Tournament.Judge`, `Tournament.Depot`) and `tarav-pkg/design/109-design.md` (`Agentos.Bloberia`, `Bloberia.Record.Namespace`).
- **Prior implementation:** `notes/live/610-agentos-tournament-v0-impl-req.md` built the v0 this request corrects. Nothing in 610 was wrong when written; the design moved.
- **In scope:** Bloberia record namespaces; a `Tournament.Depot` with a global default and `definitions/` + `records/<tournament-id>/`; the rewritten hook surface (`match_players`, `present_player`, `match_identity`, `verdict_slot`); engine-composed `Match.Verbatim` with position labels the consumer cannot touch; a `tournament.pairing` library replacing the engine sampler; a report that folds players from verdicts; the CLI surface that follows from all of it.
- **Out of scope:** covering a definition's import closure (`Issue.I0001`, deliberately open); per-namespace locking (`^c20260806-36u` keeps locking depot-wide); adaptive sampling; cross-tournament aggregation; a match cache; the index-line tournament that will consume this.

## Impl.Index

### Drift Inventory

Five landed lines the current code contradicts, each verified against source before this plan was written:

- `^c20260806-17u` — the engine holds no pool and enumerates no pairs. `sampling.py:37` does `combinations(sorted(set(pool)), 2)` over `tournament.players`.
- `^c20260806-10u` — a hook does not author the whole match prompt. `hooks.py:78` `render_match` returns the entire prompt string.
- `^c20260806-21u`, `^c20260806-22u` — match identity is required with no default. `hooks.py:105` falls back to `_default_identity(rendering)`, which is the engine computing one.
- `^c20260806-26u` — the depot resolves to a canonical global location. `commands.py:159` makes `--depot` required with no default.
- `^c20260806-31u`…`-37u` — record namespaces. `bloberia/core.py:227` hardcodes `root / "records" / f"{id}.json"`; the concept does not exist.

One live defect follows from the third: `_default_identity` hashes the rendering, and the rendering is built from `presented` — the shuffled order. The same pair run twice yields different `match_id`s about half the time, fragmenting accumulation. No current definition hits it because both supply their own identity.

### Bloberia.Record.Namespace

- A namespace is a relative POSIX path under `records/`, of arbitrary depth, addressed as a prefix.
- `create`, `get`, `edit`, `query`, and `check` accept an optional `namespace`; omitting it preserves today's meaning.
- `query(namespace=...)` walks only that prefix. `query()` with no namespace walks `records/` recursively, so an existing flat depot reads unchanged.
- `get(record_id)` without a namespace searches every namespace rather than failing; with one, it is a direct path.
- `check` must walk recursively. Today it globs `records/*.json` and would report **ok** on a namespaced depot by finding nothing — a check that passes because it looked in the wrong place is worse than no check.
- Namespace validation rejects absolute paths, `..` segments, and empty segments. A rejected namespace is an error, never a silent fallback to the root.
- Locking stays depot-wide. Namespaces partition reads only.
- New `namespaces()` returns the namespace prefixes present, so a consumer can list without reading records.

### Tournament.Depot

- Default root `~/.agentos/tournament`, overridable by `AGENTOS_TOURNAMENT_DEPOT` and by an explicit `--depot`. This follows the `~/.agentos/wayfinder` and `~/.agentos/activity` precedent.
- Layout: `definitions/<tournament-id>/` holds the frozen definition snapshot and its `File.Locking` sidecar; `records/<tournament-id>/` is the Bloberia namespace holding that tournament's record and every verdict.
- **The tournament id stops being the Bloberia record id.** The namespace must be known before the record is written, so `TournamentStore` mints the id itself. This also states the truth better: a tournament is a namespace, not a record.
- `tournaments()` lists namespace directories and reads one record per tournament, instead of scanning every record in the depot.
- `verdicts(tournament_id)` queries one namespace and never opens another tournament's files.

### Hook Surface

- Declared hooks: `match_players`, `present_player`, `match_identity`, `verdict_slot`.
- `match_players` and `match_identity` are **required and have no default**. A definition supplying neither is a load error naming both, not a tournament that runs and accumulates nothing.
- `present_player` defaults to `str(player)`. `verdict_slot` defaults to `{}`.
- `render_match` and `select_pairs` are removed outright, not deprecated (`No.Legacy.Allowed`).
- `match_players` returns one pair or `None`. `None` means no further match, ending a run before its budget.
- `match_identity` receives the players in **canonical order with their presentations**, never the presented order. Identity that varied with the shuffle would be the defect described above.
- `HookContext` gains `criteria`, `player`, `presentations`, `match_index`, and drops `presented` and `rendering`. It stays frozen and data-only.
- Hooks may randomize which players meet; only presentation-order randomization is engine-side (`^c20260806-19u`, `^c20260806-20u`). No mechanism change is needed — `locking.verify` checks for writes, and `random` writes nothing.

### Engine Framing

- The engine composes `Match.Verbatim` from: the definition's `question`, its optional `criteria`, the two presentations under engine-owned `A:` / `B:` labels, and the answer contract block.
- The consumer never sees or supplies a position label, so the `presented[_POSITIONS.index(outcome)]` decode cannot disagree with the rendering. This is the whole point of the inversion: the hazard becomes unreachable rather than guarded.
- Order of operations per match: present each player → derive identity from canonical order → shuffle → compose → hash → spawn → validate → decode → append.
- Identity is computed **before** the shuffle; the verbatim hash **after**. They are separate mechanisms and the code should read that way.

### Pairing Library

- New `agentos/tournament/pairing.py` holds strategies a definition imports and calls from its own `match_players`: round-robin, least-played, and uniform-random selection.
- Each returns one pair, matching the hook's shape.
- The engine never imports it — it exists for definitions. Placing it under `agentos.tournament` is a packaging convenience, not an engine dependency, and the test suite must not let the engine reach for it.
- `sampling.py` and `tests/test_tournament_sampling.py` are deleted.

### Reporting

- The report folds its player set from the verdicts it was given, since no declared pool exists.
- A player that has left the definition's pool keeps its accumulated history and stays visible in the report.
- The report signature drops its dependence on `tournament.players`; it takes the tournament for identity and the verdicts for content.
- POI derivation is unchanged — `poi.py` reads the report's `players` rows, whose shape is preserved.

### CLI Surface

- `tournament create` loses `--player` and `--players-file`; a tournament is a definition, not a definition plus a list.
- `--depot` becomes optional everywhere, defaulting to the global depot.
- `run`, `show`, and `list` keep their current flags. `run --budget` becomes an upper bound the definition may end early.
- `agentos bloberia ...` gains an optional `--namespace` on `create`, `get`, `edit`, and `query`.

## Impl.Agendix

- **Gate `^c20260806-46u`** — the `/tarav-hugentics --impl --dev --AUTO` turn authorizes both the design and the execution of this artifact. In `Alignment.Mode::Autonomous` this one anchor is the coarse gate covering the whole run.
- **Touched — `tarav-pkg/design/111-design.md`**: `Tournament.Hook` (`^c20260806-10u`, `-11u`, `-13u`, `-14u`, `-15u`, `-16u`, `-17u`, `-19u`, `-20u`, `-21u`, `-22u`, `-23u`), `Tournament.Match` (`^c20260806-7u`, `-8u`), `Tournament.Judge` (`^c20260806-9u`), `Tournament.Definition` (`^c20260806-5u`, `-6u`), `Tournament.Depot` (`^c20260806-25u`…`-30u`), `Agentos.Tournament` (`^c20260806-43u`, `-44u`).
- **Touched — `tarav-pkg/design/109-design.md`**: `Bloberia.Record.Namespace` (`^c20260806-31u`…`-37u`).
- **Touched — `tarav-pkg/issues/100-issues.md`**: `Issue.I0001.Tournament.Definition.Import.Closure` stays open and out of scope.
- **Structural** — `notes/live/610-agentos-tournament-v0-impl-req.md` is the prior implementation this request corrects; the derivation is the evidence.
- **Open.Space** — the pairing library's own strategy vocabulary has no index home. It stays provisional and unanchored.

## Execution.Plan

### Slice 1 - Bloberia record namespaces

- Add namespace support to `bloberia/core.py`: validation, path resolution, recursive walk, `namespaces()`, and the `get` fallback search.
- RED: prove a namespaced record round-trips; prove `query()` with no namespace finds records in every namespace; prove `query(namespace=...)` excludes siblings; prove `get(id)` finds a namespaced record without being told the namespace; prove an existing flat depot still reads; prove `check` walks into namespaces; prove `..` and absolute namespaces are rejected.
- GREEN: implement in `core.py`, then expose `--namespace` in `bloberia/commands.py`.
- Check: `uv run pytest tests/test_bloberia.py -q`.
- Observable: `agentos bloberia create --depot X --namespace a/b --value-json '{}'` then `query --namespace a` returns it and `query --namespace c` does not.
- **Done** — `core.py` gains `_validate_namespace`, `_record_paths`, `_locate`, and `namespaces()`; `commands.py` gains `--namespace` on create/get/edit/query. 11 new tests in `tests/test_bloberia_namespace.py`, existing `tests/test_bloberia.py` unchanged and green.

### Slice 2 - Tournament depot and store

- Add the depot default resolution, the `definitions/` + `records/<tid>/` layout, and store-minted tournament ids.
- RED: prove the default root resolves and `AGENTOS_TOURNAMENT_DEPOT` overrides it; prove two tournaments' verdicts land in separate namespaces; prove `verdicts(tid)` returns nothing from a sibling tournament; prove `tournaments()` lists without a full scan.
- GREEN: update `store.py` and add the depot resolution helper.
- Check: `uv run pytest tests/test_tournament_store.py -q`.
- Observable: a depot on disk shows `definitions/<tid>/` and `records/<tid>/`.
- **Done** — new `depot.py` owns `resolve_depot_root`; `store.py` mints the tournament id, writes into the per-tournament namespace, and lists by directory. `Tournament` drops `players`. 6 tests in `tests/test_tournament_depot.py`, `tests/test_tournament_store.py` rewritten.
- Depends on Slice 1.

### Slice 3 - Hook surface rewrite

- Replace `render_match`/`select_pairs` with `match_players`/`present_player`; make `match_identity` required; reshape `HookContext`.
- RED: prove a definition missing `match_players` or `match_identity` fails at load naming the missing hook; prove `present_player` defaults to `str`; prove `match_players` returning `None` is accepted as exhaustion; prove a returned pair that is not two distinct non-empty strings is rejected; prove identity does not see the presented order.
- GREEN: rewrite `hooks.py`.
- Check: `uv run pytest tests/test_tournament_hooks.py -q`.
- Observable: a three-line definition file loads and its hooks resolve.
- **Done** — `hooks.py` rewritten: `_require_hooks` fails at load naming every missing required hook, `HookContext` drops `presented`/`rendering` and gains `criteria`/`player`/`presentations`/`match_index`. 15 tests.
- Depends on nothing; may run before Slices 1-2 if convenient.

### Slice 4 - Engine framing and the match loop

- Move prompt composition into `runner.py`; compute identity before the shuffle; drive matches by repeated `match_players` calls instead of a pair list.
- RED: prove the composed verbatim carries the question, both presentations under `A:`/`B:`, and the answer contract; prove a judge answering `B` records the player presented second; prove identity is stable across two runs of the same pair despite different presented order; prove `match_players` returning `None` stops the run under budget; prove a failed spawn still appends no record.
- GREEN: rewrite the composition and loop in `runner.py`.
- Check: `uv run pytest tests/test_tournament_runner.py -q`.
- Observable: one match runs end to end against a stub judge with no consumer-authored prompt.
- **Done** — `runner.py` rewritten around `compose_verbatim`; `_presented_order` now shuffles players and presentations together; `_collect_pairs` drives the loop from the hook. 14 tests.
- Depends on Slice 3.

### Slice 5 - Pairing library

- Add `pairing.py` with round-robin, least-played, and random selection; delete `sampling.py` and its test file.
- RED: prove least-played picks an unplayed pair before a played one; prove round-robin cycles deterministically; prove random selection with a seeded rng is reproducible; prove each returns exactly one pair or `None` when the pool is too small.
- GREEN: implement, then delete the sampler.
- Check: `uv run pytest tests/test_tournament_pairing.py -q`.
- Observable: a definition importing `round_robin` runs a full pool without writing selection logic.
- **Done** — `pairing.py` with `round_robin`, `least_played`, `random_pair`, `played_counts`. `sampling.py` and its test file deleted. 10 tests, one of which greps the engine to prove it never imports the library.
- Depends on Slice 3.

### Slice 6 - Report folds from verdicts

- Derive the player set from verdicts; drop the declared-pool dependency.
- RED: prove a player appearing only in verdicts is reported; prove a player with no verdicts does not appear; prove counts and the no-contest distribution are unchanged for a pool where every player played; prove no ordering is emitted.
- GREEN: update `report.py`.
- Check: `uv run pytest tests/test_tournament_report.py -q`.
- Observable: `tournament show` reports a player whose line was edited out of the definition.
- **Done** — ran out of order, immediately after Slice 2 (see Deviation D1). `report.py` builds its rows from verdict envelopes. 13 tests.
- Depends on Slice 2.

### Slice 7 - CLI, docs, and full-suite green

- Update `commands.py` for the new create surface and optional `--depot`; refresh the `Tournament System` section of `agentos-py/AGENTS.md` and add Bloberia namespaces to its `Bloberia System` section.
- RED: prove `create` needs only a definition; prove omitting `--depot` uses the default root; prove `run` honors an early `None` from `match_players`.
- GREEN: implement, then run the full `agentos-py` suite.
- Check: `uv run pytest -q` and one live `agentos tournament run` against a real judge.
- Observable: a tournament is created, run, and shown from the terminal with no `--depot`.
- **Done** — `commands.py` updated, `AGENTS.md` `Tournament System` rewritten and `Bloberia System` extended. 10 tests. Live: 3 concurrent `claude-code` matches, 0 failures, `bloberia check` clean on the namespaced depot.
- Depends on every prior slice.

## Impl.Log

### Blockers

- None. Every landed line this plan implements is reviewed with a verifying tokenized approval, and the two design surfaces linted at 0 errors after the capture pass.

### Decisions in open space

- **The tournament id leaves Bloberia.** The namespace has to exist before the record is written, so the store mints the id. Bloberia keeps assigning its own opaque record ids underneath; they simply stop being the tournament's identity.
- **`pairing.py` ships inside `agentos.tournament`.** A separate package would be truer to `^c20260806-15u` ("never in the engine") but buys nothing at this size. The boundary is enforced by the engine never importing it, and that is worth an explicit test rather than a convention.
- **Flat-depot reads are kept deliberately.** `No.Legacy.Allowed` would normally delete the untyped path, but `^c20260806-34u` states the fallback as design, not compatibility debt.

### Execution

- **Gate `^c20260806-46u`** — the `--impl --dev --AUTO` turn authorized both phases. Git checkpoints were taken in `agentos-py`, `agentos-cli`, and `agentos-md` before the first edit.
- **Result.** 750 tests pass across the whole `agentos-py` suite (up from 705: +11 bloberia namespace, +6 depot, +10 pairing, +2 report, and net additions across the rewritten hook/runner/command suites, less the 7 deleted sampler tests).
- **Live verification.** A definition importing `pairing.round_robin` ran 3 concurrent matches against `claude-code` / `claude-sonnet-4-5-20250929`. 0 failures. The deliberately weak player (`- [CT] stuff should probably be handled well`) lost both its matches (w0 l2 m2) — the tail behaviour the system exists to surface. The depot shows `definitions/<tid>/` beside `records/<tid>/`, and `agentos bloberia check` reports 0 errors on it.
- **Uncommitted.** Implementation changes are left uncommitted for user review.

### Deviations

- **D1 — Slice 6 ran immediately after Slice 2.** Removing `players` from `Tournament` breaks `report.py` in the same edit, so deferring the report to its planned position would have left the suite red across four slices. The plan's dependency note was right; its ordering was not. No slice content changed.
- **D2 — the shuffle had to carry presentations, not just players.** The plan described shuffling the pair and composing from presentations, but the old `_presented_order` shuffled players alone. Presenting after the shuffle would have called `present_player` twice per match and let a non-deterministic hook disagree with itself; presenting before and shuffling only names would have mismatched each presentation to the wrong position. `_presented_order` now shuffles `zip(players, presentations)` and returns both, which is the only ordering that keeps a single presentation per player bound to its position.
- **D3 — one report test asserted the declared-pool order.** `test_report_emits_no_ranking_or_ordering` checked `["a", "b", "c"]`, which only existed because the pool was declared. Rather than weaken it, the test now records a match whose *loser* is encountered first, so the assertion still proves no ranking is applied while ranging over a verdict-derived set.
- **D4 — hook errors needed catching in the fan-out.** With identity now a required hook, a bad `match_identity` return raises `HookReturnError` mid-match. `run_pool` caught only `CliError`, so one bad hook would have aborted every sibling. It now catches `HookError` too and records the match as a failure row, which is what the failure-envelope design already promised.
