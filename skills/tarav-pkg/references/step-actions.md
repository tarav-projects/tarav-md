# Working a Step action

<!-- tarav.sessions
abd0372d = claude-code:d82f1801-d3f2-4deb-9c95-297028a54b7a @abd0372dd06ffeef10c625e3f68354a234a91e4992b67406f075d93ccb20f4d4
-->

A Step action closes one piece of your work into a step: an opening test, the
work, and one or more exits. Tarav records each run of it. This module says how to
work one; the Action Type's own documentation says what its step is about.
<!-- tarav.breadcrumb 464b69470978 -->

## The loop

1. **Place your input.** A Step takes a typed object from the Operator
   Context. You put it there; the action reads it from there, not from you.

   ```bash
   tarav action types
   tarav operator-context put --type <Input Type> --data '<json fields>' [--project <folder>]
   ```
<!-- tarav.breadcrumb 1287046351f0 -->

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
   tarav action do --id <action id> --operation <name>
   ```

4. **Close.** A step has one or more exits, each with its own tests;
   `tarav action types` lists them and who may take each. You take an exit an
   operator may take. The run closes only when that exit's tests pass;
   otherwise it stays running and the POIs say what is missing. A run you will
   not finish is closed with an error and a reason.

   ```bash
   tarav action close --id <action id> [--exit <name>] [--context <input id>]
   tarav action abort --id <action id> --reason '<why>'
   ```
<!-- tarav.breadcrumb a5f7a5c63c1a -->

`tarav action list [--state running|closed] [--exit <name>] [--project [<folder>]]`
shows the actions, and `tarav action show --id <action id>` one of them.

These commands, and `tarav operator-context`, print a short readable summary
by default. Add `--json` for the full result: every field of a record, every
run of a listing. Both come from the same result, so use `--json` whenever
you read the output with code or need a detail the summary leaves out.
<!-- tarav.breadcrumb 5d6a8a196a06 -->
<!-- tarav.breadcrumb 6fb6efb957cb -->

## The action that follows a POI

A POI is an event. A POI of an actionable Type also spins one action,
`Tarav.Actions.POI.Resolution`, and that action is what stays: raising the same
POI again lands on the same action. It has two closing paths:
<!-- tarav.breadcrumb 2085d9e86061 -->

- `gone` is not yours to take. The action is registered under the Project
  whose checks produce its POI. `tarav status --project` runs that
  Project's checks and hands the results to its actions. A suite of checks
  is a detector, and the signal is gone when a detector that ran no longer
  detects it: the action closes when the suite above its check ran and did
  not report the POI, whether the situation was fixed or the check was
  removed. A container Project asks each child to do the same for itself,
  and a run on a child alone updates the same actions. A situation that
  comes back reopens the same action.
- The status leaves slow suites out, such as a Project's tests, and says
  which. Their actions stay as they are, with the situation `not run`; a
  failed check leaves them with `check failed`. `--all` runs everything: use
  it to see whether a test you fixed closes its action.
- `tarav check --project` only runs the checks, and so does
  `tarav skw skills check`: neither records an action.
<!-- tarav.breadcrumb 1c0f15ed4f14 -->
<!-- tarav.breadcrumb 827356ee59de -->
<!-- tarav.breadcrumb 027aadfc2213 -->
<!-- tarav.breadcrumb 965c0a1dcf5b -->
- `blessed` is yours to take when the POI's Type allows it: the action closes
  although the situation still exists. It needs a reason, and can carry
  `support`, a list of typed references to evidence. Otherwise the attempt is
  refused and says so. The POI is still raised and reported; its action stays
  closed.
<!-- tarav.breadcrumb 619cce68b94c -->
<!-- tarav.breadcrumb bce1d3f2b688 -->

```bash
tarav operator-context put --type Tarav.Blessings.Input --data '{"reason": "<why>", "support": []}'
tarav action close --id <action id> --exit blessed --context <input id>
```

Every closing leaves a typed record on the action's tape (below):
`Tarav.Actions.POI.Gone` names the Project, and `Tarav.Blessings.Blessing`
keeps who blessed, the reason,
the support and the POI as it stood. A Blessing declares assertions that the
scoring system can assess; no score is kept on it.
<!-- tarav.breadcrumb 9642c5c017ef -->
<!-- tarav.breadcrumb 9c6fab8a87d0 -->

An action's status is three separate axes, shown by `tarav action list` and
`tarav context --id <action-id>`: the situation as the last run of the Project's checks
says it (`present`, `absent`, `check failed`, `not run`),
the action (`open`, `closed`), and the closing (`gone`, `blessed`). So a
blessing is never read as a fix: a blessed action usually has its situation
present. `tarav action sweep` closes running actions whose loop-taken exit is
met; it does not take a Project's exit.

An action has a tape (the `tape` entry of its context): the important events
of its life, in order, each an entry of its own Type, appended and never
changed. `Tarav.Actions.Tape.Opened`, `Closed` (its exit and closing record;
an `error` exit has none) and `Reopened` change its status;
`ClosingAttempt` is an operator's or the loop's try at an exit, with its
tests; `Clean` is a repository seen clean. The action's state, exit, times
and current closing are read from the tape, so reopening forgets nothing.
Git keeps every other change of the record.

The suites above an action's checks declare the repositories those checks
read, and each run records their HEAD and whether they were clean. Every
status entry holds that state, and per repository the first clean state
after it is a `Clean` entry. What changed between two of those commits is a
`git diff`. While the last status change has no clean entry, commit and run
the checks again; nothing depends on it, but it is how the action can be
traced back later.

## Testing the action loop

To work on actions with the User, set up test actions on purpose. They are
real actions of the Project, on the live path: the registry, `tarav status`,
the extension and the tape. While `<project>/.tarav/tests/` exists, the
Project's checks include the suite `Tarav.Test.Actions.Fixtures`: each
`*.txt` file whose lines hold `TODO` raises one `Tarav.Test.Actions.MarkerPOI`,
which can be blessed.

```sh
mkdir -p .tarav/tests && printf '*\n' > .tarav/tests/.gitignore
printf 'TODO switch the hall lamp off\n' > .tarav/tests/hall.txt
tarav status --project .
```

Scenarios, each followed by `tarav status --project .`:

- Fix: remove the `TODO` line. The action closes as gone.
- Change: edit the `TODO` line. That is another situation: the old action
  closes as gone and a new one opens.
- Bless: close it with a reason (above) while the line is still there; it
  stays closed. Then remove the line: its situation becomes absent.
- Git: commit the repository and run again; the action's tape gains a
  `Clean` entry.
- Reopen: fix it, then put the same line back. The action reopens; its tape
  keeps the `Closed` entry with the gone record, then `Reopened`.
- End: delete `.tarav/tests/`. Its actions close as gone and stay in the
  registry, like any action.

The `.gitignore` of `*` keeps the fixtures out of Git, so they never make
the repository dirty.

## What to keep in mind

- The tests are Checks. Read their POIs as you read any POI: open the context
  before acting.
- A run may continue in another session. Each session that works on it is
  appended to the run.
- Not all work is an action. Use one where a Project or a Type asks for it.
- Keep the repositories clean when you run the checks: commit, then run.
  `tarav status` names the ones that are not.
