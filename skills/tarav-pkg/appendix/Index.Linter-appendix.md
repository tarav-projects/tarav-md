# Index.Linter — Appendix

****

## Index.Linter/Check.ConfigSurfaces

- check that validates configured lint targets and explicit surface paths
- can emit config and surface findings
- downstream checks use its findings to avoid cascading errors

****

## Index.Linter/Check.DiscoverFiles

- check that expands configured files and directories into markdown files
- can emit `Index.Linter/Files.None`
- blocked when no configured surface is valid

****

## Index.Linter/Check.MdblocksSyntax

- check that delegates structural markdown-block validation to the shared mdblocks parser
- can emit `Index.Linter/Mdblocks.Syntax`
- blocked when markdown files have not been discovered

****

## Index.Linter/Check.BlockSections

- check that verifies H2-H6 sections are separator-anchored concept or appendix blocks
- can emit `Index.Linter/Block.UnanchoredSection`
- intentionally ignores starting prose before the first block and the depot router `000-INDEX.md`

****

## Index.Linter/Check.RouterPresence

- check that verifies each linted depot has a depot-root router file
- can emit `Index.Linter/Router.Missing`, `Index.Linter/Router.LegacyName`, or `Index.Linter/Router.Empty`
- blocked when no valid index scope is configured

****

## Index.Linter/Check.IndexFilenames

- check that verifies index chapter filenames match the chapter naming convention
- can emit `Index.Linter/Index.InvalidFilename`
- blocked when no valid index scope is configured

****

## Index.Linter/Check.ConceptInventory

- check that extracts separator-anchored concept blocks from index chapter files
- can emit `Index.Linter/Concept.InvalidHeading` or `Index.Linter/Concept.InventoryEmpty`
- downstream duplicate, router, and appendix checks depend on this inventory

****

## Index.Linter/Check.ConceptDuplicates

- check that verifies discovered index concept headings are unique inside the configured lint scope
- can emit `Index.Linter/Concept.Duplicate`
- blocked when concept inventory is unavailable

****

## Index.Linter/Check.AppendixFilenames

- check that verifies appendix filenames follow the concept appendix convention
- can emit `Index.Linter/Appendix.InvalidFilename`
- blocked when no configured surface is valid

****

## Index.Linter/Check.AppendixOrphans

- check that verifies appendix files have matching configured index concept blocks
- can emit `Index.Linter/Appendix.Orphan`
- blocked when concept inventory is unavailable

****

## Index.Linter/Check.RouterEntries

- check that parses router entries into concept-to-file routes over depot-root-relative chapter paths
- parses optional `[+N]` appendix depth annotations while normalizing routed concepts
- can emit `Index.Linter/Router.InvalidConcept` or `Index.Linter/Router.EntriesEmpty`
- blocked when router or concept inventory is unavailable

****

## Index.Linter/Check.AppendixRouteAnnotations

- check that compares routed `[+N]` annotations with discovered appendix page inventory
- can emit `Index.Linter/Appendix.RouteAnnotationMissing`, `Index.Linter/Appendix.RouteAnnotationStale`, or `Index.Linter/Appendix.PageGap`
- blocked when concept, router, or appendix filename inventory is unavailable

****

## Index.Linter/Check.RouterCoverage

- check that verifies discovered concept blocks are present in configured routers
- can emit `Index.Linter/Router.MissingEntry`
- blocked when router or concept inventory is unavailable

****

## Index.Linter/Check.RouterTargets

- check that verifies router entries point to existing files and discovered concept blocks
- can emit `Index.Linter/Router.MissingFile`, `Index.Linter/Router.UnknownConcept`, or `Index.Linter/Router.WrongFile`
- blocked when router or concept inventory is unavailable

****

## Index.Linter/External.Checks

- [DC] the linter exposes an external-check socket; the chatlas grounding-provenance bridge registers through it at the composition root — anchors must resolve and land on user turns (`AS:`-marked lines excepted, agendix only)
- [DC] core `Line.Type` checks run without chatlas: bracket syntax and known act codes (warnings); `AS:` outside `agendix/` is `Index.Linter/Source.Axis.Placement`, an error
- [DC] a missing chatlas backend renders `Index.Linter/Grounding.Provenance` as a blocked check — visible, never silently skipped
