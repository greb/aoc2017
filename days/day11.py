dirs = {
    'n':  (0,-1),
    'ne': (1,0),
    'se': (1,1),
    's':  (0,1),
    'sw': (-1,0),
    'nw': (-1,-1)
}

def move(step, pos):
    x, y = pos
    dx,dy = dirs[step]
    return x+dx, y+dy


def dist(pos0, pos1):
    x0,y0 = pos0
    x1,y1 = pos1
    return abs(x0-y0) + abs(x1-y1)

def part1(inp):
    steps = inp.strip().split(',')

    start = (0,0)
    pos = start
    for step in steps:
        pos = move(step, pos)
    return dist(start, pos)


def part2(inp):
    steps = inp.strip().split(',')

    start = (0,0)
    pos = start
    max_dist = 0
    for step in steps:
        pos = move(step, pos)
        curr_dist = dist(start, pos)
        if curr_dist > max_dist:
            max_dist = curr_dist
    return max_dist
