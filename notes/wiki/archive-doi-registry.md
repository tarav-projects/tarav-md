# Archive as a DOI registry

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Identity commitment and resolution

The Archive is a DOI registry. A DOI is assigned once and is a semantic
commitment to the same object. The system resolves it, so the object's
location can change. The Archive can reorganize its storage and relink DOI
resolution while preserving those commitments.
<!-- tarav.breadcrumb a3521d5c1f98 -->
<!-- tarav.breadcrumb c0793fd011c9 -->
<!-- tarav.breadcrumb c4c726b7eef2 -->

The archivist determines the identity contract for each DOI. Tarav need not
choose one universal interpretation such as exact bytes or a particular
logical-record identity. Abstractly the contract promises that the data is
the same. Reference tooling will help deal with changes and interpret them
according to that commitment. Changed evidence that breaks the commitment
requires a new identity rather than substitution behind the old reference.
<!-- tarav.breadcrumb 9d01f0120aec -->
<!-- tarav.breadcrumb d66f1be1e9a0 -->

## DOI roots and floating selectors

All archive-grade Tarav references must have a DOI root. A reference may then
select within its object: for example, a JSON-file DOI plus a subpath, or a
repository DOI plus a path. The Archive promises the DOI root; the additional
selection is floating. A root DOI does not automatically promise stable
identity for everything addressable beneath it.
<!-- tarav.breadcrumb 8b93a6713c57 -->

The Archive issues DOIs automatically and can also issue them on demand at a
subsystem's request. Commitment is progressive. Floating selectors do not
preclude more careful reference tooling or stronger commitments where needed.
<!-- tarav.breadcrumb f67ebe37a674 -->

## Lightweight descriptions and adjustable preservation

The Archive is the main, but not the only, provider of stable storage and
references in Tarav. Lightweight Records make it practical to commit to
retaining descriptions longer without committing comparable resources to
the Artifacts themselves. Archive-issued Records are designed with long-term
storage in mind.
<!-- tarav.breadcrumb 41a2b400c8ea -->

A file's descriptive Records can retain content hashes, paths, prefixes or
tails, timestamps, and other metadata or hints. If the file is lost or deleted,
those Records still preserve something useful and may support searching for
and identifying the file or a close version. Preserving knowledge about an
Artifact is distinct from preserving the Artifact itself.
<!-- tarav.breadcrumb e4dc56ab0c02 -->
<!-- tarav.breadcrumb f7e6673a92c4 -->

This permits adjustable resource commitments: descriptions can become cheaper
under resource constraints or richer when resources permit. Records provide
a way to describe the surrounding world while regulating how much retention
costs, rather than requiring all-or-nothing preservation.
<!-- tarav.breadcrumb 43df499ef370 -->
<!-- tarav.breadcrumb 2593edde30c2 -->

## Composable preservation capabilities

The Archive can provide primitives and typed Records through which subsystems
commit Artifacts with different semantics. It need not itself impose one
universal distinction between an object and its editions. For example, a file
can be committed under a Git repository, using Git's edition capabilities.
Observation and edition semantics are built on the Record primitives rather
than required of every Record.
<!-- tarav.breadcrumb 106bcd75765e -->

The Archive can offer concrete preservation capabilities while leaving
subsystems free to choose and combine them. This is part of Tarav's role as
a framework library.
<!-- tarav.breadcrumb a0d2dc59b6c9 -->

## A DOI must leave a durable record

The Archive must never destroy a DOI without leaving a record in the Archive
itself, retaining as much useful information as can be envisioned. Losing or
removing an object must not erase the record of its identity and the useful
information retained about it.
<!-- tarav.breadcrumb 43959c301154 -->

Record schemas may evolve through developer-managed changes to code and data,
as described in [Tarav as a record framework](record-framework.md). That
flexibility must coexist with each DOI's semantic commitment to the same
object; the commitment is not simply a fixed physical location.
<!-- tarav.breadcrumb 84b85de4bb8c -->
<!-- tarav.breadcrumb f24b00b98d4f -->
<!-- tarav.breadcrumb f0d66cfe2920 -->

## Typed registry boundary — 2026-10-22

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

The User narrowed the first Archive implementation to a registry returning typed
DOI objects. The DOI Type states the continuity and maintenance contract.
Locators describe known ways to reach the resource; compact recognition hints
help maintainers and consumers assess candidate identity. Consumers own access
and interpretation. Registry lookup itself does not retrieve the external
resource, pick a replacement or automatically repair its location. Multiple
locations may describe the same resource; maintainers explicitly declare updates.
<!-- tarav.breadcrumb 8af98748aef3 -->
<!-- tarav.breadcrumb 975f9e10897d -->

