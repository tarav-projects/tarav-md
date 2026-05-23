# Index Linter - impl-req

## Impl.Abstract

- scope: replace the old `agentos index doctor` implementation with a fresh deterministic `agentos index linter`
- status: implemented
- source context: current chat alignment on linter/doctor split; placeholder `agentos index linter` already exists in `agentos-py`
- target surfaces:
    - `agentos-py/src/agentos/index/`
    - `agentos-py/tests/`
    - `agentos-md/skills/agentos-index-doctor/SKILL.md`
- implementation intent: build the linter as a sequential battery of deterministic checks over configured index and appendix surfaces
- out of scope:
    - semantic diagnosis, placement judgment, stale-design judgment, or conceptual quality review
    - project config files for linter defaults
    - auto-fixes or mutations
    - restoring `agentos index doctor` as a CLI command

## Impl.Index

### Linter.Doctor.Split

- `agentos index linter` is the deterministic CLI surface
- it surfaces findings only: errors, warnings, blocked checks, and summary counts
- `agentos-index-doctor` remains the agentic diagnostic workflow
- the doctor may run the linter first, then add agent judgment on coherence, stale design, coverage gaps, and placement drift
- the CLI must not attempt semantic diagnosis

### Linter.Workflow

- workflow order:
    - config
    - discover files
    - iterate checks sequentially
    - gate each check against current state
    - run allowed checks
    - print findings
    - print summary
    - exit
- default output is human-friendly text
- `--json` emits a structured view derived from the same final state object
- exit code is nonzero when final state contains errors

### Linter.Config

- first configuration surface is CLI options only
- users must explicitly define places to process
- support repeated path options for surface types:
    - `--index PATH`
    - `--appendix PATH`
- each `PATH` may be a markdown file or a directory
- relative paths resolve from the current working directory
- `--root PATH` is a shortcut mode that uses `<root>/index` and `<root>/appendix`
- `--root` cannot be combined with `--index` or `--appendix`
- support `--json` for structured output
- defer persistent project config until the linter checks and output contract stabilize
- avoid positional path guessing in the first implementation because index and appendix paths have different semantics

### Linter.State.Model

- the runner maintains one global linter state object
- all output, human and JSON, is derived from this state
- state records:
    - resolved config
    - discovered files
    - parsed block/router/inventory data as it becomes available
    - findings
    - per-check status: passed, failed, blocked, skipped if later needed
    - summary counts
- checks should append to state only through runner-owned recording helpers
- checks must be deterministic and read-only

### Linter.Check.Gates

- each check has a gate function called before the check runs
- the gate inspects only current linter state
- a blocked gate records the check as blocked with a reason and dependency codes
- blocked checks are counted in final output but not run
- gates prevent cascades such as router-dependent checks producing a wall of derivative errors after router parsing fails
- gate logic handles both hard dependencies and noise-control dependencies

### Linter.Check.Contract

- each check has:
    - stable code
    - human title
    - gate function
    - run function
- each finding has:
    - severity: `error` or `warning`
    - stable code
    - message
    - path
    - optional line
    - optional details map
- runner executes checks in declared order and records status after each check

### Initial.Check.Battery

- first useful checks:
    - configured index and appendix paths exist and are directories
    - markdown/block syntax via existing `mdblocks` APIs
    - router file presence
    - index filename convention
    - concept heading syntax
    - duplicate concept headings across configured index surfaces
    - router covers discovered concept blocks
    - router entries point to real files and blocks
    - appendix filename convention
    - orphan appendix files
- early implementation may ship a smaller vertical slice if it establishes the state, gate, output, and exit contracts end to end

### Output.Contract

- human output should be the default and should be concise
- findings should be grouped or ordered by check/path in a predictable way
- blocked checks should be summarized without noisy detail
- JSON output should include:
    - config
    - check results
    - findings
    - blocked checks
    - summary counts
    - exit status basis
