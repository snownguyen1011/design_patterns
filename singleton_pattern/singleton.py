class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()

        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception('This class is a singleton, cannot instantiate another')
        else:
            Singleton.__instance = self


if __name__ == '__main__':
    s = Singleton.get_instance()

    print(s)

    s = Singleton.get_instance()

    print(s)
