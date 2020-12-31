import collections

class ExCoP:
    def __init__(self, code):
        self.code = [line.split() for line in code.splitlines()]
        self.pc = 0
        self.regs = dict()
        self.count_mul = 0
        self.status = 'run'

    def get_val(self, src):
        if src.isalpha():
            return self.regs.get(src, 0)
        return int(src)

    def step(self):
        if self.status == 'halt':
            return

        op, *args = self.code[self.pc]
        ops = {
            'set': self.op_set,
            'sub': self.op_sub,
            'mul': self.op_mul,
            'jnz': self.op_jnz
        }

        ret = ops[op](*args)
        if self.pc >= len(self.code):
            self.status = 'halt'

        return ret

    def op_set(self, x, y):
        val_y = self.get_val(y)
        self.regs[x] = val_y
        self.pc += 1

    def op_sub(self, x, y):
        val_x = self.get_val(x)
        val_y = self.get_val(y)
        self.regs[x] = val_x - val_y
        self.pc += 1

    def op_mul(self, x, y):
        val_x = self.get_val(x)
        val_y = self.get_val(y)
        self.regs[x] = val_x * val_y
        self.pc += 1
        self.count_mul += 1

    def op_jnz(self, x, y):
        val_x = self.get_val(x)
        val_y = self.get_val(y)
        if val_x != 0:
            self.pc += val_y
        else:
            self.pc += 1

def part1(inp):
    e = ExCoP(inp)
    while e.status == 'run':
        e.step()
    return e.count_mul

def slow_part2(inp):
    e = ExCoP(inp)
    e.regs['a'] = 1

    while e.status == 'run':
        e.step()
    return self.regs['h']


def part2(inp):
    start = int(inp.splitlines()[0].split()[2])
    start *= 100
    start += 100_000
    end = start + 17_000

    cnt = 0
    for n in range(start, end+1, 17):
        for i in range(2,n):
            if n % i == 0:
                cnt += 1
                break
    return cnt