- both output formats must be derived from the same final state object

## Execution.Plan

### Slice 1 - Establish Linter Runner Skeleton

- status: completed
- changes:
    - add linter state, finding, check, and gate result primitives under `agentos-py/src/agentos/index/`
    - replace placeholder command handler with config parsing for `--root`, `--index`, `--appendix`, and `--json`
    - add a minimal check registry with one always-allowed placeholder or surface-existence check
    - implement human and JSON rendering from the same final state
- observable result:
    - `agentos index linter --index <path>` runs through the runner and prints a summary
    - `agentos index linter --json --index <path>` emits structured JSON
- validation:
    - focused CLI tests cover text output, JSON output, and zero/nonzero exit behavior for the first check

### Slice 2 - Add Surface Discovery And Gating

- status: completed
- changes:
    - discover markdown files in configured index and appendix directories
    - record discovered files in state
    - implement gate helpers for missing/invalid surfaces
    - add blocked-check reporting
- observable result:
    - checks depending on valid surfaces are blocked when a configured path is missing
    - final summary counts blocked checks
- validation:
    - tests cover missing index path, missing appendix path, and blocked dependent checks

### Slice 3 - Integrate Mdblocks Syntax Check

- status: completed
- changes:
    - reuse existing `agentos.mdblocks.core` APIs for block parsing/linting
    - map mdblocks lint issues into linter findings
    - preserve stable severity and code fields
- observable result:
    - linter reports block syntax errors and warnings for configured index/appendix paths
- validation:
    - tests cover a malformed block fixture and a clean block fixture

### Slice 4 - Add First Index-Specific Consistency Checks

- status: completed
- changes:
    - build concept inventory from parsed index blocks
    - check router presence
    - check index filename convention
    - check duplicate concept headings
    - check appendix filename convention
    - check orphan appendix files when concept inventory is available
    - check router coverage and route targets when router inventory is available
- observable result:
    - linter reports deterministic index/appendix consistency findings beyond generic mdblocks syntax
- validation:
    - tests use temporary fixture directories for duplicate concepts, missing router, bad appendix name, and orphan appendix

### Slice 5 - Update Doctor Skill And Current References

- status: completed
- changes:
    - update `agentos-index-doctor` if command syntax or output contract changed during implementation
    - update current package maintenance references from old doctor wording to linter + doctor split where appropriate
    - do not rewrite archived/live historical notes unless specifically requested
- observable result:
    - current operational docs direct deterministic checking to `agentos index linter`
    - doctor remains a skill-level diagnosis workflow layered above linter output
- validation:
    - search current skill/package surfaces for stale `agentos index doctor` operational instructions

## Impl.Log

- 2026-05-22: Impl.Req created from chat alignment.
- accepted direction: linter is a deterministic battery of sequential gated checks.
- accepted direction: linter state is the shared source for human output, JSON output, summary counts, and exit behavior.
- accepted direction: CLI options are the first configuration surface; persistent linter config is deferred.
- 2026-05-22: Implemented `agentos index linter` runner with CLI config, shared state, gated sequential checks, text output, JSON output, and nonzero-on-error exit behavior.
- 2026-05-22: Added surface discovery, blocked-check accounting, mdblocks syntax mapping, concept inventory, duplicate concept checks, router presence/entry/coverage/target checks, appendix filename checks, and orphan appendix checks.
- 2026-05-22: Added focused tests for clean output, JSON output, missing surfaces with blocked checks, mdblocks error mapping, duplicate concepts, appendix filename issues, orphan appendix detection, and command handler behavior.
- 2026-05-22: Updated current doctor and package maintenance references so deterministic checking points to `agentos index linter`; `agentos-index-doctor` remains the agentic diagnostic layer.
- 2026-05-22: Adjusted command surface: explicit mode accepts repeated index/appendix files or directories; root shortcut mode uses `<root>/index` and `<root>/appendix` and rejects explicit paths.
