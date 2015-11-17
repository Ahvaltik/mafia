__author__ = 'Pawel'


class Civilian:

    def __init__(self, system):
        pass

    def step(self):
        pass

    def alive(self):
        pass

    def acknowledge(self, effects):
        pass

    def vote(self):
        pass


class Gangster(Civilian):

    def night_step(self, system):
        pass

    def night_vote(self):
        pass