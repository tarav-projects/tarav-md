---
name: agentos-skill-pkg-builder
description: "Workflow-neutral Package.Aux.Skill for the Skill.Package.Builder subsystem of agentos-pkg — the build toolchain that maintains a skill package's Skill.Runnable.Surface from its Skillware src surface. USE WHEN building or checking Skillware-managed content across a skill package's surfaces, or when authoring .skw.md sources and recipes."
---

# agentos-skill-pkg-builder

Workflow-neutral `Package.Aux.Skill` for the `Skill.Package.Builder` subsystem.

This skill is the public Batchy router for build work on a skill package. It orients the caller to the build subsystem by default and routes explicit operations such as `--build` and `--check` into named `Skill.Module`s.

This is a `Batchy.Skill`. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and the public args without running.

## Skill.Index.Section

### Skill.Package.Builder
- the support system for developing and maintaining a skill package's `Skill.Runnable.Surface`
- a bundle of agentic skills and CLI support tooling that run build workflows over the package
- canonical definition: `agentos-pkg` index `Skill.Package.Builder` (`Cited.Duplication`)

### Skillware
- the skill-development compilation system: runnable files are produced from `.skillware/src/**/*.skw.md` sources — markdown plus `[!skw]` callout recipes
- recipe bindings: `copy` (CPU-refreshed verbatim body) and `derived` (agent-authored solution kept in src); absence of a src file = hand-owned
- `agentos skillware build/check/status` is the deterministic toolchain; drift is tracked in `.skillware/lock.json`
- format and discipline: `references/skillware.md`

## Skill.Arg.Section

### Skill.Arg:Check
- the umbrella check runner — run every registered check over the package and aggregate, read-only
- required: false
- action: load `references/check.md`
- help: "run all drift checks (skillware + inline), no writes"
- examples: --check, --check --skill skills/agentos-index2

### Skill.Arg:Skillware.Checks
- run only the Skillware checks — do the managed surfaces still hold?
- required: false
- action: load `references/skillware-checks.md`
- help: "CPU drift verdicts + agentic re-derive of stale derived bodies"
- examples: --skillware-checks, --skillware-checks --skill skills/agentos-index2

### Skill.Arg:Inline.Drift
- run only the inline-drift check — does any surface contradict or go stale against a concept it mentions?
- required: false
- action: load `references/inline-drift.md`
- help: "find surfaces that contradict a concept they cite"
- examples: --inline-drift --target Hard.Evidence

### Skill.Arg:Build
- compile the package's Skillware sources and reconcile drift
- required: false
- action: load `references/build.md`
- help: "build compiled surfaces from .skillware/src sources"
- examples: --build, --build --skill skills/agentos-index2

### Skill.Arg:Skill
- the coarse scope — which skill surface to operate on
- required: false
- help: "limit the run to one skill"
- examples: --skill hugentics-designer, --skill agentos-index2

### Skill.Arg:Target
- the fine scope within a skill — a file path or a block/concept name
- required: false
- help: "limit the run to one file or block"
- examples: --target references/ground.md, --target Hard.Evidence

## Boundary

- this skill is the public entry surface for the `Skill.Package.Builder` subsystem of a skill package
- it remains a `Workflow.Neutral.Skill` when no explicit arg is selected
- it routes into named modules for concrete build operations instead of separate public skills
- it never builds a surface from scratch — it maintains relations between existing surfaces
- later capabilities (tests, lint, lineage) may be added as modules without changing the public entry surface

## Router Table

| Situation | Module / Surface |
|---|---|
| run all drift checks over the package (read-only) | `references/check.md` |
| check Skillware-managed surfaces for drift | `references/skillware-checks.md` |
| find surfaces that contradict a concept they mention | `references/inline-drift.md` |
| compile or reconcile Skillware sources | `references/build.md` |
| author or understand `.skw.md` sources and recipes | `references/skillware.md` |
| canonical subsystem concepts (`Skill.Package.Builder`, `Skill.Build.Surface`, `Module.Import`, `Derivation.Rule`, `Derived.Content`) | `agentos-pkg` index `107-design.md` |

## Builder Operating Behavior

- all authoring happens on the src surface — never edit a compiled file; the compiled surface carries zero machinery
- `agentos skillware build/check` is the deterministic CPU layer — take its verdicts as given; the agentic work is re-deriving stale `derived` bodies in src
- a failed check is a drift finding with no predefined winner — resolution is case-by-case; a particular workflow may set auto-regeneration as its own rule
- writing src for a gated package still follows the package's edit gates — propose, get approval, then re-derive and rebuild
- `--inline-drift` asserts only non-contradiction — a mention may rephrase, simplify, or scope a concept; it just may not contradict the canonical definition
- inline-drift output is candidates for judgment, never verdicts — it has no rule for how a surface should restate a concept, so it never reconciles

## Skill Modules

- `references/check.md` — the umbrella check runner: run every check, aggregate, no writes
- `references/skillware-checks.md` — Skillware drift: CPU verdicts + the agentic re-derive pass
- `references/inline-drift.md` — inline-drift: find surfaces that contradict a concept they mention
- `references/build.md` — the compile/reconcile pass over `.skillware/src` sources
- `references/skillware.md` — the src surface, the recipe format, and the toolchain

## When To Load This Skill

- when building or checking Skillware-managed content across a skill package's surfaces
- when authoring or maintaining `.skw.md` sources and recipes
- when adding a build capability (tests, lint, lineage) to a package
