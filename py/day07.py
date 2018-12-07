import collections


def run_a(filename):
    with open(filename) as fh:
        lines = fh.readlines()
        graph = build_graph(parse(lines))
        lin = linearize(graph)
        print(''.join(lin))


def run_b(filename):
    with open(filename) as fh:
        lines = fh.readlines()
        graph = build_graph(parse(lines))
        time = linearize_work(graph, 5, 60)
        print(time)


def parse(lines):
    pairs = []
    for line in lines:
        parts = line.split()
        pairs.append((parts[1], parts[7]))

    return pairs


def build_graph(pairs):
    graph = collections.defaultdict(list)
    for (a, b) in pairs:
        graph[a].append(b)

    for v in graph.values():
        v.sort()

    return graph


def alphabet(graph):
    alpha = set()
    for k, vs in graph.items():
        alpha.add(k)
        alpha.update(vs)

    return alpha


def find_no_deps(graph):
    alpha = alphabet(graph)
    for deps in graph.values():
        alpha.difference_update(deps)

    return alpha


def find_orphans(graph, task):
    orphans = set(graph[task])

    for k, vs in graph.items():
        if k == task:
            continue
        else:
            orphans.discard(k)
            orphans.difference_update(vs)

    return orphans


def linearize(graph):
    available = find_no_deps(graph)
    lin = []

    while available or graph:
        av = sorted(list(available))
        n = av[0]

        lin.append(n)
        available.remove(n)

        if graph:
            orphans = find_orphans(graph, n)
            available.update(orphans)
            graph.pop(n)
            available.update(find_no_deps(graph))

    return lin


def linearize_work(graph, n_workers, padding):
    available = {
            task: None for task in find_no_deps(graph)
    }

    workers = [ Worker(padding) for _ in range(n_workers) ]
    time = -1

    while available or graph:
        time += 1

        for w in workers:
            w.tick()

        tasks = list(available.keys())
        for task in tasks:
            worker = available[task]
            if worker is not None and worker.is_free():
                del available[task]
                if graph:
                    orphans = find_orphans(graph, task)
                    for o in orphans:
                        if o not in available:
                            available[o] = None

                    graph.pop(task)
                    orphans = find_no_deps(graph)
                    for o in orphans:
                        if o not in available:
                            available[o] = None

        free = [ w for w in workers if w.is_free() ]
        if not free:
            continue

        av = sorted([
            task for (task, worker) in available.items()
            if worker is None
        ])
        for (w, task) in zip(free, av):
            w.assign(task)
            available[task] = w

    while [ w for w in workers if not w.is_free() ]:
        time += 1
        for w in workers:
            w.tick()

    return time


class Worker():

    def __init__(self, padding=0):
        self.task = 0
        self.left = 0
        self.padding = padding

    def tick(self):
        if self.left > 0:
            self.left -= 1

        return self.left

    def assign(self, work):
        self.task = work
        self.left = ord(work) - ord('A') + 1 + self.padding

    def is_free(self):
        return self.left == 0
