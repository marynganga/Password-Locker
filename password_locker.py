#! /usr/bin/env python3
import pyperclip
from user_credentials import User, Credential

# global variables
global checking_user
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

def generate_password():
	'''
	Function to generate a password automatically
	'''
	User.generate_password()

def verify_user(first_name,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credential.check_user(first_name,password)
	return checking_user
def main():
	print('Hello! Welcome to password locker.')
	while True:
		print("-"*60)
		print('Use these codes to navigate: ca-Create an Account, li-Log In, ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			print('Goodbye')
			break

		elif short_code == 'ca':
			print("-"*60)
			print('To create a new account')
			first_name = input('Enter your first name: ').strip()
			last_name = input('Enter your last name: ').strip()
			password = input('Enter your password: ').strip()
			save_user(create_user(first_name,last_name,password))
			print(" ")
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')

		elif short_code == 'li':
			print("-"*60)
			print('Enter your account details')
			first_name = input('Enter your first name: ').strip()
			password = input('Enter your password: ').strip()
			user_exists = verify_user(first_name,password)
			if user_exists == True:
				print(f'Welcome {first_name}')
				while True:
					print("-"*60)
					print('Navigation codes: ca-Create a Credential, dc-Display Credentials, ex-Exit')
					print("-"*60)
					short_code = input('Enter a choice: ').lower().strip()
					if short_code == 'ex':
						print('Goodbye')
						break
			
				# print('Use these codes to choose an option for your password: ep - to enter an existing password, np - to generate a new password automatically')
				# print("*"*60)
				# psw_choice = input('Enter an option: ').lower().strip()
				# if psw_choice == 'ep':
				# 	password = input('Enter your password: ')






if __name__ == '__main__':
	main()

