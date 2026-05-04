# Agentos.Project.Doctor Minimal Surface - design-summary

## Purpose

Define the first minimal implementation surface for `Agentos.Project.Doctor`.

The doctor evaluates how well a concrete `Agentos.Project:<target>` conforms to `Agentos.Stack`. It is diagnosis-first and report-only by default. It does not fix.

## Accepted Direction

`Agentos.Project.Doctor` should start as a skill-first system with a CLI-ready shape.

The first implementation should be useful without `agentos doctor ...`, but it should be designed so that deterministic CLI checks can be added later and called by the skill.

## Core Concepts

- `Doctor.Check`: one test-like evaluation with structured outcome and evidence.
- `Doctor.CLI`: deterministic executable checks. It must be useful by itself for humans, scripts, CI, and skills.
- `Doctor.Skill`: agentic and mixed checks, calls `Doctor.CLI` when available, interprets results, and synthesizes the diagnosis report.
- `Agentos.Project.Doctor`: the combined diagnostic workflow for `Agentos.Project:<target>`.

The clean split is by determinism:

- deterministic checks belong in `Doctor.CLI`
- agentic and mixed checks belong in `Doctor.Skill`
- both produce or consume `Doctor.Check` results

## Minimal Skill Surface

Create:

```txt
skills/agentos-project-doctor/SKILL.md
```

The skill should:

- accept any target folder
- identify whether the target is an `Agentos.Project`
- inspect observed Agentos surfaces
- call `agentos doctor ...` or narrower doctor CLI commands when they exist
- run manual and agentic checks when CLI support is absent
- report findings with evidence
- not write files or apply fixes by default

## Minimal Check References

Create small check reference files under:

```txt
skills/agentos-project-doctor/references/
```

Initial references:

- `project-identity.md`
- `surface-presence.md`
- `index-notes.md`
- `ontology-registry.md`
- `reserved-notes.md`
- `numbering.md`
- `authority-drift.md`

These references are the skill-level test descriptions. They can include deterministic, agentic, and mixed checks.

## Minimal Checks

### project-identity

Check whether `.agentos/project.json` exists and whether the target should be treated as an `Agentos.Project`.

Report missing identity as a finding only when the target claims or appears to adopt Agentos.

### surface-presence

Detect relevant surfaces:

- `AGENTS.md`
- `notes/index/`
- `notes/live/`
- `skills/`
- `dev/live/`

Presence alone is not enough for pass/fail; the doctor should compare observed surfaces to declared or inferred adoption.

### index-entrypoint

If `notes/index/` exists, check for:

- `notes/index/000-index.md`

### ontology-registry

If dotted concepts appear in `notes/index/`, check for:

- `notes/index/ontology.md`

The skill may judge whether unregistered dotted names are real concepts or incidental references.

### reserved-notes

If `notes/live/` exists, check for:

- `notes/live/010.TODOS.md`

This is a warning-level check unless the project explicitly adopts `TODOS.Note`.

### numbering

Check obvious duplicate numeric prefixes in active numbered surfaces.

Initial scope can be simple and transparent:

- active `notes/index/`
- active `notes/live/`
- active `dev/live/` when present

Do not overreach into archived or migrated evidence unless the check is explicitly about legacy migration state.

### authority-drift

Agentic check: durable design truth should not live only in `AGENTS.md`, skills, or live notes when `notes/index/` exists.

This check requires judgment and should produce evidence, not broad accusations.

## Report Format

The first report format should be chat-first:

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

## Severity

Use a small severity set:

- `fail`: violates a declared or strongly expected `Agentos.Stack` requirement
- `warn`: likely drift, partial adoption mismatch, or missing useful surface
- `info`: useful observation that is not a problem
- `skip`: check not applicable or not enough evidence

## Non-Goals

- Do not fix findings by default.
- Do not write TODOs, issue reports, or implementation requests unless explicitly asked.
- Do not require every project to adopt every Agentos subsystem.
- Do not treat missing surfaces as failures without declared, observed, or contextual reason.
- Do not make the skill depend on `Doctor.CLI` existing.

## CLI Direction

Future `Doctor.CLI` work should implement deterministic checks as standalone commands.

Likely future command shape:

```sh
agentos doctor ...
```

The exact command tree is deferred. The important design rule is that the CLI must be independently useful and the skill may call it as one source of `Doctor.Check` results.

## Open Follow-Up

- Decide whether the first skill should load all references every time or only load references based on observed surfaces.
- Decide whether `Doctor.Check` should eventually have a JSON schema shared by CLI and skill reports.
- Decide the first deterministic CLI check to implement after the skill exists.

