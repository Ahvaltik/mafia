import RuleElement
import PredicateMatcher

class Before(RuleElement.RuleElement):
	def __init__(self, elements = None, createPattern = False, variablesBase = None):
		RuleElement.RuleElement.__init__(self, elements, 2, createPattern, variablesBase)
	
	def proceed(self, variablesBase, facts):
		results = []
	
		for i in range(len(facts)-1):
			res0 = PredicateMatcher.PredicateMatcher.match(facts[i], self.predicates[0], variablesBase)
			
			if res0 == True:
				for j in range(i+1, len(facts)):
					res1 = PredicateMatcher.PredicateMatcher.match(facts[j], self.predicates[1], variablesBase)
					if res1 == True:
						return True
					elif isinstance(res1, dict):
						result.append(res1)
				
			if isinstance(res0, dict):
				for j in range(i+1, len(facts)):
					res1 = PredicateMatcher.PredicateMatcher.match(facts[j], self.predicates[1], variablesBase)
					if res1 == True:
						result.append(res0)
					elif isinstance(res1, dict):
						res0.extend(res1)
						result.append(res0)
				
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