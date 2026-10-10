# POI visibility, navigation, and blessings

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
1ae20f8c = codex:01a0ff32-0ec2-7b72-8850-fa795135f3c9 @1ae20f8c8159f12d2402ea702cf49c876ec46a72f71ce12423ae1dbdf2a91871
64298cbc = claude-code:9da4cef5-68b7-4d17-8a06-1351ca51e82f @64298cbc8db2e7aa971e0828653c07bcb483cfed40931fdf87d5abe7ce1c60b3
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## Current design direction — 2026-10-09

This note is a history: its sections were written as the design moved, and
several describe mechanisms the design has since left. The User asked that
the Wiki state the current design and not only append to it.
<!-- tarav.breadcrumb 5a3d45aa9a03be55c284349393eb0d7627d186931662057663ff5227a80a67ea -->

Where the design stands:

- A POI is only the event that a situation was found. It carries the check,
  the situation, the evidence and a descriptive message, and no instructions.
- An actionable POI spins one action. That run is the persistent thing that
  was called a tracked POI. It closes by one of several paths: the situation
  is gone, it was dismissed, or what it asked for was provided.
- A blessing is the dismissal path. The word may be dropped.
- Guidance about what to do belongs to the action and its skill.

The last section of this note, "A POI is an event; what follows it is an
action", holds the discussion. What that makes of the earlier sections:

| Section | Standing |
| --- | --- |
| Detection, navigation, situation identity, atomic types, reported POIs | Current. |
| Recorded blessings; composable blessings; revisable blessing attention | The blessing code still exists, for Skillware packages and scored assessment. For Project POIs, dismissing the POI's action is in place beside it (request 895, first part). |
| Tracked POIs, the board; POI tracking with status axes; record status changes only | History. The tracking code was removed by request 894: the record is now an action in the central registry, and its history is that registry's Git history. |
| Neutral POIs and the producer–reader gap | Current. Request 893 removed the two fields; a Type's descriptive notes appear in the POI's context, and an action's skill says what to do. |

## Detection and presentation

### Points of interest, not inherently problems

A POI is a claim that something is of interest. It does not inherently imply
negativity, failure, or a required corrective action. This clarification
broadens the problem-oriented examples elsewhere in this note.
<!-- tarav.breadcrumb 8abe33d8f10332db0c5b33fc46c2b5db5158b467244a25704e3185c81fe780f3 -->

The base POI has two initial specializations: `CheckPOI`, coupled to the bound
Check object that produced it, and `NotificationPOI`, reporting an event or
operation worth making visible without requiring a Check. In Breadcrumb
auditing, a stale position is the first case; appending a location observation
is the second. `NotificationPOI` is the selected name, replacing the tentative
`LogPOI`.
<!-- tarav.breadcrumb 7690a9f80fa88f6a48be676f42d9762e7a5383f411e15450d725cb0e75875fea -->
<!-- tarav.breadcrumb b415403c377459d6197ea71ba7f6f8f94834fce694ac1afeb9c66e1e0c6f47d4 -->
<!-- tarav.breadcrumb d697c96ab0ef939098d62c1d6c34fd54ada553eea7e79dc01f455fea0593b944 -->

Check code raises only failure POIs by default. That is a checking convention,
not a restriction on POI meaning; positive results can also be points of
interest. The [Checks workflow](checks-workflow.md) owns the Check-coupled
specialization while sharing the general POI base. Notification mechanics
may use lighter context, such as creation and raise locations; their exact
schema remains open.
<!-- tarav.breadcrumb f8f7a8a5028c38ff390abdf6f8922a38c3d8a199f50cb0a0a110c98692daddd9 -->
<!-- tarav.breadcrumb 6a9a8c7a5a330bac00873015b2c857cf6cec13ab47979ab0319bb8366ceb65b9 -->

Detection retains all findings, including blessed ones. Presentation defaults
to all POIs in scope, with compact counts/grouping and bounded pages. Agents
can selectively expand evidence, check code, documentation, or blessing
records. This separates full finding visibility from how much material enters
the agent's context.
<!-- tarav.breadcrumb d4ecde7c9dca8847c5c9a1bb1adf063b56c6fe550d01223a2180c2b0671e2f80 -->

POIs are analogous to automatic issues. Their existence does not mean an agent
must address all of them during every task. Users and agents choose which
findings to address for a particular workflow; navigation should protect the
agent's context from being flooded.
<!-- tarav.breadcrumb 1de53d518beda0af7d752cb6dfc50665607d48b30640dbe9c9bbec1fe73a3333 -->

## Minimal navigation

An agent facing a POI needs a route to understand what it checks and where its
documentation lives. The initial navigation primitive can simply point to the
path of the POI class. A richer navigation interface is not a prerequisite for
providing that entry point.
<!-- tarav.breadcrumb 91344e5ea648264a4f4137c9317bd53f4c727886930aab86bfe1ca3bfc50ee3b -->
<!-- tarav.breadcrumb 2e48db834bb596358c667bbbf669ec45043b36582e31ee5a065261c02cc60c56 -->

## Recorded blessings and permitted resolutions

*As design, overtaken on 2026-10-09: blessing becomes the dismissal close path
of the POI's action. The blessing code still exists beside dismissal.*

### Minimal base and specialization ownership

