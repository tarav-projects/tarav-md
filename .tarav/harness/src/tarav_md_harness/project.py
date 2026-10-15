"""The Project Type of tarav-md, the documentation of Tarav."""

from __future__ import annotations

from tarav.l0.kernel import TaravClass, TypeShip
from tarav.l1.project.workflow import PROJECT_WORKFLOW_SHIP
from tarav.l2.project.dev import DocsProject


class TaravMdProject(DocsProject):
    """tarav-md: the Wiki, the skills and the notes of Tarav."""

    @classmethod
    def class_entity(cls) -> TaravClass:
        return TaravClass(target=cls, id=TypeShip("74e1832e-3d93-4fb8-b0b6-38a1b85c3d22"),
                          name="Taravangian.TaravMdProject", workflow=PROJECT_WORKFLOW_SHIP)
