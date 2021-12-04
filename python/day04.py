import re


class Board:
    def __init__(self, rows):
        self.rows = [
            {val: False for val in row}
            for row in rows]
        self.index = ({
            val: (row_index, col_index)
            for row_index, row in enumerate(self.rows)
            for col_index, val in enumerate(row)})
        self.bingo = False

    def column(self, index):
        return {list(row)[index]: list(row.values())[index] for row in self.rows}

    def check(self, n):
        coordinates = self.index.get(n)
        if coordinates is None:
            return
        self.rows[coordinates[0]][n] = True
        self.check_bingo(coordinates)

    def check_bingo(self, coordinates):
        for series in self.rows[coordinates[0]], self.column(coordinates[1]):
            if all(series.values()):
                self.bingo = True
                return

    def result(self, last_called):
        unchecked_sum = sum(
            n
            for row in self.rows
            for n, checked in row.items()
            if not checked)
        return unchecked_sum * last_called

    def __repr__(self):
        return self.rows.__repr__()


def get_game_data():
    with open("inputs/day04.txt") as f:
        lines = f.readlines()
        numbers = map(int, lines[0].split(","))
        boards = [[]]
        for line in lines[2:]:
            if line == '\n':
                boards.append([])
                continue
            boards[-1].append([
                int(digit)
                for digit in re.findall(r"\d+", line)])
    return list(numbers), [Board(board) for board in boards]


def part1():
    numbers, boards = get_game_data()
    for n in numbers:
        for b in boards:
            b.check(n)
            if b.bingo:
                return b.result(n)


def part2():
    numbers, boards = get_game_data()
    won_boards = []
    for n in numbers:
        for i, b in enumerate(boards):
            if i in won_boards:
                continue
            b.check(n)
            if b.bingo:
                if len(won_boards) < len(boards) - 1:
                    won_boards.append(i)
                else:
                    return b.result(n)


if __name__ == '__main__':
    print(part1())
    print(part2())
