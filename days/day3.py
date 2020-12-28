import itertools

def gen_spiral_coords():
    x, y = 0, 0
    yield x,y

    dirs = itertools.cycle([(1, 0), (0, -1), (-1, 0), (0, 1)])
    n = 1
    while True:
        for _ in range(2):
            dx, dy = next(dirs)
            for _ in range(n):
                x += dx
                y += dy
                yield (x, y)
        n+=1

def gen_ocatal_neighbors(pos):
    x,y = pos
    dirs = [(1,0), (1,-1), (0, -1), (-1, -1), (-1, 0), (-1,1), (0,1), (1,1)]
    for dx, dy in dirs:
        yield x+dx, y+dy

def part1(inp):
    target = int(inp.strip())

    coords = gen_spiral_coords()
    for _ in range(target):
        coord = next(coords)
    return abs(coord[0]) + abs(coord[1])

def part2(inp):
    target = int(inp.strip())
    coords = gen_spiral_coords()

    coord = next(coords)
    val = 1
    vals = {coord: val}

    while val < target:
        coord = next(coords)
        val   = sum(vals.get(n, 0) for n in gen_ocatal_neighbors(coord))
        vals[coord] = val
    return val

