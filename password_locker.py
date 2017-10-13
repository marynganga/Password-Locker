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

def generate_password():
	'''
	Function to generate a password automatically
	'''
	User.generate_password()

def main():
	print('Hello! Welcome to password locker.')
	while True:
		print('Use these codes to navigate: ca-Create an Account, li-Log In, ex-Exit')
		print("-"*60)
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			print('Goodbye')
			break

		elif short_code == 'ca':
			print('To create a new account')
			print("-"*60)
			first_name = input('Enter your first name: ')
			last_name = input('Enter your last name: ')
			password = input('Enter your password: ')
			save_user(create_user(first_name,last_name,password))
			print("-"*60)
			print(f'New Account Created for: {first_name} {last_name} using password: {password}')
			print("-"*60)


			# print('Use these codes to choose an option for your password: ep - to enter an existing password, np - to generate a new password automatically')
			# print("*"*60)
			# psw_choice = input('Enter an option: ').lower().strip()
			# if psw_choice == 'ep':
			# 	password = input('Enter your password: ')






if __name__ == '__main__':
	main()

