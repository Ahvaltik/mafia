__author__ = 'Pawel'


class Civilian:
    def __init__(self, system):
        self.__active = True

    def step(self):
        pass

    def execute(self):
        self.__active = False

    def alive(self):
        return self.__active

    def acknowledge(self, effects):
        pass

    def vote(self):
        pass

    @property
    def civilian(self):
        return True


class Gangster(Civilian):
    def night_step(self, system):
        pass

    def night_vote(self):
        pass

    @property
    def civilian(self):
        return False
