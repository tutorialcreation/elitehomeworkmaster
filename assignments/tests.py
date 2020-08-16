import unittest
from django.test import TestCase

# Create your tests here.
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')

    def test_isupper(self):
        self.assertFalse('Foo'.isupper())
        self.assertTrue('FOO'.isupper())
    
    def test_split(self):
        s='hello world'
        self.assertEqual(s.split(),['hello','world'])
        with self.assertRaises(TypeError):
            s.split(2)


        