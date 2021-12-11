from functools import reduce


def get_lines():
    with open("inputs/day10.txt") as f:
        yield from f.read().splitlines()


def closing_for(char):
    match char:
        case '(': return ')'
        case '[': return ']'
        case '{': return '}'
        case '<': return '>'


def illegal_score_for(char):
    match char:
        case ')': return 3
        case ']': return 57
        case '}': return 1197
        case '>': return 25137


def complete_score_for(char):
    match char:
        case '(': return 1
        case '[': return 2
        case '{': return 3
        case '<': return 4


def score_of_line(line):
    opened = []
    for char in line:
        if closing_for(char) is not None:
            opened.append(char)
        elif closing_for(opened[-1]) == char:
            opened.pop()
        else:
            return False, illegal_score_for(char)
    return True, reduce(
        lambda acc, el: acc * 5 + complete_score_for(el),
        reversed(opened),
        0)


def part1():
    total_score = 0
    for line in get_lines():
        legal, score = score_of_line(line)
        total_score += score * (not legal)
    return total_score


def part2():
    scores = []
    for line in get_lines():
        legal, score = score_of_line(line)
        if legal:
            scores.append(score)
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    print(part1())
    print(part2())
