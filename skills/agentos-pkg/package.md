# agentos-pkg Package

## Package.Identity

- `agentos-pkg` is the core `Package.Skill` for Agentos.
- It is a package-level public agentic surface, not the `agentos-md` repository or any single implementation surface.
- It currently lives in `agentos-md/skills/agentos-pkg/` as an implementation detail.
- The first migration is structural: Agentos Index content has moved into this package, while auxiliary skills preserve existing access paths.

## Package.Router

### Orientation

- `agentos-usage` — minimal Agentos orientation and usage routing.
- `agentos-pkg` — package-level orientation for the Agentos core package.

### Index

- `agentos-pkg/index/` — Agentos public index flat files and routing table.
- `agentos-pkg/appendix/` — Agentos public index appendix files.
- `agentos-pkg/references/` — Agentos Index operational references.
- `agentos-pkg/testing/` — Agentos Index runtime test prompts.
- `agentos-index` — auxiliary skill for direct Agentos Index design context.
- `agentos-index-activate` — index runtime bootstrap auxiliary skill.
- `agentos-index-writer` — user-gated index write path.
- `agentos-index-doctor` — index health diagnosis.
- `agentos-index-test` — index activation and runtime tests.

### Hugentics

- `agentos-hugentics` — Hugentic Harness entry point.
- `hugentics-designer` — design-session workflow master.
- `hugentics-impl-designer` — implementation-request workflow master.
- `hugentics-impl-executer` — implementation execution workflow master.

### Hugentic Triggers

- `trigger-design-session` — design-session activation auxiliary skill.
- `trigger-impl-req` — implementation-request activation auxiliary skill.
- `trigger-impl-execution` — implementation execution activation auxiliary skill.
- `trigger-hugentic-status` — hugentic workflow status auxiliary skill.
- `trigger-capture-audit` — capture audit auxiliary skill.
- `trigger-chat-status` — general chat status auxiliary skill.

### Artifacts

- `artifact-design-session` — design-session artifact format pointer.
- `artifact-design-summary` — design-summary artifact guidance.
- `artifact-impl-req` — implementation-request artifact guidance.
- `artifact-issue-report` — issue-report artifact guidance.

### Project And Surface Operations

- `agentos-project-doctor` — Agentos project health diagnosis.
- `agentos-live-note-base` — live-note location and numbering protocol.
- `agentos-live-scripts-base` — live-scripts location and numbering protocol.
- `agentos-file-numbering-base` — Agentos numeric filename protocol.

### Package And Skill Development

- `agentos-skills-miner-ingenier` — skill research and mining workflow.
- `codebase-general-cleanup` — targeted codebase cleanup workflow.
- `git-commit-trigger` — deterministic semantic commit workflow.

## Package.Boundary

- `agentos-pkg` owns Agentos core public package orientation.
- `agentos-hugentics-pkg` is not created in this pass; Hugentics and the Agentos Index remain inside `agentos-pkg`.
- `agentos-chatlas-pkg` now exists as a separate package in `agentos-chatlas-md/skills/agentos-chatlas-pkg/`. Chatlas index content has been migrated there.
- `agentos-iterante-pkg` and `agentos-md-pkg` are out of scope for this package skeleton.
- Iterante-specific and local implementation-specific surfaces should not be folded into `agentos-pkg` by default.

## Package.Dependency

- `agentos-pkg` is the dependency root for Agentos package skills.
- Other Agentos package skills may depend on `agentos-pkg` for project model, skill model, index model, live-note protocol, and Hugentic workflow concepts.
- External concept references should use qualified package names when crossing package boundaries.

## Package.Install

- Install behavior is not implemented in this structural pass.
- Future install work may create or update auxiliary skills, package-local indexes, references, or local configuration.
- Any future install behavior should make side effects explicit before changing files.

## Package.Agents

- No dedicated `Package.Agent` is defined in this structural pass.
- Existing workflow agents remain represented by their current skills.

## Local.Boundary

- `agentos-md` is the markdown implementation project for Agentos surfaces.
- `agentos-pkg` is not the same thing as `agentos-md`.
- Local `agentos-md` concerns belong in `notes/index/` or a future `agentos-md-pkg`, not in `agentos-pkg`.
- If a surface is useful only for this repository's local maintenance, route it locally instead of treating it as Agentos core package knowledge.
