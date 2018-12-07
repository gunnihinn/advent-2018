import collections


def run_a(filename):
    with open(filename) as fh:
        lines = fh.readlines()
        graph = build_graph(parse(lines))
        lin = linearize(graph)
        print(''.join(lin))


def run_b(filename):
    pass


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


        available.update(find_no_deps(graph))

    if deps:
        lin += sorted(deps)

    return lin
