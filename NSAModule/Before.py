import RuleElement
import PredicateMatcher

class Before(RuleElement.RuleElement):
	def __init__(self, elements = None, createPattern = False, variablesBase = None):
		RuleElement.RuleElement.__init__(self, elements, 2, createPattern, variablesBase)
	
	def proceed(self, variablesBase, facts):
		results = []
	
		#for fact in facts:
		#	res0 = PredicateMatcher.PredicateMatcher.match(fact, self.predicates[0], variablesBase)
			
		#	if res == True:
		#		return True
				
		#	if isinstance(res, dict):
		#		results.append(res)
				
		#if len(results) > 0:
			return results
		#else:
		#	return False