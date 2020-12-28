def parse(inp):
    rows = []
    for line in inp.splitlines():
        nums = [int(n) for n in line.split()]
        rows.append(nums)
    return rows

def part1(inp):
    rows = parse(inp)
    chk_sum = 0
    for row in rows:
        chk_sum += max(row) - min(row)
    return chk_sum

def check_disibility(row):
    for i, a in enumerate(row):
        for b in row[i+1:]:
            if a % b == 0:
                return a // b
            elif b % a == 0:
                return b // a

def part2(inp):
    rows = parse(inp)

    chk_sum = 0
    for row in rows:
        chk_sum += check_disibility(row)
    return chk_sum


