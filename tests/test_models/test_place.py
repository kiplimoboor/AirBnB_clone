"""
This module contains tests for the `place` module
"""

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_types(self):
        p = Place()
        self.assertIsInstance(p, BaseModel)
        self.assertIsInstance(p.city_id, str)
        self.assertIsInstance(p.user_id, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.name, str)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.number_bathrooms, int)
        self.assertIsInstance(p.latitude, float)
        self.assertIsInstance(p.longitude, float)
        self.assertIsInstance(p.amenity_ids, list)
