#!/usr/bin/env python3

import collections
import itertools
import unittest


class Square():

    def __init__(self, i, x, y, width, height):
        self.id = i
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    @staticmethod
    def from_line(line):
        # line = '#id @ x,y: wxh'
        parts = line.split()
        i = int(parts[0][1:])

        xys = parts[2].split(',')
        x = int(xys[0])
        y = int(xys[1][:-1])

        (w, h) = parts[3].split('x')

        return Square(i, x, y, int(w), int(h))

    def squares(self):
        return (
                (x, y) 
                for x in range(self.x, self.x + self.w)
                for y in range(self.y, self.y + self.h)
        )


def read_input(filename):
    with open(filename) as fh:
        return fh.readlines()


def count_overlaps(lines):
    counts = collections.defaultdict(int)
    for line in lines:
        s = Square.from_line(line)
        for pt in s.squares():
            counts[pt] += 1

    return sum(1 for pt in counts.keys() if counts[pt] > 1)


def find_non_overlap(lines):
    tiles = collections.defaultdict(list)
    ids = set()

    for line in lines:
        s = Square.from_line(line)
        ids.add(s.id)
        for pt in s.squares():
            tiles[pt].append(s.id)

    overlapping = set()
    for vs in tiles.values():
        if len(vs) > 1:
            ids.difference_update(vs)

    return ids


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


if __name__ == '__main__':
    #unittest.main()
    lines = read_input('inputs/input-03.txt')
    print(find_non_overlap(lines))
