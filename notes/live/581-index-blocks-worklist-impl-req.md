# Index Blocks Worklist — Impl.Req

## Impl.Abstract

- **Goal**: `agentos index blocks` — a query surface over the index AST listing concept blocks with their grounding statistics; `--sort gr-density` returns the enrichment/grounding worklist (`Index.Enrichment`: density as the default selector).
- **Why**: `Grounding.Density` (unique inline anchors / kernel lines, `Inline.Grounding` appendix) is defined but not computed anywhere; the `--enrich` module currently points at a linter-meters fallback. A worklist is a query, not a check — it does not belong in the linter (user-settled).
- **Design center** (user direction: "use the index parser — integrate nicely with the existing infra"): computation lives in the model layer (`agentos.index.model`), the CLI is a thin renderer. `parse_depot()` is the only parsing entry; no second parser, no linter dependency.
- **Out of scope**: refactoring the linter's `_grounded_block_paths` to share the stats module (future unification, note only); appendix/agendix blocks in the listing (concept blocks are chapter-surface, same denominator rule as the 579 block meter); additional sort keys beyond `gr-density` (add on demand).
- **Repos**: `agentos-py` (model stats, commands, tests); `agentos-md` docs (S3: `--enrich` module update per the user's explicit follow-up, `agentos-py/AGENTS.md`). Reinstall from `agentos-cli/` after CLI changes.
- **Source**: user turns 2026-07-09 (session `9d194db7...`): density worklist as default selector ^c20260709-7u, single axis / `--sort gr-density` naming, "use the index parser — integrate nicely"; index concepts `Index.Enrichment` (107), `Inline.Grounding` + appendix metric lines (105), `Index.Model`.
- **Status**: implemented; suite green; live worklist verified

## Impl.Index

### Design.Decisions

- **stats in the model layer**: `src/agentos/index/model/stats.py` — `BlockGroundingStats` dataclass (`block_path`, `path`, `line`, `kernel_lines`, `unique_anchors`, `gr_density`, `board`) and `block_grounding_stats(model: IndexDepotModel) -> list[BlockGroundingStats]`; exported from `agentos.index.model`
- **denominator**: chapter-surface `BlockHeading`s with `parsed["valid"]` and `parsed["segments"] == []` — identical to the 579 block-meter rule; block identity is full `parsed["path"]`
- **numerator**: unique anchor tokens over the block's chapter `KernelLine`s (`parsed["block_path"] == block path`, spans `kind == "anchor"`); inline-only — board anchors do not count (`^c20260709-4u` decision)
- **board flag**: appendix-surface heading `parsed["path"] == f"{block}/Grounding.Head"` containing ≥1 `[GR]` kernel line with an anchor span — same rule as the linter's check; small logic duplication accepted, unification noted as future work
- **CLI**: `agentos index blocks --depot <path>... [--scope <path>...] [--sort gr-density] [--limit N] [--json]`
  - `--depot` repeatable, resolved like the linter's; each depot parsed via `parse_depot`
  - `--scope` same reporting-filter semantics as 579: filters listed blocks by file-path prefix; unmatched scope entry errors
  - `--sort gr-density`: ascending density, ties by `kernel_lines` descending then block name; default (no `--sort`) is document order; unknown sort value errors
  - `--limit N` truncates after sorting
  - text render: aligned table (block, density, anchors/lines, board, path:line); JSON: `{blocks: [...], summary: {blocks, kernel_lines, unique_anchors, gr_density}}` — summary density is the scoped aggregate (unique within scope / lines in scope, `^c20260709-5u`)
- **anchor syntax**: the parser's `ANCHOR_RE` is the single authority (now `^YYYYMMDD-N` after 580) — stats reads spans, never regexes text itself

### Current.State *(inspect before coding)*

- `src/agentos/index/model/`: `parse_depot(root)` → `IndexDepotModel(root, documents)`; `IndexDocument.surface_kind` in router/chapter/appendix/agendix; `BlockHeading.parsed` path/root/segments/valid; `KernelLine.parsed["block_path"]`; anchor spans `span.parsed["anchor"]`
- `src/agentos/index/commands.py`: `register_index_commands` — `index` subparsers; only `linter` today; `_resolve_under_root`-style path handling lives in linter.py (`build_linter_config`)
- 580 landed the `^` sigil migration (parser + linter + depots); anchors in spans carry the bare token
- tests: `tests/test_index_model_parser.py`, `tests/test_index_linter.py` — fixture-depot helpers to reuse or mirror

## Execution.Plan

*(test-first; fixture depot: one chapter file with a stamped block (1 anchor × n lines), a worked block (distinct anchors), an unanchored block, a parameterized block (`Concept:Param`); appendix file giving ONE of them a `Grounding.Head`)*

### S1 — model stats
- what: `stats.py` + exports; computation per Design.Decisions
- RED: unit tests on `block_grounding_stats` — density values (0, 1/n, ~1), unique counting (repeated anchor counts once), inline-only (board anchor does not raise density), parameterized block identity, board flag on exactly the head-bearing block
- check: suite green
- status: done

### S2 — `agentos index blocks` CLI
- what: subparser + handler rendering stats; `--depot/--scope/--sort/--limit/--json`
- RED: e2e over the fixture depot — `--sort gr-density` orders unanchored (0) → stamped (1/n) → worked (~1); `--scope` filters and recomputes summary; bogus scope and bogus sort error; `--json` payload shape; `--limit`
- check: suite green; `ruff` clean
- status: done

### S3 — live + docs
- what: reinstall; live run `agentos index blocks --depot skills/agentos-pkg --sort gr-density --limit 15` in agentos-md (expect the 577-stamped/enriched blocks at the tail, legacy blocks at 0 leading); update `agentos-md` `skills/agentos-index/references/enrich.md` (replace the linter-meters fallback with the real command — the user's explicit follow-up), `references/gr-survey.md` selector mention if stale, `agentos-py/AGENTS.md` CLI listing
- check: live output sane; both depots lint clean; full suite green
- status: done

### Acceptance signals
- one command returns the sorted grounding worklist with reproducible numbers at any scope
- computation importable from `agentos.index.model` without CLI (`Dependency.Profile.Split`: model stays library-first)
- no linter behavior change; `No.Regression.Tests.Allowed` respected

### Risks / deviation triggers
- if chapter/appendix pairing needs linter-config derivation (multi-dir depots), reuse the directory-walk convention from `parse_depot` only — do not import linter internals into the model
- if `parse_depot`'s surface classification misses a live layout case, fix classification in the parser (single authority), not in stats

## Impl.Log

- 2026-07-09: designed and executed in-session (--dev --AUTO); review round skipped (same-agent develop, user-triggered)
- 2026-07-09: open-space decision: `BlockGroundingStats` retains the per-block anchor SET (frozenset) so the scoped aggregate counts unique-within-scope exactly — summing per-block uniques would double-count shared stamps (^c20260709-5u semantics)
- 2026-07-09: fixture arithmetic error in the RED (8 kernel lines, not 9) — test corrected, not the implementation
- 2026-07-09: live: `agentos index blocks --depot skills/agentos-pkg --sort gr-density` → 227 blocks, aggregate 0.0161; tail is exactly this week's worked blocks (Inline.Grounding 0.75, Kernel.Block.Grounding 0.67, Index.Enrichment 0.6) — metric validates against known history
- 2026-07-09: verification: agentos-py suite 290 passed, ruff clean; CLI reinstalled; docs updated (enrich.md fallback replaced with the real command, gr-survey.md selector, agentos-py/AGENTS.md)
