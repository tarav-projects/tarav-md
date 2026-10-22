# Tarav Breadcrumbs

<!-- tarav.sessions
3dbc7074 = codex:01a0baed-f147-77e2-b298-ed15249a9410 @3dbc7074117a70b90f57c98b25690d3ea15a519f0da6e05043e59b8add00d3c4
-->

## Surface anchors for annotations

A `Tarav.Breadcrumb` is an opaque, stable anchor embedded at a position in a
Product.Surface. The Breadcrumb is an annotation attachment primitive rather
than an annotation: typed records attached by workflows provide the semantics,
while the crumb left inside the surface identifies where they apply.
<!-- tarav.breadcrumb ddc56f53bb58 -->
<!-- tarav.breadcrumb 88752794558e -->
<!-- tarav.breadcrumb e49816883e6e -->
<!-- tarav.breadcrumb 7aa0c74bc9b3 -->

The durable surface form can therefore be a generic opaque label such as
`tarav.breadcrumb <id>`. Its identifier carries position identity rather than
annotation meaning. Resolving the identifier finds the Breadcrumb record and
the records attached at that point.
<!-- tarav.breadcrumb 8dc93616ef5e -->
<!-- tarav.breadcrumb 11f1d010dd6d -->

## Breadcrumb workflow

`Tarav.Breadcrumbs` is the general workflow pattern within which other surface
workflows operate. An Agent may create or select a Breadcrumb and attach a
record directly. Alternatively, a surface workflow can parse temporary
annotations, resolve their inputs, create Breadcrumbs and attachment records,
and clean the surface automatically.
<!-- tarav.breadcrumb d7f72a218b25 -->
<!-- tarav.breadcrumb 113fd474c151 -->
<!-- tarav.breadcrumb 10cf9642fe1c -->

For example, a Wiki capture workflow may accept a cheap temporary annotation
such as `tarav.context <direct-chatlas-reference>`. On submission it resolves
the User Turn, creates a typed context record attached to a new Breadcrumb,
and replaces the temporary annotation with the opaque Breadcrumb label. The
temporary spelling is workflow input; it does not constrain the canonical
Breadcrumb label or future workflows.
<!-- tarav.breadcrumb 01e97d82ed11 -->
<!-- tarav.breadcrumb c04bf4ff8648 -->
<!-- tarav.breadcrumb 94bb748afdad -->

This keeps capture cheap for Agents: they make a small local annotation while
working, then invoke one final workflow submission to perform resolution,
record creation, surface cleanup, and audit.
<!-- tarav.breadcrumb c3f0d6bc5a48 -->

## Directory record and attachments

Each Breadcrumb should have a directory keyed by its ID. Its entry record
contains only stable Breadcrumb identity. The Breadcrumb does not interpret or
maintain the semantics of its attachments; workflows add, amend, or remove
their own independent typed records within the Breadcrumb directory.
<!-- tarav.breadcrumb 511b00e44130 -->

A candidate logical shape is:

```text
<breadcrumb-id>/
├── main.json
├── locator-observations.jsonl
└── attachments/
    └── <typed workflow records>
```

The precise Tarav storage root remains to be decided. The directory-per-ID
shape supplies a common attachment point without forcing the Breadcrumb to
know the attached records' types or workflows.
<!-- tarav.breadcrumb 7e770ecf353a -->
<!-- tarav.breadcrumb 099dcb99aaf9 -->

## Position resolution and observations

The embedded Breadcrumb identifier is the authoritative position anchor. One
active occurrence resolves the current position; no occurrence or several
occurrences surface missing or duplicated Breadcrumb POIs. Recorded line and
neighborhood data are observations and never replace the in-surface anchor as
position identity.
<!-- tarav.breadcrumb 1ff7a0a5234b -->

Changing location knowledge stays out of `main.json`. New observations append
to `locator-observations.jsonl`, preserving earlier observations rather than
rewriting them as though they remained current.
<!-- tarav.breadcrumb bf55e0c5d788 -->

Each locator observation should use a normal `FilePositionReference`. Its
mechanical locator consists of a file and line. A check can confirm that the
selected position still contains the expected Breadcrumb. Neighborhood data,
such as fragments of the previous and next lines, belongs in `hints` and is
not used by resolution mechanics.
<!-- tarav.breadcrumb 09e4a47e02a5 -->

## Flexible embedded representation

`FilePositionReference` need not require a nested `FileReference`. Its own
`RecordInterface` can explicitly accept either a path string or a reusable
typed file-reference record:

```python
file: str | FileReference.RecordInterface
```

The owning workflow defines how path strings resolve, including relative-path
semantics. A nested `FileReference` remains available when its independent
checks, hints, or behavior are useful.
<!-- tarav.breadcrumb 024416f2f564 -->
<!-- tarav.breadcrumb 50e5a490568e -->

This illustrates the broader Record rule: every top-level Tarav Record must be
typed, while embedded typing is application-dependent. The selected top-level
class and its `RecordInterface` supply the semantic context for primitives,
anonymous structures, and embedded typed Records. Reusing typed primitives is
recommended when their behavior is useful, but it is not mandatory.
<!-- tarav.breadcrumb b69d3ced91ab -->

## Registration fallback — 2026-10-08

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

Registering a Breadcrumb is the one step of capture that is not read-only: it writes to the Breadcrumb store in the Tarav data folder, and a sandbox sometimes prevents that. When registration cannot be done, the surface must not be left without evidence. The fallback is to leave a read-only trace in the surface, the Chatlas session and User-Turn identifiers, so that the Breadcrumbs can be registered later from another sandbox or environment.
<!-- tarav.breadcrumb b13bc4b16acc -->

