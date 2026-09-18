# 788 — Inlined Capture derived session alias — Impl.Req

Status: Completed

## Impl.Abstract

Replace the human-chosen `Inlined.Capture` session alias with an opaque alias
derived from the session's Chatlas identity hash, and register that identity
hash in the surface declaration so the derivation is locally verifiable.

Scope:

- the alias is the first 8 lowercase hexadecimal characters of the session's
  Chatlas identity hash;
- a `tarav.sessions` declaration line retains alias,
  `<provider>:<native-session-id>`, and the full 64-character identity hash;
- `Inlined.Capture.Markdown.Reference.Renderer` derives the alias itself and no
  longer accepts a caller-supplied `session-alias` option;
- the `tarav-hugentics --capture --inline` contract and its audit route are
  rewritten to the current form only;
- the whole existing corpus is migrated across four repositories.

Out of scope:

- alias registries, Git-history auditing, or a document identity mechanism;
- changes to turn-hash prefix length, which stays at 16;
- any change to Reading Club, Diagram, or Chatlas query semantics.

Boundaries:

- **No backward compatibility.** No element of the delivered system exists
  because of the previous implementation: no dual parsing, no deprecated form
  accepted by the audit, no compatibility branch, no transitional aliases, and
  no migration residue left in migrated surfaces.
- The identity hash is authoritative; `<provider>:<native-session-id>` is a
  convenience pointer back to the raw provider artifact. A disagreement between
  them is a POI, not a silent preference. *(Agent-derived rule; not
  User-Touched.)*
- Migration rewrites surfaces in place. Turn hashes themselves do not change;
  only the alias token and the declaration line change.

## Impl.Req.Diagram

- **namespace:** User.Touched.Chatlas.Index / `1c99092c-ba46-4006-adc3-9ada50c00abd`
- **model:** Tarav / `b7b78eab-e5c2-4610-9bf5-1b704a106f34`
- **collection:** 788.Impl.Req / `b21afa54-a9d7-4b35-81b8-4526ce28df69`
- **collection type:** Impl.Req.Collection
- **semantic block:** Inlined.Chat.Reference / `89d8f05f-2cee-45c2-96e9-aa4b3a42102f` (new `Design.Block`)
- **draft:** `a313a4c5-297b-46a1-9839-a43326293e52` / `/Users/pereiro/Documents/tarav/diagram/drafts/a313a4c5-297b-46a1-9839-a43326293e52.json`
- **authorization gate:** `53eed4d5-e68e-4f72-8d52-07435d5732f6`

The Model had no `Inlined.Capture` or `Inlined.Chat.Reference` Block before this
request; the concept existed only in the skill and live notes 772/775/779. A new
candidate Block is therefore honest rather than a failure to reuse encapsulation.

## Execution.Plan

Session identities in play:

| alias | provider | native session id | identity hash |
| --- | --- | --- | --- |
| `4571385e` | codex | `01a06bed-b554-7770-86e3-cce2e5729994` | `4571385eb2c5457a615e836d943acad00147fda45a10dbad26848faf81e2bfe1` |
| `91c6e789` | codex | `01a05752-fa8d-7c62-abb2-5ff20c8260da` | `91c6e789df50d874a454107ba81ff86be1e99022173b3469fbcdeffaedbf86c1` |
| `c3f268cf` | claude-code | `82a1908d-4851-4a9b-8942-34fe5c1fb0eb` | `c3f268cfe8ed0140025baac15a476d5d1100762e3ed76581c39ca811c94f26c2` |

Replacing `phd` → `4571385e` and `tarav` → `91c6e789`. No 8-character prefix
collision exists across these three.

### Slice 1 — Renderer derives the alias — **DONE**

Surface: `tarav-py/src/tarav/chatlas/rendering.py`.

`_inlined_capture_markdown_renderer` currently requires a `session-alias`
Renderer option and validates it against `_SESSION_ALIAS`. `ChatlasQueryResult`
already carries `.session`, which contains `identity_hash`. Derive the alias
from that and remove the option entirely, including its validation regex if it
becomes unused.

- **Check:** renderer emits `<!-- tarav.context <alias8>:<turn16> -->` with the
  alias derived from the query result; passing `session-alias` is rejected as an
  unknown option; missing or malformed `identity_hash` raises `ChatlasRenderError`.
- **Risk:** another Renderer may share `_SESSION_ALIAS`. Inspect before removing.
- **Deviation trigger:** if `.session` does not reliably carry `identity_hash`
  for every provider, stop and report rather than falling back to an option.

### Slice 2 — Declaration renderer — **DROPPED**

Dropped on User challenge before completion. It was unrequested scope: a new
public Renderer, registry entry, and three tests to avoid hand-typing a value
the workflow already obtains from `tarav chatlas current-session` plus
`normal-model`. The declaration line is assembled by the workflow instead.

### Slice 3 — Skill contract rewrite — **DONE**

