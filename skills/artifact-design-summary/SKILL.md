---
name: artifact-design-summary
description: "Pointer to design-summary artifact format. Owner TBD — format currently defined in this stub."
---

# Artifact: Design Summary

Protocol for `design-summary` artifacts — structured live-notes that capture the converged output of a design discussion: decisions, execution plan, and deferred items.

## Location And Naming

- Use a filename ending in `-design-summary.md`
- Store in `notes/live/`

## Minimal Structure

```md
# [Short Title] - design-summary

## Summary

1-3 sentences describing what was designed and why.

## Accepted Decisions

Numbered list of decisions with brief rationale.

## Execution Plan

Ordered phases or chunks for implementation.

## Deferred Items

Items explicitly out of scope or left for later.

## Relevant Files Or Surfaces

## Open Questions

## End Log
```

## Writing Guidance

- Write for another agent or future session that did not participate in the discussion
- Capture decisions and rationale, not the exploration path
- Be concrete about what was decided and what was deferred
- Do not write a design summary automatically — only on explicit user request
