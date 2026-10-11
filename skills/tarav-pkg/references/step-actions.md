# Working a Step action

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

A Step action closes one piece of your work into a step: an opening test, the
work, and one or more exits. Tarav records each run of it. This module says how to
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

4. **Close.** A step has one or more exits, each with its own tests;
   `tarav action types` lists them and who may take each. You take an exit an
   operator may take. The run closes only when that exit's tests pass;
   otherwise it stays running and the POIs say what is missing. A run you will
   not finish is closed with an error and a reason.

   ```bash
   tarav action close --run <run id> [--exit <name>] [--context <input id>]
   tarav action abort --run <run id> --reason '<why>'
   ```
<!-- tarav.breadcrumb a5f7a5c63c1a3e708fb74a6fae7478b672d719bbfa0fbd6f2b3bde50b601fec7 -->

`tarav action list [--state running|closed] [--exit ok|error] [--project <root>]`
shows the runs, and `tarav action show --run <run id>` one full record.

## The action that follows a POI

A POI is an event. A POI of an actionable Type also spins one action,
`Tarav.Actions.POI.Resolution`, and that action is what stays: raising the same
POI again lands on the same action. It has two closing paths:
<!-- tarav.breadcrumb 2085d9e86061e70a452c384d336b71b3f9af5ef90f1ef7d7d0013362476265cc -->

- `gone` is not yours to take. A suite manages the action: the caller of a
  check run names the suite the run belongs to (`tarav check --project` runs
  the Projects suite on a Project), and when a later run of that suite on the
  same target no longer produces the POI, the suite closes the action. A check
  that crashed says nothing, and a partial run closes nothing. A situation
  that comes back reopens the same action.
<!-- tarav.breadcrumb 027aadfc22137c980123791f69cc74cca493ef5c94ecf18a109720e87db9ffb9 -->
<!-- tarav.breadcrumb 965c0a1dcf5be9688c87a38ac8315f2fe42cd6369b033e047efbf898cb96539b -->
- `blessed` is yours to take when the POI's Type allows it: the action closes
  although the situation still exists. It needs a reason, and can carry
  `support`, a list of typed references to evidence. Otherwise the attempt is
  refused and says so. The POI is still raised and reported; its action stays
  closed.
<!-- tarav.breadcrumb 619cce68b94c2a79b76ef55c0bcf5214ace29cddab4587fdd37f0b761351de9f -->
<!-- tarav.breadcrumb bce1d3f2b6889a00adcfbe98b14ef0a59c19ecc5e341f7bedc7142bc063c4f79 -->

```bash
tarav operator-context put --type Tarav.Blessings.Input --data '{"reason": "<why>", "support": []}'
tarav action close --run <action id> --exit blessed --context <input id>
```

Every closing leaves a typed record on the action: `Tarav.Actions.POI.Gone`
names the suite, and `Tarav.Blessings.Blessing` keeps who blessed, the reason,
the support and the POI as it stood. A Blessing declares assertions that the
scoring system can assess; no score is kept on it.
<!-- tarav.breadcrumb 9642c5c017ef07b3bdf8795c0f0b7194f39a4c0207785491b90af22596f1307f -->
<!-- tarav.breadcrumb 9c6fab8a87d0e8ade3bd27911d0b8c1aea8a8f111dd88258810b3c3becd03486 -->

An action's status is three separate axes, shown by `tarav action list` and
the `poi-action` view: the situation the suite last saw (`present`, `absent`),
the action (`open`, `closed`), and the closing (`gone`, `blessed`). So a
blessing is never read as a fix: a blessed action usually has its situation
present. `tarav action sweep` closes running actions whose loop-taken exit is
met; it does not take a suite's exit.

## What to keep in mind

- The tests are Checks. Read their POIs as you read any POI: open the context
  before acting.
- A run may continue in another session. Each session that works on it is
  appended to the run.
- Not all work is an action. Use one where a Project or a Type asks for it.
