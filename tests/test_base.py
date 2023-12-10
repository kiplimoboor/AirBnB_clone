"""
This is a test module for the base_model module
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """
    Test Cases for BaseModel
    """

    def test_base_init(self):
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b1.created_at, datetime)
        self.assertIsInstance(b1.updated_at, datetime)
        self.assertIsInstance(b1, BaseModel)
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
        b1.name = "Base"
        b1.number = 89
        self.assertEqual(b1.name, "Base")
        self.assertEqual(b1.number, 89)
