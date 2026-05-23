# Index.Linter — Appendix

****

## Index.Linter/Config.NoSurfaces

- emitted when no `--index` or `--appendix` paths are configured
- the linter explicit mode requires at least one surface path to process
- fix by passing one or more index or appendix files/directories

****

## Index.Linter/Surface.IndexMissing

- emitted when a configured `--index` path does not exist
- the path is resolved from the current working directory unless absolute
- fix by correcting the path or creating the intended index surface

****

## Index.Linter/Surface.AppendixMissing

- emitted when a configured `--appendix` path does not exist
- the path is resolved from the current working directory unless absolute
- fix by correcting the path or creating the intended appendix surface

****

## Index.Linter/Surface.IndexNotMarkdown

- emitted when a configured `--index` file is not a markdown file
- files passed explicitly must end in `.md`; directories may contain markdown files
- fix by passing a markdown file or an index directory

****

## Index.Linter/Surface.AppendixNotMarkdown

- emitted when a configured `--appendix` file is not a markdown file
- files passed explicitly must end in `.md`; directories may contain markdown files
- fix by passing a markdown file or an appendix directory

****

## Index.Linter/Surface.IndexInvalid

- emitted when a configured `--index` path is neither a markdown file nor a directory
- fix by passing a valid markdown file or directory path

****

## Index.Linter/Surface.AppendixInvalid

- emitted when a configured `--appendix` path is neither a markdown file nor a directory
- fix by passing a valid markdown file or directory path

****

## Index.Linter/Surface.Invalid

- used as a blocked-check dependency when no configured surface is valid
- this code is not usually emitted as a direct finding
- fix the preceding surface path errors before interpreting downstream blocked checks

****

## Index.Linter/Files.None

- emitted when configured valid surfaces contain no markdown files
- the linter can run on files or directories, but only markdown files are processed
- fix by pointing at markdown files or directories containing markdown files

****

## Index.Linter/Mdblocks.Syntax

- emitted when the shared markdown-block parser reports a structural issue
- covers syntax such as orphan separators, empty headings, unclosed fences, and overlong blocks
- details include the underlying mdblocks source code for the specific syntax condition

****

## Index.Linter/Block.UnanchoredSection

- emitted when an H2-H6 heading appears outside a separator-anchored block
- plain starting text before the first block is allowed
- router files are exempt because their sections are control-plane structure, not concept blocks
- fix by wrapping the section in a block using `****`, or by moving non-block content outside H2-H6 headings

****

## Index.Linter/Router.Missing

- emitted when configured index paths include no router file
- router files are currently `000-index.md` or `001-index.md`
- fix by including the router file in explicit file mode or pointing at the containing index directory

****

## Index.Linter/Router.Empty

- emitted when a router file exists but is empty
- the router should provide concept-to-file routing for the index surface
- fix by adding routing entries or removing the empty router from the configured lint surface

****

## Index.Linter/Index.InvalidFilename

- emitted when an index markdown file does not match the flat index filename convention
- expected ordinary names use `NNN-index.md`; routers use `000-index.md` or `001-index.md`
- fix by moving non-index markdown out of the index surface or renaming valid index files

****

## Index.Linter/Concept.InvalidHeading

- emitted when an index block heading does not match the current concept-name pattern
- index headings should name concepts using `Dotted.Notation`, optional parameterization, or scoped appendix notation
- fix by renaming the heading or updating the concept-name grammar if the design intentionally permits the form

****

## Index.Linter/Concept.Inventory

- used as a blocked-check dependency when concept inventory cannot be trusted or is unavailable
- this code is not usually emitted as a direct finding
- fix markdown block syntax errors or add discoverable concept blocks before interpreting dependent checks

****

## Index.Linter/Concept.InventoryEmpty

- emitted when a configured index surface contains no separator-anchored concept blocks
- downstream concept, router, and appendix checks may be blocked when the concept inventory is unavailable
- fix by adding concept blocks or pointing the linter at the correct index files

****

## Index.Linter/Concept.Duplicate

- emitted when the same concept heading appears in more than one configured index block
- a concept should have one authoritative index block per index depot
- fix by merging duplicates, scoping one occurrence, or moving detail into appendix material

****

## Index.Linter/Appendix.InvalidFilename

- emitted when an appendix markdown file does not match the appendix filename convention
- expected names use `Concept.Name-appendix.md` or paged forms such as `Concept.Name-appendix-2.md`
- fix by renaming the appendix file or moving non-appendix markdown out of the appendix surface

****

## Index.Linter/Appendix.Orphan

- emitted when an appendix file has no matching configured index concept block
- appendix discovery starts from an index concept, so orphaned appendix material may be undiscoverable
- fix by adding the concept block, correcting the filename, or linting the owning index surface too

****

## Index.Linter/Router.InvalidConcept

- emitted when a router entry contains a concept name that does not match the current concept-name pattern
- the router should use the same concept grammar as index block headings
- fix by correcting the routed concept name or updating the grammar if the form is intentional

****

## Index.Linter/Router.EntriesEmpty

- emitted when router files exist but no routing entries can be parsed from them
- this usually means the routing table is missing or does not match the expected bullet format
- fix by adding entries like ``- `100-index.md` — Concept.Name`` to the router

****

## Index.Linter/Router.MissingEntry

- emitted when a discovered concept block is not listed in a configured router
- routers are the compressed symbol table for index discovery
- fix by adding the concept to the appropriate router entry

****

## Index.Linter/Router.MissingFile

- emitted when a router entry points to a file that does not exist beside the router
- fix by correcting the route target or restoring the missing index file

****

## Index.Linter/Router.UnknownConcept

- emitted when a router entry points to a concept block that was not discovered
- this can mean the routed concept is stale, misspelled, or outside the configured lint surface
- fix by correcting the router, adding the missing block, or including the owning index file in the lint run

****

## Index.Linter/Router.WrongFile

- emitted when a router entry names a real concept but routes it to a different file than the discovered block
- fix by updating the route file or moving the concept block to the routed file

****

## Index.Linter/Check.ConfigSurfaces

- check that validates the explicit `--index` and `--appendix` configuration surface paths
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
- intentionally ignores starting prose before the first block and router control files

****

## Index.Linter/Check.RouterPresence

- check that verifies configured index surfaces include a router file
- can emit `Index.Linter/Router.Missing` or `Index.Linter/Router.Empty`
- blocked when no valid index surface is configured

****

## Index.Linter/Check.IndexFilenames

- check that verifies index markdown filenames match the index naming convention
- can emit `Index.Linter/Index.InvalidFilename`
- blocked when no valid index surface is configured

****

## Index.Linter/Check.ConceptInventory

- check that extracts separator-anchored concept blocks from index files
- can emit `Index.Linter/Concept.InvalidHeading` or `Index.Linter/Concept.InventoryEmpty`
- downstream duplicate, router, and appendix checks depend on this inventory

****

## Index.Linter/Check.ConceptDuplicates

- check that verifies discovered index concept headings are unique inside the configured lint surface
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

- check that parses router entries into concept-to-file routes
- can emit `Index.Linter/Router.InvalidConcept` or `Index.Linter/Router.EntriesEmpty`
- blocked when router or concept inventory is unavailable

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
