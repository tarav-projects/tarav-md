---
name: agentos-iterante-flow-canvas
description: "Write and maintain canvas representations of Iterante mission flows. Use when working with iterante-canvas, mission flow canvas, or mapping a mission.py to a visual graph."
---

# Iterante Flow Canvas

How to represent an Iterante mission workflow as an Agentos.Canvas graph.

Read `agentos-canvas-base` for canvas format, model layer, CLI commands, and layout ownership. This skill adds the conventions specific to Iterante mission flows.

## Trigger Boundary

Use this skill when:

- The user mentions iterante-canvas, mission flow canvas, or similar.
- You need to create or update a `.canvas` file that maps an Iterante mission.py workflow.
- You need to understand the operator vocabulary or card structure of an existing mission flow canvas.

## The Model

An Iterante flow canvas is a **program description** — a visual representation of what an Iterante mission will perform.

- **Edges are action headers** — `operator: verb`. Who acts and what they do.
- **Cards are action bodies** — the detail of what that action does, produces, or contains.

The edge is the function signature. The card is the function body. Each card reads as the body of its incoming edge:

| Incoming edge | Card describes |
|---|---|
| `iterante: prompt` | what is prompted |
| `agent: submit` | what is submitted |
| `iterante: checkpoint` | what is checkpointed |
| `iterante: evaluate` | what is evaluated |
| `iterante: poll` | what is polled |
| `iterante: ask` | what is asked |
| `iterante: loop` | what changes on loop |
| `iterante: advance` | what advances |
| `iterante: render` | what is rendered |

## Two Actors

| Actor | Scope |
|---|---|
| **Iterante** | The whole runtime side: CLI, mission.py, git, state machine. One actor — no internal breakdown. |
| **Agent** | The AI doing the work: reading, writing, inspecting, answering. |

## Mapping mission.py To Card Pairs

Each `ctx.*` call in mission.py produces a card pair connected by the agent's response:

| mission.py call | Edge in | Prompt card | Edge out | Result card |
|---|---|---|---|---|
| `ctx.task(...)` | `iterante: prompt` | what to do | `agent: submit` | what was done |
| `ctx.poll(...)` | `iterante: poll` | what to classify | `agent: submit` | what was classified |
| `ctx.branch(...)` | `iterante: ask` | what to decide | `agent: answer-yes` / `agent: answer-no` | (next action's card) |
| `ctx.handoff(...)` | `iterante: prompt` | what to report | `agent: submit` | what the report contains |

Program-only transitions (no agent involvement):

| mission.py logic | Edge label | Card describes |
|---|---|---|
| `init(...)` render | `iterante: render` | what instructions are rendered |
| `checkpoint_project(...)` | `iterante: checkpoint` | what is committed |
| Start work section | `iterante: advance` | what is initialized |
| Pass count comparison | `iterante: evaluate` | what is compared |
| Loop back | `iterante: loop` | what changes for next pass |
| Advance forward | `iterante: advance` | what moves forward |

## Operator Verb Vocabulary

| Arrow | Actor | Meaning |
|---|---|---|
| `iterante: render` | Iterante | render mission instructions |
| `iterante: checkpoint` | Iterante | git commit project state |
| `iterante: prompt` | Iterante | open task for agent |
| `iterante: poll` | Iterante | structured-answer request |
| `iterante: ask` | Iterante | binary branch question |
| `iterante: evaluate` | Iterante | program-internal decision point |
| `iterante: loop` | Iterante | program routes back |
| `iterante: advance` | Iterante | program routes forward |
| `agent: submit` | Agent | complete task or poll |
| `agent: answer-yes` | Agent | resolve branch: yes |
| `agent: answer-no` | Agent | resolve branch: no |

## Card Types

| Type | Meaning | Visual |
|---|---|---|
| `content` | Action body — what the action does, produces, or contains | default color |
| `question` | Decision point — what is being decided | color `"3"` (yellow) |

## Two Branch Types

- **Agent-answered branch:** `iterante: ask` going in, `agent: answer-yes` / `agent: answer-no` going out. The agent decides.
- **Program-decided branch:** `iterante: evaluate` going in, `iterante: loop` / `iterante: advance` going out. The program decides.

You can tell at a glance who decides by reading the outgoing edge labels.

## Card Content Guidance

Every card should carry information the edge label alone cannot — it is the body of the action, not a restatement of the header.

- **Prompt cards** describe what Iterante asks: what to inspect, what tools to use, what scope applies.
- **Submit cards** describe what the agent delivers: what was found, what was fixed, what remains.
- **Program cards** describe what the program does: what it checks, what state it updates, why it routes this way.
- **Question cards** describe the decision: what is being evaluated and what the outcomes mean.

## Faithfulness Rule

The canvas mirrors mission.py structure faithfully. Read the actual mission.py before building or updating the canvas.

- If a branch doesn't exist in mission.py, it doesn't exist on the canvas.
- If mission.py uses `ctx.poll`, the canvas uses `iterante: poll`, not `iterante: prompt`.
- If mission.py routes internally (no agent involvement), the edges are `iterante:`, not `agent:`.

## Workflow

1. Read mission.py to understand the flow.
2. Map each `ctx.*` call to a card pair (prompt card + result card).
3. Map program-only transitions to single cards.
4. Build the `_model` with cards and relationships.
5. Use `agentos canvas init` or direct JSON to create the canvas.
6. `agentos canvas render --file ...` to check validity.
7. `agentos canvas render --file ... --apply` to compile.
8. Arrange layout in Obsidian.

## Visual Conventions

- **Question cards** — color `"3"` (yellow)
- **Loop cards** — color `"6"` (purple)
- **Active work section** — color `"5"` (cyan) for manuscript/work-loop cards
- **Trigger event** — color `"4"` (green) for the starting card
