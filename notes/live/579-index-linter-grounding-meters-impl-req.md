# Index Linter Grounding Meters — Impl.Req

## Impl.Abstract

- **Goal**: split grounding coverage into two independent, opt-in linter meters — block-level (`Grounding.Head` presence) and line-level (inline anchors) — and add a general `--scope` so campaign counts are reproducible from the command line alone.
- **Why**: `Line.Unlinked` under-values the preferred landing form (a head-grounded block still reports every line unlinked — observed closing Gr.Req 577), and depot-only counting forced each agent to post-filter findings with their own ad-hoc scope (the 1202-vs-1208 divergence). User direction: separate the two checks, measure blocks and lines independently, integrate with existing infra, design generally — do not overfit to the 577 case.
- **Design center**: three general mechanisms, no special cases —
  1. a `coverage` set in `LinterConfig` (meter names) generalizing the ad-hoc `warn_unlinked` bool; future meters (drift, hint-desync) join the set, not the flag namespace
  2. `Block.Ungrounded`, a new coverage check measuring blocks on their own axis (no cross-coverage: inline anchors never satisfy the block meter, a `Grounding.Head` never satisfies the line meter)
  3. `--scope`, a reporting filter over findings and meter denominators; checks still run over the whole depot so cross-file context (routers, appendix pairing) stays intact
- **Out of scope**: drift/hint meters (future coverage names); semantic verification (agent-side by design); changing any structural check; the chatlas provenance bridge (unaffected — it consumes `parsed_linter_kernel_lines`, which does not change).
- **Repos**: `agentos-py` (linter, commands, tests). Docs follow-up in `agentos-md` (`skills/agentos-index/references/check.md`, `gr-survey.md` baseline step) — small, part of S4. Reinstall after CLI changes: `uv tool install --reinstall --editable .` from `agentos-cli/`.
- **Source**: user directions in session `99144906-781e-43cc-9d27-b40f166e2acf` (2026-07-09): "separate the two checks in the linter", "measure which blocks and lines independently", "do not overfit for this case only"; Gr.Req 577 `Gr.Log` meter notes; index concepts `Kernel.Block.Grounding`, `Inline.Grounding`, `Index.Linter` (+ `External.Checks` appendix).
- **Status**: implemented; suite green; live acceptance verified

## Impl.Index

### Design.Decisions

- **coverage config**: `LinterConfig.coverage: frozenset[str]` replaces `warn_unlinked: bool`; recognized names now: `"line"`, `"block"`. CLI: `--coverage <name>` repeatable, plus `--coverage all`; `--warn-unlinked` stays as a back-compat alias for `--coverage line` (help text says so). No deprecation removal in this req.
- **checks emit-per-config, not gate-per-config**: follow the existing `Line.Unlinked` pattern — coverage checks always run and consult `config.coverage` to decide what to emit; no blocked-check noise for disabled meters.
- **`Index.Linter/Block.Ungrounded`** (warning, coverage `"block"`): fires on a chapter-surface concept block with no `Grounding.Head`.
  - denominator: `BlockHeading` nodes in `surface_kind == "chapter"` documents with `parsed["segments"] == []` and `parsed["valid"]` — top-level concept blocks only; appendix/agendix headings never enter the denominator
  - block identity is `parsed["path"]`, NOT `parsed["root"]` — parameterized names split into root+params (`Line.Type::DF` → root `Line.Type`), so root-matching would collapse distinct blocks
  - grounded: some appendix-surface document has a `BlockHeading` whose `parsed["path"] == f"{block_path}/Grounding.Head"` (equivalently: same full path prefix, `parsed["segments"] == ["Grounding.Head"]`) whose section contains at least one `KernelLine` with `parsed["act"] == "GR"` AND an anchor span — an anchored non-`[GR]` line does not satisfy the block meter
  - the finding lands on the chapter block's heading line
