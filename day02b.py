#!/usr/bin/env python3

import collections
import itertools
import unittest


def read_input(filename):
    with open(filename) as fh:
        return fh.readlines()


def count_different_chars(line1, line2):
    return sum(( a != b for (a, b) in zip(line1, line2) ))


def find_prototype_ids(lines):
    return next(filter(
            lambda x: count_different_chars(x[0], x[1]) == 1,
            itertools.combinations(lines, 2)
    ))


def common_letters(id1, id2):
    return ''.join(a for (a, b) in zip(id1, id2) if a == b)


class TestExample(unittest.TestCase):

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


if __name__ == '__main__':
    #unittest.main()

    lines = read_input('inputs/input-02.txt')
    (id1, id2) = find_prototype_ids(lines)
    print(common_letters(id1, id2))
