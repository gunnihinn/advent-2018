import unittest

from py.day07 import *

class TestExample(unittest.TestCase):

    def test_parse(self):
        lines = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".strip().split('\n')
        self.assertEqual(parse(lines), [
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E'),
        ])

    def test_build_graph(self):
        pairs = [
            ('C', 'A'),
            ('C', 'F'),
            ('A', 'B'),
            ('A', 'D'),
            ('B', 'E'),
            ('D', 'E'),
            ('F', 'E'),
        ]
        self.assertEqual(build_graph(pairs), {
            'C': ['A', 'F'],
            'A': ['B', 'D'],
            'B': ['E'],
            'D': ['E'],
            'F': ['E'],
        })

    def test_alphabet(self):
        graph = {
            'C': ['A', 'F'],
            'A': ['B', 'D'],
            'B': ['E'],
            'D': ['E'],
            'F': ['E'],
        }
        self.assertEqual(alphabet(graph), set(list('ABCDEF')))

    def test_find_no_deps(self):
        graph = {
            'C': ['A', 'F'],
            'A': ['B', 'D'],
            'B': ['E'],
            'D': ['E'],
            'F': ['E'],
        }
        self.assertEqual(find_no_deps(graph), set(['C']))

    def test_linearize(self):
        graph = {
            'C': ['A', 'F'],
            'A': ['B', 'D'],
            'B': ['E'],
            'D': ['E'],
            'F': ['E'],
        }
        self.assertEqual(linearize(graph), list('CABDFE'))
