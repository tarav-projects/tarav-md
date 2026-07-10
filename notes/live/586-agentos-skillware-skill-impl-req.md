# agentos-skillware Skill — Impl.Req

## Impl.Abstract

- **Goal**: create `agentos-md/skills/agentos-skillware` — the center of all Skillware content: doctrine, language spec, authoring discipline, adoption playbook, and toolchain operation — absorbing and retiring `agentos-skill-pkg-builder`. The skill is itself Skillware-built. Plus one engine addition: `agentos skillware build` constitutively stamps `.skillware/AGENTS.md`.
- **Design source**: this session's aligned design (2026-07-10): module set, 3-arg public surface, five derived recipes, constitutive AGENTS.md (grounded `^20260710-3`, appendix `Skill.Build.Surface/Appendix`), index recast already landed (`Skillware.Recipe`, `^20260710-2`).
- **Self-containment contract**: an agent loading only this skill has everything needed to be a competent Skillware user.
- **Out of scope**: `inline-drift` (dropped — future test-engine redesign owns it); `pointer` binding tooling; any further index edits beyond mention sweeps.
- **Repos**: `agentos-py` (engine + tests), `agentos-md` (the skill, the retirement, index2 provenance cleanup).
- **Status**: designed 2026-07-10 — ready for execution

## Impl.Index

### Design.Decisions

- **public surface: 3 args** — `--about` (aliases `--info`, `--doctrine`): orientation, doctrine, language questions; `--dev`: authoring, adoption, building — the write side; `--check`: read-only drift report that also *prescribes* per-verdict responses; acting on the report is a follow-up user prompt into `--dev`. The router absorbs granularity per `Semantic.Router` — the agent selects the module from context.
- **modules (7 files)**: `SKILL.md` + `references/{doctrine,lang,author,adopt,build,check}.md`
  - `doctrine.md` — what Skillware is; self-contained `Cited.Duplication` of the 107 cluster
  - `lang.md` — canonical *operational* spec: recipe grammar, verbs, field lines, body/end rules, locators (`path#Region`, `Dotted.Name`), recursive expansion + cycle rule, `skillware.json`, src-tree mirroring, hand-owned-by-absence
  - `author.md` — roots vs derived consumers, `intent:` craft, graph discipline (real span relations only; one-liners stay `Inline.Relatedness`; no forced copies)
  - `adopt.md` — converting an existing skill: inventory, parity contract, graph extraction, verify (the 585 playbook, generalized)
  - `build.md` — `build`/`status` mechanics, lock model, src copy-refresh
  - `check.md` — verdict vocabulary + what each demands (copy refresh / agentic re-derive in src / hand-edit reconciliation), no-silent-blessing, read-only boundary
- **Skillware-built**: `.skillware/skillware.json` depots `["../agentos-pkg"]`; five `derived` recipes, zero copies:
  1. `doctrine#The Model` ← `Agentos.Skillware` + `Skill.Runnable.Surface` + `Skill.Build.Surface` + `Module.Import` + `Skillware.Recipe` + `Derivation.Rule` + `Derived.Content`
  2. `doctrine#Recipe In Brief` ← `references/lang.skw.md#Recipe Grammar` (one-paragraph digest)
  3. `author#Division Of Labor` ← `Import.Management` (the `[PR]` + realization lines)
  4. `check#Verdicts` ← `Import.Management` (same block, the verdict/no-silent-blessing side)
  5. `SKILL#What Skillware Is` ← `Agentos.Skillware` (orientation blurb)
  - everything else root; router table hand-written (rows are one-liners, not spans)
