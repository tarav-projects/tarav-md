****

## Poi.Linter/Agendix

- [DC] dependency-sync POIs come in two kinds: undeclared dependency (mention without declaration) and unhonored dependency (declaration without mention), each suppressible by blessing until the situation changes ^20260716-12 ^20260716-13
- [CT] only backticked `Dotted.Notation` mentions are visible to the check — prose paraphrases stay outside the fence, same deal as the `Line.Type` fence ^20260716-12
- [DC] first activation on an existing surface floods undeclared-dependency POIs; the baseline is a ratchet-style bulk bless, and new mentions after the baseline still flag ^20260716-12
