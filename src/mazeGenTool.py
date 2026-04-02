import random
import sys

# def generate_maze(width, height, start=(0,0), end=None):
#     if end is None:
#         end = (width-1, height-1)

#     # start with all walls
#     grid = [['#'] * width for _ in range(height)]

#     def carve(x, y):
#         grid[y][x] = '_'
#         directions = [(0,2),(0,-2),(2,0),(-2,0)]
#         random.shuffle(directions)
#         for dx, dy in directions:
#             nx, ny = x+dx, y+dy
#             if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == '#':
#                 grid[y+dy//2][x+dx//2] = '_'  # carve wall between
#                 carve(nx, ny)

#     carve(start[0], start[1])

#     # guarantee start and end are open
#     grid[start[1]][start[0]] = '_'
#     grid[end[1]][end[0]] = '_'

#     return ["".join(row) for row in grid]

def generate_maze_prims(width, height):
	grid = [['#'] * width for _ in range(height)]

	def neighbours(x, y, step=2):
		result = []
		for dx, dy in [(0,step),(0,-step),(step,0),(-step,0)]:
			nx, ny = x+dx, y+dy
			if 0 <= nx < width and 0 <= ny < height:
				result.append((nx, ny))
		return result

	# start from (1,1)
	start_x, start_y = 1, 1
	grid[start_y][start_x] = '_'

	walls = neighbours(start_x, start_y)

	while walls:
		wx, wy = random.choice(walls)
		walls.remove((wx, wy))

		# find carved neighbours of this wall cell
		carved = [(nx, ny) for nx, ny in neighbours(wx, wy) if grid[ny][nx] == '_']

		if carved:
			# connect to a random carved neighbour
			cx, cy = random.choice(carved)
			grid[wy][wx] = '_'
			# carve the wall between
			grid[(wy+cy)//2][(wx+cx)//2] = '_'

			# add new unvisited neighbours to walls
			for nx, ny in neighbours(wx, wy):
				if grid[ny][nx] == '#' and (nx, ny) not in walls:
					walls.append((nx, ny))

	# force open start and end
	grid[0][0] = '_'
	grid[0][1] = '_'
	grid[1][0] = '_'
	grid[height-1][width-1] = '_'
	grid[height-2][width-1] = '_'
	grid[height-1][width-2] = '_'

	return ["".join(row) for row in grid]


if __name__ == "__main__":
	args = sys.argv[1:]

	if len(args) == 2:
		x = generate_maze_prims(int(args[0]), int(args[1]))
		
		print(x)
		
		with open("src//tests/Test09.py", "w") as f:
			f.write(f"env_data = {x}")