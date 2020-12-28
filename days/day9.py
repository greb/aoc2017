def parse(it):
    it = iter(it)

    token = next_token(it)
    if token == '{':
        return parse_group(it)
    elif token == '<':
        return parse_garbage(it)

def next_token(it):
    token = next(it)
    while token=='!':
        next(it)
        token = next(it)
    return token

def parse_group(it):
    sub = []
    token = next_token(it)
    while token != '}':
        if token == '{':
            sub.append(parse_group(it))
        elif token == ',':
            sub.append(parse(it))
        elif token == '<':
            sub.append(parse_garbage(it))
        token = next_token(it)
    return sub

def parse_garbage(it):
    garbage_buf = []
    token = next_token(it)
    while token != '>':
        garbage_buf.append(token)
        token = next_token(it)
    return ''.join(garbage_buf)

def score(elem, depth=1):
    if not isinstance(elem, list):
        return 0
    val = depth
    for child in elem:
        val += score(child, depth+1)
    return val

def count_garbage(elem):
    if isinstance(elem, str):
        return len(elem)

    count = 0
    for child in elem:
        count += count_garbage(child)
    return count

def part1(inp):
    elem = parse(inp)
    return score(elem)

def part2(inp):
    elem = parse(inp)
    return count_garbage(elem)

import unittest
class Test(unittest.TestCase):
    def test_parse_garbage(self):
        self.assertEqual( parse('<>'), '')
        self.assertEqual( parse('<abc>'), 'abc')
        self.assertEqual( parse('<<<<>'), '<<<')
        self.assertEqual( parse('<{!>}>'), '{}')
        self.assertEqual( parse('<!!>'), '')
        self.assertEqual( parse('<!!!>>'), '')

    def test_parse_group(self):
        self.assertEqual( parse('{}'), [] )
        self.assertEqual( parse('{{{}}}'), [[[]]] )
        self.assertEqual( parse('{{},{}}'), [[],[]] )
        self.assertEqual( parse('{{{},{},{{}}}}'), [[[],[],[[]]]])
        self.assertEqual( parse('{<{},{},{{}}>}'), ['{},{},{{}}'] )
        self.assertEqual( parse('{<a>,<b>,<c>}'), ['a','b','c'] )
        self.assertEqual( parse('{{<a>},{<a>},{<a>}}'), [['a'],['a'],['a']] )
        self.assertEqual( parse('{{<!>},{<!>},{<a>}}'), [['},{<},{<a']] )


    def test_score(self):
        f = lambda x: score(parse(x))
        self.assertEqual( f('{}'), 1 )
        self.assertEqual( f('{{{}}}'), 6)
        self.assertEqual( f('{{},{}}'), 5)
        self.assertEqual( f('{{{},{},{{}}}}'), 16)
        self.assertEqual( f('{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual( f('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        self.assertEqual( f('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual( f('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)

