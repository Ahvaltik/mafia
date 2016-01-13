import agent
import random
from NSAModule import NSAModule
from NSAModule import Predicate

class NSACivilian(agent.Civilian):
	def __init__(self, system, name, nsa_elements = {}):
		agent.Civilian.__init__(self, system, name)
		self.nsa = NSAModule.NSAModule(nsa_elements)
		self.facts = {Predicate.Predicate("is", [name])}
		
	def step(self):
		self.nsa.generateRandomRules(100)
		self.nsa.removeInconsistentRules(self.name, self.system.list_of_names, self.facts)
		agent.Civilian.step(self)
		
	def acknowledge(self, effects):
		self.facts.extend(effects)
		
	def vote(self):
		res = self.nsa.proceed(self.system.list_of_names, self.facts)
		# znajdz key o najmniejszym value, key bedzie imieniem wytypowanego agenta
		if len(self.system.agents) > 0:
			return random.choice(self.system.agents)
		else:
			return None
	