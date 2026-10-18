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
