# POI visibility, navigation, and blessings

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
1f561f5d = codex:01a0b984-4664-7871-934a-89cf92595b64 @1f561f5d8db849a3a445b83a91a5e94acbb80927f9c332d45322ac70f8705a74
1ae20f8c = codex:01a0ff32-0ec2-7b72-8850-fa795135f3c9 @1ae20f8c8159f12d2402ea702cf49c876ec46a72f71ce12423ae1dbdf2a91871
64298cbc = claude-code:9da4cef5-68b7-4d17-8a06-1351ca51e82f @64298cbc8db2e7aa971e0828653c07bcb483cfed40931fdf87d5abe7ce1c60b3
-->

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
