# Batchy.Router — Appendix

****

## Batchy.Router/Skill.Arg

- [DF] `Batchy.Router/Skill.Arg` is the integration through which `Batchy.Router` resolves and binds external data to a canonical `Skill.Arg` ^c20260731-7u
- [CT] an argument route may require an explicit `Batchy.Skill.Flag`, permit conversational extraction, declare a default, or combine the permitted resolution paths ^c20260731-7u
- [CT] successful resolution identifies exactly one canonical `Skill.Arg` and validates its value against the argument’s contract ^c20260731-7u
- [DC] the routed effect ends at data binding; behavior may subsequently consume the bound value ^c20260731-7u

****

## Batchy.Router/Skill.Module

- [DF] `Batchy.Router/Skill.Module` is the integration through which `Batchy.Router` selects and loads a `Skill.Module` ^c20260731-7u
- [CT] module selection may resolve from an explicit `Batchy.Skill.Flag`, the live conversation, or a `Routing.Table` ^c20260731-7u
- [CT] successful resolution identifies the module targets permitted by the applicable selection contract ^c20260731-7u
- [DC] resolving the route loads the selected module without requiring a `Skill.Arg` binding ^c20260731-7u
- [PR] routing addressable modules provides progressive disclosure without reducing the skill’s capability surface ^c20260731-7u
