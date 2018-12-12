import unittest

from py.day12 import *

class TestExample(unittest.TestCase):

    def test_add(self):
        plants = rule_to_number('.#....##....#####...#######....#.#..##.')
        hits = [0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
        b = 0
        for (i, h) in enumerate(hits):
            if h:
                b |= 1 << i

        self.assertEqual(plants, b)
        self.assertEqual(lowest_bit(plants), 1)
        self.assertEqual(add(plants, 3), 325)

    def test_lowest_bit(self):
        self.assertEqual(lowest_bit(1), 0)
        self.assertEqual(lowest_bit(2), 1)
        self.assertEqual(lowest_bit(3), 0)
        self.assertEqual(lowest_bit(4), 2)
        self.assertEqual(lowest_bit(5), 0)
        self.assertEqual(lowest_bit(6), 1)
        self.assertEqual(lowest_bit(7), 0)
        self.assertEqual(lowest_bit(8), 3)
        self.assertEqual(lowest_bit(9), 0)

    def test_highest_bit(self):
        self.assertEqual(highest_bit(1), 1)
        self.assertEqual(highest_bit(2), 2)
        self.assertEqual(highest_bit(3), 2)
        self.assertEqual(highest_bit(4), 3)
        self.assertEqual(highest_bit(5), 3)
        self.assertEqual(highest_bit(6), 3)
        self.assertEqual(highest_bit(7), 3)
        self.assertEqual(highest_bit(8), 4)
        self.assertEqual(highest_bit(9), 4)

    def test_rule_to_number(self):
        self.assertEqual(rule_to_number('...##'), 24)
        self.assertEqual(rule_to_number('..#..'), 4)
        self.assertEqual(rule_to_number('.#...'), 2)
        self.assertEqual(rule_to_number('#.###'), 29)

    def test_parse(self):
        lines = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".strip().split('\n')

        (rules, plants) = parse(lines)
        self.assertEqual(len(rules), 14)

        hits = [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1]
        b = 0
        for (i, h) in enumerate(hits):
            if h:
                b |= 1 << i
        self.assertEqual(plants, b)

        def test_tick(self):
            lines = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".strip().split('\n')

        (rules, plants) = parse(lines)
        (ng_plants, ng_origin) = tick(rules, plants, 0)
        self.assertEqual(ng_plants, rule_to_number('#...#....#.....#..#..#..#'))
        self.assertEqual(ng_origin, 0)


        def test_sum_tick(self):
            lines = """
initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".strip().split('\n')

        (rules, plants) = parse(lines)
        self.assertEqual(tick_sum(rules, plants, 20), 325)



if __name__ == '__main__':
    unittest.main()
