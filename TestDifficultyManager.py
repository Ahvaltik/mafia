import agent
import NSAagent

class TestDifficultyManager:
	def __init__(self, system, nsa_elements, separability = "medium"):
		self.system = system
		self.nsa_elements = nsa_elements
		self.separability = separability
		self.alreadyUsedNames = -1
		
	def generateName(self):
		self.alreadyUsedNames += 1
		return "a" + str(self.alreadyUsedNames)
		
	def createCivilian(self):
		if self.separability == "hard":
			return agent.Civilian(self.system, self.generateName(), 0.6, "resource", 6, 2)
		elif self.separability == "medium":
			return agent.Civilian(self.system, self.generateName(), 0.6, "resource", 6, 1)
		else:
			return agent.Civilia(self.system, self.generateName(), 0.6, "resource", 6, 1)
		
	def createNSACivilian(self, memorySize):
		if self.separability == "hard":
			return NSAagent.NSACivilian(self.system, self.generateName(), self.nsa_elements, memorySize, 0.6, "resource", 6, 2)
		elif self.separability == "medium":
			return NSAagent.NSACivilian(self.system, self.generateName(), self.nsa_elements, memorySize, 0.6, "resource", 6, 1)
		else:
			return NSAagent.NSACivilian(self.system, self.generateName(), self.nsa_elements, memorySize, 0.6, "resource", 6, 1)
		
	def createGangster(self):
		if self.separability == "hard":
			return agent.Gangster(self.system, self.generateName(), 0.3, "resource", 3, 2)
		elif self.separability == "medium":
			return agent.Gangster(self.system, self.generateName(), 0.3, "resource", 3, 1)
		else:
			return agent.Gangster(self.system, self.generateName(), 0.0)