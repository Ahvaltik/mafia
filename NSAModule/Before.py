import RuleElement
import PredicateMatcher

class Before(RuleElement.RuleElement):
	def __init__(self, elements = None, createPattern = False, variablesBase = None):
		RuleElement.RuleElement.__init__(self, elements, 2, createPattern, variablesBase)
	
	def proceed(self, variablesBase, facts):
		results = []
	
		for i in range(len(facts)-1):
			res0 = PredicateMatcher.PredicateMatcher.match(facts[i], self.predicates[0], variablesBase)
			
			if isinstance(res0, bool) and res0 == True:
				for j in range(i+1, len(facts)):
					res1 = PredicateMatcher.PredicateMatcher.match(facts[j], self.predicates[1], variablesBase)
					if isinstance(res1, bool) and res1 == True:
						return True
					elif isinstance(res1, dict):
						results.append(res1)
				
			elif isinstance(res0, dict):
				tmpVariablesBase = variablesBase.copy()
				tmpVariablesBase.update(res0)
			
				for j in range(i+1, len(facts)):
					res1 = PredicateMatcher.PredicateMatcher.match(facts[j], self.predicates[1], tmpVariablesBase)
					if isinstance(res1, bool) and res1 == True:
						results.append(res0)
					elif isinstance(res1, dict):
						res0.update(res1)
						results.append(res0)
				
		if len(results) > 0:
			return results
		else:
			return False
		
		#for fact in facts:
		#	res0 = PredicateMatcher.PredicateMatcher.match(fact, self.predicates[0], variablesBase)
			
		#	if res == True:
		#		return True
				
		#	if isinstance(res, dict):
		#		results.append(res)
				
		#if len(results) > 0:
		#	return results
		#else:
		#	return False