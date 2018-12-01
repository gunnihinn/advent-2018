#!/usr/bin/env python3

import itertools


def read_input(filename):
    with open(filename) as fh:
        return fh.read()


def ev(stack):
    if not stack:
        return 0

    return int("".join(stack))


def get_frequency(blob):
    stack = []
    count = 0
    freqs = set()
    for c in itertools.cycle(blob):
        if c == '+':
            count += ev(stack)
            if count in freqs:
                return count
            else:
                freqs.add(count)

            stack = []

        elif c == '-':
            count += ev(stack)
            if count in freqs:
                return count
            else:
                freqs.add(count)

            stack = [c]

        else:
            stack.append(c)


if __name__ == '__main__':
    blob = read_input('inputs/input-01.txt')
    print(get_frequency(blob))
