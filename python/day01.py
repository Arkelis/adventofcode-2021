def get_input_ints():
    with open("inputs/day01.txt") as f:
        return [int(x) for x in f.readlines()]


def compare_pairs(L):
    return sum(L[i] < L[i+1] for i in range(len(L)-1))


def part1():
    return compare_pairs(get_input_ints())


def part2():
    ints = get_input_ints()
    sums = [sum(ints[i:i+3]) for i in range(len(ints)-2)]
    return compare_pairs(sums)


print(part1())
print(part2())
