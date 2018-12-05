import unittest

from py.day02 import *


class TestExample(unittest.TestCase):

    def test_count_chars(self):
        line = 'bababc'
        exp = {
            'a': 2,
            'b': 3,
            'c': 1,
        }

        self.assertEqual(count_chars(line), exp)

    def test_score(self):
        line = 'bababc'
        #import pdb; pdb.set_trace()
        self.assertEqual(score(count_chars(line)), (True, True))

    def test_checksum(self):
        lines = [
            'abcdef',
            'bababc',
            'abbcde',
            'abcccd',
            'aabcdd',
            'abcdee',
            'ababab',
        ]

        self.assertEqual(checksum(lines), 12)

    def test_count_different_chars1(self):
        self.assertEqual(count_different_chars('abcde', 'axcye'), 2)

    def test_find_prototype_ids(self):
        ids = [
	    'abcde',
	    'fghij',
	    'klmno',
	    'pqrst',
	    'fguij',
	    'axcye',
	    'wvxyz',
        ]

        self.assertEqual(find_prototype_ids(ids), ('fghij', 'fguij'))

    def test_common_letters(self):
        self.assertEqual(common_letters('fghij', 'fguij'), 'fgij')
