****

## Skw.Backend/Agendix

- [CT] skw machinery never enters docstrings or other runtime-reachable strings — machinery rides the host's comment carrier only; the docs are part of the generated surface and drift with it ^c20260718-34u
- [DC] a `Skw.Backend` adapter consumes its host's native normal model and emits one common Skillware model for shared machinery ^c20260812-5u
- [CT] on Python code surfaces, only comments classified by the native normalizer as recognized external-system directives bypass `Non.Skw.Annotation`; every other comment outside Skw machinery remains a POI, including inline comments ^c20260812-6u
