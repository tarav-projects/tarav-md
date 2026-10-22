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

## Searching across chats — 920

Tarav's Search workflow does not know about Chatlas. The Chatlas workflow
provides a search engine for its own data, because Chatlas is the one that
knows how to search its database. The interface is minimal, with simple
queries for now.
<!-- tarav.breadcrumb 20e980c50f0b -->

A search can be split by construction: messages only, or turns. The caller
decides; turns are the default, and a session without a cached Model is built
when searched. Stale caches are searched as stored and their hits say so.
Implemented in
[920](../../../tarav-py/notes/live/920-chatlas-search-engine-impl-req.md) as
`tarav.l1.chatlas.search`, registered in the runtime's Search service.
<!-- tarav.breadcrumb 54b97a3161be -->
<!-- tarav.breadcrumb f73415abce38 -->

## The Normal Models index and the pipeline — 923

Chatlas produces and caches the Normal Models; an index on top of them gives
fast and expressive search. It is named for what it holds, not for search,
because other consumers can use it: `index/normal-models.sqlite` in the
Chatlas root. The JSON Normal Model stays; the chain is generation → cache →
SQL index.
<!-- tarav.breadcrumb c84caa542bfe -->
<!-- tarav.breadcrumb c525d38d0853 -->
<!-- tarav.breadcrumb 647eb4b330d5 -->

One freshness rule runs along the chain: the raw data declares its version,
each cache file declares its own (a pass-through of the raw version it used),
and so on; a stage is fresh while the version it recorded is still the one its
input declares.
<!-- tarav.breadcrumb ed07a895f4e9 -->
<!-- tarav.breadcrumb 64b39a4527e2 -->

The pipeline runs on demand and the consumer controls it. Search reads the
index only; updating is on request, with different flags for different parts
of the pipeline, which together run the whole update from the native provider
folders to the index. Search may read what is stored without checks,
configured like the rest of its query.
<!-- tarav.breadcrumb 55dd83a8d086 -->
<!-- tarav.breadcrumb 864991df25d4 -->
<!-- tarav.breadcrumb 1a28b5e941e8 -->

Designed in
[923](../../../tarav-py/notes/live/923-normal-models-index-and-chatlas-pipeline-impl-req.md);
open: matching by words or by substring, and whether agent messages are
indexed.

The interface is expressive, even allowing direct SQL queries: search matches
words, full-text expressions or substrings, and any consumer can run read-only
SQL over the index. The index keeps only what lookups need; the full records
stay in the JSON cache. Implemented in 923: 338 MB for 10,146 chats, built in
about half a minute; a search over every chat answers in tens of
milliseconds.
<!-- tarav.breadcrumb da7492bc6466 -->
<!-- tarav.breadcrumb 4f6534f53ddc -->

## Native Codex voice transcripts — 935

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

The User requested recovery of a spoken passage and investigation of why
Chatlas Query could not find it, then selected Develop to update the
normalizer. The raw voice text had been captured; native voice projection
into Messages and Turns was missing. Tests protect the corrected behavior,
without retaining the broken implementation or adding a compatibility layer.
<!-- tarav.breadcrumb e7d9d4033dd1 -->
<!-- tarav.breadcrumb 8f90c34c1d85 -->
<!-- tarav.breadcrumb eb9daea2cffe -->

Implemented in [request 935](../../../tarav-py/notes/live/935-codex-voice-normalization-impl-req.md).
The [Codex normalizer](../../../tarav-py/src/tarav/l1/chatlas/normal_model/codex.py)
now projects `realtime_item` / `transcript_segment` records with string text
and User or Assistant roles into the existing User/Agent Events and Messages.
Text is preserved verbatim, and the existing Turn assembly, Query, typed
references, and SQL index consume the result. Voice lifecycle metadata and
malformed/unknown-speaker segments are not fabricated Messages. Recording
speech does not establish Agent.Loaded.Context consumption relationships.
The [voice tests](../../../tarav-py/tests/chatlas_normal_model/test_codex_voice.py)
exercise normalization through cache, Query and index, speaker grouping,
provenance, exclusion cases, and amendment hashes.
<!-- tarav.breadcrumb 71c32225cff3 -->

This exact session's derived cache and index were rebuilt with the existing
ChatlasStages `all` policy. All 32 voice segments in the inspected active
rollout (15 User and 17 Assistant) are present. The recovered 3,435-character
User passage matches the raw text exactly and resolves through ordinary Query
as Turn `dff422f65430f52a`; raw transcript bytes were unchanged. Existing cache
freshness remains based on raw input, so other previously built session
models require an explicit rebuild to receive the corrected projection.
<!-- tarav.breadcrumb 903f4f36879d -->

The recovery inspection also exposed an independent source-merging limit:
115 of 177 voice segments in the older retained rollout are absent by exact
text from the merged Model. A concrete older User voice Event and a different
record in another rollout receive the same address (native session scope
plus record index); pipeline reconciliation replaces the former. Both raw
sources remain retained. This change does not redefine source authority,
fork identity, or Event addressing; the measured collision and affected
counts are recorded in request 935 for separate design and repair.

## Exact cited Turns and rollout collisions — 941

<!-- tarav.sessions
ec6cf584 = codex:01a1563b-2992-7c62-8a38-05c1cc75b1fe @ec6cf5849bb6c4e66f011b015415da94eeb1a17634872aa4fb9e25d8e065ab53
-->

The User requested investigation and repair of the twelve older chat references
reported during the manager refactor.
<!-- tarav.breadcrumb 9c68f01d6637 -->
<!-- tarav.breadcrumb 68f5d3454be0 -->

[Request 941](../../../tarav-py/notes/live/941-breadcrumb-data-surfaces-and-chatlas-reference-recovery-impl-req.md)
fixes the measured merge problem above: different payloads at a reused native
Event address remain separate deterministic variants; exact copied Events merge
their source observations. Messages and loaded contexts follow the corresponding
variant. The current aggregate now retains all the observed payload variants.

Exact cited Turns are separately retained as immutable, validated snapshots in
the Chatlas Record Registry partition. They carry the Turn, Messages, supporting
Events, raw-source observations and producer commit. The original three-coordinate
reference stays pinned; resolution explicitly reports `retained-snapshot` when
using that representation. Capture retains this evidence before registering
new Breadcrumb attachments. The current aggregate remains replaceable.

All nine exact Turns backing the twelve reported labels were reconstructed from
retained raw without retargeting labels: seven with current normalization of one
tape, two with the pre-voice normalizer loaded once from Git. The historical
normalizer is not shipped. Four other previously cited Turn boundaries affected
by the corrected merge were preserved from the exact prior validated projection.
The original three affected surfaces audit with zero POIs after recovery.

The full Project check also exposed a Notebook consumer that queried only current
Turns before resolving its evidence references. It now uses the same exact-reference
result and Event chronology for source/producer/approval order. Eleven referenced
Notebook Turns were retained from their exact previous projection; no support or
review claims were retargeted. Regression tests verify both continued support
resolution and rejection of an approval preceding its proposal.
