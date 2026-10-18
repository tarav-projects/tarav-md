# Batchy skills

<!-- tarav.sessions
6734aba0 = codex:01a0d86c-9538-7be1-af96-014cd4203d61 @6734aba0b9204f614baf3987604865fa85146495877841244ad7fe1efce4104b
-->

## A callable skill surface

A Batchy.Skill is a skill interpreted by an agent as a callable, CLI-like
surface. The convention organizes invocation and configuration; it does not
require an executable command-line parser or replace agent judgment. This note
captures the Batchy design recovered from the former tarav-pkg index at the
user's request. It does not automatically reinstate every historical rule.
<!-- tarav.breadcrumb 6fc642ec8ed2 -->
<!-- tarav.breadcrumb 1e2ba88d448e -->

## Configuration and routing

The historical design separates a few responsibilities:

- **Batchy.Router** resolves explicit flags, permitted conversational inference,
  and declared defaults into one run configuration.
- **Skill.Arg** describes external run data and its contract; a route binds it.
- **Skill.Module** encapsulates an addressable capability in a file or section;
  a route selects and loads it.
- **Routing.Table** groups routing options, not sequential execution steps.

Explicit configuration takes precedence over inference and defaults. Compatible
contributions compose independently of flag order; incompatible explicit
contributions remain unresolved unless their composition is defined. Missing
required data is not permission to guess. Natural-language invocation remains
valid where the route permits semantic discovery.
<!-- tarav.breadcrumb eb2194eeba24 -->

For example, the current Hugentics call combines three dimensions:

```text
tarav-hugentics --impl --wiki --design
                 │      │       └─ phase
                 │      └───────── knowledge surface
                 └──────────────── workflow
```

These contributions describe one run, not three commands executed in order.
Only the modules needed by that run should be loaded. The current
[Hugentics skill](../../skills/tarav-hugentics/SKILL.md) and its
[Wiki implementation module](../../skills/tarav-hugentics/references/impl/wiki.md)
define the maintained behavior; the historical index explains the broader
compositional design.
<!-- tarav.breadcrumb dca72b7e31a3 -->

## Making interpretation visible

The old convention provides non-executing `--help` that takes precedence over
other flags. For configurable runs, a banner exposes resolved arguments and
routing effects, distinguishing explicit values, defaults, and semantic
inference. The banner informs the user; it is not an approval checkpoint.
Routing can be tested using explicit calls or conversational situations and
their expected destinations. Optional arguments, modules, and sections are
introduced when useful, rather than required as empty scaffolding.
<!-- tarav.breadcrumb 1a5863b5caaa -->

## Historical evidence

The inspected source is Attic Deposit
`e1636df6-0910-40eb-bd64-0aee93b06db2`, directory
`20260826T213706Z-tarav-skills-reboot`, conserved from tarav-md's skills on
2026-08-26. Within its `material/skills/tarav-pkg/`:

- `000-INDEX.md` routes the concepts.
- `design/101-design.md` defines Batchy.Skill, flags, arguments, modules, help,
  the compact contract, and the resolved-run banner.
- `design/107-design.md` defines Batchy.Router, routing rows and tables, and
  usage-pattern routing.
- `appendix/Batchy.Skill-appendix.md` describes router testability.
- `appendix/Batchy.Router-appendix.md` expands argument, module, and namespaced-call routing.

These are recovery hints, not runtime dependencies. The summary above retains
the useful design in the live Wiki; original Attic content remains historical
evidence. Its old inline grounding labels were not independently revalidated
during this inspection. The Breadcrumbs here link the current investigation
and capture request, not blanket user approval of every historical convention.
<!-- tarav.breadcrumb 12e6d114b649 -->
<!-- tarav.breadcrumb 8f1df811eab9 -->

## Batchy as a Skillware extension

The proposed implementation separates general surface production, built-in
skill support, and Batchy as an application of that support. Skill primitives
live under `tarav.l<X>.skw.skills`; Batchy-specific components belong in
`tarav.l<X>.batchy_skills`, not `skw.skills.batchy_skills`. Routing tables are
motivating components of this extension; their exact schema remains open.
This is a proposed organization, not an implemented package tree.
<!-- tarav.breadcrumb 097b87839c87 -->

The foundation is [typed SKW blocks with retained output](skillware.md#typed-surface-components-and-retained-output).
`SkillLink` is a skill component directing an agent to a target, rather than a
generic build dependency. Components may produce their output with deterministic
templates instead of agents; every block still retains its current `output`
in `.skw.json`. Batchy can build its own typed components on this foundation.
<!-- tarav.breadcrumb 78263cadbf97 -->
<!-- tarav.breadcrumb 449b55b20c95 -->
<!-- tarav.breadcrumb 1a2904c300ff -->
