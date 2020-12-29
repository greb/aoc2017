factor_a = 16807
factor_b = 48271
divider = 2147483647

def next_val(a, b):
    a = (a * factor_a) % divider
    b = (b * factor_b) % divider
    return a, b

def parse(inp):
    lines = inp.splitlines()
    a = int(lines[0].split()[-1])
    b = int(lines[1].split()[-1])
    return a, b


def next_val_picky(val, factor, picky):
    while True:
        val = (val * factor) % divider
        if val % picky == 0:
            break
    return val


def part1(inp):
    a, b = parse(inp)
    cnt = 0
    for _ in range(40_000_000):
        a,b = next_val(a,b)
        lo_a = a & 0xffff
        lo_b = b & 0xffff
        if lo_a == lo_b:
            cnt += 1
    return cnt


def part2(inp):
    a, b = parse(inp)
    cnt = 0
    for _ in range(5_000_000):
        a = next_val_picky(a, factor_a, 4)
        b = next_val_picky(b, factor_b, 8)
        lo_a = a & 0xffff
        lo_b = b & 0xffff
        if lo_a == lo_b:
            cnt += 1
    return cnt
