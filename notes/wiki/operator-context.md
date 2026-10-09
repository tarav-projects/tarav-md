# Operator Context, Directives and Harnessed Actions

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

An open design discussion (2026-10-09). Nothing here is implemented. Passages
marked "Agent proposal" were suggested by the agent and are not decided. The
names are provisional: the User expects them to follow from which objects
turn out to carry the most weight.

## Where it started: what a POI should carry

The discussion began by looking for first-principle arguments for the POI
design, compared with Python's exception system.
<!-- tarav.breadcrumb 6a065403bf4801be1289f5b49011509fd0d3706fc15a690e9cdbce4b20b8e715 -->

A POI must above all connect to the code that produced it and the situation
that produced it. Its job is to narrow the gap between producer and reader:
the producer's intention is made clear so the reader can judge with all the
available information. The producer cannot know the reader's goal, and the
design does not pretend it can.
<!-- tarav.breadcrumb 65077efb86a86aa445593ed4d1499ef859183604b3280765a1e5f7a3ba5c45ed -->

Consequences the User drew:

- A general `.throw()` on POIs that raises the POI as an exception, for
  callers that want it. The exception carries the whole POI.
<!-- tarav.breadcrumb dd8c6cd56b6fa0398631d52bcb8fe84352d51788a0f39a456e8071d22cf97fb2 -->
<!-- tarav.breadcrumb dceef8ef9c6f0091c7a15ac36d5633f44a15c377076fba16a39ee637f0037047 -->
- POIs are `Workflow.Neutral`: their wording is descriptive, not imperative.
  "What to do" may not belong on the POI at all; it belongs to the skill that
  contextualizes the agent. The POI gives evidence and clear producer
  intention, plus tooling for getting more context.
<!-- tarav.breadcrumb eb4d24a3bb90f2d3d91c87e3693c1cf7791b68607f8f76edc0c2a63c318c8674 -->
<!-- tarav.breadcrumb d24c10e1965aae4ac0fa5006ac9e46b067b6129cf19b0f3e1a3948124aeb28b7 -->
- `may_do` moves out of the POI and can be part of the context. The POI is
  concerned with the immediate producer description: the triggered check and
  the situation. Precedent (how earlier cases were handled) is another
  contextualization workflow.
<!-- tarav.breadcrumb c6df88f285916f0f3529a9df061cb6db14a5ffc901637d278d4d369a5088d06a -->
- A typed Message is a candidate: the POI has a message, and guidance is
  modelled on the Message Type instead of on the POI.
<!-- tarav.breadcrumb 4ea55fc63ea642f2fa308b50e0190c8591d53d408f58e690d4d28b6439e7528b -->
- Typed subjects (files, other objects) can add semantics beside the
  situation, so an agent, or the code on its behalf, can look for precedent
  on the same POI Type over similar subjects.
<!-- tarav.breadcrumb 6291413376a11027ae437ed6e6615b12c349cb86ec660f75767f9d2f983f8f5d -->
- Weak situations are found by maintenance while processing POIs; that
  cannot be automated.
<!-- tarav.breadcrumb b5128d39299f62137e3481f1712d38b93f70b2d6216e17f764cd44b47368b06d -->

Three layers came out of it (Agent proposal, which the User liked): the POI
carries the producer's intention and evidence; the context carries what is
available; the skill or reader carries the goal and what to do.
<!-- tarav.breadcrumb 50e39e9b55b82b7e55586e5f2086e9b2bf90e0ba762228a3515ff5d7ddb6d121 -->

The loop the User stated: workflow skill → object → context(object, workflow)
→ agent analysis. A skill can prime an agent on what to look for in a POI's
context and can provide a typed Context view. Workflows need skill modules:
the part loaded into the agent that operates them.
<!-- tarav.breadcrumb 165287a398f7a144b630d1c5ef1de052bdbe30d7bc424dc73153bff46286a0a8 -->

The balance the User is still looking for: agents are flexible, but every
added functionality needs instructions. Doing the work in code controls
execution and cost better. Workflows meant for agents should stay simple and
general, with as much as possible done on the code side.
<!-- tarav.breadcrumb 4267f40acdeee27b0e871736cdca52251c7313f172187920d62ff264f8885b67 -->

## Directives: the reader's intention, typed

Tarav should work with agents that have loaded what they are doing. An
object describes the current goal, perhaps a "directive". An agent is expected
to act with a directive at hand, so it can hook into the machinery: conditional
context and other tools that surface the relevant data. Otherwise the system
knows nothing about the caller's intention. Intentions can be typed:
`obj.context(intention)`.
<!-- tarav.breadcrumb 07104a8e8501c3eabd8729a2146e8301bd1e624985fc9b711659326d721fb933 -->

