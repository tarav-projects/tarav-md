# Index.Capture.Context.Module

`Index.Capture.Context.Module` is the runtime-selected `Skill.Module` containing the complete context an agent needs to curate touched data into the current index realization. Load the entire module at the start of every `--capture` run, before discovering candidates or drafting text.

The module contextualizes the task against `Touched.Index`; it does not assume the current Markdown surface contains all relevant touched data.

The module is internal workflow context, not a user-facing report. It makes the running agent's preparation exhaustive while allowing the visible capture workflow to remain small.

## Knowledge Closure

Close every category below before building the candidate map:

1. **Authority model.** Load `references/touched-data.md` plus the owning blocks for `Touch.Authority.Surface`, `Touched.Data`, `Support.Set`, `Touched.Support.Network`, `Index.Line`, `Live.Index.Line`, and `Index.Presumption`.
2. **Decision model.** Load `references/decision-cycle.md`, `Context.Grounding`, `Touched.Decision.Cycle`, `Open.Inference`, and `POI.Instance`.
3. **Current surface model.** Load `Agentos.Index.System`, `Index.Surface`, `Index.Ontology`, `Index.Appendix`, `Index.Agendix`, `Touched.Surface.Index`, `Index.Chat.Capture`, `InContext.Index.Chat.Capture`, `Capture.Gradient`, `User.Attention`, `Kernel.Writing`, `Kernel.Block`, `Line.Type`, `Anchory.System`, `Edition.Approval.Token`, and `Line.Verbatim.Gate`, plus appendix depth when present.
4. **Operational model.** Load `references/search.md`, `references/edit.md`, `references/agendix.md`, `references/type.md`, `references/link.md`, and `agentos-pkg/references/index-block-catalog.md`.
5. **Depot model.** Run `Index.Discovery` and resolve the task-relevant engaged `Index.Depot`s through their routers. Respect explicit `--depot` and `--chapter` scope; otherwise include every depot materially engaged by the conversation.
6. **Touched concept closure.** For every concept materially touched by the chat, load its routed ontology block, appendix page, live agendix file, and relevant line standing. Follow related concepts until overlap, contradiction, or missing grounding is explicit.
7. **Authority-surface closure.** Follow support references to original qualifying user turns when the index digest is insufficient, disputed, or consequential. Do not treat every chat or every user turn as touched merely because it exists.
8. **External evidence closure.** Inspect code, files, adjacent project surfaces, Git history, and runtime state when they change whether a candidate is new, coherent, naturally placed, or already captured.

Exhaustive means closing these categories for the engaged task, not reading every byte of every discovered depot. The agent must know which categories were checked and which surfaces do not exist.

## Context Discipline

- Keep the module load and evidence inventory internal unless a missing or conflicting source materially affects the user's decision.
- Treat the visible conversation as already shared context: do not restate what the user just established merely to prove it was grounded.
- Separate grounded authority, ungrounded index presumption, review state, and demoted history; these are independent distinctions.
- Use adjacent evidence to improve candidates, not to widen the visible session without need.
- Surface contradictions and support gaps as POIs; their existence does not prescribe a capture or deletion.
- `Index.Capture.Context.Module` carries index-capture preparation; `--capture` does not require a separate design-workflow skill at runtime.
