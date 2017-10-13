import pyperclip

# Global Variables
global users_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	users_list =[]
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		User.users_list.append(self)
		
class Credential:
	'''
	Class to create  account credentials, generate passwords and save their information
	'''
	# Class Variables
	credentials_list =[]
	def __init__(self,site_name,account_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.site_name = site_name
		self.account_name = account_name
		self.password = password

	def save_credentials(self):
		'''
		Function to save a newly created user instance
		'''
		# global users_list
		Credential.credentials_list.append(self)
	
	@classmethod
	def display_credentials(cls):
		'''
		Class method to display the list of credentials saved
		'''
		return cls.credentials_list
		
	@classmethod
	def find_by_site_name(cls, site_name):
		'''
	    Method that takes in a site_name and returns a credential that matches that site_name.
	    '''
	    for credential in credentials_list:
	    	if credential.site_name == site_name:
	    		return credential
