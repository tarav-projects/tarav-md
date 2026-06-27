# agentos-skill-pkg-builder --inline-drift

Find surfaces that contradict or go stale against a concept they mention. Read-only — a drift finder, not a reconciler.

## The Implicit Rule

No manifest needed. The index is the canonical definition surface; if a surface cites a concept, it must not contradict that concept. The "context explaining the rule" is the runnable surface itself.

This is the fully-implicit-context pole of `Derivation.Rule` — the source is the concept's index block, and the relation is **non-contradiction, not equality**. A mention is not a copy (`File.Mention`, `Inline.Relatedness`): a surface may rephrase, simplify, or scope a concept; it just may not contradict the canonical definition.

## Scope

- **default target = the recent-changes set** — the surfaces touched in the current conversation, unioned with the git change window (`--since`, default ~2-3 weeks). This makes inline-drift the post-edit drift sweep: "what just moved, and did it create contradictions downstream?"
- `--skill <skill>` — one skill surface, checked against the concepts it cites
- `--target <Concept>` — one block, checked against every surface that mentions it
- `--target <file>` — one surface, checked against every concept it cites
- `--target all` — the full sweep: every concept × its mentions (expensive)
- the default is overridable by any user prompt; the scope args just narrow the sweep

The recent-changes default is **bidirectional** — the change set holds both kinds of surface:
- a changed **index block** → sweep *its mentions* for contradiction
- a changed **non-index surface** → check *its citations* against current definitions

## Pass

1. Resolve the change set: read the conversation for surfaces touched, union the git window (`--since`).
2. For each definition in scope, resolve the canonical block from the index.
3. Find mentions via `Name.As.Index` — every surface carrying the `Dotted.Name`.
4. For each mention, read the surrounding claim and compare it against the definition.
5. Flag only contradiction or staleness — not mere rephrasing, simplification, or scoped use.

## Output

- candidates, not verdicts: each flagged mention with the concept block, the surface line, and why it may contradict or be stale
- for a human or agent to judge; any fix is a separate, gated edit
