import unittest
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Tests for the  Base class"""

    def test_str(self):
        """Test that it  returns a formatted string"""
        b1 = BaseModel()
        self.assertEqual(str(b1),
- [<class 'models.base_model.BaseModel'>] (b35598e0-62dd-4482-aabb-a2b1ea22eaad) {'id': 'b35598e0-62dd-4482-aabb-a2b1ea22eaad', 'created_at': '2023-07-03T23:21:56.213328', 'updated_at': '2023-07-03T23:21:56.213335', '__class__': 'BaseModel'})
