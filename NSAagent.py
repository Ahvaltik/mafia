import agent
import random
from NSAModule import NSAModule

class NSACivilian(agent.Civilian):
	def __init__(self, system, nsa_elements = {}):
		agent.Civilian.__init__(self, system)
		self.nsa = NSAModule.NSAModule(nsa_elements)
		self.facts = {}
		
	def step(self):
		self.nsa.generateRandomRules(100)
		self.nsa.removeInconsistentRules()
		agent.Civilian.step(self)
		
	def acknowledge(self, effects):
		self.facts.extend(effects)
		pass
		
	def vote(self):
		# TODO chosing agent according to NSA
		if len(self.system.agents) > 0:
			return random.choice(self.system.agents)
		else:
			return None
	