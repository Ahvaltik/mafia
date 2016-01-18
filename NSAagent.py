import agent
import random
from NSAModule import NSAModule
from NSAModule import Predicate

class NSACivilian(agent.Civilian):
	def __init__(self, system, name, nsa_elements = {}):
		agent.Civilian.__init__(self, system, name)
		self.nsa = NSAModule.NSAModule(nsa_elements)
		self.facts = [Predicate.Predicate("is", [name])]
		
	def step(self):
		self.nsa.generateRandomRules(100)
		self.nsa.removeInconsistentRules(self.name, self.system.list_of_names, self.facts)
		if self.name.startswith('vito'):
			rules = self.nsa.getRules()
			for rule in rules:
				print str(rule)
		agent.Civilian.step(self)
		
	def acknowledge(self, effects):
		self.facts.extend(effects)
		
	def vote(self):
		res = self.nsa.proceed(self.system.list_of_names, self.facts)
		minVal = -1
		minName = ""
		for key in res.keys():
			val = res[key]
			if minVal == -1:
				minVal = val
				minName = key
			elif minVal > val:
				minVal = val
				minName = key

		for agent in self.system.agents:
			if agent.name == minName:
				return agent