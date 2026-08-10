> $kw: ^chat-index-capture-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^chatlas-pkg-batchy-runtime-contract
> --loading-dep SKILL.skw.md^chat-index-capture-call-contract

> $kw: --from Batchy.Skill.Banner --from Chat.Index --from Chat.Index.Delta --from Chat.Index.HEAD --from Chat.Support.Set --from Chat.Touched.Index --from Chatlas.Anchory --from Index.Line --from Line.Home --from Line.Type --from Normal.Turn.Ref --from POI.Line --from Unassigned

# Chat.Index Capture Operation Module

Construct or refresh the unreviewed chronological `Chat.Index` for exactly one Chatlas session.

Treat the invocation itself as authority to write only the target `session-index/<identity-hash>/` surface and the Chatlas anchors needed by captured lines. Do not enter an Index review workflow: this product is intentionally agent-maintained and unreviewed.

This first implementation supports linear chats only.

## Capture Boundary

> $kw: ^chat-index-capture-boundary --derived
> --from Chat.Touched.Index
> --from Chat.Index
> --from Chat.Index.Delta
> --from Chat.Index.HEAD
> --intent restate the chronological Chat.Index model as the operational capture boundary;
> --cont preserve closed-over-chat evidence, qualifying user touch, fixed Delta horizons, and present-facing HEAD reconciliation

- Construct one `Chat.Touched.Index` from the target chat and materialize it as `<chatlas-root>/session-index/<identity-hash>/`.
- Capture touched semantic changes into tape-ordered `Chat.Index.Delta`s whose evidence ends at a fixed qualifying user turn.
- Resolve `Chat.Index.HEAD` from the complete chat context and the Deltas; do not treat it as a mechanical union.
- Consult no external Project Index or Package Skill Index during construction.
- Never let material merely loaded into the chat create a Delta without a qualifying user touch event.

> $kw. end

## Run Configuration

Print the `Batchy.Skill.Banner` before reading Chatlas:

```text
$agentos-chatlas-pkg — banner
  --capture  → Chat.Index.Capture.Operation.Module
  --session  → Skill.Arg::Session = <supplied selector>
```

Require `Skill.Arg::Session`. If it is missing, ask for an exact provider-native session id, session URI, or full identity hash and stop without writing.

Use the depot-local `Chatlas.Anchory` for every support record minted by this workflow.

## 1. Resolve One Session

Map the supplied value to one exact Chatlas selector:

- `agentos://chat-session/...` → `--uri`
- exactly 64 hexadecimal characters → `--identity-hash`
- every other value → `--session-id`

Refresh and resolve through the maintained Chatlas dataset:

```sh
agentos chatlas query <exact-selector-flag> <value> --update
```

Require exactly one returned row. Do not guess between candidates. Take `chatlas_root`, `identity_hash`, `session_id`, `provider`, and `uri` from that authoritative row.


## 2. Scaffold The Capture Plan

Chatlas owns every mechanical decision in this workflow. Ask it for working input instead of gathering source, tail, and evidence by hand:

```sh
agentos chatlas chat-index scaffold \
  --identity-hash <full-identity-hash> \
  --stage <temporary-directory>/stage \
  --json \
  > <temporary-directory>/scaffold.json
```

The stage must be empty. Scaffold writes two files and nothing else:

- `plan.json` — a `agentos.chat-index.capture-plan.v1` envelope Chatlas owns, plus the empty semantic region this module fills in.
- `evidence.json` — the transcript-visible user and assistant messages of every turn this capture has to read, each carrying its `Normal.Turn.Ref`, tape position, and event sequences.

`scaffold.json.mode` routes the work:

- `create` — no managed surface exists; author the complete prefix.
- `maintain-v2` — a valid descriptor-free Delta/HEAD base exists; `scaffold.json.tail.state` says what changed.

Route `maintain-v2` by `scaffold.json.tail.state`:

