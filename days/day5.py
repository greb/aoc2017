def part1(inp):
    offsets = [int(o) for o in inp.splitlines()]

    steps = 0
    i = 0
    while 0 <= i < len(offsets):
        offset = offsets[i]
        offsets[i] += 1
        i += offset
        steps += 1
    return steps


def part2(inp):
    offsets = [int(o) for o in inp.splitlines()]

    steps = 0
    i = 0
    while 0 <= i < len(offsets):
        offset = offsets[i]
        if offset >= 3:
            offsets[i] -= 1
        else:
            offsets[i] += 1
        i += offset
        steps += 1
    return steps
