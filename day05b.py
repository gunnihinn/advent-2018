#!/usr/bin/env python3

import collections
import itertools
import unittest

import linked


class Reducer():

    def __init__(self, polymer):
        self.polymer = polymer
        self.head = linked.Double.from_list(polymer)

    def run(self):
        if self.head.next is None:
            return False

        if is_pair(self.head.value, self.head.next.value):
            self.head = self.head.delete()
            self.head = self.head.delete()

            if self.head.prev is not None:
                self.head = self.head.prev

            return True

        self.head = self.head.next
        return True


def read_input(filename):
    with open(filename) as fh:
        return fh.read()


def is_pair(a, b):
    return a != b and a.lower() == b.lower()


def reduce(polymer):
    r = Reducer(polymer)
    while r.run():
        pass

    while r.head.prev is not None:
        r.head = r.head.prev

    if r.head is None or r.head.value is None:
        return []

    reduced = [r.head.value]
    while r.head.next is not None:
        r.head = r.head.next
        reduced.append(r.head.value)

    return reduced


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

    types = polymer_types(polymer)

    lengths = []
    for t in types:
        p = remove_type(polymer, t)
        lengths.append(len(reduce(p)))

    print(min(lengths))
