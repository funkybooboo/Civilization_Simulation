from __future__ import annotations

from typing import TYPE_CHECKING

from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.people.person.scheduler.task.work.work import Work

if TYPE_CHECKING:
    from src.simulation.simulation import Simulation
    from src.simulation.people.person.person import Person


class ChopTree(Work):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5, StructureType.TREE, "wood")
