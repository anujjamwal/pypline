import unittest

from ..pypline.stage import Stage

class dummyProcessor:
	def process(self, value):
		return 2*value

class TestStage(unittest.TestCase):
	def test_if_stage_is_stopped(self):
		stage = Stage(dummyProcessor)

		self.assertEqual(False, stage.isRunning())

	def test_stage_processor(self):
		stage = Stage(dummyProcessor)
		stage.start()
		
		stage.inbox.put(100)
		
		value = stage.outbox.get()
		self.assertEqual(200, value)			

if __name__ == "__main__":
    unittest.main()