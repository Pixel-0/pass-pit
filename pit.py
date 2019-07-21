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
        for c in credential_list:
            return (c.platform,c.first_name,c.last_name,c.username,c.email,c.password)


    @classmethod
    def del_credential(cls,name,credential_list):
        '''
        be able to delete a credential
        '''
        for c in credential_list:
            if name == c.platform:
                credential_list.remove(c)
        return credential_list
