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
        self.assertEqual(plants, '#..#.#..##......###...###')

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