- **`Line.Unlinked` semantics unchanged** except its trigger: coverage `"line"` instead of `warn_unlinked`. The agendix mandatory case (hard provenance) is NOT coverage — it keeps firing regardless of flags, exactly as today.
- **no cross-coverage in either direction** — each landing form moves only its own meter.
- **`--scope <path>`** (repeatable, file or directory, resolved under root like `--depot`): a *reporting* filter —
  - all checks run over the full configured surfaces (cross-file checks keep their context)
  - mechanics: `LinterState` stays unscoped; scoping is a derivation applied when rendering — filter findings by path prefix, then RECOMPUTE `CheckResult` finding/error/warning counts, the summary, and the coverage meters from the scoped findings/meter items; nothing scoped is stored back into state
  - coverage meter denominators/numerators are computed within scope (the meter traversal carries item paths for exactly this)
  - the JSON payload echoes the resolved scope; a scope that matches no configured file is a config-surface error (typo protection)
- **meters in the summary**: when any coverage name is enabled, the JSON payload gains a `coverage` object — e.g. `{"line": {"linked": n, "total": m}, "block": {"grounded": g, "total": b}}` — and the text render prints one line per enabled meter. The campaign number becomes tool output, not agent arithmetic.

### Current.State *(inspect before coding)*

- `src/agentos/index/linter.py` (~1316 lines): `LinterConfig` (frozen dataclass, `warn_unlinked` at line ~120), `build_linter_config`, `run_linter` (socket with `extra_checks`), `CHECKS` tuple, `_check_line_unlinked` (~1197, incl. the agendix always-on branch), `parsed_linter_kernel_lines` feed
- `src/agentos/index/model/`: `BlockHeading.parsed` carries `path`/`root`/`segments`/`valid` (`_parse_block_path`); `KernelLine.parsed["block_path"]`; anchor spans via `span.kind == "anchor"`
- `src/agentos/index/commands.py`: `register_index_commands` — `--depot/--index/--appendix/--json/--warn-unlinked`; `_cmd_linter` builds config from args
- callers of `build_linter_config`/`LinterConfig(warn_unlinked=...)`: commands.py and tests — grep before changing the signature; the chatlas bridge (`agentos_chatlas/index_checks.py`) touches neither
- tests: `tests/test_index_linter.py` (+ `test_index_model_parser.py`); e2e depots under the tests' fixture helpers — inspect how existing `Line.Unlinked` tests build depots and reuse

## Execution.Plan

*(test-first; each slice RED at the linter boundary — build a small fixture depot with a chapter file, an appendix file with one `Concept.X/Grounding.Head`, and a second ungrounded concept)*

### S1 — coverage config replaces warn_unlinked
- what: `LinterConfig.coverage: frozenset[str]`; `build_linter_config(coverage=...)`; `_check_line_unlinked` consults `"line" in config.coverage`; CLI `--coverage` (repeatable, accepts `all`) with `--warn-unlinked` mapping to `{"line"}`; update existing callers/tests
- RED: `--coverage line` reproduces today's `--warn-unlinked` findings; `--warn-unlinked` still works (alias test); no coverage flag → agendix lines still flagged, chapter/appendix lines not
- check: suite green
- status: done

### S2 — Block.Ungrounded check + meters payload
- what: new `_check_block_ungrounded` registered in `CHECKS` (coverage `"block"`); `coverage` object in the JSON payload and text summary lines, computed from the same traversal. Note: registering it grows the flagless check count by one (17 → 18, shown as passed) — accepted, this mirrors exactly how `Line.Unlinked` already appears when its flag is off; flagless FINDINGS must not change
- RED: fixture with grounded + ungrounded concept blocks → exactly the ungrounded one fires, on its heading line; inline-anchored-but-headless block still fires (no cross-coverage); a `Grounding.Head` whose only anchored line is NOT `[GR]`-typed does not ground its block; a parameterized block (`Concept:Param`) is matched by full path, not root; appendix/agendix headings absent from the denominator; JSON `coverage.block == {"grounded": 1, "total": 2}`; with `--coverage all` both meters appear
- check: suite green
- status: done

### S3 — --scope reporting filter
- what: `--scope` CLI + `LinterConfig.scope_paths`; findings/counts/meters filtered to scope; JSON echoes scope; unmatched scope entry → config-surface error
- RED: two-chapter fixture depot; `--scope <chapter-1>` drops the other chapter's findings from findings AND summary AND meters while structural cross-file checks still see the whole depot; bogus `--scope` errors
- check: suite green
- status: done

