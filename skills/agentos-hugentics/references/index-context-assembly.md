# Hugentic.Index.Context.Assembly.Module

`Index.Context.Assembly` is the whole-file `Context.Assembly.Module` containing the complete shared subject context for developing any managed Hugentics Index surface. Every consumer builder loads this module; running agents continue to load only the operational modules selected by their actual workflows.

The assembly is a development context boundary, not an import mediator. Consumers remain free to depend on, copy, derive, cite, or omit covered material according to their own purpose.

## Subject Universe

Close every category below before developing a Hugentics Index consumer:

1. **Touched-data authority.** Load `User.Touched`, `Touch.Authority.Surface`, `Touched.Data`, `Touched.Authority`, and their available appendix depth. Preserve the distinction between observable qualifying editions and the underlying touch event.
2. **Support network and line standing.** Load `Touched.Index`, `Support.Set`, `Touched.Support.Network` including its inline `Support.Reference` model, `Index.Line`, `Index.Line.Anchor`, `Live.Index.Line`, `Demoted.Index.Line`, `Index.Presumption`, `Reviewed.Content`, and `Reviewed.Cite.Closure`.
3. **Decision discipline.** Load `Context.Grounding`, `Index.Grounding`, `Touched.Decision.Cycle`, `Open.Inference`, `POI.Instance`, `Target.Product`, and `Product.Design.Session`.
4. **Current realization.** Load `Agentos.Index.System`, `Index.Skillware`, `Index.Surface`, `Index.Ontology`, `Index.Depot`, `Index.Chapter`, `Index.Appendix`, `Index.Agendix`, `Issue.Block`, `Touched.Surface.Index`, `Index.Discovery`, `Anchory.System`, `Grounding.Hugentic.Authority`, `Index.Chat.Capture`, and `InContext.Index.Chat.Capture`.
5. **Writing model.** Load `Kernel.Writing`, `Kernel.Block`, `Kernel.Line`, `Line.Type`, `Line.Type.Vocabulary`, `Dotted.Notation`, `Name.As.Index`, `Independent.Reader.Block`, `Cited.Duplication`, and `Not.A.Wall.Of.Text`.
6. **Workflow and gate model.** Load `Workflow.Neutral`, `Alignment.Mode`, `Alignment.Surface`, `Edition.Trigger.User.Gated`, `Verbatim.User.Gated`, `Line.Verbatim.Gate`, `Edition.Approval.Token`, `Capture.Gradient`, `Capture.Offer`, `User.Attention`, `User.Command`, `User.Command.Trigger`, `User.Command.Arg`, and `User.Command.Section`.
7. **Operations and validation.** Load `Chat.Index`, `Chat.Index.Delta`, `Chat.Index.HEAD`, `Line.Home`, `Line.Provenance`, `Project.Support.Chats`, `Project.Chat.Integration`, `Index.Edit.Action`, `Index.Edit.Modify.Line`, `Index.Enrichment`, `Index.Linter`, `Producer.Aids.Checker`, `Appendix.Discovery`, and the managed modules under `references/` whose behavior the consumer composes or routes.
8. **Skill context.** Load `Batchy.Skill`, `Package.Aux.Skill`, `Skill.Module`, `Packages.Master.Agent`, `Concept.Hardness`, `Design.Space`, `Design.Variable`, `Explicit.Namespace`, `Hugentic.Concept`, and `Writing.Friction.Reduction` where the consumer uses those boundaries.

## Development Discipline

- treat the covered set as the common universe a builder knows, not as content every consumer must reproduce
- preserve the general-model/current-realization boundary; chat-only mechanics must not redefine the global touched-data model
- inspect the consumer's direct dependencies and intent after loading the assembly, then choose its materialization and citation behavior locally
- follow related routed concepts and appendix depth when a direct block leaves a material decision unresolved
- keep builder assemblies distinct from workflow-selected preparation assemblies such as `Hugentic.Capture.Context.Assembly.Module`
- re-check the package after changing dependencies because coverage supervision is a semantic POI, not a parser failure

## Runtime Boundary

`Index.Context.Assembly` does not enter running-agent context merely because a builder used it. Runtime loading remains selective through the `agentos-hugentics` router, explicit skill arguments, and the active workflow's own modules.
