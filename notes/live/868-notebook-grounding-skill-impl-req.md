# Hugentics Notebook grounding

<!-- tarav.sessions
0f5bad01 = codex:01a15483-94e8-7fe0-86ad-ddd83e2bae52 @0f5bad0131260477b4cf3d712a95871496c3db92d67eaa7910243e312f7b552a
-->

## Impl.Abstract

Restore `tarav-hugentics --ground --notebook [HINT]` for finding Blocks about
the current conversation. Infer the Project and collect its full Model subtree
through Context by default. HINT narrows the task; it is not a required exact
Block name. This is agent-operated, read-only contextualization.
<!-- tarav.breadcrumb 704d98e2c493 -->
<!-- tarav.breadcrumb 48196a761432 -->
<!-- tarav.breadcrumb 8fc5da040170 -->

Knowledge.Surface: wiki
Alignment.Mode: Interactive
Status: ready; depends on [Python request 933](../../../tarav-py/notes/live/933-notebook-context-grounding-impl-req.md).

## Design

The skill infers the active Project from task context and cwd, uses the new
Notebook CLI to inspect the Model map, and constructs SPARQL queries from the
conversation and optional hint. It reads selected Blocks and their ancestors,
compares them with the current discussion, and returns useful Ships, context,
tensions and gaps. Relevance and sufficiency remain agent judgments. Types,
Line wording and structural relationships provide lookup clues without adding
a name/topic field. Discussion and Archive require deliberate expansion with
their meaning retained; their presence does not establish current truth.
<!-- tarav.breadcrumb 0c64fb9d5c8d -->

The module gives concrete runnable CLI/Query examples and explains the Lines
IRI vocabulary and full Model collection. It creates no Notebook, capture,
Breadcrumbs, session View or Project state when invoked. Missing or empty
coverage is reported rather than repaired. The retired Model-backed
implementation/capture routes remain parked; ModelBlock here is the new typed
Notebook Block. Bare --ground selects this Notebook route; --notebook makes
that backend explicit. Other workflow combinations are rejected rather than
implicitly authorizing writes.

Keep exact command spellings aligned with Python request 933. Edit authoritative
SKW JSON sources, add the module to main/loading declarations, record tracked
generation for changed sources and compile/deploy the skill. Do not restore
the old Index authority ladder or Diagram.View mechanics from the Attic/Git.

## Impl.Req.Wiki

Product and Wiki owner: tarav-md. Relevant Notes: line-notebook.md,
context-graph.md and lines-workflow.md. The older Grounding module removed at
55387ff and the Attic Index.Search module informed discovery only. The current
User decisions above define this reimplementation. Capture in the Notebook
topic and mandatory daily Note with exact supporting User Turns.

## Execution.Plan

1. Feature: add ground.skw.json, routing and command surface, main/loading
   declarations. Compile, run skill loading/source/reading checks, and use
   CLI help/examples from the installed Python implementation as evidence.
2. Feature verification: perform a bounded read-only grounding rehearsal on
   this Project's current Model, report its actual coverage without seeding
   data, confirm deployed skill contains the new module, and close Wiki plus
   scoped implementation evidence.

## Impl.Log

- Todo: capture/cold-reload; start checkpoint; wait for Python 933; edit SKW
  sources; generation/compile/check/deploy; rehearse; Wiki capture and closure.
- Existing Diagram design source/product and skill locks are external work;
  checkpoint them as found, preserve their meanings, and avoid unrelated edits.
