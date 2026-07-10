# Skillware v1 — Impl.Req

## Impl.Abstract

- **Goal**: land Skillware v1 — the skill-development compilation system. A skill's files can be produced from `.skillware/src/**/*.skw.md` sources; a `.skw.md` is markdown plus `[!skw]` callout recipes; `agentos skillware build/check/status` is the deterministic CPU toolchain; a POC skill `agentos-index2` demonstrates the whole system on real content.
- **Model** (user-settled across the 2026-07-09/10 design discussion):
  - src surface: `<skill>/.skillware/src/` mirrors the skill tree; `references/ground.skw.md` compiles to `references/ground.md` (strip `.skw`). No `.skw.md` = hand-owned file, never touched.
  - recipe syntax: an Obsidian callout — a blockquote whose first line is `> [!skw]- <verb>` — placed first in a section; field lines `> from: <locator>` (repeatable), `> intent: <free prose>` (continuation lines stay quoted). Verbs v1: `copy`, `derived`, `end`.
  - the produced body sits *outside* the callout as ordinary markdown, from the recipe to a `> [!skw] end` one-liner or the next heading, whichever first. Sections without a recipe are hand-owned prose. Production spans default to section scope; finer encapsulation is deferred by design.
  - `copy`: body is the target's expanded body — build refreshes it in src (CPU). `derived`: body is the agent-authored current solution — build never touches it; the agent re-derives in src when flagged stale.
  - compile = strip every `[!skw]` callout (and span-end markers) from src and emit the target file. Deterministic; zero work lands on the executable surface.
  - locators: `path#Region` / `path` — resolved against the src root first, then the skill root; a `.skw.md` target region is recursively expanded (innermost-first, cycle = error naming the chain); a plain file gives its raw region body. Bare `Dotted.Name` = index-block body (kernel lines) resolved in the depots configured in `.skillware/skillware.json`. Region = heading-section body, heading excluded, subsections included.
  - drift via `.skillware/lock.json` written at build: per compiled file the output hash; per recipe the content hash of each dependency. Check verdicts: `never-built`, `stale-build` (on-disk == lock but recompile differs), `hand-edited` (on-disk != lock), `copy-drift` (src copy body != target expansion; build fixes), `derived-stale` (dep hash changed — the agentic flag), `ok`.
- **Supersedes 583 completely** (user: "Totally, 100% — this will be the totality of the system"): `agentos skills imports`, `agentos.skills.imports`, its tests, and the two live `build/*-imports.md` manifests are removed (`No.Legacy.Allowed`); the `agentos-skill-pkg-builder` references re-route to skillware.
- **Out of scope**: index (107) concept-block updates for Skillware — the Skillware/Import blocks need a design session, noted as follow-up; `$link`/pointer verb; `--with-heading`/`--level` flags; parameters/conditionals; cross-skill import roots (settings key reserved); Obsidian CSS for the `skw` callout.
- **Repos**: `agentos-py` (skillware package + CLI), `agentos-cli` (registration + reinstall), `agentos-md` (POC skill, builder-skill re-route, manifest removals).
- **Source**: this session's design discussion (2026-07-09 evening → 2026-07-10), converged over live examples; syntax family chosen: Obsidian callouts. Prior art superseded: note `583-import-manifest-tooling-impl-req.md`.
- **Status**: executed 2026-07-10 — all slices complete; changes uncommitted for review

## Impl.Index

### Design.Decisions

