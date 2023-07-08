import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.f1 = FileStorage()

    def tearDown(self):
        """Cleans up the test"""
        self.f1._FileStorage__objects.clear()

    def test_is_instance(self):
        """Test that an instance is of type FileStorage"""
        self.assertIsInstance(self.f1, FileStorage)

    def test_all_empty(self):
        """Tests the all() method returns an empty dict """
        self.assertNotEqual(self.f1.all(), {})

    def test_all_returns_correct_objects(self):
        """Tests the all() method returns the correct dictionary"""
        self.f1._FileStorage__objects = {
            "Object1": {"id": 1, "name": "Object 1"},
            "Object2": {"id": 2, "name": "Object 2"},
            "Object3": {"id": 3, "name": "Object 3"},
        }
        expected_dict = {
            "Object1": {"id": 1, "name": "Object 1"},
            "Object2": {"id": 2, "name": "Object 2"},
            "Object3": {"id": 3, "name": "Object 3"},
        }
        self.assertEqual(self.f1.all(), expected_dict)

    def test_new_adds_object_to_objects(self):
        """Test new() method adds an object to __objects"""
        obj = BaseModel()
        self.f1.new(obj)
        expected_key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(expected_key, self.f1._FileStorage__objects)
        self.assertEqual(self.f1._FileStorage__objects[expected_key], obj)

    def test_file_path(self):
        """Test that serialized file is saved on the correct file path"""
        self.assertEqual(self.f1._FileStorage__file_path, "file.json")
