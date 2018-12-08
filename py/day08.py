def run_a(filename):
    with open(filename) as fh:
        items = list(map(int, fh.read().split()))
        items.reverse()

    t = parse(items)
    print(t.sum())


def run_b(filename):
    with open(filename) as fh:
        items = list(map(int, fh.read().split()))
        items.reverse()

    t = parse(items)
    print(t.value())

def parse(items):
    c = items.pop()
    m = items.pop()
    t = Tree()

    for _ in range(c):
        t.adopt(parse(items))

    for _ in range(m):
        t.meta(items.pop())

    return t


class Tree():

    def __init__(self):
        self.children = []
        self.metadata = []

    def __eq__(self, other):
        return len(self.children) == len(other.children) and \
            all(c == d for (c,d) in zip(self.children, other.children)) and \
            self.metadata == other.metadata

    def adopt(self, child):
        self.children.append(child)

    def meta(self, meta):
        self.metadata.append(meta)

    def sum(self):
        return sum( c.sum() for c in self.children ) + sum(self.metadata)

    def value(self):
        if not self.children:
            return sum(self.metadata)

        v = 0
        for m in [m for m in self.metadata if m]:
            try:
                c = self.children[m-1]
            except IndexError:
                continue
            v += c.value()

        return v
