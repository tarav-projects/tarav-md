---
name: hugentics-workflow-status
description: "Operational Hugentic status workflow — produce a structured checkpoint against the active workflow's artifacts and surfaces."
---

# Hugentics Workflow Status

Produce a structured status report for the active Hugentic workflow.

This is an operational `Package.Aux.Skill` under `agentos-hugentics`. It is not a general project diagnosis surface; it reports the state of an ongoing Hugentic workflow.

## Activation

Use when the user asks for workflow status, a structured checkpoint, or a workflow-aware report during an active Hugentic workflow: design session, impl-req design, or impl execution.

## What To Load

- Load `agentos-hugentics/references/hugentic-status.md` for the full report protocol.
- Identify the active workflow and report against its surfaces.
