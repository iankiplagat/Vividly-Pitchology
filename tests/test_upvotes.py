import unittest
from app.models import Upvote

class UpvoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Upvote class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_upvote = Upvote()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_upvote,Upvote))