Keep the shared POI base almost empty for now. Check-coupled semantics belong
on CheckPOI rather than becoming requirements for every point of interest.
NotificationPOI belongs directly to the POI workflow for the moment. The
foundation and Breadcrumb integration are planned in
[request 832](../../../tarav-py/notes/live/832-neutral-pois-checks-and-breadcrumb-audits-impl-req.md).
<!-- tarav.breadcrumb 84bbfb38d647a85ee4c734ebd6938623314d4a9f20ec89d7573484a91bf214df -->
<!-- tarav.breadcrumb 32cd6269b37755e08862c845eeea1f83f41fe3854c6e23d8d6876897efe72123 -->

### Neutral foundation implemented

Request 832 implemented the nearly empty `POI`, POI-owned
`NotificationPOI`, and Checks-owned `CheckPOI`. Every `CheckPOI` retains its
bound runtime `Check`; a completed `CheckResult` may therefore contain failure
POIs without confusing validation outcome with execution failure. Breadcrumb
file and commit audits now return one mixed POI stream: unresolved concerns are
CheckPOIs, while successful opt-in position refreshes are NotificationPOIs and
do not fail the audit.
<!-- tarav.breadcrumb 25a3d8ca9b8349bad8b4be0da7110da7040c73c859f8ac201be9cedfb7a045c8 -->

POI diagnostic payloads do not occupy the `context` attribute. The normal
`TaravObject.context()` entry point remains callable and exposes diagnostic
details and, for a `CheckPOI`, its exact bound Check through `obj_context`.
<!-- tarav.breadcrumb ce67a9ca6579a653135e5c1873ca487a4bf48d575d50020541f07e4bb2c33137 -->

The existing SKW `POICheck`/`POIInstance` finding model remains operational and
will migrate separately. Request 832 changes only its import boundary; it does
not reinterpret retained SKW finding Records.
<!-- tarav.breadcrumb 76e537d68e30e31f947e22ace2124bc6087179a8b4fc5962e9264df8272432ee -->

A blessing is an agent action accepting the state as valid despite a raised
POI. Blessing actions must be recorded so they can be scored. A blessed POI
remains visible, marked as blessed rather than disappearing from the findings.
<!-- tarav.breadcrumb 8dd9d281d74524536f84abc6d436511107491e4e7ad5afe44526d1a82dbcd0cd -->
<!-- tarav.breadcrumb dbcc606ac63b9ce594392f9d2bd4e2424239e99e58b7aae9363e0a2decd745b1 -->

Not every POI is blessable. Some represent errors whose intended resolution is
fixing the analyzed surface. The blessing system must preserve that distinction.
These are design requirements; this capture does not assert a completed
implementation or settle the blessing Record schema.
<!-- tarav.breadcrumb a97b61b83a06129ee2e2dfb0f0fd18924c391330b1002ff8ef8dfd283936ca9f -->

## Workflow-owned types and composable blessings

The first migration pass should define POIs in the workflows producing them,
subtyping the common POI base while preserving existing detection mechanics.
Blessing semantics belong to a separate workflow with a BlessablePOI base,
rather than becoming requirements for every POI.
<!-- tarav.breadcrumb 9448bf2344fea72adb9c7b1ef065e889db2aa1fe0bc4f78b5a336e9b70b81cf6 -->

A concrete workflow-owned POI may inherit both CheckPOI and BlessablePOI.
The accepted example is StaleGenerationPOI(CheckPOI, BlessablePOI), owned by
SKW: checking and blessing capabilities compose without changing its owner.
This establishes a modeling pattern, not universal permission to bless every
check outcome. [Request 833](../../../tarav-py/notes/live/833-workflow-owned-pois-and-blessings-impl-req.md)
plans the follow-up migration after 832.
<!-- tarav.breadcrumb 172e9cb5c36229dd35cea7f297a83f5576c86248cc93c198ee338bfde455211c -->
<!-- tarav.breadcrumb 3040b3d79f5a9c762ba9fa6874319c76a5faca1b4c6d2c5b154bb752988f054c -->

### Workflow migration implemented

[Request 833](../../../tarav-py/notes/live/833-workflow-owned-pois-and-blessings-impl-req.md)
implemented the migration. POI now supplies neutral, identified, notification,
and collection foundations. References, Navigation, Skills, SKW, Breadcrumbs,
Archive, and provisional Diagram reporting use workflow-owned concrete POIs;
the old kernel occurrence marker and parallel POI check/occurrence types were
removed.
<!-- tarav.breadcrumb 6f11b15dfaa36017af236e82a787c7a92dc12a05cc958ae93684d04868d34a70 -->

Blessings are now an independent workflow. `BlessablePOI` is the capability:
a concrete POI is blessable only when its class inherits it. The implementation
does not retain an occurrence-level boolean or an old generic occurrence model.
Check-owned behavior composes with blessability through multiple inheritance,
while the concrete workflow remains the semantic owner.
<!-- tarav.breadcrumb 6d32637f2a47a7fe9d66c98e0e4d27088aa24dc9307c51ea469f191aa037f896 -->

Typed notifications now have shared delivery. They warn once by default or are
captured explicitly without duplicate delivery. Archive uses this path for a
skipped suspicious remote while preserving its ordinary artifact return value.
<!-- tarav.breadcrumb 5791a5f84456453a1f4a41310b729a0023d8a6e12ec39a6b7f6c9004e87bf86c -->

### 2026-10-01 — Situation is the identity input

