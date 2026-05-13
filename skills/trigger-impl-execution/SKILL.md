---
name: trigger-impl-execution
description: "Activate an implementation execution workflow with the impl.executer.agent. Use when the user wants to execute an Impl.Req."
---

# Trigger: Implementation Execution

Activates the `impl.executer.agent` workflow for loading and executing an `Impl.Req` artifact.

## When To Fire

- User approves an `Impl.Req` and says "implement this", "execute the plan", "build this"
- User invokes `trigger-impl-execution` or `agentos-design-implementation`

## What To Load

Load the `hugentics-impl-executer` skill — it contains the execution workflow, realignment loop, deviation handling, and reference files.

## Context

This is the entry point to `Implementation.Execution` — the third phase of the Hugentic Harness. See `agentos-hugentics` for the full workflow map.
