from pprint import pprint

def parse(inp):
    pipes = dict()
    for line in inp.splitlines():
        src, dst = line.split(' <-> ')
        pipes[src] = dst.split(', ')
    return pipes

def find_group(prog, pipes):
    visited = set()
    stack = [prog]
    while stack:
        prog = stack.pop()
        visited.add(prog)

        for child in pipes[prog]:
            if child in visited:
                continue
            stack.append(child)

    return visited

def part1(inp):
    pipes = parse(inp)
    group = find_group('0', pipes)
    return len(group)


def part2(inp):
    pipes = parse(inp)

    cnt_group = 0
    progs = set(pipes.keys())
    while progs:
        prog = progs.pop()
        group = find_group(prog, pipes)
        progs -= group
        cnt_group += 1
    return cnt_group