- **absorption**: fold the still-current content of `agentos-skill-pkg-builder/references/{skillware,skillware-checks,build,check}.md` into `lang`/`check`/`build`; `inline-drift.md` content is dropped, not migrated; then **delete `skills/agentos-skill-pkg-builder/` entirely** (`No.Legacy.Allowed`).
- **skill links**: skills are symlinked via `agentos skills import` (state in `.agentos/state/skills-routing-links.json`, links in `.claude/skills/`); after create+delete, re-run the import for affected projects (agentos-md, agentos-py) and verify the old link is gone, the new one resolves.
- **engine — constitutive `.skillware/AGENTS.md`**: `build_skill` (agentos-py `src/agentos/skillware/build.py:342`) writes a canonical constant text to `<skill>/.skillware/AGENTS.md`, overwrite-always, engine-owned like `lock.json`. Content (~6 lines): build surface identification; targets are compiled from `src/` — never hand-edit; edit src then `agentos skillware build`; drift via `agentos skillware check`; this file + lock are engine-owned; load `agentos-skillware` for the discipline. `check`/`status` do not require it (old builds tolerated), build always (re)stamps it.
- **index2 provenance cleanup**: remove the two provenance additions from `agentos-index2/.skillware/src/SKILL.skw.md` (description prefix + provenance line), rebuild → index2 reaches zero-delta parity ("keep the execution surface clean", user 2026-07-10).
- **grounding**: the design decisions of this artifact are grounded on this session; key anchors `^20260710-2` (recast + skill decision), `^20260710-3` (constitutive AGENTS.md).

### Current.State *(inspected)*

- `skills/agentos-skill-pkg-builder/`: SKILL.md + references/{build,check,inline-drift,skillware-checks,skillware}.md — all 584-current except inline-drift (older, being dropped).
- Engine: `agentos.skillware.{model,build,commands}` green (13 tests in `agentos-py/tests/test_skillware.py`); `build_skill` at build.py:342 writes target files + lock — the AGENTS.md stamp slots beside the lock write.
- 107 index: recast landed this session (`Skillware.Recipe` block, realization lines, `[PR]` division of labor, `Skill.Build.Surface[+1]` appendix).
- index2: 12 Skillware-managed surfaces, all-ok, SKILL.md carries the 2-line provenance delta.
- Builder-skill links: `.claude/skills/agentos-skill-pkg-builder` symlink in agentos-md (and agentos-py state json); no other live references outside notes (historical) and chatlas snapshots.
- Next live note number: 586.

## Execution.Plan

### S1 — engine: constitutive AGENTS.md (agentos-py)
- what: RED test — build a tmp skill, assert `.skillware/AGENTS.md` exists with canonical content and that a hand-modified copy is overwritten by rebuild; GREEN — `AGENTS_MD_TEXT` constant + stamp in `build_skill`; run full skillware test file + ruff
- check: new tests pass; suite green
- status: pending

### S2 — author agentos-skillware (agentos-md)
- what: src tree — `.skillware/skillware.json`, `src/SKILL.skw.md`, `src/references/{doctrine,lang,author,adopt,build,check}.skw.md` with the five recipes; build; check
- check: `agentos skillware build --skill skills/agentos-skillware` emits 7 files + AGENTS.md; `check` exit 0 all-ok; derived bodies faithful to their index sources
- status: pending

### S3 — retire agentos-skill-pkg-builder + link sweep
- what: delete `skills/agentos-skill-pkg-builder/`; re-run `agentos skills import` for agentos-md and agentos-py; sweep remaining live mentions (excluding notes/chatlas history)
- check: old symlink+state gone, `agentos-skillware` linked and resolvable via `agentos skills path`; no live-surface mentions remain
- status: pending

### S4 — index2 zero-delta + final verification
- what: drop provenance additions from index2 `SKILL.skw.md`, rebuild index2; final pass — pytest (agentos-py), skillware build/check/status over index2 + agentos-skillware, index linter over agentos-pkg, parity diff for index2 SKILL.md now empty
- check: all green; index2 SKILL.md parity diff byte-empty modulo name
- status: pending

### Acceptance signals
- an agent can load `agentos-skillware` and operate the whole system: understand (doctrine/lang), write (author/adopt/build), maintain (check)
- the skill's own `check` is all-ok and its doctrine derives from the live 107 blocks
- every fresh `agentos skillware build` leaves a canonical `.skillware/AGENTS.md`
- `agentos-skill-pkg-builder` is gone from skills, links, and state

### Risks / deviation triggers
- if a derived body cannot faithfully digest its index sources without inventing content, keep it minimal and state the weaker derivation in the intent
- if `agentos skills import` selection config names the builder explicitly, update the selection source rather than hand-editing state
- if deleting the builder breaks a `.claude/skills` reference in an unrelated project, record it in Impl.Log and fix forward

## Impl.Log

*(empty — written during execution)*
