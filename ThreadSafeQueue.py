import threading
from collections import deque

class ThreadSafeQueue:
	def __init__(self):
		self._queue = deque()
		self._lock = threading.Lock()
		self._condition = threading.Condition(self._lock)

	def put(self, x):
		with self._condition:
			self._queue.append(x)
			self._condition.notify()
	
	def get(self, block=True):
		with self._condition:
			if block:
				while not self._queue:
					self._condition.wait()
			else:
				if not self._queue:
					raise Empty()
			return self._queue.popleft()
		
	@property
	def empty(self):
		with self._lock:
			return len(self._queue) == 0