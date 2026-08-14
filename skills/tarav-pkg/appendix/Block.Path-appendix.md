****

## Block.Path/Appendix

- resolution is soft and per-segment — concept segments gain meaning, label segments stay plain
- the path need not mirror the file system, but by default it does — `Concept.X/Y` resolves into `Concept.X`'s appendix file
- inside an appendix file the root is implicit — `Concept.X-appendix.md` roots every block at `Concept.X`, so a heading `Appendix` is the full path `Concept.X/Appendix`, `Concept.Y` is `Concept.X/Concept.Y`
- `./Child` abbreviates a child of the current root, legal only where a root is already established — the `namespace-members` list and appendix-file headings; in free prose spell the full `Block.Path`
- the outblock form of a `Kernel.Block.Section` is a path-named block — `Concept.X/Grounding` is the grounding section, outblock

****

## Block.Path/Concept.Scoping

- `Concept.Scoping` is the semantics of a concept-valued `Block.Path` segment — the block is hosted under that concept, viewed through its lens
- it captures a relationship that belongs to neither concept alone, read in the host's context
- the same concept can be hosted by several paths, each a distinct view
- example: `Agentos.Index.System/Index.Surface.Layout`
