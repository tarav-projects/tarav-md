# Notebook capture skill and writing guidance

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## Impl.Abstract

Implement tarav-hugentics --capture --notebook, targeting the inferred Project's
ModelBlock by default, with explicit Project/branch/Block selectors. Recover
the legacy interactive capture loop and Kernel Writing guidance, integrating
the current Notebook support/review APIs. Design the request, then execute it.
<!-- tarav.breadcrumb 5c284d942fb0 -->

Knowledge.Surface: wiki
Alignment.Mode: Interactive
Status: executing

## Design

Target context drives preparation. Infer the Project from the foreground
discussion and work, not the skill's repository. Default to its Notebook Model
subtree; --project, --branch or --block selects another target. Read the target
map and useful Blocks, siblings and ancestor context through current Notebook
Context tooling before proposing changes. Explicit capture can initialize a
missing Project Notebook through its existing create() API and report the
seeded root; audit must not create anything.
<!-- tarav.breadcrumb 4d162c7633a3 -->

Maintain focus and mode independently. Contextualize, map candidate captures,
offer a compact roadmap, then work on one Block or coherent cluster. Discuss
freely; ::discuss is sticky until ::review. Review shows exact wording and
before/after changes, their actual target and Types, and a fresh token. The
User's ::approve TOKEN accepts that presented proposal without writing it.
Approved changes accumulate while focus advances. ::land and
::land-all-approved write only approved changes; neither supplies approval.
Changed wording, Type, destination, operation or semantic context requires a
fresh token. Natural conversation may redirect or revise any current focus.
<!-- tarav.breadcrumb 92b559b75c24 -->
<!-- tarav.breadcrumb 6f0873b29d81 -->

Add a focused writing reference loaded by Notebook capture: one contribution
per Line, orthogonality relative to sibling Lines, direct wording, preserve
important qualifications/User judgments, coverage over compression, useful
future signal, and sufficient meaning within the Block/ancestor context.
Include positive/negative worked examples and a short pre-proposal checklist.
Recover the craft, not obsolete concept-only Blocks, compulsory headings,
fixed sections, line caps, order independence, or Markdown storage rules.
<!-- tarav.breadcrumb 57ad74992fdc -->

Python staging comes from [request 939](../../../tarav-py/notes/live/939-notebook-reviewed-capture-impl-req.md).
The skill is an agent-operated procedure, not a hidden agent runner. Teach the
real API and a bounded example: stage, render exact proposal, preserve a
temporary plan, obtain actual Chatlas references, restore and land after the
separate User command. Every captured Line needs substantive User-rooted
support; review evidence remains independent. Missing evidence is a reported
check finding, never permission to invent a turn or a passing score.

--capture --notebook --audit is mapping only. --auto/--unreviewed retains the
existing one-trigger unreviewed meaning where the chosen target Type permits
that route, using existing Notebook capture/support APIs and no fake review.
Do not weaken a reviewed destination to force that path. Bare legacy --capture
is not silently redirected in this change; its Diagram backend stays distinct
and is explicitly unavailable. Preserve Wiki/inline/implementation routing.

## Impl.Req.Wiki

Product/documentation owner tarav-md. Wiki: notes/wiki/line-notebook.md and
notes/wiki/daily/2026-10-20.md. Skill products are generated from
.tarav/skillware/skills/tarav-hugentics/src. Read that depot's AGENTS.md;
update retained sources, main.json and declared loading graph, then compile.
Legacy sources: Attic tarav-skills-reboot capture.md, Kernel.Writing in
tarav-pkg/design/102-design.md, index-block-catalog.md, and Git 90d6d2b's
hugentics-designer/references/writing-craft.md. They are evidence, not live
dependencies or instructions to restore old mechanics.

## Execution.Plan

1. **Verified — Feature dependency.** Execute Python request 939. Check its
   public staging/landing behavior before writing API guidance.
2. **Verified — Skill feature.** Add notebook-capture and kernel-writing
   modules and their SKW sources. Extend route/flag help, declared reading
   links, loading graph and package files; compile and validate the actual
   consumer artifact. Keep the entrypoint compact and conditional references
   discoverable. Test the documented recipe against isolated data, not the
   user's live Model. Remove no unrelated routes.
3. **Pending — Closure.** Validate skill packaging/deployment, source lint,
   links and installed artifacts; run relevant Project checks. Capture new
   Breadcrumbs, topic/daily Wiki and evidence commits, reporting older
   unavailable sources rather than retargeting them.

## Impl.Log

- Located both old capture generations and the writing-craft module. Confirmed
  current installed tarav has Notebook read commands and no Diagram CLI.
- Phase: Develop; Wiki context; Interactive alignment. The User explicitly
  authorized execution after design, so no additional implementation approval
  is required. No live Model capture is authorized by building this feature.
- Cold-read both requests. Start checkpoints: Python
  ca3cb1a8fd9698623443dec7e80a7fc184986c4d, Markdown
  c22cad08abdad997211890e1cc3705a9ae0fbb0e. They retain concurrent work as found.
  Staging, restoration, approval, evidence and architecture passed 79 focused
  tests before the skill API guidance was written. The existing fixed-Type
  storage contract is retained; the new capture path does not migrate archive
  Lines to evidence-capable Types.
- Added the Notebook capture and Kernel Writing modules through retained SKW
  sources; package files, loading nodes and declared reading links include them.
  Router help exposes --capture --notebook with Project/branch/Block scope;
  Wiki/inline/implementation remain separate. The legacy capture module now
  states its retired Diagram runtime is unavailable and stops before commands.
- The compiled guide's two Python snippets were executed as written against an
  isolated Project using actual NotebookDraft, support and review mechanics.
  Staging left the Line absent; restore/land produced the exact wording with
  valid support and review. This is mechanical recipe verification using a
  fixed Normal Model evidence fixture, not a real User review or a live capture.
- Skill validation passes. Build and isolated deploy completed artifact creation
  but return findings for 54 generation issues (51 stale
  contexts, 3 changed outputs), versus 55 before this change. No new source,
  dependency, loading, reading-path or link class findings appear. New and
  changed source blocks record the performed generation. Routing was prepared
  again after its dependent source content settled because its first generation
  correctly rejected a changed context; no failed generation was called passing.
- Deployed copy: /tmp/notebook-capture-deploy-20261020/tarav-hugentics. Its router,
  new modules and skill UUID match the products byte for byte. The active global
  depot already symlinks this maintained skill, so it exposes the new route.
  Consumer Markdown Breadcrumb positions were refreshed after compilation;
  source/metadata JSON has no registered inline convention, so the labels remain
  in the authoritative generated content instead of invented JSON comments.
- Final full root status: 1,298 completed checks, zero incomplete, 58 completed
  test-file runs with no test POIs, 67 total findings. Two neighboring Issue
  source contexts became newly stale after capture guidance changed; their
  actions were opened through Context (74fc8d68-2f01-2915-37f9-854550dd82aa and
  1f5c5807-393e-a562-b844-c3d35b2fccc3). They remain explicit maintenance
  findings; this pass does not claim Issue workflow reconciliation. Other
  context/output findings predate this work.
- Router, Notebook capture and Kernel Writing Markdown audits now pass. The
  initial audit still resolved the temporary drafting files, which retained the
  same labels. Renamed those task-owned draft copies out of their observed
  locations, then the normal refresh recorded each compiled product's unique
  position. No evidence attachment was replaced or source Turn fabricated.
