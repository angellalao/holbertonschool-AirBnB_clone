import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.u1 = User()

    def test_is_instance(self):
        """Test that an instance is of type User"""
        self.assertIsInstance(self.u1, User)
