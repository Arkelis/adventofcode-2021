from functools import reduce
from itertools import chain


def get_heightmap():
    map = {}
    with open("inputs/day09.txt") as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, height in enumerate(line):
                map[x, y] = int(height)
    return map


def risk_of_point(x, y, height_map):
    height = height_map[x, y]
    adjacents = filter(lambda x: isinstance(x, int), [
        height_map.get((x + 1, y)),
        height_map.get((x - 1, y)),
        height_map.get((x, y + 1)),
        height_map.get((x, y - 1))])
    return height + 1 if height < min(adjacents) else 0


def part1():
    height_map = get_heightmap()
    return sum(risk_of_point(*coordinates, height_map)
               for coordinates, height in height_map.items())


def part2():
    height_map = get_heightmap()
    
    def find_basin(a, b, basin=frozenset()):
        if height_map.get((a, b)) in (None, 9): 
            return set()
        points_to_explore = (
            coordinates
            for coordinates in ((a + 1, b), (a, b + 1), (a - 1, b), (a, b - 1))
            if coordinates not in basin)
        new_basin = basin | {(a, b)}
        for alpha, beta in points_to_explore:
            new_basin = new_basin | find_basin(alpha, beta, frozenset(new_basin))
        return new_basin

    def basin_size_at(x, y):
        if not risk_of_point(x, y, height_map):
            return 0
        return len(find_basin(x, y))
    
    basin_sizes = (basin_size_at(x, y) for x, y in height_map.keys())
    return reduce(
        lambda acc, el: acc * el,
        sorted(basin_sizes, reverse=True)[:3])


if __name__ == "__main__":
    print(part1())
    print(part2())
