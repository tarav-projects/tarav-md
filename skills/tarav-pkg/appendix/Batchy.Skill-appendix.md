# Batchy.Skill — Appendix

****

## Batchy.Skill/Router.Testability

- [DF] `Batchy.Skill/Router.Testability` is the ability to test a skill’s configured `Batchy.Router.Row`s against expected routing outcomes ^c20260731-193u
- [DC] a row’s permitted resolution inputs provide explicit calls or conversational situations to test ^c20260731-131u
- [DC] the row’s destination provides the expected routing outcome ^c20260731-182u
- [CT] tests respect whether the applicable table permits selecting none, one, or several rows ^c20260731-105u
- [DC] behavioral tests run through `tarav-testground` ^c20260731-139u
- [PR] a wrong or missed resolution indicates that the row’s inputs, configuration, or destination need refinement ^c20260731-234u
