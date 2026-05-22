# Agentos.Surfaces — Appendix

Paired with `index/100-index.md`.

## Surface.Link.Directionality

- `Public.Surface` — skills, externally reachable (by other agents, other projects)
- `Local.Surface` — index notes, project-internal design truth
- `Local → Public` links are allowed (index notes can reference skills)
- `Public → Local` links are not allowed (skills must not reference index notes)
- rationale: skills are portable and shared; index notes are project-local truth. A skill that depends on a local index note breaks when used outside the project.
- the skill document is portable and can't link back to the index
- but local agents have access to both skills and index — they use `agentos-index` or the `Index.Agent` role to discover index data alongside the skill
- the agent bridges both worlds; the skill stays self-contained
- example: `hugentics-designer` (skill) references `agentos-hugentics` (skill) for the general alignment model, not an index note directly. A local agent running the skill can still access index concepts through index workflows.
