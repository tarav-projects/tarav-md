# Batchy.Skill — Appendix

****

## Batchy.Skill/Skill.Module

- in a `Batchy.Skill`, a `Skill.Module` is a named, on-demand-loadable part — a file or section, loaded by mentioning its name (progressive disclosure made addressable)
- it generalizes the subcommand — any sub-file or section is an implicit module, activatable without a declared argument
- a `Skill.Arg` carrying an `action` is the optional formal front for a module — for help text, parameters, or selector-exclusivity
- placement is `Natural.Placement` — an inline section, a skill-root file, or a `references/` file, never a mandated subfolder
- the agent resolves loose mentions (`--examples`, `examples`, `EXAMPLES`) to the canonical module name; arg, file, and section names share one collision-free resolution space
