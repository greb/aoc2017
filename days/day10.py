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

def part1(inp):
    lst = list(range(256))
    lengths = [int(l) for l in inp.split(',')]
    twist(lst, lengths)
    return lst[0] * lst[1]

def part2(inp):
    return compute_hash(inp.strip())
