import threading

import channel

class Stage(threading.Thread):
	def __init__(self, runnable, inChannel = None, outChannel = None):
		threading.Thread.__init__(self)
		self.lambda = runnable()
		self.inChannel = inChannel or channel.new_channel()
		self.outChannel = outChannel or channel.new_channel()

	def run(self):
		self.run = True
		while start:
			value = inChannel.get()
			return_value = self.lambda.process(value)
			outChannel.put(return_value)

	def stop(self):
		self.run = False

	def inChannel(self):
		return self.inChannel

	def outChannel(self):
		return self.outChannel
