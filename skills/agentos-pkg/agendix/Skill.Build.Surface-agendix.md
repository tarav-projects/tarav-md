****

## Skill.Build.Surface/Agendix/Built.AGENTS.Surface

- [DF] the engine-owned `.skw/AGENTS.md` (agent guidance for the build surface) is a candidate to become a skw-built artifact — produced and model-maintained, not hardcoded in the engine ^c20260723-19u
- [DC] its source lives once in `agentos-skillware`; each package's `.skw/AGENTS.md` is a `--copy --from` it via `@<id>`, so currency is an ordinary `Skw.Pkg.Dependency` drift check, not a bespoke linter ^c20260724-8u
- [PR] lintability drives the placement: the source can live in `agentos-skillware` because the dependency system already carries its expected content to the check ^c20260724-8u
- [EX] `agentos-skillware`'s own `.skw/AGENTS.md` becomes a copy of what it produces — a self-hosting fixpoint ^c20260723-19u
- [RJ] the current engine-hardcoded stamp is what the direction moves away from — the `agentos-skillware` doctrine still calls it "engine-stamped `AGENTS.md`", a wording left in tension ^c20260723-19u
