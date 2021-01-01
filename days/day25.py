from pprint import pprint

def parse(inp):
    lines = inp.splitlines()

    rules = {}
    n_steps = int(lines[1].split()[-2])

    for offset in range(3, len(lines), 10):
        name = lines[offset][-2]
        if_false = (
            lines[offset+2][-2] == '1',
            lines[offset+3].split()[-1][0],
            lines[offset+4][-2],
        )
        if_true = (
            lines[offset+6][-2] == '1',
            lines[offset+7].split()[-1][0],
            lines[offset+8][-2]
        )
        rules[name] = if_false, if_true
    return n_steps, rules


def part1(inp):
    n_steps, rules = parse(inp)

    state = 'A'
    tape = set() # Only stores ones
    pos = 0
    for _ in range(n_steps):
        val, direction, state = rules[state][pos in tape]
        if val:
            tape.add(pos)
        else:
            tape.discard(pos)
        if direction == 'r':
            pos += 1
        else:
            pos -= 1
    return len(tape)
