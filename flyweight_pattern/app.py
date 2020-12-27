import json
from typing import Dict

class Flyweight:

    def __init__(self, shared_state):
        self._shared_state = shared_state

    def operation(self, unique_state):
        shared = json.dumps(self._shared_state)
        unique = json.dumps(unique_state)

        print(f"Flyweight: Displaying shared ({shared}) and unique ({unique})", end="")


class FlyweightFactory:

    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights):
        for state in initial_flyweights:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state):
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state):
        key = self.get_key(shared_state)

        if not self._flyweights.get(key):
            self._flyweights[key] = Flyweight(shared_state)
            print('Creating a new flyweight')
        else:
            print('Reusing the existing flyweight')

        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print(f"I have {count} flyweights")
        print("\n".join(map(str, self._flyweights.keys())), end="")



def add_car_to_database(factory, plates, owner, brand, model, color):
    print('\nI am adding a car to the database')
    flyweight = factory.get_flyweight([brand, model, color])

    flyweight.operation([plates, owner])


if __name__ == '__main__':

    factory = FlyweightFactory([
        ["Toyota", 'Model1', 'pink'],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"]
    ])

    factory.list_flyweights()

    add_car_to_database(factory, "XYZ", "James Doe", "BMW", "M5", "red")
    add_car_to_database(factory, "XYZ", "James Doe", "BMW", "X1", "red")
    add_car_to_database(factory, "XYZ", "James Doe", "BMW", "X1", "red")

    factory.list_flyweights()