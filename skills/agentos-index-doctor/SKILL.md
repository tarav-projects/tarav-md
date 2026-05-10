---
name: agentos-index-doctor
description: "Index health review and diagnosis. Runs agentos index doctor CLI checks plus agent judgment on staleness, coherence, and coverage gaps. Reports issues, does not auto-fix."
---

# agentos-index-doctor

Index health review and diagnosis for the Agentos Index.

This is an `Alias.Skill` of the `agentos-index` `Skill.Package`.
Full design reference: `agentos-index/references/maintenance.md`

## When To Use

- user asks for an index health check, quality review, or lint pass
- user invokes manually: "run index doctor", "check index health"
- never auto-triggered — diagnosis is user-initiated

## Behavior

1. Run `agentos index doctor` on the project for deterministic checks (separators, reserved files, lint)
2. Add agent judgment on top: staleness, concept coherence, coverage gaps
3. Report issues with evidence — quote the problematic content
4. Suggest fixes but do NOT auto-fix

Use `agentos index doctor --json` for structured output. The index lives at `notes/index/`.

## Checks

### Structural (deterministic)

- `****` separator presence between H2-level blocks
- `Index.Block.Syntax` compliance (heading, fundamentals, size)
- 25-line block ceiling enforcement
- per-line character limit

### Semantic (agent judgment)

- ontology registry staleness — concepts used but not registered
- naming issues — inconsistent or approximate names across notes
- unrouted notes — notes not reachable from `000-index.md`
- concept coherence — blocks that mix multiple concepts
- coverage gaps — important concepts referenced but not defined

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
