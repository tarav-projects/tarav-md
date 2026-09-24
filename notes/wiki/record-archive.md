# Record Archive

<!-- tarav.sessions
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

## Archive-owned navigation

The Archive exposes one navigable tree starting at a global `TaravArchive`. `ls()` returns `ArchiveEntry` objects and `cd()` follows placements. Each entry is a TaravObject representing its position in the Archive tree. It can wrap another TaravObject, including a Workflow or typed Archive, without requiring that contained object to know the Archive path. A path-only grouping can be represented by its entry without retaining another Record on disk.
<!-- tarav.breadcrumb 4c46879445861fd20115515cbe8871358a61e75a565ed5d7f6fb93ae7db36e8e -->
<!-- tarav.breadcrumb d87d89d196030299d00a38a67b16d1033d7400a32e0df7224ce6bf5786cae0df -->
<!-- tarav.breadcrumb 72c3b160dd8c5e87a4059eebf3aa95ae03796cf0737bb9e5662e1ebd1a82d5d7 -->

Archive navigation is one Workflow-defined graph across TaravObjects. It complements the Type-to-Workflow relationship and `context(obj)`; these paths can overlap at the same object without making its Archive placement part of its identity.
<!-- tarav.breadcrumb 243d0d929710afe923b31687bd45ef2a8964f17b8fabb1eaa7635812f1ab632b -->
<!-- tarav.breadcrumb 83fcc7c41df51cafdb05141b766e6596df5fbcafa59c14c3562e9fdccfa4f50f -->

## Workflow partitions and typed storage

The first Archive level beneath the root is addressed by the Workflow Ship, not its mutable `workflow_name`. Archive code may resolve the Ship to the registered Workflow and present its readable name. `ARCHIVE.for_workflow(WorkflowType)` supplies the partition handler and its standard path without creating data. The Workflow then chooses its own child names, such as a test run UUID, and creates typed Archives inside that partition.
<!-- tarav.breadcrumb 0726266f6af022b870a0dc9712ebdff34feb42b461c4450338ecb72dbb811ecc -->
<!-- tarav.breadcrumb 71b52cf62e4e41142e45f18c4a8a47d1815d8234ae63809b7583dec1f29c3a5a -->
<!-- tarav.breadcrumb 4689fafab3ef9969aa34d909d02e4473fc31718cb66c3ec6492ab47a73e1da48 -->

`DictionaryArchive` and `VectorArchive` are typed directory Records. Their `main.json` represents the Archive Entity with its identity and constitution; `entries.json` separately indexes names or ordered positions to stored object paths. The Workflow partition and optional grouping directories need no retained `main.json` solely to be navigable.
<!-- tarav.breadcrumb d9fc0491d60832ece847a8daae43a4e4200892d1b13a178373e260c998cec195 -->
<!-- tarav.breadcrumb d31f7445d9e6b8c14e5253a43e6e84d20d1da10c81575d726d3d2bd4a4742c64 -->

## Git configuration below the Workflow boundary — proposed

Git repository boundaries should be configurable from children of the Workflow Ship partition downward. The Workflow partition itself must not host a repository; the design explicitly discourages one repository for all of a Workflow's data. By default, creating a child should use the nearest parent repository within that Workflow subtree, or initialize a repository at the child when none exists before the Workflow boundary. An explicit local choice can override this default.
<!-- tarav.breadcrumb 8b1f754acbb09deeecea48d4d65074ef72cdd86a26911e1c0752762e0e4b4361 -->
<!-- tarav.breadcrumb f4a1f1a45121c843beabfd6aa40f5b414910b2227ae0111be9e29104b41648b2 -->

`git-config.json` may live at any relevant Archive level, including the Workflow partition as policy for descendants, without making that level a Git repository. A lower-level file may override inherited configuration. `.gitignore` remains a native Git file, while Archive code should expose its expected path and whether it exists. A `.gitignore` outside a repository rooted at a child does not govern that repository; workflow-wide ignore defaults would need to be applied inside each new repository. The effective configuration and its source should be inspectable.
<!-- tarav.breadcrumb e1c03cff0fbca2fe7f1f382a7a06ec13c2f55d304ef68a02e68a92c042e2126d -->
<!-- tarav.breadcrumb 70df72ace50730b0f915d29d6002f674657c48531fb898c86de4d53734cb9de4 -->

The Git policy and configuration interface are candidate design. The current Python slice still runs `git init` in each typed Archive, so sibling Dictionary and Vector Archives have separate repositories until that behavior is changed.
<!-- tarav.breadcrumb 58ed3ee7dec8e30d08ca5080f6ba70c336b308db056140b4329bdf19bf5fcef7 -->