That trace is the existing provisional form: the session declaration and the provisional context markers stay where the Breadcrumbs would go. A Markdown surface carries its own declaration; a surface without one, such as Python, relies on the same alias being declared in the related Wiki Note or Impl.Req. A later session that can write runs the ordinary `tarav breadcrumbs submit chatlas-context --surface <file>` and then the audit. This was proven the same day: thirteen markers in five files, some of them weeks old, were submitted without any guessing because their declarations were intact. The Project check `Tarav.Project.Dev.ProvisionalMarker` keeps the pending Notes visible as POIs, and a pending registration is reported as pending, not as done.
<!-- tarav.breadcrumb 9bb337c221dc -->

Two related mechanics are easy to miss. Stale label positions after lines move are repaired by rerunning the audit with `--refresh-positions`; several sessions that day wrongly reported that no such operation existed. And a session first used by a later section can be declared in a block beside that section, as this section does, so earlier Breadcrumb lines do not shift.

The `tarav-hugentics` modules for Inlined Capture, Wiki capture, Reading Club, Wiki-backed implementation and commit evidence now state this fallback.

## TypeScript surfaces (draft) — 2026-10-08

The Tarav Center extension had no Breadcrumbs in its TypeScript because no
convention existed. The User asked the agent to draft one itself and to build
it in an autonomous pass.
<!-- tarav.breadcrumb d8eb66d7318b -->

The convention is the agent's draft, not a User decision. TypeScript markers
and labels are `//` line comments, `// tarav.context <alias>:<prefix>` and
`// tarav.breadcrumb <id>`, on `.ts`, `.tsx`, `.mts` and `.cts` files.
`TypeScriptNormalModel` in `tarav.l1.surfaces.typescript` finds comments with a
small lexer that skips strings, template literals with nested expressions,
regular expressions and block comments. Block comments never carry markers. A
lexer diagnostic stops submission and audit, as Python's tokenizer
diagnostics do. Like Python, a TypeScript file has no session declaration;
submission takes `--provider` and `--session-id`. In `.tsx`, `//` inside JSX
text would be read as a comment; that limit is recorded, not handled. See
[Impl.Req 885](../../../tarav-py/notes/live/885-typescript-breadcrumb-convention-impl-req.md).
The extension's four TypeScript files now carry seven Breadcrumbs.

## Short labels — 2026-10-18

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

Surfaces now carry the first 12 characters of a Breadcrumb's ID, as in
`tarav.breadcrumb 51335b338b37`; the registry keeps the full 64. A label names
the one registered ID it starts with. A label matching several IDs is an error
that lists them, and Tarav never picks one: "no automatic disambiguation"
concerns markers already registered. Tarav, not the Agent, writes labels at
submission.
<!-- tarav.breadcrumb 3662dcc770a1 -->

Drawing a new random ID whenever its first 12 characters are taken was
proposed and declined: a collision is unlikely (about 1 in 17 million at
5,736 Breadcrumbs) and narrow in effect, so submission simply reports one.
After choosing the intended Breadcrumb, an Agent or User lengthens its label
one character at a time until it is unique. Full 64-character labels remain
valid as the longest prefix.
<!-- tarav.breadcrumb 2933dddf1a4e -->

The User asked for every existing marker to be migrated, in all 29 places
that carried them, each Git repository with a checkpoint of the work found
there and a migration commit: 4,264 labels in 621 files. Commit messages keep
their full labels (history is not rewritten), and their evidence envelopes
keep full IDs; message labels map to envelope IDs by prefix. Resolution checks
that an observed line contains the 12-character label, which every valid
label of that Breadcrumb contains, so the migration needed no new
observations. See [Impl.Req 918](../../../tarav-py/notes/live/918-short-breadcrumb-prefixes-impl-req.md).
<!-- tarav.breadcrumb c86a4fbe2f89 -->
<!-- tarav.breadcrumb a2785dcc025d -->

Audits were the migration's bottleneck, and the User asked whether that was a
design flaw. Profiling one audit (170 labels, 93 seconds) put 90 seconds in
rebuilding Chatlas Normal Models from raw provider files: the chatlas-context
audit calls `compute_normal_model`, bypassing Chatlas's fresh-checked cache
(5.1 s rebuild against 1.8 s cached load, 0.08 s to open), and a batch audit
rebuilds the same sessions for every file. Using the cache and sharing models
across one command are the proposed fixes, not yet made.
<!-- tarav.breadcrumb 9bee380a3bbb -->

## JSON and TOML surfaces — 2026-10-22

<!-- tarav.sessions
ec6cf584 = codex:01a1563b-2992-7c62-8a38-05c1cc75b1fe @ec6cf5849bb6c4e66f011b015415da94eeb1a17634872aa4fb9e25d8e065ab53
-->

The User explicitly requested JSON/TOML capture after the manager refactor
reported those formats as unsupported.
<!-- tarav.breadcrumb ceac340b5a6f -->

Implemented in [request 941](../../../tarav-py/notes/live/941-breadcrumb-data-surfaces-and-chatlas-reference-recovery-impl-req.md):
TOML uses native `#` comments; JSON uses a `tarav.breadcrumbs` array of strings
at a schema-permitted object position. Submit replaces each provisional string
with its opaque label and preserves the surrounding text. Nested metadata and
several strings on one line work. Ordinary strings are inactive, including TOML
multiline strings containing apparent comments. Both formats use the ordinary
submit, resolve and audit paths and reject invalid native syntax before writes.
These embedding choices are implementation decisions, not additional User design.

New Chatlas-context attachments retain exact cited Turn evidence before replacing
markers. This protects their targets when later normalization changes grouping;
see [Chatlas recovery](chatlas-normal-model.md#exact-cited-turns-and-rollout-collisions--941).
