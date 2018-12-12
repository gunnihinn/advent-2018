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

def tick(rules, plants, origin):
    plants = plants << 5
    origin += 5

    ng = 0
    m = highest_bit(plants)
    for i in range(m+1):
        plants >> 1
        for rule in rules:
            if (plants & rule) == rule:
                ng |= 1 << i

    if ng == 0:
        return (ng, origin)

    while not (ng & 1):
        ng >> 1
        origin -= 1

    return (ng, origin)


def highest_bit(n):
    if n == 0:
        return 0

    m = 1
    while 1 << m <= n:
        if m == n:
            return m
        else:
            m += 1

    return m


def add(plants, origin):
    s = 0
    for i in range(highest_bit(plants) + 1):
        if plants & 1 << i:
            s += i - origin

    return s

def parse(lines):
    plants = 0
    for (i, p) in enumerate(lines[0][15:].strip()):
        if p == '#':
            plants |= 1 << i

    rules = []
    for line in lines[2:]:
        line = line.strip()
        if line[-1] == '#':
            rules.append(rule_to_number(line[0:5]))

    return (rules, plants)

def first_set_bit(n):
    if n == 0:
        return 0

    o = 0
    while not n & 1 << o:
        o += 1

    return o


def reverse(n):
    if n == 0:
        return 0

    o = 1
    while 1 << o <= n:
        if 1 << o == n:
            return n-1
        elif 1 << o < n:
            o += 1

    return ~n + (1 << o)


def tick_sum(rules, plants, ticks):
    #import pdb; pdb.set_trace()
    plants = reverse(plants)
    origin = first_set_bit(plants)

    a = time.time()
    for i in range(0, ticks):
        (plants, origin) = tick(rules, plants, origin)
        if i % 100000 == 0:
            print(ticks - i, "left")
            print("Have run for ", time.time() - a, "seconds")

    plants = reverse(plants)

    return add(plants, origin)

def rule_to_number(rule):
    b = 0
    for i in range(0, len(rule)):
        if rule[i] == '#':
            b |= 1 << i

    return b

def to_number(part):
    b = 0
    for i in range(0, len(part)):
        if part[i]:
            b |= 1 << i

    return b
