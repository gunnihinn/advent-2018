import unittest

from py.day04 import *


class TestExample(unittest.TestCase):

    lines = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
""".strip().split('\n')

    def test_guards(self):
        gs = guards(TestExample.lines)
        self.assertEqual(len(gs), 2)

    def test_most_sleepy(self):
        gs = guards(TestExample.lines)
        self.assertEqual(most_sleepy(gs).ID, 10)

    def test_most_sleepy_minute(self):
        gs = guards(TestExample.lines)
        g = most_sleepy(gs)
        (m, v) = most_sleepy_minute(g)
        self.assertEqual(m, 24)

    def test_strategy1(self):
        self.assertEqual(strategy1(TestExample.lines), 240)

    def test_strategy2(self):
        self.assertEqual(strategy2(TestExample.lines), 4455)
