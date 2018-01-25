import unittest
from memory_game.main import Main


class TestMain(unittest.TestCase):
	def setUp(self):
		self.main = Main()
		
	def test_initializer(self):
		self.assertEqual(self.main.elapsed, 0.0)
