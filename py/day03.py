#!/usr/bin/env python3

import collections
import itertools


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


def run_a(filename):
    lines = read_input(filename)
    print(count_overlaps(lines))


def run_b(filename):
    lines = read_input(filename)
    print(find_non_overlap(lines))
