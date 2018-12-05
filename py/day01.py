#!/usr/bin/env python3

import sys
import itertools


def read_input(filename):
    with open(filename) as fh:
        return fh.read()


def ev(stack):
    if not stack:
        return 0

    return int("".join(stack))


def a(blob):
    stack = []
    count = 0
    for c in blob:
        if c == '+':
            count += ev(stack)
            stack = []
        elif c == '-':
            count += ev(stack)
            stack = [c]
        else:
            stack.append(c)

    count += ev(stack)

    return count


def b(blob):
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


def run_a(filename):
    blob = read_input(filename)
    print(a(blob))


def run_b(filename):
    blob = read_input(filename)
    print(b(blob))


def test():
    pass


if __name__ == '__main__':
    run(sys.argv[1:])
