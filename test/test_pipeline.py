import unittest

from ..pypline.pipeline import Pipeline
from ..pypline.stage import Stage

class dummyProcessor:
	def process(self, value):
		return 2*value

class TestPipeline(unittest.TestCase):
	def test_pipeline(self):
		pipeline = Pipeline()

		pipeline.appendStage(Stage(dummyProcessor))
		pipeline.appendStage(Stage(dummyProcessor))

		pipeline.run()

		pipeline.process(10)

		value = pipeline.outbox.get()

		self.assertEqual(40, value)


if __name__ == "__main__":
    unittest.main()