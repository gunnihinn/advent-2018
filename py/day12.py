from collections import defaultdict
import time

def run_a(filename):
    with open(filename) as fh:
        lines = fh.readlines()
        (rules, plants) = parse(lines)
        print(tick_sum(rules, plants, 20))


def run_b(filename):
    with open(filename) as fh:
        lines = fh.readlines()
        (rules, plants) = parse(lines)
        print(tick_sum(rules, plants, 50000000000))


def print_b(n):
    print('{:b}'.format(n))


def tick(rules, plants, origin):
    m = 3 # m = max(( lowest_bit(r) for r in rules ))
    plants = plants << m
    origin += m

    ng = 0
    i = m-1 # 5 - m?
    while plants:
        if plants & 31 in rules:
            ng |= 1 << i
        plants = plants >> 1
        i += 1

    if ng == 0:
        return (ng, origin)

    while not ng & 1:
        ng = ng >> 1
        origin -= 1

    return (ng, origin)


def lowest_bit(n):
    b = 0
    while not n & 1:
        b += 1
        n = n >> 1

    return b


def highest_bit(n):
    b = 0
    while n:
        b += 1
        n = n >> 1

    return b


def add(plants, origin):
    s = 0
    i = 0
    while plants:
        if plants & 1:
            s += i - origin
        plants = plants >> 1
        i += 1

    return s


def parse(lines):
    plants = rule_to_number(lines[0][15:].strip())

    rules = []
    for line in lines[2:]:
        line = line.strip()
        if line[-1] == '#':
            rules.append(rule_to_number(line[0:5]))

    return (set(rules), plants)


def tick_sum(rules, plants, ticks):
    #import pdb; pdb.set_trace()
    origin = lowest_bit(plants)

    t = time.time()
    for i in range(0, ticks):
        (plants, origin) = tick(rules, plants, origin)

        if i % 1000000 == 0:
            print("{:d}/{:d} rounds done in {:02f} sec".format(i, ticks, time.time() - t))

    return add(plants, origin)

def rule_to_number(rule):
    b = 0
    for i in range(0, len(rule)):
        if rule[i] == '#':
            b |= 1 << i

    return b
