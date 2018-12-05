import unittest

from py.day03 import *

class TestExample(unittest.TestCase):

    def test_square_from(self):
        s = Square.from_line('#123 @ 3,2: 5x4')
        self.assertEqual(s.id, 123)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.w, 5)
        self.assertEqual(s.h, 4)

        self.assertEqual(len(list(s.squares())), 20)
        self.assertEqual(len(set(x[0] for x in s.squares())), 5)

    def test_overlap_count(self):
        lines = [
	    '#1 @ 1,3: 4x4',
	    '#2 @ 3,1: 4x4',
	    '#3 @ 5,5: 2x2',
        ]

        self.assertEqual(count_overlaps(lines), 4)

    def test_non_overlap(self):
        lines = [
	    '#1 @ 1,3: 4x4',
	    '#2 @ 3,1: 4x4',
	    '#3 @ 5,5: 2x2',
        ]

        self.assertEqual(find_non_overlap(lines), set([3]))
