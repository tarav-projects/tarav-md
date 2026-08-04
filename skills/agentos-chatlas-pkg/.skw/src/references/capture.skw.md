> $kw: ^chat-index-capture-loading-path --context-loading-path
> --step SKILL.md
> --loading-dep SKILL.skw.md^chatlas-pkg-batchy-runtime-contract
> --loading-dep SKILL.skw.md^chat-index-capture-call-contract

> $kw: --from Batchy.Skill.Banner --from Chat.Index --from Chat.Index.Delta --from Chat.Index.HEAD --from Chat.Support.Set --from Chat.Touched.Index --from Chatlas.Anchory --from Index.Line --from Line.Home --from Line.Provenance --from Normal.Turn.Ref --from POI.Line --from Turn.Type --from Unassigned

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

## 2. Inspect Existing Surface And Tail

Keep inspection payloads in the temporary directory:

```sh
agentos chatlas chat-index show \
  --identity-hash <full-identity-hash> \
  > <temporary-directory>/existing.json
```

When `existing.json.capture.schema` is v2, inspect only the source evidence not yet represented by its stored source prefix:

```sh
agentos chatlas chat-index tail \
  --identity-hash <full-identity-hash> \
  --detail turn \
  > <temporary-directory>/tail.json
```

Route by `tail.json.tail.state`:

- `current` — report an idempotent no-op by default; maintain an existing fixed-horizon extraction only when the request explicitly calls for it.
- `append-only` — focus semantic inspection on the returned pending turns, preserving prior Deltas whose bounded evidence and content remain valid.
- `expanded` — newly observed turns occur inside the prior source range; inspect them and revalidate every Delta whose horizon follows affected evidence plus HEAD.
- `revised` — one or more stable turn coordinates now carry revised hashes or timestamps; inspect the returned authoritative turns and revalidate affected Deltas plus HEAD.
- `diverged` — stop without writing; a stored turn coordinate is missing, reordered, or replaced on the current tape.
- `blocked` — stop without writing; branch-aware maintenance remains outside this linear implementation.

A missing surface follows full initial capture. A legacy v1 surface follows full v2 recapture with the recoverable-snapshot rule in step 9; never treat it as incrementally maintainable or silently edit its descriptor in place.

## 3. Materialize The Linear Source

Create a temporary directory with `mktemp -d`. Keep source payloads out of conversational context and write them directly to files:

```sh
agentos chatlas chat-index source \
  --identity-hash <full-identity-hash> \
  > <temporary-directory>/source-meta.json

agentos chatlas turns query \
  --identity-hash <full-identity-hash> \
  --detail turn --sort oldest --limit 100000 \
  > <temporary-directory>/source.json
```

Require `source-meta.json.source.linear = true`, exactly one selected source session, and `returned_turn_count = match_count`. If Chatlas reports rollback or inactive-lineage evidence, surface that finding and stop without writing: branch-aware Delta horizons are outside this first implementation.

Use `source-meta.json.source.turn_refs` as the authoritative tape order. Join those entries to the detailed turns in `source.json` by `Normal.Turn.Ref`; never use filenames or timestamps to order the chat. Every `normal_turn.events` entry—including message, reasoning, tool-call, and tool-result events—is source chat content.

## 4. Enforce Content Closure

During capture, allow knowledge to enter only from:

1. the materialized source and tail files for this session; and
2. an existing `session-index/<identity-hash>/` from the same session, used only as resumable candidate state and revalidated against the current source and each fixed Delta horizon.

Treat this skill, its loaded package concepts, the current agent conversation, repository files, and any Project or Package Skill Index as operational guidance only. Never copy their ontology or lines into the generated `Chat.Index` unless the same material is observable inside the source chat.

Resolving an anchor literally present in the source or prior surface through the Chatlas Anchory depot is allowed. Searching an external Index for a concept, attachment, missing line, or newer wording is forbidden.

## 5. Choose Delta Horizons

Inspect qualifying user turns in tape order. A qualifying user turn materially touches a durable definition, decision, constraint, rejection, preference, correction, accepted proposal, or open conceptual gap.

- Create one Delta per qualifying user turn by default.
- Group several touched events only when one meaningful extraction is clearer; use the last qualifying user turn in the group as `Delta.Horizon.Turn`.
- A Delta may interpret only the causal prefix through its horizon `tape_position`.
- Later maintenance may extend, correct, or reorganize the extraction using that same prefix, but must never use later chat evidence.
- Assistant and tool context inside the prefix may inform interpretation but cannot independently provide user touch.

The Delta heading is:

```markdown
# Chat.Index.Delta/<turn-id> @ <timestamp>
```

When the horizon `Normal.Turn.Ref` provides `at`, include it after `@`. Omission then creates a blessable POI; do not classify the cause mechanically. When the source has no timestamp, omit the suffix.

## 6. Capture Delta Content

Capture only the semantic change touched within each Delta's bounded prefix. Preferentially attach lines to concepts already visible by that horizon, and avoid restating earlier Deltas without a meaningful new touch.

