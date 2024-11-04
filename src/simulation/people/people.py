from src.simulation.people.people_generator import PeopleGenerator


class People:
    def __init__(self, simulation, actions_per_day):
        self._actions_per_day = actions_per_day
        people_generator = PeopleGenerator(simulation)
        self._people = people_generator.generate()

    def print(self):
        for person in self._people:
            print(person)

    def take_actions_for_day(self):
        for action in range(self._actions_per_day):
            for person in self._people:
                person.take_action()

    def age(self):
        for person in self._people:
            person.age()
    