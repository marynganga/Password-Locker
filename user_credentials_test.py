import unittest
import pyperclip
#from user_credentials import User, Credentials 

class TestUserCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the contact class behaviours.

	Args:
	    unittest.TestCase: helps in creating test cases
	'''
	def setUp(self):
		'''
		Function to create a user account before each test
		'''
		self.new_user = User('Mary','pswd100')

if __name__ == '__main__':
	unittest.main()