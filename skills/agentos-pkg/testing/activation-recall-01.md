# Test: activation-recall-01

## Subagent Prompt

You are working on the agentos-md project. Start by activating the index:

Run the `agentos-index` skill and perform the `Index.Agent` role to collect the relevant index context.

Once the index is loaded, answer these questions about the project's index system:

1. What naming convention do appendix files follow?
2. What are the reserved file prefixes in the 000-099 range? List them all.
3. What is the difference between `Global.Index.Scope` and `Extended.Index.Scope`?
4. What numbering range is used for public index flat files vs local index flat files?
5. How does an agent discover appendix content for a concept?

Respond in this exact format:

```json
{
  "answers": {
    "1": "your answer",
    "2": "your answer",
    "3": "your answer",
    "4": "your answer",
    "5": "your answer"
  }
}
```

## Expected Answers (hints for reviewer — semantic match, not verbatim)

1. `Concept.Name-appendix.md`
2. `000-index.md` (public router), `001-index.md` (local router), `010.TODOS.md` (TODO parking), `011.ISSUES.md` (issue parking)
3. Global is always-loaded (`index/`), Extended is on-demand (`appendix/`)
4. Public: `100-299`, Local: `300-499`
5. Check `appendix/Concept.Name-appendix.md` — naming convention is the discovery mechanism, no outlink required
