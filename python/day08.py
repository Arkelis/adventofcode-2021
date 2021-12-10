from itertools import chain
from functools import reduce


def extract_digits_with_len(n, digits):
    predicate = lambda d: len(d) == n
    filtered = list(map(set, filter(predicate, digits)))
    if len(filtered) == 1:
        filtered = filtered[0]
    return filtered


def get_digits_and_outputs():
    with open("inputs/day08.txt") as f:
        yield from (tuple(x.split(" ") for x in line.split(" | "))
                    for line in f.read().splitlines())


def part1():
    def int_of_output(output):
        match len(output):
            case 2: return 1
            case 4: return 4
            case 3: return 7
            case 7: return 8
            case _: return None

    parsed_ints = chain.from_iterable(
        map(int_of_output, outputs)
        for _, outputs in get_digits_and_outputs())

    return sum(map(bool, parsed_ints))


def get_normalized_output(digits, outputs):
    one = extract_digits_with_len(2, digits)
    seven = extract_digits_with_len(3, digits)
    four = extract_digits_with_len(4, digits)
    eight = extract_digits_with_len(7, digits)
    two_three_five = extract_digits_with_len(5, digits)
    zero_six_nine = extract_digits_with_len(6, digits)

    a = seven - one
    dg = reduce(set.intersection, two_three_five) - a
    bd = four - seven
    eg  = eight - seven - four
    g = dg & eg
    d = dg - g
    e = eg - g
    b = bd - d
    f = reduce(set.intersection, zero_six_nine) - (a | b | g)
    c = one - f
    
    conversion_map = {
        next(iter(a)): 'a',
        next(iter(b)): 'b',
        next(iter(c)): 'c',
        next(iter(d)): 'd',
        next(iter(e)): 'e',
        next(iter(f)): 'f',
        next(iter(g)): 'g'}

    return ({conversion_map[val] for val in output} for output in outputs)


def part2():
    def digit_of_output(output):
        if output == {'a', 'c', 'f', 'g', 'b', 'e'}: return "0"
        elif output == {'c', 'f'}: return "1"
        elif output == {'a', 'c', 'd', 'g', 'e'}: return "2"
        elif output == {'a', 'c', 'd', 'f', 'g'}: return "3"
        elif output == {'b', 'c', 'f', 'd'}: return "4"
        elif output == {'a', 'b', 'f', 'g', 'd'}: return "5"
        elif output == {'a', 'b', 'f', 'g', 'd', 'e'}: return "6"
        elif output == {'a', 'c', 'f'}: return "7"
        elif output == {'a', 'c', 'f', 'g', 'b', 'e', 'd'}: return "8"
        elif output == {'a', 'b', 'c', 'd', 'f', 'g'}: return "9"

    parsed_ints = (
        int("".join(ints)) for ints in (
            map(digit_of_output, get_normalized_output(digits, outputs))
            for digits, outputs in get_digits_and_outputs()))

    return sum(parsed_ints)


if __name__ == "__main__":
    print(part1())
    print(part2())