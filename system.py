import agent
import random

__author__ = 'Pawel'


class System:

    def __init__(self, n_civilians=100, n_gangsters=10):
        self.agents = []
        self.gangsters = []
        self.resources = {}
        self.polls = []
        self.night_polls = []
        self.deadmen = []
        for i in range(n_civilians):
            self.agents.append(agent.Civilian(self))
        for i in range(n_gangsters):
            self.gangsters.append(agent.Gangster(self))
        self.agents.extend(self.gangsters)
        self.agents = random.sample(self.agents, len(self.agents))

    def add_resource(self, resource_name, number):
        if resource_name in self.resources.keys():
            self.resources[resource_name] += number
        else:
            self.resources[resource_name] = number

    def substract_resource(self, resource_name, number):
        if resource_name not in self.resources.keys():
            return 0
        if self.resources[resource_name] < number:
            result = number - self.resources[resource_name]
            self.resources[resource_name] = 0
            return result
        self.resources[resource_name] -= number
        return number

    def __create_poll(self):
        vote = {}
        results = {}
        max_votes = 0
        best_candidate = None
        for civilian in self.agents:
            vote[civilian] = civilian.vote()
            if vote[civilian] not in results.keys():
                results[vote[civilian]] = 0
            results[vote[civilian]] += 1
            if results[vote[civilian]] > max_votes:
                max_votes = results[vote[civilian]]
                best_candidate = vote[civilian]
        if best_candidate:
            self.agents.remove(best_candidate)
            if not best_candidate.civilian:
                self.gangsters.remove(best_candidate)
            best_candidate.execute()
            self.deadmen.append(best_candidate)
            self.polls.append(vote)

    def __create_night_poll(self):
        vote = {}
        results = {}
        max_votes = 0
        best_candidate = None
        for gangster in self.gangsters:
            vote[gangster] = gangster.vote()
            if vote[gangster] not in results.keys():
                results[vote[gangster]] = 0
            results[vote[gangster]] += 1
            if results[vote[gangster]] > max_votes:
                max_votes = results[vote[gangster]]
                best_candidate = vote[gangster]
        if best_candidate:
            self.agents.remove(best_candidate)
            best_candidate.execute()
            self.deadmen.append(best_candidate)
            self.night_polls.append(vote)

    def step(self):
        print str(len(self.gangsters)) + "/" + str(len(self.agents))
        self.__night_step()
        self.__create_night_poll()
        self.__day_step()
        self.__create_poll()

    def __day_step(self):
        for civilian in self.agents:
            civilian.step()

    def __night_step(self):
        for gangster in self.gangsters:
            gangster.night_step()

    def finished(self):
        return 2 * len(self.gangsters) > len(self.agents) or len(self.gangsters) == 0
