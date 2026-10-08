# Tarav Breadcrumbs

<!-- tarav.sessions
3dbc7074 = codex:01a0baed-f147-77e2-b298-ed15249a9410 @3dbc7074117a70b90f57c98b25690d3ea15a519f0da6e05043e59b8add00d3c4
-->

## Surface anchors for annotations

A `Tarav.Breadcrumb` is an opaque, stable anchor embedded at a position in a
Product.Surface. The Breadcrumb is an annotation attachment primitive rather
than an annotation: typed records attached by workflows provide the semantics,
while the crumb left inside the surface identifies where they apply.
<!-- tarav.breadcrumb ddc56f53bb58bc0e5cf2cea4a02e36a8cba8d84e0e7140b491522a0e5001a8c7 -->
<!-- tarav.breadcrumb 88752794558e0cda58a9bfa0fbac009f717abd4d8bfc45d131362bd3d0c142df -->
<!-- tarav.breadcrumb e49816883e6e0e5036c809f9088229a4aa7e53ddc2b77c90af793e63c05ab015 -->
<!-- tarav.breadcrumb 7aa0c74bc9b3f5508b04236a8b73d14e51cb94d3bd20eb1c23fd53e0134bcc9a -->

The durable surface form can therefore be a generic opaque label such as
`tarav.breadcrumb <id>`. Its identifier carries position identity rather than
annotation meaning. Resolving the identifier finds the Breadcrumb record and
the records attached at that point.
<!-- tarav.breadcrumb 8dc93616ef5e8242fcf9dfa3cd905a82f3ac5eab996f81ae50e8b6104d267308 -->
<!-- tarav.breadcrumb 11f1d010dd6de97fb6f38523492724aad28dbb80d3cfd89a0c4242e62fb8a119 -->

## Breadcrumb workflow

`Tarav.Breadcrumbs` is the general workflow pattern within which other surface
workflows operate. An Agent may create or select a Breadcrumb and attach a
record directly. Alternatively, a surface workflow can parse temporary
annotations, resolve their inputs, create Breadcrumbs and attachment records,
and clean the surface automatically.
<!-- tarav.breadcrumb d7f72a218b25591174316384c20f57f2888b029f9a7825dcf5a4d1f10fded8ce -->
<!-- tarav.breadcrumb 113fd474c151ab34728bd3b04a506cfa10418c0988c42117469add71e64e1a4a -->
<!-- tarav.breadcrumb 10cf9642fe1cb384e78398e59180ca6b73ac5e730ab7aed2cf44be36e0c2ac1f -->

For example, a Wiki capture workflow may accept a cheap temporary annotation
such as `tarav.context <direct-chatlas-reference>`. On submission it resolves
the User Turn, creates a typed context record attached to a new Breadcrumb,
and replaces the temporary annotation with the opaque Breadcrumb label. The
temporary spelling is workflow input; it does not constrain the canonical
Breadcrumb label or future workflows.
<!-- tarav.breadcrumb 01e97d82ed11367cf22c16101c365992fbba65435a8f9330e0f27c82cbd65b54 -->
<!-- tarav.breadcrumb c04bf4ff8648733cfde23f3c3b4038d3b3ba4370a1ea6e2331fc250cd925a71f -->
<!-- tarav.breadcrumb 94bb748afdad6ef58bf2d9e2f73e9c1601ddd56721607abe06aa6a942d4cc363 -->

This keeps capture cheap for Agents: they make a small local annotation while
working, then invoke one final workflow submission to perform resolution,
record creation, surface cleanup, and audit.
<!-- tarav.breadcrumb c3f0d6bc5a48a4aead1e89cd8ea763ae09d737a8551a396a4fe117d75223f968 -->

## Directory record and attachments

