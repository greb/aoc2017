class Node:
    def __init__(self, val):
        self.val = val
        self.nxt = None

    def insert(self, val):
        new_node = Node(val)
        self.nxt, new_node.nxt = new_node, self.nxt
        return new_node


def part1(inp):
    n_steps = int(inp.strip())
    n_rounds = 2017

    node = Node(0)
    node.nxt = node # Make a cycle

    for i in range(n_rounds):
        #spin lock
        for _ in range(n_steps):
            node = node.nxt
        node = node.insert(i+1)
    return node.nxt.val


def part2(inp):
    n_steps = int(inp.strip())
    n_rounds = 50_000_000

    idx = 0
    for t in range(n_rounds):
        idx = (idx+n_steps) % (t+1) + 1
        if idx == 1:
            val = t+1
    return val
