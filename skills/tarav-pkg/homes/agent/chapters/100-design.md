> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

****

## Scope.Axis

- [DF] the storage axis is project-scope versus user-scope: what is project data and what is user data ^c20260818-0u
- [DC] a project holds a project-level .tarav2 folder and the user holds a global ~/.tarav2 ^c20260818-1u
- [CT] public data is written on the project folder while private data belongs to the user tier and is not exported by default ^c20260818-2u
- [DC] scope and authority are separate axes that both name the user: scope is what the data spans, authority is whose touch governs it ^c20260818-3u

****

## Touch.Authority.Manifest

- [DF] a surface declares its type and its Touch.Authority through a centrally controlled manifest that a project must register to be a source of Touched.Data ^c20260818-4u
- [DC] manifest approval is a simple User.Approval.Gate decided once per surface, and its implementation is deferred ^c20260818-5u
- [CT] any surface carrying Touch.Authority is git backed ^c20260818-6u
- [PR] the manifest is presently a declaration surface rather than an enforcement system ^c20260818-7u

****

## Touched.Index.Record

- [DF] the record is the serialized representation of an Index line, described first as a model rather than as a file or a format ^c20260818-8u
- [CT] a canonical JSON schema defines the record while storage stays free, so one record may be spread across several files ^c20260818-9u
- [DC] Tarav provides the storage primitives beneath the record rather than fixing one on-disk form ^c20260818-10u

****

## Project.Home

- [DF] a Skill.Package and a notes surface each carry homes, one per user plus an agent home, holding chapters and appendix under a local index ^c20260818-11u
- [DC] homes/ceo is the default user home and the default user name ^c20260818-12u
- [RJ] multi-user mechanics are not designed yet; the ceo home stays a plain default rather than a role with precedence ^c20260818-13u

****

## Tarav2.MVP

- [DF] the tarav2 MVP is parity with the tarav1 index and hugentic system only, so tarav2 can handle its own index and workflows ^c20260818-14u
- [DC] the MVP includes chatlas2 integration because the whole hugentic system turns on the index and the chats together ^c20260818-15u
- [CT] the goal is a bootstrapping system that can be used and evolved instead of the old one ^c20260818-16u
- [DC] tarav2 ships both tarav2- skills and a tarav2 python library and CLI, integrating the new design with the old implementation ^c20260818-17u
- [DC] all tarav2 subsystems are implemented under a single tarav2 root folder ^c20260818-18u

****

## Index.WIP.Surface

- [CT] the index is a WIP.Surface and anything in it may be changed ^c20260818-19u
- [CT] drift is a signal to work rather than a violation ^d20260818-20u

****

## Typed.Agent.State

- [CT] the system will not carry a value which is merely agent-based ^c20260819-15u
- [DC] where a value must be agent-generated it carries inlined assertions close by, so it is harder for an agent to just talk ^c20260819-19u
- [DC] a more auditable structure always displaces an agent definition, so a standing tied to a surface needs no field ^c20260819-20u
- [DF] a Gate is a token round-trip: the user turn carries the token and qualifies as touch, and an agent turn carries the same token with the line verbatim ^c20260819-21u
- [CT] evidence must be solid, like a User.Turn opening a Gate, rather than a recorded summary ^c20260819-22u

****

## Index.Removal

- [CT] deleted lines are tracked on git and not by the index system ^c20260819-23u
- [DC] an index-side removals ledger is an invented mechanism, so removal carries no reason and no refusal ^c20260819-24u

****

## Index.Head.Surface

- [DF] a line is in the HEAD if it is on a HEAD.Surface, which states what has been promoted ^c20260819-25u
- [DC] index standing is linked to presence on a surface, so no supersedes field is needed ^c20260819-26u
- [DC] a field may state design status when it is a turn containing a gate with a proper token mechanism ^c20260819-27u
- [DF] the approval turn is that gate, and approval there also means moving the line to the HEAD ^c20260819-16u

****

## State.Estimation

- [CT] an Agent.State is dangerous because it is not easy to verify in general, so the design question is how costly verification is ^c20260819-17u
- [DF] an Untyped.Agent.State is expensive to validate and is avoided; a Typed.Agent.State carries assertions that are cheap to validate ^c20260819-18u
- [DC] the implemented assertions belong to the type of the state, which is what tooling such as the linter reacts to ^d20260819-13u
- [DF] a variable is not fundamental when something in the world computes it cheaply, so determinacy was never the test ^d20260819-14u
- [CT] the Touched.Index is a collection of Agent.State.Variables and the system around it exists to validate them ^d20260819-15u
- [DF] a state is minimally a value plus an err or unknown estimate, and using it without estimating that pair is an antipattern ^d20260819-16u
- [DC] the assertions are the estimator, so a state failing many systematic assertions is probably a Bad.State, or the system drifted ^d20260819-17u

****

## Dumb.Code

- [CT] DUMB.CODE.IS.BETTER: the linter saves the agent computable operations and never does the semantic work ^d20260819-18u
- [DC] rules may overdetect and produce false positives because an agent is on the other side, and that is acceptable by design ^d20260819-19u
- [DC] agent search is expensive because finding one error requires semantically re-verifying everything as good ^d20260819-20u
- [DF] the check catalog is a Fishing.Net: cheap tests run over all items, converting expensive semantic attention into cheap mechanical attention ^d20260819-21u
- [DC] the growth rule is TDD's: a bad index with a clean linter means the check is missing ^d20260819-22u

****

## Signal.Not.Semantics

- [CT] the linter communicates no semantic value because agents double-check from first principles and that is their job ^d20260819-23u
- [DF] a finding is a standardized typed signal of a well-declared computation ^d20260819-24u
- [CT] a check's prose description is itself Untyped.Agent.State, a stored copy of a computable fact ^d20260819-25u
- [DC] point the agent at the check's implementation, because for understanding a check the agent reads the code ^d20260819-26u
- [DC] do not describe the object; describe how to explore the system and tell the agent where to look ^d20260819-27u

****
