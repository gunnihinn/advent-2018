import re


def run_a(filename):
    with open(filename) as fh:
        lines = fh.readlines()

        points = []
        for line in lines:
            points.append(Point.from_line(line))

        ys = []
        match = 0
        for _ in range(0, 50000):
            [ p.tick() for p in points ]
            s = y_spread(points)
            ys.append(s)

            if s == 9 or s == 19:
                match += 1
                if match == 2:
                    print_box(points)
                    break

        ys.sort()
        print(ys[0:10])


def run_b(filename):
    with open(filename) as fh:
        lines = fh.readlines()

        points = []
        for line in lines:
            points.append(Point.from_line(line))

        ys = []
        match = 0
        for i in range(0, 50000):
            [ p.tick() for p in points ]
            s = y_spread(points)
            ys.append(s)

            if s == 9 or s == 19:
                match += 1
                if match == 2:
                    print(i)
                    break


class Point():

    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.vx = a
        self.vy = b

    def tick(self):
        self.x += self.vx
        self.y += self.vy

    def xy(self):
        return (self.x, self.y)

    @staticmethod
    def from_line(line):
        xyab = list(map(int, [ d for d in re.split(r'[a-z=<> ,]', line) if d and d != '\n' ]))
        return Point(*xyab)


def y_spread(points):
    ys = set([ p.y for p in points ])

    return max(ys) - min(ys)


def is_message(points):
    return y_spread(points) == 7


def print_box(points):
    pts = set([ p.xy() for p in points ])

    for y in range(min(b for (a,b) in pts), max(b for (a,b) in pts)+1):
        for x in range(min(a for (a,b) in pts), max(a for (a,b) in pts)+1):
            if (x,y) in pts:
                print('x', end='')
            else:
                print(' ', end='')
        print('\n', end='')

lines = """
position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>
""".strip().split('\n')

if __name__ == '__main__':
    points = []
    for line in lines:
        points.append(Point.from_line(line))

    for i in range(0,6):
        if is_message(points):
            print(i)