- **package layout**: `agentos-py/src/agentos/skillware/` — `model.py` (dataclasses + src parsing), `build.py` (locator resolution, expansion, compile, lock, check), `commands.py` (`register_skillware_commands`). Library-first; CLI is a thin wrapper (house pattern: anchory, index).
- **parsing** is a line scan, no new markdown engine: a blockquote block whose first line matches `> [!skw]±  <verb>` opens a recipe; `> key: value` lines feed the schema; a bare `> ...` line continues the previous field; the blockquote ends at the first non-`>` line. A `skw` callout with an unknown verb or missing required fields is a finding, not a crash. A recipe callout not in first-position-of-section is a v1 finding (convention, not grammar).
- **span rule**: recipe body = lines after the callout until `> [!skw] end` (stripped) or the next ATX heading. `end` with no open body = finding.
- **compile normalization**: dropping a callout also drops one adjacent blank line so output has no double-blank scars; pinned by test, deterministic.
- **build semantics**: for each src file — refresh `copy` bodies in src (write src only when changed), compile, write target (src is truth; an existing divergent target is simply overwritten — check exists to warn first), update `lock.json`. Report per file: `built` / `unchanged`, plus src refreshes.
- **settings**: `.skillware/skillware.json`, v1 keys: `{"depots": ["<path relative to skill root>", ...]}` for `Dotted.Name` resolution via `agentos.index.model.parse_depot`. Missing file = no depots.
- **CLI surface**: `agentos skillware <build|check|status> --skill <path> [--json]`; `check` exits non-zero on findings; `status` is the inventory (managed files, verbs, lock presence). Registered in `agentos-cli/src/agentos_cli/cli.py` beside the other `register_*_commands`.
- **POC `agentos-index2`** (`agentos-md/skills/agentos-index2/`): a do-over of `agentos-index` on a representative subset, marked POC in its SKILL.md.
  - `references/search.skw.md` — recipe-free src (pure passthrough proves the noop case)
  - `references/ground.skw.md` — the full demo: `copy` of `references/search.skw.md#Citation Behavior`; `derived` with two deps (`references/search.skw.md#Search Model` + bare `Context.Grounding` from the agentos-pkg depot) and an intent; one `[!skw] end` mixed section with a hand tail
  - `references/gr-survey.md` — hand-owned, no src (absence = hand-owned)
  - `SKILL.md` — hand-owned POC banner + module table
  - `.skillware/skillware.json` — depots: `["../agentos-pkg"]`
  - content adapted from the real `agentos-index` modules so the dependencies are meaningful, not lorem
- **583 supersession**: delete `src/agentos/skills/imports.py`, `tests/test_skills_imports.py`, the `imports` subparser + handler in `agentos/skills/commands.py`; delete `skills/agentos-pkg/build/references-index-block-catalog-imports.md` and `skills/agentos-index/build/references-ground-imports.md` (empty `build/` dirs go too); rewrite `agentos-skill-pkg-builder` `references/imports.md` → `references/skillware.md` (src/recipe format, points at the CLI) and `references/import-checks.md` → `references/skillware-checks.md` (step 0 = `agentos skillware check`; agentic pass = re-derive stale `derived` bodies in src); update `check.md`, `build.md`, `SKILL.md` rows/args accordingly; update `agentos-py/AGENTS.md` (drop the `skills imports` entry, add `skillware`).
- **index follow-up (not executed here)**: 107's `Module.Import`/`Import.Manifest`/`Import.Management` realization lines describe the removed mechanics; a design session should recast them over Skillware. Recorded as follow-up, index untouched.

### Current.State *(inspected)*

- `agentos skills imports` + `agentos.skills.imports` + `tests/test_skills_imports.py` landed yesterday (583), all uncommitted in `agentos-py`; the two live import manifests and builder-skill import references landed uncommitted in `agentos-md`.
- CLI aggregation: `agentos-cli/src/agentos_cli/cli.py` imports `register_*_commands` and calls them over one `subparsers` (skills at line 75).
- depot parsing: `agentos.index.model.parse_depot` + `BlockHeading`/`KernelLine` — the yesterday pattern for block-body extraction is in `agentos/skills/imports.py` (`_resolve_target`) and can be lifted before that module is deleted.
- `agentos-index` real content: `references/search.md` (`## Search Model`, `## Citation Behavior` sections), `references/ground.md` (`## Grounding Model` explicitly derives from `--search`), `references/gr-survey.md` — the POC adapts these.
- `Context.Grounding` block exists: `agentos-md/skills/agentos-pkg/design/107-design.md:315`.
- live-note numbering: 583 is the latest; this artifact is 584.
- tests style: fixture-tree tests as in `tests/test_skills_imports.py` / `test_index_blocks.py`.

## Execution.Plan

*(test-first; fixture: a skill tree with `.skillware/src/` holding one recipe-free src, one src with copy + multi-dep derived + end-marker mixed section; a hand-owned file; a fixture depot with one concept block; `skillware.json` pointing at it)*

### S1 — src parsing (model)
- what: `model.py` — `SkwRecipe` (verb, froms, intent, heading, line), `SkwSrcFile` (segments: prose spans, recipe callouts, produced bodies, end markers); `parse_skw_source(text)`
- RED: unit tests — callout detection (`[!skw]-` and `[!skw]`), verbs, repeated `from:`, quoted intent continuation, body span to heading vs to `end`, unknown verb → finding, `end` without body → finding, non-first-position recipe → finding
- check: suite green
- status: done

### S2 — locators + expansion + compile
- what: `build.py` — locator resolution (src-root/skill-root paths, region body extraction, `.skw.md` recursive expansion with cycle chain error, `Dotted.Name` via depots), `compile_src` (strip machinery + blank-line normalization)
- RED: unit tests — region body excludes heading and includes subsections; whole-file locator; depot block body; missing target / missing region / no-depot findings; cycle error names the chain; compile output byte-pinned for the fixture
- check: suite green
- status: done

