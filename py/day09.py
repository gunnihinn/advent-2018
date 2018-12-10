from collections import defaultdict, deque

def run_a(filename):
    print(play(459, 72103))

def run_b(filename):
    print(play(459, 72103 * 100))

def play(players, highest_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, highest_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values())

if __name__ == '__main__':
    run_a('')
