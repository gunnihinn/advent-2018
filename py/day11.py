import itertools

def run_a(filename):
    s = square(power(9798))
    print(max_square(s, 3))

def run_b(filename):
    s = square(power(9798))
    print(total_square(s))

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

def square(power):
    """Compute the power of an lxl square whose top-left coordinate is (x,y)."""
    cache = {}

    def _s(x, y, l):
        if l == 0:
            return 0

        if (x, y, l) not in cache:
            cache[(x, y, l)] = power(x+l-1, y+l-1) \
                    + sum(( power(_x, y+l-1) for _x in range(x, x+l-1) )) \
                    + sum(( power(x+l-1, _y) for _y in range(y, y+l-1) )) \
                    + _s(x, y, l-1)

        if (x, y, l-1) in cache:
            del cache[(x, y, l-1)]

        return cache[(x, y, l)]

    return _s

def max_square(square, l):
    """Compute the (x,y) coordinates of the biggest square lxl square."""
    (maxX, maxY) = (0, 0)
    maxPower = 0

    for (x, y) in itertools.product(range(1, 301-l), range(1, 301-l)):
        if square(x, y, l) > maxPower:
            (maxX, maxY) = (x, y)
            maxPower = square(x, y, l)

    return (maxX, maxY)

def total_square(square):
    (maxX, maxY) = (0, 0)
    maxPower = 0
    maxSize = 0

    for size in range(1, 300):
        print("Checking size", size)
        (x, y) = max_square(square, size)
        if square(x, y, size) > maxPower:
            (maxX, maxY) = (x, y)
            maxPower = square(x, y, size)
            maxSize = size

    return (maxX, maxY, maxSize)
