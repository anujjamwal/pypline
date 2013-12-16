from stage import Stage

class Pipeline:
	def __init__(self):
		self.stages = list()

	def appendStage(self, stage):
		if len(self.stages) == 0:
			self.inbox = stage.inbox
		else:
			stage.inbox = self.outbox
		self.outbox = stage.outbox
		self.stages.append(stage)

	def run(self):
		for stage in self.stages:
			stage.start()

	def process(self, message):
		self.inbox.put(message)