import agent
import random
from NSAModule import NSAModule
from NSAModule import Predicate

class NSACivilian(agent.Civilian):
	def __init__(self, system, name, nsa_elements = {}, capacityOfMemory = 30):
		agent.Civilian.__init__(self, system, name)
		self.nsa = NSAModule.NSAModule(nsa_elements)
		self.facts = [Predicate.Predicate("is", [name])]
		self.capacityOfMemory = capacityOfMemory
		
	def step(self):
		self.nsa.generateRandomRules(1000)

		self.system.add_resource(self, 'A', 6)
		#for rule in self.nsa.getRules():
		#	print str(rule)
		#print "\n\n"
		
		self.nsa.removeInconsistentRules(self.name, self.system.list_of_names, self.facts)
		if len(self.nsa.getRules()) > 0:
			print self.name, len(self.nsa.getRules())
		
		
	def acknowledge(self, effects):
		self.facts.extend(effects)
		
		if len(self.facts) > self.capacityOfMemory:
			tmp = [Predicate.Predicate("is", [self.name])]

			for i in range (len(self.facts) - self.capacityOfMemory, len(self.facts)):
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