import unittest

from py.day09 import *

class TestExample(unittest.TestCase):

    def test_play1(self):
        self.assertEqual(play(10, 1618), 8317)

    def test_play2(self):
        self.assertEqual(play(13, 7999), 146373)

    def test_play3(self):
        self.assertEqual(play(17, 1104), 2764)

    def test_play4(self):
        self.assertEqual(play(21, 6111), 54718)

    def test_play5(self):
        self.assertEqual(play(30, 5807), 37305)
