import threading

import channel

class Stage(threading.Thread):
	def __init__(self, executor, inbox = None, outbox = None):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.executor = executor()
		self.inbox = inbox or channel.new_channel()
		self.outbox = outbox or channel.new_channel()

	def run(self):
		print("Starting Stage ")
		while True:
			value = self.inbox.get()
			print("Running Stage for ", value)
			return_value = self.executor.process(value)
			self.outbox.put(return_value)	

	def isRunning(self):
		return self.isAlive()
