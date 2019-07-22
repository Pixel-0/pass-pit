from random import *
import string
max_char = 8
password = "".join(choice(string.ascii_letters) for x in range(randint(8, max_char)))
print ("Your password is: ",password)

class Credential:
    """
    Class that generates new instances of account credentials.

    """

    def __init__(self,platform,first_name,last_name,username,email,password):

        self.platform = platform
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

class User:
    """
    Class that generates new instances of users.

    """

    def __init__(self,first_name,last_name,username,email,password):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    credential_list = []

    @classmethod
    def create_credential(cls,detail1,detail2,detail3,detail4,detail5,detail6):
        '''
        be able to create a new credential/account with all details
        '''
        new_credential = Credential(detail1,detail2,detail3,detail4,detail5,detail6)

        return new_credential

    @classmethod
    def save_credential(cls,new_credential,credential_list):
        '''
        be able to save a new credential/account with all details to a list
        '''
        credential_list.append(new_credential)

    @classmethod
    def display_credentials(cls,credential_list):
        for cred in credential_list:
            return (cred.platform,cred.first_name,cred.last_name,cred.username,cred.email,cred.password)

    @classmethod
    def del_credential(cls,name,credential_list):
        '''
        be able to delete a credential
        '''
        for cred in credential_list:
            if name == cred.platform:
                credential_list.remove(cred)
        return credential_list



