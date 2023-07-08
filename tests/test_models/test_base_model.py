import unittest
from models.base_model import BaseModel
#from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def setUp(self):
        """Test that class can be instantiated"""
#        self.f1 = FileStorage()
        self.b1 = BaseModel()
#        self.f1.new(self.b1)

#    def tearDown(self):
#        """Clean up after each test"""
#        self.f1._FileStorage__objects.clear()

    def test_is_instance(self):
        """Test that an instance is of type BaseModel"""
        self.assertIsInstance(self.b1, BaseModel)

    def test_str_returns_a_string(self):
        """Test that __str__ returns type str"""
        model_string = self.b1.__str__()
        self.assertIsInstance(model_string, str)

    def test_str_returns_the_expected_format(self):
        """Test that __str__ returns a formatted string"""
        expected_formatted_string = (
            f"[{self.b1.__class__.__name__}] ({self.b1.id}) "
            f"{{'id': '{self.b1.id}', "
            f"'created_at': '{self.b1.created_at.isoformat()}', 'updated_at': "
            f"'{self.b1.updated_at.isoformat()}', '__class__': "
            f"'{type(self.b1).__name__}'}}"
        )
        self.assertEqual(str(self.b1), expected_formatted_string)

    def test_save_correctly_updates_updated_at_time(self):
        """Test that save correctly updates the updated_at time"""
        initial_updated_at_time = self.b1.updated_at
        self.b1.save()
        updated_at_time_after_save = self.b1.updated_at
        self.assertNotEqual(initial_updated_at_time, updated_at_time_after_save)

    def test_to_dict_makes_a_copy(self):
        """Test that to_dict makes copy"""
        new_dict = self.b1.__dict__.copy()
        self.assertEqual(new_dict, self.b1.__dict__)

    def test_to_dict_modifies_created_at_to_isoformat(self):
        """Test that to_dict modifies created_at to isoformat"""
        new_dict = self.b1.to_dict()
        self.assertEqual(new_dict["created_at"], self.b1.created_at.isoformat())

    def test_to_dict_modifies_updated_at_to_isoformat(self):
        """Test that to_dict modifies updated_at to isoformat"""
        new_dict = self.b1.to_dict()
        self.assertEqual(new_dict["updated_at"], self.b1.updated_at.isoformat())

    def test_to_dict_sets_correct_class_name(self):
        """Test that to_dict sets the correct class name"""
        new_dict = self.b1.to_dict()
        self.assertEqual(new_dict["__class__"], type(self.b1).__name__)
