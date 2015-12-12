import Rule

class NSAModule:
	def __init__(self, elements):
		self.elements = elements
		self.rules = []
		
	def generateRandomRules(self, no):
		for i in range(no):
			self.rules.append(Rule.Rule(self.elements))
		
	def removeInconsistentRules(self):
		pass #TODO
		
	def getRules(self):
		return self.rules
		
	def proceed(self, candidatesNames, facts):
		pass #TODO