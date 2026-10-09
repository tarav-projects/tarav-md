# Operator Context, Directives and Harnessed Actions

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

The design of 2026-10-09. Passages marked "Agent proposal" or "Agent" were
suggested by the agent and are not decided. The names are provisional: the
User expects them to follow from which objects turn out to carry the most
weight.

## Current model (read this first)

The discussion changed its own conclusions several times in one day. This
section states where it ended; the User asked that the Wiki state the current
design and not only append to the old one. The sections after it are the path
that led here, and each says where it has been overtaken.
<!-- tarav.breadcrumb 5dd288aa0c73682cbb141ad086fd2d5eec7359b9513861a503e5e632668cccd1 -->

1. **A POI is only an event**: a situation was found and raised. It is worded
   descriptively and says nothing about what to do.
<!-- tarav.breadcrumb 54d21242642e665e2fc3416e2efa205b2244035a941f28fe7292e4cbc8f3ff22 -->
<!-- tarav.breadcrumb 3c0839b2e58d5a70a728aa53a5813a5c827feba8e93ba88c3272602d5585812f -->
2. **What follows a POI is an action.** An actionable POI spins one action.
   That run is what persists and is worked on; it is what a tracked POI used
   to be. It has several close paths: the situation is gone, it was dismissed
   (what was called a blessing), or what it asked for was provided. See
   [POI system](poi-system.md).
<!-- tarav.breadcrumb 50d6b3493b971b669649c5a632031997ceabcf723e902039c420a102df44aaec -->
<!-- tarav.breadcrumb f1b94bc2e319c52519b61e2081b343e44be5350d6c26fc1d89867a75046d14b1 -->
3. **Actions are typed.** An Action Type is a definition and a run is an
   instance, as a program and a process. The first concrete kind is the Step
   action: an opening test, the work, close paths. Each action links to a
   skill section; guidance about what to do lives there.
<!-- tarav.breadcrumb 8279f72e640ac940129f1e89aae98658542c2bd45809d8fad956b8e5136e0223 -->
<!-- tarav.breadcrumb 1160415612b251b41079255752fc6b8de3f333c3b54e92f1f5f4be4c87248d0a -->
4. **The Operator Context is a place, not an object per session.** Agents put
   typed input objects there for whatever consumer needs them. The consumer
   takes them itself, so it can check and keep what it was given. Objects may
   be edited; a consumer that cares keeps a hash.
<!-- tarav.breadcrumb e4daa5264af4c53c5ce346b5a185044f94e0b851da9afa97b72e941f91dbd8ed -->
<!-- tarav.breadcrumb 8e482dde4c1c74bd7feed2e6463909674f316ff422e49ad8cc17360373ee48c4 -->
5. **Everything is central and tracked**, as Records in the Record Registry,
   outside the Project's folder. POI tracking is to move out of the Project
   too.
<!-- tarav.breadcrumb 6ec9fe6072d4aeea4b4fd9d811a951e693d37e3ac969f1d7f1f7b55007c63a16 -->
<!-- tarav.breadcrumb 4c43c70038342fbc4fb1e0bf8fbdf234a2af374f521d0a80cdda434fdc88d82d -->
6. **No invariant about actions**: Tarav offers elemental primitives and
   packaged bundles, and a bundle may require its parts.
<!-- tarav.breadcrumb 511ffff50643f1f1c78968544da785ea7db0aa90b44fed182e7aa5b1396013bb -->
<!-- tarav.breadcrumb bce0730b024fd8ca96e7026dcfae2028b9e3b02fafd851a8f819dc9f8937a663 -->

Still open, discussed below and not settled: Directives and gating; surfaces
that only certain actions may change; how Programs and Actions merge; a typed
Message; typed subjects and precedent; grades of dismissal; other workflows'
actions hooked to a POI and chains between actions.

In code (`tarav-py`): request 891 built the Operator Context store, the Step
action with a single closing test, and a blessing bundle. Request 892, designed
and not executed, replaces that bundle with the POI resolution action and its
close paths. The Project's POI tracking and blessings are unchanged.

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

