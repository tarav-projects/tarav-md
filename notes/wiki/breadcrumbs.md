# Tarav Breadcrumbs

<!-- tarav.sessions
3dbc7074 = codex:01a0baed-f147-77e2-b298-ed15249a9410 @3dbc7074117a70b90f57c98b25690d3ea15a519f0da6e05043e59b8add00d3c4
-->

## Surface anchors for annotations

A `Tarav.Breadcrumb` is an opaque, stable anchor embedded at a position in a
Product.Surface. The Breadcrumb is an annotation attachment primitive rather
than an annotation: typed records attached by workflows provide the semantics,
while the crumb left inside the surface identifies where they apply.
<!-- tarav.context 3dbc7074:d2d9885a64e821b1 -->
<!-- tarav.context 3dbc7074:f7c0a33122f9799c -->
<!-- tarav.context 3dbc7074:fcde51a768e8fabc -->
<!-- tarav.context 3dbc7074:e80da0b1b7837546 -->

The durable surface form can therefore be a generic opaque label such as
`tarav.breadcrumb <id>`. Its identifier carries position identity rather than
annotation meaning. Resolving the identifier finds the Breadcrumb record and
the records attached at that point.
<!-- tarav.context 3dbc7074:dc5a9dcb733cd749 -->
<!-- tarav.context 3dbc7074:e80da0b1b7837546 -->

## Breadcrumb workflow

`Tarav.Breadcrumbs` is the general workflow pattern within which other surface
workflows operate. An Agent may create or select a Breadcrumb and attach a
record directly. Alternatively, a surface workflow can parse temporary
annotations, resolve their inputs, create Breadcrumbs and attachment records,
and clean the surface automatically.
<!-- tarav.context 3dbc7074:aa6844a49db1d0b2 -->
<!-- tarav.context 3dbc7074:b482720a72501c83 -->
<!-- tarav.context 3dbc7074:e80da0b1b7837546 -->

For example, a Wiki capture workflow may accept a cheap temporary annotation
such as `tarav.context <direct-chatlas-reference>`. On submission it resolves
the User Turn, creates a typed context record attached to a new Breadcrumb,
and replaces the temporary annotation with the opaque Breadcrumb label. The
temporary spelling is workflow input; it does not constrain the canonical
Breadcrumb label or future workflows.
<!-- tarav.context 3dbc7074:dc5a9dcb733cd749 -->
<!-- tarav.context 3dbc7074:b482720a72501c83 -->
<!-- tarav.context 3dbc7074:e80da0b1b7837546 -->

This keeps capture cheap for Agents: they make a small local annotation while
working, then invoke one final workflow submission to perform resolution,
record creation, surface cleanup, and audit.
<!-- tarav.context 3dbc7074:dc5a9dcb733cd749 -->

## Directory record and attachments

Each Breadcrumb should have a directory keyed by its ID. Its entry record
contains only stable Breadcrumb identity. The Breadcrumb does not interpret or
maintain the semantics of its attachments; workflows add, amend, or remove
their own independent typed records within the Breadcrumb directory.
<!-- tarav.context 3dbc7074:eb0176d543222b4a -->

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
<!-- tarav.context 3dbc7074:eb0176d543222b4a -->
<!-- tarav.context 3dbc7074:a0231bb651b05773 -->

## Position resolution and observations

The embedded Breadcrumb identifier is the authoritative position anchor. One
active occurrence resolves the current position; no occurrence or several
occurrences surface missing or duplicated Breadcrumb POIs. Recorded line and
neighborhood data are observations and never replace the in-surface anchor as
position identity.
<!-- tarav.context 3dbc7074:e80da0b1b7837546 -->

Changing location knowledge stays out of `main.json`. New observations append
to `locator-observations.jsonl`, preserving earlier observations rather than
rewriting them as though they remained current.
<!-- tarav.context 3dbc7074:a0231bb651b05773 -->

Each locator observation should use a normal `FilePositionReference`. Its
mechanical locator consists of a file and line. A check can confirm that the
selected position still contains the expected Breadcrumb. Neighborhood data,
such as fragments of the previous and next lines, belongs in `hints` and is
not used by resolution mechanics.
<!-- tarav.context 3dbc7074:55f7d43aab1dab55 -->

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
<!-- tarav.context 3dbc7074:0faef4ba5b49b773 -->
<!-- tarav.context 3dbc7074:0c0ecc3a242ba0cb -->

This illustrates the broader Record rule: every top-level Tarav Record must be
typed, while embedded typing is application-dependent. The selected top-level
class and its `RecordInterface` supply the semantic context for primitives,
anonymous structures, and embedded typed Records. Reusing typed primitives is
recommended when their behavior is useful, but it is not mandatory.
<!-- tarav.context 3dbc7074:0c0ecc3a242ba0cb -->

