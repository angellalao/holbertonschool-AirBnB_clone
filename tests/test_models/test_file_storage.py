import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Test that class can be instatiated"""
                self.f1 = FileStorage()

    def test_is_instance(self):
        """Test that an instance is of type FileStorage"""
        self.assertIsInstance(self.f1, FileStorage)
