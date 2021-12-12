from collections import Counter
from collections import deque


def get_fish():
    with open("inputs/day06.txt") as f:
        yield from map(int, f.read().split(","))


def population_after(generations):
    fish_count = Counter(get_fish())
    population = deque([fish_count[k] for k in range(9)])
    for _ in range(generations):
        zeros = population.popleft()
        population.append(zeros)
        population[6] += zeros
    return sum(population)


if __name__ == "__main__":
    print(population_after(80))
    print(population_after(256))
