# Notebook capture skill and writing guidance

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## Impl.Abstract

Implement tarav-hugentics --capture --notebook, targeting the inferred Project's
ModelBlock by default, with explicit Project/branch/Block selectors. Recover
the legacy interactive capture loop and Kernel Writing guidance, integrating
the current Notebook support/review APIs. Design the request, then execute it.
<!-- tarav.context 0f5bad01:ed97fca951f83f57 -->

Knowledge.Surface: wiki
Alignment.Mode: Interactive
Status: ready

## Design

Target context drives preparation. Infer the Project from the foreground
discussion and work, not the skill's repository. Default to its Notebook Model
subtree; --project, --branch or --block selects another target. Read the target
map and useful Blocks, siblings and ancestor context through current Notebook
Context tooling before proposing changes. Explicit capture can initialize a
missing Project Notebook through its existing create() API and report the
seeded root; audit must not create anything.
<!-- tarav.context 0f5bad01:0b6f920b7868f147 -->

Maintain focus and mode independently. Contextualize, map candidate captures,
offer a compact roadmap, then work on one Block or coherent cluster. Discuss
freely; ::discuss is sticky until ::review. Review shows exact wording and
before/after changes, their actual target and Types, and a fresh token. The
User's ::approve TOKEN accepts that presented proposal without writing it.
Approved changes accumulate while focus advances. ::land and
::land-all-approved write only approved changes; neither supplies approval.
Changed wording, Type, destination, operation or semantic context requires a
fresh token. Natural conversation may redirect or revise any current focus.
<!-- tarav.context 0f5bad01:4884e333f0d4a0eb -->
<!-- tarav.context 0f5bad01:3501f527bcf950c4 -->

Add a focused writing reference loaded by Notebook capture: one contribution
per Line, orthogonality relative to sibling Lines, direct wording, preserve
important qualifications/User judgments, coverage over compression, useful
future signal, and sufficient meaning within the Block/ancestor context.
Include positive/negative worked examples and a short pre-proposal checklist.
Recover the craft, not obsolete concept-only Blocks, compulsory headings,
fixed sections, line caps, order independence, or Markdown storage rules.
<!-- tarav.context 0f5bad01:f109f50a7381a0c5 -->

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

1. **Pending — Feature dependency.** Execute Python request 939. Check its
   public staging/landing behavior before writing API guidance.
2. **Pending — Skill feature.** Add notebook-capture and kernel-writing
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
