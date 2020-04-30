import unittest
from lexicon import Lexigui
class Lexicon_functional_test(unittest.TestCase):
	"""docstring for Lexicon_functional_test"""
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def test_GUI(self):
		self.gui = Lexigui()
		self.assertEqual(self.gui.title(), 'Lexicon')
		
if __name__ == "__main__":
	unittest.main()

