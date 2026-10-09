# Working a Step action

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

A Step action closes one piece of your work into a step: an opening test, the
work, closing tests. Tarav records each run of it. This module says how to
work one; the Action Type's own documentation says what its step is about.
<!-- tarav.breadcrumb 464b694709788c0eed4861abfa91d78dfacab67305da4c05ae7795d77fdf2212 -->

## The loop

1. **Place your input.** A Step takes a typed object from the Operator
   Context. You put it there; the action reads it from there, not from you.

   ```bash
   tarav action types
   tarav operator-context put --type <Input Type> --data '<json fields>' [--project <folder>]
   ```
<!-- tarav.breadcrumb 1287046351f035e96ea77e41d0a6d1027b6978302d4fa90083055b5dcb88fe49 -->

2. **Start.** Tarav takes the input, keeps what it read, and runs the opening
   test. If it does not pass, the run is recorded as closed with an error and
   the reported POIs say why.

   ```bash
   tarav action start --type <Action Type> --context <input id>
   ```

3. **Work.** Do what the step is for. An operation the action offers is done
   through the run, so the write it makes names the run. To change your input
   while working, put it again with its id; each command records the input it
   read.

   ```bash
   tarav operator-context put --id <input id> --data '<json fields>'
   tarav action do --run <run id> --operation <name>
   ```

4. **Close.** Tarav runs the closing tests. The run closes only when they
   pass; otherwise it stays running and the POIs say what is missing. A run
   you will not finish is closed with an error and a reason.

   ```bash
   tarav action close --run <run id>
   tarav action abort --run <run id> --reason '<why>'
   ```
<!-- tarav.breadcrumb a5f7a5c63c1a3e708fb74a6fae7478b672d719bbfa0fbd6f2b3bde50b601fec7 -->

`tarav action list [--state running|closed] [--exit ok|error] [--project <root>]`
shows the runs, and `tarav action show --run <run id>` one full record.

## What to keep in mind

- The tests are Checks. Read their POIs as you read any POI: open the context
  before acting.
- A run may continue in another session. Each session that works on it is
  appended to the run.
- Not all work is an action. Use one where a Project or a Type asks for it.
