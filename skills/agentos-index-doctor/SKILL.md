---
name: agentos-index-doctor
description: "Index health review and diagnosis. Runs agentos index doctor CLI checks plus agent judgment on staleness, coherence, coverage gaps, and placement drift. Reports issues, does not auto-fix."
---

# agentos-index-doctor

Index health review and diagnosis for the Agentos Index.

This is a `Package.Aux.Skill` for the Agentos Index subsystem of `agentos-pkg`.
Full design reference: `agentos-pkg/references/maintenance.md`

## Prerequisites

The full index must be in context before running the doctor. If not already activated, run `agentos-index-activate` first. Semantic checks depend on the agent knowing the index contents.

## When To Use

- user asks for an index health check, quality review, or lint pass
- user invokes manually: "run index doctor", "check index health"
- never auto-triggered — diagnosis is user-initiated

## Behavior

1. Run `agentos index doctor` on the project for deterministic checks
2. Add agent judgment on top: staleness, coherence, coverage gaps, placement drift
3. Report issues with evidence — quote the problematic content
4. Suggest fixes but do NOT auto-fix

Use `agentos index doctor --json` for structured output.

## Checks

### Structural (deterministic)

- `****` separator presence between H2-level blocks
- `Index.Block.Syntax` compliance (heading, fundamentals, size)
- 25-line block ceiling enforcement
- per-line character limit

### Routing (deterministic + agent)

- public routing table (`000-index.md`) covers active concepts in public flat files
- local routing table (`001-index.md`) covers active concepts in local flat files
- routing entries match actual block headings in flat files
- no unrouted flat files in either public or local index

### Appendix (deterministic + agent)

- appendix files follow `Concept.Name-appendix.md` naming convention
- no orphaned appendix files (appendix exists but concept doesn't)
- no appendix files for concepts that don't exist in the index

### Semantic (agent judgment)

- concept coherence — blocks that mix multiple concepts
- coverage gaps — important concepts referenced but not defined
- naming issues — inconsistent or approximate names across index files
- `Placement.Heuristic` drift — design knowledge in skills/references that belongs in index/appendix
- stale blocks — content that contradicts current project state

## Report Format

```
## Index Doctor Report

### Issues Found

1. **[severity]** [file]: [description]
   > [evidence quote]
   Suggested fix: [what to do]

### Summary

- [N] issues found ([critical/warning/info breakdown])
- [overall health assessment]
```

## Constraints

- diagnosis-first — understand before suggesting fixes
- do not modify any files
- report should be actionable — every issue has a suggested fix
- when in doubt, flag it — false positives are better than missed issues
