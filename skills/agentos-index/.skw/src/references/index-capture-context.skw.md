> $kw: --from Agentos.Index.System --from Anchory.System --from Capture.Gradient --from Context.Grounding --from Edition.Approval.Token --from InContext.Index.Chat.Capture --from Index.Agendix --from Index.Appendix --from Index.Chat.Capture --from Index.Depot --from Index.Discovery --from Index.Ontology --from Index.Surface --from Kernel.Block --from Kernel.Writing --from Line.Type --from Line.Verbatim.Gate --from Skill.Module --from Touched.Surface.Index --from User.Attention
> --dev-from references/index-context-assembly.skw.md

# Index.Capture.Context.Module

`Index.Capture.Context.Module` is the runtime-selected `Skill.Module` containing the complete context an agent needs to work safely across a `Touched.Surface.Index`. Load the entire module at the start of every `--capture` run, before discovering candidates or drafting text.

The module is internal workflow context, not a user-facing report. It makes the running agent's preparation exhaustive while allowing the visible capture workflow to remain small.

## Knowledge Closure

Close every category below before building the candidate map:

1. **Surface model.** Load the owning blocks for `Agentos.Index.System`, `Index.Surface`, `Index.Ontology`, `Index.Appendix`, `Index.Agendix`, `Touched.Surface.Index`, `Index.Chat.Capture`, `InContext.Index.Chat.Capture`, `Capture.Gradient`, `User.Attention`, `Context.Grounding`, `Kernel.Writing`, `Kernel.Block`, `Line.Type`, `Anchory.System`, `Edition.Approval.Token`, and `Line.Verbatim.Gate`, plus appendix depth for those concepts when present.
2. **Operational model.** Load `references/search.md`, `references/edit.md`, `references/agendix.md`, `references/type.md`, `references/link.md`, and `agentos-pkg/references/index-block-catalog.md`. These are the workflow-neutral rules capture consumes.
3. **Depot model.** Run `Index.Discovery` and resolve the task-relevant engaged `Index.Depot`s through their routers. Respect explicit `--depot` and `--chapter` scope; otherwise include every depot materially engaged by the conversation.
4. **Touched concept closure.** For every concept materially touched by the chat, load its routed ontology block, appendix page, and agendix file when those surfaces exist. Follow related routed concepts until the proposed edit can be judged without unresolved overlap or contradiction.
5. **External evidence closure.** Inspect code, files, adjacent project surfaces, Git history, and anchored chat evidence when they can change whether a candidate is new, correct, naturally placed, or already captured.

Exhaustive means closing these categories for the engaged task, not reading every byte of every discovered depot. The agent must know which categories were checked and which surfaces do not exist.

## Context Discipline

- Keep the module load and evidence inventory internal unless a missing or conflicting source materially affects the user's decision.
- Treat the visible conversation as already shared context: do not restate what the user just established merely to prove it was grounded.
- Separate reviewed ontology and appendix knowledge from unreviewed agendix leads.
- Use adjacent evidence to improve candidates, not to widen the visible session without need.
- `Index.Capture.Context.Module` carries index-capture preparation; `--capture` does not require a separate design-workflow skill at runtime.
