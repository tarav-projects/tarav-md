# agentos-pkg Package

## Package.Identity

- `agentos-pkg` is the core `Package.Skill` for Agentos.
- It is a package-level public agentic surface, not the `agentos-md` repository or any single implementation surface.
- It currently lives in `agentos-md/skills/agentos-pkg/` as an implementation detail.
- The first migration is structural: Agentos Index content has moved into this package, while auxiliary skills preserve existing access paths.

## Package.Router

### Orientation

- `agentos-pkg` — workflow-neutral package-level orientation for the Agentos core package.
- `package.md` — package router, boundary, dependency, install, and agent notes.

### Index

- `agentos-pkg/index/` — Agentos public index flat files and routing table.
- `agentos-pkg/appendix/` — Agentos public index appendix files.
- `agentos-pkg/references/` — Agentos Index tutorials and operational references.
- `agentos-pkg/testing/` — package skill behavioral tests (testground format).
- `agentos-index` — public `Package.Aux.Skill` for Agentos Index orientation and index functions: research/navigation, writing/mutation, diagnosis, testing, and maintenance.
- `agentos-testground` — public `Package.Aux.Skill` for testground-based package skill testing.

Index entry points:

- `agentos-index` — first stop when an agent needs index workflow orientation without changing the caller's task.
- `references/index-system-guide.md` — compact cited tutorial for index architecture, surfaces, and workflows.
- `index/000-index.md` — routing table for concept lookup.
- `index/103-index.md` — index architecture concepts: `Index.Architecture`, `Index.Router`, `Index.Runtime`, `Distributed.Index`, `Soft.Programming.Language`.
- `index/104-index.md` — index operation concepts: `Index.Activation`, `Index.Agent`, `Multi.Index.Operation`, `Appendix.Discovery`, `Index.Linter`.
- `references/launch-runtime.md` — bootstrap procedure for loading index runtime context.
- `references/maintenance.md` — maintenance, writing, linting, deduplication, promotion, and placement checks.
- `references/test-system.md` — deprecated; use `agentos-testground` and `references/testground-runner.md`.
- `references/testground-format.md` — test file format, behavior tiers, testground folder structure.
- `references/testground-runner.md` — runner isolation, chatlas trace capture, evaluation, reports.

### Hugentics

- `agentos-hugentics` — workflow-neutral Hugentic Harness subsystem map.
- `hugentics-designer` — operational design-session workflow master for `What.Design`.
- `hugentics-impl-designer` — operational implementation-request workflow master for `How.Design`.
- `hugentics-impl-executer` — operational implementation-execution workflow master for `Impl.Exec`.

### Artifacts

- `artifact-design-session` — design-session artifact format pointer.
- `artifact-design-summary` — design-summary artifact guidance.
- `artifact-impl-req` — implementation-request artifact guidance.
- `artifact-issue-report` — issue-report artifact guidance.
- `hugentics-issue-tracker` — planned operational issue workflow paired with `artifact-issue-report`.

### Hugentic Status And Capture

- `hugentics-workflow-status` — structured status report for an active Hugentic workflow and its active artifacts.
- `hugentics-chat-status` — short/medium chat realignment report for reconnecting to the current conversation.
- `hugentics-capture-audit` — audit for significant chat material not captured in more durable surfaces.

### Project And Surface Operations

- `agentos-project-doctor` — Agentos project health diagnosis.
- `agentos-live-note-base` — live-note location and numbering protocol.
- `agentos-live-script` — live-script location and numbering protocol.
- `agentos-file-numbering-base` — deprecated compatibility surface; durable numbering content now lives in `File.Numbering.Protocol`, `appendix/File.Numbering.Protocol-appendix.md`, and `references/file-numbering-protocol.md`.

### Package And Skill Development

- `agentos-skills-ingenier` — skill research and mining workflow.
- `agentos-codebase-cleanup` — targeted codebase cleanup workflow.
- `agentos-git-commit` — deterministic semantic commit workflow.

### Compatibility And Deprecated Surfaces

- `agentos-index-activate` — deprecated standalone index runtime bootstrap; use `agentos-index`.
- `agentos-index-writer` — deprecated standalone index write skill; use the writing function in `agentos-index`.
- `agentos-index-doctor` — deprecated standalone index diagnosis skill; use the diagnosis function in `agentos-index`.
- `agentos-index-test` — deprecated standalone index test skill; use `agentos-testground`.
- `trigger-design-session` — deprecated trigger-only route; use `hugentics-designer`.
- `trigger-impl-req` — deprecated trigger-only route; use `hugentics-impl-designer`.
- `trigger-impl-execution` — deprecated trigger-only route; use `hugentics-impl-executer`.
- `agentos-usage` — deprecated general Agentos orientation; use `agentos-pkg`.
- `agentos-live-scripts-base` — renamed to `agentos-live-script`.
- `agentos-skills-miner-ingenier` — renamed to `agentos-skills-ingenier`.
- `codebase-general-cleanup` — renamed to `agentos-codebase-cleanup`.
- `git-commit-trigger` — renamed to `agentos-git-commit`.
- `trigger-hugentic-status` — renamed to `hugentics-workflow-status`.
- `trigger-capture-audit` — renamed to `hugentics-capture-audit`.
- `trigger-chat-status` — renamed to `hugentics-chat-status`.

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
