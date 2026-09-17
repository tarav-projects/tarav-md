# Archive as a DOI registry

<!-- tarav.sessions
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Identity commitment and resolution

The Archive is a DOI registry. A DOI is assigned once and is a semantic
commitment to the same object. The system resolves it, so the object's
location can change. The Archive can reorganize its storage and relink DOI
resolution while preserving those commitments.
<!-- tarav.context 5626cd5f:be7eb9c3d6d8a1a0 -->
<!-- tarav.context 5626cd5f:3d6f416d87eeaa4d -->
<!-- tarav.context 5626cd5f:ccd25f622704459f -->

The archivist determines the identity contract for each DOI. Tarav need not
choose one universal interpretation such as exact bytes or a particular
logical-record identity. Abstractly the contract promises that the data is
the same. Reference tooling will help deal with changes and interpret them
according to that commitment. Changed evidence that breaks the commitment
requires a new identity rather than substitution behind the old reference.
<!-- tarav.context 5626cd5f:cd87ceb69b039d5f -->
<!-- tarav.context 5626cd5f:3d6f416d87eeaa4d -->

## DOI roots and floating selectors

All archive-grade Tarav references must have a DOI root. A reference may then
select within its object: for example, a JSON-file DOI plus a subpath, or a
repository DOI plus a path. The Archive promises the DOI root; the additional
selection is floating. A root DOI does not automatically promise stable
identity for everything addressable beneath it.
<!-- tarav.context 5626cd5f:cd87ceb69b039d5f -->

The Archive issues DOIs automatically and can also issue them on demand at a
subsystem's request. Commitment is progressive. Floating selectors do not
preclude more careful reference tooling or stronger commitments where needed.
<!-- tarav.context 5626cd5f:cd87ceb69b039d5f -->

## A DOI must leave a durable record

The Archive must never destroy a DOI without leaving a record in the Archive
itself, retaining as much useful information as can be envisioned. Losing or
removing an object must not erase the record of its identity and the useful
information retained about it.
<!-- tarav.context 5626cd5f:cd87ceb69b039d5f -->

Record schemas may evolve through developer-managed changes to code and data,
as described in [Tarav as a record framework](record-framework.md). That
flexibility must coexist with each DOI's semantic commitment to the same
object; the commitment is not simply a fixed physical location.
<!-- tarav.context 5626cd5f:b1f11f560186fdb4 -->
<!-- tarav.context 5626cd5f:be7eb9c3d6d8a1a0 -->
<!-- tarav.context 5626cd5f:3d6f416d87eeaa4d -->
