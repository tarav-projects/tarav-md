---
name: agentos-project-doctor
description: Diagnose how well a target folder conforms to the Agentos.Stack project model. Use directly or delegate to a subagent when the user asks for an Agentos doctor pass, project health check, adoption assessment, migration assessment, or wants to evaluate an Agentos.Project target. Suitable for low-reasoning, cost-efficient models because the default task is report-only inspection. Do not fix unless explicitly asked in a follow-up.
---

# Agentos Project Doctor

Diagnosis-first workflow for evaluating how well a concrete `Agentos.Project:<target>` conforms to `Agentos.Stack`.

## Source Model

This skill operationalizes:

- `notes/index/108-Agentos.Project.Doctor.md`
- `notes/index/105-Agentos.Project.md`
- `notes/index/104-Maintenance.System.md`
- `notes/index/001-ontology.md`

If this skill conflicts with `notes/index/`, the index wins and this skill should be updated.

## Trigger Boundary

Use this skill when the user asks to:

- run an Agentos doctor pass
- assess an Agentos project
- check Agentos adoption or migration state
- evaluate whether a target follows `Agentos.Stack`
- inspect project health for Agentos surfaces

Do not use it for fixing findings by default. The doctor reports; fixes require explicit follow-up.

## Delegation Guidance

This skill is suitable for subagent delegation.

Recommended use:

- delegate a bounded doctor pass to a subagent
- give the target path explicitly
- ask for report-only output
- ask the subagent not to edit files
- use a low-reasoning or cost-efficient model when available

Provider-agnostic examples:

- small/mini low-reasoning model
- fast Sonnet-class model
- `gpt-5.4-mini` with low reasoning
- any provider's cheap inspection-oriented model with shell access

Use a stronger model only when the diagnosis depends on difficult design judgment, large migration interpretation, or subtle authority-drift analysis.

## Core Rule

`Agentos.Project.Doctor` does not fix.

The default output is a chat report with findings, evidence, passed checks, skipped checks, and suggested next steps.

`Agentos.Project.Doctor` must follow the optional-surface policy from `notes/index/108-Agentos.Project.Doctor.md`.

Policy baseline:

- `.agentos/project.json` is mandatory for a target evaluated as an `Agentos.Project`.
- `AGENTS.md` should normally exist at the project root.
- `notes/index/`, `notes/live/`, `skills/`, and `dev/live/` are optional by capability adoption.
- Optional surfaces are silent when both the capability and the canonical surface are absent.
- Optional surfaces become reportable when the capability appears through near-standard, overlapping, or off-protocol alternatives.
- Adopted canonical surfaces must satisfy their internal protocol.

## Target Resolution

1. If the user provides a target path, use it.
2. If no target is provided, use the current working directory.
3. State the resolved target in the report.
4. Do not create `.agentos/`, notes, skills, or config during a doctor pass.

## Reference Loading

Load references based on the observed target surfaces and near-standard alternatives.

Always load:

- `references/project-identity.md`
- `references/surface-presence.md`

Load when relevant:

- `.agentos/AGENTS.md` from the target project when it exists.
- `references/index-notes.md` when `notes/index/` exists or the project appears to use an index-like durable design surface.
- `references/ontology-registry.md` when `notes/index/` exists or dotted concepts appear in an index-like durable design surface.
- `references/ontology-registry.md` when integration ontology files, namespace notes, or cross-project concept declarations appear.
- `references/reserved-notes.md` when `notes/live/` exists or a near-standard live TODO/issues note alternative appears.
- `references/numbering.md` when numbered files exist in active Agentos surfaces or in near-standard overlapping alternatives.
- `references/authority-drift.md` when `AGENTS.md`, `skills/`, `notes/live/`, or `notes/index/` exist.
- `references/usage-skill-prompt.md` when `AGENTS.md` exists and the project adopts Agentos skills.

If uncertain, load the relevant reference rather than guessing.

## CLI Use

If `agentos doctor ...` or narrower doctor CLI commands exist, run them when they are relevant and safe.

Current fallback rule:

- If no doctor CLI exists, continue with shell-supported inspection and agentic checks.
- Do not treat missing `agentos doctor` support as a project finding unless the target explicitly claims to require it.

Useful deterministic commands may include:

- `test -f <path>` and `test -d <path>`
- `python3 -m json.tool <file>` for JSON validity
- `find` for numbered files
- `rg` for dotted concepts and authority-drift evidence
- `agentos prefix next --project-base <project-root-basename> --target <surface>` only for allocation context, not as a doctor verdict

## Check Outcome Model

Use these statuses:

