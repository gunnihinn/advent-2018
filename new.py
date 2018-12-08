#!/usr/bin/env python3

import argparse
import os

def py(day):
    return """
def run_a(filename):
    pass

def run_b(filename):
    pass
"""

def test(day):
    return """
import unittest

from py.day{:02d} import *

class TestExample(unittest.TestCase):

    def test_nothing(self):
        pass
""".format(day)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create Advent of code solutions')
    parser.add_argument('day', type=int, help='Day to create')
    args = parser.parse_args()

    pyfile = 'py/day{:02d}.py'.format(args.day)
    testfile = 'py/tests/day{:02d}_test.py'.format(args.day)

    with open(pyfile, 'w') as fh:
        fh.write(py(args.day))

    with open(testfile, 'w') as fh:
        fh.write(test(args.day))
