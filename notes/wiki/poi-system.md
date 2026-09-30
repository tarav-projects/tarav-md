# POI visibility, navigation, and blessings

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
5626cd5f = codex:01a0af61-72e2-7bd2-94a3-26529d6914ec @5626cd5f7db74c4f2e3838250516b5e300cc9387ac254eb65a0816a5f30555a1
-->

## Detection and presentation

### Points of interest, not inherently problems

A POI is a claim that something is of interest. It does not inherently imply
negativity, failure, or a required corrective action. This clarification
broadens the problem-oriented examples elsewhere in this note.
<!-- tarav.breadcrumb 8abe33d8f10332db0c5b33fc46c2b5db5158b467244a25704e3185c81fe780f3 -->

The proposed base POI has two specializations: `CheckPOI`, coupled to a Check
class that explains the check, and `NotificationPOI`, reporting an event or
operation worth making visible without requiring a Check. In Breadcrumb
auditing, a stale position is the first case; appending a location observation
is the second. `NotificationPOI` is the selected name, replacing the tentative
`LogPOI`. This is design direction, not a claim that the migration has landed.
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
