# Agentos Agentic Framework Redesign - design-summary

## Summary

This note captures the converged design direction for consolidating the agentic part of Agentos. The goal is to define a coherent agentic framework layer, clarify its philosophy and subsystem model, and use `agentos-md` as the clean redesign home for updated specs and skill surfaces.

## Accepted Decisions

1. `agentos` is framed as a library of solutions to recurring project-development problems, including but not limited to agentic workflows.
Rationale: this makes the framework broader than a single feature set and lets agentic capabilities sit on top of a stable base.

2. `agentos project` is a base project identity and should be detected canonically through `.agentos/project.json`.
Rationale: non-agentic and agentic subsystems both need a stable way to know that a repository participates in the Agentos ecosystem.

3. The agentic part should be modeled as a higher-level framework layer on top of the base Agentos project identity.
Rationale: this separates general project participation in Agentos from the specific surfaces used for agent-human collaboration.

4. The agentic framework should be defined by composable subsystems and workflow primitives rather than by a fixed folder checklist.
Rationale: the important contract is which problems are solved and how surfaces interact, not whether every repository contains the same tree.

5. Agentic subsystems are opt-in, but dependency-aware.
Rationale: a repository may adopt only some capabilities, but each subsystem must define the prerequisites and lower-level conventions it depends on.

6. Existing pieces such as skills, notes, live notes, index notes, and live scripts should be consolidated as parts of one coherent development philosophy.
Rationale: these are not isolated tools; they are coordinated answers to how humans and agents should work together in a repository.

7. Workflow skills are first-class and should embody the Agentos philosophy operationally.
Rationale: skills should not only expose knowledge; they should also install, maintain, and enforce repeatable ways of working such as bootstrap, maintenance, consolidation, review, and artifact production.

8. `agentos-md` should be the fresh design workspace for the redesign of the agentic framework.
Rationale: this provides a clean place to redesign specs, workflow primitives, and skill surfaces without inheriting legacy structure by default.

## Execution Plan

1. Establish `agentos-md` as the redesign workspace and treat it as the design authority for the new agentic framework layer during the redesign.

2. Define the top-level model in `agentos-md`: base Agentos project identity, agentic framework layer, subsystem boundaries, and workflow-primitive philosophy.

3. Specify the first canonical workflow primitives, including bootstrap, maintenance, consolidation, subsystem adoption, artifact creation, and transition from live work to durable knowledge.

4. Define the updated subsystem surfaces and their dependency contracts, especially around notes, live notes, index notes, live scripts, artifacts, and skill mechanics.

5. Design the new skill surfaces that implement and maintain those workflow primitives and subsystem contracts.

6. Compare the redesigned surfaces against the current Agentos implementation and identify what should be migrated, superseded, or left as legacy.

## Deferred Items

- Final naming for the higher-level agentic layer remains open.
Reason: the architectural split is agreed, but the umbrella term may still change as the specs become more concrete.

- Detailed filesystem layout inside `agentos-md` is deferred.
Reason: the initial need is the design workspace and artifact home; exact internal structure should follow the subsystem and workflow definitions.

- Migration strategy back into the broader `agentos-py` codebase is deferred.
Reason: the redesign should converge first before deciding how and when each surface becomes canonical in the main project.

## Relevant Files Or Surfaces

- `/Users/pereiro/projects/agentos-project/agentos-py/.agentos/project.json`
- `/Users/pereiro/projects/agentos-project/agentos-py/`
- `/Users/pereiro/projects/agentos-project/agentos-md/skills/`
- `/Users/pereiro/projects/agentos-project/agentos-md/notes/index/`
- `/Users/pereiro/projects/agentos-project/agentos-md/notes/live/`

## Open Questions

- What should the canonical name of the higher-level layer be in the final specs?
- Which workflow primitives should be considered mandatory first-class surfaces in the redesign?
- How should the redesigned skill taxonomy be expressed so that foundation, adoption, operation, and artifact skills stay clearly separated?

## End Log

- 2026-05-03: Created initial design-summary artifact from the converged design discussion and anchored it in the new `agentos-md` workspace.
