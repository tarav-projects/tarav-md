# Session Status Report

When the user asks for session status, provide a short structured report.

## Format

```
Session: [title]
Progress: [N closed / M converging / K open] — T total

Layers:
- Core.Design: [absent / fresh / active / settled / needs capture]
- TODO.Design: [absent / fresh / active / ready / needs capture]
- Exec.Plan: [absent / fresh / active / ready / blocked]

Items:
  [converging]
  - [item] — [one-line state]

  [in-progress]
  - [item] — [one-line state]

  [fresh]
  - [item] — [one-line state]

Uncommitted:
  - [layer/item] — [what was discussed but not written]

Open Space:
  - [unsettled material] — [why it matters, or "none"]

Sufficiency:
  [agent judgment of whether enough alignment exists for the current next move]

Suggest closing:
  - [item] — [why: saturated / no new ground / sufficient for session]

Active: [what we're currently discussing, if anything]

Next:
1. [item] — [why]
2. [item] — [why]
3. [item] — [why]

Recommendation: [N] — [short reason].
```

## Rules

- Group items by status, most actionable first.
- Split open items into "has work" (`in-progress`) vs "not started" (`fresh`).
- Report layer state before item details when the session has more than one layer.
- Uncommitted lists layer/item discussion not yet captured in the artifacts. Say "none" if clean.
- Open Space lists significant unsettled design material only. Do not list every possible unanswered question.
- Sufficiency is the agent's judgment, not a user gate. Keep it short and practical.
- Suggest closing lists items the agent thinks are ready to close (saturated, no new ground, sufficient). Omit section if none.
- Next suggests up to 3 items with one-line rationale. Include a recommendation.
- Keep it scannable. The user may call this repeatedly.

## Next Item Selection Criteria

In rough priority:

- Items with significant uncommitted work (finish what's started).
- Layer transitions that unblock progress (`Core.Design -> TODO.Design -> Exec.Plan`).
- Items that unblock other items.
- Highest-leverage open items.
- Items closest to closing.

Keep explanations to one line each. The user picks.
