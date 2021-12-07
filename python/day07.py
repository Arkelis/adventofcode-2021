def get_positions():
    with open("inputs/day07.txt") as f:
        yield from map(int, f.readline().split(","))


def fuel_calculator_linear(dist):
    return abs(dist)


def fuel_calculator_sum(dist):
    n = abs(dist)
    return n * (n + 1) // 2


def get_optimal_position_using(fuel_calculator):
    positions = list(get_positions())
    return min(*(sum(fuel_calculator(x - pos) for pos in positions)
                 for x in range(min(positions), max(positions) + 1)))


if __name__ == "__main__":
    print(get_optimal_position_using(fuel_calculator_linear))
    print(get_optimal_position_using(fuel_calculator_sum))