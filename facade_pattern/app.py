from __future__ import annotations


class Facade:

    def __init__(self, subsystem1, subsystem2):
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()

    def operation(self):
        results = []

        results.append('Initializing subsystems')
        results.append(self._subsystem1.operation_init())
        results.append(self._subsystem2.operation_init())

        results.append('Ordering the subsystems to perform the action:')
        results.append(self._subsystem1.operation_x())
        results.append(self._subsystem2.operation_x())

        return "\n".join(results)


class Subsystem1:

    def operation_init(self):
        return 'Subsystem 1: Initialized'

    def operation_x(self):
        return 'Subsytem 1: Execute Operation X'


class Subsystem2:

    def operation_init(self):
        return 'Subsystem 2: Initialized'

    def operation_x(self):
        return 'Subsytem 2: Execute Operation X'


def client_call(facade):
    print(facade.operation(), end="")


if __name__ == '__main__':
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_call(facade)