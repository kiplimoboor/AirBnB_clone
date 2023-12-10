# """
# This is a test module for the base_model module
# """

# import os
# import unittest
# from datetime import datetime
# import models
# from models.base_model import BaseModel

# filename = "file.json"


# class TestBase(unittest.TestCase):
#     """
#     Test Cases for BaseModel
#     """

#     def setUp(self):
#         if os.path.exists(filename):
#             os.remove(filename)

#     def tearDown(self):
#         if os.path.exists(filename):
#             os.remove(filename)

#     def test_base_init(self):
#         b1 = BaseModel()
#         self.assertIsInstance(b1.id, str)
#         self.assertIsInstance(b1.created_at, datetime)
#         self.assertIsInstance(b1.updated_at, datetime)
#         self.assertIsInstance(b1, BaseModel)
#         b2 = BaseModel()
#         self.assertNotEqual(b1.id, b2.id)
#         b1.name = "Base"
#         b1.number = 89
#         self.assertEqual(b1.name, "Base")
#         self.assertEqual(b1.number, 89)

#     def test_str(self):
#         b1 = BaseModel()
#         b1_str = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
#         self.assertEqual(str(b1), b1_str)

#     def test_save(self):
#         b1 = BaseModel()
#         update_at_create = b1.updated_at
#         b1.name = "My First Model"
#         b1.my_number = 89
#         self.assertFalse(os.path.exists(filename))
#         b1.save()
#         self.assertTrue(os.path.exists(filename))
#         update_at_save = b1.updated_at
#         self.assertNotEqual(update_at_create, update_at_save)

#     def test_to_dict(self):
#         b = BaseModel()
#         b_dict = b.to_dict()

#         self.assertIsInstance(b_dict, dict)
#         self.assertEqual(b_dict['__class__'], type(b).__name__)
#         self.assertIn('id', b_dict.keys())
#         self.assertIn('created_at', b_dict.keys())
#         self.assertIn('updated_at', b_dict.keys())
