from itertools import cycle


def get_dots():
    with open("inputs/day13.txt") as f:
        coords, _, folds = f.read().partition("\n\n")
    dots_map = {
        tuple(map(int, coord.strip().split(",")))
        for coord in coords.splitlines()}
    instructions = []
    for fold in folds.splitlines():
        axe, val = fold.removeprefix("fold along ").split("=")
        instructions.append((axe, int(val)))
    return dots_map, tuple(instructions)


def get_mirror(x, y, axe, val):
    if ((axe == "x" and x < val)
            or (axe == "y" and y < val)):
        return (x, y)
    if axe == "x":
        return (x + (val-x)*2, y)
    else:
        return (x, y + (val-y)*2)


def fold(dots, instruction):
    for coord in list(dots):
        dots.remove(coord)
        dots.add(get_mirror(*coord, *instruction))


def part1():
    dots, folds = get_dots()
    instruction = folds[0]
    fold(dots, instruction)
    return len(dots)



def part2():
    dots, folds = get_dots()
    for instruction in folds:
        fold(dots, instruction)
    max_x = max(t[0] for t in dots)
    max_y = max(t[1] for t in dots)
    screen = [
        ["#" if (x, y) in dots else " "
         for x in range(max_x + 1)]
        for y in range(max_y + 1)]
    return "\n".join("".join(line) for line in screen)


if __name__ == "__main__":
    print(part1())
    print(part2())
