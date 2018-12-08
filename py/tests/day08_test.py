import unittest

from py.day08 import *

class TestExample(unittest.TestCase):

    def test_parse1(self):
        items = [0, 1, 99]
        items.reverse()

        t = parse(items)
        exp = Tree()
        exp.metadata = [99]
        self.assertEqual(items, [])
        self.assertEqual(t, exp)

    def test_parse2(self):
        items = list(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()))
        items.reverse()
        t = parse(items)

        D = Tree()
        D.metadata = [99]

        C = Tree()
        C.children = [D]
        C.metadata = [2]

        B = Tree()
        B.metadata = [10, 11, 12]

        A = Tree()
        A.children = [B, C]
        A.metadata = [1, 1, 2]

        self.assertEqual(items, [])
        self.assertEqual(t, A)

    def test_value1(self):
        D = Tree()
        D.metadata = [99]

        C = Tree()
        C.children = [D]
        C.metadata = [2]

        self.assertEqual(C.value(), 0)

    def test_value2(self):
        items = list(map(int, '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split()))
        items.reverse()
        t = parse(items)

        self.assertEqual(t.value(), 66)