### S4 — live acceptance + docs
- what: reinstall; live: `agentos index linter --depot skills/agentos-pkg --coverage all --scope skills/agentos-pkg/design --json` in agentos-md — expect the block meter to show the four 577-grounded blocks as grounded and the line meter to reproduce the 10X count without post-filtering; update `agentos-md` `skills/agentos-index/references/check.md` (built-in checks + flags), `references/gr-survey.md` step 1 (baseline = the scoped linter command, recorded verbatim in `Gr.Abstract`), and `agentos-py/AGENTS.md` (it documents the linter CLI flags and requires updating on CLI changes)
- check: live numbers sane; both depots lint clean unflagged (no default-behavior change); `uv run pytest` + `ruff` green in agentos-py
- status: done

### Acceptance signals
- one command yields reproducible scoped campaign numbers: findings + two independent meters
- default (flagless) linter FINDINGS are unchanged on both live depots (0 errors / 0 warnings stays 0/0); the check count grows by exactly one passed check — the only permitted default-output difference
- `No.Regression.Tests.Allowed` respected; the chatlas bridge untouched and its tests green

### Risks / deviation triggers
- if `LinterConfig` freezing makes the `warn_unlinked` → `coverage` migration awkward at call sites, keep a `warn_unlinked` constructor kwarg that folds into `coverage` — do not keep two sources of truth in the dataclass
- if the full-path (`parsed["path"]`) block ↔ appendix-head matching hits a naming wrinkle, log it in `Impl.Log` rather than inventing normalization — never fall back to `root`-only matching (parameterized blocks would collide)
- if scope filtering of per-check counts requires deep `LinterState` surgery, filter at render/payload time only — state internals stay unscoped

## Impl.Log

- 2026-07-09: review round — `agentos-hugentics-impl --review` run in a fresh agent returned `not ready` with 5 findings (default-output conflict, root-vs-path block identity, [GR]-typed grounding requirement, scope derivation mechanics, agentos-py/AGENTS.md docs); all 5 folded into Design.Decisions / Execution.Plan / Acceptance above
- 2026-07-09: execution checkpoint created before edits per workflow: `agentos-py` empty checkpoint `cb8e4f2`; `agentos-md` checkpoint `da2d646` captured pre-existing index changes.
- 2026-07-09: executed S1-S3 in `agentos-py`: `LinterConfig.coverage` replaces `warn_unlinked` as state, `--warn-unlinked` folds into `coverage={"line"}`, `--coverage line|block|all` and `--scope` are wired, scoped render/payload recomputes findings/check counts/summary/meters without mutating `LinterState`.
- 2026-07-09: implemented `Index.Linter/Block.Ungrounded` with full `parsed["path"]` block identity and `[GR]`+anchor `Grounding.Head` satisfaction; parameterized block coverage test added.
- 2026-07-09: implementation decision: `Block.Ungrounded` is registered in `CHECKS`, so flagless clean depots now report 18 passed checks instead of 17; flagless findings remain unchanged.
- 2026-07-09: updated `agentos-py/AGENTS.md`, `agentos-index` `references/check.md`, and `references/gr-survey.md` for the new linter flags and campaign baseline.
- 2026-07-09: installed CLI refreshed from `agentos-cli` with `uv tool install --reinstall --editable .`.
- 2026-07-09: live acceptance: `agentos index linter --depot skills/agentos-pkg --coverage all --scope skills/agentos-pkg/design --json` reports line `23/1231` linked (1208 unlinked) and block `7/224` grounded; scoped summary has 1425 warnings, 0 errors.
- 2026-07-09: default live depots clean unflagged: `agentos-md/skills/agentos-pkg` and `agentos-chatlas-md/skills/agentos-chatlas-pkg` both report 18 checks, 0 findings.
- 2026-07-09: verification: `uv run pytest tests/test_index_linter.py` 30 passed; `uv run pytest` 285 passed; `uv run ruff check src tests` clean.