The User added control to the reasons: some actions should not work without a
stated Directive; the harness can gate the available Directives; a Project can
have a numbered set of them; a "wild" Directive means the agent is not
particularly instructed. It is a typed context object for the operator: the
operator establishes its context, including the active Directives, and the
code reacts. It is a communication protocol.
<!-- tarav.breadcrumb 6b4f005d4b5f94b69215782f6bd91ed6f64136cb7b9a5837e4ec3967eef19b20 -->

`Workflow.Neutral` is the good practice when the reader's context is unknown.
Once the agent models its intention explicitly, the machinery has a place to
look and can return what is prescribed for that caller. It is a step toward
formalizing the full agent cycle. The intention is not free text: it is a
typed object, a vocabulary.
<!-- tarav.breadcrumb 5dd4a681584f47ef12175c73bc1f848e7f3664e603e5773630a851de48ad1fa6 -->

Agent proposals, not decided: a Directive selects and ranks, and never changes
facts or a POI's identity; without one the general context must still be
enough; no taxonomy of intentions up front.

## Harnessed Actions

The User described a minimal unit of controlled agent work, composable like
Bash commands, in which the harness decides how much free rein the agent has
and how many checks, scorings and resources are spent.
<!-- tarav.breadcrumb a9d659efc418680caa06d9952f86dc41c45cd07c7081f57cbdcb25385d88ba68 -->

The shape the User accepted, and named "harnessed action":

1. A declared start: a typed Directive plus the operator context.
2. A conditioned middle: every interaction with Tarav can see the Directive.
3. A reserved final stop where the validations of the action run. Checks may
   run anywhere before; what is guaranteed is that the final stop exists.
<!-- tarav.breadcrumb 002932ad51d99ccf5e4c470e9a3f87a7c29aa391ed9f68da08e63916d088a113 -->

Agents are either free or working under a Harnessed Action. A surface can
state that only certain Harnessed Actions may manipulate it, with mechanics
to detect when that did not happen.
<!-- tarav.breadcrumb e679957a05754649deea91bfdb8877b0e92ec814e8d00f263cfa0b33bfe5e610 -->

The dial is controlled mostly by checks. Tarav does not control the agent's
internal harness and does not want to rely on that. An unharnessed ("illegal")
action is detected, and the agent feels the consequence later: a POI, or the
next command failing. Tarav controls the Project and the machinery that
defines the action space over it. An action may have no checks at all. An
action run may be closable only with a hash produced by its passing final
tests; an open run keeps raising POIs.
<!-- tarav.breadcrumb 51cb51293c28cb46e9bbe2c6d90563704b37a525cfe29af54c30e1e9c3d2eba1 -->

Action Types form a vocabulary. For instance a Type can demand that its
completion tests fail when the action is activated.
<!-- tarav.breadcrumb 9394ee6c04d55c38d7fa6cf2a3aaa005f46a69de96a506a2a019d9837bb072be -->

On the Constitution: "validation must not block capture" is about workflows
whose incoming data is valuable enough to ignore the rest, such as the User's
ideas. For workflows that force work in a direction, any amount of friction
toward the fail state is acceptable. The User intends to revise the
Constitution at some point.
<!-- tarav.breadcrumb 2220a9e1745e5350af6b48870b3aa6b24836a855cdd1d218e8a74ec202a798ac -->

Agent proposal: the refusal is of a claim (closing a run), never of a write;
the Constitution keeps only the floor (never lose touched data, never make a
write impossible) and each Action Type declares its own friction.

## Programs and Actions

The User sees [Programs](programs.md) and Harnessed Actions as the same
nature: definitions, particular running instances, tracking, and POIs to work
on. Not all work must go through them; they are how a workflow forces some
formalization. "Action" is the better name for the atomic unit; a Program
might be a root with active Actions. Left for later.
<!-- tarav.breadcrumb dead0cafa04abc3b7bce8be764ea47b5e099ab3f9538549884655ad1ee5bf7df -->
<!-- tarav.breadcrumb c67b44d3057f84ee9f6e56e0e27ec2bb9c9a895a5e0eadbfc2523845d91a1d9c -->

## Operator Context: the object to define first

The realization: the operator context is an explicit object, so the code
finally knows who is calling it. A Directive is one component; a running
Program or Action can be another. Define the context and its mechanics first,
then see what else follows, perhaps by simulating usage.
<!-- tarav.breadcrumb 65cc48ef180dee58212feec357fb0cdd24ccc4cdbf24a4fcf5100224d6d095a0 -->

What the User fixed:

- It holds what the agent puts there for the code to contextualize.
- It is linked to the session ID.
- It is a JSON file somewhere in the Project's `.tarav/`, maintained by the
  agent; every run can read it. It is the agent's typed input.
- Workflows implement inside it whatever they need. A workflow can require
  the context to be well set up.
- Standard checks follow, such as "this session has open actions".
<!-- tarav.breadcrumb 14ce3760145a0b66987d4ea595e1619a105e9a8c5e757efaa1fac734d812e7c8 -->