The next design replaces the separate identity/state model described above.
An identified POI is identified by its concrete class Ship and an explicit
caller-supplied `situation`. Blessings are one application of that identity,
not its definition. There is no second POI state under the same identity.
Producers decide which inputs distinguish situations; prefer a concern
resurfacing for reblessing over accidentally treating a new concern as blessed.
<!-- tarav.breadcrumb 6b9ffe48e00b884a0d118ddc08674245a1312244a066e40a5d8d52b1a0cf1402 -->
<!-- tarav.breadcrumb c31b79dbad097e4e61f431c619b366db77f0db20214f543ecd2c423bd088f930 -->

A producer can represent recurring equivalent situations or intentionally
fresh occurrences. The situation must be a LiteRecord: dictionary-shaped data
whose accepted values have controlled serialization. Supported native values,
such as dates and Tarav Types, need not be manually converted by callers.
Unsupported objects are not accepted merely because they can be stringified.
<!-- tarav.breadcrumb a3381fa6a0ac200a485612966357671e6eb9197eec87ac4a428550d82d6cc646 -->
<!-- tarav.breadcrumb 06d3860c914cdcd1010bf2a4b15e43dd74e210d134de0bc7ea3a2be3d042b6d0 -->
<!-- tarav.breadcrumb 367513415a77439aa627d488aedc9e3b3ddb937407f9b632492199b811a3ef94 -->

[Request 834](../../../tarav-py/notes/live/834-situation-poi-identity-and-lite-records-impl-req.md)
carries the implementation plan. This section records the new design, not a
claim that the current implementation already follows it.

### Situation identity implemented

Request 834 implemented `LiteRecord` as the controlled, deterministic value
contract for caller-declared situations. `IdentifiedPOI` now derives identity
from its concrete class Ship and explicit situation; evidence and presentation
remain outside identity, while producers include revision inputs when a changed
surface must produce a new situation.
<!-- tarav.breadcrumb 1025bc0dd5374da0251638f7123f905b80348fa839821ce2d417c664658e228d -->

Repeated emissions of one situation remain distinct report occurrences. A
collector addresses them by the stable situation identity plus a zero-based,
evaluation-local emission index. The index is navigation data and does not
participate in identity or blessing.
<!-- tarav.breadcrumb 849ab6b37feb2cf4c16c9cf7476c9b0ba3df518bcc92f3a648f41031fc35578d -->

Blessings now retain and validate the situation identity directly, with only
`blessed` and `unblessed` standing. CLI inspection exposes occurrence indexes,
and the implementation is documented and verified in Request 834.
<!-- tarav.breadcrumb 8110cf98d0196230887cba7e9f457c767d3cfbe350ac8a68b2fa73062210b916 -->

## Revisable blessing attention

Detection remains authoritative about whether a POI still exists. A blessing
accepts that exact situation for now, without erasing it. An attention view
can defer a still-detected, reviewed POI, show when its next review is due,
and always let an agent inspect or force review of deferred entries. A POI
that no longer appears in the current evaluation has no attention schedule.
<!-- tarav.breadcrumb def8b47d7f1b7b6abdb46cd0d9415fe63cd01134c686466e7394fe81c74968b2 -->
<!-- tarav.breadcrumb ebad637d2356361702cbbe3752afde31622b0fb0f41527b259a63725274db309 -->

Request [849](../../../tarav-py/notes/live/849-blessing-attention-and-reassessment-impl-req.md)
implemented a separate pageable `attention_report` over a current collector,
BlessingStore, and ScoringRepository. Its pilot policy defers a first or weakly
assessed blessing briefly. A sufficiently sampled favorable *relative* score
can extend that interval, and only separately scored reviews by distinct
actors with explicitly disjoint source groups extend it further, within a cap.
Score, coverage, review count, and due time remain separate signals; none is a
truth verdict. The existing full POI report and binary standing remain intact.
The product commit is `e419920`; 63 focused and 155 configured Python tests
passed.
<!-- tarav.breadcrumb d2354eb4a3b6665325f7580368a4850b862e520756f3f87e59528fbc112977ec -->
<!-- tarav.breadcrumb 751d3074eb14ff66b15620e9c9e3d339752a020789def2d6dcd7bc98c5972453 -->

## Tracked POIs, the board, and attention

From the g70203 redesign discussion; see also [Decisions](decisions.md).

"Attention" names the workflow, or workflows, that rank and sort POIs. Many
words mean nearly the same thing with different nuances; naming will settle
with time.
<!-- tarav.breadcrumb 55af6d704daecce1aedebfbed879df5c70f4e6c2121dad93fd2b0adafd552259 -->

The engine produces POIs, events we record. Recorded POIs are like GitHub
issues: explicit, and they need resolving — closed, ignored, and so on. Some
are not under agent control (a check ran and failed); others are introduced by
the agent. A board, like GitHub's, lets agents and any workflow see and filter
POIs, for example the unresolved POIs of their own workflow. Blessings and
other decisions attach to recorded POIs. A system that generates POIs and
prompts the agent to resolve them is already a driving force; with evaluation
and automatic scoring it starts to run by itself, as md-library begins to.
<!-- tarav.breadcrumb cb2ffc8a73a7a6d61faddbb55a13585b27e25ea0277acafbc341b96f2f09be24 -->

