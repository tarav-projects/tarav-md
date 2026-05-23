---
name: agentos-file-numbering-base
description: Deprecated compatibility surface for Agentos numeric filename protocols. Prefer `agentos-pkg` concept `File.Numbering.Protocol`, its appendix, and `agentos-pkg/references/file-numbering-protocol.md`.
---

# Agentos File Numbering Base

Deprecated compatibility surface. Durable numbering semantics now live in `agentos-pkg/index/100-index.md` under `File.Numbering.Protocol`; design depth lives in `agentos-pkg/appendix/File.Numbering.Protocol-appendix.md`; operational commands live in `agentos-pkg/references/file-numbering-protocol.md`.

Minimal protocol for Agentos-managed numeric filename workflows.

This skill operationalizes `notes/index/103-File.Numbering.Protocol.md`. The index note is the durable design source; this skill provides reusable workflow guidance for agents.

## Scope

- Define shared numbering mechanics, not document body structure.
- Centralize how `agentos stdlib prefix next` relates to numbered artifact protocols.
- Define only the base numbering rules that domain-specific `base` skills inherit.

## Shared Numbering Rules

- Canonical numbered filename shape is `NNN-short-topic.ext`.
- `NNN` is zero-padded to a fixed width, currently `3`.
- Numeric prefixes are stable handles, so the meaningful title may change while the number remains fixed.
- A numbering domain is defined by:
  - the project-relative target path
  - the filename pattern matched by the allocator
  - the allocation range
  - any manually assigned reserved prefix table
  - whether numbers must be unique only inside the domain or across a broader project surface
- For Agentos project-aware allocation, the numbering source is the configured project scan scope for numbered surfaces, filtered by the resolved target route.

## Allocator Behavior

- `agentos stdlib prefix next --project-base <project-root-basename> --target <path>` discovers the `Agentos.Project` from `pwd`, asserts the resolved project root basename, loads the project prefix policy, and allocates for the project-relative target path.
- Use `--project /path/to/project --project-base <project-root-basename> --target <path>` when outside the intended project tree.
- Numbered artifact prefixes must be allocated with `agentos stdlib prefix`; do not assign ordinary prefixes by manual inspection.
- If `agentos stdlib prefix` fails, stop and ask the user how to resolve the project or numbering surface. Do not fall back to inspection.
- In nested workspaces, verify that the resolved `project_root` is the intended numbered surface. Use `--project-base <basename>` for discovery from `pwd`, or `--project /path/to/project --project-base <basename>` to disambiguate from outside the tree; do not use `--project .` unless `.` is the actual initialized project root.
- If the intended artifact surface is not an initialized `Agentos.Project`, stop and ask whether to initialize it, target a parent project explicitly, or use another project root.
- It scans the configured project numbered-surface scope. The current default includes are `notes` and `dev/live`.
- It extracts ordinary allocated prefixes using the filename regex `^(\d{width})-`.
- It ignores files that do not begin with a valid zero-padded ordinary prefix.
- Reserved prefixes are manually assigned fixed-role prefixes, not ordinary allocator output.
- It returns:
  - the selected route lower bound if no eligible prefixes exist
  - otherwise `max(existing eligible prefixes in the selected route range) + 1`
- This is append-only allocation, not gap-filling allocation.

## Stability Rules

- Numeric prefixes are stable identifiers once assigned.
- Gaps are allowed.
- Deleted files do not cause renumbering of surviving files.
- Deleted prefixes are not reused by the shared allocator.
- Do not renumber existing numbered files, because renumbering breaks links and external references.

## Domain Ownership

- This skill must not carry a concrete inventory of numbering domains.
- Each domain `base` skill must define its own:
  - location
  - filename pattern
  - target path
  - numbering source or project scan-scope assumption
  - floor or reserved range
  - uniqueness scope
  - exact `agentos stdlib prefix next` command, if allocation is automated
- This skill owns only the shared numbering semantics that all those domain skills inherit.

## Cross-Domain Coordination

- Some systems need numbers to be unique across a broader surface than one folder.
- Example: Agentos notes use project-wide md-surface allocation, where the same ordinary note number should not identify different ordinary files in different numbered surfaces.
- Current `agentos stdlib prefix next --project-base ... --target ...` supports project-aware allocation with project root basename assertion. Full project-wide diagnostics such as duplicate reports, range violations, and reserved-prefix consistency checks remain future `prefix doctor` or equivalent work.

## Workflow For A New Numbered Artifact Type

1. Decide the domain root and canonical filename extension.
2. Decide whether the domain is human-managed, agent-managed, or split by range.
3. Pick a minimum floor and any reserved range policy.
4. Define the target path and numbering source, for example `--project-base <project-root-basename> --target notes/live` using the project numbered-surface scan policy.
5. Add a domain base protocol skill or base spec that states:
   - location
   - filename pattern
   - target path
   - numbering source or project scan-scope assumption
   - floor or reserved range
   - uniqueness scope
   - exact `agentos stdlib prefix next` command, if allocation is automated
   - stability rule: gaps allowed, no renumbering
6. Ensure the domain protocol stays focused on numbering/location only, unless it intentionally owns broader structure.
7. Update this skill only if the shared numbering model changes, not merely because a new domain was added.

## Review Checklist

- Is the target path routed to the intended range?
- Has `agentos stdlib prefix next --project-base ... --target ...` been run successfully for this exact allocation?
- Does the resolved project root and project-base assertion match the intended artifact surface?
- Does the filename pattern use the same width as the allocator?
- Does the protocol state the exact numbering source?
- Is the minimum floor explicit?
- Is the human-vs-agent range policy explicit?
- Is the uniqueness scope explicit?
- Does the protocol explicitly allow gaps and forbid renumbering?
- Does the protocol include the exact `agentos stdlib prefix next` command when automation exists?

## Non-goals

- Do not define body templates for notes, scripts, or reports here.
- Do not introduce gap-filling or reuse semantics unless the allocator is intentionally redesigned.
- Do not treat directory-local habits as protocol until they are written in the relevant base skill or spec.
