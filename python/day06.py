from collections import Counter
from collections import defaultdict


def get_fish():
    with open("inputs/day06.txt") as f:
        yield from map(int, f.read().split(","))


def population_after(generations):
    current_fish = Counter(get_fish())
    for _ in range(generations):
        new_fish = defaultdict(int)
        for days_remaining, count in current_fish.items():
            if days_remaining == 0:
                new_fish[8] += count
                new_fish[6] += count
            else:
                new_fish[days_remaining - 1] += count
        current_fish = new_fish
    return Counter(current_fish).total()


if __name__ == "__main__":
    print(population_after(80))
    print(population_after(256))
