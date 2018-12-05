#!/usr/bin/env python3

import itertools
import collections


def read_input(filename):
    with open(filename) as fh:
        return fh.readlines()


def count_chars(line):
    d = collections.defaultdict(int)
    for c in line:
        d[c] += 1

    return d


def common_letters(id1, id2):
    return ''.join(a for (a, b) in zip(id1, id2) if a == b)


def score(char_count):
    d = collections.defaultdict(list)
    d[2] = []
    d[3] = []
    for char, count in char_count.items():
        d[count].append(char)

    return len(d[2]), len(d[3])


def count_different_chars(line1, line2):
    return sum(( a != b for (a, b) in zip(line1, line2) ))


def find_prototype_ids(lines):
    return next(filter(
            lambda x: count_different_chars(x[0], x[1]) == 1,
            itertools.combinations(lines, 2)
    ))


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


def run_a(filename):
    lines = read_input(filename)
    print(checksum(lines))


def run_b(filename):
    lines = read_input(filename)
    (id1, id2) = find_prototype_ids(lines)
    print(common_letters(id1, id2))
