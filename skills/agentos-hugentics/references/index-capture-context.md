# Hugentic.Capture.Context.Assembly.Module

`Hugentic.Capture.Context.Assembly.Module` contains the complete preparation context an agent needs to curate touched data into the current index realization. Load the entire assembly at the start of every Index-targeted `--capture` run, before discovering candidates or drafting text.

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
7. **Line-centered projection.** Use the current chat to nominate materially relevant blocks and lines, then inspect only those subjects with one `agentos index line manifest show --depot <depot> --anchor <anchor> ... --verification stored --detail reference` batch. Read each selected line together with its parsed `Line.Type`, `Index.Line.Body`, enclosing block, bounded sibling context, anchor-occurrence standing, attachment standing, and independently typed support, gate, and provenance relationships. The manifest is a derived `Volatile.Surface`; it may reuse the last normal-lint locator but verifies its source fingerprints, falls back to depot parsing when needed, and neither establishes authority nor creates relationships. Scope selection may expose unanchored lines and their Index context, but only attached lines have dossier relationships. An `ambiguous` occurrence standing stops anchor-as-line lookup and routes the anchor to normal Index lint.
8. **Authority-surface closure.** Use the stored relationship projection to select the references that require validation. Re-run the nominated lines with `--verification sampled --verification-sample N` for a bounded confidence check, or `--verification complete` only when full validation is justified. Evidence rendering is independent: add `--detail turn` or bounded `--detail context --chat-radius N` only when text or chat neighborhood is needed. Do not treat every chat or every user turn as touched merely because it exists.
9. **External evidence closure.** Inspect code, files, adjacent project surfaces, Git history, and runtime state when they change whether a candidate is new, coherent, naturally placed, or already captured.

Exhaustive means closing these categories for the engaged task, not reading every byte of every discovered depot. The agent must know which categories were checked and which surfaces do not exist.

## Context Discipline

- Keep the module load and evidence inventory internal unless a missing or conflicting source materially affects the user's decision.
- Treat the visible conversation as already shared context: do not restate what the user just established merely to prove it was grounded.
- Separate grounded authority, ungrounded index presumption, review state, and demoted history; these are independent distinctions.
- Prefer terminal manifest inspection. Use `--neighbors N` to bound sibling Index context. Materialize beneath the ignored Chatlas workspace only when the same derived projection will be reused, and never make its path a durable dependency. Run normal depot lint after Index edits so comprehensive anchor agreement is checked and the volatile locator is refreshed.
- Use adjacent evidence to improve candidates, not to widen the visible session without need.
- Surface contradictions and support gaps as POIs; their existence does not prescribe a capture or deletion.
- `Hugentic.Capture.Context.Assembly.Module` carries index-capture preparation; `--capture` does not require a separate design-workflow skill at runtime.
