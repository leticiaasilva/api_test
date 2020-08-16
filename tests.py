import unittest
from api_test import *

class TestStringMethods(unittest.TestCase):

    def test_types(self):
        self.assertTrue(type(distance_in_mega_lights) is int)
        self.assertTrue(type(list_of_print) is list)

    def test_all_starships(self):
        self.assertTrue(len(list_of_print) is 10)    

if __name__ == '__main__':
    unittest.main()