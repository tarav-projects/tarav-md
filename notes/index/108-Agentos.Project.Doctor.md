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

## Initial Agentos Project Checks

The first scope should stay modest.

Useful initial checks:

- `.agentos/project.json` exists when the target claims to be an `Agentos.Project`
- `AGENTS.md` exists when agent workflow guidance is expected
- `notes/index/000-index.md` exists when index notes are present
- `notes/index/001-ontology.md` exists when dotted concepts are used
- `notes/live/010.TODOS.md` exists when live notes are used
- skills exist or are intentionally absent
- numbered files avoid obvious duplicate prefixes in active numbered surfaces
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
