# Chatlas Normal Model

<!-- tarav.sessions
3dbc7074 = codex:01a0baed-f147-77e2-b298-ed15249a9410 @3dbc7074117a70b90f57c98b25690d3ea15a519f0da6e05043e59b8add00d3c4
-->

## Semantic object and directory representation

The Chatlas Normal Model aggregate is its own Tarav object. It can be
materialized on demand and remain entirely derived and rebuildable; those
storage mechanics do not transfer semantic ownership to a cache system.
<!-- tarav.breadcrumb 673fdf452db8 -->
<!-- tarav.breadcrumb fc08b487e1d4 -->

Its canonical serialization is a directory rooted at the Model identity:

```text
normal-model/<identity>/
  main.json
  events.jsonl
  messages.jsonl
  turns.jsonl
  loaded-contexts.jsonl
```

`main.json` declares the Normal Model's registered type and aggregate
metadata. The JSONL files serialize its typed semantic collections. The
Normal Model module owns this shape, loading, validation, normalization, and
materialization.
<!-- tarav.breadcrumb 93f5c5c9538c -->
<!-- tarav.breadcrumb fa438431605a -->

## Cache decoration

Caching is a Chatlas mechanism that uses the Normal Model; the Normal Model
does not depend on or need to know about caching. Cache code therefore belongs
outside the Normal Model module.

When a materialized Model participates in caching, the cache system may add an
ordinary operational file to the same directory:

```text
normal-model/<identity>/
  main.json
  events.jsonl
  messages.jsonl
  turns.jsonl
  loaded-contexts.jsonl
  cache.json
```

The Model loader owns and reads only its canonical files and tolerates
unowned auxiliary files. A missing or invalid `cache.json` makes freshness or
reuse unavailable; it does not invalidate the Normal Model. Cache mechanics
may stage the canonical representation, add `cache.json`, and atomically
install the directory without becoming the representation's semantic owner.
<!-- tarav.breadcrumb 923e021836ac -->

This arrangement keeps the Normal Model at the directory root. Cache state is
an optional operational attachment rather than a wrapper object or semantic
subtype.
<!-- tarav.breadcrumb 07d513308f3e -->

## Session and representation navigation

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

ChatSession represents the session separately from its retained representations.
The selected navigation direction is Chatlas → ChatSession → Model → Turn,
with Messages and supporting Events available through deeper relationships.
<!-- tarav.breadcrumb 79ee770dacca -->

The user accepted the proposed shape `sessions.get(session_id).open()` followed
by `session.model()`. The first implementation slice introduces ChatSession and
its connection to the existing Normal Model; Turn/Message/Event navigation can
follow progressively without redesigning their retained formats. This remains
a design, coordinated in [823](../../../tarav-py/notes/live/823-chat-session-model-navigation-impl-req.md).
<!-- tarav.breadcrumb 124748b606f8 -->

## Session navigation implementation — 823

<!-- tarav.sessions
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
-->

The user requested implementation of 823. The implemented
[Session view](../../../tarav-py/src/tarav/l1/chatlas/sessions.py) supports
`ChatSessions(...).get(session_id).open()` and `session.model()` through the
existing reader/cache. Native session IDs are the default folder keys; collisions
require provider/instance scope or an explicit `key_by="identity_hash"` view.
`get_by_identity()` also selects an exact identity. Opening an entry does not
capture or normalize. The portable ChatSession Record retains its selectors and
existing identity hash, while `bind_root()` selects runtime storage without
persisting a depot path. The [Session tests](../../../tarav-py/tests/chatlas_normal_model/test_sessions.py)
verify read-only navigation, Record dispatch, root isolation, real normalization,
cache reuse, and explicit availability errors. Deeper collection navigation is
still follow-up work; this implementation advances the earlier design status.
<!-- tarav.breadcrumb ef7ede98c40e -->

## Cache freshness from the raw data — 919

<!-- tarav.sessions
3537df0a = claude-code:2bff854f-66a0-4e8c-8f96-9078af34c479 @3537df0a6015d884a94e9594478f971cb92e38df63776b87b5eea38741740d8a
-->

Cache validation is only about whether the raw data changed. Each cached
artifact is paired with the `raw_version` of the raw data it used: a hash of
the transcript sources' paths, sizes and modification times, which the capture
side writes into the Session Index row. Code evolution is outside the
validation workflow; invalidating after a normalizer change is the
maintainers' responsibility, not the code's. The earlier cache key also
carried the tarav-py Git HEAD, so every commit made every cached Model stale.
<!-- tarav.breadcrumb 0884213d7e7e -->
<!-- tarav.breadcrumb 948b67aabef3 -->

Parts are cached and judged separately. `cache.json` records the version each
part (`main`, `events`, `messages`, `turns`, `loaded_contexts`) was built
from. Some consumers, such as search, use what is cached; others request a
brand new Model.
<!-- tarav.breadcrumb 913b6c3bed3d -->

The library and the public surfaces have separate jobs. The library gives all
access with full information: `NormalModelCache` returns what is stored with a
fresh or stale flag per part and never builds on its own. The CLI and other
public surfaces choose a safe path, building when a part they need is missing
or stale. Implemented in
[919](../../../tarav-py/notes/live/919-chatlas-raw-version-cache-impl-req.md):
all 10,180 indexed rows now carry a `raw_version`, and the depot no longer
tracks `normal-model/` in Git.
<!-- tarav.breadcrumb 10d1eae421f5 -->
<!-- tarav.breadcrumb 4ec272724dde -->
