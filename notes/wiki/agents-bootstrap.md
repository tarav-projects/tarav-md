# Agents bootstrap

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## Purpose

Bootstrap here is the minimal, operating-system-loading level of contextualization: what must be in place in a Project so that an arriving agent can hook into the harness even when it has nothing else. The first entry point is the agents file, because agent harnesses already load it. Tarav should integrate with those industry-standard interfaces, the agents file and the skill system, rather than replace them.
<!-- tarav.breadcrumb e000c8302098 -->

Redundancy is intended. No single contextualization workflow has to be perfect; several stacked workflows are what make the system robust.
<!-- tarav.breadcrumb a877553bedfa -->
<!-- tarav.breadcrumb c1d2d42629ac -->

## Tarav System Prompt

The Tarav System Prompt is a section that every Project's agents file must contain. It is constitutive: identical across Projects, so there is homogeneity. It is not a short pointer. One to two pages are acceptable, because always-loaded context that explains core Tarav and how to get more context saves more than it costs.
<!-- tarav.breadcrumb e0cad8ed5b0c -->

Its text lives in the Tarav code base and is maintained like any other code; the wording is expected to change as Tarav improves. The mechanics are deliberately small: a document and a check. When a Project's copy is missing or not identical, a POI points to the command or source file where the current text can be found.
<!-- tarav.breadcrumb 8b741022aa37 -->

## Project System Prompt

The same mechanics apply one level down. After bootstrapping into Tarav, the agent needs to bootstrap into the Project, so each Project defines its own system prompt and a Project without one has a POI. Tarav does not prescribe what Projects add beyond that.
<!-- tarav.breadcrumb 83192095c38f -->
<!-- tarav.breadcrumb 97d4fce9a7af -->

Every Project carries both prompts, child Projects included. A Project can disable the requirement explicitly in its configuration; otherwise a missing or stale prompt is reported.
<!-- tarav.breadcrumb 5e11963a1fec -->

## The agents file under Skillware

The whole agents file is under Tarav control. It is developed with Skillware like a skill, with blocks, annotations and dependencies, and its source sits in a skillware folder inside the Project's `.tarav/` folder.
<!-- tarav.breadcrumb 4af507948a51 -->

Skillware is the only path. The bootstrap concerns the arriving agent, which only reads the file. Maintaining it is work for an agent that already has Tarav context, with the User in the loop, and a POI may ask for the matter to be raised to the User.
<!-- tarav.breadcrumb aeb65baed418 -->

A Project may declare several agents files, but only one arrangement is accepted: one main file under Skillware control, and every other file a symlink to it.
<!-- tarav.breadcrumb 2c15b8fc849e -->

## Project access and checks

The agents file is a property of the Project. It is a class object built on Skillware primitives, reached through a `project.agents` namespace that will hold more over time, under an explicit agents-file name. The Project can be asked for its path and source, and the file has its own checks.
<!-- tarav.breadcrumb 92e5b7527dd9 -->
<!-- tarav.breadcrumb 89b2b791edd7 -->
<!-- tarav.breadcrumb 7ac5b9eea838 -->
<!-- tarav.breadcrumb 007156807257 -->

Findings are typed check POIs produced by the existing Check machinery, and the agents checks are part of the general Project checks, so `tarav check --project` runs them. Further checks, such as alias equivalence, can be added in the same place.
<!-- tarav.breadcrumb 3b88fa399d5f -->
<!-- tarav.breadcrumb 2c07046416d6 -->

## Implementation

[Impl.Req 872](../../../tarav-py/notes/live/872-project-agents-bootstrap-impl-req.md) delivered the first implementation in `tarav-py`: `TaravProject` exposes `project.agents.agents_md`; a code-owned [Tarav prompt](../../../tarav-py/src/tarav/l1/project/tarav-system-prompt.md) and Project-authored prompt compile from `.tarav/skillware/src/AGENTS.skw.json`; built-in checks report typed POIs for missing or stale sections, product drift, and invalid aliases. The User approved landing the first prompt draft in the [daily record](daily/2026-10-08.md#project-agents-bootstrap-draft-landed). Separate default-on prompt switches are an agent implementation choice, not a separately recorded User design decision.
<!-- tarav.breadcrumb 0f7a73e0c6bc -->

## Skill availability

Skills are the second bootstrap entry point. A Tarav Project is the Tarav version of the folder-rooted project that agent harnesses already use, so the Project should know which skills an agent started in its folder would have, and check that the required ones are available.
<!-- tarav.breadcrumb 64fdf1a03d75 -->

Two skills are required. The Tarav package skill is the documentation system behind the short bootstrap text; its name is fixed in Tarav code because the check ships with Tarav. The Project package skill is the entry point to the skill part of a Project; each Project names it in its configuration. It need not be developed in the Project, and several Projects may name the same skill, as `tarav-py` and `tarav-md` both name the Tarav package skill.
<!-- tarav.breadcrumb 95e8c7e9b3d8 -->
<!-- tarav.breadcrumb b06883ae628e -->

The check is about presence only, over fixed search places: `.agents/skills` in the Project and in the home folder. These are not configurable for now; Tarav starts rigid and can add configuration later. Tarav also checks the minimal structure it requires, such as `.claude/skills` being a sensible link to `.agents/skills` in both places.
<!-- tarav.breadcrumb 14ee4bb80c84 -->

For this purpose a skill is modelled from the outside, by looking at its folder, with just enough for identity. That object need not be a Skillware skill, although a Skillware skill can be one.
<!-- tarav.breadcrumb 568549e1c071 -->

Every Project has its own skill folders, sub-projects included; how they are populated or linked is outside the checks. The checks state that the bootstrap infrastructure is in place in case an agent starts in the folder. They make no claim about what a harness will actually load.
<!-- tarav.breadcrumb a1667ab9d311 -->

[Impl.Req 873](../../../tarav-py/notes/live/873-project-skills-bootstrap-impl-req.md) designs the implementation on top of request 872. Its skill object, check names and the "resolves to the same directory" structure rule are agent proposals awaiting confirmation; nothing is implemented yet.
<!-- tarav.breadcrumb 5c27b317fbdb -->

### Implementation

The 873 implementation adds [FolderSkill](../../../tarav-py/src/tarav/l1/skills/folder.py), `project.agents.skills` discovery, and typed checks for the fixed Tarav skill, configured Project skill, and Project/home folder structure. The folder comparison uses resolved directories, which accepts sibling links into one depot; this and unconditional checks are bounded implementation choices, not additional User decisions. The [tests](../../../tarav-py/tests/test_project_skills.py) cover declared names, Project and home discovery, missing and undeclared skills, and both valid link layouts. The shared worktree's full Python suite passed 183 tests and Ruff passed. The root Project check completed all 362 checks; its new skill checks found three undeclared Project package skills, with no missing Tarav skill or folder findings. The Project markers were left unchanged because adoption is outside 873.
<!-- tarav.breadcrumb 987b86ca316c -->

Request 873 is committed as `2ea7d0b`. The scoped clean checkout passed 173 tests and Ruff; the commit includes the minimal Skills Workflow prerequisite while preserving unrelated worktree edits.
<!-- tarav.breadcrumb 7a98fdeae6d7 -->