Artifact immutability describes Archive's maintenance authority. Archive does not
own the shape of external resources or mutate them; their owners may change them
while a typed DOI continues tracking their identity. DOI Records, schemas,
locators and hints are Archive-owned and amendable. A repository DOI may identify
the continuing repository across checkouts, whereas a stricter contract can
identify a particular state. Consumers can retain observations of the registry
information and decide how to respond to subsequent changes.
<!-- tarav.breadcrumb e65b0f30ce3f -->

The User requested a simple replacement of the old Archive implementation after
inspection, retaining useful ideas and preserving any displaced data losslessly
in the Attic. Retired code should leave the active codebase rather than remain as
compatibility infrastructure. Artifact hosting and general recovery are deferred.
<!-- tarav.breadcrumb 390c3674dbdb -->
<!-- tarav.breadcrumb 4cb9c9ddeb13 -->

The resulting design requests are [Python 942](../../../tarav-py/notes/live/942-archive-doi-registry-impl-req.md)
and [Markdown 870](../live/870-archive-doi-contracts-impl-req.md). Their implementation
has not started. Inspection of the active default Archive and Record Registry
roots found shared Record Archive data and no old artifact registration records;
that data remains in place. Exact inventory scope and counts are retained in 942.

## Registry implementation and independent locator checks — 2026-10-22

The User requested execution of request 942 and added that Archive should check
broken links and surface its own actions in the System Project. This maintenance
path is separate from reading DOI information and does not perform resolution
on behalf of consumers or automatically change locator declarations.
<!-- tarav.breadcrumb c10ed2fed2ae -->

Implemented in `tarav.l1.archive`: DOI and RepositoryDOI declare identity
contracts; LocalLocator/RemoteLocator carry reachability information;
RepositoryHints retains at most ten commit hashes. The registry uses its
standard RecordMap partition, supports explicit register/read/update/list,
and returns typed DOI objects through DOIReference. Its CLI is now
`tarav archive init|register|show|list|update|repository`. General Record Archive
and Attic retain their own storage and identities. The old registration,
materialization and artifact-fetching code and migration utilities were retired.

`ArchiveLocatorSuite` is composed into `TaravSystemProject.Checks`. Local path
absence and HTTP 404/410 produce missing-locator findings. Other transport or
access errors are distinguished as unreachable. HTTP probes use HEAD, a
three-second timeout, no response-body download and no redirect following.
Other hosts, unsupported protocols, authentication and unsupported HEAD replies
remain unassessed. Archive-owned actions use the ordinary System Project
lifecycle; incomplete checks do not assert that an earlier finding disappeared.

Verification recorded in [942](../../../tarav-py/notes/live/942-archive-doi-registry-impl-req.md):
72 focused integration tests passed, including opening an action, retaining it
through unassessed checks and closing it on recovery. The installed CLI smoke
passed against an absent-resource fixture. Constitution and candidate Archive
sources were rebuilt through SKW. The full Project run also exposed unrelated
Chatlas/Kernel test findings, tracked separately in the request log.

The final full Project recheck completed 80 checks with no incomplete checks;
all 62 pytest suites passed. The earlier test findings disappeared. Only the
existing Gitleaks flag and two synthetic test-marker findings remain. New
implementation evidence links audited cleanly; ten older Architecture links
still report unavailable/amended Chatlas turns and were preserved as found.

## Repository references and Change-ID — 2026-10-22

The User requested repository-specialized Archive references integrated with
tarav-change before Notebook adopts them. Repository identity and action
ownership are independent: multiple repositories may belong to one Project.
<!-- tarav.breadcrumb fc2cd350d770 -->

`RepositoryReference` retains a registry, repository DOI, exact commit and tree,
plus optional Change-ID and relative file path. Its lookup returns the maintained
declaration and coordinates without accessing Git. The explicit consumer in
`tarav.l2.git.archive` captures from a declared local repository and resolves
locally: use the original commit, or find Change-ID candidates and accept exactly
one with the captured tree. Mismatches and ambiguity remain failures. Original
coordinates are never rewritten. The full tree includes `.tarav/changes`.

Witnesses now use repository DOI and branch; Project is ownership metadata.
The existing tarav-py witness migrated explicitly, preserving original bytes
in Attic. Ordinary repositories can install hooks with `--repo` and
`--owner-project`; the owner's checks revisit bound external repositories.
See [request 943](../../../tarav-py/notes/live/943-repository-doi-change-references-impl-req.md)
and [tarav-change](tarav-change.md#repository-identity-and-owner--2026-10-22).

Verification passed all 64 pytest suites in the full Python Project run, with
82 completed checks and none incomplete. The first real implementation commit
updated the migrated witness correctly. All 15 captured surfaces audited clean.
Five unrelated Project findings remained; their details are in request 943.