- `pass`: the check satisfied the expected condition
- `fail`: violates mandatory identity or an adopted canonical surface's required protocol
- `warn`: likely drift, partial adoption mismatch, overlapping near-standard alternative, or malformed adopted surface
- `info`: useful observation that is not a problem
- `skip`: optional capability is not adopted, or there is not enough evidence to evaluate it
- `unknown`: attempted but inconclusive

Each finding should include concrete evidence.

## Report Format

```md
## Agentos.Project.Doctor Report

Target: ...
Mode: report-only

### Summary

- Status: pass/warn/fail/unknown
- Findings: N
- Checked surfaces: ...

### Findings

#### [severity] Finding title

- Check: ...
- Surface: ...
- Evidence: ...
- Why it matters: ...
- Suggested next step: ...

### Passed Checks

- ...

### Skipped Checks

- ...
```

## Report Guidance

- Keep findings concrete and evidence-backed.
- Do not imply a partial-adoption project is broken just because some Agentos surfaces are absent.
- Distinguish declared adoption, observed adoption, and expected adoption.
- `.agentos/project.json` is mandatory project identity.
- `AGENTS.md` should normally exist at the project root; report its absence as a warning unless the target clearly establishes a different root-guidance convention.
- `notes/index/`, `notes/live/`, `skills/`, and `dev/live/` are optional by capability adoption.
- For optional surfaces, absence alone is not a finding.
- For optional surfaces, warn when the project appears to use that capability through a near-standard, overlapping, or off-protocol alternative instead of the canonical Agentos surface.
- When a canonical optional surface is adopted, enforce its internal protocol.
- Do not write findings titled as missing optional surfaces. Name the actual problem: overlapping alternative, malformed adopted surface, stale reserved file, unnumbered active file, duplicate prefix, range violation, or authority conflict.
- Use `fail` only for strong violations.
- Use `warn` for likely drift or incomplete adoption.
- Use `info` for useful context.
- Include skipped checks when they explain why a surface was not evaluated.

## Initial Check List

The first doctor scope should include these lower-level checks:

- `.agentos/project.json` is mandatory and must parse as valid JSON.
- `.agentos/config.json` is supporting config evidence only; it does not define project identity.
- `AGENTS.md` should normally exist at the project root.
- `notes/index/` is optional by capability adoption.
  - If index-like durable design/reference behavior is absent, no finding.
  - If index-like behavior exists outside `notes/index/`, warn about overlapping or nonstandard alternatives.
  - If `notes/index/` is adopted, missing `notes/index/000-index.md` or `notes/index/001-ontology.md` is a protocol failure.
  - When those reserved index files exist, check whether they appear stale relative to the active index surface.
  - Extra ontology namespace or integration-hook files are valid when routed from `notes/index/001-ontology.md`.
  - If an ontology namespace or integration-hook file exists but `001-ontology.md` does not route to it, treat it as an unrouted/stale ontology surface rather than as a replacement ontology entrypoint.
- `notes/live/` is optional by capability adoption.
  - If absent, no finding.
  - If live-note behavior exists through near-standard alternatives, warn.
  - `notes/live/010.TODOS.md` is optional; if TODO-note behavior exists through a near-standard alternative such as `notes/live/TODOS.md`, warn.
  - `notes/live/011.ISSUES.md` is optional; if issues-note behavior exists through a near-standard alternative such as `notes/live/ISSUES.md` or `notes/live/200.ISSUES.md`, warn.
- `skills/` is optional by capability adoption.
  - If the project does not define project-local skills, no finding.
  - `.agents/skills` and `.claude/skills` may exist as valid runtime depots and are not findings by themselves when they are symlinked imported depots.
  - If project-local Agentos-style skills exist, they should live in `skills/`.
  - If project-local skill packages exist elsewhere in a near-standard way, warn about overlapping or nonstandard alternatives.
  - If `.agents/skills` or `.claude/skills` are materialized as local non-symlink directories in a way that blurs imported-depot vs project-local authority, warn.
- `dev/live/` is optional by capability adoption.
  - If absent, no finding.
  - If live-script behavior exists through near-standard alternatives, warn.
- In active adopted numbered surfaces, non-numbered files produce a warning unless they are clearly reserved or intentionally outside the active numbering protocol.
- Duplicate numeric prefixes and obvious range violations remain valid numbering findings in active adopted surfaces.

## Non-Goals

- Do not apply fixes.
- Do not write TODOs, issue reports, or implementation requests unless explicitly asked.
- Do not require every project to adopt every Agentos subsystem.
- Do not treat missing surfaces as failures without declared, observed, or contextual reason.
- Do not warn on absence alone for optional surfaces.
- Do not describe optional capability absence as debt when there is no evidence that the project uses that capability.
- Do not depend on `Doctor.CLI` existing.
