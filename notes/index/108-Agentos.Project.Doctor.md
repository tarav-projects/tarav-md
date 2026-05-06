# Agentos.Project.Doctor

`Agentos.Project.Doctor` is a diagnosis-first workflow for evaluating how well a concrete `Agentos.Project:<target>` conforms to `Agentos.Stack`.

It checks a target project through test-like doctor checks, reports problems with evidence, and supports follow-up discussion. It does not fix by default.

## Core Model

`Agentos.Project.Doctor` composes three concepts:

- `Doctor.Check`: one test-like evaluation with structured outcome and evidence
- `Doctor.CLI`: deterministic executable checks exposed through a project CLI
- `Doctor.Skill`: agentic and mixed checks, CLI orchestration, interpretation, and report synthesis

The clean split is by determinism, not by whether the result is pass/fail.

## Doctor.Check

`Doctor.Check` is the shared unit of evaluation.

A check may return:

- `pass`
- `fail`
- `warn`
- `skip`
- `unknown`

Each result should include enough evidence to support diagnosis:

- check name
- target surface
- status
- observed fact or missing fact
- relevant file, command, or path
- optional severity or importance
- optional suggested follow-up

## Doctor.CLI

`Doctor.CLI` runs deterministic checks.

It must be useful by itself for humans, shell scripts, CI, and other skills. `Doctor.Skill` may call it, but it is not merely an implementation detail of the skill.

Good CLI-owned checks include:

- required file existence
- JSON parse and basic schema checks
- duplicate numeric prefixes
- obvious range violations
- reserved-file presence
- broken links when deterministic link checking exists
- stale path patterns
- command availability

For Agentos, `Doctor.CLI` is expected to appear through `Project.CLI:Agentos`, likely as `agentos doctor ...`.

## Doctor.Skill

`Doctor.Skill` owns agentic and mixed diagnosis.

It can define checks directly, call `Doctor.CLI` checks when useful, interpret outputs, and produce the final diagnosis report.

Good skill-owned checks include:

- whether `AGENTS.md` is becoming a design source of truth
- whether durable design truth exists only outside `notes/index/`
- whether the project appears to partially adopt Agentos and what that implies
- whether dotted concepts are meaningful enough to require registry attention
- whether derived surfaces drift from `Agentos.Index.Notes`
- whether the project's `Usage.Surface` is coherent and derives hard facts from the index
- whether findings should become TODOs, issue reports, or implementation requests

Mixed checks combine both layers. For example, `Doctor.CLI` can list dotted names missing from `001-ontology.md`, while `Doctor.Skill` judges whether those names are concepts, incidental prose, or migration debt.

## Diagnosis Workflow

The default workflow is:

- identify the target project
- detect declared and observed Agentos adoption
- run relevant deterministic checks
- run relevant agentic checks
- synthesize findings
- report first
- wait for user direction before fixes

The doctor does not fix by default.

## Adoption Model

The doctor should distinguish:

- declared adoption: what the project claims or configures
- observed adoption: which Agentos surfaces are present
- expected adoption: what the relevant `Agentos.Stack` model expects for that context

A project can be partially adopting Agentos. Missing surfaces are not automatically failures; they become findings when they conflict with declared adoption, observed usage, or the desired model for the target.

## Optional Surface Policy

`Agentos.Project` requires `.agentos/project.json`.

Other Agentos surfaces are optional by default at the level of project capability adoption.

This means:

- if a project does not use a capability, the absence of that surface is not a finding
- if a project does use a capability through a near-standard, overlapping, or off-protocol alternative, the doctor should warn that the project is not using the canonical Agentos surface
- if the canonical Agentos surface is adopted, the doctor should enforce that surface's internal protocol

The doctor should therefore ask two questions for optional surfaces:

1. is this capability present at all?
2. if yes, is the project using the canonical Agentos surface for it?

Examples:

- no `skills/` and no skill-like workflow packages: no finding
- skill-like workflow packages exist outside `skills/`: warn about overlapping or nonstandard skill surfaces
- no `notes/index/`: no finding if the project does not appear to use an index-like durable design surface
- durable index-like design/reference notes exist outside `notes/index/`: warn about overlapping or nonstandard index-surface adoption
- `notes/live/TODOS.md` instead of `notes/live/010.TODOS.md`: warn because the capability is present through a near-standard reserved-note alternative
- `notes/live/ISSUES.md` instead of `notes/live/011.ISSUES.md`: warn because the capability is present through a near-standard reserved-note alternative

Absence alone is not enough for a warning on optional surfaces. Findings should come from broken mandatory identity, malformed adopted surfaces, overlapping near-standard alternatives, or conflicting authority between adopted surfaces.

## Initial Agentos Project Checks

The first scope should stay modest.

Useful initial checks:

- `.agentos/project.json` exists and parses as JSON for every target being evaluated as an `Agentos.Project`
- `AGENTS.md` exists at the project root, unless the target clearly establishes a different root-guidance convention
- `notes/index/000-index.md` exists when `notes/index/` is adopted
- `notes/index/001-ontology.md` exists when `notes/index/` is adopted
- `000-index.md` and `001-ontology.md` are checked for staleness relative to the active index surface
- TODO notes are optional; when a TODO note exists under `notes/live/`, it uses the reserved `notes/live/010.TODOS.md` path
- issue notes are optional; when an issues note exists under `notes/live/`, it uses the reserved `notes/live/011.ISSUES.md` path
- skills are optional; when skill-like workflow packages exist, canonical Agentos skills should live in `skills/`
- numbered files avoid obvious duplicate prefixes in active numbered surfaces
- active adopted numbered surfaces avoid unnumbered files unless the file is clearly reserved or intentionally outside the numbering protocol
- durable design truth is not only in skills, live notes, or `AGENTS.md`

## Relation To Maintenance.System

`Agentos.Project.Doctor` is a diagnostic workflow inside a broader `Maintenance.System`.

`Maintenance.System:<target>` may include doctor checks, issue reports, follow-up implementation workflows, cleanup passes, and project-specific maintenance conventions. The doctor is the report-first assessment part of that broader system.

## Related Concepts

- `Agentos.Stack`
- `Agentos.Project`
- `Maintenance.System`
- `Project.CLI`
- `Doctor.Check`
- `Doctor.CLI`
- `Doctor.Skill`
- `Agentos.Index.Notes`
