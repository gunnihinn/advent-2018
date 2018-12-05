#!/usr/bin/env python3

import collections
import itertools
import unittest


def read_input(filename):
    with open(filename) as fh:
        return fh.read()


def is_pair(a, b):
    return a != b and a.lower() == b.lower()


def reduce(polymer):
    processed = []
    for p in polymer:
        if not processed:
            processed.append(p)
        elif is_pair(processed[-1], p):
            processed.pop()
        else:
            processed.append(p)

    return processed


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


if __name__ == '__main__':
    #unittest.main()
    polymer = list(read_input('inputs/input-05.txt').strip())
    print(len(reduce(polymer)))
