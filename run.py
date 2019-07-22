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


                            
if __name__ == '__main__':

    main()



