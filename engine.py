class Engine:
	def __init__(self, system):
		self.system = system
	
	def start(self):
		while not self.system.finished():
			self.system.step()
	
	def result(self):
		#here print something about winner
		pass