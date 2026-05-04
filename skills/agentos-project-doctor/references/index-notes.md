# Index Notes Checks

Check `Agentos.Index.Notes` basics.

## Deterministic Checks

When `notes/index/` exists:

- check for `notes/index/000-index.md`
- list direct markdown files under `notes/index/`
- check whether numbered index notes use the active `100-499` rolling range, except reserved files such as `000-index.md`

## Agentic Checks

- Does `000-index.md` route durable concept notes rather than progress artifacts?
- Are migrated or legacy notes clearly marked as evidence rather than active authority?
- Do index notes appear concept-centered enough to be useful?

## Expected Findings

- `fail`: `notes/index/` exists but `000-index.md` is missing.
- `warn`: index routing points mainly to live/progress artifacts.
- `warn`: durable-looking index content is un-routed.
- `info`: index exists and appears intentionally minimal.

