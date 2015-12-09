__author__ = 'Pawel'
import random


class Civilian:

    def __init__(self, system):
        self.__active = True
        self.system = system

    def step(self):
        pass

    def execute(self):
        self.__active = False

    def alive(self):
        return self.__active

    def acknowledge(self, effects):
        pass

    def vote(self):
        if len(self.system.agents) > 0:
            return random.choice(self.system.agents)
        else:
            return None

    @property
    def civilian(self):
        return True


class Gangster(Civilian):
    def night_step(self):
        pass

    def night_vote(self):
        if len(self.system.agents - self.system.gangsters) > 0:
            return random.choice(self.system.agents - self.system.gangsters)
        else:
            return None

    @property
    def civilian(self):
        return False
