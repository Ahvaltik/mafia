__author__ = 'Pawel'
import random


class Civilian:

	def __init__(self, system, name):
		self.name = name
		self.__active = True
		self.system = system
		# TODO declaration of necessary agent resources and knowledge

	def step(self):
		pass

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
		#self.system.add_resource(self, 'A', 5)
		pass

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
