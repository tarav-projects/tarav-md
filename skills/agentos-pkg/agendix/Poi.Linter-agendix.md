****

## Poi.Linter/Agendix

- [DC] dependency-sync POIs come in two kinds: undeclared dependency (mention without declaration) and unhonored dependency (declaration without mention), each suppressible by blessing until the situation changes ^c20260716-12u ^c20260716-13u
- [CT] only backticked `Dotted.Notation` mentions are visible to the check — prose paraphrases stay outside the fence, same deal as the `Line.Type` fence ^c20260716-12u
- [DC] first activation on an existing surface floods undeclared-dependency POIs; the baseline is a ratchet-style bulk bless, and new mentions after the baseline still flag ^c20260716-12u
