import re
import collections

def parse(inp):
    pattern = re.compile(r'(.)=<(-?\d+),(-?\d+),(-?\d+)>')
    parts = []
    for line in inp.splitlines():
        components = pattern.findall(line)
        part = [tuple(map(int, vals)) for _, *vals in components]
        parts.append(part)
    return parts

def manhatten_dist(v0, v1):
    return sum(abs(a-b) for a,b in zip(v0, v1))

def part1(inp):
    parts = parse(inp)
    origin = (0,0,0)
    dists = []
    for i, (p,v,a) in enumerate(parts):
        dp = manhatten_dist(origin, p)
        dv = manhatten_dist(origin, v)
        da = manhatten_dist(origin, a)
        dists.append( ((da,dv,dp), i) )
    return min(dists)[1]

def vec_add(v0, v1):
    return tuple(a+b for a,b in zip(v0, v1))

def tick(parts):
    new_parts = {}
    for part, vecs in parts.items():
        p,v,a = vecs
        v = vec_add(v, a)
        p = vec_add(p, v)
        new_parts[part] = (p,v,a)
    return new_parts


def find_collisions(parts):
    keys = list(parts.keys())
    collisions = set()
    for i, a in enumerate(keys):
        for b in keys[i+1:]:
            if parts[a][0] == parts[b][0]:
                collisions.add(a)
                collisions.add(b)
    return collisions

def part2(inp):
    parts = {i:p for i,p in enumerate(parse(inp))}

    n_ticks = 0
    min_ticks = 100
    queue = collections.deque(maxlen=min_ticks)

    while True:
        collisions = find_collisions(parts)
        for c in collisions:
            del parts[c]
        queue.append(len(collisions))
        if n_ticks > min_ticks and sum(queue) == 0:
            break
        parts = tick(parts)
        n_ticks += 1

    return len(parts)
