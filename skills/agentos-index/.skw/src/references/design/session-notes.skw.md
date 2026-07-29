# Session.Notes

This detailed product-design module is owned by `agentos-index --design`.

> $kw: --dev-from references/index-context-assembly.skw.md

`Session.Notes` is the working-state section of a `Design.Session`.

It keeps useful loose material out of fragile chat memory without pretending it is settled design.

## Role

Use `Session.Notes` for:

- open questions
- possible next questions
- parked ideas
- active assumptions
- references to inspect
- capture TODOs
- loose task-shaped observations
- uncommitted discussion reminders
- scope drift notes

## Shape

Prefer small named lists:

```md
## Session.Notes

### Open Questions

- [question] — [why it matters]

### References

- [path or note] — [why it matters]

### Parking Lot

- [idea] — [when to revisit]
```

## Writing Guidance

- Be explicit about what is unsettled.
- Do not let notes become a dumping ground for everything said in chat.
- Move stable concept fundamentals into `Design.Index`.
- Move concept rationale, examples, pressure tests, tradeoffs, rejected alternatives, and design depth into `Design.Index` appendix.
- Move concept-level session mechanics into `Design.Index` meta.
- Clear or rewrite notes when they become stale.

## User Gate

Notes are still artifact state and require approval to write.

Once the user approves an active capture/update workflow, the agent may include proportional notes updates if it states the intended changes.
