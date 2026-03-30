from Worker import Worker
from TaskEnvironment import TaskEnvironment
from Environment import GridEnvironment
from Display import Display

import pygame
import sys


def test01():
	env_data = [
		"#######",
		"#___#_#",
		"#_###_#",
		"#___#_#",
		"#_#_#_#",
		"#_#___#",
		"#######",
	]


	environment = GridEnvironment((7,7))
	environment.loadMapData(env_data)

	task = TaskEnvironment(environment, environment[1,1], environment[6,6])
	agent = Worker()

	disp = Display(environment, (400, 400))
	disp.redraw()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

	itt = 0

	# while (itt < 100 and not agent.solved):
	# 	...



if __name__ == "__main__":
	test01()