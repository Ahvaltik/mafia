from Predicate import Predicate
import random
import math

class RuleElement:
	'''
		RuleElement is using following keys in elements:
		------------------------------------------------
		- possible_predicate_names
		- possible_predicates_args
		- predicates_data - which should be dict with predicates names as keys, where value is dict with key amount_of_args
		
		Example:
		--------
		elements ={
			"possible_predicate_names":
				["killed", "dead", "alive"], 
			"possible_predicates_args":
				["stefan", "jerry"], 
			"predicates_data":{
					"killed":{
						"amount_of_args": 1
						}
				}
			}
	'''

	def __init__(self, elements = None, amountOfPredicates = 0, createPattern = False, variablesBase = None):
		self.elements = elements
		self.predicates = []
		predicateNameVariablesBase = []
		
		if elements:
		
			for i in range(amountOfPredicates):
				predicatesArgs = []
			
				if createPattern and random.random() < 0.0:
					if predicateNameVariablesBase and random.random() < 0.6:
						predicateName = "P" + str(random.randrange(0, len(predicateNameVariablesBase) + 1))
					else:
						predicateName = "P" + str(len(predicateNameVariablesBase))
						predicateNameVariablesBase.append(predicateName)
				else:
					predicateName = random.choice(elements["possible_predicate_names"])
			
				try:
					amountOfArgs = elements["predicates_data"][predicateName]["amount_of_args"]
				except:
					amountOfArgs = 2
					
				amountOfVariableArgs = 0
				amountOfNewlyCreatedVariables = 0
				
				if createPattern:
					if amountOfArgs < 3:
						amountOfVariableArgs = amountOfArgs #= random.randint(math.ceil(amountOfArgs/2), amountOfArgs)
						amountOfNewlyCreatedVariables = random.randint(math.ceil(amountOfVariableArgs/2), amountOfVariableArgs)
					else:
						amountOfVariableArgs = int(amountOfArgs * random.gauss(1, 0))
						amountOfNewlyCreatedVariables = int(amountOfVariableArgs * random.gauss(0.3, 0.2))
					
					for i in range(len(variablesBase), len(variablesBase) + amountOfNewlyCreatedVariables):
						predicatesArgs.append("V" + str(i))
						variablesBase.append("V" + str(i))
						
					for i in range(amountOfVariableArgs - amountOfNewlyCreatedVariables):
						predicatesArgs.append(random.sample(variablesBase, 1)[0])
					
				predicatesArgs.extend(random.sample(elements["possible_predicates_args"], amountOfArgs - amountOfVariableArgs))
				random.shuffle(predicatesArgs);
			
				self.predicates.append(Predicate(predicateName, predicatesArgs))
		
		
	def factory(self):
		return elements == None
	
	def proceed(self, variablesBase, facts):
		'''
		This function should be implemented in child class or RuleElement.
		It should return one of following:
		- True (if exists exact match)
		- False (if it is impossible to match for any values of variables)
		- list of variables sets (dicts) for which it would be true
		'''
		pass
		
	def __str__(self):
		res = self.__class__.__name__ + "("
		
		try:
			res = res + str(self.predicates[0])
			
			for i in range(1, len(self.predicates)):
				res = res + ", " + str(self.predicates[i])
			
		except:
			pass
		
		res = res + ")"
		return res