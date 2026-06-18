---
name: hugentics-codebase-cleaner
description: Improve a git-tracked codebase in place by scanning for targeted cleanup refactors, producing an Impl.Req via hugentics-impl-designer, and executing it via hugentics-impl-executer in Alignment.Mode:Autonomous after one user confirmation. USE WHEN the user wants the agent to simplify code, reduce duplication, address repeated-knowledge or DRY violations, remove poor abstractions, centralize repeated knowledge, tighten boundaries, or generally clean up a repository after implementation.
---

# Hugentics Codebase Cleaner

Improve the current repository directly. Do not stop at an audit unless blocked. The default outcome is edited code plus a short summary of the changes and rationale.

This is an operational `Package.Aux.Skill` under `agentos-pkg`.

Default assumption: backward compatibility is not a goal unless the user explicitly asks for it. If an old abstraction, interface, or implementation should be replaced, replace it instead of preserving it behind compatibility layers.

This is a `Batchy.Skill` — called like a terminal command. Load `agentos-batchy-skills` for the full convention.

- `-h` / `--help` prints usage and exits without running (`Batchy.Skill.Help`).
- every run prints a banner of the resolved arguments as its first step (`Batchy.Skill.Banner`).
- supplied flags resolve to the `Skill.Arg` names below; a bare path is `--codebase`.

## Skill.Arg.Section

### Skill.Arg:Target.Codebase
- the git-tracked repository to clean in place
- required: false
- default: the current repository
- help: "the repository to clean"
- examples: --codebase "./my-repo"

### Skill.Arg:Alignment.Mode
- whether the agent prompts at each `Alignment.Checkpoint` or resolves them itself and runs end-to-end
- here, `Interactive` keeps cleanup's single boundary confirmation of the `Impl.Req`; `--AUTO` skips it
- required: false
- default: Interactive
- type: switch
- help: "run autonomously instead of prompting at checkpoints"
- examples: --AUTO
- detail: `agentos-hugentics/references/alignment-session.md`

## Cleanup Model

Use these dimensions internally to decide what to improve:

- repeated knowledge: centralize constants, paths, config keys, branching rules, and helper logic when the shared form is clearer.
- DRY: remove repeated code when the shared abstraction is clearer than the duplication.
- Design clarity: reduce boundary leakage, unclear ownership, needless indirection, and dead layers.
- Maintainability: improve naming, file organization, API shape, error handling, and local complexity.
- Safety: prefer small and reversible refactors over speculative rewrites.

Only act on changes that improve the repo under its current architecture. Respect existing style and conventions, but treat public interfaces as replaceable unless the user explicitly asks for backward compatibility.

## Workflow

Cleanup is a two-stage hugentic flow: scan + scope here, then hand off to `hugentics-impl-designer` and `hugentics-impl-executer` for the design + execution. Cleanup owns a single boundary confirmation as its own declared `Alignment.Checkpoint`: it presents the `Impl.Req` for one user confirmation, then runs design and execution in `Alignment.Mode:Autonomous` (see `agentos-hugentics/references/alignment-session.md`).

### 1. Prepare the working tree (always, first)

- This step runs unconditionally. It is not gated on whether "obvious" cleanup work exists, and it is not subject to evaluation. A cleanup run starts by getting the tree clean — every time.
- Run `git status`. If dirty:
  - Commit existing changes as one or more coherent commits with accurate messages, grouping related edits.
  - When boundaries are unclear, use one explicit `chore: pre-cleanup checkpoint` commit rather than guessing at history.
- If the repo is not a git repo, has unresolved conflicts, or commits cannot be made safely, stop and surface the concrete blocker.
- The executer's own pre-execution checkpoint runs later as an additional rollback marker — it does not replace this step.

### 2. Reconstruct local context

- Inspect repo structure, primary languages, tooling, and tests.
- Read enough to ground the cleanup choice — do not produce a long findings report.

### 3. Choose a scoped cleanup set

- Pick 1-3 coherent cleanup themes that can be verified together. There is almost always something worth doing — repeated knowledge, dead code, oversized functions, confusing boundaries, bypassed abstractions. Do not invent "no candidate justified" as an exit; pick the highest-ROI target and proceed. Stop only if the repo is empty, structurally unsafe, or genuinely already optimal.
- Avoid broad rewrites, repo-wide renames, or architecture migrations unless the user asked for them.
- Do not exclude code based on how recently it was written. Freshness is not a protected status.

### 4. Produce an Impl.Req via hugentics-impl-designer

- Hand off the scoped cleanup set to `hugentics-impl-designer` and produce an `Impl.Req`.
- The `Impl.Req` lives in the **cleaned project's** `notes/live/`, not the invoker's. Use `agentos-live-surfaces` for naming and numbering.
- Carry over cleanup's constraints into the `Impl.Req`: stay narrow, prefer module-local helpers, no new frameworks, replace obsolete interfaces rather than wrap them.
- Run the designer in `Alignment.Mode:Autonomous`: the loop runs without prompting and produces the `Impl.Req`.
- Present the produced `Impl.Req` to the user for one confirmation — cleanup's own boundary `Alignment.Checkpoint` — before execution.

### 5. Execute via hugentics-impl-executer

- Hand the user-confirmed `Impl.Req` to `hugentics-impl-executer` in `Alignment.Mode:Autonomous`.
- The executer owns the mandatory pre-execution checkpoint commit (the rollback floor and the only commit phase) and the deviation contract.
- For cleanup, a deviation that would reshape the design or broaden scope is a hard boundary — abort the autonomous run and surface to the user; cleanup never silently broadens its own scope.

### 6. Validate (per slice and at completion)

- Slice-level verification is part of the executer's per-slice loop.
- At completion, run the narrowest relevant verification for the cleaned areas: tests, linters, type checks, build steps, or focused commands.
- If verification cannot be run, say so explicitly.

### 7. Finish

- Summarize what changed, why it was worth doing, what verification ran, and any remaining risk.
- Cite the `Impl.Req` location and the checkpoint commit so the user has the audit trail and rollback handle.

## Constraints

- Do not produce a long findings report before acting unless the user explicitly asks for one.
- Do not touch unrelated files just because they look messy.
- Do not replace understandable duplication with an abstraction that is harder to read.
- Do not introduce new frameworks or cross-cutting patterns just to clean up local code smells.
- Prefer module-local helper extraction before creating broad utility layers.
- Do not spend effort preserving backward compatibility by default. Replace outdated interfaces cleanly when reimplementation is the better design.
- If the repository state is unsafe for automatic work, stop early with a concrete explanation.

## Response Shape

After the cleanup work, respond with a concise summary that includes:

- what you changed
- why those changes were chosen
- what verification ran
- the `Impl.Req` path and the checkpoint commit details (rollback handle)
