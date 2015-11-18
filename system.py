import agent
import random

__author__ = 'Pawel'


class System:

    def __init__(self, n_civilians=100, n_gangsters=10):
        self.agents = []
        self.gangsters = []
		self.deadmen = []
        for i in range(n_civilians):
            self.agents.append(agent.Civilian(self))
        for i in range(n_gangsters):
            self.gangsters.append(agent.Gangster(self))
        self.agents.extend(self.gangsters)
        self.agents = random.sample(self.agents, len(self.agents))
    
    def add_resource(self):
        pass

    def substract_resource(self):
        pass

    def create_poll(self):
        pass

    def create_night_poll(self):
        pass
        
    def step(self):
        self.night_step()
        self.day_step()

    def day_step(self):
        for civilian in self.agents:
            civilian.step()

    def night_step(self):
        for gangster in self.gangsters:
            gangster.night_step()

    def finished(self):
        pass