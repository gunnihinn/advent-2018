import unittest

from py.day11 import *

class TestExample(unittest.TestCase):

    def test_power_level(self):
        self.assertEqual(power_level(3, 5, 8), 4)
        self.assertEqual(power_level(122, 79, 57), -5)
        self.assertEqual(power_level(217, 196, 39), 0)
        self.assertEqual(power_level(101, 153, 71), 4)

    def test_square1(self):
        p = power(18)
        self.assertEqual(square(p, 33, 45), 29)

    def test_square2(self):
        p = power(42)
        self.assertEqual(square(p, 21, 61), 30)

    def test_max_square1(self):
        self.assertEqual(max_square(18), (33, 45))

    def test_max_square2(self):
        self.assertEqual(max_square(42), (21, 61))
