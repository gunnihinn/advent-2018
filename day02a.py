#!/usr/bin/env python3

import unittest
import collections


def read_input(filename):
    with open(filename) as fh:
        return fh.readlines()


def count_chars(line):
    d = collections.defaultdict(int)
    for c in line:
        d[c] += 1

    return d


def score(char_count):
    d = collections.defaultdict(list)
    d[2] = []
    d[3] = []
    for char, count in char_count.items():
        d[count].append(char)

    return len(d[2]), len(d[3])


def checksum(lines):
    tw = 0
    th = 0

    for line in lines:
        (a, b) = score(count_chars(line))
        if a:
            tw += 1
        if b:
            th += 1

    return tw * th


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

if __name__ == '__main__':
    #unittest.main()

    lines = read_input('inputs/input-02.txt')
    print(checksum(lines))
