#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
from datetime import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ """
        self.b2 = BaseModel()
        self.b1 = BaseModel()
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs(self):
        """ checks if an instance is created from a dictionary """
        dictionary = self.b1.to_dict()
        b1_copy_test = BaseModel(**dictionary)
        self.assertIsInstance(b1_copy_test, BaseModel)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_updated(self):
        """ checks if the instance for created_at and updated_at
        are datetime objects """
        self.assertIsInstance(self.b2, BaseModel)
        self.assertTrue(hasattr(self.b2, "created_at"))
        self.assertTrue(hasattr(self.b2, "updated_at"))
        self.assertIsInstance(self.b2.created_at, datetime)
        self.assertIsInstance(self.b2.updated_at, datetime)
        self.assertNotEqual(self.b2.created_at, self.b2.updated_at)