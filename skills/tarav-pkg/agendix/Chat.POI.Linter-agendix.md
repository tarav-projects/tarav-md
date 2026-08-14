****

## Chat.POI.Linter/Agendix

- [DC] an agent session may bind its `Session.Identity` once so protected commands can obtain the corresponding `Chatlas.Session.Model` directly ^c20260724-64u
- [PR] command-side chat inspection provides stronger evidence than asking the agent to self-report its context ^c20260724-110u
- [DC] a protected command may lint the bound chat state and refuse the act while required evidence is missing ^c20260724-63u
- [PR] unmet chat conditions should surface as POIs that explain why the act was refused ^c20260724-120u
- [PR] the agent uses those POIs to request the missing user or context turn and retry the command ^c20260724-117u
