#!/usr/bin/python3
"""unittest for BaseModel"""
import unittest
import pep8
from models.amenity import Amenity
import inspect


class TestAmenity(unittest.TestCase):
    """defining the unittest cases for BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/amenity.py"])
        self.assertEqual(result.total_errors, 0, "Found code style " +
                         "errors (and warnings).")

    def test_pep8_conformance_test_Amenity(self):
        """
        Test that test_square.py file conform to PEP8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Amenity.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