- `current` — report an idempotent no-op by default; maintain an existing fixed-horizon extraction only when the request explicitly calls for it.
- `append-only` — `evidence.json` already narrows to the pending turns; preserve prior Deltas whose bounded evidence and content remain valid by simply omitting them from the plan.
- `expanded` or `revised` — newly observed or rehashed turns sit inside the prior source range; inspect them and re-author every Delta whose horizon follows affected evidence, plus HEAD.
- `diverged` or `blocked` — stop without writing; a stored coordinate is gone or the chat is not linear, and branch-aware maintenance stays outside this implementation.

Escalate one turn to `chat-index tail --detail turn --json` only when its messages are insufficient. Never substitute a Chatlas Product for this evidence.

## 3. Enforce Content Closure

During capture, allow knowledge to enter only from:

1. `evidence.json` and the scaffolded envelope for this session; and
2. an existing `session-index/<identity-hash>/` from the same session, used only as resumable candidate state and revalidated against each fixed Delta horizon.

Treat this skill, its loaded package concepts, the current agent conversation, repository files, and any Project or Package Skill Index as operational guidance only. Never copy their ontology or lines into the generated `Chat.Index` unless the same material is observable inside the source chat.

Resolving an anchor literally present in the source or prior surface through the Chatlas Anchory depot is allowed. Searching an external Index for a concept, attachment, missing line, or newer wording is forbidden.

## 4. Choose Delta Horizons

Inspect qualifying user turns in tape order. A qualifying user turn materially touches a durable definition, decision, constraint, rejection, preference, correction, accepted proposal, or open conceptual gap.

- Create one Delta per qualifying user turn by default.
- Group several touched events only when one meaningful extraction is clearer; use the last qualifying user turn in the group as `Delta.Horizon.Turn`.
- A Delta may interpret only the causal prefix through its horizon `tape_position`.
- Later maintenance may extend, correct, or reorganize the extraction using that same prefix, but must never use later chat evidence.
- Assistant and tool context inside the prefix may inform interpretation but cannot independently provide user touch.

Name each horizon once, as `delta_edits[].horizon_turn_id`. Chatlas derives the Delta filename, heading, timestamp, and `tape_position` from the authoritative turn; do not write headings by hand.

An edited Delta is a complete replacement bounded by its original horizon. An omitted existing Delta is carried forward byte-for-byte.

## 5. Capture Delta Content

Capture only the semantic change touched within each Delta's bounded prefix. Preferentially attach lines to concepts already visible by that horizon, and avoid restating earlier Deltas without a meaningful new touch.

- Preserve exact observable `Line.Type + body` when recovering a line already present in chat content.
- Type synthesized extractions using the normal `Index.Line` vocabulary.
- Keep a chat-local `Unassigned` block only while no honest attachment is visible inside the prefix.
- Do not mark imported versus new lines syntactically; materialization does not assert origin.

Author each line as an object under an ordered concept block:

```json
{
  "horizon_turn_id": "turn-r123",
  "blocks": [
    {
      "concept": "Chat.Index.Tail",
      "lines": [
        {
          "content": "- [CT] exact canonical line",
          "support": {
            "members": ["<identity-hash>:turn-r123"],
            "gates": {
              "semantic_approval": [],
              "tokenized_verbatim_approval": []
            }
          }
        }
      ]
    }
  ]
}
```

Line content must be typed and must never carry a trailing anchor; the renderer owns `Support.Reference`s. The same exact canonical line may appear in several Deltas, and its `Line.Home` is the oldest exact occurrence in authoritative tape order. Do not write a second home registry.

## 6. Ground Every Line

Each Delta line names its support once, as either a proposed record or an existing anchor:

- proposed — ordered support `members` of `<identity-hash>:<turn-id>` and optional explicit `gates` with `semantic_approval` and `tokenized_verbatim_approval` lists.
- existing — `{"anchor": "<anchor-key>"}`, accepted only when that anchor resolves to `chatlas.line-anchor-dossier.v1` and its attachment hash matches this exact `Line.Type + body + Anchor.Id` triplet.

Support members form the line's ordered `Chat.Support.Set` and must be qualifying user turns at or before that Delta's horizon. A changed line body or `Line.Type` requires relationship reevaluation; the maintainer may retain the anchor only by updating its attachment assertion and every affected relationship coherently.

