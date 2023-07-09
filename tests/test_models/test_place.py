import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    """Tests for the Place class"""

    def setUp(self):
        """Test that class can be instatiated"""
        self.p1 = Place()

    def test_is_instance(self):
        """Test that an instance is of type Place"""
        self.assertIsInstance(self.p1, Place)

    def test_city_id_attribute(self):
        """Test that city_id attribute exists"""
        self.assertEqual(self.p1.city_id, "")

    def test_user_id_attribute(self):
        """Test that user_id attribute exists"""
        self.assertEqual(self.p1.user_id, "")

    def test_name_attribute(self):
        """Test that name attribute exist"""
        self.assertEqual(self.p1.name, "")
    def test_description_attribute(self):
        """Test that description attribute exist"""
        self.assertEqual(self.p1.description, "")

    def test_number_rooms_is_0(self):
        """Test that number_rooms is 0"""
        self.assertEqual(self.p1.number_rooms, 0)

    def test_number_bathrooms_is_0(self):
        """Test that number_bathrooms is 0"""
        self.assertEqual(self.p1.number_bathrooms, 0)

    def test_max_guest_is_0(self):
        """Test that max_guest is 0"""
        self.assertEqual(self.p1.max_guest, 0)

    def test_price_by_night_is_0(self):
        """Test price_by_night is 0"""
        self.assertEqual(self.p1.price_by_night, 0)

    def test_latitude_is_float_0(self):
        """Test latitude is 0.0"""
        self.assertEqual(self.p1.latitude, 0.0)

    def test_longitude_is_float_0(self):
        """Test longitude is 0.0"""
        self.assertEqual(self.p1.longitude, 0.0)

    def test_amenity_ids_attribute_is_empty_list(self):
        """Test amenity_ids is []"""
        self.assertEqual(self.p1.amenity_ids, [])


