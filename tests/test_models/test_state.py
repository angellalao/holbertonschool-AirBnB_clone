import unittest
from models.state import State

class TestState(unittest.TestCase):
    """Tests for the State class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.s1 = State()

    def test_is_instance(self):
        """Test that an instance is of type State"""
        self.assertIsInstance(self.s1, State)
