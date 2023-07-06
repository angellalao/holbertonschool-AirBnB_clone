import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Tests for the City class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.c1 = City()

    def test_is_instance(self):
        """Test that an instance is of type City"""
        self.assertIsInstance(self.c1, City)
