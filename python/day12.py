from collections import defaultdict


def build_map():
    caves_map = defaultdict(set)
    with open("inputs/day12.txt") as f:
        lines = f.read().splitlines()
    for line in lines:
        origin, destination = line.split("-")
        if origin != "end" and destination != "start":
            caves_map[origin].add(destination)
        if origin != "start" and destination != "end":
            caves_map[destination].add(origin)
    return caves_map


def crawl(path, caves_map, can_revisit, small_caves_visits=frozenset()):
    cave = path[-1]
    if cave == "end":
        return 1
    paths = 0

    new_small_caves_visits = frozenset(
        small_caves_visits | ({cave} if cave.islower() else set()))

    for next_cave in caves_map[cave]:
        if next_cave not in small_caves_visits:
            paths += crawl(path + [next_cave], caves_map, can_revisit, new_small_caves_visits)
        elif next_cave in small_caves_visits and can_revisit:
            paths += crawl(path + [next_cave], caves_map, False, new_small_caves_visits)
    
    return paths


def find_paths_with_threshold(can_revisit):
    caves_map = build_map()
    paths = crawl(["start"], caves_map, can_revisit)
    return paths


if __name__ == "__main__":
    print(find_paths_with_threshold(can_revisit=False))
    print(find_paths_with_threshold(can_revisit=True))
