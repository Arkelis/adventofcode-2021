def get_bins():
    with open("inputs/day03.txt") as f:
        return f.read().splitlines()


def count_bits(bins):
    counter = [0] * len(bins[0])
    for binary in bins:
        for i, digit in enumerate(binary):
            counter[i] += digit == "1"
    return counter


def compute_rates(counter):
    threshold = len(bins) // 2 + 1
    gamma = "".join(str(int(val >= threshold)) for val in counter)
    epsilon = "".join(str(int(not int(val))) for val in gamma)
    return int(gamma, 2), int(epsilon, 2)


def part1():
    bins = get_bins()
    counter = count_bits(bins)
    gamma, epsilon = compute_rates(counter)
    return gamma * epsilon


def to_keep(bins, one_count, most_or_least):
    match most_or_least:
        case "least":
            return "0" if one_count >= len(bins) / 2 else "1"
        case "most":
            return "1" if one_count >= len(bins) / 2 else "0"


def filter_binaries(bins, most_or_least):
    index = 0
    while len(bins) > 1:
        one_count = sum(binary[index] == "1" for binary in bins)
        bins = [binary for binary in bins if binary[index] == to_keep(bins, one_count, most_or_least)]
        index += 1
    return int(bins[0], 2)


def part2():
    bins = get_bins()
    ogr = filter_binaries(list(bins), "most")
    csr = filter_binaries(list(bins), "least")
    return ogr * csr


if __name__ == '__main__':
    print(part1())
    print(part2())
