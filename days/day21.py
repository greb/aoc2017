def flip(grid):
    return tuple(reversed(grid))

def rot(grid):
    return tuple(''.join(reversed(s)) for s in zip(*grid))

def transforms(grid):
    # Yield all 8 possible transforms
    for _ in range(4):
        grid = rot(grid)
        yield grid
        yield flip(grid)

def parse(inp):
    rules = {}
    for line in inp.splitlines():
        inp, out = line.split(' => ')
        out = tuple(out.split('/'))
        for inp in transforms(inp.split('/')):
            rules[inp] = out
    return rules

def print_grid(grid):
    for row in grid:
        print(row)
    print()

def split(grid):
    l = len(grid)
    bs = 2 if l%2==0 else 3
    n = l // bs

    blocks = []
    for y in range(n):
        for x in range(n):
            block = []
            for by in range(bs):
                block_row = grid[y*bs+by][x*bs:x*bs+bs]
                block.append(block_row)
            blocks.append(tuple(block))
    return n, blocks

def merge(blocks, n):
    bs = len(blocks[0])
    grid = []

    for y in range(n):
        for ry in range(bs):
            row = []
            for x in range(n):
                block = blocks[y*n+x]
                row.append(block[ry])
            grid.append(''.join(row))
    return tuple(grid)

def iteration(grid, rules):
    n, blocks = split(grid)
    blocks = [rules[block] for block in blocks]
    grid = merge(blocks, n)
    return grid

def count_tiles(grid):
    cnt = 0
    for row in grid:
        cnt += sum(tile=='#' for tile in row)
    return cnt


def run_iterations(n, rules):
    grid = [
        '.#.',
        '..#',
        '###'
    ]
    for _ in range(n):
        grid = iteration(grid, rules)

    print_grid(grid)
    return count_tiles(grid)

def part1(inp):
    rules = parse(inp)
    return run_iterations(5, rules)

def part2(inp):
    rules = parse(inp)
    return run_iterations(18, rules)
