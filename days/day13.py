def parse(inp):
    depths = {}
    for line in inp.splitlines():
        layer, depth = [int(v) for v in line.split(': ')]
        depths[layer] = depth
    return depths

def part1(inp):
    depths = parse(inp)

    severity = 0
    n_layers = max(depths) + 1
    for t in range(n_layers):
        if t not in depths:
            continue

        depth = depths[t]
        pos = t % (depth*2 - 2)
        if pos == 0:
            severity += depth * t

    return severity


def part2(inp):
    depths = parse(inp)

    delay = 0
    n_layers = max(depths) + 1

    while True:
        fallthrough = True
        for t in range(n_layers):
            if t not in depths:
                continue

            depth = depths[t]
            pos = (delay+t) % (depth*2 - 2)
            if pos == 0:
                fallthrough = False
                break

        if fallthrough:
            break
        delay += 1
    return delay
