# agentos-index --link

Use this module when a caller needs an `Anchory.Anchor` minted for a chat context: the linking primitive behind grounding lines, inline grounding, and agendix provenance.

This module is `Workflow.Neutral`: it produces an anchor and returns it — it writes no index surface. Consumers decide where the anchor lands: `--edit` writes gated `[GR]` grounding lines and inline anchors; `--agendix` tags captured lines. Minting an anchor mutates only the anchory depot, which is register plumbing, not an index edit.

Authority lives in the index: `Anchory.System`, `Chatlas.Anchory`, `Index.Linking`, `Kernel.Block.Grounding` own the concepts.

## Linking Pipeline

All steps run through `agentos chatlas` and `agentos anchory` commands — never provider raw files or transcript paths.

1. **Resolve the session.** Identify the session holding the evidence turn and resolve its chatlas identity, refreshing first so live sessions are ingested:
   - own live session: `chatlas-agentos-chatlas-my-session-id`, or `agentos chatlas query --session-id <native-id> --field identity_hash --update`
   - past session: normal `agentos chatlas query` filters, `--update` when staleness is possible
2. **Locate the evidence turn.** Search the tape directly:
   - `agentos chatlas views inline --identity-hash <hash> --view events --contains "<text>" [--role user] [--around <ISO time>] --format json` — returns the matching events as a model fragment with timestamps
   - the anchor lands in a neighborhood: pick the turn that best *lands* the reader, not a span that contains everything
3. **Register the anchor.** One command — chatlas owns the record, validates, allocates, and echoes:
   - `agentos chatlas anchory register --identity-hash <hash> --at "<ISO time>" --hint "<one sentence: what is at this location>"`
   - chatlas validates the session and that `at` falls inside its event-time bounds, derives the `YYYYMMDD` prefix, registers atomically through anchory, and returns the anchor PLUS the landing neighborhood — double-check it shows the intended turns before tagging
   - the raw plumbing remains available: `agentos anchory register --depot <chatlas-root>/anchory --prefix <YYYYMMDD> --record-json '…'`
4. **Verify.** The mint echo already shows the neighborhood; for later re-checks, `agentos chatlas views inline --anchor <anchor> [--radius N]` returns it again.
5. **Return the anchor** to the caller, which tags its line: trailing position, `… @20260707-0`.

## Anchor Discipline

- an anchor's meaning is immutable: no reuse; a wrong hint or wrong date means minting a new anchor, never repurposing
- `agentos anchory amend` exists only to correct an error or improve resolution of the same context
- the hint is the desync tripwire: write it so a reader can tell whether the resolved neighborhood matches
- the register is plumbing, not truth — the information lives on the surfaces; agents detect desync by reading them
- one anchor per claim: if two lines ground on the same neighborhood, they may share the anchor

## Resolution (reading an anchor)

- `agentos chatlas views inline --anchor <anchor> [--radius N]` — resolves through the chatlas anchory depot and returns the landing-turn neighborhood as a model fragment; read the landing turn and around it
- `agentos anchory resolve --depot … --anchor <anchor>` remains the record-level (plumbing) view
