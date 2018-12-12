#!/usr/bin/env pypy3

#   #!/usr/bin/env python3

import argparse
import importlib
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Advent of code solutions')
    parser.add_argument('day', type=int, help='Day to run')
    parser.add_argument('--test', help='run tests', action='store_true')
    args = parser.parse_args()

    filename = 'inputs/input-{:02d}.txt'.format(args.day)
    module = 'py.day{:02d}'.format(args.day)

    mod = importlib.import_module(module)

    if args.test:
        os.system('nosetests')
    else:
        mod.run_a(filename)
        mod.run_b(filename)
