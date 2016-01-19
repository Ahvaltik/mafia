import RuleElement
import random

class Less(RuleElement.RuleElement):
	def __init__(self, elements = None, createPattern = False, variablesBase = None):
		self.variablesBase = variablesBase
		self.createPattern = createPattern
		self.predicates = []
		
		if variablesBase:
			self.predicates.append(random.choice(variablesBase))
			self.predicates.append(random.choice(variablesBase))
	
	def proceed(self, variablesBase, facts):
		try:
			return int(variablesBase[self.predicates[0]]) < int(variablesBase[self.predicates[1]])
		except:
			return False