Chatlas ensures each line's complete relationship dossier in one ordered batch during `apply`. Exact triplet-and-relationship equivalence may reuse an anchor; content equality alone does not establish relationship identity. Preview with `agentos chatlas anchory preview --line-content ... --member ... --detail context` only while investigating; the workflow itself does not register anchors by hand.

The Markdown occurrence records Delta materialization and is the SSOT for the current line triplet. Its dossier stores only the attachment assertion and independent support, gate, and provenance relationships. Delta containment remains the materialization evidence, and `Line.Home` is derived from it.

## 7. Resolve `Chat.Index.HEAD`

Author `head.blocks` as the present-facing model of the complete inspected prefix.

- Select exact Delta lines when they represent the current model well; a HEAD line that occurs in the resulting Delta set inherits that occurrence's anchor and needs no `support`.
- Synthesize better ordinary model lines when the full chat context requires it, then reconcile them backward into the appropriate bounded Delta before considering capture complete.
- A `POI.Line` may remain HEAD-first as maintenance state only when its own line object supplies user-grounded `support`. Its subject lines' anchors are inputs to the agent's investigation, not inherited authority.
- Do not create general line-to-line provenance or supersession links.

Chatlas derives the HEAD heading and `Evidence.Horizon` from the last source turn of the inspected prefix. Set the plan `status` to `ready` only when the semantic plan is complete; audit findings are computed after rendering and are never persisted on `Chat.Index`.

## 8. Validate The Plan

```sh
agentos chatlas chat-index validate \
  --plan <temporary-directory>/stage/plan.json \
  --json \
  > <temporary-directory>/validate.json
```

Validation writes nothing — no anchors, no surface. It reloads the authoritative source, checks the inspected prefix is still `current` or `append-only`, verifies the base-surface fingerprint, resolves or previews every line support in one batch, builds the complete resulting model, and returns the planned anchor actions plus the rendered-file inventory.

Fix the plan and rerun until it succeeds. A refusal names its cause: an unreproducible prefix, base-surface drift, an unresolved or drifted anchor, a horizon that is not a qualifying user turn, support reaching past a horizon, or an ungrounded HEAD-first line.

## 9. Apply

```sh
agentos chatlas chat-index apply \
  --plan <temporary-directory>/stage/plan.json \
  --json \
  > <temporary-directory>/apply.json
```

`apply` takes a visible lock keyed by identity hash, revalidates under it, batch-ensures the line anchors, renders the complete Delta/HEAD surface, audits the staged directory, and installs it through a recoverable rename. Unedited Deltas survive byte-for-byte. Files outside the resulting `deltas/` plus `HEAD.md` surface are reported in `removed_paths` and dropped.

Anchors are written before the directory swap. They are append-only and idempotent, so a retry after a failed installation reuses them instead of duplicating them — never claim cross-depot atomicity.

Append-only growth after scaffold is not a failure. `apply` installs exactly the inspected prefix, leaves HEAD at that evidence horizon, and returns the remaining tail for the next maintenance pass.

## 10. Audit And Report

```sh
agentos chatlas chat-index audit --identity-hash <identity-hash> --json
```

One read-only pass replaces the former per-anchor and per-line inspection loop. It derives the surface from its directory and Markdown, checks identity placement, source linearity and prefix compatibility, Delta and HEAD horizons against the authoritative chat, one trailing anchor per line, anchor resolution and exact attachment-triplet hashes, anchor/triplet collisions, Delta support horizons, `Line.Home` selection, and HEAD-only support. It exits nonzero when blocking findings exist and never repairs what it inspects.

A `head-line-without-delta-home` finding is advisory reconciliation work, not a failed capture: keep the HEAD-first edition, record the finding, and reconcile it on a later pass.

Report the materialized path, mode, plan status, counts for Deltas, Delta lines, HEAD lines, resolved homes, anchors minted and reused, removed paths, the remaining tail, and every audit finding. Do not paste captured session content into the caller chat unless explicitly requested.
