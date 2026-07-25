****

## User.Gate/Agendix/Candidate.Skw.Context.Gate

- [DF] a `Skw.Context.Gate` is a `Skw.Gate` that controls and audits whether required context is available to the agent performing a protected act ^c20260724-24u
- [CT] the agent cannot complete the protected act without satisfying every required context checkpoint ^c20260724-24u
- [PR] its gold standard is evidence that the required context was loaded and understood sufficiently for the protected act ^c20260724-24u
- [PR] weaker evidence mechanisms may provide partial robustness when the gold standard cannot be established practically ^c20260724-24u
- [CT] each mechanism must make its evidence strength explicit ^c20260724-24u
- [FR] several context-gating mechanisms may compose to increase confidence ^c20260724-24u

****

## User.Gate/Agendix/Candidate.Skw.Pull

- [DF] a `Skw.Pull` is a challenge-response mechanism that requests evidence from an agent before a protected act ^c20260724-25u
- [CT] each pull defines what must be returned and how the response is evaluated ^c20260724-25u
- [PR] a pull makes satisfaction of an instruction mechanically inspectable ^c20260724-25u
- [CT] the evidence strength of a pull depends on what its response demonstrates ^c20260724-25u
- [RJ] a `Skw.Pull` does not define the protected act or its acceptance condition ^c20260724-25u
- [FR] a `Skw.Gate` may require one or more pulls ^c20260724-25u
- [EX] an unlock-token pull requests a literal obtained through a context surface ^c20260724-25u
- [EX] a semantic pull requests an answer derived from the meaning of loaded context ^c20260724-25u
- [EX] a session-id pull lets tooling inspect the agent's `Chat.Surface` independently ^c20260724-25u