Not every POI is recorded; that is the workflow implementer's choice. Some are
just notifications, for instance in the command line, and still use the POI
system for contextualization, Diagram integration, and knowing which checker
produced them. "Issue" was a candidate name for the recorded ones but
suggests something wrong. The agent proposed **tracked POI** (tracking as a
property, not a new noun) and the User chose it.
<!-- tarav.breadcrumb 0ebb27abb363a0581d03a19a36113c454a35ae0ef4a67ecb713a1316f92a44da -->
<!-- tarav.breadcrumb aba381da3ffc2a7c7eb8a774f5082103b98c9aadc4ba7b770bd7350c702903c7 -->

POIs are typed and can express any axes we need. `CheckPOI` forces a companion
Check class, so it is clear which check failed; `NotificationPOI` is raised
text. Both share the common POI features, and more types will come as new
functionality is discovered. Being tracked is a separate axis from these
types.
<!-- tarav.breadcrumb 8b3336827f9fbccf388c9f401345f53a11cb8da238a5e592047801db4967c302 -->

### First tracking and board slice

Request 854 added optional `TrackedPOI` records at a caller-selected root.
An identified POI is tracked by its situation identity; completed evaluations
of its exact declared scope can update detection and history. Absence from an
incomplete run or another scope changes nothing. The pageable board filters by
workflow, type, detection, disposition, and subject. It may join Blessings and
other Decisions, but a Blessing never changes detection: a still-detected POI
remains visible. The initial disposition view distinguishes blessed from
unreviewed; broader attention policy is later work. See
`tarav-py/src/tarav/l1/poi/tracking.py`, `tarav-py/src/tarav/l2/poi/board.py`,
and `tarav-py/tests/decisions/`.
<!-- tarav.breadcrumb 2bb73a07d0cbaea4b24a0b1086e966016ff1235491737c85db59122fd81d5250 -->
<!-- tarav.breadcrumb b124ef563fb16387a160682d14c030280730d37f6d59a9de5be47ebbcbce7f28 -->

## Reported POIs and their context — 2026-10-08

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

While reviewing the bootstrap POIs, the full record of a POI was only reachable by writing a script. The User took this as evidence that any presentation of data must give the agent a clear way to escalate to full context, because an agent should not act on limited context, and that guards may be added later. The expansion should be central instead of implemented by each surface, and the connection should itself be checkable, so that its absence is a POI.
<!-- tarav.breadcrumb 2693f678cb96406b488dc5cc53479027f99300b4255c6dfdd009abbd3d37aa1c -->
<!-- tarav.breadcrumb d67600570d36441519e1991e0b3d43e999597368f8c8051c024474e629fec3d0 -->

The POI life cycle is: a POI is shown with its identifier and a short message, and the agent is told explicitly that before doing anything with any POI it must open its context, and how. That instruction is stated once per output, with the command, placeholders, an example and a pointer to help. Arguments are explicit key/value. The view is named for a POI that has been presented, not just "poi". The POIs currently reported on Tarav are not repaired; they are the test bench.
<!-- tarav.breadcrumb e56c308512a66e8d242577a0b1b3fac11b303d3924d0f17c42556ac0b1d4ee57 -->
<!-- tarav.breadcrumb 978b9c97f5aa6f5d3bfa9306221294af264b12c9ee4c888279e236133c1ad83d -->
<!-- tarav.breadcrumb 9a060f83b08b95d5c9facee5c47a36ce405333050e8ae0e9e6eed0ffae9f9d2c -->

Implemented in `tarav-py` commit `4289796`. `tarav check --project` retains what it reported under `~/.tarav/check-reports/`, and every report with POIs opens with the instruction and an example. `tarav context --id <poi-id> --view reported-poi` lists `poi-type`, `raised-by`, `finding`, `read-first` and `may-do`. A POI Type declares `read_first` and `may_do`; the seven bootstrap POI types do, as the worked example. Two checks run where the POI base Type is developed: a reminder for each POI Type without guidance (48 today, left in place) and a round trip from the advertised example to the view. The view name, the retention place and the omission of an earlier-actions entry were agent choices. [Impl.Req 876](../../../tarav-py/notes/live/876-context-command-and-reported-poi-impl-req.md) has the detail.
<!-- tarav.breadcrumb 9fa116eb350f3a3a90b076b7567658a1bd59ee8e6b02febdc20c72b2b484f1e0 -->

## Atomic POI types — 2026-10-08

Reading a reported POI through the context command, the User met a `code` field and asked what it was for. A search of the POI design sessions found no User turn asking for it: it came from the index linter of May 2026 as a rule label and was carried into the neutral POI base by request 832 without discussion. The User asked for it to be eliminated.
<!-- tarav.breadcrumb 26fb5d73cc1cdc44ff4aea293e14b29eaecc70a5a76317e4200892d2e926ddbf -->
<!-- tarav.breadcrumb a91da531e00ad680449290b95f80f10dcefc0375a26101cc77f0136b64d89bde -->

The decision: POIs are atomic. Each POI type describes one situation and there is no further degeneracy inside a type; the field was an inherited linter habit duplicating the type system.
<!-- tarav.breadcrumb c7aba3389e0880a5237de099536aae60c6ad587639957500693684c243042227 -->

A family parent that is never raised may remain so related cases can be selected together, because in Tarav the typing system expresses semantics. The base type loses the argument, every multi-case type is split into one class per case, checks stop copying the code into the situation, and reports group by type instead of code.
<!-- tarav.breadcrumb 0281a7a663e90194c0194f45cb95a56e229f5762b5d93baf76518e6c03d5e43c -->

