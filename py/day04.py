#!/usr/bin/env python3

import collections
import itertools


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


def run_a(filename):
    lines = read_input(filename)
    print(strategy1(lines))


def run_b(filename):
    lines = read_input(filename)
    print(strategy2(lines))