Refined by the User: it need not be a single file. It is better as a folder
with a main record, described by a class. The Operator Context is itself a
workflow, and other workflows integrate with it: they demand things from it
or put things there themselves. The agent states what its workflows require;
the action workflow, for instance, can have its own space inside. The
internal organization of each space is owned by its workflow.
<!-- tarav.breadcrumb 399dbb5668464134c93a86101a527238cb311ae3e7a57bb95c82ebfc18a4852c -->

The minimum demanded from the internal harness is that an agent can reach
its current session ID. Tarav has Chatlas, but no workflow for dealing with
agents in this way: the User sees Chatlas as an archive concerned with full
transcripts, not as the provider of a model of a running agent. Tarav also
holds earlier code for configuring and running agents. These should be
grouped, or a couple of basic workflows produced, so that "give me the
current session" belongs to a workflow and not only to a command.
<!-- tarav.breadcrumb 83ffb176019ce5d8f5eaed6d44a2da29274a434afaf9b47a46a161be25a85a29 -->

The Operator Context is its own workflow, not a part of Agents: it is just
a folder that agents modify. What is new is that it is an entry point. The
first node of any action or pipeline is now formalized: the context is
prepared, the pipeline runs only on that stated context, and when something
is missing it says what must be configured. It is the same as before, one
level up in formalizing the whole process.
<!-- tarav.breadcrumb c6547af77a56309952094b87d26b25d88f24dbe3d4a515c2e89eb4a81ac7c1f0 -->

### An explicit Agents workflow

Tarav needs an Agents workflow that gathers what it has for interfacing with
providers: how the runners are modelled and asked things. Chatlas stays
important and must not be handicapped; it focuses on transcripts. Agents has
submodules per provider, as the code is already organized. `project.agents`
is another workflow, a sub-workflow of the Project. The existing code is old
but working: it is to be organized, made an explicit workflow and brought to
the current philosophy, not removed.
<!-- tarav.breadcrumb 48fec0342a4cc0eb37731c9d69ffa0e8475f8ed150e83404fa53f86bd37ca9b1 -->

Supported providers are reduced to Claude, Codex and Copilot. The others are
removed as noise; Git history keeps them.
<!-- tarav.breadcrumb f456f4d68a14c12f947cbd1007b8de5c5e889d7c1d4b1a054bc9a064c46a31e3 -->

Agent proposals, not decided:

- One file per session, so several agents in one Project do not overwrite
  each other.
- A small fixed part (session, who) plus one section per workflow, owned by
  that workflow and opaque to the others, as hints are.
- A command finds its file through the session it already can resolve
  (`tarav chatlas current-session`), so no flag is needed on every call.
- The context is a declaration, not proof: checks verify it.
- The live context is operational state; durable records of closed runs are
  a separate thing.

## Simulated usage (Agent draft, for discussion)

Three cases that exist today, written as they might go with an Operator
Context. Each lists what the operator declares, what the code sees, what is
recorded, and where something refuses or raises a POI.

### 1. Blessing a POI from a pasted reference

Today: the User pastes a reference copied from Tarav Center; the agent opens
`tarav context --id … --view tracked-poi` and decides with the User.

- Declares: session; who (agent, on behalf of the User); a Directive such as
  "review POIs".
- Code sees: `context(poi, directive)` adds what a review needs, for instance
  precedent: earlier blessings of this POI Type with their rationales and
  situations.
- Records: the blessing stores the operator context beside the actor it
  stores today.
- Refuses: blessing without a declared Directive, if the Project asks for
  one. With the wild Directive it works and says so in the record.
- Open: does a single blessing need an action run, or only a Directive?

### 2. A Wiki capture pass

Today: the skill resolves the session, writes Notes, submits Breadcrumbs,
commits.

- Declares: session; Directive "capture"; an action run of a capture Type.
- Code sees: nothing may refuse. Checks run and raise POIs only.
- Records: the run lists the Notes it touched; the final stop runs the
  Breadcrumb audits.
- Refuses: only closing the run while a Note still carries provisional
  markers. The Notes themselves are already written.
- Open: an abandoned capture run. Is the open-run POI enough?

### 3. An implementation Develop

Today: Impl.Req, start checkpoint, slices, completion commit.

- Declares: session; Directive "implement request N"; an action run whose
  Type may demand that the completion tests fail at activation.
- Code sees: the request's declared scope as the surfaces this run may touch.
- Records: start state, slices, the hash of the state the final tests passed
  on.
- Refuses: closing without the passing final tests. A change outside the
  scope, or to a protected surface by no run, is detected and raised as a POI.
- Open: several requests at once in one session; the User editing files by
  hand during the run.

### What the three share

A session; a declared intention; optionally a run with a start and a final
stop; a record that keeps the context. They differ in friction: none for
capture, a little for blessing, as much as wanted for implementation.
