from taskEnvironment import TaskEnvironment

class Agent:
	...

class AsAgent(Agent):
	def __init__(self, taskEnv: TaskEnvironment):
		self.position = taskEnv.start.location
		self.goal = taskEnv.goal.location
		self.visited = set()

		self._minCellDist = {}
		self._prev = {}

		self._open = set()

	def move(self, taskEnv: TaskEnvironment):
		percept = taskEnv.environment.getAdjacent_empty(self.position)

		for cell in percept:
			if cell in self.visited:
				continue

			distTo = self._minCellDist.get(self.position, 0) + 1

			if (self._minCellDist.get(cell.location) is None) or (distTo < self._minCellDist[cell.location]):
				self._minCellDist[cell.location] = distTo
				self._prev[cell.location] = self.position

				self._open.add(cell.location)
		
		actions = []

		for cell in self._open:
			if cell not in self.visited:
				actions.append(cell)

		if not actions:
			return None

		action = max(actions, key=lambda k: self.utility(k))

		self._open.remove(action)

		self.visited.add(action)
		self.position = action

		return action		

	def dist(self, a, b):
		return abs(a[0] - b[0]) + abs(a[1] - b[1]) # manhattan dist
		# return max(abs(a[0]-b[0]), abs(a[1]-b[1])) # chebyshev dist

	def utility(self, b):
		gn = self._minCellDist[b]
		hn = self.dist(self.goal, b)

		return -(gn+hn)

	@property
	def solution(self):
		path = []
		current = self.goal
		while current in self._prev:
			path.append(current)

			if (current == self._prev[current]):
				break

			current = self._prev[current]
		path.append(self.position)
		return list(reversed(path))

	@property
	def solved(self) -> bool:
		return self.position == self.goal