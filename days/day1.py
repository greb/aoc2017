def part1(inp):
    captcha = inp.strip()

    total = 0
    for i, c in enumerate(captcha):
        if captcha[i-1] == c:
            total += int(c)
    return total


def part2(inp):
    captcha = inp.strip()
    total = 0
    l = len(captcha)
    for i, c in enumerate(captcha):
        i = (i + l//2) % l
        if captcha[i] == c:
            total += int(c)
    return total

