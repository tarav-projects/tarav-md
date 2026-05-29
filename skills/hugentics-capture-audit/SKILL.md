---
name: hugentics-capture-audit
description: "Operational capture audit workflow — scan chat for significant material not captured in durable surfaces. Use when the user says capture-audit, did we miss anything, scan the chat."
---

# Hugentics Capture Audit

Scan for converged material stuck upstream in the info flow. The goal is to avoid forgetting work and ideas — advance them across the progress pipeline:

```
Chat → Design.Artifact → Stable.Surface
Chat ——————————————————→ Stable.Surface (shortcut)
```

At each stage: is there material that's further upstream than its maturity warrants?

## Activation

Use when the user asks for a capture audit, "did we miss anything?", or similar. Works during any Hugentic workflow: design session, impl-req design, or impl execution.

The agent may suggest it after a long discussion stretch, before ending a session or workflow phase, or when multiple items were discussed rapidly without updates.

## Sources

Default sources:

- Current chat
- Any live notes or artifacts mentioned or active in the chat

The agent narrows by context and common sense. If the chat mentions a design session, scan it. If an impl-req was just executed, scan it. If nothing specific, scan the chat alone.

The user can scope with a prompt: "audit 523 and 529", "audit the last 3 design sessions", "just the chat."

## What To Look For

**Chat → working artifact:**

- Uncaptured ideas, decisions, approvals sitting in chat
- Settled concept fundamentals not yet in Design.Index or Impl.Index
- Rationale, tradeoffs, rejected alternatives not in appendix sections
- Session mechanics not in meta sections
- Unsettled significant material not visible in notes

**Working artifact → Stable.Surface:**

- Settled design blocks ready for promotion to index notes
- Implemented work not yet reflected in index or skills
- Concepts used across surfaces but not yet indexed

**General:**

- User-gated writes or settlements should not be treated as captured unless the user explicitly approved them
- Completed impl-reqs with settled design blocks that were never promoted

## Output

Produce a short report — do not auto-update any surface:

```
Capture audit:

Upstream material:
- [where it is] → [where it should go]: [description]

In sync:
- [surface]: up to date
```

If nothing is missing: "Capture audit: all sources in sync."

## After The Report

The user decides what to update. The agent may propose specific edits based on the report, but waits for approval as usual.
