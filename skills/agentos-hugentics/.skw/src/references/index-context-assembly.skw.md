> $kw: --context-assembly --from Agentos.Index.System --from Alignment.Mode --from Alignment.Surface --from Anchory.System --from Appendix.Discovery --from Batchy.Skill --from Capture.Gradient --from Capture.Offer --from Cited.Duplication --from Concept.Hardness --from Context.Grounding --from Demoted.Index.Line --from Design.Space --from Design.Variable --from Dotted.Notation --from Edition.Approval.Token --from Edition.Trigger.User.Gated --from Explicit.Namespace --from Gr.Req --from Grounding.Hugentic.Authority --from Hugentic.Concept --from Independent.Reader.Block --from InContext.Index.Chat.Capture --from Index.Agendix --from Index.Appendix --from Index.Chapter --from Index.Chat.Capture --from Index.Depot --from Index.Discovery --from Index.Edit.Action --from Index.Edit.Modify.Line --from Index.Enrichment --from Index.Grounding --from Index.Line --from Index.Linter --from Index.Ontology --from Index.Presumption --from Index.Skillware --from Index.Surface --from Kernel.Block --from Kernel.Line --from Kernel.Writing --from Line.Type --from Line.Type.Vocabulary --from Line.Verbatim.Gate --from Live.Index.Line --from Name.As.Index --from Not.A.Wall.Of.Text --from Open.Inference --from Package.Aux.Skill --from Packages.Master.Agent --from POI.Instance --from Producer.Aids.Checker --from Product.Design.Session --from Reviewed.Cite.Closure --from Reviewed.Content --from Skill.Module --from Support.Set --from Touch.Authority.Surface --from Touched.Authority --from Touched.Data --from Touched.Decision.Cycle --from Touched.Index --from Touched.Support.Network --from Touched.Surface.Index --from User.Attention --from User.Command --from User.Command.Arg --from User.Command.Section --from User.Command.Trigger --from User.Touched --from Verbatim.User.Gated --from Workflow.Neutral --from Writing.Friction.Reduction

# Index.Context.Assembly

`Index.Context.Assembly` is the whole-file `Context.Assembly.Module` containing the complete shared subject context for developing any managed Hugentics Index surface. Every consumer builder loads this module; running agents continue to load only the operational modules selected by their actual workflows.

The assembly is a development context boundary, not an import mediator. Consumers remain free to depend on, copy, derive, cite, or omit covered material according to their own purpose.

## Subject Universe

Close every category below before developing a Hugentics Index consumer:

1. **Touched-data authority.** Load `User.Touched`, `Touch.Authority.Surface`, `Touched.Data`, `Touched.Authority`, and their available appendix depth. Preserve the distinction between observable qualifying editions and the underlying touch event.
2. **Support network and line standing.** Load `Touched.Index`, `Support.Set`, `Touched.Support.Network` including its inline `Support.Reference` model, `Index.Line`, `Live.Index.Line`, `Demoted.Index.Line`, `Index.Presumption`, `Reviewed.Content`, and `Reviewed.Cite.Closure`.
3. **Decision discipline.** Load `Context.Grounding`, `Index.Grounding`, `Touched.Decision.Cycle`, `Open.Inference`, `POI.Instance`, `Target.Product`, and `Product.Design.Session`.
4. **Current realization.** Load `Agentos.Index.System`, `Index.Skillware`, `Index.Surface`, `Index.Ontology`, `Index.Depot`, `Index.Chapter`, `Index.Appendix`, `Index.Agendix`, `Touched.Surface.Index`, `Index.Discovery`, `Anchory.System`, `Grounding.Hugentic.Authority`, `Index.Chat.Capture`, and `InContext.Index.Chat.Capture`.
5. **Writing model.** Load `Kernel.Writing`, `Kernel.Block`, `Kernel.Line`, `Line.Type`, `Line.Type.Vocabulary`, `Dotted.Notation`, `Name.As.Index`, `Independent.Reader.Block`, `Cited.Duplication`, and `Not.A.Wall.Of.Text`.
6. **Workflow and gate model.** Load `Workflow.Neutral`, `Alignment.Mode`, `Alignment.Surface`, `Edition.Trigger.User.Gated`, `Verbatim.User.Gated`, `Line.Verbatim.Gate`, `Edition.Approval.Token`, `Capture.Gradient`, `Capture.Offer`, `User.Attention`, `User.Command`, `User.Command.Trigger`, `User.Command.Arg`, and `User.Command.Section`.
7. **Operations and validation.** Load `Index.Edit.Action`, `Index.Edit.Modify.Line`, `Index.Enrichment`, `Index.Linter`, `Producer.Aids.Checker`, `Appendix.Discovery`, `Gr.Req`, and the managed modules under `references/` whose behavior the consumer composes or routes.
8. **Skill context.** Load `Batchy.Skill`, `Package.Aux.Skill`, `Skill.Module`, `Packages.Master.Agent`, `Concept.Hardness`, `Design.Space`, `Design.Variable`, `Explicit.Namespace`, `Hugentic.Concept`, and `Writing.Friction.Reduction` where the consumer uses those boundaries.

## Development Discipline

- treat the covered set as the common universe a builder knows, not as content every consumer must reproduce
- preserve the general-model/current-realization boundary; chat-only mechanics must not redefine the global touched-data model
- inspect the consumer's direct dependencies and intent after loading the assembly, then choose its materialization and citation behavior locally
- follow related routed concepts and appendix depth when a direct block leaves a material decision unresolved
- keep builder assemblies distinct from workflow-selected runtime context modules such as `Index.Capture.Context.Module`
- re-check the package after changing dependencies because coverage supervision is a semantic POI, not a parser failure

## Runtime Boundary

`Index.Context.Assembly` does not enter running-agent context merely because a builder used it. Runtime loading remains selective through the `agentos-hugentics` router, explicit skill arguments, and the active workflow's own modules.
