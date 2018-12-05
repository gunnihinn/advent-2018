#!/usr/bin/env python3

import collections
import itertools
import unittest


def read_input(filename):
    with open(filename) as fh:
        return fh.read()


def is_pair(a, b):
    return a != b and a.lower() == b.lower()


def bad_indexes(polymer):
    indexes = set()

    i = 0
    while i < len(polymer)-1:
        if is_pair(polymer[i], polymer[i+1]):
            indexes.add(i)
            indexes.add(i+1)
            i += 1
        i += 1

    return indexes


def reduce_step(polymer):
    ixs = bad_indexes(polymer)

    return [ p for (i, p) in enumerate(polymer) if i not in ixs ]


def reduce(polymer):
    l = 0
    while l != len(polymer):
        l = len(polymer)
        polymer = reduce_step(polymer)

    return polymer


def polymer_types(polymer):
    return set([ c.lower() for c in polymer ])


def remove_type(polymer, t):
    return [ a for a in polymer if a.lower() != t ]


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
