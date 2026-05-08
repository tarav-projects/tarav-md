# Iterante.Canvas.Model - design-summary

## Summary

Semantic model for representing Iterante mission workflows as Agentos.Canvas graphs. The model is a state-transition graph with two actors (Iterante and Agent), where cards are state/content descriptors and edges are operator-labeled actions.

## Accepted Decisions

1. **Two actors only: Iterante and Agent.** Iterante is the whole runtime side (CLI + mission.py + git). Agent is the AI doing the work. No finer breakdown — internal CLI/mission.py distinctions are invisible on the canvas.

2. **Edges are operator actions, cards are state descriptors.** The arrow says *who does what*. The card says *how, with what, finding what* — the body of the operator's action. Cards earn their space by carrying information the arrow label alone cannot.

3. **Past-tense card naming.** Cards describe the state of the world after an action: "project oriented", "paragraphs checked", "biblio metadata cached". This makes them clearly states, not instructions. Imperative naming would blur the model.

4. **Prompt/submit rhythm for tasks.** The real Iterante workflow is a conversation:
   - `iterante: prompt` → task card (what the agent should do) → `agent: submit` → result card (what was found/fixed)
   - Each step in mission.py produces a prompt card and a result card.

5. **Three Iterante command types reflected in edge verbs:**
   - `iterante: prompt` — open task (`ctx.task`)
   - `iterante: poll` — structured-answer request (`ctx.poll`)
   - `iterante: ask` — binary branch question (`ctx.branch`)

6. **Two branch types, visually distinguishable:**
   - **Agent-answered branch:** `iterante: ask` going in, `agent: answer-yes` / `agent: answer-no` going out. The agent decides.
   - **Program-decided branch:** `iterante: evaluate` going in, `iterante: loop` / `iterante: advance` going out. mission.py decides. No agent involvement.

7. **Program-only transitions use Iterante as operator.** Checkpoints, routing, state advances — all `iterante:` edges. Examples: `iterante: checkpoint`, `iterante: render`, `iterante: evaluate`, `iterante: loop`, `iterante: advance`.

8. **Canvas mirrors mission.py structure faithfully.** The canvas is a structural mirror of the real mission flow, not aspirational. If a branch doesn't exist in mission.py, it doesn't exist on the canvas.

## Operator Verb Vocabulary

| Arrow | Actor | Meaning |
|---|---|---|
| `iterante: render` | Iterante | render mission instructions |
| `iterante: checkpoint` | Iterante | git commit project state |
| `iterante: prompt` | Iterante | open task for agent |
| `iterante: poll` | Iterante | structured-answer request |
| `iterante: ask` | Iterante | binary branch question |
| `iterante: evaluate` | Iterante | program-internal decision point |
| `iterante: loop` | Iterante | program routes back |
| `iterante: advance` | Iterante | program routes forward |
| `agent: orient` | Agent | orientation work |
| `agent: work` | Agent | general agent work |
| `agent: submit` | Agent | complete task or poll |
| `agent: answer-yes` | Agent | resolve branch: yes |
| `agent: answer-no` | Agent | resolve branch: no |

## Card Types

| Type | Meaning |
|---|---|
| `content` | State descriptor — what the world looks like after an action |
| `question` | Decision-point state — waiting for resolution |

## Execution Plan

1. **Draft a section of the canvas** (orient through first branch) in the new model to pressure-test card density and rhythm.
2. **Revise the full md-library workflow canvas** based on pressure-test findings.
3. **Update Agentos.Canvas index note** if the model introduces new conventions worth documenting.

## Deferred Items

- Whether `agent: submit` needs sub-verbs (e.g., `agent: report` for structured results vs `agent: submit` for open tasks). Current decision: keep it simple with `agent: submit` for all.
- Whether poll result cards need a distinct type from task result cards. Currently both are `content`.
- Renderer implications — the dialog model roughly doubles card count; layout strategy for longer canvases is deferred to Canvas.Renderer work.
- Formal relationship between this model and the Agentos.Canvas protocol (TID.Pair enforcement, edge labels, etc.).

## Relevant Files Or Surfaces

- `notes/canvas/md-library-iteration-mission-workflow.canvas` — the canvas being redesigned
- `notes/index/110-Agentos.Canvas.md` — canvas surface protocol
- `md-library/.agentos/templates/md-library-iteration/mission.py` — source of truth for flow structure
- `notes/live/510-agentos-canvas-model-design-session.md` — earlier canvas model design session
- `notes/live/511-canvas-renderer-split-impl-req.md` — renderer split impl-req

## Open Questions

- Should the prompt card and result card for a single step share the same id (with a suffix like `-prompt`/`-result`) or have independent ids?
- How do `iterante: evaluate` cards handle multi-way branches (more than binary)?

## End Log

- 2026-05-08: Initial design summary written from canvas dialog representation discussion. Converged on two-actor model (Iterante/Agent), state-transition semantics, prompt/submit rhythm, and two branch types.
