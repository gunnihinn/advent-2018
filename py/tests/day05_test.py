import unittest

from py.day05 import *

class TestExample(unittest.TestCase):

    def test_reduce1(self):
        self.assertEqual(reduce('aA'), [])

    def test_reduce2(self):
        self.assertEqual(reduce('abBA'), [])

    def test_reduce3(self):
        self.assertEqual(reduce('abAB'), list('abAB'))

    def test_reduce4(self):
        self.assertEqual(reduce('aabAAB'), list('aabAAB'))

    def test_reduce5(self):
        self.assertEqual(reduce('dabAcCaCBAcCcaDA'), list('dabCBAcaDA'))
