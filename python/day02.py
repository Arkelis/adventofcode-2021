from operator import methodcaller


def get_commands():
    with open("inputs/day02.txt") as f:
        yield from ((line[0], int(line[1]))
                    for line in map(methodcaller("split"), f.readlines()))


def apply_command(command, value, position, depth, aim):
    match command:
        case 'forward':
            return position + value, depth, aim
        case 'down':
            return position, depth + value, aim
        case 'up':
            return position, depth - value, aim


def apply_command2(command, value, position, depth, aim):
    match command:
        case 'forward':
            return position + value, depth + aim*value, aim
        case 'down':
            return position, depth, aim + value
        case 'up':
            return position, depth, aim - value


def travel_with(func):
    x, y, aim = 0, 0, 0
    for command, value in get_commands():
        x, y, aim = func(command, value, x, y, aim)
    return x * y


if __name__ == "__main__":
    print(travel_with(apply_command))
    print(travel_with(apply_command2))
