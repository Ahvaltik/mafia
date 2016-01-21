import agent
import random
from NSAModule import NSAModule
from NSAModule import Predicate


class NSACivilian(agent.Civilian):
    def __init__(self, system, name, nsa_elements={}, capacityOfMemory=30, probabilityOfGeneratingResource=0.5,
                 typeOfResource="resource", meanAmountOfResource=3, varianceOfResource=1):
        agent.Civilian.__init__(self, system, name, probabilityOfGeneratingResource, typeOfResource,
                                meanAmountOfResource, varianceOfResource)
        self.nsa = NSAModule.NSAModule(nsa_elements)
        self.facts = [Predicate.Predicate("is", [name])]
        self.capacityOfMemory = capacityOfMemory

    def step(self):
        self.nsa.generateRandomRules(100)

        self.generateResource()

        list_of_names = []
        for agent in self.system.agents:
            list_of_names.append(agent.name)
        self.nsa.removeInconsistentRules(self.name, list_of_names, self.facts)

    # if len(self.nsa.getRules()) > 0:
    # print "\t", self.name, len(self.nsa.getRules())

    def acknowledge(self, effects):
        self.facts.extend(effects)

        if len(self.facts) > self.capacityOfMemory:
            tmp = [Predicate.Predicate("is", [self.name])]

            for i in range(len(self.facts) - self.capacityOfMemory, len(self.facts)):
                tmp.append(self.facts[i])
            self.facts = tmp

    def vote(self):
        list_of_names = []
        for agent in self.system.agents:
            list_of_names.append(agent.name)
        res = self.nsa.proceed(list_of_names, self.facts)
        minVal = -1
        minName = []
        for key in res.keys():
            val = res[key]
            if minVal == -1:
                minVal = val
                minName.append(key)
            elif minVal > val:
                minVal = val
                minName = [key]
            elif minVal == val:
                minName.append(key)

        minName = random.choice(minName)
        for agent in self.system.agents:
            if agent.name == minName:
                return agent
