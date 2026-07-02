# Agent.Normal.Model — Appendix

****

## Agent.Normal.Model/Interface

- the impl-free interface of `Agent.Normal.Model`, in Python pseudocode — provider-agnostic; the names are normal sub-models in the `Normal.Model.Namespace`, not implementation classes
- a `Raw.Adapter` (`Agentos.Agent.Adapter`) realizes it; a provider that implements only some capabilities is a `Model.Fragment` of this interface

****

## Agent.Normal.Model/Class

- normalized state bundled with the canonical capabilities; state is shared freely with `Agent.Profile` and `Provider.Instance`

```python
class AgentNormalModel:
    # state
    provider:    ProviderFamily
    account:     AccountRef | None
    home:        Home | None
    model:       ModelId | None
    project_dir: Dir
    env:         Mapping[str, str]

    # capabilities
    def run(self, intent: RunIntent) -> RunResult: ...
    def ping(self)                    -> PingResult: ...
    def profile_check(self)           -> ProfileCheck: ...
    def account_status(self)          -> AccountStatus: ...
```

****

## Agent.Normal.Model/Result.Models

- the argument and result sub-models, themselves part of the `Normal.Model.Namespace`

```python
class RunIntent:
    prompt:           str | None
    argv:             tuple[str, ...]
    model:            ModelId | None
    interaction_mode: Literal["interactive", "non_interactive"]

class RunResult:        exit_code: int; stdout: str | None; stderr: str | None
class PingResult:       ok: bool; model: ModelId; elapsed_ms: int; failure: str | None
class CheckpointResult: id: CheckpointId; passed: bool; reason: str | None
class ProfileCheck:     checkpoints: list[CheckpointResult]; ok: bool
class AccountStatus:    usage: AccountUsageStatus   # → Normalization.Pipeline:Account.Usage.Model
```
