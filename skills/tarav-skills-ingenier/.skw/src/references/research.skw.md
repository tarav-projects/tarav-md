> $kw: ^skill-research-direct-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^skills-ingenier-batchy-runtime-contract

# Skill.Research.Operation.Module

Use this read-only module to audit an existing skill or mine a focused evidence set for a new one. It changes context, not the target.

## Target Inspection

1. Resolve `Skill.Arg::Target.Skill`; when several targets remain plausible, ask rather than choose.
2. Read the target's owning `AGENTS.md` before inspecting project-local surfaces.
3. Determine whether the target is new, hand-managed, or Skillware-managed. For Skillware, treat `.skw/src/` as source and compiled runnable files as products.
4. Inspect the trigger, boundary, arguments, router, modules, commands, references, scripts, assets, metadata, tests, and current validation state that matter to the request.
5. Preserve unrelated worktree changes and distinguish target defects from repository-wide issues.

## Source Selection

- read `references/source-registry.md` first as a menu, not as a crawl order
- read `references/custom-recommendations/README.md` and applicable recommendations early
- add `Skill.Arg::Sources` supplied by the caller
- for Agentos skills, prefer current `tarav-pkg`, `tarav-batchy-skills`, `tarav-skillware`, relevant maintained local skills, and target-local guidance over historical Agentos copies
- select the smallest evidence set that can answer the active question; browse externally only when local and user-provided evidence is insufficient or the caller requests it
- follow symlinks when traversing installed skill depots

## Mining Pass

Classify each high-signal finding twice:

- decision: `adopt`, `adapt`, or `avoid`
- artifact: instruction, reference, script, asset, workflow, agent, command, router row, or module

Distinguish reusable design from source-specific wording. Prefer complete working patterns, explicit trigger boundaries, progressive disclosure, deterministic validation, and honest source dependencies. Treat prompt theater, arbitrary constraints, and copied product machinery as weak evidence.

Read `references/mining-rubric.md` when findings must be ranked or mapped into a concrete target stack.

## Report

Return only what advances the task:

- current target model and material POIs
- sources actually used and why
- high-signal `adopt` / `adapt` / `avoid` findings
- uncertainties or conflicts that affect the design region
- the single best next move: stop, design, develop, or evaluate

Do not edit, build, bless, or otherwise mutate the target from this module.
