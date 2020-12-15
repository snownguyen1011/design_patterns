import types


class Strategy:

    def __init__(self, tactic=None):
        self.name = 'possession tactic'
        if tactic is not None:
            self.execute = types.MethodType(tactic, self)

    def execute(self):
        print(self.name)


def attacking_tactic(self):
    print(self.name)


def defending_tactic(self):
    print(self.name)


if __name__ == '__main__':
    initial_tactic = Strategy()
    attack_tactic = Strategy(tactic=attacking_tactic)
    attack_tactic.name = 'attacking tactic'
    defend_tactic = Strategy(tactic=defending_tactic)
    defend_tactic.name = 'defending tactic'

    initial_tactic.execute()
    attack_tactic.execute()
    defend_tactic.execute()
