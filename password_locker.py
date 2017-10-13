#! /usr/bin/env python3
import pyperclip
from user_credentials import User, Credential

def create_user(fname,lname,password):
	'''
	Function to create a new user account
	'''
	new_user = User(fname,lname,password)
	return new_user

def save_user(user):
	'''
	Function to save a new user account
	'''
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user

def generate_password():
	'''
	Function to generate a password automatically
	'''
	gen_pass = Credential.generate_password()
	return gen_pass

def create_credential(user_name,site_name,account_name,password):
	'''
	Function to create a new credential
	'''
	new_credential=Credential(user_name,site_name,account_name,password)
	return new_credential

def save_credential(credential):
	'''
	Function to save a newly created credential
	'''
	Credential.save_credentials(credential)

def display_credentials(user_name):
	'''
	Function to display credentials saved by a user
	'''
	return Credential.display_credentials(user_name)
	
def main():
	print('Hello! Welcome to password locker.')
	while True:
		print(" ")
		print('Use these codes to navigate: ca-Create an Account, li-Log In, ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print('To create a new account:')
			first_name = input('Enter your first name - ').strip()
			last_name = input('Enter your last name - ').strip()
			password = input('Enter your password - ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')

		elif short_code == 'li':
			print("-"*60)
			print('To login, enter your account details:')
			user_name = input('Enter your first name - ').strip()
			password = input('Enter your password - ').strip()
			user_exists = verify_user(user_name,password)
			if user_exists.first_name == user_name:
				print(" ")
				print(f'Welcome {user_name}. Please choose an option to continue.')
				while True:
					print(" ")
					print('Navigation codes: cc-Create a Credential, dc-Display Credentials, ex-Exit')
					short_code = input('Enter a choice: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print('Goodbye')
						break
					elif short_code == 'cc':
						print('Enter your credential details:')
						site_name = input('Enter the site\'s name- ').strip()
						account_name = input('Enter your username - ').strip()
						while True:
							print(' ')
							print('Please choose an option for entering a password: ep-enter existing password, gp-generate a password, ex-exit')
							psw_choice = input('Enter an option: ').lower().strip()
							if psw_choice == 'ep':
								password = input('Enter your password: ').strip()
								break
							elif psw_choice == 'gp':
								password = generate_password()
								break
							elif psw_choice == 'ex':
								break
							else:
								print('Oops! Wrong option entered.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
					elif short_code == 'dc':
						if display_credentials(user_name):
							print('Here is a list of all your credentials')
							for credential in display_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
								print(' ')
						else:
							print(' ')
							print("You don't seem to have any contacts saved yet")
							print(' ')
			else: 
				print('The details entered are incorrect. Try again or Create an Account.')		
		else:
			print("-"*60)
			print('Oops! Wrong option entered. Try again.')
				






if __name__ == '__main__':
	main()

