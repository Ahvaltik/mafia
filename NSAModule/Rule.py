import random
import Exists

class Rule:
	'''
		Rule is using following keys in elements:
		-----------------------------------------
		- average_number_of_rule_elements (optional) - is used during generation of rule elements
		- deviation_of_number_of_rule_elements (optional) - is used during generation of rule elements
		- rule_elements_factories (optional) - factories from which will be generated rules elements later - they usually should be objects extended from RuleElement
	'''
		
	def __init__(self, elements):
		self.positive = None
		
		averageNumberOfRuleElements = 2
		if elements.has_key("average_number_of_rule_elements"):
			averageNumberOfRuleElements = elements["average_number_of_rule_elements"]
			
		deviationOfNumberOfRuleElements = 1
		if elements.has_key("deviation_of_number_of_rule_elements"):
			deviationOfNumberOfRuleElements = elements["deviation_of_number_of_rule_elements"]
			
		listOfRuleElementsFactories = [Exists.Exists()]
		if elements.has_key("rule_elements_factories"):
			listOfRuleElementsFactories = elements["rule_elements_factories"]
			
		numberOfElements = averageNumberOfRuleElements + random.randrange(-deviationOfNumberOfRuleElements, deviationOfNumberOfRuleElements+1)
		self.ruleElements = []
		
		variablesBase = ["CandidateName"]
		
		for i in range(numberOfElements):
			self.ruleElements.append(random.choice(listOfRuleElementsFactories).__class__(elements, True, variablesBase))
		
	def setPositive(positive):
		self.positive = positive
		
	def positive():
		return self.positive
	
	def negative():
		return not self.positive
	
	def proceed(self, candidatesNames, facts):
		'''
		Will return dict where keys will be candidates names, and values will be one of following:
		- False
		- dict of variables set for which this rule is true for this facts (it means that it is true)
		'''
		candidateRes = {}
	
		for candidateName in candidatesNames:
			variables = [{"CandidateName": candidateName}]
			for element in self.ruleElements:
				tmp = []
				for variableSet in variables:
					res = element.proceed(variableSet, facts)
					
					if isinstance(res, bool) and res == False:
						variables = False
						break
					
					if isinstance(res, bool) and res == True:
						tmp.append(variableSet)
					
					if isinstance(res, list):
						for resultPiece in res:
							resultPiece.update(variableSet)
							tmp.append(resultPiece)
							
				if variables == False:
					break
				
				variables = tmp
					
			candidateRes[candidateName] = variables
			
		return candidateRes
		
	def __str__(self):
		string = "empty rule"
		
		if len(self.ruleElements) > 0:
			string = str(self.ruleElements[0])
		
			for i in range(1, len(self.ruleElements)):
				string = string + " and " + str(self.ruleElements[i])
		
		return string