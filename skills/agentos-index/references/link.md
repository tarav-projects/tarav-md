# agentos-index --link

Use this module when a caller needs an `Anchory.Anchor` minted for a chat context: the linking primitive behind grounding lines, inline grounding, and agendix provenance.

This module is `Workflow.Neutral`: it produces an anchor and returns it — it writes no index surface. Consumers decide where the anchor lands: `--edit` writes gated `[GR]` grounding lines and inline anchors; `--agendix` tags captured lines. Minting an anchor mutates only the anchory depot, which is register plumbing, not an index edit.

Authority lives in the index: `Anchory.System`, `Chatlas.Anchory`, `Index.Linking`, `Kernel.Block.Grounding` own the concepts.

## Linking Pipeline

All steps run through `agentos chatlas` and `agentos anchory` commands — never provider raw files or transcript paths.

1. **Resolve the session.** Identify the session holding the evidence turn and resolve its chatlas identity, refreshing first so live sessions are ingested:
   - own live session: `chatlas-agentos-chatlas-my-session-id`, or `agentos chatlas query --session-id <native-id> --field identity_hash --update`
   - past session: normal `agentos chatlas query` filters, `--update` when staleness is possible
2. **Locate the evidence turn.** Pull the turn-level view and find the landing turn's timestamp:
   - `agentos chatlas views inline --identity-hash <hash> --view user --format json` — events carry `timestamp`; scan for the evidence turn
   - the anchor lands in a neighborhood: pick the turn that best *lands* the reader, not a span that contains everything
3. **Register the anchor.** Depot is the chatlas anchory depot (`<chatlas-root>/anchory/`); key prefix is the evidence turn's date `YYYYMMDD`:
   - `agentos anchory register --depot <chatlas-root>/anchory --prefix <YYYYMMDD> --record-json '{"app":"chatlas","session":"<identity_hash>","at":"<ISO time>","hint":"<one sentence: what is at this location>"}'`
   - `register --prefix` allocates the next `<YYYYMMDD>-N` atomically under the depot lock and returns the full anchor
4. **Verify.** `agentos anchory resolve --depot … --anchor <anchor>` must round-trip the record.
5. **Return the anchor** to the caller, which tags its line: trailing position, `… @20260707-0`.

## Anchor Discipline

- an anchor's meaning is immutable: no reuse; a wrong hint or wrong date means minting a new anchor, never repurposing
- `agentos anchory amend` exists only to correct an error or improve resolution of the same context
- the hint is the desync tripwire: write it so a reader can tell whether the resolved neighborhood matches
- the register is plumbing, not truth — the information lives on the surfaces; agents detect desync by reading them
- one anchor per claim: if two lines ground on the same neighborhood, they may share the anchor

## Resolution (reading an anchor)

- `agentos anchory resolve` → record → chatlas traversal to the session and turn neighborhood; read the landing turn and around it
- target CLI (planned): `agentos chatlas query --anchor <anchor>` — chatlas digests anchors natively as the successor of the retired `Chat.Ref` reference surfaces
