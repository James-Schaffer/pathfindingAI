class CELL_STATES:
	DEFAULT = 0
	EMPTY = 1
	BLOCKED = 2

class Cell:
	def __init__(self, location: tuple[int, int]):
		self._location = location
		
		self._state = CELL_STATES.DEFAULT
		self._color = (255,0,0)

	@property
	def location(self):
		return self._location
	
	@property
	def state(self):
		return self._state
	
	@property
	def color(self) -> tuple[int, int, int]:
		return self._color
	
	@color.setter
	def color(self, val: tuple[int, int, int]):
		self._color = val

	def setState(self, state):
		match (state):
			case CELL_STATES.DEFAULT:
				self._state = state
				self._color = (255,0,0)
			case CELL_STATES.EMPTY:
				self._state = state
				self._color = (255,255,255)
			case CELL_STATES.BLOCKED:
				self._state = state
				self._color = (0,0,0)
			case _:
				raise ValueError(f"Un-reccognised state {state}")

# DIRECTIONS = [
#     (-1, -1), (0, -1), (1, -1),
#     (-1,  0), (0,  0), (1,  0),
#     (-1,  1), (0,  1), (1,  1),
# ]

DIRECTIONS = [
			  (0, -1),
	(-1,  0), (0,  0), (1,  0),
			  (0,  1),
]

class GridEnvironment:
	def __init__(self, size: tuple[int, int]):
		self._grid = [[Cell((x,y)) for y in range(0, size[1])] for x in range(0, size[0])]
		self._size = size

	@property
	def size(self) -> tuple:
		return self._size
	
	def __getitem__(self, key: int | tuple[int, int]) -> Cell:
		if isinstance(key, tuple):
			if len(key) != 2:
				raise IndexError(f"Expected 2 indices, got {len(key)}")
			x, y = key
			return self._grid[x][y]
		return self._grid[key]
	
	def getAdjacent(self, target: tuple[int, int]) -> set[Cell]:
		return {
			self[(tmp:=(target[0]+x,target[1]+y))] for x,y in DIRECTIONS
				if 0 <= tmp[0] < self._size[0] and 0 <= tmp[1] < self._size[1]
		}
	
	def getAdjacent_empty(self, target: tuple[int, int]) -> set[Cell]:
		filt = lambda x : 0 <= x[0] < self._size[0] and 0 <= x[1] < self._size[1] and self[x].state == CELL_STATES.EMPTY

		return { self[dx,dy] for dx,dy in
			filter(filt, [(target[0]+x,target[1]+y) for x,y in DIRECTIONS])
		}

	def loadMapData(self, data: list[str]) -> None:
		if (len(data)!=self._size[1]) or (len(data[0])!=self._size[0]):
			raise ValueError(f"Data not of size {self._size}")
	
		for y, row in enumerate(data):
			for x, cell in enumerate(row):
				match (cell):
					case '_':
						tmp = CELL_STATES.EMPTY
					case '#':
						tmp = CELL_STATES.BLOCKED
					case _:
						tmp = CELL_STATES.DEFAULT

				self[x,y].setState(tmp)