What the User fixed at this point, of which two items were later changed:

- It holds what the agent puts there for the code to contextualize.
- It is linked to the session ID.
- It is the agent's typed input, and every run can read it. *First stated as
  a JSON file in the Project's `.tarav/`; later changed to objects in a
  central, tracked place outside the Project.*
- Workflows implement inside it whatever they need. A workflow can require
  the context to be well set up.
- Standard checks follow, such as "this session has open actions".
<!-- tarav.breadcrumb 14ce3760145a0b66987d4ea595e1619a105e9a8c5e757efaa1fac734d812e7c8 -->

Refined by the User (itself overtaken by "objects per consumer" in the
current model): it need not be a single file. It is better as a folder
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

Overtaken: these were drafted for the session-wide context and for Directives,
before Actions were designed. The first case, blessing, is now the dismissal
close path of a POI's action. They are kept as the record of that stage.

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

## Later the same day: the model changed, and Actions were designed

This is the stage the current model comes from. It supersedes the
folder-per-session picture above where they differ. One part of it was
overtaken in turn: the blessing root action became a close path of the POI's
own action (see [POI system](poi-system.md)).

### Operator Context as a place for typed arguments

A single context object per session creates traffic problems and makes
continuing an action in another session awkward. The User prefers a
collection of context objects, produced for whatever consumer needs one: an
action, a workflow. An action can keep a hash of its context to know when it
changed and react.
<!-- tarav.breadcrumb dd199293c06c2ada8f0cbb5837d482eaeeac9065191809bbf252308b9b9e6ca4 -->

The objects need not be immutable. A consumer that wants that can check and
detect changes; the store does not enforce it.
<!-- tarav.breadcrumb d6e11423bb45d4880ff96db93cb5216db94540cfdf890ce7d6fc809332f1e1ae -->

It is like another file system: a folder where agents put the typed objects
that are the arguments of other pipelines. A general or central object may
exist, depending on how workflows are organized; none is required. An object
may be tied to a Project, to a session, or be free, each repeating inside
which Project and session it concerns. Nothing is prescribed.
<!-- tarav.breadcrumb 3ec63a8bef306b47f0c14e7f1f66db145fe9def41063e2b928e7674e6aa2ed49 -->
<!-- tarav.breadcrumb 8697e56ae8a14848307d83adf1783d0612d9045a4536512080df2f0b2b66bc88 -->

The gain is control at the point of taking. The agent prepares the starting
input in this place, and the workflow takes it from there: that taking is
Tarav's code, so it can check and snapshot what it was given. The agent does
not meddle with the action's mechanics, and the action stores its execution
elsewhere. A new session registers on the action and is appended. It is the
situation pattern applied to input.
<!-- tarav.breadcrumb 6a38cb979ee66c3b035155962799b6a1f90725a82fe865ffc4d3236ba4a7a7b5 -->

Different workflows inventing different conventions is an implementation
matter that base Types and maintenance can settle, not a risk for the
harnessing.
<!-- tarav.breadcrumb 68e325772948e573ddfd35dbb8a61461094bd74fbc81d04ff4b82487f0cddd6c -->

### Everything is centralized and tracked

Tarav provides standard places, outside the Project's folder, for the
Operator Context and for the actions' durable data, as Records in the Record
Registry with its Git configuration. Cluttering a Tarav-owned repository is
cheaper to fix than interfering with a Project's repository. Portability is
not a concern yet. For the same reason POI tracking is to move out of the
Project too.
<!-- tarav.breadcrumb 863ed54ece31d570d62ee01b0ef5221a1dc3538971437ad1441fd360c9ab360a -->
<!-- tarav.breadcrumb fb8a584942f03291fe4d31abc8d4e7ecf32bd81701cf6916e46aa92cc8cf4fac -->

### Actions

