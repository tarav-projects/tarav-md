****

## Reviewed.Cite.Closure/Agendix/Linter.Enforcement

- [DC] the closure is enforced as an `Index.Linter` check (`reviewed-cite-closure`): a reviewed surface addressing a real agendix block raises an error, not blessable ^c20260725-114u
- [DF] "citing the agendix" is addressing a specific agendix block by its `Block.Path` (a content dependency) — not naming the surface: a bare `agendix/…md` file mention, as the `Index.Agendix` definition itself uses, is not a cite ^c20260725-122u
- [DC] v1 is surface-level: the agendix directory is the unreviewed surface, and the check resolves each cite against the depot's real agendix blocks, so format-description placeholders (`Concept.X/Agendix/…`) never fire ^c20260725-120u
- [CT] scope is index surfaces — the only surface today carrying a reviewed/unreviewed split; line-level review status is the growth path ^c20260725-83u
