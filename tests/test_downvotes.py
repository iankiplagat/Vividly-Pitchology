import unittest
from app.models import Downvote

class DownvoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Downvote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_downvote = Downvote()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_downvote,Downvote))
