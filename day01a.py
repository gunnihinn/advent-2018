#!/usr/bin/env python3


def read_input(filename):
    with open(filename) as fh:
        return fh.read()


def ev(stack):
    if not stack:
        return 0

    return int("".join(stack))


if __name__ == '__main__':
    blob = read_input('inputs/input-01.txt')

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

    print(count)