[Impl.Req 877](../../../tarav-py/notes/live/877-atomic-poi-types-impl-req.md) implemented it in `tarav-py` commit `9559db7`: fourteen families became 88 case types, and `tarav check` lost `--by code` and `--code`. Three older finding classes that subclass the bare `POI` (`BreadcrumbFinding`, `ReferenceFinding`, the Diagram `Finding`) still carry a code and are a follow-up. Guidance reminders rose from 48 to 93 on the Taravangian root because each atomic type without guidance is now reported separately.
<!-- tarav.breadcrumb fe5f488b22795d4fa14c5101c5b0463306b0b85d6987f31c4efbce24d3dca7a2 -->

## Shared presentation and further POI integration — 2026-10-08

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

The User accepted a common presentation path: a POI Type supplies one POI's meaning, selection fixes the page before rendering, and a named renderer lays out that page and tells the agent how to open full context. Surfaces select a renderer by name; the default and JSON-lines presentations support line, record, and context levels. The connection from a displayed identifier to context is itself checked.
<!-- tarav.breadcrumb 943d1c7cf40bcfcb203dde81ffc3810e81d0210c1392557041410e3c3de58ca0 -->
<!-- tarav.breadcrumb a73e6a566f612a4d20cfef20187a9e1190ec77a266369fa95607a2bbf62f0016 -->

[Impl.Req 879](../../../tarav-py/notes/live/879-one-poi-system-and-rendering-impl-req.md) integrates `tarav check`, Skillware POI reports, and Breadcrumb audit output with that renderer contract. Breadcrumb and Reference resolution now use atomic identified POI families. A displayed identified POI is retained so its advertised `tarav context` path can open the reported occurrence. Chatlas query matches and low-level record observations were renamed as plain data, rather than treated as POIs. The Diagram's coded `Finding` remains: Capture Receipt records retain its `code` shape, so its conversion needs a separate typed-case and data-migration pass.
<!-- tarav.breadcrumb 4278a7af9829e72ff7774c1caa7f4fc27acbd1fdcd132bbf39a76d063f798f4c -->
<!-- tarav.breadcrumb 99eded3fcfc86cc66781292ca27db3a654925056a17116b1f10bb7d8d9404466 -->

## POI tracking: records with status axes — 2026-10-08

*Overtaken on 2026-10-09 and removed from the code by request 894: the
tracking record became an action. This section is history.*

This section replaces the mechanics of "Tracked POIs, the board, and attention"
above. That earlier text stays as the history of the first design.

The User decided that tracking is a capability and that every check POI is
tracked by default, because a check POI is defined by its situation. The
trackable class has a setting that can disable a particular instance. POI
tracking is its own workflow; the User does not love the name and kept it for
now.
<!-- tarav.breadcrumb 816354d3714ce24cfb00d547e35ca16a19c51a9f9847db2ffbd0f8416d0a3e57 -->

The check run is where tracking integrates. A run starts from the beginning,
so it gives the tracking system a new data point. It has to register the
positive sign, a POI was raised, and the negative sign: the owning check
finished and did not raise it, "the check passed". The User rejected the word
"board" for this: it is a record system that tracks the state of POIs.
<!-- tarav.breadcrumb 5fe3457a6a93fde37a08f10f8698b52288e8506318fde83bb4c02ceaaa2f8a5c -->

Status is a vector, not one value. "Passed" is one status on one axis and does
not prevent closing a POI or saying more about it. The store is a database of
every POI ever tracked, like the issues of a GitHub repository: records stay,
can be referenced, and can be discussed indefinitely.
<!-- tarav.breadcrumb d9ad9ba945523e1671e7155d7a6cc8ec24e0812bc503c6a9e1e075026f0630cd -->

Blessing is one of the axes. Workflows can add their own, several axes may
speak about related things, and that overlap is accepted on purpose. The aim
is a system flexible enough to express everything, to be formalized and
simplified later. The earlier tracking code was inspiration only and could be
redesigned from the ground up.
<!-- tarav.breadcrumb b5049e5e5d6a1192e58cdb01f0ad2d5f15ddaa68091a9c41f62a946502bcf572 -->
<!-- tarav.breadcrumb 75e6fd8732d1e841de3cf6d6bcc99405e56f358152bf724d7346e498cd18721c -->

### Implemented

[Impl.Req 883](../../../tarav-py/notes/live/883-poi-tracking-workflow-impl-req.md)
built this in `tarav-py`, commit `0d524e2`.

- `tarav.l1.poi_tracking` owns the workflow. `TrackablePOI` is the capability;
  `CheckPOI` extends it. One `TrackRecord` per POI identity is kept in a
  `TrackRecordStore`, and nothing deletes a record.
- A record holds the POI snapshot, the owning check with its identity, and
  `axes`. Each axis entry has its Type, owner workflow, value, the time since
  it holds, and its own history of changes with what made each one. The
  tracker stores and filters axes and does not interpret them. A workflow
  adds one by subtyping `TrackAxis`.
- `Check.identity` says which check this is across runs. A `SituationCheck`
  derives it from its Type and situation; a plain `Check` returns nothing
  unless it declares one.
- `CheckRun.track(into=tracker)` turns each `CheckResult` into one data point.
  A raised POI is `active`. A record whose owning check completed without
  raising it is `passed`. A check that did not complete, did not run, or has
  no identity gives no evidence, and the record reads `not-evaluated`.
