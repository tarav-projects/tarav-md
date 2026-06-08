---
name: hugentics-codebase-cleaner
description: Improve a git-tracked codebase in place by scanning for targeted cleanup refactors, producing an Impl.Req via hugentics-impl-designer, and executing it via hugentics-impl-executer in Alignment.Mode:Gated. USE WHEN the user wants the agent to simplify code, reduce duplication, address repeated-knowledge or DRY violations, remove poor abstractions, centralize repeated knowledge, tighten boundaries, or generally clean up a repository after implementation.
---

# Hugentics Codebase Cleaner

Improve the current repository directly. Do not stop at an audit unless blocked. The default outcome is edited code plus a short summary of the changes and rationale.

This is an operational `Package.Aux.Skill` under `agentos-pkg`.

Default assumption: backward compatibility is not a goal unless the user explicitly asks for it. If an old abstraction, interface, or implementation should be replaced, replace it instead of preserving it behind compatibility layers.

## Cleanup Model

Use these dimensions internally to decide what to improve:

- repeated knowledge: centralize constants, paths, config keys, branching rules, and helper logic when the shared form is clearer.
- DRY: remove repeated code when the shared abstraction is clearer than the duplication.
- Design clarity: reduce boundary leakage, unclear ownership, needless indirection, and dead layers.
- Maintainability: improve naming, file organization, API shape, error handling, and local complexity.
- Safety: prefer small and reversible refactors over speculative rewrites.

Only act on changes that improve the repo under its current architecture. Respect existing style and conventions, but treat public interfaces as replaceable unless the user explicitly asks for backward compatibility.

## Workflow

Cleanup is a two-stage hugentic flow: scan + scope here, then hand off to `hugentics-impl-designer` and `hugentics-impl-executer` for the design + execution. The default `Alignment.Mode` for the handoff is `Gated` (see `agentos-hugentics/references/alignment-session.md`): one user confirmation at the `Impl.Req` boundary, then autonomous execution.

### 1. Reconstruct local context

- Inspect repo structure, primary languages, tooling, tests, and `git status`.
- Identify a small set of high-value cleanup candidates.
- If nothing is clearly worth changing, stop and say that no cleanup was justified.

### 2. Choose a scoped cleanup set

- Prefer 1-3 coherent cleanup themes that can be verified together.
- Prioritize repeated knowledge, bypassed abstractions, dead code, oversized functions, and confusing module boundaries.
- Avoid broad rewrites, repo-wide renames, or architecture migrations unless the user asked for them.

### 3. Produce an Impl.Req via hugentics-impl-designer

- Hand off the scoped cleanup set to `hugentics-impl-designer` and produce an `Impl.Req`.
- The `Impl.Req` lives in the **cleaned project's** `notes/live/`, not the invoker's. Use `agentos-live-surfaces` for naming and numbering.
- Carry over cleanup's constraints into the `Impl.Req`: stay narrow, prefer module-local helpers, no new frameworks, replace obsolete interfaces rather than wrap them.
- Run the designer in `Alignment.Mode:Gated`: the loop runs autonomously, then the `Impl.Req` is presented for one user confirmation before execution.

### 4. Execute via hugentics-impl-executer

- Hand the approved `Impl.Req` to `hugentics-impl-executer` in `Alignment.Mode:Gated`.
- The executer owns the mandatory pre-execution checkpoint commit (rollback floor), per-slice commits, and the deviation contract.
- A `Gated`-mode deviation that requires reshaping the design or expanding scope aborts back to the user — cleanup never silently broadens its own scope.

### 5. Validate (per slice and at completion)

- Slice-level verification is part of the executer's per-slice loop.
- At completion, run the narrowest relevant verification for the cleaned areas: tests, linters, type checks, build steps, or focused commands.
- If verification cannot be run, say so explicitly.

### 6. Finish

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
