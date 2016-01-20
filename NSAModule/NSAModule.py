import Rule

class NSAModule:
	def __init__(self, elements):
		self.elements = elements
		self.rules = []
		
	def generateRandomRules(self, no):
		for i in range(no):
			self.rules.append(Rule.Rule(self.elements))
		
	def removeInconsistentRules(self, candidateName, candidatesNames, facts):
		newRules = []
		for rule in self.rules:
			notTrueForAll = False
			trueForSome = False
			res = rule.proceed(candidatesNames, facts)
			if res[candidateName] != False:
				for key in res.keys():
					if res[key] == False:
						notTrueForAll = True
					if res[key] != False and key != candidateName:
						trueForSome = True
					if notTrueForAll and trueForSome:
						newRules.append(rule)
						break
			
		self.rules = newRules
		
	def getRules(self):
		return self.rules
		
	def proceed(self, candidatesNames, facts):
		res = {}
		for candidateName in candidatesNames:
			res[candidateName] = 0
			
		for rule in self.rules:
			result = rule.proceed(candidatesNames, facts)
			for key in result.keys():
				if result[key] != False:
					res[key] = res[key] + 1
					
		return res