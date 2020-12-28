def is_valid(line):
    words = line.split()
    for i, w0 in enumerate(words):
        for w1 in words[i+1:]:
            if w0 == w1:
                return False
    return True

def is_valid2(line):
    words = [sorted(w) for w in line.split()]
    for i, w0 in enumerate(words):
        for w1 in words[i+1:]:
            if w0 == w1:
                return False
    return True


def part1(inp):
    cnt = 0
    for line in inp.splitlines():
        if is_valid(line):
            cnt += 1
    return cnt

def part2(inp):
    cnt = 0
    for line in inp.splitlines():
        if is_valid2(line):
            cnt += 1
    return cnt


import unittest
class Test(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue( is_valid('aa bb cc dd ee') )
        self.assertFalse( is_valid('aa bb cc dd aa') )
        self.assertTrue( is_valid('aa bb cc dd aaa') )

    def test_is_valid2(self):
        self.assertTrue( is_valid2('abcde fghij') )
        self.assertFalse( is_valid2('abcde xyz ecdab') )
        self.assertTrue( is_valid2('a ab abc abd abf abj') )
        self.assertTrue( is_valid2('iiii oiii ooii oooi oooo') )
        self.assertFalse( is_valid2('oiii ioii iioi iiio') )
