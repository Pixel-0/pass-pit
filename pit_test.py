import unittest
from random import *
import string
from pit import User
from pit import Credential

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
        self.new_credential = Credential("Facebook","Beyonce","Knowles","@beybey","bknowles@carter.com","#####")
    
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