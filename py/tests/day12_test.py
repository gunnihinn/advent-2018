import unittest

from py.day12 import *

class TestExample(unittest.TestCase):

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
