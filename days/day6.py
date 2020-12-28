def redistribute(blocks):
    new_blocks = list(blocks)
    l = len(blocks)

    n = max(blocks)
    m_idx = blocks.index(n)
    idx = (m_idx + 1) % l
    new_blocks[m_idx] = 0

    while n > 0:
        new_blocks[idx] += 1
        n -= 1
        idx = (idx + 1) % l
    return tuple(new_blocks)


def part1(inp):
    blocks = tuple(int(b) for b in inp.split())

    cnt = 0
    seen = set()
    while blocks not in seen:
        seen.add(blocks)
        blocks = redistribute(blocks)
        cnt += 1
    return cnt


def part2(inp):
    blocks = tuple(int(b) for b in inp.split())

    cnt = 0
    seen = {}
    while blocks not in seen:
        seen[blocks] = cnt
        blocks = redistribute(blocks)
        cnt += 1

    return cnt - seen[blocks]
