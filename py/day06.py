import collections

def run_a(filename):
    pts = parse(read_input(filename))
    print(largest_area(pts))


def run_b(filename):
    pass


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
    return ( (x,y) for x in range(minX, maxX) for y in range(minY, maxY) )


def manhattan(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


def claim(points):
    pt_to_claim = collections.defaultdict(list)

    for pt in box_points(*corners(points)):
        dist_to_pts = collections.defaultdict(list)
        for p in points:
            dist_to_pts[manhattan(p, pt)].append(p)

        m = min(dist_to_pts.keys())
        if len(dist_to_pts[m]) == 1:
            p = dist_to_pts[m][0]
            pt_to_claim[p].append(pt)

    return pt_to_claim


def smallest_area(points):
    claims = claim(points)
    pts = [ p for p in points if p not in set(boundary(points)) ]
    pts.sort(key=lambda p: len(claims[p]))

    return len(claims[pts[0]])


def largest_area(points):
    claims = claim(points)
    pts = [ p for p in points if p not in set(boundary(points)) ]
    pts.sort(key=lambda p: len(claims[p]), reverse=True)

    if pts[0] in boundary(points):
        raise Exception('Got boundary point')

    return len(claims[pts[0]])
