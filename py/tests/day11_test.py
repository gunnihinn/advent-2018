import unittest

from py.day11 import *

class TestExample(unittest.TestCase):

    def test_power_level(self):
        self.assertEqual(power_level(3, 5, 8), 4)
        self.assertEqual(power_level(122, 79, 57), -5)
        self.assertEqual(power_level(217, 196, 39), 0)
        self.assertEqual(power_level(101, 153, 71), 4)
