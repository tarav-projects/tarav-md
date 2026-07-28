> $kw: --context-assembly --from Agentos.Index.System --from Alignment.Mode --from Alignment.Surface --from Anchory.System --from Appendix.Discovery --from Batchy.Skill --from Capture.Gradient --from Capture.Offer --from Cited.Duplication --from Concept.Hardness --from Context.Grounding --from Demoted.Anchored.Line --from Design.Space --from Design.Variable --from Dotted.Notation --from Edition.Approval.Token --from Edition.Trigger.User.Gated --from Explicit.Namespace --from Gr.Req --from Grounding.Hugentic.Authority --from Hugentic.Concept --from Independent.Reader.Block --from InContext.Index.Chat.Capture --from Index.Agendix --from Index.Appendix --from Index.Chapter --from Index.Chat.Capture --from Index.Depot --from Index.Discovery --from Index.Edit.Action --from Index.Edit.Modify.Line --from Index.Enrichment --from Index.Grounding --from Index.Line --from Index.Linking --from Index.Linter --from Index.Ontology --from Index.Skillware --from Index.Surface --from Kernel.Block --from Kernel.Line --from Kernel.Writing --from Line.Type --from Line.Type.Vocabulary --from Line.Verbatim.Gate --from Name.As.Index --from Not.A.Wall.Of.Text --from Package.Aux.Skill --from Packages.Master.Agent --from Producer.Aids.Checker --from Reviewed.Cite.Closure --from Reviewed.Content --from Skill.Module --from Touched.Authority --from Touched.Surface.Index --from User.Attention --from User.Command --from User.Command.Arg --from User.Command.Section --from User.Command.Trigger --from User.Touched --from Verbatim.User.Gated --from Workflow.Neutral --from Writing.Friction.Reduction

# Index.Context.Assembly

`Index.Context.Assembly` is the whole-file `Context.Assembly.Module` containing the complete shared subject context for developing any managed `agentos-index` surface. Every consumer builder loads this module; running agents continue to load only the operational modules selected by their actual workflows.

The assembly is a development context boundary, not an import mediator. Consumers remain free to depend on, copy, derive, cite, or omit covered material according to their own purpose.

## Subject Universe

Close every category below before developing an `agentos-index` consumer:

1. **Index system.** Load the owning blocks and available appendix depth for `Agentos.Index.System`, `Index.Skillware`, `Index.Surface`, `Index.Ontology`, `Index.Depot`, `Index.Chapter`, `Index.Appendix`, `Index.Agendix`, and `Index.Discovery`.
2. **Writing model.** Load `Kernel.Writing`, `Kernel.Block`, `Kernel.Line`, `Index.Line`, `Line.Type`, `Line.Type.Vocabulary`, `Dotted.Notation`, `Name.As.Index`, `Independent.Reader.Block`, `Cited.Duplication`, and `Not.A.Wall.Of.Text`.
3. **Grounding model.** Load `Context.Grounding`, `Index.Grounding`, `Index.Linking`, `Index.Chat.Capture`, `InContext.Index.Chat.Capture`, `Anchory.System`, `Grounding.Hugentic.Authority`, `Touched.Authority`, `Touched.Surface.Index`, `Reviewed.Cite.Closure`, and `Demoted.Anchored.Line`.
4. **Workflow and gate model.** Load `Workflow.Neutral`, `Alignment.Mode`, `Alignment.Surface`, `Edition.Trigger.User.Gated`, `Verbatim.User.Gated`, `Line.Verbatim.Gate`, `Edition.Approval.Token`, `Reviewed.Content`, `Capture.Gradient`, `Capture.Offer`, `User.Touched`, `User.Attention`, `User.Command`, `User.Command.Trigger`, `User.Command.Arg`, and `User.Command.Section`.
5. **Operations and validation.** Load `Index.Edit.Action`, `Index.Edit.Modify.Line`, `Index.Enrichment`, `Index.Linter`, `Producer.Aids.Checker`, `Appendix.Discovery`, `Gr.Req`, and the current managed modules under `references/` whose behavior the consumer composes or routes.
6. **Skill context.** Load `Batchy.Skill`, `Package.Aux.Skill`, `Skill.Module`, `Packages.Master.Agent`, `Concept.Hardness`, `Design.Space`, `Design.Variable`, `Explicit.Namespace`, `Hugentic.Concept`, and `Writing.Friction.Reduction` where the consumer uses those boundaries.

## Development Discipline

- treat the covered set as the common universe a builder knows, not as content every consumer must reproduce
- inspect the consumer's direct dependencies and intent after loading the assembly, then choose its materialization and citation behavior locally
- follow related routed concepts and appendix depth when a direct block leaves a material decision unresolved
- keep builder assemblies distinct from workflow-selected runtime context modules such as `Index.Capture.Context.Module`
- re-check the package after changing dependencies because coverage supervision is a semantic POI, not a parser failure

## Runtime Boundary

`Index.Context.Assembly` does not enter running-agent context merely because a builder used it. Runtime loading remains selective through the `agentos-index` router, explicit skill arguments, and the active workflow's own modules.
