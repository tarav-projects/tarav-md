# Index Notes Checks

Check `Agentos.Index.Notes` basics.

## Deterministic Checks

When `notes/index/` exists:

- check for `notes/index/000-index.md`
- check for `notes/index/001-ontology.md`
- list direct markdown files under `notes/index/`
- check whether numbered index notes use the active `100-499` rolling range, except reserved files such as `000-index.md`
- identify non-numbered files that are not clearly reserved

## Agentic Checks

- Does `000-index.md` route durable concept notes rather than progress artifacts?
- Does `001-ontology.md` appear stale relative to the active concept set?
- Does `000-index.md` appear stale relative to the active index surface?
- Are migrated or legacy notes clearly marked as evidence rather than active authority?
- Do index notes appear concept-centered enough to be useful?

If `notes/index/` does not exist, check whether the project appears to use an index-like durable design/reference surface elsewhere.

## Expected Findings

- `fail`: `notes/index/` exists but `000-index.md` is missing.
- `fail`: `notes/index/` exists but `001-ontology.md` is missing.
- `warn`: index routing points mainly to live/progress artifacts.
- `warn`: `000-index.md` or `001-ontology.md` appears stale relative to the active surface it should route.
- `warn`: durable-looking index content is un-routed.
- `warn`: index-like durable design/reference notes exist outside `notes/index/`.
- `warn`: active index notes contain non-numbered files that are not clearly reserved.
- `info`: index exists and appears intentionally minimal.
- `skip`: the project does not appear to adopt an index-like durable design/reference surface.
