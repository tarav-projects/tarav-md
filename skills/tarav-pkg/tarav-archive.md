# Tarav.Archive

The Archive provides a small registry of typed DOI objects. It is subordinate
to the Constitution. Artifact hosting and general recovery are deferred.

## Identity and maintenance

A DOI is a stable randomly assigned 256-bit identifier. Its Type declares
what continuity its maintainers promise. A Repository DOI tracks the same
repository across locations and evolving checkouts. A stricter Type may
commit to an exact state. Hints assist judgment and never rebind identity.
Archive maintains the DOI Records; external resources remain under their
owners' mutation authority.

## Registry information

Each DOI carries its identifier, optional label and typed locators. Local
locators state a path and host; remote locators state a URI. Multiple locations
may coexist. Repository recognition hints hold the Git object format and at
most ten sampled commit hashes, without commit messages or repository copies.
Shared commits do not distinguish forks: maintainers decide identity continuity.

A DOI lookup returns this maintained typed information. It does not open,
fetch or recover the resource, choose a preferred locator or repair links.
An inaccessible resource does not make its DOI Record unreadable. Consumers
own access, interpretation and their response to observed changes.

## Storage and references

The registry uses the standard Git-backed Record Registry partition for
Archive, keyed by DOI identifier. Initialization is explicit; reads never
provision storage. Updates preserve identifier and Type. Normal Git references
can retain observed Record editions without embedding duplicate snapshots.
Direct References and DOI References have separate contracts. A DOI Reference
loads a registered DOI object; it does not deliver external artifact bytes.

## Locator checks

Read-only checks may assess known locations separately from registry lookup.
Broken-link findings become Archive-owned actions in the System Project;
subsequent checks follow its normal action and closing lifecycle. Checks do
not repair or block storage, mutation or lookup. Unsupported protocols and
locations belonging to another host are unassessed, not declared broken.

## Boundaries

The first implementation provides registration, lookup, maintained updates,
enumeration and location checks. It does not provide artifact hosting,
automatic identity matching, fetching, cloning, recursive materialization,
exact-file registration or a recovery engine. Shared Record Archive storage
and Attic remain independent Archive child capabilities.
