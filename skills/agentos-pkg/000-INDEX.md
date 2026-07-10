# Agentos Index

> `Appendix.Discovery`: for depth on any concept, check `appendix/Concept.Name-appendix.md`

- public index router

## Routing

- `design/100-design.md` — Stable.Surface, Stable.Md.Surface, Natural.Placement, Natural.Placement:Skills, Placement.Balance, Reference.Implementation, Cited.Duplication, Surface.Link.Directionality[+1], Chat.Surface[+1], Chat.Grounding, Grounding.Audit, Index.Grounding, Chat.Surface.Closure, Agentos.Live.Note, Parking.Note, Agentos.Live.Script, Agentos.Index.Notes, Index.Concept.Coverage, Index.Block[+1], Appendix.Block, Design.Block[+1], Md.Surface, Dotted.Notation[+1], Dotted.Parameterized.Notation, File.Numbering.Protocol[+1], Maintenance.System, Index.Editor.Maintenance.Pass, Agentos.Project, Dot.Agentos.AGENTS.File
- `design/101-design.md` — Project.Discovery.System, Agentos.Skills, Usage.Surface, Package.Skill, Package.Driver, Package.Driver.Base, Package.Driver.Router, Context.Loading.Path, Agentos.AGENTS.Section, Cold.Loading, Cold.Loading.Hook, Cold.Loading.Surface, SKILL.Loading, Dynamic.Loading, Package.Aux.Skill, Workflow.Neutral.Skill, Package.Skill.Index, Package.Manifest, Project.Manifest, Package.Skill.Install, Packages.Master.Agent[+1], Multi.Package.Operation, Package.Agent, Aux.Workflow.Skill, Skill.Explicit.Args, Skill.Source, Skill.Export.Package, Skill.Profile, Skill.Depot, Selected.Skills, Imported.Skills, Batchy.Skill[+1], Batchy.Skill.Template, Batchy.Skill.Contract, Skill.Arg, Skill.Arg.Section, Skill.Index.Section, Batchy.Skill.Help, Skill.Module, Batchy.Skill.Banner
- `design/102-design.md` — Alignment.Loop, Alignment.User.Turn, Alignment.Maintenance.Turn, Alignment.Backend, Hard.Evidence, We.Distrust.Summaries, Alignment.Session, Impl.Req[+1], Gr.Req, Development.Principles[+1], Dependency.Profile.Split, Deep.Modules, Agent.Navigable.Codebase, Vertical.Slice, No.Legacy.Allowed, No.Regression.Tests.Allowed, Test.At.Boundaries, Design.Target.Model, Current.Implementation, Progress.Gradient, Design.Implementation.CoEvolution, Kernel.Writing[+1], Kernel.Block, Kernel.Block.Section, Kernel.Block.Meta, Kernel.Block.Fundamentals, Kernel.Block.Appendix
- `design/103-design.md` — Index.Chapter[+1], Index.Appendix, Surface.Concept, Surface.Types, Block.Path[+1], Explicit.Namespace, Agentos.Index.System[+1], Spec.Hardness, Concept.Hardness, Hugentic.Concept, Index.Router, Inline.Relatedness, File.Mention, Project.Surfaces, Project.Dev.Install, Index.Skillware
- `design/104-design.md` — Project.File.Index, Unresolved.Index.Name, BuiltIn.Namespace, Project.Index.Skill, Concept.Cite, Appendix.Discovery[+1], Index.Pages, Placement.Heuristic, Install.Skill, Index.Empirical.Placement[+1], Alignment.Surface, Index.Depot, Agent.Profile[+1], Provider.Instance, Linked.Home, Agentos.Agent.Adapter, Agent.Normal.Model[+1], Normalization.Pipeline:Account.Usage.Model, Harness.Injected.ENV[+1], Config.Injected.ENV[+1], Index.Linter[+1], Edit.Trigger.Gated, Content.Verbatim.Gated, Kernel.Note, Account.Management[+1]
- `design/105-design.md` — Kernel.Block.Grounding[+1], Inline.Grounding[+1], Context.Hook, Index.AGENTS.MD, Appendix.AGENTS.MD, Grounding.Retrieval.Boundary[+1], Chat.Grounding.Target.Block[+1], Grounding.Hugentic.Authority[+1], Designer.Turn.Kernel.Form, RED.GREEN.Test.Suite, Alignment.Mode, Alignment.Checkpoint, Alignment.Checkpoint:Readiness, Alignment.Checkpoint:Executable, Name.As.Index, Not.A.Wall.Of.Text, Independent.Reader.Block[+1], Dangling.Cite
- `design/106-design.md` — What.Design.Session, Alignment.Loop:What[+1], Design.Status.Report, Alignment.Loop.Interruptions, Alignment.Backend:InChat:What, Alignment.Backend:Artifact:What, Forward.Alignment, Internal.Alignment, Hugentic.Alignment, Design.Space, User.Touched, Touched.Space, Untouched.Space, Open.Space, Line.Type, Line.Type.Vocabulary[+1], Line.Type:DF, Line.Type:DC, Line.Type:CT, Line.Type:RJ, Line.Type:PR, Line.Type:FR, Line.Type:EX, Line.Type:GR, Design.Variable, Hugentic.Variable, Agentic.Variable, Alignment.Loop:How, Alignment.Loop:Exec, Alignment.Loop.Gradient, Program.Hardness, Soft.Program, Agentic.Program, CPU.Program, Supervisor.Agent, Normalization.Pipeline[+1], Comparative.Normalization[+1], Fuzzy.Dotted.Name, General.Avoids.Specific
- `design/107-design.md` — Agentos.Skillware, Skill.Runnable.Surface, Skill.Build.Surface[+1], Skill.Package.Builder, Derivation.Rule, Derived.Content, Module.Import, Import.Management, Derived.Module, Skillware.Recipe, Semantic.Router[+1], Usage.Pattern.Routing[+1], Specified.By.Precedence, Index.Main, Index.Surface, Index.Discovery, Block.Line.Gradient, Appendix.Default.Block, Writing.Friction.Reduction[+1], Index.Agendix, Capture.Offer, Concept.Explosion, Tail.Capture, Kernel.Line[+1], Index.Edit.Action, Index.Edit.Create.Block, Index.Edit.Append.Line, Index.Edit.Modify.Line, Index.Edit.Revise.Block, Partial.Cite, Context.Grounding, Index.Linking, Index.Enrichment, Git.Dating, Anchory.System[+1]

## File System

```
AGENTS.md                         — project-root agent instructions
notes/
├── index/                        — local index layer (points to public)
├── appendix/                     — local appendix (project-specific depth)
├── live/                         — active work: design sessions, TODOs, issues
├── canvas/                       — visual collaboration surfaces
└── index-migration/              — archived pre-flat-index files
skills/
├── agentos-pkg/                  — Agentos core package skill
│   ├── 000-INDEX.md              — public index router (concept → chapter file)
│   ├── design/                   — public index chapter (flat numbered files)
│   ├── appendix/                 — public appendix (concept-named depth)
│   ├── references/               — operational detail (runtime, syntax, gating)
│   └── testing/                  — index runtime tests
├── agentos-index/                — workflow-neutral aux skill for Agentos Index functions
├── agentos-hugentics/            — hugentic harness entry point
├── agentos-pkg/                  — Agentos core package orientation
├── agentos-project-doctor/       — project health diagnosis
└── (33 skills total)             — see skills/ for full listing
dev/                              — development scripts and tooling
```
