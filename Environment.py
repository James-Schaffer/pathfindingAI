class CELL_STATES:
	DEFAULT = 0
	EMPTY = 1
	BLOCKED = 2

class Cell:
	def __init__(self, location: tuple[int, int]):
		self._location = location
		
		self._state = CELL_STATES.DEFAULT
		self._color = (255,0,0)

	def setState(self, state):
		match (state):
			case CELL_STATES.DEFAULT:
				self._state = state
				self._color = (255,0,0)
			case CELL_STATES.EMPTY:
				self._state = state
				self._color = (0,0,0)
			case CELL_STATES.BLOCKED:
				self._state = state
				self._color = (255,255,255)
			case _:
				raise ValueError(f"Un-reccognised state {state}")

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