The action workflow is designed first and the Operator Context emerges from
it. Blessing a POI is an action: a Type represents it, with state and
validation. There is a blessing action that is the root of all actions that
aim to bless. *(Later: blessing is a way to close the POI's action, not a root
action.)*
<!-- tarav.breadcrumb 7e6d19863d913c2f31448ae0882f0239f044910590e92a26471ff57eaa84b36d -->
<!-- tarav.breadcrumb 74ffe11189a45aa46b3735fe0e064ff85594a4c4f915364eb4c17346d6668bfa -->

With actions typed, POIs, checks, situations, blessings, assertions and
scores are objects gathered around well-defined actions, which can be
narrowly specialized. This is the fundamental way agents interact with the
system.
<!-- tarav.breadcrumb 222ab470a9e0fca7ad47730aed2c64f6d941794e4993b4e9072614a1866b934d -->

There is no invariant here in either direction: not that everything must be
an action, not that work must be free of them. Tarav is expressive. It has
elemental primitives and packaged bundles, and a bundle can require its parts
as a `CheckPOI` requires its check. A Project grows from being harnessed by
the User's input toward types, checks and then actions.
<!-- tarav.breadcrumb e958f6c8437778ceff9df8c6b211f32a1f58b465aec061a6009a5637b2ea6dfb -->
<!-- tarav.breadcrumb cce141adefb886e377a99681b80b81b83cc94bd639ac8341a128b2271c0415f3 -->
<!-- tarav.breadcrumb 1e5a458f3e1ae71bb857fa470f1265c291944af0ffa55972203abb5dd51b8983 -->
<!-- tarav.breadcrumb 3d34fb11ec787ac0b8a4cba8fb8c17c0bed372879e6f2a6390cd9d9350d2ff18 -->

The base Types have almost no functionality. An action has an identity as a
Type and as an instance, as a program and a process do; runs are asked of the
Project by state. Every action links to a skill or a path inside one, and
starting it tells the agent what to load. It reminded the User of Iterante and
should be more minimal: starting tests, the work, a validation test.
<!-- tarav.breadcrumb 773cd1f16773ed64b1c6145e5c3037efe3c446ce9eca12fa6ffc32ea996795a3 -->

The first concrete action is the Step action: an initial test and closing
tests around a piece of work of any size. "Batchy" (typed input and output,
exit code) is a capability an action may have. A Step gets its input from the
Operator Context, its tests are typed and can be Checks, and it has an output
so steps can be stacked.
<!-- tarav.breadcrumb 296e8e5b329f88f14b9c1788e07fa7683722478c75a422c2974a7c4d67eb5419 -->
<!-- tarav.breadcrumb 1f355fdd0f990ed1ed954477e375c91774bb1697d3c794ffc728f8195c1e1cec -->

### What was built (request 891)

The User asked for a minimal viable product, tried on a test workflow with
POIs and blessings controlled by an action.
<!-- tarav.breadcrumb 5334c80664f90112266915971098f4af4178bcf8726ce04487ea16d861a622b7 -->

[Request 891](../../../tarav-py/notes/live/891-actions-workflow-step-action-mvp-impl-req.md)
built it in `tarav-py`:

- `tarav.l1.operator_context`: `OperatorContext` and a store whose `take()`
  returns the object with the hash of what was read.
- `tarav.l1.actions`: `Action`, `StepAction`, the recorded `ActionRun` and
  `StepRunner` (start, operation, close, abort).
- `tarav.l2.actions.blessing`: the blessing root action, the POI capability
  "blessed through an action", and a check that reports a blessing made
  outside a run.
- `tarav.l2.tests.actions`: a workspace of text files whose marker lines raise
  POIs, blessed through `Tarav.Test.Actions.Blessing`.
- Commands `tarav operator-context put|show|list` and
  `tarav action types|start|do|close|abort|show|list`.

Agent choices in it, not decided by the User: a run closes only when its
closing tests pass and is otherwise left running, with `abort` for an exit
with error; a failed opening test still records a closed run; operations are
how a domain write is put under the action; Action Types are registered
explicitly; registry keys are flat.

