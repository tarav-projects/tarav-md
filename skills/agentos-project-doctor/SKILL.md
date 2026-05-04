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
- `notes/index/ontology.md`

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

## Target Resolution

1. If the user provides a target path, use it.
2. If no target is provided, use the current working directory.
3. State the resolved target in the report.
4. Do not create `.agentos/`, notes, skills, or config during a doctor pass.

## Reference Loading

Load references based on the observed target surfaces.

Always load:

- `references/project-identity.md`
- `references/surface-presence.md`

Load when relevant:

- `references/index-notes.md` when `notes/index/` exists or dotted concepts appear.
- `references/ontology-registry.md` when `notes/index/` exists or dotted concepts appear.
- `references/reserved-notes.md` when `notes/live/` exists.
- `references/numbering.md` when numbered files exist in active Agentos surfaces.
- `references/authority-drift.md` when `AGENTS.md`, `skills/`, `notes/live/`, or `notes/index/` exist.

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
- `agentos prefix next` only for allocation context, not as a doctor verdict

## Check Outcome Model

Use these statuses:

- `pass`: the check satisfied the expected condition
- `fail`: violates a declared or strongly expected `Agentos.Stack` requirement
- `warn`: likely drift, partial adoption mismatch, or missing useful surface
- `info`: useful observation that is not a problem
- `skip`: not applicable or not enough evidence
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
- Use `fail` only for strong violations.
- Use `warn` for likely drift or incomplete adoption.
- Use `info` for useful context.
- Include skipped checks when they explain why a surface was not evaluated.

## Non-Goals

- Do not apply fixes.
- Do not write TODOs, issue reports, or implementation requests unless explicitly asked.
- Do not require every project to adopt every Agentos subsystem.
- Do not treat missing surfaces as failures without declared, observed, or contextual reason.
- Do not depend on `Doctor.CLI` existing.
