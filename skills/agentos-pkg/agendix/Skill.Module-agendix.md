****

## Skill.Module/Agendix/Candidate.Context.Assembly.Module

- [DF] a `Context.Assembly.Module` is a `Skill.Module` whose product is a curated context assembly for one coherent scope ^c20260725-17u
- [DC] the assembly gives a consumer's `Builder.Agent` the complete shared context for deriving that consumer surface ^c20260725-17u
- [PR] consumers load the assembly instead of independently gathering its context from sparse index and other project surfaces ^c20260725-17u
- [DC] the assembly declares the package-level source set whose importing it owns ^c20260725-18u
- [DF] `--dev-from` is a dependency role requiring the `Builder.Agent` to load its target as development context ^c20260725-18u
- [DF] `--cite` is a dependency role requiring its target to remain explicitly cited by the generated surface ^c20260725-18u
- [DC] any dependency on a source claimed by a `Context.Assembly.Module` requires a companion `--dev-from` edge to that assembly ^c20260725-18u
- [CT] the companion-edge rule covers every dependency role, including generic `--from`, `--cite`, and future roles ^c20260725-18u
- [PR] a missing companion edge raises a semantic POI because the builder may be using assembly-owned material without its broader context; it does not invalidate the direct dependency ^c20260725-18u
- [CT] dependencies internal to the assembly are exempt from the companion-edge rule ^c20260725-18u
