class PredicateMatcher:
	@staticmethod
	def match(predicate, pattern, variablesBase = None):
		'''As result you will get False - if it is not possible to match them, or True or dict with variables'''
		variables = {}
		
		if PredicateMatcher.isVariable(pattern.name):
			if variablesBase and variablesBase.has_key(pattern.name) and variablesBase[pattern.name] != predicate.name:
				return False
			else:
				variables[pattern.name] = predicate.name
		elif pattern.name != predicate.name:
			return False
			
		if len(predicate.args) != len(pattern.args):
			return False
			
		for i in range(len(predicate.args)):
			if PredicateMatcher.isVariable(pattern.args[i]):
				if variablesBase and variablesBase.has_key(pattern.args[i]) and variablesBase[pattern.args[i]] != predicate.args[i]:
					return False
				else:
					variables[pattern.args[i]] = predicate.args[i]
			elif pattern.args[i] != predicate.args[i]:
				return False
				
		if len(variables) == 0:
			return True
			
		return variables
		
	@staticmethod
	def isVariable(string):
		return string[:1].isupper()