import unittest

from ..pypline.channel import Channel

class TestChannel(unittest.TestCase):
	def test_channel_put_and_get_behaviour(self):
		value = "channel value"

		channel = Channel()
		channel.put(value)
		return_value = channel.get()

		self.assertEqual(return_value, value)

if __name__ == "__main__":
    unittest.main()