---
name: trigger-design-session
description: "Activate a Design.Session workflow with the Main.Designer.Agent. Use when the user wants to start or continue a design session."
---

# Trigger: Design Session

Activates the `Main.Designer.Agent` workflow for scoped human-agent design convergence.

## When To Fire

- User says "let's start a design session", "let's design X", "start a design-session"
- User invokes `trigger-design-session`
- User says "continue the design-session"

## What To Load

Load the `hugentics-designer` skill — it contains the full workflow instructions, session runtime, artifact formats, and reference files.

## Context

This is the entry point to `Fundamentals.Design` — the first phase of the Hugentic Harness. See `agentos-hugentics` for the full workflow map.
