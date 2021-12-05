from collections import defaultdict
from operator import eq


def get_lines():
    with open("inputs/day05.txt") as f:
        yield from (
            sorted(
                tuple(map(int, coordinates))
                for coordinates in (t.split(",")
                                    for t in line.split(" -> ")))
            for line in f.readlines())


def detect(lines, part2=False):
    wind_map = defaultdict(int)
    for [(x1, y1), (x2, y2)] in get_lines():
        if x1 == x2:
            for y in range(y1, y2 + 1):
                wind_map[(x1, y)] += 1
        elif y1 == y2:
            for x in range(x1, x2 + 1):
                wind_map[(x, y1)] += 1
        elif part2 and x2 - x1 == y2 - y1:
            for x in range(x2 - x1 + 1):
                wind_map[(x1 + x, y1 + x)] += 1
        elif part2 and x2 - x1 == y1 - y2:
            for x in range(x2 - x1 + 1):
                wind_map[(x1 + x, y1 - x)] += 1
        elif part2:
            print(f"[({x1}, {y1}), ({x2}, {y2})]")
    return sum(map(lambda p: p > 1, wind_map.values()))


if __name__ == '__main__':
    print(detect(get_lines()))
    print(detect(get_lines(), part2=True))
