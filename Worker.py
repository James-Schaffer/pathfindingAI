import TaskEnvironment

class Worker:
	def __init__(self):
		pass

	def action(self, taskEnv: TaskEnvironment):
		...

	@property
	def solved(self, taskEnv: TaskEnvironment):
		...