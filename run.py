#!/usr/bin/env python3.6
from pit import User, Credential
from random import *
import string

def signup_user(first_name,last_name,username,email,password):
'''
Function to sign up a new user
'''
new_user = User(first_name,last_name,username,email,password)
return new_user

def generate_password(passlength):
'''
Function to generate a new password
'''
mypassword = "".join(choice(string.ascii_letters) for x in range(randint(passlength,passlength)))

return mypassword

def authenticate_user(user,username,password):
'''
Function to authenticate user details for access
'''
if user.username == username and user.password == password:
    return True

else:
    return False

def signup_credentials(platform,first_name,last_name,username,email,password):
'''
Function to add a new credential
'''
return User.create_credential(platform,first_name,last_name,username,email,password)

def save_credentials(credential,credential_list):
'''
Function to append new credential
'''
return User.save_credential(credential,credential_list)

def show_credentials(credential_list):
'''
Function to show a users' credentials
'''
return User.display_credentials(credential_list)

def delete_credential(name,credential_list):
'''
Function to show a users' credentials
'''
return User.del_credential(name,credential_list)

def main():
print("Hello, you're in pass-pit. What is your name?")
user_name = input()
if user_name == "":
    print("Enter a user name")
    user_name = input()
else:
    print(f"Hello {user_name}. Sign Up")
    print("Sign up new user")
    print ("First name ....")
    first_name = input()
    if first_name == "":
        print("Enter a valid input")
        print ("First name ....")
        first_name = input()
    else:
        print("Last name ...")
        last_name = input()
        if last_name == "":
            print("Enter a valid input")
            print("Last name ...")
            last_name = input()
        else:
            print("Preferred username ...")
            username = input()
            if username == "":
                print("Enter a valid input")
                print("Preferred username ...")
                username = input()
            else:
                print("Email address ...")
                email = input()
                if email == "":
                    print("Enter a valid input")
                else:
                    print("Password ...")
                    print("Would you like us to generate you password? [Y/n]")
                    passprompt = input()
                    if passprompt == "Y":
                        print("Length of the password?")
                        passlength = int(input())
                        password = generate_password(passlength)
                        print("Enter your password for sign in")
                        print(password)
                        currentuser = signup_user(first_name,last_name,username,email,password)
                        print(f"New User {first_name} {last_name} signed up")
                        print("Enter your details to sign in")
                        print("Username:")
                        username = input()
                        print("Password:")
                        password = input()
                        authentication = authenticate_user(currentuser,username,password)

                        if authentication == True:
                            print("Sign in was successful.")
                            while True:
                                a_list = []
                                print ("""Use these short codes : 
                                1. Register new social media account
                                2. Sign out""")
                                shortcode = input()
                                if shortcode == '1':
                                    print("Register a new social media account")
                                    print("Enter social media platform?")
                                    platform = input()

                                    print (f"First name on {platform} ...")
                                    first_name = input()

                                    print(f"Last name on {platform} ...")
                                    last_name = input()

                                    print(f"Username on {platform}...")
                                    username = input()

                                    print(f"Email address used for {platform}...")
                                    email = input()
                                    print("Password ...")
                                    print(f"Do you have a password for your {platform} account? [Y/n]")
                                    passprompt = input()
                                    if passprompt == "Y":
                                        print("Type password ...")
                                        password = input()
                                    elif passprompt == "":
                                        print("Enter a valid input")
                                    else:
                                        print("Would you like us to generate you password? [Y/n]")
                                        passprompt = input()
                                        if passprompt == "Y":
                                            print("Enter length of the password")
                                            passlength = int(input())
                                            password = generate_password(passlength)
                                        print("Password generated! ...")
                                        cred = signup_credentials(platform,first_name,last_name,username,email,password)
                                        save_credentials(cred,a_list)
                                        print(f"Details for {platform} are now saved")
                                        print("""Select what to do next
                                                    1. View locker
                                                    2. Delete an account
                                                    3.Add other account""")
                                        option = input()
                                        if option == '1':
                                            print(show_credentials(a_list))
                                        if option == '3':
                                            print("Register a new social media account")
                                    print("Enter social media platform")
                                    platform = input()

                                    print (f"First name on {platform} ...")
                                    first_name = input()

                                    print(f"Last name on {platform} ...")
                                    last_name = input()

                                    print(f"Username on {platform}...")
                                    username = input()

                                    print(f"Email address used for {platform}...")
                                    email = input()
                                    print("Password ...")
                                    print(f"Do you have a password for your {platform} account? [Y/n]")
                                    passprompt = input()
                                    if passprompt == "Y":
                                        print("Type password ...")
                                        password = input()
                                    elif passprompt == "":
                                        print("Enter a valid input")
                                    else:
                                        print("Would you like us to generate you password? [Y/n]")
                                        passprompt = input()
                                        if passprompt == "Y":
                                            print("Enter length of the password")
                                            passlength = int(input())
                                            password = generate_password(passlength)
                                        print("Password generated! ...")
                                        cred = signup_credentials(platform,first_name,last_name,username,email,password)
                                        save_credentials(cred,a_list)
                                        print(f"Details for {platform} are now saved")
                                        print("""Select what to do next
                                                    1. View locker
                                                    2. Delete an account
                                                    3. Add other account""")
                                        elif option == '2':
                                            print("Which account would you like to delete?")
                                            name = input()
                                            delete_credential(name,a_list)
                                            print(show_credentials(a_list))
                                        elif option == "":
                                            print("Enter a valid input")
                                        elif passprompt == "":
                                            print("Enter a valid input")
                                        else:
                                            print("Type password ...")
                                            password = input()
                                        cred = signup_credentials(platform,first_name,last_name,username,email,password)
                                        save_credentials(cred,a_list)
                                        print(f"Details for {platform} are now saved")
                                        print("""Select what to do next
                                                    1. View locker
                                                    2. Sign out""")
                                        option = input()
                                        if option == '1':
                                            print(show_credentials(a_list))
                                        elif option == '2':
                                            print("Which account would you like to delete?")
                                            name = input()
                                            delete_credential(name,a_list)
                                            print(show_credentials(a_list))
                                        elif option == "":
                                            print("Enter a valid input")

                                elif shortcode == "":
                                    print("Enter a valid input")

                        elif shortcode == "":
                            print("Enter a valid input")
                                    
                    else:
                        print("Type password ...")
                        password = input()
                        print("Enter your password for sign in")
                        print(password)
                        currentuser = signup_user(first_name,last_name,username,email,password)
                        print(f"New User {first_name} {last_name} signed up")
                        print("Enter your details to sign in")
                        print("Username:")
                        username = input()
                        print("Password:")
                        password = input()
                        authentication = authenticate_user(currentuser,username,password)

                                elif shortcode == "":
                                    print("Enter a valid input")

                        elif shortcode == "":
                            print("Please use short codes")
                        
if __name__ == '__main__':

main()