- The blessing axis lives in `tarav.l2.blessings.tracking` and reads the
  unchanged blessing store. A read shows the current blessing without writing;
  the next observation puts the change into the axis history.
- A Project's records live in `.tarav/poi-tracking/`. `tarav check --project`
  writes them and `--tracking skip` leaves them alone. `tarav poi tracking list
  --project --axis observation=passed` filters, and `tarav context --id
  <poi-id> --view tracked-poi` opens one record.
- Tests: `tests/test_poi_tracking.py`, 10 tests; the suite passed 232 tests in
  the shared worktree and 222 on the exact commit tree, and Ruff passed.
<!-- tarav.breadcrumb 48116b70313445e807f3d6f75557e59cc7c304c85ac70eef6960481a3383b24a -->

### What the first real run showed

Two runs of `tarav check --project` on the root wrote 149 records for 151
reported POIs. Only 14 of them belong to a check that states an identity
(`Tarav.SKW.Check.ContextFreshness`). The other 135 come from four checks
without one, so they can never read `passed`; when one stops being raised it
will read `not-evaluated`. Giving those checks an identity is follow-up work.

### Agent choices and open questions

These were chosen by the agent, not decided by the User.

- The per-instance switch works only for a POI Type that lists `TrackablePOI`
  in `settings_include`, because the settings capability includes a parent's
  settings only explicitly.
- The record stores the last-active and last-evaluated times, so every check
  run rewrites every evaluated record. In a Project under Git that leaves the
  tree modified after each check.
- The store is inside the Project, and a child Project checked through its
  root is tracked in the root's store.
- The machine-local check-report cache stays. It holds what a surface last
  showed; the tracking store is durable Project state.

Left for later: a manual disposition axis, a discussion thread on a record,
links between records, a scoring axis, notifications when axes disagree, and
retirement rules.

### Record status changes only — 2026-10-08

The User rejected the rewrite on every run. Repeating a check whose POIs did
not change must not touch the store: tracking records changes of state, not a
refreshed timestamp, and it is append-only. A record keeps the moment each
change was detected; the latest entry is the last change, not the latest run.
<!-- tarav.breadcrumb 13aaea0e57f140884ec9d262cb9d7363f1b15e4027d449899ebb61b3659d3860 -->

The User also asked to keep it simple, with zero smartness in the code and no
event system. The tracker builds one explicit object per POI describing its
current tracking situation, the status it assigns, in the same way a check
declares a situation for POI identity. It hashes that object and compares the
hash with the last recorded one. Equal hashes write nothing; a different hash
appends one entry. The hashed object is stored beside its hash, so what was
hashed stays explicit.
<!-- tarav.breadcrumb d43f415e15e15cb3b2bd599a8ea5b6623b58446e94a732588c5ec2fe353f2127 -->

Agent reading of the 883 code, not yet decided or built: the rewrite comes
from the `last_active_at` and `last_evaluated_at` times, which would go; the
per-axis histories would become one list of entries per record; the POI copy
in a record would be refreshed only when an entry is appended, so a changed
count in a message alone changes nothing. Blessing stays an axis inside the
situation, so a new blessing enters the record at the next check run.
## Diagram POIs and retained Drafts

The Diagram now raises atomic identified POIs. Its 81 concrete cases sit under twelve
family Types and the shared `Tarav.Diagram.POI` parent. Each case's Type and path
define identity; the message and evidence explain the current observation.
The family Types are grouping points and cannot be raised. Capture Receipts and
Diagram command JSON retain `pois` with `type`, `path`, and `message` per row.
Commands use the shared POI renderer and retain displayed POIs for Context.
<!-- tarav.breadcrumb 067092b81400cc8b761a64dae4f2abaf10d8484cab766e9af8cc7591e84bbd12 -->
<!-- tarav.breadcrumb 2666bd852678b24d93732c2bca25c9a3b556e3c9209848ca7866ac2cde6eb948 -->
<!-- tarav.breadcrumb 434a6263ff7817a24cd10326c40dd3800ce7589e00bdb0c31ca8dedb48f2c7a4 -->

Draft schema 2 holds those typed receipt rows. The explicit
`tarav diagram draft migrate --to 2` operation maps version-1 rows; the reader
does not translate them. Before migration, 53 Drafts held 13,347 coded rows in
50 receipts. A dated sibling backup was made, the migration reported no unmapped
rows, and all 53 Drafts and 13,347 rehydrated POIs loaded afterward. See
[Impl.Req 881](../../../tarav-py/notes/live/881-diagram-poi-atomic-types-impl-req.md).
<!-- tarav.breadcrumb 7999d9e48b0db92fcbd33b00ff26858facb673bfa7890518309bbbbb9ed50e66 -->

## Check report filtering and batch Breadcrumb audits

<!-- tarav.sessions
473c89a0 = codex:01a1176b-f14c-7fd0-a97c-b22279c3f8c8 @473c89a00e2367fb827193af74a6375c60a96b0be110f21df0aff49360ca972f
-->

`tarav check --type NAME` selects POIs whose Type is `NAME` or descends from
it. The report states how many POIs matched out of the full run; filtering
changes presentation, while tracking, retention, and the command's exit status
still reflect the entire run. `--check` remains a report filter by exact Check
Type name. Group pagination applies after selection.
<!-- tarav.breadcrumb 6bf9b64281e5913e114d30348e2d396b44c263ffae742a2810c2dd034d2f52e0 -->

