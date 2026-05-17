# Index Notes Checks

Check `Agentos.Index.Notes` basics.

## Deterministic Checks

When `skills/agentos-index/index/` exists (public index):

- check for `000-index.md` routing table
- list flat index files, verify numbering in `100-299` range

When `notes/index/` exists (local index):

- check for `000-index.md` local entry point
- list flat index files, verify numbering in `300-499` range
- check that local `000-index.md` points to public index if it exists

## Agentic Checks

- Does `000-index.md` routing table cover the active concept set?
- Does the routing table appear stale relative to the active index surface?
- Are migrated or legacy notes clearly marked as evidence rather than active authority?
- Do index notes appear concept-centered enough to be useful?

If neither `skills/agentos-index/index/` nor `notes/index/` exists, check whether the project appears to use an index-like durable design/reference surface elsewhere.

## Expected Findings

- `fail`: index exists but `000-index.md` routing table is missing.
- `warn`: index routing points mainly to live/progress artifacts.
- `warn`: routing table appears stale relative to the active surface.
- `warn`: durable-looking index content is un-routed.
- `warn`: index-like durable design/reference notes exist outside the expected locations.
- `info`: index exists and appears intentionally minimal.
- `skip`: the project does not appear to adopt an index-like durable design/reference surface.
