"""Index.Line type tournament: which type best classifies this line?

Every match is one index line shown under five different type codes — its
registered one and four drawn from the rest of the vocabulary. The judge ranks
the classifications; the read asks whether the registered type finished on top.

Two things fall out of the same verdicts. Across many lines, a type that keeps
losing on lines that are correctly typed indicts the *type's definition*. A line
that loses while its type wins everywhere else indicts *that line's typing*. One
match separates neither; only the aggregate does.

`control_rate` is 0 deliberately. The engine substitutes a control for one pool
player, and every player in a match here is a variant of one line — a foreign
control would land among four variants of a different line and break the match's
premise. Calibration for this shape has to come from inside `match_players`,
not from the control pool. That is a real limit of the mechanism against
variant-style matches, not an oversight here.
"""

import random

TYPES = ("DF", "DC", "CT", "RJ", "PR", "FR", "EX", "GR")

TYPE_MEANING = {
    "DF": "fixes what a name means",
    "DC": "pins a design variable to one specific value",
    "CT": "bounds a design variable to a subset without picking a value",
    "RJ": "excludes a considered alternative",
    "PR": "orients decisions generatively across several variables",
    "FR": "explicitly declares a variable free for the agent to decide",
    "EX": "illustrates another line's claim with a concrete case",
    "GR": "accounts for what an anchored evidence neighborhood grounds",
}

ARITY = 5

question = (
    "Below are candidate classifications of one index line. Each candidate shows "
    "the same line carrying a different type code, followed by what that code "
    "means. The type is a claim about the act the line performs. Rank the "
    "candidates by how well the code matches what the line actually does."
)

criteria = (
    "A type is valid only if the line performs its act: a bounding code must "
    "actually exclude something, a pinning code must actually fix a value, an "
    "illustrating code must actually illustrate a specific claim elsewhere. Judge "
    "the fit between the act named by the code and the act the sentence performs. "
    "Ignore wording quality, importance, and whether you agree with the line."
)

