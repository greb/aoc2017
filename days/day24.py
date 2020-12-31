def parse(inp):
    ports = []
    for line in inp.splitlines():
        t = tuple(int(p) for p in line.split('/'))
        ports.append(t)
    return set(ports)

def iter_chains(s, ports):
    nxt = []
    for a,b in ports:
        if a==s or b==s:
            n = b if a==s else a
            nxt.append((n, (a,b)))

    for n, t in nxt:
        yield [t]
        n_ports = set(ports)
        n_ports.discard(t)
        for chain in iter_chains(n, n_ports):
            yield [t] + chain


def score(chain):
    return sum(a+b for a,b in chain)

def part1(inp):
    ports = parse(inp)
    return max(score(chain) for chain in iter_chains(0, ports))

def part2(inp):
    ports = parse(inp)
    bridges = list(iter_chains(0, ports))

    bridges = sorted(bridges, key=lambda x: len(x), reverse=True)
    length = len(bridges[0])

    max_bridge_score = 0
    for bridge in bridges:
        if len(bridge) < length:
            break
        bridge_score = score(bridge)
        if bridge_score >= max_bridge_score:
            max_bridge_score = bridge_score
    return max_bridge_score
