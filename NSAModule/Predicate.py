class Predicate:
	def __init__(self, name, args):
		self.name = name
		self.args = args
		
	def __str__(self):
		res = self.name + "("
		try:
			res = res + self.args[0]
		
			for i in range(1, len(self.args)):
				res = res + ", " + self.args[i]
		
		except:
			pass
			
		res = res + ")"
		
		return res