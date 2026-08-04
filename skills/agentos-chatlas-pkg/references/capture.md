# Chat.Index Capture Operation Module

Construct or refresh the unreviewed `Chat.Index` for exactly one Chatlas session.

Treat the invocation itself as authority to write only the target `session-index/<identity-hash>/` surface and the Chatlas anchors needed by newly captured lines. Do not enter an Index review workflow: this product is intentionally unreviewed.

## Capture Boundary

- Construct one `Chat.Touched.Index` from the target chat and materialize it as `<chatlas-root>/session-index/<identity-hash>/`.
- Recover `Chat.Ontology` from Index blocks and lines actually present in the source session, then capture additional touched knowledge from qualifying user turns.
- Keep `ontology/` and `appendix/` unreviewed. Use `Chat.Ontology` for the recovered/core structure and `Chat.Appendix` for depth.
- Preserve unchanged recovered line content and support relationships whenever they remain internally valid.
- Consult no external Project Index or Package Skill Index during construction.

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

## 2. Materialize The Closed Source

Create a temporary directory with `mktemp -d`. Keep the large source payload out of conversational context and write it directly to a file:

```sh
agentos chatlas turns query \
  --identity-hash <full-identity-hash> \
  --detail turn --sort oldest --limit 100000 \
  > <temporary-directory>/source.json
```

Require `selected_session_count = 1` and `returned_turn_count = match_count`. Every `normal_turn.events` entry—including message, reasoning, tool-call, and tool-result events—is source chat content for recovery. Use each returned `turn_ref` as the exact `Normal.Turn.Ref` when grounding new lines.

Do not use `agentos chatlas views`, named views, provider-home files, or paths mentioned inside the chat as alternate content sources.

## 3. Enforce Content Closure

During capture, allow knowledge to enter only from:

1. the materialized `source.json` for this session; and
2. an existing `session-index/<identity-hash>/` generated from the same session, used only as resumable prior state and revalidated against the current source.

Treat this skill, its loaded package concepts, the current agent conversation, repository files, and any Project or Package Skill Index as operational guidance only. Never copy their ontology or lines into the generated `Chat.Index` unless the same material is observable inside `source.json`.

Resolving an anchor literally present in the source or prior surface through the Chatlas Anchory depot is allowed. Searching an external Index for a concept, attachment, missing line, or newer wording is forbidden.

## 4. Recover `Chat.Ontology`

Inspect text carried by source events, including tool-result content. Recover every observable Index block, partial block, and typed `Index.Line` without completing it from external memory.

- Preserve exact recovered `Line.Type + body` content.
- Preserve observable block attachment when it is present.
- Attach a recovered standalone line to an observable nearby block when the source establishes one; otherwise use a chat-local block, initially `Unassigned` when no honest name is available.
- Deduplicate repeated materializations by canonical `Line.Type + body`; block path, file, and source position are not deterministic line identity.
- Preserve a recovered trailing anchor when it remains one relationship for that same line content.
- Keep an unanchored recovered line unanchored unless qualifying user turns in this session independently support it.

Do not infer the remainder of a truncated block, update a recovered line to current package wording, or import sibling lines from a named concept.

## 5. Capture Additional Touched Knowledge

Read the user turns and their neighborhoods from `source.json`. Capture durable definitions, decisions, constraints, rejections, preferences, corrections, accepted proposals, and open conceptual gaps.

- Exclude preset prompts, administrative capture invocations, and turns that do not materially touch the subject.
- Prefer attachment to recovered ontology blocks.
- Create a chat-local concept when no recovered block fits; use `Unassigned` while its name is genuinely unclear.
- Put compact/core lines in ontology and deeper elaboration in appendix.
- Type each new line using the normal `Index.Line` vocabulary.
- Ground each new line only in exact supporting user-turn members from this session. Assistant content supplies neighborhood context but never substitutes for user support.

Imported and freshly captured lines have no structural marker in the output. Their provenance remains inspectable through their support relationships.

## 6. Normalize Support Relationships

Make every grounded materialization end in exactly one trailing anchor.

- Equal canonical line content may share one anchor across repeated materializations.
- Different canonical line contents must never share an anchor, even when their `Chat.Support.Set` members are equivalent.
- When one recovered anchor occurs on different contents, resolve its members and mint a distinct v4 line-bound relationship for each content; do not choose one meaning silently.
- When one recovered line carries several anchors, union their ordered members and `Turn.Type` cargo, then mint one v4 line-bound relationship for the line.
- If a recovered anchor cannot resolve, preserve the literal relationship, record a capture finding, and mark the capture `needs-review`; never invent replacement support.

For every new or normalized relationship, preview before registering:

```sh
agentos chatlas anchory preview \
  --line-content '<exact typed line without trailing anchor>' \
  --member <identity-hash>:<turn-id> \
  --member-types '<typed member cargo JSON when present>' \
  --hint '<what these turns support>' \
  --detail context
```

Omit `--member-types` only when every member uses the default base-support type. Preserve member order and all `Turn.Type` cargo when reconstructing an existing set. Treat `equivalent_anchors` only as a support-membership hint: reuse an equivalent anchor only when resolving it proves a v4 subject hash for this exact line content. Otherwise register a new anchor with the same members:

```sh
agentos chatlas anchory register \
  --line-content '<exact typed line without trailing anchor>' \
  --member <identity-hash>:<turn-id> \
  --member-types '<typed member cargo JSON when present>' \
  --hint '<what these turns support>'
```

## 7. Write The Session Surface

Create or resume:

```text
<chatlas-root>/session-index/<identity-hash>/
├── capture.json
├── ontology/
│   └── chat-ontology.md
└── appendix/
    └── chat-appendix.md
```

Split the Markdown files only when size materially improves navigation; list every managed file in `capture.json`. Use ordinary `****`-delimited Kernel blocks in both layers. Do not add review-standing markers or distinguish imported lines from fresh lines.

Write `capture.json` with:

- schema `agentos.chat-index.capture.v1`
- the resolved session row (`identity_hash`, `session_id`, `provider`, `uri`)
- ordered source `Normal.Turn.Ref` values and source turn count
- managed relative file paths
- capture status: `complete` or `needs-review`
- concrete findings, including unresolved anchors or ambiguous attachments
- capture timestamp

When the target exists, treat it as resumable state: snapshot or preserve its managed files before replacement, retain unrelated files, and never mint a duplicate anchor for an unchanged line whose existing relationship still validates.

## 8. Validate And Report

Before reporting completion, verify:

- every generated knowledge line is either exact recovered content or grounded in qualifying user turns from the target session
- every grounded materialization has one trailing anchor
- no anchor spans distinct canonical line contents inside the capture
- every newly minted v4 subject matches its line content
- every retained imported anchor resolves, or appears as a concrete `needs-review` finding
- `ontology/`, `appendix/`, and `capture.json` exist under the resolved identity-hash path
- no external Project or Package Skill Index was read during construction

Return the materialized path, status, counts for ontology blocks/lines and appendix blocks/lines, anchors minted/reused, and any findings. Do not paste the captured session content into the caller chat unless explicitly requested.
