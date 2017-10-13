import pyperclip
import random
import string

# Global Variables
# global users_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	global users_list
	users_list = []
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
	@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		for user in cls.users_list:
			if password = user.password:
				return True
			return False
			
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
	
	def generate_password(self,size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		self.password = gen_pass
		return self.password

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
		for credential in cls.credentials_list:
			if credential.site_name == site_name:
				return credential

	@classmethod
	def copy_credential(cls,site_name):
		'''
		Class method that copies a credential's info after the credential's site name is entered
		'''
		find_credential = cls.find_by_site_name(site_name)
		pyperclip.copy(f'Site Name: {find_credential.site_name} - UserName: {find_credential.site_name} - Password:  {find_credential.password}')

