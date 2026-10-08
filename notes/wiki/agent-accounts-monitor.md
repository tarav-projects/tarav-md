# Agent accounts monitor

<!-- tarav.sessions
4d59cf87 = claude-code:d237f00a-2da8-4b96-9b54-a1addd3a5b4e @4d59cf8708efc859c0e9288a51784c98da8592021f8fe020fe298adc78972589
-->

`tarav agent accounts monitor` runs configured workflows from `agent.accounts.monitor` in the Tarav config: `limits-tracking` reads each account's usage limits, `auto-prime-zero-limits` pings accounts, and `account-rotation` keeps credentials materialized.

## Auto-prime pings

The ping should be a simple workflow. The User first framed it as an hourly ping for each working account.
<!-- tarav.breadcrumb 021d6c6f1f68f81e6a087ed4be90a88e13072c313c3ad67a43fe95897063f608 -->

The User then chose to simplify the existing workflow rather than add one. The check frequency is a parameter, preferably 10 minutes. Each check reads the last usage reading and pings when burst usage is below 5%.
<!-- tarav.breadcrumb 350728ccedbabab78ae1d978b0ff39831a250a00a095672982390b0607cac215 -->

The pinged accounts come from an explicit ping configuration rather than everything the monitor shows. Only Claude and Codex accounts are eligible, and individual accounts can be excluded — for example all monitored Claude and Codex accounts except Claude `om`.
<!-- tarav.breadcrumb 743f0a99dcdeb73c1c27df093a2779770a1cd6bf01bea88421cd1edd7a795a17 -->
<!-- tarav.breadcrumb 0d3a932acbe733cfbeef0911c4e259a998c5b076ee383e361fa35c5502e7d179 -->
<!-- tarav.breadcrumb 263d241f6bb32af5c164688438cfe5cb1144415668ed53776e9876ba116239cb -->

Codex pings use Luna (`gpt-6-luna`); the previous `gpt-5.4-mini` default is rejected for ChatGPT-account Codex logins.
<!-- tarav.breadcrumb 625fdc8b396924ee6307fd930c4c75a171b0ec6a73106beae850b1f396562bb1 -->

Open tension: an idle account stays below the threshold after its ping, so it is pinged again at every interval. No repeat guard was requested; a "no repeat within N minutes" guard remains an alternative. Implementation: [Impl.Req 869](../../../tarav-py/notes/live/869-auto-prime-burst-threshold-impl-req.md).