- Preserve exact observable `Line.Type + body` when recovering a line already present in chat content.
- Type synthesized extractions using the normal `Index.Line` vocabulary.
- Ground every line in exact qualifying user turns from this session. The horizon need not be the only support member.
- Keep a chat-local `Unassigned` block only while no honest attachment is visible inside the prefix.
- Do not mark imported versus new lines syntactically; known origin is provenance, not authority.

The same exact canonical line may appear in several Deltas. Its default `Line.Home` is derived as the oldest containing Delta in `capture.json.deltas` order. Do not write a second home registry or choose the known origin as home automatically.

## 7. Normalize Line Anchors And Provenance

Make every grounded materialization end in exactly one trailing line-bound Chatlas anchor.

- Equal canonical line content may share one anchor across repeated materializations.
- Different canonical line contents must never share an anchor, even when their `Chat.Support.Set` members are equivalent.
- Preserve member order and all `Turn.Type` cargo when reconstructing an existing set.
- If a recovered anchor cannot resolve, preserve the literal relationship, record a capture finding, and mark the capture `needs-review`; never invent replacement support.
- `Line.Provenance` belongs to this line anchor. Do not serialize known-origin observations, materialization history, or Git evidence into `capture.json` or a parallel Chat.Index registry.
- Until the line-anchor provenance dossier has a maintained cargo schema, preserve only representable anchor state and leave richer provenance unasserted.

Preview every new or normalized relationship before registering it:

```sh
agentos chatlas anchory preview \
  --line-content '<exact typed line without trailing anchor>' \
  --member <identity-hash>:<turn-id> \
  --member-types '<typed member cargo JSON when present>' \
  --hint '<what these turns support>' \
  --detail context
```

Omit `--member-types` only when every member uses the default base-support type. Reuse an equivalent anchor only after resolving it proves a line-bound subject hash for this exact line content. Otherwise register a new anchor with the same members.

## 8. Resolve `Chat.Index.HEAD`

Construct `HEAD.md` as the present-facing model of the complete source chat.

- Select exact Delta lines when they represent the current model well.
- Synthesize better ordinary model lines when the full chat context requires it, then reconcile them backward into the appropriate bounded Delta before considering capture complete.
- If an ordinary HEAD line has no exact Delta materialization, keep the HEAD-first edition but add a concrete missing-home finding and mark capture `needs-review`.
- A `POI.Line` may remain HEAD-first as maintenance state only when it owns its own user-grounded support set. Its subject lines' anchors are inputs to the agent's investigation, not inherited authority.
- Do not create general line-to-line provenance or supersession links.

Use the last available source `Normal.Turn.Ref` as the HEAD horizon. HEAD currentness is local to this session.

## 9. Write The V2 Session Surface

Stage a complete replacement before changing managed paths:

```text
<chatlas-root>/session-index/<identity-hash>/
├── capture.json
├── deltas/
│   ├── <horizon-turn-id>.md
│   └── ...
└── HEAD.md
```

Retain unrelated files. When a prior surface exists, preserve a recoverable snapshot of its managed files until the staged v2 surface validates. During append-only maintenance, carry unaffected prior Deltas forward byte-for-byte; amend an old Delta only from evidence inside its unchanged horizon. Never silently convert a v1 descriptor in place or mint duplicate anchors for unchanged relationships.

Write `capture.json` with:

- schema `agentos.chat-index.capture.v2`;
- capture status `complete` or `needs-review` and capture timestamp;
- the resolved session locator;
- `source.materialized_source_hash`, `turn_count`, `linear: true`, and tape-ordered source turn references from `source-meta.json`;
- `deltas`, each containing safe relative `path`, exact horizon `Normal.Turn.Ref`, and integer `tape_position`, in strictly increasing order;
- `head` containing `path: "HEAD.md"` and its horizon `Normal.Turn.Ref`;
- `managed_files` containing exactly `capture.json`, every declared Delta path, and `HEAD.md`, without duplicates;
- concrete findings.

## 10. Validate And Report

Run the public inspectors against the staged or landed surface:

```sh
agentos chatlas chat-index status --identity-hash <identity-hash>
agentos chatlas chat-index deltas --identity-hash <identity-hash>
agentos chatlas chat-index head --identity-hash <identity-hash>
agentos chatlas chat-index tail --identity-hash <identity-hash>
```

For each ordinary HEAD line, run `chat-index home --line-content '<line>'`. Missing homes become explicit findings; repeated matches must select the oldest descriptor-ordered Delta.

Before reporting completion, verify:

- every Delta line is exact recovered content or grounded extraction from evidence at or before its fixed horizon;
- every grounded materialization has one trailing line-bound anchor;
- no anchor spans distinct canonical line contents;
- Delta paths and horizons are unique and tape positions strictly increase;
- `capture.json`, all declared Deltas, and `HEAD.md` exist under the resolved identity-hash path;
- the post-write tail state is `current` with zero pending turns;
- no external Project or Package Skill Index was read during construction;
- inspection did not rewrite the surface.

Return the materialized path, status, counts for Deltas, Delta lines, HEAD lines, pending turns consumed, anchors minted/reused, home findings, and other findings. Do not paste captured session content into the caller chat unless explicitly requested.
