from collections import defaultdict
import collections

def run_a(filename):
    pts = parse(read_input(filename))
    print(largest_area(pts))


def run_b(filename):
    points = parse(read_input(filename))
    box = box_points(*corners(points))
    area = 0
    for p in box:
        if total_distance(p, points) < 10000:
            area += 1

    print(area)


def read_input(filename):
    with open(filename) as fh:
        return fh.readlines()


def parse(lines):
    pts = []
    for line in lines:
        (x, y) = line.split(', ')
        pts.append((int(x), int(y)))

    return pts


def corners(points):
    minX = min(( x for (x,y) in points))
    maxX = max(( x for (x,y) in points))
    minY = min(( y for (x,y) in points))
    maxY = max(( y for (x,y) in points))

    return (minX, maxX, minY, maxY)


def boundary(points):
    (minX, maxX, minY, maxY) = corners(points)

    return set([
            (x,y) for (x,y) in points
            if x == minX or x == maxX or y == minY or y == maxY
    ])


def box_points(minX, maxX, minY, maxY):
    return [ (x,y) for x in range(minX, maxX) for y in range(minY, maxY) ]


def manhattan(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


def claim(points):
    pt_to_area = collections.defaultdict(int)

    box = box_points(*corners(points))

    for p in box:
        distance = collections.defaultdict(list)
        for q in points:
            distance[manhattan(p, q)].append(q)

        m = min(distance.keys())
        if len(distance[m]) == 1:
            q = distance[m][0]
            pt_to_area[q] += 1

    return pt_to_area


def smallest_area(points):
    areas = claim(points)
    pts = [ p for p in points if p not in set(boundary(points)) ]
    pts.sort(key=lambda p: areas[p])

    return areas[pts[0]]


def largest_area(points):
    areas = claim(points)
    pts = [ p for p in points if p not in set(boundary(points)) ]
    pts.sort(key=lambda p: areas[p], reverse=True)

    for p in pts[0:5]:
        print(p, areas[p])

    return areas[pts[0]]


def total_distance(p, points):
    return sum(( manhattan(p, q) for q in points ))


def total_area(points, limit):
    box = box_points(*corners(points))
    area = 0
    for p in box:
        if total_distance(p, points) < limit:
            area += 1

    return area
