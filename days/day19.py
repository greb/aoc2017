dirs = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}

turn_l = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}

turn_r = {
    'N': 'W',
    'E': 'N',
    'S': 'E',
    'W': 'S'
}


def move(pos, direction):
    x,y = pos
    dx, dy = dirs[direction]
    return x+dx, y+dy

def get_tile(pos, grid):
    x, y = pos
    return grid[y][x]

def find_path(grid):
    no_go = ' '
    # Find starting point
    for x, c in enumerate(grid[0]):
        if c != no_go:
            break

    path = []
    direction = 'S'
    pos = (x, 0)
    steps = 0

    tile = get_tile(pos, grid)
    while tile != no_go:
        steps += 1
        if tile == '+':
            if get_tile(move(pos, turn_l[direction]), grid) != no_go:
                direction = turn_l[direction]
            else:
                direction = turn_r[direction]
        elif tile.isalpha():
            path.append(tile)
        pos = move(pos, direction)
        tile = get_tile(pos, grid)
    return ''.join(path), steps


def part1(inp):
    grid = inp.splitlines()
    return find_path(grid)[0]

def part2(inp):
    grid = inp.splitlines()
    return find_path(grid)[1]

