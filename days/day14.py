def reverse_segement(lst, start, length):
    l = len(lst)
    for i in range(length//2):
        a = (start+i) % l
        b = (start+(length-i-1)) % l
        lst[a], lst[b] = lst[b], lst[a]

def twist(lst, lengths, rounds=1):
    idx = 0
    skip = 0
    for _ in range(rounds):
        for length in lengths:
            reverse_segement(lst, idx, length)
            idx += skip + length
            skip += 1

def compute_hash(s):
    lengths = [ord(c) for c in s]
    lengths.extend([17,31,73,47,23])

    lst = list(range(256))
    twist(lst, lengths, 64)

    buf = []
    for i in range(0, 256, 16):
        chunk = lst[i:i+16]
        val = 0
        for v in chunk:
            val = val ^ v
        buf.append(f'{val:02x}')
    return ''.join(buf)

def hex_to_bin(s):
    n = int(s, 16)
    return f'{n:0128b}'

def gen_grid(key):
    used = set()
    for y in range(128):
        h = compute_hash(f'{key}-{y}')
        b = hex_to_bin(h)
        for x, bit in enumerate(b):
            if bit == '1':
                used.add((x,y))
    return used

def part1(inp):
    key = inp.strip()
    grid = gen_grid(key)
    return len(grid)


def find_group(start, grid):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        visited.add(node)
        x,y = node
        neighbors = [(x+1, y), (x-1,y), (x,y+1), (x,y-1)]
        for neigh in neighbors:
            if neigh in visited:
                continue
            if neigh not in grid:
                continue
            stack.append(neigh)
    return visited

def part2(inp):
    key = inp.strip()
    grid = gen_grid(key)

    cnt_group = 0
    while grid:
        start = grid.pop()
        group = find_group(start, grid)
        grid -= group
        cnt_group += 1
    return cnt_group
