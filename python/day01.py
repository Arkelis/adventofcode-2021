def get_measurements():
    with open("inputs/day01.txt") as f:
        return [int(x) for x in f.readlines()]


def compare_pairs(L):
    return sum(L[i] < L[i+1] for i in range(len(L)-1))


def part1():
    return compare_pairs(get_measurements())


def part2():
    measurements = get_measurements()
    sums = [sum(measurements[i:i+3]) for i in range(len(measurements)-2)]
    return compare_pairs(sums)


if __name__ == "__main__":
    print(part1())
    print(part2())
