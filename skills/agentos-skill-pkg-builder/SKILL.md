---
name: agentos-skill-pkg-builder
description: "Workflow-neutral Package.Aux.Skill for the Skill.Package.Builder subsystem of agentos-pkg — the build toolchain that maintains a skill package's Skill.Runnable.Surface from its Skill.Build.Surface. USE WHEN building or checking derived content across a skill package's surfaces, or when authoring derivation manifests."
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

### Skill.Build.Surface
- the builder's workspace — a per-package `build/` folder of build-time material, never loaded at run time
- `build/derivation/` holds derivation manifests; tests, lint, lineage get their own sub-areas

### Derivation.Rule
- a relation `Dependencies + Context → Derived` — keeps a derived span in sync with its source
- written soft, `Index.Block`-style: it carries the relation plus the context a smart builder needs, not a character-precise spec
- op vocabulary, by how much the source is reshaped: `copy` (verbatim), `projection` (a structural part), `transform` (reshaped by intent)

## Skill.Arg.Section

### Skill.Arg:Check
- the umbrella check runner — run every registered check over the package and aggregate, read-only
- required: false
- action: load `references/check.md`
- help: "run all drift checks (manifest + inline), no writes"
- examples: --check, --check --target references/index-block-catalog.md

### Skill.Arg:Manifest.Checks
- run only the declared-rule checks — do the `Derivation.Rule`s in the manifests still hold?
- required: false
- action: load `references/manifest-checks.md`
- help: "check declared derivation rules for drift"
- examples: --manifest-checks, --manifest-checks --manifest build/derivation/catalog.md

### Skill.Arg:Inline.Drift
- run only the inline-drift check — does any surface contradict or go stale against a concept it mentions?
- required: false
- action: load `references/inline-drift.md`
- help: "find surfaces that contradict a concept they cite"
- examples: --inline-drift --target Hard.Evidence

### Skill.Arg:Build
- make the package's derived content match its sources — run the manifest relations forward and reconcile drift
- required: false
- action: load `references/build.md`
- help: "build/reconcile derived content from its sources"
- examples: --build, --build --target references/index-block-catalog.md

### Skill.Arg:Skill
- the coarse scope — which skill surface to operate on
- required: false
- help: "limit the run to one skill"
- examples: --skill hugentics-designer, --skill agentos-index

### Skill.Arg:Target
- the fine scope within a skill — a file path or a block/concept name
- required: false
- help: "limit the run to one file or block"
- examples: --target references/index-view.md, --target Hard.Evidence

### Skill.Arg:Manifest
- scope a manifest run to one manifest file (manifest-checks / build)
- required: false
- help: "limit the run to a single manifest"
- examples: --manifest build/derivation/catalog.md

### Skill.Arg:Since
- the inline-drift window — how far back the recent-changes default target reaches
- required: false
- default: ~2-3 weeks
- help: "set the recent-changes window for inline-drift (date or git ref)"
- examples: --since 3.weeks, --since HEAD~20

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
| check declared derivation rules for drift | `references/manifest-checks.md` |
| find surfaces that contradict a concept they mention | `references/inline-drift.md` |
| run or reconcile derived content from its sources | `references/build.md` |
| author or understand derivation manifests and the rule format | `references/derivation.md` |
| canonical subsystem concepts (`Skill.Package.Builder`, `Skill.Build.Surface`, `Derivation.Rule`, `Derived.Content`, `Derivation.Manifest`) | `agentos-pkg` index `107-design.md` |

## Builder Operating Behavior

- the builder is agentic and smart — derivation rules are soft; resolve target spans by reading the runnable surface, not by markers planted in it
- never add bookkeeping noise to a `Skill.Runnable.Surface` — addressing lives on the build side, expressed over the surface's own structure (headings, code fences, `Dotted.Name`s)
- load all manifests in `build/derivation/` and run every rule; narrow with `--skill` (coarse) or `--target` (fine)
- one owner per target span — if two rules claim the same span, report the collision instead of guessing
- `--check` is read-only and reports drift; `--build` reconciles declared rules with common sense, preserving surrounding hand-written content
- `--inline-drift` asserts only non-contradiction — a mention may rephrase, simplify, or scope a concept; it just may not contradict the canonical definition
- inline-drift output is candidates for judgment, never verdicts — it has no rule for how a surface should restate a concept, so it never reconciles
- writing to a runnable surface is gated like any package edit — propose, get approval, then reconcile

## Skill Modules

- `references/check.md` — the umbrella check runner: run every check, aggregate, no writes
- `references/manifest-checks.md` — declared-rule drift: report `Derivation.Rule`s that no longer hold
- `references/inline-drift.md` — inline-drift: find surfaces that contradict a concept they mention
- `references/build.md` — the build/reconcile pass: load manifests, resolve targets, write derived content
- `references/derivation.md` — the derivation manifest format, the op vocabulary, and the worked `Hard.Evidence` example

## When To Load This Skill

- when building or checking derived content across a skill package's surfaces
- when authoring or maintaining derivation manifests
- when adding a build capability (tests, lint, lineage) to a package
