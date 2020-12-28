import re
import functools

from pprint import pprint

def parse(inp):
    nodes = dict()

    for line in inp.splitlines():
        segs = line.split(' -> ')
        node, weight = re.match(r'([a-z]+) \((\d+)\)', segs[0]).groups()
        if len(segs) > 1:
            children = segs[1].split(', ')
        else:
            children = []
        nodes[node] = (int(weight), children)
    return nodes

def find_root(nodes):
    all_children = set()
    for _, children in nodes.values():
        all_children.update(children)

    for node in nodes:
        if node not in all_children:
            return node

def total_weight(node, nodes, cache):
    if node in cache:
        return cache[node]

    weight, children = nodes[node]
    for child in children:
        weight += total_weight(child, nodes, cache)

    cache[node] = weight
    return weight


def fix_weight(node, nodes, delta, cache):
    weight, children = nodes[node]
    child_weights = [total_weight(child, nodes, cache)
            for child in children]

    if len(set(child_weights)) == 1:
        return node, weight + delta

    median = sorted(child_weights)[len(child_weights)//2]
    for child, weight in zip(children, child_weights):
        if weight != median:
            break

    delta = median-weight
    return fix_weight(child, nodes, delta, cache)

def part1(inp):
    nodes = parse(inp)
    return find_root(nodes)

def part2(inp):
    nodes = parse(inp)
    root = find_root(nodes)

    cache = {}
    node, weight = fix_weight(root, nodes, 0, cache)
    return weight
