"""
This module contains tests for the `amenity` module
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_types(self):
        a = Amenity()
        self.assertIsInstance(a, BaseModel)
        self.assertIsInstance(a.name, str)