Surface: `tarav-md/skills/tarav-hugentics/references/inline-capture.md`.

Rewrite the Markdown contract and audit contract to the current form only.
Update the declaration example, the alias rule, the capture workflow step that
passes `--renderer-option session-alias=<alias>`, and the audit conditions so a
non-derived alias or a declaration missing its identity hash is a reported POI.

- **Check:** the file describes exactly one form; `grep` finds no
  `session-alias` option and no semantic-alias example.

### Slice 4 — Corpus migration — **DONE**

Four repositories, two alias tokens, 370 references:

| repo | files | refs |
| --- | --- | --- |
| `University/Phd` | 31 | 257 |
| `Documents/tarav/reading-club` | 4 | 101 |
| `taravangian-project/tarav-md` | 1 | 1 |
| `taravangian-project/tarav-py` | 2 | 11 |

Actual result: 37 files, 369 references. The 370th occurrence was this note's own
acceptance criterion quoting the old literal; it was reworded rather than
migrated. `University/Phd/.claude/skills/` is a symlink into `tarav-md`, so no
duplicated skill copy required migration.

Rewrite declaration lines and alias tokens. `tarav-py` occurrences include test
fixtures using `phd:`; update them to the derived form so tests assert the
current contract.

- **Check:** no reference remains on either previous alias token; every
  declaration carries its identity hash and an alias equal to that hash's first
  8 characters; reference counts per file are unchanged before and after.
- **Risk:** fenced examples inside documentation must migrate too, but examples
  that deliberately show the declaration format are content, not references.

### Slice 5 — Verification — **DONE**

- `tarav chatlas` focused suite and Ruff in `tarav-py`.
- Skill validation for `tarav-hugentics`.
- Run `--capture --inline --audit` over a representative migrated surface in
  each corpus repo and confirm zero structural POIs.

- **Acceptance:** turn resolution still succeeds for migrated references, since
  turn hashes are untouched and only the alias token changed.

## Impl.Log

- Routed to Develop from a bare "implement" instruction; the router never infers
  Develop, so the resolution was named in the banner before any product edit.
- Live-note number 788 chosen because Collection labels already occupy 771–787
  across both `tarav-md` and `tarav-py`; the numbering pool is shared even though
  `tarav-md/notes/live` only reaches 781.
- Draft check reports 5 `archive-grounding-unassessable` and 8
  `semantic-record-unasserted` for this request's own records. The additional 326
  findings (`block-type-missing`, `line-type-missing`, `impl-req-closed-write`,
  `model-staleness`) are pre-existing Model backlog; none resolve to a path in
  this Draft.
- The authoritativeness rule between identity hash and native session id is
  Agent-derived and deliberately not captured as a User-Touched Line.
- **Deviation — Slice 2 dropped.** The designer added a declaration Renderer
  that the User never requested, contradicting `general-practices.md`
  ("implement the minimum coherent change", "prefer existing surfaces over
  unnecessary new abstractions"). The User challenged the diff size mid-slice
  and it was reverted. Slice 1's final diff is 37 lines across the renderer and
  its tests. Guard for the remaining slices: this request's value is the
  contract rewrite and the corpus migration, not new Chatlas surface.
- Slice 1 dropped `_SESSION_ALIAS`, which had no other consumer, and added
  `SESSION_ALIAS_LENGTH` plus `_session_identity_hash` / `_session_alias`.
  `tests/chatlas/test_core_cli.py` needed `provider` and `identity_hash` in its
  fake reader session, since the renderer now derives the alias from them.

## Result

- Renderer derives the alias from `ChatlasQueryResult.session["identity_hash"]`;
  `session-alias` is rejected as an unknown option. 79 Chatlas tests pass, Ruff
  clean.
- Contract rewritten to the current form only, including a new audit POI for a
  declaration missing its identity hash or carrying a non-derived alias.
- 37 files migrated across four repositories; 369 references preserved exactly,
  count invariant asserted per file.
- 39 declarations corpus-wide are well-formed and derived; the only alias tokens
  present are `4571385e` and `91c6e789`.
- Inline audit clean on one representative surface per corpus repo:
  `THESIS-CONSTITUTION.md` (1 declaration, 17 references, 11 distinct Turns),
  the Reading Project notes (42 references, 35 distinct), and note 772
  (2 declarations, 7 references, 3 distinct). Zero POIs, zero unresolved.
- `tarav skw check` reports 0 POIs for `tarav-md`.

Migrated references resolve unchanged because only the alias token moved; turn
hashes were never rewritten.

### Deferred

- No declaration Renderer exists; the workflow assembles the `tarav.sessions`
  line from `tarav chatlas current-session` plus the session identity hash.
- The audit's alias-vs-declaration check is now fully offline, but the audit
  route remains Agent-operated and has no CLI implementation.
- This Claude Code session (`c3f268cf`) is not declared in any surface; it will
  be declared by the first capture that actually references one of its Turns.
