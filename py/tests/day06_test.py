import unittest

from py.day06 import *

class TestExample(unittest.TestCase):

    def test_corners(self):
        points = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
        self.assertEqual(corners(points), (1, 8, 1, 9))

    def test_boundary(self):
        points = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
        self.assertEqual(boundary(points), set([(1,1), (1,6), (8,3), (8,9)]))

    def test_smallest_area(self):
        points = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
        self.assertEqual(smallest_area(points), 9)

    def test_largest_area(self):
        points = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
        self.assertEqual(largest_area(points), 17)

    def test_total_distance(self):
        points = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
        self.assertEqual(total_distance((4,3), points), 30)

    def test_total_area(self):
        points = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
        self.assertEqual(total_area(points, 32), 16)

