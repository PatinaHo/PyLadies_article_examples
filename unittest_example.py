import unittest
import example
print(unittest)

class TestExample(unittest.TestCase):
	"""docstring for TestInteger_check"""
	# def __init__(self, arg):
	# 	super(TestInteger_check, self).__init__()
	# 	self.arg = arg
	
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_integer(self):
		integer = "15"
		result = example.integer_check(integer)
		self.assertEqual(result, '15')

	def test_other_format(self):
		text = 'whatever'
		result = example.integer_check(text)
		self.assertEqual(result, 'This is not an integer')

if __name__ == '__main__':
	unittest.main()