import NSAModule
import Rule
import Predicate
import Before
import Less
import Exists

nsa = NSAModule.NSAModule({})
nsa.rules = []

rule = Rule.Rule({})
before = Before.Before()
before.predicates = [Predicate.Predicate("day", ["1"]), Predicate.Predicate("killed", ["X"])]
rule.ruleElements = [before]
nsa.rules = [rule]
res = nsa.proceed(["john", "finn"], [Predicate.Predicate("day", ["1"]), Predicate.Predicate("resource", ["finn", "5"]), Predicate.Predicate("killed", ["finn"])])
print res

rule = Rule.Rule({})
before = Before.Before()
before.predicates = [Predicate.Predicate("day", ["1"]), Predicate.Predicate("night_killed", ["X"])]
rule.ruleElements = [before]
nsa.rules = [rule]
res = nsa.proceed(["john", "finn"], [Predicate.Predicate("day", ["1"]), Predicate.Predicate("resource", ["finn", "5"]), Predicate.Predicate("killed", ["finn"])])
print res

rule = Rule.Rule({})
before = Before.Before()
before.predicates = [Predicate.Predicate("day", ["1"]), Predicate.Predicate("killed", ["X"])]
rule.ruleElements = [before]
nsa.rules = [rule]
res = nsa.proceed(["john", "finn"], [Predicate.Predicate("resource", ["finn", "5"]), Predicate.Predicate("killed", ["finn"]), Predicate.Predicate("day", ["1"])])
print res

rule = Rule.Rule({})
exists = Exists.Exists()
exists.predicates = [Predicate.Predicate("day", ["X"])]
exists2 = Exists.Exists()
exists2.predicates = [Predicate.Predicate("resource", ["Z", "Y"])]
rule.ruleElements = [exists, exists2]
nsa.rules = [rule]
res = nsa.proceed(["john", "finn"], [Predicate.Predicate("day", ["1"]), Predicate.Predicate("resource", ["finn", "5"]), Predicate.Predicate("killed", ["finn"])])
print res

rule = Rule.Rule({})
less = Less.Less()
less.predicates = ["X", "Y"]
exists = Exists.Exists()
exists.predicates = [Predicate.Predicate("day", ["X"])]
exists2 = Exists.Exists()
exists2.predicates = [Predicate.Predicate("resource", ["Z", "Y"])]
rule.ruleElements = [less, exists, exists2]
nsa.rules = [rule]
res = nsa.proceed(["john", "finn"], [Predicate.Predicate("day", ["1"]), Predicate.Predicate("resource", ["finn", "5"]), Predicate.Predicate("killed", ["finn"])])
print res

rule = Rule.Rule({})
less = Less.Less()
less.predicates = ["X", "Y"]
exists = Exists.Exists()
exists.predicates = [Predicate.Predicate("day", ["X"])]
exists2 = Exists.Exists()
exists2.predicates = [Predicate.Predicate("resource", ["Z", "Y"])]
rule.ruleElements = [exists, exists2, less]
nsa.rules = [rule]
res = nsa.proceed(["john", "finn"], [Predicate.Predicate("day", ["1"]), Predicate.Predicate("resource", ["finn", "5"]), Predicate.Predicate("killed", ["finn"])])
print res