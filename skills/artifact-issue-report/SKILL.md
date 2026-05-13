---
name: artifact-issue-report
description: "Pointer to issue-report artifact format. Owner TBD — format currently defined in this stub."
---

# Artifact: Issue Report

Protocol for `issue-report` artifacts — structured live-notes that describe a discovered problem, its context, reproduction path, and expected resolution.

## Location And Naming

- Use a filename ending in `-issue-report.md`
- Store in `notes/live/`

## Minimal Structure

```md
# [Short Title] - issue-report

## Status

One sentence describing the current state of the issue.

## Problem

What is wrong. Observable behavior, not interpretation.

## Expected Behavior

What should happen instead.

## Reproduction

Steps or conditions to reproduce the problem.

## Context

Why this matters. Impact on the user, system, or other work.

## Relevant Files Or Surfaces

## Root Cause (if known)

## Suggested Fix (if known)

## Open Questions

## End Log
```

## Writing Guidance

- Write for another agent who has not seen the problem before
- Be concrete: include specific files, error messages, and reproduction steps
- Separate observation from interpretation
- Do not write an issue report automatically — only on explicit user request
