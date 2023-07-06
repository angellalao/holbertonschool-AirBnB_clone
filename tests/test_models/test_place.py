import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.p1 = Place()

    def test_is_instance(self):
        """Test that an instance is of type Place"""
        self.assertIsInstance(self.p1, Place)
