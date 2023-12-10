"""
This module contains tests for the `file_storage` module
"""

import os
import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    Test cases for File Storage

    Args:
        unittest (class): unittest class TestCase
    """

    def setUp(self):
        pass

    def tearDown(self):
        filename = "file.json"
        if os.path.exists(filename):
            os.remove(filename)

    def test_all(self):
        b = BaseModel()
        storage.new(b)
        self.assertIn(f"BaseModel.{b.id}", storage.all().keys())
