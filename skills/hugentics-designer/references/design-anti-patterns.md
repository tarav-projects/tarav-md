# Design Anti-Patterns

A catalog of known failure modes for `What.Design.Session`. Each item names the failure, shows what it looks like, says why it kills the session, and gives the correction.

Designed to be re-read mid-session when something feels off. Original to this skill.

## Question Anti-Patterns

### Bundled questions

- looks like: one prompt that contains three sub-questions or asks for multiple decisions at once
- why it kills: violates one-question-at-a-time; user can only answer one and the others rot
- correction: pick the highest-leverage one (per `interview.md`), park the rest as candidates for the next `Alignment.Maintenance.Turn`

### Leading questions

- looks like: "Do you want option A (recommended) or option B (which has these obvious downsides)?"
- why it kills: pretends to ask but is actually a paraphrased recommendation; user's "yes" is not evidence of alignment
- correction: state the recommendation honestly, then ask whether the user agrees, wants to redirect, or wants to see alternatives

### Premature questions

- looks like: a question whose answer is already in the codebase, prior notes, or the user's earlier turn
- why it kills: burns a question slot and signals the agent isn't reading the evidence; per `interview.md`, "if a question can be answered by inspecting evidence, inspect that evidence instead"
- correction: orient first — read the file, grep the index, recall the prior turn — *then* ask only what evidence cannot answer

### Low-leverage questions

- looks like: asking about decoration, naming, or surface details before the structural decisions
- why it kills: locks in trivia that may get invalidated by the structural decision still pending
- correction: ask the question that unlocks the most downstream choices first

## Discussion Anti-Patterns

### Option dumps

- looks like: "here are five possible approaches, each with tradeoffs..." without a recommendation
- why it kills: pushes design synthesis onto the user; agent is supposed to recommend, not enumerate
- correction: per `discussion.md`, recommend one; mention alternatives in one line if material; expand only if the user asks

### Frictionless agreement

- looks like: the user says X, the agent agrees, the user says Y, the agent agrees with Y too — no pressure, no boundary
- why it kills: not a design session, just a dictation session; no convergence is happening because there was no divergence
- correction: surface the tension when X and Y conflict; pressure-test with a usage scenario; name the tradeoff the user just glossed over

### Restatement without contribution

- looks like: each agent turn rephrases what the user said and adds "agreed"
- why it kills: burns turns without advancing alignment; produces no new design value
- correction: add at least one of — a boundary, a pressure test, an open question, a concrete recommendation, an evidence pointer

### Abstraction drift

- looks like: question was about a concrete contract; agent or user drifted up into "what is design philosophy" or down into "what variable name"
- why it kills: the active question never gets resolved; convergence becomes impossible
- correction: name the drift ("we drifted up a level"), park the new question, return to the active level

### Prose dumps

- looks like: a wall of paragraphs explaining context the user already has
- why it kills: dilutes the signal; the user has to scan for the actual move
- correction: short delta updates per `discussion.md` output shape; full recaps only on explicit request

## Capture Anti-Patterns

### Silent writes

- looks like: agent updates a session artifact or surface without showing the proposed text first
- why it kills: violates the user-gate; user loses the chance to correct wording that carries design judgment
- correction: show the exact proposed text or a concise diff summary, ask for approval, then write

### Premature compression

- looks like: collapsing a settled discussion into a one-liner that loses the boundary or open-pressure that was part of the convergence
- why it kills: the captured block reads clean but cannot rebuild the agent's later judgment from the captured material
- correction: preserve the boundary, the rejected alternative, and the open question — these are `Kernel.Writing`'s "fundamental dimensions"

### Paraphrased user judgment

- looks like: the user said "anyone can put a halo on the model and that is the way"; the agent captured "the model is the mediation surface for halos"
- why it kills: erases user-tone wording that carries authority and reads as a concrete design rule
- correction: preserve user wording when it carries design judgment (per `Kernel.Block:Design`); summarize only the prose, not the judgments

### Settling open material

- looks like: capturing a half-decided block as if every line were converged
- why it kills: future agents (and future-you) read it as settled and stop questioning it
- correction: mark open items explicitly in `#### meta` under `open:`; per `interview.md`, "mark unsettled material explicitly instead of presenting it as settled"

## Evidence Anti-Patterns

### Assumption as fact

- looks like: agent writes a fundamental line based on its prior of how things probably work, with no evidence
- why it kills: contaminates the `Design.Index` with material the agent will later defend as if it were `Hard.Evidence`
- correction: mark provisional lines as such; move to `#### meta` open until evidence lands

### Ignoring user contradiction

- looks like: user says X is wrong; agent acknowledges, then keeps building on X two turns later
- why it kills: user-stated correction is the highest grade of `Hard.Evidence`; ignoring it kills trust
- correction: when the user contradicts session state, update the state immediately or surface the contradiction explicitly

### Stale-evidence cascade

- looks like: the agent is acting on context from earlier in the session that has since been overridden
- why it kills: convergence built on stale ground collapses when the user notices
- correction: per `alignment-loop.md`, surface stale state when it materially affects the current discussion

## Session-Mechanics Anti-Patterns

### Silent turn-switching

- looks like: agent switches from `Alignment.User.Turn` (following user thread) into `Alignment.Maintenance.Turn` (driving the next question) without the user asking
- why it kills: per `alignment-loop.md`, turn switching is user-gated; silent switching produces unwanted questions and burns trust
- correction: suggest the next move; wait for `next`, `continue`, or equivalent

### Interruption bundling

- looks like: the user asks for a status report; the agent also runs a capture audit, also proposes an artifact upgrade
- why it kills: bundling violates "one primary move per maintenance turn"; the user can't respond to three asks in one turn
- correction: per `session-interruptions.md`, one interruption shape per response

### Uncommitted-work blindness

- looks like: user says "next"; agent presents a new question without surfacing that the previous discussion produced uncommitted material
- why it kills: the previous turn's design value evaporates; per `uncommitted-work.md`, the agent must track this
- correction: on continue triggers, check for uncommitted material first; offer capture before advancing

## Self-Audit Prompts

Re-read mid-session if something feels off:

- am I still on the highest-leverage unresolved question?
- did the last user turn contradict any session state I'm still acting on?
- have I preserved the user's wording where it carries judgment?
- are my captured lines marked as evidence-based, assumed, or open?
- did I switch turn modes without user approval?
- is there uncommitted material I'm about to skip past?
- am I writing fundamentals (definition, boundary, judgment, relation, open) or just prose bullets?
