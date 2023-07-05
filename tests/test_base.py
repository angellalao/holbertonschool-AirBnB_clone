import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Tests for the  Base class"""

    def test_str(self):
        """Test that it  returns a formatted string"""
        b1 = BaseModel()
        expected_formatted_string = f"[{b1.__class__}] ({b1.id}) {{'id': '{b1.id}', 'created_at': '{b1.created_at.isoformat()}', 'updated_at': '{b1.updated_at.isoformat()}', '__class__': '{type(b1).__name__}'}}"
        self.assertEqual(str(b1), expected_formatted_string)
