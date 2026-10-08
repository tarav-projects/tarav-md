# Agents bootstrap

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

## Purpose

Bootstrap here is the minimal, operating-system-loading level of contextualization: what must be in place in a Project so that an arriving agent can hook into the harness even when it has nothing else. The first entry point is the agents file, because agent harnesses already load it. Tarav should integrate with those industry-standard interfaces, the agents file and the skill system, rather than replace them.
<!-- tarav.breadcrumb e000c8302098ea237ba7fa0e93f4aeaea2d5be80b83b630d4dde093e48fbfe2e -->

Redundancy is intended. No single contextualization workflow has to be perfect; several stacked workflows are what make the system robust.
<!-- tarav.breadcrumb a877553bedfa0590fe7813ddaebe7034936dc71b8fcd95437c24e5a3d5cdc87b -->
<!-- tarav.breadcrumb c1d2d42629ac6249232eb87e4d10342b09b9749c2897f440d885d866298d37d8 -->

## Tarav System Prompt

The Tarav System Prompt is a section that every Project's agents file must contain. It is constitutive: identical across Projects, so there is homogeneity. It is not a short pointer. One to two pages are acceptable, because always-loaded context that explains core Tarav and how to get more context saves more than it costs.
<!-- tarav.breadcrumb e0cad8ed5b0c339485dfd845c6ff36646d2149e799be1944b7df4b14303df86b -->

Its text lives in the Tarav code base and is maintained like any other code; the wording is expected to change as Tarav improves. The mechanics are deliberately small: a document and a check. When a Project's copy is missing or not identical, a POI points to the command or source file where the current text can be found.
<!-- tarav.breadcrumb 8b741022aa37c36900121991219a17cca17ae12480675dd2194efc43e53b61f4 -->

## Project System Prompt

The same mechanics apply one level down. After bootstrapping into Tarav, the agent needs to bootstrap into the Project, so each Project defines its own system prompt and a Project without one has a POI. Tarav does not prescribe what Projects add beyond that.
<!-- tarav.breadcrumb 83192095c38faf1273c4230a8b63645f429d11c132d86a946235889496737527 -->
<!-- tarav.breadcrumb 97d4fce9a7af2335d08937638a745c72c768f6baea5d8f0907fd03d1d5bf67a4 -->

Every Project carries both prompts, child Projects included. A Project can disable the requirement explicitly in its configuration; otherwise a missing or stale prompt is reported.
<!-- tarav.breadcrumb 5e11963a1fecd31681a93180a662aaa9dc71454b26816e6c39d82e11902d0b07 -->

## The agents file under Skillware

The whole agents file is under Tarav control. It is developed with Skillware like a skill, with blocks, annotations and dependencies, and its source sits in a skillware folder inside the Project's `.tarav/` folder.
<!-- tarav.breadcrumb 4af507948a51d176b0a1010323b674a6c137498fd9af5f5ff4646d65e0b33619 -->

Skillware is the only path. The bootstrap concerns the arriving agent, which only reads the file. Maintaining it is work for an agent that already has Tarav context, with the User in the loop, and a POI may ask for the matter to be raised to the User.
<!-- tarav.breadcrumb aeb65baed418200293a162a482c631769b65b68cf5a1291a49a2ecf61c40e83b -->

A Project may declare several agents files, but only one arrangement is accepted: one main file under Skillware control, and every other file a symlink to it.
<!-- tarav.breadcrumb 2c15b8fc849e8b89674f010baebb8b91e2bb62887ecf48d3213734b3d1cdc504 -->

## Project access and checks

