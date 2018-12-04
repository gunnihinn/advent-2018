#!/usr/bin/env python3

import collections
import itertools
import unittest


class Guard():

    def __init__(self, ID):
        self.ID = ID
        self.slept = 60 * [0]

    def __str__(self):
        return "{}: {}".format(self.ID, self.slept)

    def __repr__(self):
        return self.__str__()

    def sleep(self, start, end):
        for m in range(start, end):
            self.slept[m] += 1


def read_input(filename):
    with open(filename) as fh:
        return fh.readlines()


def guards(lines):
    gs = {}

    ID = None
    start = None
    end = None

    for line in lines:
        (timestamp, message) = (line[0:18], line[19:])
        minute = int(timestamp[-3:-1])

        if message.startswith('Guard'):
            parts = message.split()
            ID = int(parts[1][1:])
        elif message.startswith('falls'):
            start = minute
        else:
            end = minute
            if ID not in gs:
                gs[ID] = Guard(ID)

            gs[ID].sleep(start, end)

    return gs.values()


def most_sleepy(guards):
    return sorted(guards, key=lambda g: sum(g.slept), reverse=True)[0]

def most_sleepy_minute(guard):
    minute = 0
    maxSleep = 0
    for (m, v) in enumerate(guard.slept):
        if v > maxSleep:
            minute = m
            maxSleep = v

    return (minute, maxSleep)

def strategy1(lines):
    lines.sort()
    gs = guards(lines)
    g = most_sleepy(gs)
    (m, v) = most_sleepy_minute(g)

    return g.ID * m


def strategy2(lines):
    lines.sort()
    gs = guards(lines)

    minute = 0
    sleep = 0
    ID = 0

    for g in gs:
        (m, v) = most_sleepy_minute(g)
        if v > sleep:
            sleep = v
            minute = m
            ID = g.ID

    return ID * minute


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

if __name__ == '__main__':
    #unittest.main()
    lines = read_input('inputs/input-04.txt')
    print(strategy2(lines))
