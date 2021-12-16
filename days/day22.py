dirs = {
    'N': (0, -1),
    'E': (1, 0),
    'S': (0, 1),
    'W': (-1, 0),
}

turn_r = {
    'N': 'E',
    'E': 'S',
    'S': 'W',
    'W': 'N',
}

turn_l = {
    'N': 'W',
    'E': 'N',
    'S': 'E',
    'W': 'S'
}

rev = {
    'N': 'S',
    'E': 'W',
    'S': 'N',
    'W': 'E'
}

def move(pos, d):
    x,y = pos
    dx, dy = dirs[d]
    return x+dx, y+dy


def parse(inp):
    lines = inp.splitlines()

    infected = dict()
    for y, row in enumerate(lines):
        for x, tile in enumerate(row):
            if tile == '#':
                infected[(x,y)] = 'I'
    return x, y, infected


def part1(inp):
    width, height, infected = parse(inp)

    cnt_inf = 0
    d = 'N'
    pos = width//2, height//2
    for _ in range(10_000):
        if pos in infected:
            d = turn_r[d]
            del infected[pos]
        else:
            d = turn_l[d]
            infected[pos] = 'I'
            cnt_inf += 1
        pos = move(pos, d)

    return cnt_inf


def part2(inp):
    width, height, infected = parse(inp)

    cnt_inf = 0
    d = 'N'
    pos = width//2, height//2

    for _ in range(10_000_000):
        status = infected.get(pos)

        if status is None:
            d = turn_l[d]
            infected[pos] = 'W'

        elif status == 'W':
            cnt_inf += 1
            infected[pos] = 'I'

        elif status == 'I':
            d = turn_r[d]
            infected[pos] = 'F'

        elif status == 'F':
            d = rev[d]
            del infected[pos]

        pos = move(pos, d)
    return cnt_inf