The agents file is a property of the Project. It is a class object built on Skillware primitives, reached through a `project.agents` namespace that will hold more over time, under an explicit agents-file name. The Project can be asked for its path and source, and the file has its own checks.
<!-- tarav.breadcrumb 92e5b7527dd9fccc56d938f3aa91e64aee181b707b23b0f0fa8e1f61237ab477 -->
<!-- tarav.breadcrumb 89b2b791edd799b8b08caee5a6ad06e7f490f15bb1eaf574b9b4d34ea378fb83 -->
<!-- tarav.breadcrumb 7ac5b9eea838298d4963f3f88a9041868f233da37407bcd0577ce2b9fff68e4f -->
<!-- tarav.breadcrumb 007156807257bf8d1678a38632c64ddd4a204976d2ca8cc0111b04eb1b28a9f9 -->

Findings are typed check POIs produced by the existing Check machinery, and the agents checks are part of the general Project checks, so `tarav check --project` runs them. Further checks, such as alias equivalence, can be added in the same place.
<!-- tarav.breadcrumb 3b88fa399d5f160dcc48264b170c8ebae4f58310568cde675bdafdf24ee74302 -->
<!-- tarav.breadcrumb 2c07046416d669f0397c7b83fff9b2c5835d57c9842f3f87cf27501fc6438e59 -->

## Implementation

[Impl.Req 872](../../../tarav-py/notes/live/872-project-agents-bootstrap-impl-req.md) designs the first implementation in `tarav-py`. Its proposed carrier class, depot location and opt-out granularity are agent proposals awaiting the User's confirmation; nothing is implemented yet.
<!-- tarav.breadcrumb 0f7a73e0c6bcdc262a35856cb46dd12e77bee9679338ae1554c6bfcb1dbaf098 -->

## Skill availability

Skills are the second bootstrap entry point. A Tarav Project is the Tarav version of the folder-rooted project that agent harnesses already use, so the Project should know which skills an agent started in its folder would have, and check that the required ones are available.
<!-- tarav.breadcrumb 64fdf1a03d756cc69d4e9bcb44239a8b97d982b306b37ed89959e499fd168c05 -->

Two skills are required. The Tarav package skill is the documentation system behind the short bootstrap text; its name is fixed in Tarav code because the check ships with Tarav. The Project package skill is the entry point to the skill part of a Project; each Project names it in its configuration. It need not be developed in the Project, and several Projects may name the same skill, as `tarav-py` and `tarav-md` both name the Tarav package skill.
<!-- tarav.breadcrumb 95e8c7e9b3d8b117cd85ef230213f8cec65fc136ddb025adfa6db8a895523321 -->
<!-- tarav.breadcrumb b06883ae628e0a9d73c88fa74b1b159189ea11995d389ab6f9ac019ab8669ace -->

The check is about presence only, over fixed search places: `.agents/skills` in the Project and in the home folder. These are not configurable for now; Tarav starts rigid and can add configuration later. Tarav also checks the minimal structure it requires, such as `.claude/skills` being a sensible link to `.agents/skills` in both places.
<!-- tarav.breadcrumb 14ee4bb80c84ac5199be0c06c2ed61c065b803b9186ac8cf595302e159d8c97e -->

For this purpose a skill is modelled from the outside, by looking at its folder, with just enough for identity. That object need not be a Skillware skill, although a Skillware skill can be one.
<!-- tarav.breadcrumb 568549e1c07110f0f8254b76561e220f48527e3d0c48b2a3c831ab2001609bf6 -->

Every Project has its own skill folders, sub-projects included; how they are populated or linked is outside the checks. The checks state that the bootstrap infrastructure is in place in case an agent starts in the folder. They make no claim about what a harness will actually load.
<!-- tarav.breadcrumb a1667ab9d311ab261cf9eaf643ecb00a78137f4fc01888389a0dcba929d3e8df -->

[Impl.Req 873](../../../tarav-py/notes/live/873-project-skills-bootstrap-impl-req.md) designs the implementation on top of request 872. Its skill object, check names and the "resolves to the same directory" structure rule are agent proposals awaiting confirmation; nothing is implemented yet.
<!-- tarav.breadcrumb 5c27b317fbdbd2fb89a53dc9b4f816d68764474bc4c9606369804e6e1f212061 -->
