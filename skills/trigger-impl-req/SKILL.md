---
name: trigger-impl-req
description: "Activate an Impl.Req design workflow with the impl.designer.agent. Use when the user wants to plan an implementation."
---

# Trigger: Impl-Req Design

Activates the `impl.designer.agent` workflow for designing an implementation plan and producing an `Impl.Req` artifact.

## When To Fire

- User says "let's plan the implementation", "create an impl-req", "make an impl-req"
- User triggers `Impl.Req.Handoff` interruption from a design session
- User invokes `trigger-impl-req` or `agentos-artifact-impl-req`

## What To Load

Load the `hugentics-impl-designer` skill — it contains the impl-req design workflow, artifact format, and reference files.

## Context

This is the entry point to `Implementation.Design` — the second phase of the Hugentic Harness. Can be triggered from a design session or independently. See `agentos-hugentics` for the full workflow map.
