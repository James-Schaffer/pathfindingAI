from Environment import GridEnvironment
import pygame

class Display:
	def __init__(self, env: GridEnvironment, windowSize: tuple):
		self._windowSize = windowSize
		self._environment = env

		pygame.init()
		self.SCREEN = pygame.display.set_mode((self._windowSize[0], self._windowSize[1]))
		self.SCREEN.fill((0,0,0))

		self._cellSize = (
			int(self._windowSize[0] / self._environment.size[0]),
			int(self._windowSize[1] / self._environment.size[1])
		)

	def redraw(self):
		for x in range(self._environment.size[0]):
			for y in range(self._environment.size[1]):
				px = x * self._cellSize[0]
				py = y * self._cellSize[1]

				rect = pygame.Rect(px, py, self._cellSize[0], self._cellSize[1])
				pygame.draw.rect(self.SCREEN, self._environment[x,y]._color, rect)

		pygame.display.update()