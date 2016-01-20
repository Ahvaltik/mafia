__author__ = 'Pawel'
import random


class Civilian:

	def __init__(self, system, name, probabilityOfGeneratingResource = 0.5, typeOfResource = "resource", meanAmountOfResource = 3, varianceOfResource = 1):
		self.name = name
		self.__active = True
		self.system = system
		self.probabilityOfGeneratingResource = probabilityOfGeneratingResource
		self.typeOfResource = typeOfResource
		self.meanAmountOfResource = meanAmountOfResource
		self.varianceOfResource = varianceOfResource
		# TODO declaration of necessary agent resources and knowledge

	def step(self):
		self.generateResource()
		
	def generateResource(self):
		if random.random() < self.probabilityOfGeneratingResource:
			self.system.add_resource(self, self.typeOfResource, str(self.meanAmountOfResource + random.random()*self.varianceOfResource))
		

	def execute(self):
		self.__active = False

	def alive(self):
		return self.__active

	def acknowledge(self, effects):
		# TODO transforming actions of other agents into rules
		pass

	def vote(self):
		# TODO chosing agent according to NSA
		if len(self.system.agents) > 0:
			return random.choice(self.system.agents)
		else:
			return None

	@property
	def civilian(self):
		return True


class Gangster(Civilian):
	def step(self):
		self.generateResource()

	def night_step(self):
		pass

	def night_vote(self):
		if len(self.system.agents - self.system.gangsters) > 0:
			return random.choice(self.system.agents - self.system.gangsters)
		else:
			return None

	@property
	def civilian(self):
		return False
