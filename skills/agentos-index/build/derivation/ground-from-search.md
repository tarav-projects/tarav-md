## Ground/Retrieval.Behavior
- `transform`: the retrieval behavior in `references/ground.md` is derived from `references/search.md`
- source: `agentos-index/references/search.md`
- target: the retrieval-behavior span in `agentos-index/references/ground.md` (`## Grounding Model`, plus any retrieval statements elsewhere in the module)
- placement hint: the retrieval-overlap lives under `## Grounding Model` near the top of `references/ground.md`
- why it exists: `--ground` depends on the canonical search doctrine, so the overlapping retrieval behavior should stay aligned with `--search` instead of drifting into a second independently-authored search contract
- context: preserve the `--search` doctrine in transformed form for grounding use; keep depot-scoped routing, chapter-scoped selective loading, citation behavior, and selective appendix loading aligned with `references/search.md`, but do not collapse the grounding-specific orchestration, report shape, or conversation-comparison behavior into a copy of the search module
- on drift: refresh the retrieval-overlap in `references/ground.md` to match the current `references/search.md` behavior while preserving the grounding-only sections and their wording
