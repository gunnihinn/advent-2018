def run_a(filename):
    pass

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
