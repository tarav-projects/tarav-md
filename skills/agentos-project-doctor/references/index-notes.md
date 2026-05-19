# Index Notes Checks

Check `Agentos.Index.Notes` basics. Architecture context comes from the index itself — this file covers only what to check and what to report.

## Deterministic Checks

When `skills/agentos-index/index/` exists (public index):

- check for `000-index.md` routing table
- list flat index files, verify numbering in public range

When `notes/index/` exists (local index):

- check for `001-index.md` local entry point
- list flat index files, verify numbering in local range
- check that local `001-index.md` points to public index if it exists

When both exist:

- check routing table coverage across public and local flat files
- check for dotted concept-like names in stable surfaces that are missing from routing tables

## Agentic Checks

- Does the routing table appear stale relative to the active index surface?
- Are migrated or legacy notes clearly marked as evidence rather than active authority?
- Do index notes appear concept-centered enough to be useful?

If neither public nor local index exists, check whether the project appears to use an index-like durable design surface elsewhere.

## Expected Findings

- `fail`: index exists but routing table is missing.
- `warn`: index routing points mainly to live/progress artifacts.
- `warn`: routing table appears stale relative to the active surface.
- `warn`: durable-looking index content is un-routed.
- `warn`: index-like durable design/reference notes exist outside the expected locations.
- `info`: index exists and appears intentionally minimal.
- `skip`: the project does not appear to adopt an index-like durable design/reference surface.
