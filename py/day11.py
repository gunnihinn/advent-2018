import itertools

def run_a(filename):
    print(max_square(9798))

def run_b(filename):
    pass

def power_level(x, y, serial):
    rack_id = x + 10
    level = rack_id * y
    level += serial
    level *= rack_id
    level = int(level / 100)
    level = level % 10

    return level - 5

def power(serial):
    """Return a function that computes the power of an (x,y) coordinate for the
    given serial number."""
    cache = {}

    def _p(x, y):
        if (x,y) not in cache:
            cache[(x,y)] = power_level(x, y, serial)

        return cache[(x,y)]

    return _p

def square(power, x, y):
    """Compute the power of a 3x3 square whose top-left coordinate is (x,y)."""
    return sum((
        power(_x, _y)
        for _x in range(x, x+3)
        for _y in range(y, y+3)
    ))

def max_square(serial):
    p = power(serial)

    (maxX, maxY) = (0, 0)
    maxPower = 0

    for (x, y) in itertools.product(range(1, 298), range(1, 298)):
        if square(p, x, y) > maxPower:
            (maxX, maxY) = (x, y)
            maxPower = square(p, x, y)

    return (maxX, maxY)
