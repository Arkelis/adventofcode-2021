from bisect import insort
from itertools import product
from operator import itemgetter


def get_map():
    risk_map = {}
    with open("inputs/day15.txt") as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, risk in enumerate(line):
                risk_map[x, y] = int(risk)
    return x, y, risk_map


def get_extended_map():
    max_x, max_y, risk_map = get_map()
    for (x, y), val in list(risk_map.items()):
        for xx, yy in product(range(5), range(5)):
            if (xx, yy) == (0, 0):
                continue
            risk_map[x + xx*(max_x+1), y + yy*(max_y+1)] = (val + (xx+yy)) % 9 or 9
    return (max_x+1)*5 - 1, (max_y+1)*5 - 1, risk_map


def neighbours_of(x, y, max_x, max_y, considered):
    for dx, dy in product(range(-1, 2), range(-1, 2)):
        if ((x+dx, y+dy) in considered
                or dx == 0 and dy == 0
                or dx != 0 and dy != 0
                or not 0 <= x + dx <= max_x
                or not 0 <= y + dy <= max_y):
            continue
        yield (x+dx, y+dy) 


def roam(max_x, max_y, risk_map, acc_risks=None, considered=None):
    acc_risks = []
    considered = {(0, 0)}
    x, y, lower_risk = 0, 0, 0

    while (x, y) != (max_x, max_y):
        for xx, yy in neighbours_of(x, y, max_x, max_y, considered):
            considered.add((xx, yy))
            insort(
                acc_risks,
                (xx, yy, lower_risk + risk_map[xx, yy]),
                key=itemgetter(2))
        x, y, lower_risk = acc_risks.pop(0)
    
    return lower_risk


if __name__ == "__main__":
    print(roam(*get_map()))
    print(roam(*get_extended_map()))
