# Explain Me

```text
tarav-hugentics --explain-me [TOPIC]
```

Explain a topic to the User: find what the User last discussed about it, then
explain it from first principles.
Without TOPIC, explain what the most recent Agent message is about.

The topic can be anything the User asks about: a component, a design
decision, an Agent report, a finding. No kind of topic is special. A POI is
a typical example, not a distinct object of this workflow; like any topic,
the Agent must understand what it is about before it can explain it.

Agents implement most of the system, so the User's knowledge of it is
partial. Agent reports tend to carry situation-specific detail without the
context needed to read them. Grounding contextualizes the Agent; Explain Me
contextualizes the User by linking the topic to conversations the User
already had.

## Workflow

1. Identify the topic and restate it in one line. Ask when materially
   different topics remain plausible.
2. Understand the topic yourself first. Inspect the code, notes, or evidence
   behind it until you can explain it without its situation-specific jargon.
3. Decompose it into the concepts, components, and decisions the User needs
   to follow it. Keep only load-bearing ones.
4. Find what the User last discussed about the topic and each concept, in
   User.Touched.Data. Search the cheapest paths first:
   - Project.Wiki Notes and live-note Impl.Reqs that define it; follow their
     Breadcrumbs (`tarav breadcrumbs show --label <id> --json`) to the cited
     User Turns;
   - Chatlas sessions where the concept appears in User Turns (see
     `tarav chatlas query --help`);
   - Git commits carrying commit evidence.

   Read the User Turn itself before citing it. Prefer the most recent Turn
   where the User introduced, decided, corrected, or reacted to the concept.
5. Classify each concept:
   - **User-anchored**: a User Turn introduced, decided, or reacted to it;
   - **Agent-introduced**: only Agent text, code, or notes support it. Say so
     plainly; this is a finding, not a failure;
   - **Unknown**: the search was inconclusive within budget.

## Presentation

Present in this order:

1. **What you already know**: each anchor with its date, the User's own words
   in short (quotation marks only for exact retained text), and a locator such
   as a Wiki Note, an Impl.Req number, or a short session id.
2. **What changed since**: what Agents built or decided on top of it, marking
   Agent-introduced concepts.
3. **The point**: the topic explained from first principles, building on
   those anchors.
4. **Ask**: what the User needs to decide, if anything. Omit when nothing.

Be economical. Aim for about 15 lines and stay under about 30 unless the User
asks for more. Prefer the User's vocabulary to internal identifiers; introduce
an identifier only when the User will need it. End with at most three
expansion handles, such as "ask about X".

## Boundary

Explain Me is read-only. It writes nothing to the Wiki, Diagram, Breadcrumbs,
or Git. When an explanation deserves retention, the User can follow it with
`--capture --wiki` or `--design --dialogue --wiki`.

A cited User Turn locates context; it does not claim the User endorsed later
implementation. Do not invent consensus or present Agent proposals as User
decisions.

