from __future__ import annotations

from typing import TYPE_CHECKING, override, Optional

from src.settings import settings
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.people.person.scheduler.task.task_type import TaskType

if TYPE_CHECKING:
    from src.simulation.people.person.person import Person
    from src.simulation.simulation import Simulation
    from src.simulation.grid.structure.structure import Structure


class FindSpouse(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation,
                         person,
                         settings.get("find_spouse_priority", 5),
                         TaskType.FIND_SPOUSE)

    @override
    def execute(self) -> None:
        if not self._person.has_spouse():
            for other in self._simulation.get_people():
                if not other.has_spouse():
                    self._person.assign_spouse(other)
                    other.assign_spouse(self._person)

                    # make sure they have the same house
                    if self._person.has_home():
                        other.assign_home(self._person.get_home())
                    else:
                        if other.has_home():
                            self._person.assign_home(other.get_home())
                    break
        # if you have a spouse, or there are no options, finish the task
        self._finished()

    @override
    def _clean_up_task(self) -> None:
        pass

    @override
    def get_remaining_time(self) -> int:
        return 1

    @override
    def get_work_structure(self) -> Optional[Structure]:
        return None