Each Breadcrumb should have a directory keyed by its ID. Its entry record
contains only stable Breadcrumb identity. The Breadcrumb does not interpret or
maintain the semantics of its attachments; workflows add, amend, or remove
their own independent typed records within the Breadcrumb directory.
<!-- tarav.breadcrumb 511b00e44130ebc3d56f770cb19c2f342a209b3ca47c9a2bdc4c35d5ff80d735 -->

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
<!-- tarav.breadcrumb 7e770ecf353a754b3dd14140e76a5a01bc8a9ba0e0ce4f982e4f16168b8ced78 -->
<!-- tarav.breadcrumb 099dcb99aaf96102c85b245a7f2f70773ca60defc578cc134db0a26e7e50fc3f -->

## Position resolution and observations

The embedded Breadcrumb identifier is the authoritative position anchor. One
active occurrence resolves the current position; no occurrence or several
occurrences surface missing or duplicated Breadcrumb POIs. Recorded line and
neighborhood data are observations and never replace the in-surface anchor as
position identity.
<!-- tarav.breadcrumb 1ff7a0a5234bcd6dc960423eac2a98e90729aa88f697793dc61f2ea70657bd1c -->

Changing location knowledge stays out of `main.json`. New observations append
to `locator-observations.jsonl`, preserving earlier observations rather than
rewriting them as though they remained current.
<!-- tarav.breadcrumb bf55e0c5d78814e07e99c3a2811950e1600a24d4249006e149c3a094e293b97b -->

Each locator observation should use a normal `FilePositionReference`. Its
mechanical locator consists of a file and line. A check can confirm that the
selected position still contains the expected Breadcrumb. Neighborhood data,
such as fragments of the previous and next lines, belongs in `hints` and is
not used by resolution mechanics.
<!-- tarav.breadcrumb 09e4a47e02a5e96b6c145ce3bb6499808694bf7e5ec32a2a68c0206b341d25b0 -->

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
<!-- tarav.breadcrumb 024416f2f564245fb340593405f8a924134012c9a8c289a9301ee541a4ce4a3e -->
<!-- tarav.breadcrumb 50e5a490568e44789f25ac80c840222998c81d8cc2b97ecf8225aa0fc3a8c7ca -->

This illustrates the broader Record rule: every top-level Tarav Record must be
typed, while embedded typing is application-dependent. The selected top-level
class and its `RecordInterface` supply the semantic context for primitives,
anonymous structures, and embedded typed Records. Reusing typed primitives is
recommended when their behavior is useful, but it is not mandatory.
<!-- tarav.breadcrumb b69d3ced91ab095467117847483676612eba47fb4af982f9d00485be8c525cf5 -->

## Registration fallback — 2026-10-08

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

Registering a Breadcrumb is the one step of capture that is not read-only: it writes to the Breadcrumb store in the Tarav data folder, and a sandbox sometimes prevents that. When registration cannot be done, the surface must not be left without evidence. The fallback is to leave a read-only trace in the surface, the Chatlas session and User-Turn identifiers, so that the Breadcrumbs can be registered later from another sandbox or environment.
<!-- tarav.breadcrumb b13bc4b16acc8f800913779143b1a83c0346945255dae696083a488c5be6c9b9 -->

That trace is the existing provisional form: the session declaration and the provisional context markers stay where the Breadcrumbs would go. A Markdown surface carries its own declaration; a surface without one, such as Python, relies on the same alias being declared in the related Wiki Note or Impl.Req. A later session that can write runs the ordinary `tarav breadcrumbs submit chatlas-context --surface <file>` and then the audit. This was proven the same day: thirteen markers in five files, some of them weeks old, were submitted without any guessing because their declarations were intact. The Project check `Tarav.Project.Dev.ProvisionalMarker` keeps the pending Notes visible as POIs, and a pending registration is reported as pending, not as done.
<!-- tarav.breadcrumb 9bb337c221dc4daebaf868f48cb7af2389d3617af36dbda53061c1d0a77ce882 -->

Two related mechanics are easy to miss. Stale label positions after lines move are repaired by rerunning the audit with `--refresh-positions`; several sessions that day wrongly reported that no such operation existed. And a session first used by a later section can be declared in a block beside that section, as this section does, so earlier Breadcrumb lines do not shift.

The `tarav-hugentics` modules for Inlined Capture, Wiki capture, Reading Club, Wiki-backed implementation and commit evidence now state this fallback.
