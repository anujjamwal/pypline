import Queue

class Channel:
	def __init__(self):
		self.queue = Queue.Queue()

	def get(self):
		return self.queue.get()

	def put(self, value):
		self.queue.put(value)

def new_channel():
	return Channel()