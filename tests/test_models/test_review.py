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

    def test_place_id_exist(self):
        """Test place_id attribute is empty string"""
        self.assertEqual(self.r1.place_id, "")

    def test_user_id_exist(self):
        """Test user_id attribute is empty string"""
        self.assertEqual(self.r1.user_id, "")

    def test_text_exist(self):
        """Test text attribute is empty string"""
        self.assertEqual(self.r1.text, "")
