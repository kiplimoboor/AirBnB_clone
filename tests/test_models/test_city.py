"""
This module contains tests for the `city` module
"""

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def test_types(self):
        c = City()
        self.assertIsInstance(c, BaseModel)
        self.assertIsInstance(c.state_id, str)
        self.assertIsInstance(c.name, str)
