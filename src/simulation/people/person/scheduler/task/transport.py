from typing import override, Optional

from src.simulation.grid.structure.store.store import Store
from src.simulation.grid.structure.structure import Structure
from src.simulation.grid.structure.structure_type import StructureType
from src.simulation.people.person.backpack import Backpack
from src.simulation.people.person.person import Person
from src.simulation.people.person.scheduler.task.task import Task
from src.simulation.simulation import Simulation


class Transport(Task):
    def __init__(self, simulation: Simulation, person: Person) -> None:
        super().__init__(simulation, person, 5)
        self._backpack: Backpack = self._person.get_backpack()
        
        self._store_structure: StructureType = StructureType.BARN

        self._what_resource: Optional[str] = None
        self._resource: Optional[int] = None
        self._store: Optional[Store] = None

    @override
    def execute(self) -> None:
        if not self._backpack.has_items():
            self._finished()
            return
        if self._resource:
            if self._store:
                self._store.add_resource(self._what_resource, self._resource)
                self._what_resource = None
                self._resource = None
                self._store = None
                self._finished()
            else:
                self._store: Optional[Store] = self._person.move_to_workable_structure(self._store_structure)
        else:
            self._what_resource = self._backpack.what_resource()
            amount = self._backpack.get_resource(self._what_resource)
            self._resource = self._backpack.remove_resource(self._what_resource, amount)

    @override
    def _clean_up_task(self) -> None:
        if self._what_resource and self._resource:
            self._backpack.add_resource(self._what_resource, self._resource)
            self._what_resource = None
            self._resource = None
            self._store = None
    
    @override
    def get_remaining_time(self) -> int:
        return 3

    @override
    def get_work_structure(self) -> Optional[Structure]:
        return self._store
