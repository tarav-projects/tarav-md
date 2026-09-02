# Hugentics Grounding

This module runs the active `tarav-hugentics --ground [FOCUS]` workflow. It
uses a retained `Diagram.View` to bridge the current chat context to relevant
Diagram data while leaving semantic navigation and sufficiency judgment with
the Agent.

Read [`../../tarav-pkg/tarav-diagram.md`](../../tarav-pkg/tarav-diagram.md)
before operating. Grounding is ungated and read-only toward the Diagram
semantic database. It may create and maintain the session's View.

## Responsibility Boundary

> Tarav provides navigable context mechanics; the Agent decides what is
> relevant and whether it has loaded enough.

`--ground` does not recommend context mechanically, infer what influenced an
Agent, capture missing material, or resolve contradictions. It exposes context
and POIs so the Agent and User can reason from them.

## Session View Convention

Grounding Views use these top-level `about.json` fields:

```json
{
  "workflow": "tarav-hugentics.ground",
  "chatlas_session_identity": "<Chatlas identity hash>",
  "chatlas_session_id": "<native provider session id>"
}
```

`Session.Diagram.View` interprets `chatlas_session_identity` as its session
coordinate. The remaining fields stay an open consumer convention preserved
and queryable through `about.json`.

## Workflow

1. Resolve and refresh the current session with
   `tarav-chatlas-my-session-id`. Use the returned native session ID and
   neutral Chatlas identity; do not perform a second refresh.
2. Resolve the Project's configured main Model without bootstrapping Diagram or
   Project state with `tarav diagram model show --project --json`. If the
   Project has no main Model, report that POI and stop.
3. Find the session View:

   ```bash
   tarav diagram view list \
     --about workflow=tarav-hugentics.ground \
     --about chatlas_session_identity=<identity-hash> \
     --json
   ```

   Resume the sole match. When no View exists, create one from the Project
   Model:

   ```bash
   tarav diagram view create \
     --project \
     --view-type Session.Diagram.View \
     --about-field workflow=tarav-hugentics.ground \
     --about-field chatlas_session_identity=<identity-hash> \
     --about-field chatlas_session_id=<native-session-id> \
     --json
   ```

   Several matches are a View-identity POI. Do not silently choose one unless
   the invocation or visible discussion already identifies the intended View.
4. Synchronize a resumed View, then check it. Staleness, visible-Line budget,
   dependency, and materialization findings are POIs rather than blockers.
5. Read the self-contained View. The initial projection retains every scoped
   Block shallowly and seeds visible Lines mechanically; this is only a
   starting map.
6. Derive candidate relevance from `FOCUS` and the visible discussion. Inspect
   Block names, dependencies, statistics, and visible Lines. The focus narrows
   the pass but does not erase relevant current-chat context.
7. Navigate through generic View commands:

   - `expand` and `collapse` move a Block along its disclosure ladder;
   - `include-line` and `exclude-line` maintain the Agent's relevance
     selection;
   - `expand --full` exposes all Lines and deep support for one Block when a
     selective route is not yet known;
   - progressive disclosure moves from wording to compact support, review, and
     POI statistics, then to rendered Chatlas neighborhoods;
   - contextual renderings use short identity prefixes and omit raw support and
     reference JSON. The Line ship remains the escalation pointer when exact
     Diagram evidence coordinates are needed. Do not rewrite identifier-shaped
     text inside support verbatims; evidence content remains exact.

   The Agent, not the initial ranking, owns every later selection decision.
8. Treat each successful View mutation's returned Block rendering as the
   incremental context supplied by that operation. Mutation commands return
   the complete current rendering of every affected Block, so do not reload
   the full View after each change. Read `view show --json` or `view render`
   when bootstrapping or resuming the View, reconciling uncertain local
   context, or deliberately inspecting the complete selection. Material merely
   retained in a View but neither read nor returned by an operation is not
   loaded context.
9. Run `view check` again. If the View exceeds its configured budget, reduce it
   deliberately; Tarav never auto-evicts context.

Direct block-by-block Model navigation remains the fallback when View tooling
is unavailable or insufficient.

## Completion Report

Return a compact, continuation-oriented report containing only useful parts:

- the View ship and its exact repository commit/path edition;
- the most relevant Blocks and Lines retained for the session;
- how they contextualize the visible discussion or explicit focus;
- material contradictions, ambiguity, missing coverage, and other POIs;
- whether the Agent considers grounding sufficient for the foreground work;
- the next useful escalation when it is not sufficient.

Cite Block and Line ships when they materially improve verification or future
maintenance. Distinguish Diagram content from Agent inference. Missing Diagram
coverage is a capture opportunity, not permission to invent context or mutate
the Diagram during grounding.
