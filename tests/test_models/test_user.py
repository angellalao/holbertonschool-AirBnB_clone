import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.u1 = User()

    def test_is_instance(self):
        """Test that an instance is of type User"""
        self.assertIsInstance(self.u1, User)

    def test_inherits_from_base_model(self):
        """Test that User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_empty_attributes_initialization(self):
        """Test the initialization of User attributes"""
        self.assertEqual(self.u1.email, "")
        self.assertEqual(self.u1.password, "")
        self.assertEqual(self.u1.first_name, "")
        self.assertEqual(self.u1.last_name, "")

    def test_pre_filled_attributes_initialization(self):
        """Test the initialization of User with predefined attributes"""
        email = "betty@holberton.com"
        password = "battery89"
        first_name = "Betty"
        last_name = "Holberton"
        user = User(email=email, password=password, first_name=first_name,
                    last_name=last_name)
        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)

    def test_save(self):
        """Test the save() method"""
        initial_updated_at = self.u1.updated_at
        self.u1.email = "test@example.com"
        self.u1.save()
        self.assertNotEqual(self.u1.updated_at, initial_updated_at)

    def test_str_returns_the_expected_format(self):
        """Test that __str__ returns a formatted string"""
        self.maxDiff = None
        self.u1.email = "betty@holberton"
        self.u1.password = "battery89"
        expected_formatted_string = (
            f"[User] ({self.u1.id}) "
            f"{{'id': '{self.u1.id}', "
            f"'created_at': '{self.u1.created_at.isoformat()}', "
            f"'updated_at': '{self.u1.updated_at.isoformat()}', "
            f"'email': '{self.u1.email}', 'password': '{self.u1.password}', "
            f"'__class__': '{type(self.u1).__name__}'}}"
        )
        self.assertEqual(str(self.u1), expected_formatted_string)
