"""
This module contains tests for the `review` module
"""

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_types(self):
        r = Review()
        self.assertIsInstance(r, BaseModel)
        self.assertIsInstance(r.place_id, str)
        self.assertIsInstance(r.user_id, str)
        self.assertIsInstance(r.text, str)
