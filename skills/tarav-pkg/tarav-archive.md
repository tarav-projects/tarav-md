# Tarav.Archive

This document describes the current candidate design of `Tarav.Archive`.
It is subordinate to the Tarav Constitution and remains amendable.

## Purpose

`Tarav.Archive` is a flat registry of Artifacts and Git-tracked Records
about them.

The Archive helps consumers determine:

- What an Artifact is.
- Which locators are known for it.
- What retained hints may help recognize, recover, or understand it.

The Archive stores Artifacts and flat Records about them; consumers
construct organization and meaning.

## Artifacts

An `Archive.Artifact` is the actual data. There is no separate Payload
concept.

For now, an Artifact must be at least one file:

- A file.
- A folder or file group.
- A Git repository.

The Archive does not parse Artifacts into semantic units. Messages,
turns, document sections, and similar internal structures belong to
consumers such as Chatlas or `Tarav.Diagram`.

Artifacts may live in Archive-managed repositories, external
repositories, external locations, or be temporarily unavailable.

## Archive Records

An `Archive.Record` is retained data about one Artifact.

Records may preserve:

- Archive registration bureaucracy.
- Current and historical locations.
- Git coordinates and observations.
- Content fingerprints and mechanical properties.
- External URLs and observation times.
- Other descriptions produced or supplied by consumers.

Records are cheap, retained aggressively, and tracked by the Archive’s
Record Git repository.

Every Record carries `recorded_at`: the time it was added to the
Archive. The Archive is not an activity log. A timestamp does not make
transient state worth retaining, and Records should not present copied
operational state as current truth.

Records do not need to agree. The Archive preserves them without
endorsing their correctness or interpreting their meaning.

The Archive is flat. It provides no semantic Sections or Chapters.
Consumers group and query Records using the data available in them.

## Locators

`locators.jsonl` is an appendable registry of known locator hints for an
Artifact. Each line is one independently timestamped Record.

Locators may include local paths, external URLs, and Git remote URLs.
Repository registration captures its local path and the configured
remotes it can admit through simple, bounded checks.

The Archive stores an admitted Git remote locator verbatim. It does not
sanitize, repair, or normalize it into another locator. Local filesystem
paths may be canonicalized mechanically. No locator is interpreted as
authoritative. A suspicious or unsupported Git remote is skipped and
surfaced as a warning without reproducing the potentially sensitive
value in that warning.

Re-registering an already registered Repository is a no-op. It does not
refresh the Git Hint, rescan remotes, or append newly discovered
locators. Consumers add further locator hints explicitly.

## Git Hints

A Repository’s `git-hint.json` is a compact recognition hint, not its
identity, current state, or an Archive activity log.

For the branch selected at registration, the Archive samples between
one and ten commits across the reachable history, beginning with the
first commit. The sample is deterministic and distributed across that
history when more than ten commits are available.

The Git Hint retains each sampled commit hash together with its Git
commit metadata, including its message. This is cheap descriptive
evidence that consumers may use to assess whether a candidate
repository contains the sampled commits.

The Git Hint does not retain `HEAD`. Repository growth, shallow clones,
missing objects, or history rewrites may weaken the hint without
changing the Archive-issued Repository ID.

## External Descriptors

Consumers may register Artifacts as `External.Descriptors` of another
Artifact.

`External.Descriptors` is an ordinary Record associated with the target
Artifact. It contains references to other Artifacts declared to be
useful descriptions, representations, or recovery hints.

Examples include a transcript for a video, extracted text for a
document, or a thumbnail for an image.

The Archive preserves these attributed references without endorsing
their correctness or meaning.

Each External Descriptor remains an ordinary Artifact with its own
identity, locations, Records, and possible External Descriptors.

The Archive does not provide a general semantic relationship graph.
Richer relationships and their assessment belong to consumers.

## Artifact Identity

Every `Artifact.ID` occupies one uniform 256-bit identity space and is
represented as 64 lowercase hexadecimal characters.

A root or repoless Artifact receives a cryptographically random
Archive-issued `Artifact.ID`.

A repository-contained Artifact receives a deterministic ID derived
from a canonical encoding of:

- The containing `Repository.ID`.
- The Git object format.
- The exact commit.
- The Artifact subpath.

Conceptually:

`Artifact.ID = SHA-256(Repository.ID, Commit, Subpath)`

The canonical encoding must be versioned and unambiguous.

The Artifact ID is also the physical key for its Record directory.
There is no separate storage-key mapping.

## References and Resolution

Archive references are stable and non-rebinding. A reference may become
dead, but it must never resolve to different data.

A registered repository and an exact commit/subpath are sufficient to
locate a repository-contained Artifact before individual Records have
been materialized for it.

When the system shows interest in an Artifact, the Archive materializes
its Record directory and applicable Records.

If the Artifact cannot be found, the Archive returns its retained
location history, fingerprints, External Descriptors, and other hints.

## Materialization

Root Artifacts such as repositories are materialized eagerly.

Repository-contained Artifacts are discoverable by querying Git
directly and are materialized lazily when referenced or otherwise
selected by a consumer.

Tarav must also be capable of materializing:

- One Artifact.
- A folder or subtree.
- Every Artifact in a registered repository.

Materialization policy affects cost, not Artifact identity.

## Physical Shape

`~/Documents/tarav-archive/` has two primary surfaces:

- `records/` — the Git repository containing Archive Records.
- `repositories/` — repositories physically managed by the Archive.

External repositories remain in their natural locations. Their
locations are recorded by the Archive.

A candidate layout is:

    tarav-archive/
    ├── records/
    │   ├── .git/
    │   ├── archive.json
    │   └── artifacts/
    │       └── <artifact-id>/
    │           ├── registration.json
    │           ├── locators.jsonl
    │           ├── git-hint.json
    │           ├── external-descriptors.json
    │           └── <other-records>.json
    └── repositories/
        └── <managed-git-repositories>/

The Record repository is Archive infrastructure and is not recursively
materialized as an ordinary Archive Artifact.
