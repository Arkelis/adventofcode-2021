def get_energy_map():
    map = {}
    with open("inputs/day11.txt") as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, height in enumerate(line):
                map[x, y] = int(height)
    return map


def adjacents_points(x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            yield x + dx, y + dy


def flash(x, y, energies):
    if not energies.get((x, y)):
        return 0
    
    energies[x, y] += 1
    if energies[x, y] < 10:
        return 0
    
    flashes = 1
    energies[x, y] = 0
    for a, b in adjacents_points(x, y):
        flashes += flash(a, b, energies)
    
    return flashes

def iterate(energies):
    for k in energies:
        energies[k] += 1

    flashes = 0
    for (x, y), energy in energies.items():
        if energy > 9:
            flashes += flash(x, y, energies)
    return flashes
            

def part1():
    flash_count, energies = 0, get_energy_map()
    for _ in range(100):
        flash_count += iterate(energies)
    return flash_count


def part2():
    energies = get_energy_map()
    step = 0
    while True:
        step += 1
        flash_count = iterate(energies)
        if flash_count == len(energies):
            return step


if __name__ == "__main__":
    print(part1())
    print(part2())
