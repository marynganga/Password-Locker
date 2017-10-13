# Password Locker

#### This is a python application that allows a user to generate and store passwords for various accounts.

## Built By [Mary Ng'ang'a](https://github.com/marynganga/)

## Description
Password Locker is a terminal run app that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **in terminal $./password_locker.py** | Welcome choose an option: ca - Create Account, li - Log In, ex - Exit |
| Display prompt for creating an account | **ca** | Enter your first name, last name and password |
| Display prompt for login in | **li** | Enter your account name and password |
| Display codes for navigation | **successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **cc** | Enter the site name, your username and password |
| Display a list of credentials | **dc** | list of saved credentials |
| Display prompt for which credential to copy | **copy** | details of the copied credential saved to clipboard |
| Exit application | **ex** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* pyperclip
* xclip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/marynganga/Password-Locker/
        $ cd Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x password_locker.py
        $ ./password_locker.py
        

## Technologies Used
* Python3.6

## License
MIT &copy;2017 [Mary Ng'ang'a](https://github.com/marynganga/)

