from NSAModule import NSAModule
from Predicate import Predicate
from PredicateMatcher import PredicateMatcher

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
		
nsa = NSAModule(elements)
nsa.generateRandomRules(30)
rules = nsa.getRules()

for rule in rules:
	print rule
	res = rule.proceed(["stefan", "jerry"], [Predicate("killed", ["stefan"])])
	print "\t", str(res)
	
predicate = Predicate("killed", [])
print str(predicate)

predicate = Predicate("killed", ["stefan"])
print str(predicate)

predicate = Predicate("killed", ["stefan", "lidia"])
print str(predicate)

res = PredicateMatcher.match(Predicate("kill", ["john"]), Predicate("kill", ["john"]))
print str(res)

res = PredicateMatcher.match(Predicate("kill", ["john"]), Predicate("kill", ["X"]))
print str(res)

res = PredicateMatcher.match(Predicate("kill", ["john"]), Predicate("Y", ["X"]))
print str(res)

res = PredicateMatcher.match(Predicate("kill", ["john"]), Predicate("kill", ["X", "lol"]))
print str(res)