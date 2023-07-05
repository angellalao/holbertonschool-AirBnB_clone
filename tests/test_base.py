import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.b1 = BaseModel()
        self.assertIsInstance(self.b1, BaseModel)

    def test_str_returns_a_string(self):
        """Test that __str__ returns type str"""
        model_string = self.b1.__str__()
        self.assertIsInstance(model_string, str)

    def test_str_returns_the_expected_format(self):
        """Test that __str__ returns a formatted string"""
        expected_formatted_string = (
            f"[{self.b1.__class__}] ({self.b1.id}) {{'id': '{self.b1.id}', "
            f"'created_at': '{self.b1.created_at.isoformat()}', 'updated_at': "
            f"'{self.b1.updated_at.isoformat()}', '__class__': "
            f"'{type(self.b1).__name__}'}}"
            )
        self.assertEqual(str(self.b1), expected_formatted_string)

    def test_save_correctly_updates_updated_at_time(self):
        """Test that save correctly updates the updated_at time"""
        expected_updated_time = self.b1.updated_at.isoformat()
        self.assertEqual(expected_updated_time, self.b1.updated_at.isoformat())