`tarav breadcrumbs audit chatlas-context` accepts repeated `--surface` paths
or `--files-from` with one path per line. The command audits each selected file,
returns a result for each, and can refresh uniquely located stale positions in
one pass. A missing file is reported beside successful files. The manifest
mechanic does not choose which User Turns are relevant to a surface; that
judgment remains with the agent. See [Impl.Req 884](../../../tarav-py/notes/live/884-check-poi-filter-and-breadcrumb-batch-audit-impl-req.md).
<!-- tarav.breadcrumb 94da2d7f8b1ff38498e670c267c7b0fb9809f2bd993f80e5122894754e21e55f -->

## Diagram POI completion

Request 881's follow-up covered the twelve Diagram POI families through their
emitting methods. The separate `tarav diagram render` content command now
retains its typed POIs and displays them through the shared POI renderer. Its
`--renderer` still selects Diagram content; `--poi-renderer` and `--level`
select POI presentation. The command's JSON output retains typed POI rows.
The retained Draft migration remained intact: 53 version-2 Drafts and 13,347
typed receipt POIs, with no coded rows. [Impl.Req 881](../../../tarav-py/notes/live/881-diagram-poi-atomic-types-impl-req.md)
records the verification and the existing Project and Skillware POIs that are
outside its repair scope.
<!-- tarav.breadcrumb 256e980bf25b4e0264b31cadd62f99e08b0df54666a047eb8530e9f236955e5a -->

## Neutral POIs and the producer–reader gap — 2026-10-09

An open design discussion; nothing here is implemented. The full thread is in
[Operator Context, Directives and Harnessed Actions](operator-context.md).

The User looked for first-principle arguments for the current POI design,
compared with Python's exception system.
<!-- tarav.breadcrumb 0def7e3aa8e7057e0917313ff8471bfbec14a16870f7905b3d9a75eba25f4cc4 -->

A POI connects above all to the code and the situation that produced it. It
narrows the gap between producer and reader, making the producer's intention
clear so the reader can judge. The producer cannot know the reader's goal and
the design does not pretend to.
<!-- tarav.breadcrumb c2b80891fb46668c0319a8d44122fa11f204fda2cd05a0b4ce327534bf2aa454 -->

Directions the User set:

- A general `.throw()` on POIs, raising the POI as an exception that carries
  the whole POI. Today only `CheckPOI.error()` does this
  (`tarav-py/src/tarav/l1/checks/__init__.py`), through `POIError`.
<!-- tarav.breadcrumb 2e42c09421a1a80109cecfc9c8d93f11005a9418bf55fc1ae50a6811e38360fc -->
<!-- tarav.breadcrumb f1457b7d3440906dae02124887d21afd9aa6b420021ee635467f07bb5e72dee4 -->
- POI wording is descriptive, not imperative (`Workflow.Neutral`). "What to
  do" belongs to the skill that contextualizes the agent, not to the POI.
<!-- tarav.breadcrumb 19846c92b781118e4eaab53e3f1265465912fde6b5b59ed31b1f41581c9e1855 -->
<!-- tarav.breadcrumb 09c8c5868c097b3e1e11867078f5659df9e00fb50d2e1fbd6b289d702224d30c -->
- `may_do` moves out of the POI. It was first to become part of the context;
  later in the day its home became the POI's action and that action's skill.
  The POI is concerned with the triggered check and the situation. Precedent is another
  contextualization workflow, and a skill can prime the agent on what to look
  for, even with its own typed Context view.
<!-- tarav.breadcrumb 0f6799fa762b75d065cf2d563c634f8ac882a55747c385dfe7b18e9e5e5518a1 -->
- Candidates, not decided: a typed Message that models guidance instead of
  the POI; typed subjects beside the situation, so precedent on similar
  subjects can be found.
<!-- tarav.breadcrumb 330361530e4c21f30aaa19131c2e611d4c35ffe96c67b2772069e1c13b0f4910 -->
<!-- tarav.breadcrumb 5c5fefb93f6588fe9c4ae77bd817fef5ca65460fe614d3535bf3bf4c534bc075 -->
- Weak situations are found by maintenance while processing POIs.
<!-- tarav.breadcrumb d749600056e2146395498f387e4bdd5fd8edf7b15a60475d2004d0121ee2c928 -->

The User was unsure what it means for a check to have no identity, and whether
some POIs are ill-typed and should be CheckPOIs. In code a Check's `identity`
says which check this is across runs; `Check` returns `None` and
`SituationCheck` derives it from its Type and situation. Agent reading, not
decided: the identity-less checks are debt to convert explicitly, not a
meaning to preserve.
<!-- tarav.breadcrumb 89514a83ccf70085e11e9a67ca33baf41aca603e922cf58282d8c449f4cd7668 -->

Agent's comparison with exceptions, as discussed: both let the class be the
kind and carry no severity; POIs differ in that they do not interrupt, outlive
the process and therefore need an identity kept apart from description, have
an attributed acceptance, and make absence meaningful only when the check ran
completely.