LINES = {
    "L00": {
        "type": "DC",
        "body": "resolving that conflict on the live index is a separate gated reconciliation action"
    },
    "L01": {
        "type": "PR",
        "body": "by contextualizing prior touched work, the index makes alignment reusable without requiring the user to restate it"
    },
    "L02": {
        "type": "CT",
        "body": "every `Index.Line` is intended to link its dense statement to supporting touch evidence; a missing or unresolvable link is a grounding POI, not loss of index membership"
    },
    "L03": {
        "type": "CT",
        "body": "natural conversation may interrupt or reshape a workflow, but a gated transition remains unresolved until a valid explicit `User.Command`"
    },
    "L04": {
        "type": "RJ",
        "body": "unresolved detail above the floor does not produce parser errors or warnings"
    },
    "L05": {
        "type": "DC",
        "body": "fully composed of conceptual blocks under tight `Kernel.Writing` compression, every one routed by `Index.Router`"
    },
    "L06": {
        "type": "RJ",
        "body": "it does not cover mining a chat corpus for material whose meaning and support have not yet been loaded"
    },
    "L07": {
        "type": "DF",
        "body": "`Skw.Touched.Index` is the `Touched.Surface.Index` member attached to `Skw.Annotation`s: `Index.Line`s riding annotations on generated surfaces — file, module, region, construct"
    },
    "L08": {
        "type": "DC",
        "body": "standing test: the assertion rides next to the content forever; every later pass has a small, local, closed-set claim to check against"
    },
    "L09": {
        "type": "DF",
        "body": "`User.Command.Section` is the section of a skill that declares its `User.Command` blocks"
    },
    "L10": {
        "type": "PR",
        "body": "typing makes the index computable — backward, lint for coherence; forward, agents derive their bounds and freedoms mechanically instead of interpreting prose"
    },
    "L11": {
        "type": "FR",
        "body": "the agent may act on open inference without waiting for additional `User.Touch`"
    },
    "L12": {
        "type": "EX",
        "body": "a `POI.Catalog` is a `Skw.Kernel.Index` application whose `poi` chapter registers `POI.Class` blocks"
    },
    "L13": {
        "type": "PR",
        "body": "it is the only outcome that evaluates the tournament rather than its players"
    },
    "L14": {
        "type": "CT",
        "body": "omitted routing context may be filled only by defaults declared by applicable rows"
    },
    "L15": {
        "type": "RJ",
        "body": "the reference does not encode an absolute path, chapter filename, or package installation layout"
    },
    "L16": {
        "type": "PR",
        "body": "each type creates a validation point: a typed line must perform its act — a constraint line must constrain something; a typed line that performs nothing is mistyped filler"
    },
    "L17": {
        "type": "DF",
        "body": "`User.Command.Trigger` is one accepted `::`-prefixed spelling that invokes a canonical `User.Command`"
    },
    "L18": {
        "type": "PR",
        "body": "growing `Touched.Space` improves the user model by increasing its grounded interaction evidence"
    },
    "L19": {
        "type": "DF",
        "body": "`Usage.Pattern.Routing` is a `Batchy.Router.Row` style whose discovery key describes a usage situation and whose destination describes the response that situation needs"
    },
    "L20": {
        "type": "DF",
        "body": "`Cold.Loading.Hook` is a `Context.Hook` that the harness loads automatically before the agent acts"
    },
    "L21": {
        "type": "DC",
        "body": "storage is depot-scoped and every initial operation receives one explicit `Bloberia.Depot`."
    },
    "L22": {
        "type": "FR",
        "body": "capture may operate over chats already loaded in agent context or mine chats that have not yet been loaded; specializations define the source-access mode"
    },
    "L23": {
        "type": "EX",
        "body": "Chatlas refresh is a job — each run re-ingests only sessions touched since the last run (`chatlas update --since`), keyed off recently active sessions detected at minute granularity"
    },
    "L24": {
        "type": "FR",
        "body": "an agent may use the POI and its hints to discover and verify a relocated resource"
    },
    "L25": {
        "type": "CT",
        "body": "a fixed region is not a decision point for the agent; the agent's job is to recognize and obey the fixed answer"
    },
    "L26": {
        "type": "RJ",
        "body": "resolving one instance does not resolve its class, another instance, or a future occurrence"
    },
    "L27": {
        "type": "RJ",
        "body": "a judge is not told that its match has run before, or what any earlier run decided"
    },
    "L28": {
        "type": "DC",
        "body": "`Line.Verbatim.Gate` is its independently checkable per-`Index.Line` realization"
    },
    "L29": {
        "type": "CT",
        "body": "a row matching policy may require explicit configuration, permit semantic discovery, or accept either resolution path"
    }
}


def _variants(line_id):
    """The five type codes this line is judged under.

    Seeded on the line alone, so repeat runs of one line are the same match and
    accumulate against one identity instead of scattering across type samples.
    """
    registered = LINES[line_id]["type"]
    others = [code for code in TYPES if code != registered]
    picked = random.Random(f"variants:{line_id}").sample(others, ARITY - 1)
    return (registered,) + tuple(picked)


def match_players(ctx):
    """One match per line, cycling once the roster is exhausted."""
    line_id = sorted(LINES)[ctx.match_index % len(LINES)]
    return tuple(f"{line_id}@{code}" for code in _variants(line_id))


def present_player(ctx):
    line_id, code = ctx.player.split("@")
    return (
        f"- [{code}] {LINES[line_id]['body']}\n"
        f"\n"
        f"    [{code}] — a line that {TYPE_MEANING[code]}."
    )


def match_identity(ctx):
    line_id = ctx.players[0].split("@")[0]
    codes = sorted(player.split("@")[1] for player in ctx.players)
    return f"{line_id}:{'+'.join(codes)}"


def verdict_slot(ctx):
    """What the fold needs, recorded per match so the read stays cheap."""
    line_id = ctx.players[0].split("@")[0]
    return {
        "line": line_id,
        "registered": LINES[line_id]["type"],
        "candidates": sorted(player.split("@")[1] for player in ctx.players),
    }
