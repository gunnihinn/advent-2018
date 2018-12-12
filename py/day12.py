def run_a(filename):
    with open(filename) as fh:
        lines = fh.readlines()
        (rules, plants) = parse(lines)
        print(tick_sum(rules, plants, 20))

def run_b(filename):
    pass

def tick(rules, plants):
    #import pdb; pdb.set_trace()
    ng = ''
    ps = '....' + plants + '....'

    for i in range(0, len(ps) - 2):
        p = ps[i-2:i+3]
        if p in rules:
            ng += '#'
        else:
            ng += '.'

    return ng

def add(plants, origin):
    s = 0
    for i in range(0, len(plants)):
        if plants[i] == '#':
            s += i - origin

    return s

def parse(lines):
    rules = []

    plants = lines[0][15:].strip()
    for line in lines[2:]:
        line = line.strip()
        if line[-1] == '#':
            rules.append(line[0:5])

    return (set(rules), plants)

def tick_sum(rules, plants, ticks):
    ng = plants
    for _ in range(0, ticks):
        ng = tick(rules, ng)

    return add(ng, 4 * ticks)