Request 889 built the first of these directions on 2026-10-09: every POI has
`throw()`, which raises `POIError` carrying the POI
(`tarav-py/src/tarav/l1/poi/primitives.py`). `CheckPOI.error()` was removed in
its favour, so the `.error()` named in [Checks workflow](checks-workflow.md)
is the earlier name.
<!-- tarav.breadcrumb 3d95d861eb7d695f4e7c4eef0e26fdcd4d4954da167fadd1c2abc6046b4d288a -->

## A POI is an event; what follows it is an action — 2026-10-09

A later turn of the same day's discussion. It replaces the idea, held for a
few minutes, that a POI declares its own resolutions, and it changes what a
tracked POI is. Nothing here is implemented. The Actions it builds on are in
[Operator Context, Directives and Harnessed Actions](operator-context.md).

### What a blessing means

Reviewing the first Actions example, the User asked what blessing a POI such
as "this file has a TODO" means: that it is done, that it is not really a
TODO, that it is recorded elsewhere? A blessing answers a specific question,
and the types should carry that semantic.
<!-- tarav.breadcrumb 264fa41857a6f3a80df2d18e49bfd4d89a60810bae04630c03d262999f78b67e -->

The same POI can be blessed by different kinds of blessing. What makes
something a blessing is that the POI's claim is attenuated or dismissed; its
original nature is an overrule of the check. It is not the only relationship
one can have with a POI: a POI may be annotated, or may ask for something to
be provided.
<!-- tarav.breadcrumb 302d002af40f552fb2a6ae859a6f26c511d8f578f082226a96fd7aeb30e23038 -->

The general frame is that a POI can be resolved, in several typed ways:
because the situation was changed, because something the POI asks for was
done, or because it was dismissed, which is the softest. Dismissal has grades,
from no justification to a reason that must score well. The word "blessing"
may not survive.
<!-- tarav.breadcrumb 4475d3796feda6a3de78bcfe919c74db6e83c077c38decb3310f2152fc48c72f -->

### The POI is only the event

Too much responsibility was being put on the POI. A POI is the event that a
situation happened and was raised. It can have consequences: it can activate
an action. A blessing is a way to finish that action.
<!-- tarav.breadcrumb 6c821818375582933e70f7c47a768214ebdcdbab98db543e0924040c1c1cbbde -->

What used to be a tracked POI is not a POI: it is an action triggered when the
POI is first raised, closed automatically when a later check no longer raises
it. An action can have more than one close path, as a program has; dismissal
is one. The design starts from scratch and need not keep earlier names. The
guidance about what to do lives with the action and its skill, not in the POI.
<!-- tarav.breadcrumb 58bd0fd530f8dc452be8474969267ab066dddd4e439e93e6ce45ce4f42f1bab9 -->

One action per POI, for simplicity. Other workflows may hook their own,
independent actions from outside when a kind of POI is raised, and an action
may close when another closes, as a chain.
<!-- tarav.breadcrumb a2447cd89c1e47729ab0d3096353506c33b1890828c6b642d04313b37af27592 -->

The name for now is an actionable POI: a POI that also spins an action.
Everything stays typed: situation, check, check POI, action. What is
happening in a Project is asked as "which actions are active?". Closing is
done by a loop that belongs to the Actions workflow: it asks each running
action whether one of its close paths is met, and closes it if so. That is
simpler than hooking into the checks.
<!-- tarav.breadcrumb 2e49cb0920a57e6c4d4e044d2fa4621c81825e0fd9261dc3f11b154ebaeb8179 -->

Agent proposals, not decided: keep the close path visible wherever runs are
listed, so a dismissal never looks like a fix; a dismissed POI that is still
raised does not reopen its run while its situation is unchanged; a situation
that returns after it was gone opens a new run; other workflows' extra
actions come from an explicit list consulted when a run opens, and
dependencies between actions are checks that read run states, so no event
system is needed.

### What was built from it — 2026-10-09

The User asked for the requests to be prepared and executed.
<!-- tarav.breadcrumb 1bf2b756ce759ada01608d441210978f80e293f842fac10408d8fd4d9222ea02 -->

- [892](../../../tarav-py/notes/live/892-actionable-pois-and-resolution-action-impl-req.md):
  exits on Step actions; the POI resolution action; `Check.subject_key`,
  `Check.clear()` and `ClearPOI`. The instance of a POI's action is derived
  from the POI's identity, and reopening shows in the registry's Git history.
- [893](../../../tarav-py/notes/live/893-elementary-pois-guidance-to-context-impl-req.md):
  `POI.context_notes`; the guidance check is gone, which took the root
  Project from about 190 reported POIs to 54.
- [894](../../../tarav-py/notes/live/894-project-pois-on-actions-impl-req.md):
  `CheckPOI` is actionable; `tarav check --project --actions write|skip`;
  `tarav action list --project`; `tarav context --id <poi id> --view poi-action`;
  tracking removed. On the root Project 52 actions opened, and after the
  agents file was compiled from its source the action of its drift POI closed
  as `gone` with the signal printed.
- [895](../../../tarav-py/notes/live/895-dismissal-replaces-blessings-impl-req.md),
  first part: `DismissablePOI`; dismissal refused where the Type does not
  allow it; a dismissed finding counts as settled.

Agent choices made while building, not decided by the User: a check's stable
key is called `subject_key`, because checks already use an attribute named
`subject`; the caller passes the completed checks to the Actions workflow, and
no clear POI is synthesized for every check; in a whole run a check Type that
can name neither a subject nor an identity closes its absent actions; no real
check declares a subject key yet; the blessing code was not removed.

