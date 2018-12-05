#!/usr/bin/env python3

import collections
import itertools


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


def polymer_types(polymer):
    return set([ c.lower() for c in polymer ])


def remove_type(polymer, t):
    return [ a for a in polymer if a.lower() != t ]


def run_a(filename):
    polymer = list(read_input(filename).strip())
    print(len(reduce(polymer)))


def run_b(filename):
    polymer = list(read_input(filename).strip())

    types = polymer_types(polymer)

    lengths = []
    for t in types:
        p = remove_type(polymer, t)
        lengths.append(len(reduce(p)))

    print(min(lengths))
