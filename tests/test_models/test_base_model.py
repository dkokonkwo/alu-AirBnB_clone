#!/usr/bin/python3
""" 
unittests for BaseModel class
"""
import os
import sys
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """Test BaseModel class"""

    def test_init(self):
        """Test init method"""
        # create and object instance of BaseModel class
        obj = BaseModel()
        # check if obj is instance of BaseModel
        self.assertIsInstance(obj, BaseModel)
        # check if dict contains all expected attributes
        self.assertIn("id", obj.__dict__)
        self.assertIn("created_at", obj.__dict__)
        self.assertIn("updated_at", obj.__dict__)
        # check if P.I attributes are of correct types
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        # create dict to set obj values to with **kwargs
        new_dict = {}
        new_dict["id"] = "012345"
        new_dict["created_at"] = "1985-2-2T10:23:35.123467"
        new_dict["updated_at"] = "1999-1-4T7:15:05.543210"
        # created object instance with **kwargs and run testing
        obj2 = BaseModel(**new_dict)
        self.assertIsInstance(obj2, BaseModel)
        self.assertIn("id", obj2.__dict__)
        self.assertIn("created_at", obj2.__dict__)
        self.assertIn("updated_at", obj2.__dict__)
        self.assertIsInstance(obj2.id, str)
        self.assertIsInstance(obj2.created_at, datetime)
        self.assertIsInstance(obj2.updated_at, datetime)
        #  can also test exact values, including formatting of datetimes
        self.assertEqual(obj2.id, "012345")
        string1 = "1985-2-2T10:23:35.123467"
        self.assertEqual('{}'.format(obj2.created_at), string1)
        string2 = "1999-1-4T7:15:05.543210"
        self.assertEqual('{}'.format(obj2.updated_at), string2)
