import pyperclip

users_list = []
class User:
	'''
	Class to create user accounts and save their information
	'''
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password