# Index.Linter — Appendix

****

## Index.Linter/Config.NoSurfaces

- emitted when no lint target is configured
- normal use is `--depot`; explicit surface paths exist only for advanced or partial linting
- fix by passing a depot root, or an explicit surface path when doing partial linting

****

## Index.Linter/Surface.IndexMissing

- emitted when a configured `--index` path does not exist
- the path is resolved from the current working directory unless absolute
- fix by correcting the path or creating the intended index scope

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

- fallback emitted when the shared markdown-block parser reports a structural issue without a first-class linter code
- most known mdblocks issues are promoted to `Index.Linter/Block.*` codes
- details include the underlying mdblocks source code for the specific syntax condition

****

## Index.Linter/Block.NoHeadings

- emitted when a markdown file contains no headings in the configured heading range
- usually means a non-index document is inside a linted surface, or the file is an empty shell
- fix by moving the file out of the linted surface, adding the intended block heading, or passing a narrower file set

****

## Index.Linter/Block.UnclosedCodeFence

- emitted when a file appears to contain an unclosed fenced code block
- unclosed fences make heading and separator parsing unreliable
- fix by closing the code fence before interpreting downstream block findings

****

## Index.Linter/Block.SeparatorOutsideSemantics

- emitted when a `****` separator is not consumed as a block opening or closing boundary
- common causes are a separator followed by plain text, duplicate separators, or misplaced structural markers
- fix by placing separators immediately before block headings and after block bodies

****

## Index.Linter/Block.EmptyHeading

- emitted when a heading title is empty after markdown sanitization
- empty headings cannot name index concepts or appendix sections
- fix by naming the heading or removing the empty heading marker

****

## Index.Linter/Block.TooLong

- emitted when a separator-anchored block exceeds the hard block line limit
- details include `line_span`, `max_block_lines`, and `end_line`
- fix by splitting depth into scoped appendix blocks or moving non-fundamental detail out of the block

****

## Index.Linter/Block.DuplicateHeading

- emitted when a file repeats the same heading title at the same markdown level
- duplicate local headings are usually ambiguous for block search and citation
- fix by merging, renaming, or scoping one of the repeated headings

****

## Index.Linter/Block.UnanchoredSection

- emitted when an H2-H6 heading appears outside a separator-anchored block
- plain starting text before the first block is allowed
- the depot router `000-INDEX.md` is exempt because its sections are control-plane structure, not concept blocks
- fix by wrapping the section in a block using `****`, or by moving non-block content outside H2-H6 headings

****

## Index.Linter/Router.Missing

- emitted when configured surfaces include no depot-root router file
- the required router is `000-INDEX.md` at the `Index.Depot` root
- fix by adding `000-INDEX.md`, pointing `--depot` at the depot root, or including a surface that belongs to a depot with that router

****

## Index.Linter/Router.LegacyName

- emitted when a depot contains a legacy router filename such as `000-index.md` or `001-index.md`
- the only valid router name is `000-INDEX.md` at the `Index.Depot` root
- fix by renaming the legacy router to `000-INDEX.md` and placing it at the depot root

****

## Index.Linter/Router.Empty

- emitted when the depot router `000-INDEX.md` exists but is empty
- the router should provide concept-to-file routing for the index depot
- fix by adding routing entries or removing the empty router from the linted depot

****

## Index.Linter/Index.InvalidFilename

- emitted when an index markdown file does not match the chapter filename convention
- chapter files use `NNN-<chapter>.md`, where `<chapter>` matches the containing folder name
- fix by renaming the file to match its chapter folder or moving non-index markdown out of the linted index scope

****

## Index.Linter/Concept.InvalidHeading

- emitted when an index block heading does not match the current `Block.Path` pattern
- a valid heading starts with a rooted `Dotted.Notation` concept and may continue with `/` segments for concept refs or free labels
- fix by renaming the heading to a valid `Block.Path`, or by updating the grammar if the design intentionally permits the form

****

## Index.Linter/Concept.Inventory

- used as a blocked-check dependency when concept inventory cannot be trusted or is unavailable
- this code is not usually emitted as a direct finding
- fix markdown block syntax errors or add discoverable concept blocks before interpreting dependent checks

****

## Index.Linter/Concept.InventoryEmpty

- emitted when a configured index scope contains no separator-anchored concept blocks
- downstream concept, router, and appendix checks may be blocked when the concept inventory is unavailable
- fix by adding concept blocks or pointing the linter at the correct index chapter files

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
- fix by adding the concept block, correcting the filename, or including the owning index scope in the lint run

****

## Index.Linter/Appendix.RouteAnnotationMissing

- emitted when a routed concept has appendix pages but the router entry has no `[+N]` annotation
- annotations expose appendix depth at the router surface
- fix by adding `[+N]` to the routed concept, where `N` is the contiguous appendix page count

****

## Index.Linter/Appendix.RouteAnnotationStale

- emitted when a router `[+N]` annotation does not match discovered appendix page depth
- stale annotations mislead agents about available depth for the concept
- fix by updating the annotation to the expected count reported by the linter

****

## Index.Linter/Appendix.PageGap

- emitted when appendix page files for a concept are non-contiguous
- expected pages are `Concept.Name-appendix.md`, then `Concept.Name-appendix-2.md`, `Concept.Name-appendix-3.md`, and so on without gaps
- fix by adding the missing page file, renaming the later page, or consolidating the appendix material

****

## Index.Linter/Router.InvalidConcept

- emitted when a router entry contains a concept name that does not match the current `Block.Path` pattern
- routed concepts use the same heading grammar as index block headings
- fix by correcting the routed concept name or by updating the grammar if the form is intentional

****

## Index.Linter/Router.EntriesEmpty

- emitted when router files exist but no routing entries can be parsed from them
- this usually means the routing table is missing or does not match the expected bullet format
- fix by adding entries like ``- `design/100-design.md` — Concept.Name`` to the router

****

## Index.Linter/Router.MissingEntry

- emitted when a discovered concept block is not listed in a configured router
- routers are the compressed symbol table for index discovery
- fix by adding the concept to the appropriate router entry

****

## Index.Linter/Router.MissingFile

- emitted when a router entry points to a file that does not exist at its routed depot path
- route files are resolved depot-root-relatively from `000-INDEX.md`
- fix by correcting the route target or restoring the missing chapter file

****

## Index.Linter/Router.UnknownConcept

- emitted when a router entry points to a concept block that was not discovered
- this can mean the routed concept is stale, misspelled, or outside the configured lint scope
- fix by correcting the router, adding the missing block, or including the owning chapter file in the lint run

****

## Index.Linter/Router.WrongFile

- emitted when a router entry names a real concept but routes it to a different file than the discovered block
- fix by updating the route file or moving the concept block to the routed chapter file

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
