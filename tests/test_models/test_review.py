import unittest
from models.review import Review

class TestReview(unittest.TestCase):
    """Tests for the Review class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.r1 = Review()

    def test_is_instance(self):
        """Test that an instance is of type Review"""
        self.assertIsInstance(self.r1, Review)
