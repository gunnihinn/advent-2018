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
        s = square(p)
        self.assertEqual(s(33, 45, 3), 29)

    def test_square2(self):
        p = power(42)
        s = square(p)
        self.assertEqual(s(21, 61, 3), 30)

    @unittest.skip("This takes way too long")
    def test_max_square1(self):
        s = square(power(18))
        self.assertEqual(max_square(s, 3), (33, 45))

    @unittest.skip("This takes way too long")
    def test_max_square2(self):
        s = square(power(42))
        self.assertEqual(max_square(s, 3), (21, 61))

    @unittest.skip("This takes way too long")
    def test_total_square1(self):
        s = square(power(18))
        self.assertEqual(total_square(s), (90, 269, 16))
