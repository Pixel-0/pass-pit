import unittest
from random import *
import string
from pit import User, Credential

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Instagram","Pixel","Aurry","@pixel","pixel@live.com","#####")
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credential.platform,"Instagram")
        self.assertEqual(self.new_credential.first_name,"Pixel")
        self.assertEqual(self.new_credential.last_name,"Aurry")
        self.assertEqual(self.new_credential.username,"@pixel")
        self.assertEqual(self.new_credential.email,"pixel@live.com")
        self.assertEqual(self.new_credential.password,"#####")

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Aurora","Pixel","@tello","pixel@live.com","#####")

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            credential_list = []
        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Aurora")
        self.assertEqual(self.new_user.last_name,"Pixel")
        self.assertEqual(self.new_user.username,"@tello")
        self.assertEqual(self.new_user.email,"pixel@live.com")
        self.assertEqual(self.new_user.password,"#####")


    def test_create_credential(self):
        '''
        test_create_credential allows user to update a new credential
        '''
        instagram_credential = User.create_credential("instagram","Pixel","Aurry","@tello","pixel@live.com","password")
        self.assertTrue(instagram_credential)

    def test_save_credential(self):
        '''
        test_save_credentials test case to test if the credential object is saved into
         the credential list
        '''
        instagram_credential = User.create_credential("instagram","Pixel","Aurry","@tello","pixel@live.com","password")
        user_credential_list = []
        User.save_credential(instagram_credential,user_credential_list)
        self.assertEqual(len(user_credential_list),1)

    def test_delete_credentials(self):
        '''
        test_display_credential test case to test if all credentials will be returned
        '''
        instagram_credential = User.create_credential("instagram","Pixel","Aurry","@tello","pixel@live.com","password")
        user_credential_list = []
        User.save_credential(instagram_credential,user_credential_list)
        new_list = User.del_credential("instagram",user_credential_list)
        self.assertEqual(len(new_list),0)



if __name__ == '__main__':
    unittest.main()