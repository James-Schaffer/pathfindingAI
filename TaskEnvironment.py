from Environment import GridEnvironment, Cell

class TaskEnvironment:
	def __init__(self, environment: GridEnvironment, start: Cell, goal: Cell):
		self.environment = environment

		self.start = start
		self.goal = goal

