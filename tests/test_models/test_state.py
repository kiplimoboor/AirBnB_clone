"""
This module contains tests for the `state` module
"""

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    def test_types(self):
        s = State()
        self.assertIsInstance(s, BaseModel)
        self.assertIsInstance(s.name, str)
