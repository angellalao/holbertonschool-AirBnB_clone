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

    def test_name_attribute_exist(self):
        """Test that name attribute exists"""
        self.assertEqual(self.c1.name, "")

    def test_state_id_attribute_exist(self):
        self.assertEqual(self.c1.state_id, "")
