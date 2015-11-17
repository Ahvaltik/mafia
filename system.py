import agent

__author__ = 'Pawel'


class System:

    def __init__(self, n_civilians=100, n_gangsters=10):
        self.agents = []
        self.gangsters = []
        for i in range(n_civilians):
            self.agents.append(agent.Civilian(self))
        for i in range(n_gangsters):
            self.gangsters.append(agent.Gangster(self))
        self.agents.extend(self.gangsters)

    def add_resource(self):
        pass

    def substract_resource(self):
        pass

    def create_poll(self):
        pass

    def create_night_poll(self):
        pass

    def step(self):
        for civilian in self.agents:
            civilian.step()

    def night_step(self):
        for gangster in self.gangsters:
            gangster.night_step()

    def finished(self):
        pass
