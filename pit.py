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