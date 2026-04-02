from agent import Agent, AsAgent
from taskEnvironment import TaskEnvironment
from environment import GridEnvironment
from display import Display
from threadSafeQueue import ThreadSafeQueue

import tests

import threading
import time
import pygame
import sys


class APP_STATES:
	START = 0
	RUNNNING = 1
	PAUSED = 2
	STOPPED = 3

def loadTaskEnvironment(test: tests.test):
	env_size = (len(test.env_data[0]), len(test.env_data))
	_env = GridEnvironment(env_size)
	_env.loadMapData(test.env_data)

	_env[test.end].color = (125,0,0)

	task_env = TaskEnvironment(_env, _env[test.start], _env[test.end])

	return task_env


def runAgent(agent: AsAgent, task_env: TaskEnvironment, updateQueue: ThreadSafeQueue, maxDepth=100):	
	i = 0

	while (i < maxDepth) and (agent.solved is False):
		move = agent.move(task_env)
		#disp.redraw()

		if not move:
			break

		updateQueue.put(move)
		i+=1

		# input()
		# time.sleep(0.01)

	if agent.solved:
		print(f"Solved in {i} moves")

		# path = agent.solution
		# for cell in path:
		# 	updateQueue.put(cell)

		print("HI_")
		#print(agent.solution)
		print(agent._prev)
		print(agent._minCellDist)
		print("_HI")

		updateQueue.put("solved")
		updateQueue.put(agent.solution)

	else:
		print("Failed")

if __name__ == "__main__":
	# args = sys.argv[1:]

	# if sys.argv.get(1) != None:
	# 	print("HI")

	displayUpdateQueue = ThreadSafeQueue()

	task_env = loadTaskEnvironment(tests.Test09)

	disp = Display(task_env.environment, (500, 500))
	disp.redraw()

	agent = AsAgent(task_env)

	appState = APP_STATES.START


	while appState != APP_STATES.STOPPED:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				print("exit")
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.unicode == ' ':
					match (appState):
						case APP_STATES.START:
							print("Starting...")
							threading.Thread(target=runAgent, daemon=True, args=(agent, task_env, displayUpdateQueue, 300000)).start()
							appState = APP_STATES.RUNNNING
						case APP_STATES.RUNNNING:
							#pause
							...
						case APP_STATES.PAUSED:
							#resume
							...
						case _:
							pass


		while (e := displayUpdateQueue.get(block=False)) != None:
			if e=="solved":
				for cell in displayUpdateQueue.get(block=False):
					task_env.environment[cell].color = (0,0,255)

				appState = APP_STATES.STOPPED
				break


			#print(f"e _ {e}")
			task_env.environment[e].color = (0,255,0)

		disp.redraw()


		# keys = pygame.key.get_pressed()

	input("Press enter to exit...")

