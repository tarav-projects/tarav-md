# Uncommitted Work

The session artifacts are the committed state. The chat is the working tree. Discussion that has not been captured in the relevant artifact is uncommitted work.

The agent tracks this internally — no formal computation needed. It knows what was discussed and what made it into the session artifacts.

Uncommitted work may belong to:

- `Core.Design`
- `TODO.Design`
- `Exec.Plan`
- a specific item inside one of those layers
- cross-layer notes such as an unresolved transition or dependency

## When To Surface

- **After any artifact update:** "BTW, [layer/item] also has uncommitted discussion — want me to propose an update for that too?"
- **On continue triggers:** when the user says "continue", "what's next", "now what", or similar — surface uncommitted work before suggesting the next item.
- **On layer or item switch:** if the user moves to a different layer or item and there is substantial uncommitted work on the previous one — brief nudge: "[previous layer/item] has uncommitted discussion — park it or update?"

## Continue Semantics

When the user says "continue" / "what's next" / "now what":

1. If there's uncommitted work: "We have uncommitted discussion on [item] — want me to propose an update before moving on?"
2. If the user declines (or nothing uncommitted): show session status + next item suggestions.
3. If resuming a previously discussed item: briefly recall where we left off.

Prefer finishing uncommitted capture before moving from `Core.Design` to `TODO.Design`, or from `TODO.Design` to `Exec.Plan`, unless the user explicitly wants to defer capture.
