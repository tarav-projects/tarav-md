# Record Archive

<!-- tarav.sessions
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

## Archive-owned navigation

The Archive exposes one navigable tree starting at a global `TaravArchive`. `ls()` returns `ArchiveEntry` objects and `cd()` follows placements. Each entry is a TaravObject representing its position in the Archive tree. It can wrap another TaravObject, including a Workflow or typed Archive, without requiring that contained object to know the Archive path. A path-only grouping can be represented by its entry without retaining another Record on disk.
<!-- tarav.breadcrumb 4c4687944586 -->
<!-- tarav.breadcrumb d87d89d19603 -->
<!-- tarav.breadcrumb 72c3b160dd8c -->

Archive navigation is one Workflow-defined graph across TaravObjects. It complements the Type-to-Workflow relationship and `context(obj)`; these paths can overlap at the same object without making its Archive placement part of its identity.
<!-- tarav.breadcrumb 243d0d929710 -->
<!-- tarav.breadcrumb 83fcc7c41df5 -->

## Workflow partitions and typed storage

The first Archive level beneath the root is addressed by the Workflow Ship, not its mutable `workflow_name`. Archive code may resolve the Ship to the registered Workflow and present its readable name. `ARCHIVE.for_workflow(WorkflowType)` supplies the partition handler and its standard path without creating data. The Workflow then chooses its own child names, such as a test run UUID, and creates typed Archives inside that partition.
<!-- tarav.breadcrumb 0726266f6af0 -->
<!-- tarav.breadcrumb 71b52cf62e4e -->
<!-- tarav.breadcrumb 4689fafab3ef -->

`DictionaryArchive` and `VectorArchive` are typed directory Records. Their `main.json` represents the Archive Entity with its identity and constitution; `entries.json` separately indexes names or ordered positions to stored object paths. The Workflow partition and optional grouping directories need no retained `main.json` solely to be navigable.
<!-- tarav.breadcrumb d9fc0491d608 -->
<!-- tarav.breadcrumb d31f7445d9e6 -->

## Git configuration below the Workflow boundary — proposed

Git repository boundaries should be configurable from children of the Workflow Ship partition downward. The Workflow partition itself must not host a repository; the design explicitly discourages one repository for all of a Workflow's data. By default, creating a child should use the nearest parent repository within that Workflow subtree, or initialize a repository at the child when none exists before the Workflow boundary. An explicit local choice can override this default.
<!-- tarav.breadcrumb 8b1f754acbb0 -->
<!-- tarav.breadcrumb f4a1f1a45121 -->

`git-config.json` may live at any relevant Archive level, including the Workflow partition as policy for descendants, without making that level a Git repository. A lower-level file may override inherited configuration. `.gitignore` remains a native Git file, while Archive code should expose its expected path and whether it exists. A `.gitignore` outside a repository rooted at a child does not govern that repository; workflow-wide ignore defaults would need to be applied inside each new repository. The effective configuration and its source should be inspectable.
<!-- tarav.breadcrumb e1c03cff0fbc -->
<!-- tarav.breadcrumb 70df72ace507 -->

The Git policy and configuration interface are candidate design. The current Python slice still runs `git init` in each typed Archive, so sibling Dictionary and Vector Archives have separate repositories until that behavior is changed.
<!-- tarav.breadcrumb 58ed3ee7dec8 -->
