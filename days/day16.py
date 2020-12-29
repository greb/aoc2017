from collections import deque

def dance(progs, steps):
    progs = deque(progs)
    for step in steps:
        args = step[1:].split('/')
        if step[0] == 's':
            for _ in range(int(args[0])):
                val = progs.pop()
                progs.appendleft(val)
        else:
            if step[0] == 'x':
                a, b = (int(n) for n in args)
            elif step[0] == 'p':
                a, b = (progs.index(n) for n in args)
            progs[a], progs[b] = progs[b], progs[a]
    return ''.join(progs)


def part1(inp):
    steps = inp.strip().split(',')
    progs = 'abcdefghijklmnop'
    return dance(progs, steps)


def part2(inp):
    steps = inp.strip().split(',')
    progs = 'abcdefghijklmnop'

    cnt = 0
    seen = set()
    history = dict()
    while progs not in seen:
        history[cnt] = progs
        seen.add(progs)
        progs = dance(progs, steps)
        cnt += 1

    m = 1_000_000_000 % cnt
    return history[m]
