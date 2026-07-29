# Uncommitted Work

This detailed product-design module is owned by `agentos-hugentics --design`.

The session artifacts are the committed state. The chat is the working tree. Discussion that has not been captured in the relevant artifact is uncommitted work.

The agent tracks this internally — no formal computation needed. It knows what was discussed and what made it into the session artifacts.

Uncommitted work may belong to:

- `Design.Index`
- `Session.Notes`
- `Session.Log`
- `Impl.Req`
- a specific concept, section, question, or handoff
- cross-section notes such as an unresolved transition or dependency

## When To Surface

- **After any artifact update:** "BTW, [surface/item] also has uncommitted discussion — want me to propose an update for that too?"
- **On continue triggers:** when the user says "continue", "what's next", "now what", or similar — surface uncommitted work before suggesting the next item.
- **On component or item switch:** if the user moves to a different component or item and there is substantial uncommitted work on the previous one — brief nudge: "[previous surface/item] has uncommitted discussion — park it or update?"

## Continue Semantics

When the user says "continue" / "what's next" / "now what":

1. If there's uncommitted work: "We have uncommitted discussion on [item] — want me to propose an update before moving on?"
2. If the user declines (or nothing uncommitted): show session status + next item suggestions.
3. If resuming a previously discussed item: briefly recall where we left off.

Prefer finishing uncommitted capture before moving from concept alignment into implementation handoff, unless the user explicitly wants to defer capture.