### S3 — build + lock + check
- what: `build_skill(root)` (refresh copy bodies in src, emit targets, write `.skillware/lock.json`), `check_skill(root)` with the six verdicts (`never-built`, `stale-build`, `hand-edited`, `copy-drift`, `derived-stale`, `ok`) + recipe/locator findings
- RED: unit tests — build then check = all ok; edit target → `hand-edited`; edit src prose → `stale-build`; edit copy target → `copy-drift` and build repairs src; edit derived dep → `derived-stale`; no lock → `never-built`
- check: suite green
- status: done

### S4 — CLI + registration
- what: `commands.py` — `agentos skillware build|check|status --skill <path> [--json]`, findings-style report, check exits non-zero on findings; register in `agentos-cli/cli.py`; reinstall
- RED: e2e — handler-level tests over the fixture: build report shape, check exit codes and JSON payload, status inventory; `CliError` on a non-skill path
- check: suite green; ruff clean; `agentos skillware --help` live
- status: done

### S5 — POC `agentos-index2`
- what: author the POC skill per Design.Decisions (src files, hand-owned files, settings); run `agentos skillware build` then `check` live; verify compiled `ground.md` matches the design examples' shape; perturb one dep and show `derived-stale`, restore
- check: live `build` emits `search.md` + `ground.md`; `check` all-ok after build; the perturb/restore cycle shows the agentic flag; compiled files contain zero skillware machinery
- status: done

### S6 — 583 supersession + docs
- what: the removals and builder-skill re-route listed in Design.Decisions; `agentos-py/AGENTS.md` update; reinstall; full suites both repos' relevant checks
- check: `agentos skills imports` no longer parses; no `*-imports.md`, no `agentos.skills.imports`, no stale mentions outside `notes/live/` provenance; agentos-py suite green; ruff clean on touched files
- status: done

### Acceptance signals
- `agentos skillware build/check/status` run live over `agentos-index2`; compiled surfaces carry zero machinery
- the six check verdicts are each observable in tests; `derived-stale` demonstrated live on the POC
- the 583 import system is fully gone; the builder skill speaks skillware
- `No.Regression.Tests.Allowed`; index linter and existing `agentos skills` subcommands untouched

### Risks / deviation triggers
- if callout parsing collides with legitimate quoted content, tighten the match to exact `[!skw]` first-lines only and add an escape note to the builder reference — never guess about ambiguous blockquotes (finding instead)
- if `Dotted.Name` depot resolution needs more than block-body kernel lines (meta, sections), keep v1 to kernel-line bodies and record the limit
- if the POC do-over content drifts too far from real `agentos-index` doctrine, prefer faithful-but-trimmed adaptations over invention; the POC is a demo, not a replacement (agentos-index stays canonical)
- if blank-line normalization proves ambiguous, pin the simplest rule the tests can state and record it

## Impl.Log

- **derived blessing rule (open-space decision)**: `build` keeps a derived recipe's old dependency hashes in the lock while its body hash is unchanged — a rebuild can never silently clear `derived-stale`; only an actual re-derive (body change) re-blesses. Pinned by test.
- **copy uses its first `from:` only** for splicing (extra `from:` lines hash as dependencies but do not splice); multi-from splicing semantics deferred.
- **checkpoint deviation (agentos-cli)**: the registration edit and its checkpoint landed in one commit (`chore: checkpoint before 584 skillware registration`) instead of checkpoint-then-edit; the repo was clean before, so the pre-edit state is the parent commit.
- **live acceptance (S5)**: `agentos-index2` — build compiled `search.md` + `ground.md`, materialized the copy placeholder into src; check all-ok; perturbing `search.skw.md#Search Model` flagged `derived-stale` on ground's `Grounding Model` and `stale-build` on `search.md`; restore → clean. Compiled surfaces carry zero `[!skw]` machinery.
- **S6 counts**: agentos-py suite 303 passed (5 imports tests removed, 13 skillware tests added); ruff clean on touched files; `agentos skills imports` now rejects as invalid choice; no `build/*-imports.md` or `build/derivation/` remain.
- **known stale index line (declared out of scope)**: `107-design.md:99` (`Import.Manifest` flat-rule realization) describes the removed 583 mechanics — follow-up design session should recast the 107 Skillware cluster (`Module.Import`, `Import.Manifest`, `Import.Management`) over Skillware.
